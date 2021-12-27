#!/usr/bin/env python3
# coding: utf-8

from typing import List
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.ensemble import ExtraTreesClassifier, RandomForestClassifier
import joblib
from sklearn.model_selection import cross_val_predict, cross_validate
from sklearn.metrics import confusion_matrix
import sys
import os
from sklearn.model_selection import GridSearchCV

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from mylib import load_csv
from mylib import ml_pipeline_components as pipeline_comps
from mylib import record_model_data as rec
from mylib import load_constants


def main(csv_list: List, consts: load_constants.ML_Consts = None):
    '''
    Parameters
    ----------
    csv_list: array-like
      読み込むCSVファイルのリスト
    consts: load_constants.ML_Consts, default None
      定数が定義されたML_Consts Classのインスタンス

    Returns
    -------
    '''
    ####################
    ### データ読み込み ###
    ####################
    # 定数の読み込み(引数で指定されていない場合)
    if consts == None:
        consts = load_constants.ML_Consts()

    # CSVを読み込む
    df = load_csv.CsvToDf(csv_list, consts.CSV_PATH)
    # 訓練データとテストデータを分ける(式を評価するengineとしてnumexprを使用することで、処理の高速化を狙う。)
    # train_set = df.query('session_id == "trial1"', engine='numexpr')
    # test_set = df.query('session_id == "trial2"', engine='numexpr')
    train_set = df[df['session_id'].isin(consts.TRAIN_SET_SESSION)]
    test_set = df[df['session_id'].isin(consts.TEST_SET_SESSION)]

    print('[Complete] データの読み込み')

    #########################
    ### データのクリーニング ###
    #########################
    # 特徴量抽出パイプライン
    features_pipeline = Pipeline([
        ('selector', pipeline_comps.DataFrameSelector(consts.FEATURE_ATTRBS)),
        ('imputer', SimpleImputer(strategy="median"))
    ])
    X_train = features_pipeline.fit_transform(train_set)
    X_test = features_pipeline.fit_transform(test_set)

    # ラベル抽出パイプライン
    label_pipeline = Pipeline([
        ('selector', pipeline_comps.DataFrameSelector(consts.LABEL_ATTRB)),
        ('transducer', pipeline_comps.ValueTransducer(consts.FACING_DOV_ANGLES))
    ])
    y_train = label_pipeline.fit_transform(train_set)
    y_test = label_pipeline.fit_transform(test_set)

    print('[Complete] データのクリーニング')

    ###########
    ### 訓練 ###
    ###########
    # Extra-Trees推定器
    # グリッドサーチ
    estimator = ExtraTreesClassifier()
    hyper_params_search = GridSearchCV(estimator=estimator, param_grid=consts.PARAM_GRID, scoring=consts.SCORING,
                                       n_jobs=-1, refit=consts.REFIT_SCORING, cv=consts.NCV, return_train_score=False)
    hyper_params_search.fit(X_train, y_train)

    print('[Complete] 訓練')

    ###########
    ### 検証 ###
    ###########
    best_estimator = hyper_params_search.best_estimator_

    # Accuracy, Balanced Accuracy, F1 Score
    scores = cross_validate(best_estimator, X_test, y_test,
                            scoring=consts.SCORING, cv=consts.NCV, n_jobs=-1)

    # Confusion Matrix
    y_test_pred = cross_val_predict(
        best_estimator, X_test, y_test, cv=consts.NCV, n_jobs=-1)
    conf_mat = confusion_matrix(y_test, y_test_pred)

    print('[Complete] 検証')

    ################
    ### 結果の出力 ###
    ################
    # 実行中のスクリプトの名前を取得
    fname = os.path.splitext(os.path.basename(__file__))[0]

    record_md = rec.RecModelDataToMarkdown(fname=fname, consts=consts, csv_list=csv_list,
                                           estimator=estimator, best_estimator=best_estimator, scores=scores, conf_mat=conf_mat)
    record_md.write()


if __name__ == '__main__':
    if len(sys.argv) > 1:
        filename = sys.argv[1]

        csv_list = []
        for i in range(1, len(sys.argv)):
            csv_list.append(sys.argv[i])

        # 定数の定義
        param_grid = [
            {'n_estimators': [10, 100, 1000], 'min_samples_split': [2, 5, 10], 'min_samples_leaf': [1, 5, 10], 'max_features': [
                'sqrt', 'log2', None], 'bootstrap': [False], 'n_jobs': [-1], 'random_state': [42], 'max_samples': [0.01, 0.5, 0.09]},
            {'n_estimators': [10, 100, 1000], 'min_samples_split': [2, 5, 10], 'min_samples_leaf': [1, 5, 10], 'max_features': [
                'sqrt', 'log2', None], 'bootstrap': [True], 'oob_score': [True, False], 'n_jobs': [-1], 'random_state': [42], 'max_samples': [0.01, 0.5, 0.09]}
            # {'n_estimators': [100, 300, 500, 800, 1000, 1300, 1500], 'min_samples_split': [2, 5, 10], 'min_samples_leaf': [1, 5, 10], 'max_features': ['sqrt', 'log2', None], 'bootstrap': [False], 'n_jobs': [-1], 'random_state': [42], 'max_samples': [0.01, 0.5, 0.09]},
        ]
        csv_path = '../out/csv/experiment'
        label_attrb = ['dov_angle']
        facing_dov_angles = [0, 45, 315]
        ncv = 8
        train_set_session = ['trial1']
        test_set_session = ['trial2', 'trial3']
        consts = load_constants.ML_Consts(param_grid=param_grid, csv_path=csv_path, label_attrb=label_attrb,
                                          facing_dov_angles=facing_dov_angles, ncv=ncv, train_set_session=train_set_session, test_set_session=test_set_session)

        main(csv_list, consts=consts)
    else:
        print("You need to specify the CSV file to be loaded.", file=sys.stderr)
        sys.exit(1)
