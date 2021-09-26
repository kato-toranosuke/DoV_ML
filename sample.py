#!/usr/bin/env python3
# coding: utf-8

import numpy as np

rows = np.zeros((4, 4))
add = np.ones((4, 1))

rows.tolist()
add.tolist()

for i in range(len(rows)):
  # print(np.hstack([rows[i], add[i]]))
  print(rows[i] + add[i])