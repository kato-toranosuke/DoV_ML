# !/usr/bin/env python3
# coding: utf-8

import cis
import sys, os
# 自作ライブラリのパス追加
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from mylib import fetch_features_func as fff

v, fs = cis.wavread(
    "../dataset/s10/s10_downstairs_wall_trial2/C1_5_45/recording1_45_0.wav")

ratio, all_ix, max_ix = fff.GetRatioMaxToOtherAvePeaks(v, 3, fs, 0.01)

all_ix_list = list(all_ix)
tix = all_ix_list.index(max_ix)
print(tix)
print(all_ix[tix-100:tix+100])
