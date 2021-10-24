#!/usr/bin/env python3
# coding: utf-8

from sklearn.base import BaseEstimator, TransformerMixin
import pandas as pd
from typing import List
import numpy as np


class DataFrameSelector(BaseEstimator, TransformerMixin):
    '''
    DataFrameから、属性を選択し、Numpy Arrayへ変換する変換器。

    Attributes
    ----------
    attribute_names: array-like
      抽出する属性名のリスト
    '''

    def __init__(self, attribute_names: List) -> None:
        self.attribute_names = attribute_names

    def fit(self, X: pd.DataFrame, y=None):
        return self

    def transform(self, X: pd.DataFrame) -> np.ndarray:
        return X[self.attribute_names].to_numpy()


class ValueTransducer(BaseEstimator, TransformerMixin):
    '''
    True/Falseのラベル付けを行う。

    Attributes
    ----------
    vals: array-like
      Trueラベルに振り分ける正解値のリスト
    '''

    def __init__(self, vals) -> None:
        self.vals = vals

    def fit(self, X: np.ndarray, y=None):
        return self

    def transform(self, X: np.ndarray) -> np.ndarray:
        _X = []
        # Trueになる値->1, それ以外->0
        for val in self.vals:
            x_ = np.where(X == val, 1, 0)
            _X.append(x_)
        # ndarrayに変換
        _X = np.array(_X)

        # 1次元配列にまとめる
        label_list = []
        for i in range(len(X)):
            bool = _X[:, i].any()
            label_list.append(int(bool))
        # ndarrayに変換
        label_np = np.array(label_list)

        return label_np
