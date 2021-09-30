#!/usr/bin/env python3
# coding: utf-8

import pandas as pd
from typing import List, Any, Union, Dict

##################################
### csvファイルからのデータ読み込み ###
##################################

CSV_PATH = "../out/csv/"

def CsvToDf(csv_list: List) -> pd.DataFrame:
  df = pd.concat([pd.read_csv(CSV_PATH + filename) for filename in csv_list])
  return df

# データを訓練データとテストデータに分割

# 訓練

# テスト

if __name__ == "__main__":
  # 読み込むCSVファイルのリスト
  csv_list = ["features_ch0.csv"]
  df = CsvToDf(csv_list)
  print(df)
