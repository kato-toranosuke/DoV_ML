#!/usr/bin/env python3
# coding: utf-8

import pandas as pd
from typing import List

def CsvToDf(csv_list: List, CSV_PATH: str) -> pd.DataFrame:
    df = pd.concat([pd.read_csv(CSV_PATH + '/' + filename)
                   for filename in csv_list])
    return df
