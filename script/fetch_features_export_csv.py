#!/usr/bin/env python3
# coding: utf-8

import csv
import sys
import os
from typing import List, Any, Union, Dict

# 自作ライブラリのパス追加
sys.path.append('..')
from mylib import fetch_features as ff

# 出力ファイルへのパス
OUTPUT_PATH = "../out/"
# データセットへのパス
DATASET_PATH = "../../dataset/"


def createCsv(filename: str = 'features.csv') -> None:
    '''
    CSVを作成する関数

    Parameters
    ----------
    filename : str, default 'features.csv'
        CSVファイルの名前

    Returns
    -------
    None
    '''

    with open(OUTPUT_PATH + filename, 'w') as f:
        writer = csv.writer(f)

        # ヘッダー行を追加する
        header_attr = ['id', 'filename', 'participant', 'room', 'placement', 'session', 'polar_position', 
                  'utterance', 'dov_angle', 'channel']
        header_feature_vals = ['low_power', 'high_power', 'hlbr', 'coe1[0]', 'coe1[1]', 'coe3[0]', 'coe3[1]', 'coe3[2]', 'coe3[3]',
                               'ratio_max_to_10ms_ave_peaks', 'ratio_max_to_9th_ave_peaks', 'ac_std', 'ac_auc', 'diff_std', 'diff_auc', 'srmr']
        header_gp_tdoa = ['gp_max_val_ch1', 'gp_max_ix_ch1', 'gp_auc_ch1', 'tdoa_ch1', 'gp_max_val_ch2', 'gp_max_ix_ch2', 'gp_auc_ch2', 'tdoa_ch2',
                          'gp_max_val_ch3', 'gp_max_ix_ch3', 'gp_auc_ch3', 'tdoa_ch3', 'gp_max_val_ch4', 'gp_max_ix_ch4', 'gp_auc_ch4', 'tdoa_ch4']
        header = header_attr + header_feature_vals + header_gp_tdoa
        # 書き込む
        writer.writerow(header)

        num = 0
        # 特徴量を計算
        ff_gen = ff.FetchFeaturesFromDataset(DATASET_PATH)
        for rows in ff_gen:
            if(num > 3):
                break
            writer.writerows(rows)
            num += 1



if __name__ == '__main__':
    if len(sys.argv) > 1:
        filename = sys.argv[1]
        createCsv(filename)
    else:
        createCsv()
