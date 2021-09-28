#!/usr/bin/env python3
# coding: utf-8

import csv
import sys
import os
from typing import List, Any, Union, Dict

# 自作ライブラリのパス追加
# sys.path.append('..')
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from mylib import fetch_features_ch0 as ff

# 出力ファイルへのパス
OUTPUT_PATH = "../out/"
# データセットへのパス
DATASET_PATH = "../../dataset"


def createCsv(filename: str = 'features_ch0.csv') -> None:
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
        header_attr = ['id', 'filename', 'participant_id', 'room_id', 'device_placement_id', 'session_id', 'polar_position_id', 'distance', 'polar_angle', 'utterance_id', 'dov_angle', 'mic_channel']
        header_feature_vals = ['low_power', 'high_power', 'hlbr', 'coe1[0]', 'coe1[1]', 'coe3[0]', 'coe3[1]', 'coe3[2]', 'coe3[3]',
                               'ratio_max_to_10ms_ave_peaks', 'ratio_max_to_9th_ave_peaks', 'ac_std', 'ac_auc', 'diff_std', 'diff_auc', 'srmr']
        header_gp_tdoa = ['gp_max_val_std', 'gp_max_val_range', 'gp_max_val_min', 'gp_max_val_max', 'gp_max_val_mean', 'gp_max_ix_std', 'gp_max_ix_range', 'gp_max_ix_min', 'gp_max_ix_max',
                          'gp_max_ix_mean', 'gp_auc_std', 'gp_auc_range', 'gp_auc_min', 'gp_auc_max', 'gp_auc_mean', 'tdoa_std', 'tdoa_range', 'tdoa_min', 'tdoa_max', 'tdoa_mean']
        header = header_attr + header_feature_vals + header_gp_tdoa
        # 書き込む
        writer.writerow(header)

        # 特徴量を計算
        ff_gen = ff.FetchFeaturesFromDataset(DATASET_PATH)
        for rows in ff_gen:
            writer.writerows(rows)

            # ファイルへ出力する
            print(f'flush data to a csv file: {filename}.')
            f.flush()

if __name__ == '__main__':
    if len(sys.argv) > 1:
        filename = sys.argv[1]
        createCsv(filename)
    else:
        createCsv()
