#!/usr/bin/env python3
# coding: utf-8

import numpy as np
from scipy import signal
from scipy import fftpack
import numba as nb

# 型ヒントのサポート
from typing import List, Any, Union, Dict


# @nb.jit(nopython=True, parallel=True, cache=True)
def ov(data: List[float], fs: int, N: int, overlap: Union[int, float]) -> List and int:
    '''
    オーバーラップ処理を行う関数。

    Parameters
    ----------
    data : array-like
      音声データ
    fs : int
      サンプリング周波数
    N : int
      フレームサイズ
    overlap : int or float
      オーバーラップ率[%]

    Returns
    -------
    array : array-like
      オーバーラップ抽出されたデータ配列
    N_ave : int
      データの個数

    '''

    Ts = len(data) / fs  # 全データ長[sec]
    Fc = N / fs  # フレーム周期[sec]
    x_ol = N * (1 - (overlap/100))  # オーバーラップ時のフレームずらし幅

    # 抽出するフレーム数（平均化に使うデータ個数）
    # Fc*(1-(overlap/100) : フレームずらし幅に相当する秒数
    N_ave = int((Ts - (Fc * (overlap/100))) / (Fc * (1-(overlap/100))))

    array = []  # 抽出したデータを入れる空配列の定義

    # forループでデータを抽出
    for i in nb.prange(N_ave):
        ps = int(x_ol * i)  # 切り出し位置をループ毎に更新
        array.append(data[ps:ps+N:1])  # 切り出し位置psからフレームサイズ分抽出して配列に追加

    return array, N_ave  # オーバーラップ抽出されたデータ配列とデータ個数を戻り値にする


# @nb.jit(parallel=True, cache=True)
def hanning(data_array: List, N: int, N_ave: int) -> List and float:
    '''
    窓関数処理（ハニング窓）を行う関数。

    Parameters
    ----------
    data_array : array-like
      フレームデータ
    N : int
      フレームサイズ
    N_ave : int
      処理対象のフレームの数

    Returns
    -------
    data_array : array-like
      音声データ
    acf : float
      振幅補正係数(Amplitude Correction Factor)

    '''

    han = signal.hann(N)  # ハニング窓作成
    acf = 1 / (sum(han) / N)  # 振幅補正係数(Amplitude Correction Factor)

    # オーバーラップされた複数時間波形全てに窓関数をかける
    for i in nb.prange(N_ave):
        data_array[i] = data_array[i] * han  # 窓関数をかける

    return data_array, acf


# @nb.jit(parallel=True, cache=True)
def fft_ave(data_array: List, fs: int, N: int, N_ave: int, acf: float):
    '''
    平均化FFT処理を行う関数。

    Parameters
    ----------
    data_array : array-like
      フレームデータ
    fs : int
      サンプリング周波数
    N : int
      フレームサイズ
    N_ave : int
      フレームの数
    acf : float
      振幅補正係数(Amplitude Correction Factor)

    Returns
    -------
    fft_array : array-like
      FFTの振幅レベル
    fft_mean : array-like
      平均化したFFTの振幅レベル
    fft_axis : array-like
      周波数軸
    '''

    fft_array = []
    for i in range(N_ave):
        # FFTをして配列に追加、窓関数補正値をかけ、(N/2)の正規化を実施。
        fft_array.append(acf*np.abs(fftpack.rfft(data_array[i])/(N/2)))

    fft_axis = np.linspace(0, fs, N)  # 周波数軸を作成
    fft_array = np.array(fft_array)  # 型をndarrayに変換
    # 全てのFFT波形のパワー平均を計算してから振幅値とする
    fft_mean = np.sqrt(np.mean(fft_array ** 2, axis=0))

    return fft_array, fft_mean, fft_axis
