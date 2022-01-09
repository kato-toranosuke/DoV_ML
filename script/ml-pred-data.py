#!/usr/bin/env python3
# coding: utf-8

import joblib
import sys
import os
from typing import List
import argparse
from export_csv_mono_ch import createWav2Csv
from sklearn.metrics import accuracy_score, balanced_accuracy_score, f1_score, confusion_matrix
from sklearn.model_selection import cross_val_predict, cross_validate

from imblearn.under_sampling import RandomUnderSampler, ClusterCentroids
from imblearn.over_sampling import RandomOverSampler, SMOTE
from imblearn.combine import SMOTEENN, SMOTETomek

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from mylib.load_constants import Exp_Consts
from mylib.load_csv import CsvToDf
from mylib.ml_pipeline_components import MlPipeline
from mylib.record_model_data import RecExpResultToMarkdown
from mylib import record_model_data as rec

class MlPred():
    def __init__(self, exp_consts: Exp_Consts, train_filename_list: List = None, test_filename_list: List = None, input_pkl_filename: str = None, output_pkl_filename: str = None, csv_filename: str = None) -> None:
        self.consts = exp_consts
        self.train_filename_list = train_filename_list
        self.test_filename_list = test_filename_list
        self.input_pkl_filename = input_pkl_filename
        self.output_pkl_filename = output_pkl_filename
        self.csv_filename = csv_filename

    def wav2csv(self, csv_filename=None, dataset_path=None, test_csv_path=None, w=1, N=2**12, overlap=80):
        '''
        Parameters
        ----------
        csv_filename: str
            出力するCSVファイルの名前
        dataset_path: str
            読み込むwavファイルのディレクトリパス
        test_csv_path: str
            CSVの出力先ディレクトリ
        '''
        if csv_filename == None:
            csv_filename = self.csv_filename
        if dataset_path == None:
            dataset_path = self.consts.DATASET_PATH
        if test_csv_path == None:
            test_csv_path = self.consts.TEST_CSV_PATH

        # wav -> csv
        createWav2Csv(csv_filename, dataset_path, test_csv_path, w, N, overlap)

    def fit(self, resampler=None, train_filename_list: List = None, train_csv_path: str = None, train_set_trial: List = None, input_pkl_filename: str = None, output_pkl_filename: str = None):
        '''
        hyper-parameters tuning済みのモデルを入力し、fittingさせたモデルを出力。

        Parameters
        ----------
        train_filename_list: array-like, default None
            fit時に使用するデータが保存されているCSV
        train_csv_path: str, default None
            fit時に使用するCSVが格納されているディレクトリへのパス
        train_set_trial: array-like, default None
            使用するデータのsession番号のリスト
        input_pkl_filename: str, default None
            hyper-parameters tuning済みのモデルが保存されているpklファイルの名前
        output_pkl_filename: str, default None
            fit済みのモデルを保存するpklファイルの名前
        '''

        # [training data] csv -> DataFrame
        if train_filename_list == None:
            train_filename_list = self.train_filename_list
        if train_csv_path == None:
            train_csv_path = self.consts.TRAIN_CSV_PATH
        df_train = CsvToDf(train_filename_list, train_csv_path)

        # trainingに使用するsessionの抽出
        if train_set_trial != None:
            train_set = df_train[df_train['session_id'].isin(train_set_trial)]
        else:
            train_set = df_train

        print("CSV->DataFrameへの変換完了")

        # 特徴量とラベルの分離
        pl = MlPipeline(self.consts)
        _X = pl.pick_features_pipeline.fit_transform(train_set)
        _y = pl.pick_label_pipeline.fit_transform(train_set)
        print('特徴量とラベルの分離完了')

        # 学習データのリサンプリング
        if resampler == None:
            X_train = _X
            y_train = _y
        else:
            X_train, y_train = resampler.fit_resample(_X, _y)

        print("X_train: %d, y_train: %d" % (len(X_train), len(y_train)))

        # 学習
        if input_pkl_filename == None:
            input_pkl_filename = self.input_pkl_filename
        input_pkl_filepath = self.consts.INPUT_PKL_PATH + '/' + \
            input_pkl_filename + '/' + input_pkl_filename + '.pkl'
        model = joblib.load(input_pkl_filepath)
        model.fit(X_train, y_train)
        print('学習完了')

        # fittingした結果をpklへ保存する
        os.makedirs(self.consts.OUTPUT_PKL_PATH, exist_ok=True)
        if output_pkl_filename == None:
            output_pkl_filename = self.output_pkl_filename
        output_pkl_filepath = self.consts.OUTPUT_PKL_PATH + '/' + output_pkl_filename
        joblib.dump(model, output_pkl_filepath)
        print(f'pklへの出力: {output_pkl_filepath}\n')

    def fit_predict(self, test_filename_list: List = None, test_csv_path: str = None, test_set_trial: List = None, input_pkl_filename: str = None):
        '''
        hyper-parameters tuning済みのモデルを入力し、cross validationした結果を出力。

        Parameters
        ----------
        test_filename_list: array-like, default None
            cross validation時に使用するデータが保存されているCSVのリスト
        test_csv_path: str, default None
            cross validation時に使用するCSVが格納されているディレクトリへのパス
        test_set_trial: array-like, default None
            使用するデータのsession番号のリスト
        input_pkl_filename: str, default None
            hyper-parameters tuning済みのモデルが保存されているpklファイルの名前
        '''

        # [test data] csv -> DataFrame
        if test_filename_list == None:
            test_filename_list = self.test_filename_list
        if test_csv_path == None:
            test_csv_path = self.consts.TEST_CSV_PATH
        df_test = CsvToDf(test_filename_list, test_csv_path)

        # testに使用するsessionの抽出
        if test_set_trial != None:
            test_set = df_test[df_test['session_id'].isin(test_set_trial)]
        else:
            test_set = df_test

        print("CSV->DataFrameへの変換完了")

        # 特徴量とラベルの分離
        pl = MlPipeline(self.consts)
        X_test = pl.pick_features_pipeline.fit_transform(test_set)
        y_test = pl.pick_label_pipeline.fit_transform(test_set)
        print('特徴量とラベルの分離完了')

        # モデルの読み込み
        if input_pkl_filename == None:
            # fitしてないpklファイルを使用
            input_pkl_filename = self.input_pkl_filename
        input_pkl_filepath = self.consts.INPUT_PKL_PATH + '/' + \
            input_pkl_filename + '/' + input_pkl_filename + '.pkl'
        model = joblib.load(input_pkl_filepath)
        print(f'ハイパーパラメータ調整済みのモデルを読み込む: {input_pkl_filepath}')

        # Accuracy, Balanced Accuracy, F1 Score
        scores = cross_validate(model, X_test, y_test,
                                scoring=self.consts.SCORING, cv=self.consts.NCV, n_jobs=-1)
        print(scores)
        # Confusion Matrix
        y_test_pred = cross_val_predict(
            model, X_test, y_test, cv=self.consts.NCV, n_jobs=-1)
        conf_mat = confusion_matrix(y_test, y_test_pred)
        print(conf_mat)

        print('検証完了')

        # 結果の出力
        record = rec.RecModelDataToMdWithResampler(
            self.consts, test_filename_list, None, model, scores, conf_mat)
        record.write()

    def predict(self, test_filename_list: List = None, test_csv_path: str = None, test_set_trial: List = None, input_pkl_filename: str = None):
        '''
        fit済みのモデルを入力し、評価結果を出力する。

        Parameters
        ----------
        test_filename_list: array-like, default None
            predict時に使用するデータが保存されているCSVのリスト
        test_csv_path: str, default None
            predict時に使用するCSVが格納されているディレクトリへのパス
        test_set_trial: array-like, default None
            使用するデータのsession番号のリスト
        input_pkl_filename: str, default None
            hyper-parameters tuning済みのモデルが保存されているpklファイルの名前
        '''

        # [test data] csv -> DataFrame
        if test_filename_list == None:
            test_filename_list = self.test_filename_list
        if test_csv_path == None:
            test_csv_path = self.consts.TEST_CSV_PATH
        df_test = CsvToDf(test_filename_list, test_csv_path)

        # testに使用するsessionの抽出
        if test_set_trial != None:
            test_set = df_test[df_test['session_id'].isin(test_set_trial)]
        else:
            test_set = df_test

        print("CSV->DataFrameへの変換完了")

        # 特徴量とラベルの分離
        pl = MlPipeline(self.consts)
        X_test = pl.pick_features_pipeline.fit_transform(test_set)
        y_test = pl.pick_label_pipeline.fit_transform(test_set)
        print('特徴量とラベルの分離完了')

        # モデルの読み込み
        if input_pkl_filename == None:
            # fit()で生成したpklファイルを使用
            input_pkl_filename = self.output_pkl_filename
        input_pkl_filepath = self.consts.OUTPUT_PKL_PATH + '/' + input_pkl_filename
        model = joblib.load(input_pkl_filepath)
        print(f'fitting済みのモデルを読み込む: {input_pkl_filepath}')

        # 学習
        predicted_label = model.predict(X_test)

        # 正答率の算出
        # accuracy
        accuracy = accuracy_score(y_test, predicted_label)
        print(f'accuracy_score: {accuracy}')
        # balanced_accuracy
        balanced_accuracy = balanced_accuracy_score(y_test, predicted_label)
        print(f'balanced_accuracy_score: {balanced_accuracy}')
        # f1
        f1 = f1_score(y_test, predicted_label)
        print(f'f1_score: {f1}')
        # confusion matrix
        conf_mat = confusion_matrix(y_test, predicted_label)
        print(f'confusion matrix: {conf_mat}')

        # 記録
        fname = input_pkl_filename
        record = RecExpResultToMarkdown(fname, self.consts, accuracy, balanced_accuracy,
                                        f1, conf_mat, input_pkl_filepath, self.train_filename_list, test_filename_list)
        record.write()

    def main(self):
        # [training data] csv -> DataFrame
        df_train = CsvToDf(self.train_filename_list,
                           self.consts.TRAIN_CSV_PATH)
        # [test data] csv -> DataFrame
        df_test = CsvToDf(self.test_filename_list, self.consts.TEST_CSV_PATH)
        # train_set_trial = ['trial1', 'trial2']
        # test_set_trial = ['trial3']
        # train_set = df[df['session_id'].isin(train_set_trial)]
        # test_set = df[df['session_id'].isin(test_set_trial)]
        print("CSV->DataFrameへの変換完了")

        # 特徴量とラベルの分離
        pl = MlPipeline(self.consts)
        X_train = pl.pick_features_pipeline(df_train)
        y_train = pl.pick_label_pipeline(df_train)
        X_test = pl.pick_features_pipeline(df_test)
        y_test = pl.pick_label_pipeline(df_test)
        print('特徴量とラベルの分離完了')

        # 学習
        model = joblib.load(self.input_pkl_filename)
        model.fit(X_train, y_train)
        print('学習完了')

        # 予測
        predict_label = model.predict(X_test)
        print('予測完了')

        # 正答率の算出
        # accuracy
        accuracy = accuracy_score(y_test, predict_label)
        print(f'accuracy_score: {accuracy}')
        # balanced_accuracy
        balanced_accuracy = balanced_accuracy_score(y_test, predict_label)
        print(f'balanced_accuracy_score: {balanced_accuracy}')
        # f1
        f1 = f1_score(y_test, predict_label)
        print(f'f1_score: {f1}')
        # confusion matrix
        conf_mat = confusion_matrix(y_test, predict_label)
        print(f'confusion matrix: {conf_mat}')

        # 記録
        fname = ''
        record = RecExpResultToMarkdown(fname, self.consts, accuracy, balanced_accuracy,
                                        f1, conf_mat, self.input_pkl_filename, self.train_filename_list, self.test_filename_list)
        record.write()


if __name__ == '__main__':
    # parser = argparse.ArgumentParser()
    # parser.add_argument('--train_files', nargs='+', required=True)
    # parser.add_argument('--test_files', nargs='+', required=True)
    # parser.add_argument('--input_pkl_filename', default=None)
    # parser.add_argument('--output_pkl_filename', default=None)
    # parser.add_argument('--csv_filename', default=None)
    # args = parser.parse_args()

    # eng = MlPred(train_filename_list=args.train_files, test_filename_list=args.test_files,
    #              input_pkl_filename=args.input_pkl_filename, output_pkl_filename=args.output_pkl_filename, csv_filename=args.csv_filename)

    ###################
    ###  wav -> csv ###
    ###################
    # eng.wav2csv()

    ###########
    ### fit ###
    ###########
    # consts
    # input_pkl_paths = ['../out/experiment_result/data_of_2022-01-07_new/AGC-0angle-under5m', '../out/experiment_result/data_of_2021-12-27/NoAGC-0angle-under5m',
    #                    '../out/experiment_result/data_of_2021-12-27/AGC-45angle-under5m', '../out/experiment_result/data_of_2021-12-27/NoAGC-45angle-under5m']
    # label_attrbs = [['facing'], ['facing'], ['facing2'], ['facing2']]
    # facing_dov_angles = [[1], [1], [1, 2], [1, 2]]
    input_pkl_paths = ['../out/experiment_result/data_of_2022-01-07_new/AGC-0angle-under5m',
                       '../out/experiment_result/data_of_2022-01-07_new/AGC-45angle-under5m']
    label_attrbs = [['facing'], ['facing2']]
    facing_dov_angles = [[1], [1, 2]]

    # other
    train_filename_list = [
        '2021-12-27_raspi_48000Hz_w1_N2^12_overlap80_with2022-01-07.csv']
    test_filename_list = [
        '2021-12-27_raspi_48000Hz_w1_N2^12_overlap80_with2022-01-07.csv']
    # input_pkl_filenames = ['ExtraTreesClassifier_ClusterCentroids_2021-12-28_no8', 'ExtraTreesClassifier_RandomOverSampler_2021-12-29_no3',
    #                        'ExtraTreesClassifier_SMOTE_2021-12-29_no4', 'ExtraTreesClassifier_NoResampler_2021-12-29_no0']  # ここを編集
    # output_pkl_filenames = ['AGC-0angle-under5m_2021-12-27_ExtraTreesClassifier_ClusterCentroids_2021-12-28_no8.sav', 'NoAGC-0angle-under5m_2021-12-27_ExtraTreesClassifier_RandomOverSampler_2021-12-29_no3.sav',
    #                         'AGC-45angle-under5m_2021-12-27_ExtraTreesClassifier_SMOTE_2021-12-29_no4.sav', 'NoAGC-45angle-under5m_2021-12-27_ExtraTreesClassifier_NoResampler_2021-12-29_no0.sav']  # ここを編集
    input_pkl_filenames = ['ExtraTreesClassifier_RandomUnderSampler_2022-01-09_no2',
                           'ExtraTreesClassifier_NoResampler_2022-01-09_no0']  # ここを編集
    output_pkl_filenames = ['AGC-0angle-under5m_2022-01-07_ExtraTreesClassifier_RandomUnderSampler_2022-01-09_no2.sav',
                            'AGC-45angle-under5m_2022-01-07_ExtraTreesClassifier_NoResampler_2022-01-09_no0.sav']  # ここを編集
    csv_filename = None  # wav->csvの時のcsvの名前 no edit

    # resampler
    # resamplers = [ClusterCentroids(random_state=42), RandomOverSampler(
    #     random_state=42), SMOTE(random_state=42, n_jobs=-1), None]
    resamplers = [ClusterCentroids(random_state=42), RandomOverSampler(
        random_state=42), SMOTE(random_state=42, n_jobs=-1), None]

    for i in range(2):
        input_pkl_path = input_pkl_paths[i]
        label_attrb = label_attrbs[i]
        facing_dov_angle = facing_dov_angles[i]

        input_pkl_filename = input_pkl_filenames[i]
        output_pkl_filename = output_pkl_filenames[i]
        resampler = resamplers[i]

        consts = Exp_Consts(dataset_path='../../experiment_dataset/2021-12-01_gym_mac',
                            train_csv_path='../out/csv/experiment',
                            test_csv_path='../out/csv/experiment',
                            input_pkl_path=input_pkl_path,  # edit
                            output_pkl_path='../out/ml_model_fitting_result/2022-01-07',
                            output_path='../out/experiment_result',
                            label_attrb=label_attrb,
                            facing_dov_angles=facing_dov_angle)

        eng = MlPred(consts, train_filename_list, test_filename_list,
                     input_pkl_filename, output_pkl_filename, csv_filename)
        eng.fit(resampler, train_set_trial=['trial3', 'trial4', 'trial5'])

    ###############
    ### predict ###
    ###############
    # pkl_filename = 'ExtraTreesClassifier_ClusterCentroids_2021-11-04_no0.sav'
    # # [raspi]立った状態
    # test_set_trial = ['trial1', 'trial2', 'trial3']
    # eng.predict(test_set_trial=test_set_trial, test_filename_list=[
    #             '2021-11-26_raspi_16000Hz_w1_N2^12_overlap80.csv'], input_pkl_filename=pkl_filename)

    # # [raspi]座った状態
    # print('------')
    # test_set_trial = ['trial4', 'trial5', 'trial6']
    # eng.predict(test_set_trial=test_set_trial, test_filename_list=[
    #             '2021-11-26_raspi_16000Hz_w1_N2^12_overlap80.csv'], input_pkl_filename=pkl_filename)

    # # [mac]立った状態
    # print('------')
    # test_set_trial = ['trial1', 'trial2', 'trial3']
    # eng.predict(test_set_trial=test_set_trial, test_filename_list=[
    #             '2021-11-29_mac_48000Hz_w1_N2^12_overlap80.csv'], input_pkl_filename=pkl_filename)

    # # [mac]座った状態
    # print('------')
    # test_set_trial = ['trial4', 'trial5', 'trial6']
    # eng.predict(test_set_trial=test_set_trial, test_filename_list=[
    #             '2021-11-29_mac_48000Hz_w1_N2^12_overlap80.csv'], input_pkl_filename=pkl_filename)

    ###################
    ### fit_predict ###
    ###################
    # eng.fit_predict(test_filename_list=['2021-11-26_raspi_16000Hz_w1_N2^12_overlap80.csv'],
    #                 test_set_trial=['trial1', 'trial2', 'trial3'], input_pkl_filename='')
