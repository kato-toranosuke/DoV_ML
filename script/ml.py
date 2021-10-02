#!/usr/bin/env python3
# coding: utf-8

import numpy as np
import pandas as pd
from typing import List, Any, Union, Dict
from sklearn.impute import SimpleImputer
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import MinMaxScaler
import pprint

##################################
### csvファイルからのデータ読み込み ###
##################################

CSV_PATH = "../out/csv/"


def CsvToDf(csv_list: List) -> pd.DataFrame:
    '''
    CSVファイルを読み込んで、DataFrameで返す。
    '''
    df = pd.concat([pd.read_csv(CSV_PATH + filename) for filename in csv_list])
    return df

########################################
### データを訓練データとテストデータに分割 ###
########################################


class DataFrameSelector(BaseEstimator, TransformerMixin):
    '''
    DataFrameから、属性を選択し、Numpy Arrayへ変換する変換器。
    '''

    def __init__(self, attribute_names: List) -> None:
        self.attribute_names = attribute_names

    def fit(self, X: pd.DataFrame, y=None):
        return self

    def transform(self, X: pd.DataFrame) -> np.ndarray:
        return X[self.attribute_names].to_numpy()


class ValueTransducer(BaseEstimator, TransformerMixin):
    '''
    値を他の値に変換する。
    '''

    def __init__(self, vals) -> None:
        self.vals = vals

    def fit(self, X: np.ndarray, y=None):
        return self

    def transform(self, X: np.ndarray) -> np.ndarray:
        X_ = []
        # Trueになる値->1, それ以外->0
        for val in self.vals:
            x_ = np.where(X == val, 1, 0)
            X_.append(x_)
        # ndarrayに変換
        X_ = np.array(X_)

        # 1次元配列にまとめる
        label_list = []
        for i in range(len(X)):
            bool = X_[:, i].any()
            label_list.append(int(bool))
        # ndarrayに変換
        label_np = np.array(label_list)

        return label_np

# 訓練

# テスト

# 評価


if __name__ == "__main__":
    # 読み込むCSVファイルのリスト
    csv_list = ["features_ch0.csv"]
    df = CsvToDf(csv_list)

    # session1のデータの抽出(式を評価するengineとしてnumexprを使用することで、処理の高速化を狙う。)
    train_set = df.query('session_id == "trial1"', engine='numexpr')
    test_set = df.query('session_id == "trial2"', engine='numexpr')

    # 特徴量に該当する列の抽出
    feature_attribs = ['low_power', 'high_power', 'hlbr', 'coe1[0]',	'coe1[1]', 'coe3[0]', 'coe3[1]', 'coe3[2]',	'coe3[3]', 'ratio_max_to_10ms_ave_peaks', 'ratio_max_to_9th_ave_peaks', 'ac_std', 'ac_auc', 'diff_std', 'diff_auc',	'srmr', 'gp_max_val_std',	'gp_max_val_range',
                       'gp_max_val_min',	'gp_max_val_max',	'gp_max_val_mean', 'gp_max_ix_std',	'gp_max_ix_range', 'gp_max_ix_min',	'gp_max_ix_max', 'gp_max_ix_mean', 'gp_auc_std', 'gp_auc_range', 'gp_auc_min', 'gp_auc_max', 'gp_auc_mean',	'tdoa_std', 'tdoa_range', 'tdoa_min', 'tdoa_max', 'tdoa_mean']

    # pipeline
    features_pipeline = Pipeline([
        ('selector', DataFrameSelector(feature_attribs)),
        ('imputer', SimpleImputer(strategy="median")),
        ('min_max_scaler', MinMaxScaler())
    ])
    train_X = features_pipeline.fit_transform(train_set)

    # 特徴量に該当する列の抽出
    # df_session1_features = train_set.loc[:, feature_attribs]
    # df_session2_features = test_set.loc[:, feature_attribs]

    # 正解値に該当する列の抽出
    # train_angle = train_set.loc[:, label_attrib]
    # test_angle = test_set.loc[:, label_attrib]

    # 正解値labelを生成するpipeline
    label_attrib = ['dov_angle']
    facing_dov_angles = [0, 45, 315]
    label_pipeline = Pipeline([
        ('selector', DataFrameSelector(label_attrib)),
        ('transducer', ValueTransducer(facing_dov_angles))
    ])
    train_label = label_pipeline.fit_transform(train_set)
    test_label = label_pipeline.fit_transform(test_set)
