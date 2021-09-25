#!/usr/bin/env python3
# coding: utf-8

import fft_func
import numpy as np
import math
from typing import List, Any, Union, Dict


def fft(data: List, fs: int, N: Union[str, int] = "full", overlap: Union[int, float] = 0) -> List:
    '''
    FFT処理を行う関数。

    Parameters
    ----------
    data : array-like
      音声データ
    fs : int
      サンプリング周波数
    N : str or int, default "full"
      フレームサイズ
    overlap : int or float, default 0
      オーバーラップ率[%]

    Returns
    -------
    fft_array : array-like
      FFTの振幅レベル
    fft_mean : array-like
      平均化したFFTの振幅レベル
    fft_axis : array-like
      周波数軸
    '''
    # フレームサイズを求める（FFTの点数）
    if N == "full":
        l = len(data)
        ex = math.floor(math.log2(l))
        N = 2**ex
        overlap = 0

    # オーバーラップ抽出を行い、時間波形配列を得る。
    time_array, N_ave = fft_func.ov(data, fs, N, overlap)

    # ハニング窓関数をかける
    time_array, acf = fft_func.hanning(time_array, N, N_ave)

    # 平均化FFT処理を行う
    fft_array, fft_mean, fft_axis = fft_func.fft_ave(
        time_array, fs, N, N_ave, acf)

    return fft_array, fft_mean, fft_axis
