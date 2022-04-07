#!/usr/bin/env python3
# coding: utf-8

class ML_Consts():
    '''
    機械学習に用いる定数を定義するクラス
    '''

    def __init__(self, csv_path="../out/csv", output_path="../out/ml_model_result", feature_attrbs=['low_power', 'high_power', 'hlbr', 'coe1[0]', 'coe1[1]', 'coe3[0]', 'coe3[1]', 'coe3[2]', 'coe3[3]', 'ratio_max_to_10ms_ave_peaks', 'ratio_max_to_9th_ave_peaks', 'ac_std', 'ac_auc', 'diff_std', 'diff_auc', 'srmr', 'gp_max_val_std', 'gp_max_val_range', 'gp_max_val_min', 'gp_max_val_max', 'gp_max_val_mean', 'gp_max_ix_std', 'gp_max_ix_range', 'gp_max_ix_min', 'gp_max_ix_max', 'gp_max_ix_mean', 'gp_auc_std', 'gp_auc_range', 'gp_auc_min', 'gp_auc_max', 'gp_auc_mean', 'tdoa_std', 'tdoa_range', 'tdoa_min', 'tdoa_max', 'tdoa_mean'], label_attrb=['dov_angle'], facing_dov_angles=[0, 45, 315], ncv=10, scoring=['accuracy', 'balanced_accuracy', 'f1'], refit_scoring='balanced_accuracy', param_grid=None, train_set_session=['trial1'], test_set_session=['trial2'], distance=['AGC'], agc_status=[1, 3, 5]):
        # インスタンス変数
        self.CSV_PATH = csv_path
        self.OUTPUT_PATH = output_path
        self.FEATURE_ATTRBS = feature_attrbs
        self.LABEL_ATTRB = label_attrb
        self.FACING_DOV_ANGLES = facing_dov_angles
        self.NCV = ncv
        self.SCORING = scoring
        self.REFIT_SCORING = refit_scoring
        self.PARAM_GRID = param_grid
        self.TRAIN_SET_SESSION = train_set_session
        self.TEST_SET_SESSION = test_set_session
        self.DISTANCE = distance
        self.AGC_STATUS = agc_status

class Eval_Sys_Consts():
    '''
    機械学習に用いる定数を定義するクラス
    '''

    def __init__(self, csv_path="../out/csv", output_path="../out/ml_model_result", feature_attrbs=['low_power', 'high_power', 'hlbr', 'coe1[0]', 'coe1[1]', 'coe3[0]', 'coe3[1]', 'coe3[2]', 'coe3[3]', 'ratio_max_to_10ms_ave_peaks', 'ratio_max_to_9th_ave_peaks', 'ac_std', 'ac_auc', 'diff_std', 'diff_auc', 'srmr', 'gp_max_val_std', 'gp_max_val_range', 'gp_max_val_min', 'gp_max_val_max', 'gp_max_val_mean', 'gp_max_ix_std', 'gp_max_ix_range', 'gp_max_ix_min', 'gp_max_ix_max', 'gp_max_ix_mean', 'gp_auc_std', 'gp_auc_range', 'gp_auc_min', 'gp_auc_max', 'gp_auc_mean', 'tdoa_std', 'tdoa_range', 'tdoa_min', 'tdoa_max', 'tdoa_mean'], label_attrb=['dov_angle'], facing_dov_angles=[0, 45, 315], ncv=10, scoring=['accuracy', 'balanced_accuracy', 'f1'], refit_scoring='balanced_accuracy', param_grid=None, hp_set_session=[], train_set_session=['trial1'], test_set_session=['trial2'], distance=['AGC'], agc_status=[1, 3, 5]):
        # インスタンス変数
        self.CSV_PATH = csv_path
        self.OUTPUT_PATH = output_path
        self.FEATURE_ATTRBS = feature_attrbs
        self.LABEL_ATTRB = label_attrb
        self.FACING_DOV_ANGLES = facing_dov_angles
        self.NCV = ncv
        self.SCORING = scoring
        self.REFIT_SCORING = refit_scoring
        self.PARAM_GRID = param_grid
        self.HP_SET_SESSION = hp_set_session
        self.TRAIN_SET_SESSION = train_set_session
        self.TEST_SET_SESSION = test_set_session
        self.DISTANCE = distance
        self.AGC_STATUS = agc_status


class Exp_Consts(ML_Consts):
    '''
    機械学習に用いる定数を定義するクラス

    Attributes
    ----------
    FITTIG_PKL_PATH : str
        Modelに訓練データをfittingした結果を保存したpklファイルが格納されているディレクトリへのパス
    '''

    def __init__(self, input_pkl_path='../out/ml_model_result', output_pkl_path='../out/ml_model_fitting_result', dataset_path='../../experiment_dataset/2021-11-19', train_csv_path='../out/csv', test_csv_path='../out/csv/experiment', output_path="../out/experiment_result", csv_path="../out/csv", feature_attrbs=['low_power', 'high_power', 'hlbr', 'coe1[0]', 'coe1[1]', 'coe3[0]', 'coe3[1]', 'coe3[2]', 'coe3[3]', 'ratio_max_to_10ms_ave_peaks', 'ratio_max_to_9th_ave_peaks', 'ac_std', 'ac_auc', 'diff_std', 'diff_auc', 'srmr', 'gp_max_val_std', 'gp_max_val_range', 'gp_max_val_min', 'gp_max_val_max', 'gp_max_val_mean', 'gp_max_ix_std', 'gp_max_ix_range', 'gp_max_ix_min', 'gp_max_ix_max', 'gp_max_ix_mean', 'gp_auc_std', 'gp_auc_range', 'gp_auc_min', 'gp_auc_max', 'gp_auc_mean', 'tdoa_std', 'tdoa_range', 'tdoa_min', 'tdoa_max', 'tdoa_mean'], label_attrb=['dov_angle'], facing_dov_angles=[0, 45, 315], ncv=10, scoring=['accuracy', 'balanced_accuracy', 'f1'], refit_scoring='balanced_accuracy', param_grid=None):
        # インスタンス変数
        super().__init__(csv_path, output_path, feature_attrbs, label_attrb,
                         facing_dov_angles, ncv, scoring, refit_scoring, param_grid)
        self.DATASET_PATH = dataset_path
        self.TRAIN_CSV_PATH = train_csv_path
        self.TEST_CSV_PATH = test_csv_path
        self.INPUT_PKL_PATH = input_pkl_path
        self.OUTPUT_PKL_PATH = output_pkl_path
