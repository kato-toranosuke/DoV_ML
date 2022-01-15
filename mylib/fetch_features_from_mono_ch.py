#!/usr/bin/env python3
# coding: utf-8

from sys import stderr
from typing import List, Any, Union, Dict
import itertools
import numpy as np
import os
import sys
from . import fetch_features_func as fff
from . import cis
from . import fetch_features as ff

def GetRowData(dir_path: str, attr: Dict, gp_tdoa_mic_channels: List, w: int, N: Union[int, str] = 'full', overlap: Union[int, float] = 0.8) -> List:
    '''
    音声ファイルに対応する特徴量の抽出。

    Parameters
    ----------
    dir_path: str
        ファイルが格納されているディレクトリまでのパス
    attr: dict
        属性値が格納された辞書
    gp_tdoa_mic_channels: 
    w: int
        ピーク検出に対する感度
    N : int or str
        FFTのサイズ
    overlap : int or float
        FFTのオーバーラップ率

    Returns
    -------
    row: list
        1行分のデータ
    '''
    ##########################
    ### GCC-PHAT & TDOA以外 ###
    ##########################

    # channel0のファイルパス
    filename = attr['utterance_id'] + '_' + \
        attr['dov_angle'] + '_' + str(attr['mic_channel']) + '.wav'
    file_path = dir_path + '/' + filename

    # 指定したfile_pathに該当するwavがない場合、スキップする
    if not os.path.isfile(file_path):
        raise FileNotFoundError(file_path + ' is not found!')

    id = attr['id']
    print(f'id: {id}, file path: {file_path}')

    # channel0の音声データを読み込む
    v, fs = cis.wavread(file_path)

    # 特徴量を得る
    features = ff.FetchFeaturesFromMonoData(v, fs, N, overlap, w=w)

    # FFTサイズ
    # N = 2**12
    # 特徴量を得る
    # features = ff.FetchFeaturesFromMonoDataNo128Fitting(v, fs, N, overlap, w=w)

    #######################
    ### GCC-PHAT & TDOA ###
    #######################

    # channel1~4の音声データを読み込む
    voice_data = []
    for ch in gp_tdoa_mic_channels:
        fname = attr['utterance_id'] + '_' + \
            attr['dov_angle'] + '_' + str(ch) + '.wav'
        fpath = dir_path + '/' + fname
        v_, fs_ = cis.wavread(fpath)
        voice_data.append([v_, fs_])

    # GCC-PHATの特徴量を格納する配列を生成
    pair_gp_tdoa_features = []

    # 各ペアについて計算
    mic_ch_pairs = itertools.combinations(gp_tdoa_mic_channels, 2)
    for pair in mic_ch_pairs:
        # マイクのチャンネル
        mic_ch1 = pair[0]
        mic_ch2 = pair[1]
        # インデックスを計算（mic channelは1から始まる）
        ix1 = mic_ch1 - 1
        ix2 = mic_ch2 - 1
        # 音声データを取得
        v1 = voice_data[ix1][0]
        v2 = voice_data[ix2][0]
        # サンプリング周波数を取得
        fs = voice_data[ix1][1]

        # GCC-PHATとTDOAを計算
        gp_max_val, gp_max_ix, gp_auc, tdoa = fff.GetGccPhatAndTdoa(
            v1, v2, fs=fs, w=w)

        # 配列に格納する
        pair_gp_tdoa_features.append([gp_max_val, gp_max_ix, gp_auc, tdoa])

    # 標準偏差、範囲、最小値、最大値、平均を求める
    gp_tdoa_features = []
    np_pair_gp_tdoa_features = np.array(pair_gp_tdoa_features)
    for i in range(4):
        vals = np_pair_gp_tdoa_features[:, i]
        std = np.std(vals)
        max = np.max(vals)
        min = np.min(vals)
        r = max - min
        mean = np.mean(vals)

        gp_tdoa_features.extend([std, r, min, max, mean])

    ###############
    ### 属性情報 ###
    ###############
    attr = [attr['id'], filename, attr['participant_id'], attr['room_id'], attr['device_placement_id'], attr['session_id'],
            attr['polar_position_id'], attr['distance'], attr['polar_angle'], attr['utterance_id'], attr['dov_angle'], attr['mic_channel']]

    # 行情報を生成
    row = attr + features + gp_tdoa_features
    # row = attr + gp_tdoa_features

    return row

def GetRowDataFromExpData(dir_path: str, attr: Dict, gp_tdoa_mic_channels: List, w: int, N: Union[int, str] = 'full', overlap: Union[int, float] = 0.8) -> List:
    '''
    音声ファイルに対応する特徴量の抽出。

    Parameters
    ----------
    dir_path: str
        ファイルが格納されているディレクトリまでのパス
    attr: dict
        属性値が格納された辞書
    gp_tdoa_mic_channels: 
    w: int
        ピーク検出に対する感度
    N : int or str
        FFTのサイズ
    overlap : int or float
        FFTのオーバーラップ率

    Returns
    -------
    row: list
        1行分のデータ
    '''
    ##########################
    ### GCC-PHAT & TDOA以外 ###
    ##########################

    # channel0のファイルパス
    filename = 'rec' + '_' + str(attr['mic_channel']) + '.wav'
    file_path = dir_path + '/' + filename

    # 指定したfile_pathに該当するwavがない場合、スキップする
    if not os.path.isfile(file_path):
        raise FileNotFoundError(file_path + ' is not found!')

    id = attr['id']
    print(f'id: {id}, file path: {file_path}')

    # channel0の音声データを読み込む
    v, fs = cis.wavread(file_path)

    # 特徴量を得る
    features = ff.FetchFeaturesFromMonoData(v, fs, N, overlap, w=w)

    # FFTサイズ
    # N = 2**12
    # 特徴量を得る
    # features = ff.FetchFeaturesFromMonoDataNo128Fitting(v, fs, N, overlap, w=w)

    #######################
    ### GCC-PHAT & TDOA ###
    #######################

    # channel1~4の音声データを読み込む
    voice_data = []
    for ch in gp_tdoa_mic_channels:
        fname = 'rec' + '_' + str(ch) + '.wav'
        fpath = dir_path + '/' + fname
        v_, fs_ = cis.wavread(fpath)
        voice_data.append([v_, fs_])

    # GCC-PHATの特徴量を格納する配列を生成
    pair_gp_tdoa_features = []

    # 各ペアについて計算
    mic_ch_pairs = itertools.combinations(gp_tdoa_mic_channels, 2)
    for pair in mic_ch_pairs:
        # マイクのチャンネル
        mic_ch1 = pair[0]
        mic_ch2 = pair[1]
        # インデックスを計算（mic channelは1から始まる）
        ix1 = mic_ch1 - 1
        ix2 = mic_ch2 - 1
        # 音声データを取得
        v1 = voice_data[ix1][0]
        v2 = voice_data[ix2][0]
        # サンプリング周波数を取得
        fs = voice_data[ix1][1]

        # GCC-PHATとTDOAを計算
        gp_max_val, gp_max_ix, gp_auc, tdoa = fff.GetGccPhatAndTdoa(
            v1, v2, fs=fs, w=w)

        # 配列に格納する
        pair_gp_tdoa_features.append([gp_max_val, gp_max_ix, gp_auc, tdoa])

    # 標準偏差、範囲、最小値、最大値、平均を求める
    gp_tdoa_features = []
    np_pair_gp_tdoa_features = np.array(pair_gp_tdoa_features)
    for i in range(4):
        vals = np_pair_gp_tdoa_features[:, i]
        std = np.std(vals)
        max = np.max(vals)
        min = np.min(vals)
        r = max - min
        mean = np.mean(vals)

        gp_tdoa_features.extend([std, r, min, max, mean])

    ###############
    ### 属性情報 ###
    ###############
    attr = [attr['id'], filename, attr['participant_id'], attr['date'], attr['status'], attr['agc_status'],
            attr['distance'], attr['angle'], attr['session_id'], attr['mic_channel'], attr['facing'], attr['facing2']]

    # 行情報を生成
    row = attr + features + gp_tdoa_features

    return row

def FetchFeaturesFromExpDataset(DATASET_PATH: str, w: int, N: Union[int, str], overlap: Union[int, float]) -> List:
    ####################
    ### 各種パラメータ ###
    ####################
    # raspi
    participant_ids = ['raspi-ubuntu-' + str(i) for i in range(1, 6)]
    # 日付
    dates = ['2022-01-13']
    # 状態
    statuses = ['standup']
    # AGC
    agc_statuses = ['AGC', 'NoAGC']
    # 距離
    distances = [1, 3, 5]
    # 角度
    angles = [0, 45, 90, 135, 180]
    # セッション
    session_ids = ['trial' + str(i) for i in range(1, 21)]

    # GCC-PHAT, TDOA以外の計算に用いるマイクチャンネル(音声認識用に使用しているchannel0のみ特徴量抽出に利用する。)
    mic_channel = 0
    # GCC-PHAT, TDOAの計算に用いるマイクチャンネル
    gp_tdoa_mic_channels = range(1, 5)

    #########################
    ### 各種特徴量を取得する ###
    #########################
    # ファイルのフェッチ
    id = 0
    for participant_id in participant_ids:
        # 第一階層
        first_dir_name = participant_id
        for date in dates:
            for status in statuses:
                for agc_status in agc_statuses:
                    for distance in distances:
                        for angle in angles:
                            rows = []
                            for session_id in session_ids:
                                # 第二階層
                                second_dir_name = date + '-' + status + '-' + agc_status + \
                                    '_' + str(distance) + 'm_' + \
                                    str(angle) + '_' + session_id

                                # 音声ファイルが格納されているディレクトリまでのパス
                                dir_path = DATASET_PATH + '/' + first_dir_name + \
                                    '/' + second_dir_name

                                # 属性値を格納する辞書の作成
                                attr = {}
                                attr['id'] = id
                                attr['participant_id'] = participant_id
                                attr['date'] = date
                                attr['status'] = status
                                attr['agc_status'] = agc_status
                                attr['distance'] = distance
                                attr['angle'] = angle
                                attr['session_id'] = session_id
                                attr['mic_channel'] = mic_channel

                                if participant_id == 'raspi-ubuntu-1':
                                    if angle == 0:
                                        attr['facing'] = 1
                                        attr['facing2'] = 1
                                    elif angle == 45:
                                        attr['facing'] = 0
                                        attr['facing2'] = 2
                                    else:
                                        attr['facing'] = 0
                                        attr['facing2'] = 0
                                elif participant_id == 'raspi-ubuntu-2':
                                    if angle == 45:
                                        attr['facing'] = 1
                                        attr['facing2'] = 1
                                    elif angle == 0 or angle == 90:
                                        attr['facing'] = 0
                                        attr['facing2'] = 2
                                    else:
                                        attr['facing'] = 0
                                        attr['facing2'] = 0
                                elif participant_id == 'raspi-ubuntu-3':
                                    if angle == 90:
                                        attr['facing'] = 1
                                        attr['facing2'] = 1
                                    elif angle == 45 or angle == 135:
                                        attr['facing'] = 0
                                        attr['facing2'] = 2
                                    else:
                                        attr['facing'] = 0
                                        attr['facing2'] = 0
                                elif participant_id == 'raspi-ubuntu-4':
                                    if angle == 135:
                                        attr['facing'] = 1
                                        attr['facing2'] = 1
                                    elif angle == 90 or angle == 180:
                                        attr['facing'] = 0
                                        attr['facing2'] = 2
                                    else:
                                        attr['facing'] = 0
                                        attr['facing2'] = 0
                                elif participant_id == 'raspi-ubuntu-5':
                                    if angle == 180:
                                        attr['facing'] = 1
                                        attr['facing2'] = 1
                                    elif angle == 135:
                                        attr['facing'] = 0
                                        attr['facing2'] = 2
                                    else:
                                        attr['facing'] = 0
                                        attr['facing2'] = 0

                                try:
                                    row = GetRowDataFromExpData(
                                        dir_path, attr, gp_tdoa_mic_channels, w=w, N=N, overlap=overlap)
                                except FileNotFoundError as e:
                                    # print(e, file=sys.stderr)
                                    continue
                                else:
                                    # 配列に追加
                                    rows.append(row)
                                    id = id + 1

                            # 第2階層以下同一angleのファイルについて計算が終われば、一旦出力する。
                            yield rows


def FetchFeaturesFromDataset(DATASET_PATH: str, w: int, N: Union[int, str], overlap: Union[int, float]) -> List:
    '''
    データセットの音声データから特徴量を抽出する関数

    Parameters
    ----------
    DATASET_PATH : str
        datasetへのpath
    w: int
        ピーク検出に対する感度
    N : int or str
        FFTのサイズ
    overlap : int or float
        FFTのオーバーラップ率

    Returns
    -------
    all_data : array-like
        csvに出力するデータ
    '''

    ####################
    ### 各種パラメータ ###
    ####################

    # 被験者
    participant_ids = ['s' + str(i) for i in range(1, 12)]
    # 発言
    utterance_ids = ['recording' + str(i) for i in range(2)]
    # セッション
    session_ids = ['trial' + str(i) for i in range(1, 7)]
    # 部屋
    room_ids = ['upstairs', 'downstairs', 'onshinlab', 'gym']
    # 設置場所
    device_placement_ids = ['wall', 'nowall']
    # ユーザ距離
    distance_ids = ['A', 'B', 'C']
    # ユーザ極座標
    polar_angle_ids = [0, 1, 2]
    # DoV angles
    dov_angles = [str(i) for i in range(0, 360, 45)]
    # GCC-PHAT, TDOA以外の計算に用いるマイクチャンネル(音声認識用に使用しているchannel0のみ特徴量抽出に利用する。)
    mic_channel = 0

    # GCC-PHAT, TDOAの計算に用いるマイクチャンネル
    gp_tdoa_mic_channels = range(1, 5)

    #########################
    ### 各種特徴量を取得する ###
    #########################

    # ファイルのフェッチ
    id = 0
    for participant_id in participant_ids:
        # 第1階層
        first_dir_name = participant_id
        for room_id in room_ids:
            for device_placement_id in device_placement_ids:
                for session_id in session_ids:
                    # 第2階層
                    second_dir_name = participant_id + '_' + room_id + \
                        '_' + device_placement_id + '_' + session_id

                    for distance_ix, distance_id in enumerate(distance_ids):
                        for polar_angle_ix, polar_angle_id in enumerate(polar_angle_ids):
                            polar_position_id = distance_id + \
                                str(polar_angle_id)
                            distance = 2 * distance_ix + 1
                            polar_angle = 45 * polar_angle_ix
                            # 第3階層
                            third_dir_name = polar_position_id + '_' + \
                                str(distance) + '_' + str(polar_angle)

                            for utterance_id in utterance_ids:
                                # 一度に書き込む行範囲（特徴量をまとめる配列）
                                rows = []

                                for dov_angle in dov_angles:
                                    # # idが11209以上で実行する
                                    # if(id < 211):
                                    #     id += 1
                                    #     continue
                                    # # idが11210以上は実行しない
                                    # if (id > 11209):
                                    #     id += 1
                                    #     continue

                                    # 音声ファイルが格納されているディレクトリまでのパス
                                    dir_path = DATASET_PATH + '/' + first_dir_name + \
                                        '/' + second_dir_name + '/' + third_dir_name

                                    # 属性値を格納する辞書の作成
                                    attr = {}
                                    attr['id'] = id
                                    attr['participant_id'] = participant_id
                                    attr['room_id'] = room_id
                                    attr['device_placement_id'] = device_placement_id
                                    attr['session_id'] = session_id
                                    attr['polar_position_id'] = polar_position_id
                                    attr['distance'] = distance
                                    attr['polar_angle'] = polar_angle
                                    attr['utterance_id'] = utterance_id
                                    attr['dov_angle'] = dov_angle
                                    attr['mic_channel'] = mic_channel

                                    try:
                                        row = GetRowData(
                                            dir_path, attr, gp_tdoa_mic_channels, w=w, N=N, overlap=overlap)
                                    except FileNotFoundError as e:
                                        # print(e, file=sys.stderr)
                                        continue
                                    else:
                                        # 配列に追加
                                        rows.append(row)
                                        id = id + 1

                                # 第３階層以下同一語句のファイルについて計算が終われば、一旦出力する。
                                yield rows
