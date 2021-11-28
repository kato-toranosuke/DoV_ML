#!/usr/bin/env python3
# coding: utf-8

import joblib
import sys
import os
from typing import List
import argparse
from export_csv_mono_ch import createWav2Csv
from sklearn.metrics import accuracy_score, balanced_accuracy_score, f1_score, confusion_matrix
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from mylib.load_constants import Exp_Consts
from mylib.load_csv import CsvToDf
from mylib.ml_pipeline_components import MlPipeline
from mylib.record_model_data import RecExpResultToMarkdown

class MlPred():
    def __init__(self, train_filename_list: List = None, test_filename_list: List = None, input_pkl_path: str = None, output_pkl_path: str = None, csv_filename: str = None) -> None:
        self.consts = Exp_Consts(dataset_path='../../experiment_dataset/2021-11-26',
                                 train_csv_path='../out/csv',
                                 test_csv_path='../out/csv/experiment',
                                 output_path='../out/experiment_result',
                                 fitting_pkl_path='../out/ml_model_fitting_result')
        self.train_filename_list = train_filename_list
        self.test_filename_list = test_filename_list
        self.input_pkl_path = input_pkl_path
        self.output_pkl_path = output_pkl_path
        self.csv_filename = csv_filename

    def wav2csv(self):
        # wav -> csv
        createWav2Csv(self.csv_filename, self.consts.DATASET_PATH,
                      self.consts.TEST_CSV_PATH, w=1, N=2**12, overlap=80)

    def fit(self, train_filename_list: List = None, train_csv_path: str = None, train_set_trial: List = None, input_pkl_path: str = None):
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
        if input_pkl_path == None:
            input_pkl_path = self.input_pkl_path
        model = joblib.load(input_pkl_path)
        model.fit(X_train, y_train)
        print('学習完了')

        # fittingした結果をpklへ保存する
        pkl_filepath = self.consts.FITTING_PKL_PATH + '/' + self.output_pkl_path
        joblib.dump(model, pkl_filepath)
        print(f'pklへの出力: {pkl_filepath}')

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
        model = joblib.load(self.input_pkl_path)
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
                                        f1, conf_mat, self.input_pkl_path, self.train_filename_list, self.test_filename_list)
        record.write()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--train_files', nargs='+', required=True)
    parser.add_argument('--test_files', nargs='+', required=True)
    parser.add_argument('--input_pkl_path', default=None)
    parser.add_argument('--output_pkl_path', default=None)
    parser.add_argument('--csv_filename', default=None)

    args = parser.parse_args()

    eng = MlPred(train_filename_list=args.train_files, test_filename_list=args.test_files,
                 input_pkl_path=args.input_pkl_path, output_pkl_path=args.output_pkl_path, csv_filename=args.csv_filename)
    # wav -> csv
    # eng.wav2csv()

    # fitting
    eng.fit()
