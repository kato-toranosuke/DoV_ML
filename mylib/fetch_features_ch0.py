#!/usr/bin/env python3
# coding: utf-8

from . import fetch_features_func as fff
from .fft import fft
from . import cis
from typing import List, Any, Union, Dict
from srmrpy.srmr import *
import itertools
import numpy as np


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
    rows: array-like
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


def FetchFeaturesFromDataset(DATASET_PATH) -> List:
    '''
    データセットの音声データから特徴量を抽出する関数

    Parameters
    ----------
    DATASET_PATH : str
        datasetへのpath

    Returns
    -------
    all_data : array-like
        csvに出力するデータ
    '''

    ####################
    ### 各種パラメータ ###
    ####################

    # 被験者
    participant_ids = ['s' + str(i) for i in range(1, 11)]
    # 発言
    utterance_ids = ['recording' + str(i) for i in range(2)]
    # セッション
    session_ids = ['trial1', 'trial2']
    # 部屋
    room_ids = ['upstairs', 'downstairs']
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
    mic_ch_pairs = itertools.combinations(gp_tdoa_mic_channels, 2)

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
                    second_dir_name = participant_id + '_' + room_id + '_' + device_placement_id + '_' + session_id

                    for distance_ix, distance_id in enumerate(distance_ids):
                        for polar_angle_ix, polar_angle_id in enumerate(polar_angle_ids):
                            polar_position_id = distance_id + str(polar_angle_id)
                            distance = 2*distance_ix + 1
                            polar_angle = 45*polar_angle_ix
                            # 第3階層
                            third_dir_name = polar_position_id + '_' + distance + '_' + polar_angle

                            # 一度に書き込む行範囲（特徴量をまとめる配列）
                            rows = []

                            for utterance_id in utterance_ids:
                                for dov_angle in dov_angles:
                                    # idが42360以上で実行する
                                    # if(id < 42360):
                                    #     id += 1
                                    #     continue


                                    ###############
                                    ### 属性情報 ###
                                    ###############
                                    attr = [id, filename, participant_id, room_id, device_placement_id, session_id,
                                            polar_position_id, distance, polar_angle, utterance_id, dov_angle, mic_channel]

                                    ##########################
                                    ### GCC-PHAT & TDOA以外 ###
                                    ##########################

                                    # channel0のファイルパス
                                    filename = utterance_id + '_' + dov_angle + '_' + str(mic_channel) + '.wav'
                                    file_path = DATASET_PATH + '/' + first_dir_name + '/' + second_dir_name + '/' + third_dir_name + '/' + filename

                                    print(f'id: {id}, file path: {file_path}')

                                    # channel0の音声データを読み込む
                                    v, fs = cis.wavread(file_path)

                                    # 特徴量を得る
                                    features = FetchFeaturesFromMonoData(v, fs)

                                    #######################
                                    ### GCC-PHAT & TDOA ###
                                    #######################

                                    # channel1~4の音声データを読み込む
                                    voice_data = []
                                    for ch in gp_tdoa_mic_channels:
                                        fname = utterance_id + '_' + dov_angle + '_' + str(ch) + '.wav'
                                        fpath = DATASET_PATH + '/' + first_dir_name + '/' + second_dir_name + '/' + third_dir_name + '/' + fname
                                        v_, fs_ = cis.wavread(fpath)
                                        voice_data.append([v_, fs_])
                                    
                                    # GCC-PHATの特徴量を格納する配列を生成
                                    pair_gp_tdoa_features = []

                                    # 各ペアについて計算
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
                                        gp_max_val, gp_max_ix, gp_auc, tdoa = fff.GetGccPhatAndTdoa(v1, v2, fs)

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

                                    # 行情報を生成
                                    row = attr + features + gp_tdoa_features

                                    # 配列に追加
                                    rows.append(row)

                                    id = id + 1

                            # 第３階層以下のファイルについて計算が終われば、一旦出力する。
                            yield rows
