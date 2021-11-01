#!/usr/bin/env python3
# coding: utf-8

from typing import List, Union, Dict
from sklearn.ensemble import ExtraTreesClassifier, RandomForestClassifier
import datetime, os, re, joblib
from .load_constants import ML_Consts


class RecModelDataToMarkdown():
  def __init__(self, fname: str, consts: ML_Consts, csv_list: List, estimator, best_estimator, scores, conf_mat) -> None:
    self.fname = fname
    self.consts = consts
    self.csv_list = csv_list
    self.estimator = estimator
    self.best_estimator = best_estimator
    self.scores = scores
    self.conf_mat = conf_mat

  def RecModelDataToMarkdown(self):
    # 実行中のスクリプトの名前を取得
    dir_name = self.GetDirname(self.fname, self.consts.OUTPUT_PATH)
    output_dir_path = self.consts.OUTPUT_PATH + dir_name
    # 出力するデータを格納するディレクトリを作成
    os.mkdir(output_dir_path)

    # モデルの保存
    pkl_path = output_dir_path + "/" + dir_name + ".pkl"
    joblib.dump(self.best_estimator, pkl_path)

    # 結果ファイル
    result_file_path = output_dir_path + "/" + dir_name + ".md"
    with open(result_file_path, 'w') as f:
      output_str = '# ' + dir_name + '\n'
      # 定数の記録
      consts_str = "## Constants\n" + self.GetInstanceValStr(self.consts)
      # 読み込んだCSVファイル
      csv_str = '## Loaded CSV\n' + self.GetListStr(self.csv_list)
      # 推定器
      estimator_str = '## Estimator\n'
      estimator_str += '### Type\n'
      estimator_str += '- estimator = ' + self.estimator.__class__.__name__ + '\n'
      # Grid Search CV
      estimator_str += '### Arguments for hyperparameter search\n'
      estimator_str += '- estimator = ' + self.estimator.__class__.__name__ + '\n'
      estimator_str += '- param_grid = \n' + self.GetListStr(self.consts.PARAM_GRID, level=1)
      estimator_str += '- scoring = ' + str(self.consts.SCORING) + '\n'
      estimator_str += '- refit = ' + str(self.consts.REFIT_SCORING) + '\n'
      estimator_str += '- cv = ' + str(self.consts.NCV) + '\n'
      estimator_str += '\n'
      # Best Estimator(ベストハイパラ、特徴量の重要度)
      estimator_str += '### Parameters of the best estimator\n'
      estimator_str += '#### The best hyper-parameters\n'
      estimator_str += self.GetDictStr(self.best_estimator.__dict__, level=0)
      estimator_str += '#### Importance of features\n'
      feature_importance = self.GetFeaturesImportance(self.best_estimator, self.consts.FEATURE_ATTRBS)
      estimator_str += self.GetDictStr(feature_importance, level=0)

      # 評価
      evaluation_str = '## Evaluation\n'
      evaluation_str += 'cv = ' + str(self.consts.NCV) + '\n'
      evaluation_str += self.GetEvaluationScore(self.scores, self.consts.SCORING)
      evaluation_str += '### Confusion Matrix\n'
      evaluation_str += f"""\
        |  | Predicted Negative | Predicted Positive |
        | Actual Negative | {self.conf_mat[0][0]} | {self.conf_mat[0][1]} |
        | Actual Positive | {self.conf_mat[1][0]} | {self.conf_mat[1][1]} |

      """

      output_str += (consts_str + csv_str + estimator_str + evaluation_str)

      f.writelines(output_str)

    print(f'Complete!\nResult file is {result_file_path}')


  def GetInstanceValStr(self, inst) -> str:
    output_str = ''
    output_str += self.GetDictStr(inst.__dict__)
    return output_str


  def GetDictStr(self, dict: Dict, level: int = 0) -> str:
    prefix = '\t' * level
    output_str = ''
    for key, val in dict.items():
      if key == 'estimators_':
        _val = '\n'
        _val += self.GetListStr(val, level=1)
        val = _val

      output_str += prefix + '- ' + key + ' = ' + str(val) + '\n'
    output_str += '\n'
    return output_str


  def GetListStr(self, list: List, level: int = 0) -> str:
    prefix = '\t' * level
    output_str = ''
    for item in list:
      output_str += prefix + '- ' + str(item) + '\n'
    output_str += '\n'
    return output_str


  def GetDirname(self, fname: str, output_path: str) -> str:
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
    # resultディレクトリに同一日時のディレクトリがいくつあるか
    dirs_list = os.listdir(output_path)
    no = 0
    regex = re.compile(r'.*' + re.escape(d_today) + r'.*')
    for dir_name in dirs_list:
      is_match = regex.match(dir_name)
      if is_match != None:
        no += 1

    dir_name = fname + '_' + d_today + '_no' + str(no)
    return dir_name


  def GetFeaturesImportance(self, model: Union[ExtraTreesClassifier, RandomForestClassifier], feature_attrbs: List) -> Dict:    
    feature_score = {}
    for name, score in zip(feature_attrbs, model.feature_importances_):
      feature_score[name] = score

    # sort
    feature_score_sorted_tuple = sorted(
        feature_score.items(), key=lambda x: x[1], reverse=True)
    # 辞書型に変換
    feature_score_sorted_dict = {}
    for t in feature_score_sorted_tuple:
      feature_score_sorted_dict[t[0]] = t[1]

    return feature_score_sorted_dict


  def GetEvaluationScore(self, scores: List, metrics: List, level=3) -> str:
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

      score_str = '[ '
      score_str += ', '.join([str(s) for s in score])
      score_str += ' ]'

      score_dict = {
          'Scores': score_str,
          'Mean': score.mean(),
          'Standard deviation': score.std()
      }
      output_str += (prefix + ' ' + metric + '\n')
      output_str += self.GetDictStr(score_dict)

    return output_str

class RecModelDataToMdWithResampler(RecModelDataToMarkdown):
  def __init__(self, consts: ML_Consts, csv_list: List, best_resampler, best_estimator, scores, conf_mat) -> None:
      self.consts = consts
      self.csv_list = csv_list
      self.best_resampler = best_resampler
      self.best_estimator = best_estimator
      self.scores = scores
      self.conf_mat = conf_mat

  def write(self):
    # 実行中のスクリプトの名前を取得
    dir_name = self.GetDirname(self.consts.OUTPUT_PATH, self.best_estimator, self.best_resampler)
    output_dir_path = self.consts.OUTPUT_PATH + dir_name
    # 出力するデータを格納するディレクトリを作成
    os.mkdir(output_dir_path)

    # モデルの保存
    pkl_path = output_dir_path + "/" + dir_name + ".pkl"
    joblib.dump(self.best_estimator, pkl_path)

    # 結果ファイル
    result_file_path = output_dir_path + "/" + dir_name + ".md"
    with open(result_file_path, 'w') as f:
      output_str = '# ' + dir_name + '\n'
      # 定数の記録
      consts_str = "## Constants\n" + self.GetInstanceValStr(self.consts)
      # 読み込んだCSVファイル
      csv_str = '## Loaded CSV\n' + self.GetListStr(self.csv_list)
      # 推定器
      estimator_str = '## Estimator\n'
      estimator_str += '### Type\n'
      estimator_str += '- resampler = ' + self.best_resampler.__class__.__name__ + '\n'
      estimator_str += '- estimator = ' + self.best_estimator.__class__.__name__ + '\n'
      estimator_str += '\n'
      # Grid Search CV
      estimator_str += '### Arguments for hyperparameter search\n'
      estimator_str += '- resampler = ' + self.best_resampler.__class__.__name__ + '\n'
      estimator_str += '- estimator = ' + self.best_estimator.__class__.__name__ + '\n'
      estimator_str += '- param_grid = \n' + self.GetListStr(self.consts.PARAM_GRID, level=1)
      estimator_str += '- scoring = ' + str(self.consts.SCORING) + '\n'
      estimator_str += '- refit = ' + str(self.consts.REFIT_SCORING) + '\n'
      estimator_str += '- cv = ' + str(self.consts.NCV) + '\n'
      estimator_str += '\n'
      # Best Estimator(ベストハイパラ、特徴量の重要度)
      estimator_str += '### Parameters of the best estimator\n'
      estimator_str += '#### The best hyper-parameters\n'
      estimator_str += '- best_resampler\n'
      estimator_str += self.GetDictStr(self.best_resampler.__dict__, level=1)
      estimator_str += '- best_estimator\n'
      estimator_str += self.GetDictStr(self.best_estimator.__dict__, level=1)
      estimator_str += '#### Importance of features\n'
      feature_importance = self.GetFeaturesImportance(self.best_estimator, self.consts.FEATURE_ATTRBS)
      estimator_str += self.GetDictStr(feature_importance, level=0)

      # 評価
      evaluation_str = '## Evaluation\n'
      evaluation_str += 'cv = ' + str(self.consts.NCV) + '\n'
      evaluation_str += self.GetEvaluationScore(self.scores, self.consts.SCORING)
      evaluation_str += '### Confusion Matrix\n'
      evaluation_str += f"""\
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | {self.conf_mat[0][0]} | {self.conf_mat[0][1]} |
| Actual Positive | {self.conf_mat[1][0]} | {self.conf_mat[1][1]} |

      """

      output_str += (consts_str + csv_str + estimator_str + evaluation_str)

      f.writelines(output_str)

    print(f'Complete!\nResult file is {result_file_path}')

  def GetDictStr(self, dict: Dict, level: int = 0) -> str:
    prefix = '\t' * level
    output_str = ''
    for key, val in dict.items():
      if key == 'estimators_':
        continue
      output_str += prefix + '- ' + key + ' = ' + str(val) + '\n'
    output_str += '\n'
    return output_str

  def GetDirname(self, output_path, estimator, resampler) -> str:
    # 現在日時
    d_today = datetime.date.today().isoformat()
    # 実行中のスクリプトの名前を取得
    # resultディレクトリに同一日時のディレクトリがいくつあるか
    dirs_list = os.listdir(output_path)
    no = 0
    regex = re.compile(r'.*' + re.escape(d_today) + r'.*')
    for dir_name in dirs_list:
      is_match = regex.match(dir_name)
      if is_match != None:
        no += 1

    est_str = estimator.__class__.__name__
    resmp_str = resampler.__class__.__name__

    dir_name = est_str + '_' + resmp_str + '_' + d_today + '_no' + str(no)
    return dir_name
