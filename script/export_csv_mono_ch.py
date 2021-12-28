#!/usr/bin/env python3
# coding: utf-8

import csv
import sys
import os
from typing import List, Any, Union, Dict

# 自作ライブラリのパス追加
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from mylib import fetch_features_from_mono_ch as ff
from mylib.load_constants import ML_Consts

# 出力ファイルへのパス
OUTPUT_PATH = "../out/csv/experiment"
# データセットへのパス
DATASET_PATH = "../../experiment_dataset/2021-12-27_gym_new"

def createWav2Csv(output_csv_filename: str, dataset_path: str = DATASET_PATH, output_path: str = OUTPUT_PATH, w: int = 1, N: int = 2**12, overlap: int = 80) -> None:
    '''
    CSVを作成する関数

    Parameters
    ----------
    output_csv_filename : str
        出力するCSVファイルの名前
    datase_path : str
        WAVデータを格納されているディレクトリへのパス
    output_path : str
        CSVファイルを出力する先のディレクトリへのパス
    w: int
        ピーク検出に対する感度
    N : int
        FFTのサイズ
    overlap : int or float
        FFTのオーバーラップ率

    Returns
    -------
    None
    '''
    output_csv_path = output_path + '/' + output_csv_filename
    with open(output_csv_path, 'w') as f:
        writer = csv.writer(f)

        # ヘッダー行を追加する
        # header_attr = ['id', 'filename', 'participant_id', 'room_id', 'device_placement_id', 'session_id',
        #                'polar_position_id', 'distance', 'polar_angle', 'utterance_id', 'dov_angle', 'mic_channel']
        header_attr = ['id', 'filename', 'participant_id', 'date', 'status', 'agc_status',
                       'distance', 'angle', 'session_id', 'mic_channel']
        header_feature_vals = ['low_power', 'high_power', 'hlbr', 'coe1[0]', 'coe1[1]', 'coe3[0]', 'coe3[1]', 'coe3[2]', 'coe3[3]',
                               'ratio_max_to_10ms_ave_peaks', 'ratio_max_to_9th_ave_peaks', 'ac_std', 'ac_auc', 'diff_std', 'diff_auc', 'srmr']
        header_gp_tdoa = ['gp_max_val_std', 'gp_max_val_range', 'gp_max_val_min', 'gp_max_val_max', 'gp_max_val_mean', 'gp_max_ix_std', 'gp_max_ix_range', 'gp_max_ix_min', 'gp_max_ix_max',
                          'gp_max_ix_mean', 'gp_auc_std', 'gp_auc_range', 'gp_auc_min', 'gp_auc_max', 'gp_auc_mean', 'tdoa_std', 'tdoa_range', 'tdoa_min', 'tdoa_max', 'tdoa_mean']
        header = header_attr + header_feature_vals + header_gp_tdoa
        # 書き込む
        writer.writerow(header)

        # 特徴量を計算
        # ff_gen = ff.FetchFeaturesFromDataset(
        #     dataset_path, w=w, N=N, overlap=overlap)
        ff_gen = ff.FetchFeaturesFromExpDataset(
            dataset_path, w=w, N=N, overlap=overlap)
        for rows in ff_gen:
            writer.writerows(rows)

            # ファイルへ出力する
            print(f'flush data to a csv file: {output_csv_path}.')
            f.flush()

def createCsv(filename: str, consts: ML_Consts = None) -> None:
    '''
    CSVを作成する関数

    Parameters
    ----------
    filename : str
        CSVファイルの名前
    consts: mylib.load_constants.ML_Consts, default None
        定数

    Returns
    -------
    None
    '''

    # 定数の設定
    if consts is None:
        output_path = OUTPUT_PATH
        dataset_path = DATASET_PATH
    else:
        output_path = consts.OUTPUT_PATH
        dataset_path = consts.DATASET_PATH

    with open(output_path + '/' + filename, 'w') as f:
        writer = csv.writer(f)

        # ヘッダー行を追加する
        header_attr = ['id', 'filename', 'participant_id', 'room_id', 'device_placement_id', 'session_id',
                       'polar_position_id', 'distance', 'polar_angle', 'utterance_id', 'dov_angle', 'mic_channel']
        header_feature_vals = ['low_power', 'high_power', 'hlbr', 'coe1[0]', 'coe1[1]', 'coe3[0]', 'coe3[1]', 'coe3[2]', 'coe3[3]',
                               'ratio_max_to_10ms_ave_peaks', 'ratio_max_to_9th_ave_peaks', 'ac_std', 'ac_auc', 'diff_std', 'diff_auc', 'srmr']
        header_gp_tdoa = ['gp_max_val_std', 'gp_max_val_range', 'gp_max_val_min', 'gp_max_val_max', 'gp_max_val_mean', 'gp_max_ix_std', 'gp_max_ix_range', 'gp_max_ix_min', 'gp_max_ix_max',
                          'gp_max_ix_mean', 'gp_auc_std', 'gp_auc_range', 'gp_auc_min', 'gp_auc_max', 'gp_auc_mean', 'tdoa_std', 'tdoa_range', 'tdoa_min', 'tdoa_max', 'tdoa_mean']
        header = header_attr + header_feature_vals + header_gp_tdoa
        # 書き込む
        writer.writerow(header)

        # 特徴量を計算
        ff_gen = ff.FetchFeaturesFromDataset(dataset_path)
        for rows in ff_gen:
            writer.writerows(rows)

            # ファイルへ出力する
            # print(f'flush data to a csv file: {filename}.')
            f.flush()


def createCsvGp(filename: str, consts: ML_Consts = None) -> None:
    '''
    CSVを作成する関数。GCC-PHAT&TDOAのみを計算し、CSVに格納する。

    Parameters
    ----------
    filename : str, default 'features.csv'
        CSVファイルの名前
    consts: mylib.load_constants.ML_Consts, default None
        定数

    Returns
    -------
    None
    '''

    # 定数の設定
    if consts is None:
        output_path = OUTPUT_PATH
        dataset_path = DATASET_PATH
    else:
        output_path = consts.OUTPUT_PATH
        dataset_path = consts.DATASET_PATH

    with open(output_path + '/' + filename, 'w') as f:
        writer = csv.writer(f)

        # ヘッダー行を追加する
        header_attr = ['id', 'filename', 'participant_id', 'room_id', 'device_placement_id', 'session_id',
                       'polar_position_id', 'distance', 'polar_angle', 'utterance_id', 'dov_angle', 'mic_channel']
        header_gp_tdoa = ['gp_max_val_std', 'gp_max_val_range', 'gp_max_val_min', 'gp_max_val_max', 'gp_max_val_mean', 'gp_max_ix_std', 'gp_max_ix_range', 'gp_max_ix_min', 'gp_max_ix_max',
                          'gp_max_ix_mean', 'gp_auc_std', 'gp_auc_range', 'gp_auc_min', 'gp_auc_max', 'gp_auc_mean', 'tdoa_std', 'tdoa_range', 'tdoa_min', 'tdoa_max', 'tdoa_mean']
        header = header_attr + header_gp_tdoa
        # 書き込む
        writer.writerow(header)

        # 特徴量を計算
        ff_gen = ff.FetchFeaturesFromDataset(
            dataset_path, w=1, N='full', overlap=0)
        for rows in ff_gen:
            writer.writerows(rows)

            # ファイルへ出力する
            print(f'flush data to a csv file: {filename}.')
            f.flush()


if __name__ == '__main__':
    if len(sys.argv) > 1:
        filename = sys.argv[1]
        createWav2Csv(filename)
    else:
        createCsvGp()
