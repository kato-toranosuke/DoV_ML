#!/usr/bin/env python3
# coding: utf-8

from typing import List
import sys
import os
import numpy as np
import pprint
from imblearn.pipeline import Pipeline as ImbPipeline
from imblearn.under_sampling import RandomUnderSampler, ClusterCentroids
from imblearn.over_sampling import RandomOverSampler, SMOTE
from imblearn.combine import SMOTEENN, SMOTETomek
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.model_selection import cross_val_predict, cross_validate
from sklearn.metrics import confusion_matrix, f1_score, accuracy_score, recall_score, precision_score, multilabel_confusion_matrix
from sklearn.pipeline import Pipeline
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import train_test_split

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from mylib import load_csv
from mylib import ml_pipeline_components as pipeline_comps
from mylib import record_model_data as rec
from mylib import load_constants
from mylib.elect import select_robot, select_robot_45

def main(csv_filename_list: List, estimator, resampler, consts: load_constants.Eval_Sys_Consts = None, n_robot=5):
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
    #################
    ### CSV -> DF ###
    #################
    # 定数の読み込み(引数で指定されていない場合)
    if consts == None:
        consts = load_constants.ML_Consts()

    # CSVを読み込む
    df = load_csv.CsvToDf(csv_filename_list, consts.CSV_PATH)
    print("データ読み込み完了")

    ###############################
    ### Hyper-Parameter Tuning  ###
    ###############################
    # hp tuningに使用するデータを抽出する
    hp_set = df[(df['session_id'].isin(consts.HP_SET_SESSION)) & (
        df['agc_status'].isin(consts.AGC_STATUS)) & (df['distance'].isin(consts.DISTANCE))]

    # 特徴量とラベルを分離
    pl = pipeline_comps.MlPipeline(consts)
    X_hp = pl.pick_features_pipeline.fit_transform(hp_set)
    y_hp = pl.pick_label_pipeline.fit_transform(hp_set)

    # Pipeline
    if resampler != None:
        hp_pipeline = ImbPipeline(
            steps=[('resmp', resampler), ('est', estimator)])
    else:
        hp_pipeline = Pipeline(steps=[('est', estimator)])

    # グリッドサーチ
    search = GridSearchCV(estimator=hp_pipeline, param_grid=consts.PARAM_GRID, scoring=consts.SCORING,
                          n_jobs=-1, refit=consts.REFIT_SCORING, cv=consts.NCV, return_train_score=False)
    search.fit(X_hp, y_hp)
    print('Hyper-Parameter Tuning 完了')

    #######################
    ### Training & Test ###
    #######################
    train_test_set_session = ['trial' + str(i) for i in range(1, 26)]
    train_test_set_session = [
        i for i in train_test_set_session if not i in consts.HP_SET_SESSION]

    result = {'accuracy': [], 'f1': [], 'precision': [],
              'recall': [], 'confusion_matrix': [], 'facing_probas': []}
    results = [result for i in range(n_robot + 1)]
    for k in range(consts.NCV):
        print('--------------')
        print(f'[{k+1}/{consts.NCV}] Training & Test')
        # train_set_session と test_set_sessionに分離
        train_set_session, test_set_session = train_test_split(
            train_test_set_session, train_size=3)

        # training, testに使用するデータを抽出する
        train_set = df[(df['session_id'].isin(train_set_session)) & (
            df['agc_status'].isin(consts.AGC_STATUS)) & (df['distance'].isin(consts.DISTANCE))]
        test_set = df[(df['session_id'].isin(test_set_session)) & (
            df['agc_status'].isin(consts.AGC_STATUS)) & (df['distance'].isin(consts.DISTANCE))]

        # [Training]
        # 特徴量とラベルを分離
        X_train_ = pl.pick_features_pipeline.fit_transform(train_set)
        y_train_ = pl.pick_label_pipeline.fit_transform(train_set)

        # resamplerの設定 & データのリサンプリング
        if resampler != None:
            best_resampler = search.best_estimator_['resmp']
            X_train, y_train = best_resampler.fit_resample(X_train_, y_train_)
        else:
            best_resampler = pipeline_comps.NoResampler()
            X_train = X_train_
            y_train = y_train_

        # training
        best_estimator = search.best_estimator_['est']
        fitted_model = best_estimator.fit(X_train, y_train)

        # fitted_model = ExtraTreesClassifier(random_state=42)
        # fitted_model.fit(X_train_, y_train_)

        # [Test]
        # 正解ラベルを作成する
        X_test = []
        for d in consts.DISTANCE:
            for angle in range(0, 181, 45):
                for session in test_set_session:
                    # 5台分をまとめた辞書型
                    X = {'distance': d, 'angle': angle,
                         'robot_data': [], 'label': int(angle / 45) + 1}
                    for robot_id in range(1, 6):
                        robot_item = {'robot_id': robot_id}
                        robot_df = test_set[(test_set['session_id'] == session) & (
                            test_set['angle'] == angle) & (test_set['distance'] == d) & (test_set['participant_id'] == 'raspi-ubuntu-' + str(robot_id))]
                        if len(robot_df) == 0:
                            continue
                        X_robot = pl.pick_features_pipeline.fit_transform(
                            robot_df)
                        robot_item['features'] = X_robot
                        X['robot_data'].append(robot_item)

                    if len(X['robot_data']) == 0:
                        continue
                    X_test.append(X)

        for X in X_test:
            # classとprobaの計算
            predicted_results = []
            for i in range(n_robot):
                feature_vals = [j['features']
                                for j in X['robot_data'] if j['robot_id'] == i + 1][0]
                predicted_result = fitted_model.predict(feature_vals)
                predicted_class = predicted_result[0]
                proba_result = fitted_model.predict_proba(feature_vals)
                proba = proba_result[0][predicted_class]
                probas = proba_result[0]

                # 後の評価のため
                X['robot_data'][i]['predicted_class'] = predicted_class
                X['robot_data'][i]['proba'] = proba
                X['robot_data'][i]['probas'] = probas

                # 選定器に渡すため
                predicted_results.append(
                    {'robot_id': i + 1, 'predicted_class': predicted_class, 'proba': proba, 'probas': probas})

            # elect
            if consts.LABEL_ATTRB[0] == 'facing':
                # 0angle
                elected_result = select_robot(predicted_results, 'proba')
            elif consts.LABEL_ATTRB[0] == 'facing2':
                # 45angle
                elected_result = select_robot_45(predicted_results, 'proba')
            X['label_pred'] = elected_result['robot_id']

        ##################
        ### Evaluation ###
        ##################
        # Robot1~5毎の単体精度
        for i in range(n_robot):
            target_angle = 45 * i

            X_test_target = [X for X in X_test if (
                X['distance'] in consts.DISTANCE and X['angle'] == target_angle)]

            y_true = [X.get('label') for X in X_test_target]
            y_pred = [X.get('label_pred') for X in X_test_target]
            robot_probas = []
            for j in range(n_robot):
                # robot毎のfacing probaを算出
                facing_probas = [X['robot_data'][j]['probas'][1]
                                 for X in X_test_target]
                mean_facing_proba = np.mean(facing_probas)
                robot_probas.append(mean_facing_proba)

            sys_accuracy = accuracy_score(y_true, y_pred)
            sys_f1 = f1_score(y_true, y_pred, average='micro')
            sys_precision = precision_score(y_true, y_pred, average='micro')
            sys_recall = recall_score(y_true, y_pred, average='micro')
            y_true_bin = [1] * len(y_true)
            y_pred_bin = [1 if y_pred[i] == y_true[i]
                          else 0 for i in range(len(y_true))]
            sys_conf_mat = confusion_matrix(y_true_bin, y_pred_bin)

            results[i]['accuracy'].append(sys_accuracy)
            results[i]['f1'].append(sys_f1)
            results[i]['precision'].append(sys_precision)
            results[i]['recall'].append(sys_recall)
            results[i]['confusion_matrix'].append(sys_conf_mat)
            results[i]['facing_probas'].append(robot_probas)

        # トータル精度
        y_true = [X.get('label') for X in X_test]
        y_pred = [X.get('label_pred') for X in X_test]

        sys_accuracy = accuracy_score(y_true, y_pred)
        sys_f1 = f1_score(y_true, y_pred, average='micro')
        sys_precision = precision_score(y_true, y_pred, average='micro')
        sys_recall = recall_score(y_true, y_pred, average='micro')
        y_true_bin = [1] * len(y_true)
        y_pred_bin = [1 if y_pred[i] == y_true[i]
                      else 0 for i in range(len(y_true))]
        sys_conf_mat = confusion_matrix(y_true_bin, y_pred_bin)

        results[n_robot]['accuracy'].append(sys_accuracy)
        results[n_robot]['f1'].append(sys_f1)
        results[n_robot]['precision'].append(sys_precision)
        results[n_robot]['recall'].append(sys_recall)
        results[n_robot]['confusion_matrix'].append(sys_conf_mat)
        results[n_robot]['facing_probas'] = [-100]

    ################
    ### 結果の出力 ###
    ################
    record = rec.RecModelDataToMdEvalSys(
        consts, csv_list, best_resampler, best_estimator, results)
    record.write()

def ml_main(csv_list, consts):
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


if __name__ == '__main__':
    csv_list = ['2021-12-27_AGC.csv', '2022-01-10_NoAGC.csv',
                '2022-01-13_raspi_48000Hz_w1_N2^12_overlap80.csv']
    # 定数の設定
    # 探索パラメータ
    # range(100, 1600, 100) 使える
    # param_grid = [
    #     {'est__n_estimators': range(10, 1000, 25), 'est__min_samples_split': [2, 5, 10], 'est__min_samples_leaf': [1, 5, 10], 'est__max_features': [
    #         'sqrt', 'log2', None], 'est__bootstrap': [False], 'est__n_jobs': [-1], 'est__random_state': [42], 'est__max_samples': [0.01, 0.5, 0.09]},
    # ]
    param_grid = [
        {'est__n_estimators': range(50, 1001, 50), 'est__min_samples_split': [2, 5, 10], 'est__min_samples_leaf': [1, 5, 10], 'est__max_features': [
            'sqrt', 'log2', None], 'est__bootstrap': [False], 'est__n_jobs': [-1], 'est__random_state': [42], 'est__max_samples': [0.01, 0.5, 0.09]},
        {'est__n_estimators': range(50, 1001, 50), 'est__min_samples_split': [2, 5, 10], 'est__min_samples_leaf': [1, 5, 10], 'est__max_features': [
            'sqrt', 'log2', None], 'est__bootstrap': [True], 'est__oob_score': [True, False], 'est__n_jobs': [-1], 'est__random_state': [42], 'est__max_samples': [0.01, 0.5, 0.09]}
    ]

    ############################
    ### Searching Parameters ###
    ############################
    label_attrbs = [['facing'], ['facing2']]
    facing_dov_angles = [[1], [1, 2]]
    angles = ['0', '45']

    agc_statuses = [['AGC'], ['NoAGC']]

    distances = [[1], [3], [5], [1, 3, 5]]
    distances_name = ['1m', '3m', '5m', 'under5m']

    for i, label_attrb in enumerate(label_attrbs):
        for agc_status in agc_statuses:
            for j, distance in enumerate(distances):
                output_path = '../out/experiment_result/data_of_2022-01-13_eval_system/' + \
                    agc_status[0] + '-' + angles[i] + \
                    'angle-' + distances_name[j]
                os.makedirs(output_path, exist_ok=True)

                hp_set_session = ['trial1', 'trial21']
                consts = load_constants.Eval_Sys_Consts(param_grid=param_grid, label_attrb=label_attrb, facing_dov_angles=facing_dov_angles[i], csv_path='../out/csv/experiment', ncv=8,
                                                        hp_set_session=hp_set_session, test_set_session=None, train_set_session=None, output_path=output_path, distance=distance, agc_status=agc_status)

                ml_main(csv_list, consts)