#!/usr/bin/env python3
# coding: utf-8

from typing import List
from sklearn.ensemble import ExtraTreesClassifier, RandomForestClassifier
from sklearn.model_selection import cross_val_predict, cross_validate
from sklearn.metrics import confusion_matrix
import sys
import os
from sklearn.model_selection import GridSearchCV
from imblearn.pipeline import Pipeline as ImbPipeline
from imblearn.under_sampling import RandomUnderSampler, ClusterCentroids
from imblearn.over_sampling import RandomOverSampler, SMOTE
from imblearn.combine import SMOTEENN, SMOTETomek
from sklearn.pipeline import Pipeline
import pprint

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from mylib import load_csv
from mylib import ml_pipeline_components as pipeline_comps
from mylib import record_model_data as rec
from mylib import load_constants


def main(csv_filename_list: List, estimator, resampler, consts: load_constants.ML_Consts = None):
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
    df = load_csv.CsvToDf(csv_filename_list, consts.CSV_PATH)
    # 訓練データとテストデータを分ける(式を評価するengineとしてnumexprを使用することで、処理の高速化を狙う。)
    # train_set = df.query('session_id == "trial1"', engine='numexpr')
    # test_set = df.query('session_id == "trial2"', engine='numexpr')
    # train_set = df[df['session_id'].isin(consts.TRAIN_SET_SESSION)]
    # test_set = df[df['session_id'].isin(consts.TEST_SET_SESSION)]
    train_set = df[(df['session_id'].isin(consts.TRAIN_SET_SESSION)) & (
        df['agc_status'] == 'AGC') & (df['distance'] <= 3)]
    test_set = df[(df['session_id'].isin(consts.TEST_SET_SESSION))
                  & (df['agc_status'] == 'AGC') & (df['distance'] <= 3)]

    print("データ読み込み完了")

    #########################
    ### データのクリーニング ###
    #########################
    pl = pipeline_comps.MlPipeline(consts)
    # 特徴量抽出パイプライン
    X_train = pl.pick_features_pipeline.fit_transform(train_set)
    X_test = pl.pick_features_pipeline.fit_transform(test_set)
    # ラベル抽出パイプライン
    y_train = pl.pick_label_pipeline.fit_transform(train_set)
    y_test = pl.pick_label_pipeline.fit_transform(test_set)

    print('データのクリーニング完了')

    ###########
    ### 訓練 ###
    ###########
    # パイプライン
    if resampler != None:
        train_pipeline = ImbPipeline(
            steps=[('resmp', resampler), ('est', estimator)])
    else:
        train_pipeline = Pipeline(steps=[('est', estimator)])

    # グリッドサーチ
    search = GridSearchCV(estimator=train_pipeline, param_grid=consts.PARAM_GRID, scoring=consts.SCORING,
                          n_jobs=-1, refit=consts.REFIT_SCORING, cv=consts.NCV, return_train_score=False, verbose=2)
    search.fit(X_train, y_train)
    print('訓練完了')

    ###########
    ### 検証 ###
    ###########
    # resamplerの設定
    if resampler != None:
        best_resampler = search.best_estimator_['resmp']
    else:
        best_resampler = pipeline_comps.NoResampler()

    best_estimator = search.best_estimator_['est']

    # パイプライン
    if resampler != None:
        test_pipeline = ImbPipeline(
            steps=[('resmp', best_resampler), ('est', best_estimator)])
    else:
        test_pipeline = Pipeline(steps=[('est', best_estimator)])

    # Accuracy, Balanced Accuracy, F1 Score
    scores = cross_validate(test_pipeline, X_test, y_test,
                            scoring=consts.SCORING, cv=consts.NCV, n_jobs=-1)

    # Confusion Matrix
    y_test_pred = cross_val_predict(
        test_pipeline, X_test, y_test, cv=consts.NCV, n_jobs=-1)
    conf_mat = confusion_matrix(y_test, y_test_pred)

    print('検証完了')

    ################
    ### 結果の出力 ###
    ################
    record = rec.RecModelDataToMdWithResampler(
        consts, csv_list, best_resampler, best_estimator, scores, conf_mat)
    record.write()


if __name__ == '__main__':
    if len(sys.argv) > 1:
        csv_list = []
        for i in range(1, len(sys.argv)):
            csv_list.append(sys.argv[i])

        # 定数の設定
        # 探索パラメータ
        param_grid = [
            {'est__n_estimators': [50, 100, 150, 200, 300], 'est__min_samples_split': [2, 5, 10], 'est__min_samples_leaf': [1, 5, 10], 'est__max_features': [
                'sqrt', 'log2', None], 'est__bootstrap': [False], 'est__n_jobs': [-1], 'est__random_state': [42], 'est__max_samples': [0.01, 0.5, 0.09]},
            {'est__n_estimators': [50, 100, 150, 200, 300], 'est__min_samples_split': [2, 5, 10], 'est__min_samples_leaf': [1, 5, 10], 'est__max_features': [
                'sqrt', 'log2', None], 'est__bootstrap': [True], 'est__oob_score': [True, False], 'est__n_jobs': [-1], 'est__random_state': [42], 'est__max_samples': [0.01, 0.5, 0.09]}
        ]
        # param_grid = [
        #     {'est__n_estimators': range(100, 1600, 100), 'est__min_samples_split': [2, 5, 10], 'est__min_samples_leaf': [1, 5, 10], 'est__max_features': [
        #         'sqrt', 'log2', None], 'est__bootstrap': [False], 'est__n_jobs': [-1], 'est__random_state': [42], 'est__max_samples': [0.01, 0.5, 0.09]},
        #     {'est__n_estimators': range(100, 1600, 100), 'est__min_samples_split': [2, 5, 10], 'est__min_samples_leaf': [1, 5, 10], 'est__max_features': [
        #         'sqrt', 'log2', None], 'est__bootstrap': [True], 'est__oob_score': [True, False], 'est__n_jobs': [-1], 'est__random_state': [42], 'est__max_samples': [0.01, 0.5, 0.09]}
        # ]
        # param_grid = [
        #   {'est__n_estimators': range(10, 30, 10), 'est__min_samples_split': [2], 'est__min_samples_leaf': [5], 'est__max_features': [
        #       None], 'est__bootstrap': [False], 'est__n_jobs': [-1], 'est__random_state': [42], 'est__max_samples': [0.5]}
        # ]

        # 特徴量(最大値・最小値を除外)
        # feature_attrbs_no_max_min = ['low_power', 'high_power', 'hlbr', 'coe1[0]', 'coe1[1]', 'coe3[0]', 'coe3[1]', 'coe3[2]', 'coe3[3]', 'ratio_max_to_10ms_ave_peaks', 'ratio_max_to_9th_ave_peaks', 'ac_std', 'ac_auc', 'diff_std',
        #                              'diff_auc', 'srmr', 'gp_max_val_std', 'gp_max_val_range', 'gp_max_val_mean', 'gp_max_ix_std', 'gp_max_ix_range', 'gp_max_ix_mean', 'gp_auc_std', 'gp_auc_range', 'gp_auc_mean', 'tdoa_std', 'tdoa_range', 'tdoa_mean']
        # 定数の設定（最大値・最小値を無視する場合）
        # consts = load_constants.ML_Consts(
        #     param_grid=param_grid, feature_attrbs=feature_attrbs_no_max_min)

        ####################################
        ### (0, 45, 315)をfacingとする場合 ###
        ####################################
        # # train-> trial2 / test-> trial1,3
        # estimator = ExtraTreesClassifier()
        # resampler = None
        # # 定数の設定（実験データで学習する場合）
        # consts = load_constants.ML_Consts(
        #     param_grid=param_grid, facing_dov_angles=[0, 45, 315], csv_path='../out/csv/experiment', ncv=8, train_set_session=['trial2'], test_set_session=['trial1', 'trial3'], output_path='../out/experiment_result')
        # main(csv_list, estimator, resampler, consts)

        # # train-> trial3 / test-> trial1,2
        # estimator = ExtraTreesClassifier()
        # resampler = None
        # # 定数の設定（実験データで学習する場合）
        # consts = load_constants.ML_Consts(
        #     param_grid=param_grid, facing_dov_angles=[0, 45, 315], csv_path='../out/csv/experiment', ncv=8, train_set_session=['trial3'], test_set_session=['trial1', 'trial2'], output_path='../out/experiment_result')
        # main(csv_list, estimator, resampler, consts)

        #############################
        ### 0のみをfacingとする場合 ###
        #############################
        consts = load_constants.ML_Consts(
            param_grid=param_grid, label_attrb=['facing'], facing_dov_angles=[1], csv_path='../out/csv/experiment', ncv=8, train_set_session=['trial1', 'trial2'], test_set_session=['trial3', 'trial4', 'trial5'], output_path='../out/experiment_result/mbp2019')

        # No resampler
        estimator = ExtraTreesClassifier()
        resampler = None
        main(csv_list, estimator, resampler, consts)

        # ClusterCentroids
        estimator = ExtraTreesClassifier()
        resampler = ClusterCentroids(random_state=42)
        main(csv_list, estimator, resampler, consts)

        # RandomUnderSampler
        estimator = ExtraTreesClassifier()
        resampler = RandomUnderSampler(random_state=42)
        main(csv_list, estimator, resampler, consts)

        # RandomOverSampler
        estimator = ExtraTreesClassifier()
        resampler = RandomOverSampler(random_state=42)
        main(csv_list, estimator, resampler, consts)

        # SMOTE
        estimator = ExtraTreesClassifier()
        resampler = SMOTE(random_state=42, n_jobs=-1)
        main(csv_list, estimator, resampler, consts)

        # SMOTEENN
        estimator = ExtraTreesClassifier()
        resampler = SMOTEENN(random_state=42, n_jobs=-1)
        main(csv_list, estimator, resampler, consts)

        # SMOTETomek
        estimator = ExtraTreesClassifier()
        resampler = SMOTETomek(random_state=42, n_jobs=-1)
        main(csv_list, estimator, resampler, consts)

        # # trial-rf-1
        # estimator = RandomForestClassifier()
        # resampler = ClusterCentroids(random_state=42)
        # main(csv_list, estimator, resampler, consts)

        # # trial-rf-2
        # estimator = RandomForestClassifier()
        # resampler = RandomUnderSampler(random_state=42)
        # main(csv_list, estimator, resampler, consts)

        # # trial-rf-3
        # estimator = RandomForestClassifier()
        # resampler = RandomOverSampler(random_state=42)
        # main(csv_list, estimator, resampler, consts)

        # # trial-rf-4
        # estimator = RandomForestClassifier()
        # resampler = SMOTE(random_state=42, n_jobs=-1)
        # main(csv_list, estimator, resampler, consts)

        # # trial-exf-0
        # estimator = ExtraTreesClassifier()
        # resampler = None
        # main(csv_list, estimator, resampler, consts)

        # # trial-exf-1
        # estimator = ExtraTreesClassifier()
        # resampler = ClusterCentroids(random_state=42)
        # main(csv_list, estimator, resampler, consts)

        # # trial-exf-2
        # estimator = ExtraTreesClassifier()
        # resampler = RandomUnderSampler(random_state=42)
        # main(csv_list, estimator, resampler, consts)

        # # trial-exf-3
        # estimator = ExtraTreesClassifier()
        # resampler = RandomOverSampler(random_state=42)
        # main(csv_list, estimator, resampler, consts)

        # # trial-exf-4
        # estimator = ExtraTreesClassifier()
        # resampler = SMOTE(random_state=42, n_jobs=-1)
        # main(csv_list, estimator, resampler, consts)

    else:
        print("You need to specify the CSV file to be loaded.", file=sys.stderr)
        sys.exit(1)
