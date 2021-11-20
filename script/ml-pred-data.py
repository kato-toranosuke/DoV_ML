#!/usr/bin/env python3
# coding: utf-8

import joblib
import sys
import os
from typing import List
from export_csv_mono_ch import createCsv
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from mylib.load_constants import ML_Consts
from mylib.load_csv import CsvToDf
from mylib.ml_pipeline_components import MlPipeline


def main(csv_filename_list: List, pkl_path: str):
    consts = ML_Consts(csv_path='../out/csv/experiment',
                       dataset_path='hoge/hoge', output_path='hoge/hoge')
    filename = 'hoge'
    # wav -> csv
    createCsv(filename, consts.OUTPUT_PATH, consts.DATASET_PATH)

    # csv -> DataFrame
    df = CsvToDf(csv_filename_list, consts.CSV_PATH)
    # train_set_trial = ['trial1', 'trial2']
    # test_set_trial = ['trial3']
    # train_set = df[df['session_id'].isin(train_set_trial)]
    # test_set = df[df['session_id'].isin(test_set_trial)]
    print("データの読み込み完了")

    # データのクリーニング
    pl = MlPipeline(consts)
    X = pl.pick_features_pipeline(df)
    y = pl.pick_label_pipeline(df)
    print('データのクリーニングが完了')

    # 予測
    model = joblib.load(pkl_path)

    # 正答率の算出


if __name__ == '__main__':
    if len(sys.argv) > 1:
        csv_filename_list = []
        for i in range(1, len(sys.argv)):
            csv_filename_list.append(sys.argv[i])
