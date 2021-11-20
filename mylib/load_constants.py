#!/usr/bin/env python3
# coding: utf-8

class ML_Consts():
    '''
    機械学習に用いる定数を定義するクラス
    '''

    def __init__(self, csv_path="../out/csv/", output_path="../out/ml_model_result/", feature_attrbs=['low_power', 'high_power', 'hlbr', 'coe1[0]', 'coe1[1]', 'coe3[0]', 'coe3[1]', 'coe3[2]', 'coe3[3]', 'ratio_max_to_10ms_ave_peaks', 'ratio_max_to_9th_ave_peaks', 'ac_std', 'ac_auc', 'diff_std', 'diff_auc', 'srmr', 'gp_max_val_std', 'gp_max_val_range', 'gp_max_val_min', 'gp_max_val_max', 'gp_max_val_mean', 'gp_max_ix_std', 'gp_max_ix_range', 'gp_max_ix_min', 'gp_max_ix_max', 'gp_max_ix_mean', 'gp_auc_std', 'gp_auc_range', 'gp_auc_min', 'gp_auc_max', 'gp_auc_mean', 'tdoa_std', 'tdoa_range', 'tdoa_min', 'tdoa_max', 'tdoa_mean'], label_attrb=['dov_angle'], facing_dov_angles=[0, 45, 315], ncv=10, scoring=['accuracy', 'balanced_accuracy', 'f1'], refit_scoring='balanced_accuracy', param_grid=None, dataset_path=None):
        # インスタンス変数
        self.DATASET_PATH = dataset_path
        self.CSV_PATH = csv_path
        self.OUTPUT_PATH = output_path
        self.FEATURE_ATTRBS = feature_attrbs
        self.LABEL_ATTRB = label_attrb
        self.FACING_DOV_ANGLES = facing_dov_angles
        self.NCV = ncv
        self.SCORING = scoring
        self.REFIT_SCORING = refit_scoring
        self.PARAM_GRID = param_grid
