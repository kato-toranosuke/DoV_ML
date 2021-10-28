#!/usr/bin/env python3
# coding: utf-8

from typing import List, Union, Dict
from sklearn.ensemble import ExtraTreesClassifier, RandomForestClassifier
import datetime, os, re

def GetInstanceValStr(inst) -> str:
  output_str = ''
  output_str += GetDictStr(inst.__dict__)
  return output_str

def GetDictStr(dict: Dict, level: int=0) -> str:
  prefix = '\t' * level
  output_str = ''
  for key, val in dict.items():
    output_str += prefix + '- ' + key + ' = ' + str(val) + '\n'
  output_str += '\n'
  return output_str

def GetListStr(list: List, level: int = 0) -> str:
  prefix = '\t' * level
  output_str = ''
  for item in list:
    output_str += prefix + '- ' + str(item) + '\n'
  output_str += '\n'
  return output_str

def GetDirname(fname: str, output_path: str) -> str:
  '''
  結果を出力するディレクトリ名を生成

  Parameters
  ----------
  fname: str
    実行中のスクリプトのファイル名
  output_path: str
    結果のファイルを出力するディレクトリのパス
  '''
  # 現在日時
  d_today = datetime.date.today().isoformat()
  # 実行中のスクリプトの名前を取得
  # fname = os.path.basename(__file__)
  # resultディレクトリに同一日時のディレクトリがいくつあるか
  dirs_list = os.listdir(output_path)
  no = 0
  regex = re.compile(r'^' + re.escape(d_today) + r'.*')
  for dir_name in dirs_list:
    is_match = regex.match(dir_name)
    if is_match != None:
      no += 1

  dir_name = d_today + '_no' + str(no) + '_' + fname
  return dir_name

def GetFeaturesImportance(model: Union[ExtraTreesClassifier, RandomForestClassifier], feature_attrbs: List) -> Dict:
  feature_score = {}
  for name, score in zip(feature_attrbs, model.feature_importances_):
    feature_score[name] = score
  
  # sort
  feature_score_sorted_tuple = sorted(feature_score.items(), key=lambda x:x[1], reverse=True)
  # 辞書型に変換
  feature_score_sorted_dict = {}
  for t in feature_score_sorted_tuple:
    feature_score_sorted_dict[t[0]] = t[1]

  return feature_score_sorted_dict  

def GetEvaluationScore(scores: List, metrics: List, level=3) -> str:
  '''
  評価の結果を文字列で返す。

  Parameters
  ----------
  score: array-like
    各種スコアが格納された配列
  metrics: array-like
    評価指標

  Returns
  -------
  output_str: str
    結果ファイル用の文字列
  '''
  output_str = ""
  prefix = '#' * level

  for metric in metrics:
    index = 'test_' + metric
    score = scores[index]
    score_dict = {
      'Scores': score,
      'Mean': score.mean(),
      'Standard deviation': score.std()
    }
    print(score)
    output_str += (prefix + ' ' + metric + '\n')
    output_str += GetDictStr(score_dict)

  return output_str
  
