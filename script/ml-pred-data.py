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

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from mylib.load_constants import Exp_Consts
from mylib.load_csv import CsvToDf
from mylib.ml_pipeline_components import MlPipeline
from mylib.record_model_data import RecExpResultToMarkdown
from mylib import record_model_data as rec

class MlPred():
    def __init__(self, train_filename_list: List = None, test_filename_list: List = None, input_pkl_filename: str = None, output_pkl_filename: str = None, csv_filename: str = None) -> None:
        self.consts = Exp_Consts(dataset_path='../../experiment_dataset/2021-11-29_mac',
                                 train_csv_path='../out/csv',
                                 test_csv_path='../out/csv/experiment',
                                 input_pkl_path='../out/ml_model_result',
                                 output_pkl_path='../out/ml_model_fitting_result',
                                 output_path='../out/experiment_result')
        # self.consts = Exp_Consts(dataset_path='../../experiment_dataset/2021-11-26',
        #                          train_csv_path='../out/csv',
        #                          test_csv_path='../out/csv/experiment',
        #                          input_pkl_path='../out/ml_model_result',
        #                          output_pkl_path='../out/ml_model_fitting_result',
        #                          output_path='../out/experiment_result')
        self.train_filename_list = train_filename_list
        self.test_filename_list = test_filename_list
        self.input_pkl_filename = input_pkl_filename
        self.output_pkl_filename = output_pkl_filename
        self.csv_filename = csv_filename

    def wav2csv(self):
        # wav -> csv
        createWav2Csv(self.csv_filename, self.consts.DATASET_PATH,
                      self.consts.TEST_CSV_PATH, w=1, N=2**12, overlap=80)

    def fit(self, train_filename_list: List = None, train_csv_path: str = None, train_set_trial: List = None, input_pkl_filename: str = None, output_pkl_filename: str = None):
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
        X_train = pl.pick_features_pipeline.fit_transform(train_set)
        y_train = pl.pick_label_pipeline.fit_transform(train_set)
        print('特徴量とラベルの分離完了')

        # 学習
        if input_pkl_filename == None:
            input_pkl_filename = self.input_pkl_filename
        input_pkl_filepath = self.consts.INPUT_PKL_PATH + '/' + \
            input_pkl_filename + '/' + input_pkl_filename + '.pkl'
        model = joblib.load(input_pkl_filepath)
        model.fit(X_train, y_train)
        print('学習完了')

        # fittingした結果をpklへ保存する
        if output_pkl_filename == None:
            output_pkl_filename = self.output_pkl_filename
        output_pkl_filepath = self.consts.OUTPUT_PKL_PATH + '/' + output_pkl_filename
        joblib.dump(model, output_pkl_filepath)
        print(f'pklへの出力: {output_pkl_filepath}')

    def fit_predict(self, test_filename_list: List = None, test_csv_path: str = None, test_set_trial: List = None, input_pkl_filename: str = None):
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
    parser = argparse.ArgumentParser()
    parser.add_argument('--train_files', nargs='+', required=True)
    parser.add_argument('--test_files', nargs='+', required=True)
    parser.add_argument('--input_pkl_filename', default=None)
    parser.add_argument('--output_pkl_filename', default=None)
    parser.add_argument('--csv_filename', default=None)

    args = parser.parse_args()

    eng = MlPred(train_filename_list=args.train_files, test_filename_list=args.test_files,
                 input_pkl_filename=args.input_pkl_filename, output_pkl_filename=args.output_pkl_filename, csv_filename=args.csv_filename)
    ###################
    ###  wav -> csv ###
    ###################
    # eng.wav2csv()

    ###########
    ### fit ###
    ###########
    # eng.fit()

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
    eng.fit_predict(test_filename_list=['2021-11-26_raspi_16000Hz_w1_N2^12_overlap80.csv'],
                    test_set_trial=['trial1', 'trial2', 'trial3'], input_pkl_filename='')
