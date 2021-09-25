#!/usr/bin/env python3
# coding: utf-8

from mylib import fft
import csv
import sys
import os
from typing import List, Any, Union, Dict

# 自作ライブラリのパス追加
sys.path.append('..')

# 出力ファイルへのパス
OUTPUT_PATH = "../out/"


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
        header = ['id', 'filename', 'participant',
                  'utterance', 'session', 'room', 'placement', 'distance', 'position', 'angle', 'channel']
        writer.writerow(header)


if __name__ == '__main__':
    if len(sys.argv) > 1:
        filename = sys.argv[1]
        createCsv(filename)
    else:
        createCsv()
