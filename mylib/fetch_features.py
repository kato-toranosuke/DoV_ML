#!/usr/bin/env python3
# coding: utf-8

from . import fetch_features_func as fff
from .fft import fft
from . import cis
from typing import List, Any, Union, Dict
from srmrpy.srmr import *
import itertools
import numpy as np


# def FetchFeaturesFromMonoData(file_path: str, th: Union[int, float] = 7000, w: int = 3, sec_range: float = 0.01, nth: int = 9):
def FetchFeaturesFromMonoData(v: List, fs: int, th: Union[int, float] = 7000, w: int = 3, sec_range: float = 0.01, nth: int = 9):
    '''
    単一の音声データから特徴量を取得する。

    Parameters
    ----------
    # file_path: str
    #     音声ファイルへのパス
    v : array-like
        音声データ
    fs : int
        音声データのサンプリング周波数
    th: int or float, default 7000
        高周波成分と低周波成分の閾値[Hz]
    w: int, default 3
        ピーク検出の感度に関する値
    sec_range: float, default 0.01
        最大ピークから切り出す時間範囲[sec]
    nth: int, default 9
        最大ピークと比較する、次に高いn番目のピーク

    Returns
    -------
    features: array-like
        各種特徴量が格納された配列
    '''

    # 音声データの読み込み
    # v, fs = cis.wavread(file_path)

    # FFTを用いた周波数解析
    fft_array, fft_mean, fft_axis = fft(v, fs)

    # 低周波成分と高周波成分の取得
    low_power, high_power = fff.GetLHPower(fft_mean, fft_axis, th)
    # 低周波成分と高周波成分の比
    hlbr = fff.GetHLBR(low_power, high_power)

    # 128-bin FFT
    fft_array_128, fft_mean_128, fft_axis_128 = fft(v, fs, 128, 50)
    # 128-bin FFTにフィッティングした線形回帰
    coe1 = fff.FitFFT(fft_mean_128, fft_axis_128, 1)
    # 128-bin FFTにフィッティングした3度の多項式
    coe3 = fff.FitFFT(fft_mean_128, fft_axis_128, 3)

    # 最大ピークと、+-10ms以内の他のピークの平均値の比
    ratio_max_to_10ms_ave_peaks = fff.GetRatioMaxToOtherAvePeaks(
        v, w, fs, sec_range)
    # 最大ピークと、次に高い9つのピークの平均値の比
    ratio_max_to_9th_ave_peaks = fff.GetRatioMaxToNthAvePeaks(v, w, nth+1)

    # 自己相関の標準偏差と曲線下面積
    ac, ac_std, ac_auc = fff.AutocorStdAuc(v)
    # 自己相関関数の微分の標準偏差と曲線下面積
    diff, diff_std, diff_auc = fff.DifferStdAuc(v)

    # SRMR
    srmr_val, _ = srmr(v, fs)

    return [low_power, high_power, hlbr, coe1[0], coe1[1], coe3[0], coe3[1], coe3[2], coe3[3], ratio_max_to_10ms_ave_peaks, ratio_max_to_9th_ave_peaks, ac_std, ac_auc, diff_std, diff_auc, srmr_val]


def FetchFeaturesFromDataset(DATASET_PATH: str = '../../dataset'):
    '''
    データセットの音声データから特徴量を抽出する関数

    Parameters
    ----------
    DATASET_PATH : str, default '../dataset'
        datasetへのpath

    Returns
    -------
    None
    '''

    ####################
    ### 各種パラメータ ###
    ####################

    # 被験者
    participants = ['s' + str(i) for i in range(1, 11)]
    # 発言
    utterances = ['recording' + str(i) for i in range(2)]
    # セッション
    sessions = ['trial1', 'trial2']
    # 部屋
    rooms = ['upstairs', 'downstairs']
    # 設置場所
    placements = ['wall', 'nowall']
    # ユーザとの距離
    distances = [str(i) for i in range(1, 6, 2)]
    # 極座標
    positions = []
    for i, d in enumerate(['A', 'B', 'C']):
        for p in range(0, 3):
            positions.append(d + str(p) + '_' + str(2*i+1) + '_' + str(45*p))
    # DoV angles
    angles = [str(i) for i in range(0, 360, 45)]
    # マイクチャンネル
    mic_channels = range(1, 5)

    #########################
    ### 各種特徴量を取得する ###
    #########################

    # ファイルのフェッチ
    id = 0
    for participant_id in participants:
        first_dir_name = participant_id
        for room_id in rooms:
            for device_placement_id in placements:
                for session_id in sessions:
                    second_dir_name = participant_id + '_' + room_id + \
                        '_' + device_placement_id + '_' + session_id
                    for polar_position_id in positions:
                        third_dir_name = polar_position_id
                        for utterance_id in utterances:
                            for dov_angle in angles:
                                # idが13976以上で実行する
                                if(id < 13976):
                                    id += 4
                                    continue

                                # 特徴量をまとめる配列
                                rows = []
                                # 音声データを格納する
                                voices = []

                                # channel 0: 音声認識用に加工されている。channnel 5: 再生されたデータ→ch1~4を使用する
                                for mic_channel in mic_channels:
                                    filename = utterance_id + '_' + dov_angle + '_' + str(mic_channel) + '.wav'
                                    file_path = DATASET_PATH + '/' + first_dir_name + '/' + second_dir_name + '/' + third_dir_name + '/' + filename

                                    print(f'id: {id}, file path: {file_path}')

                                    # 音声データを読み込む
                                    v, fs = cis.wavread(file_path)
                                    voices.append([v, fs])

                                    # 音声ファイルの各種属性値を配列に格納する
                                    attr = [id, filename, participant_id, room_id, device_placement_id, session_id, polar_position_id, utterance_id, dov_angle, mic_channel]
                                    # 特徴量を得る
                                    # feature = FetchFeaturesFromMonoData(file_path)
                                    feature = FetchFeaturesFromMonoData(v, fs)
                                    # 属性情報と特徴量を合算->csvの1行分
                                    row = attr + feature
                                    
                                    # 配列に追加
                                    rows.append(row)

                                    id = id + 1
                                
                                # GCC-PHATの計算に使うためのマイクのペアを生成
                                mic_ch_pairs = itertools.combinations(mic_channels, 2)
                                n_mic_channels = len(mic_channels) # マイクチャンネル数
                                n_gp_tdoa_features = 4 # GCC-PHATとTDOAの処理で得られる
                                # GCC-PHATの特徴量の配列(mic_channels * (特徴数*チャンネル数)の配列を作成)
                                gp_tdoa_features = np.zeros((n_mic_channels, n_gp_tdoa_features * n_mic_channels))

                                for pair in mic_ch_pairs:
                                    # マイクのチャンネル
                                    mic_ch1 = pair[0]
                                    mic_ch2 = pair[1]
                                    # インデックスを計算（mic channelは1から始まる）
                                    ix1 = mic_ch1 - 1
                                    ix2 = mic_ch2 - 1
                                    # 音声データを取得
                                    v1 = voices[ix1][0]
                                    v2 = voices[ix2][0]
                                    # サンプリング周波数を取得
                                    fs = voices[ix1][1]

                                    # GCC-PHATとTDOAを計算
                                    gp_max_val, gp_max_ix, gp_auc, tdoa = fff.GetGccPhatAndTdoa(v1, v2, fs)

                                    # 配列に格納する
                                    for i, j in ((ix1, ix2), (ix2, ix1)):
                                        gp_tdoa_features[i][j * n_gp_tdoa_features] = gp_max_val
                                        gp_tdoa_features[i][j * n_gp_tdoa_features + 1] = gp_max_ix
                                        gp_tdoa_features[i][j * n_gp_tdoa_features + 2] = gp_auc
                                        gp_tdoa_features[i][j * n_gp_tdoa_features + 3] = tdoa

                                # rowsにgp_tdoa_featuresの内容を追加する
                                all_data = []
                                for i in range(n_mic_channels):
                                    data = np.hstack([rows[i], gp_tdoa_features[i]])
                                    all_data.append(data)

                                yield all_data
