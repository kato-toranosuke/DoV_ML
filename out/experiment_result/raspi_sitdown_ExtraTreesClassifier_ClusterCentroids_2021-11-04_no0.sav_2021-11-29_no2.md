# ExtraTreesClassifier_ClusterCentroids_2021-11-04_no0.sav
## Constants
- CSV_PATH = ../out/csv
- OUTPUT_PATH = ../out/experiment_result
- FEATURE_ATTRBS = ['low_power', 'high_power', 'hlbr', 'coe1[0]', 'coe1[1]', 'coe3[0]', 'coe3[1]', 'coe3[2]', 'coe3[3]', 'ratio_max_to_10ms_ave_peaks', 'ratio_max_to_9th_ave_peaks', 'ac_std', 'ac_auc', 'diff_std', 'diff_auc', 'srmr', 'gp_max_val_std', 'gp_max_val_range', 'gp_max_val_min', 'gp_max_val_max', 'gp_max_val_mean', 'gp_max_ix_std', 'gp_max_ix_range', 'gp_max_ix_min', 'gp_max_ix_max', 'gp_max_ix_mean', 'gp_auc_std', 'gp_auc_range', 'gp_auc_min', 'gp_auc_max', 'gp_auc_mean', 'tdoa_std', 'tdoa_range', 'tdoa_min', 'tdoa_max', 'tdoa_mean']
- LABEL_ATTRB = ['dov_angle']
- FACING_DOV_ANGLES = [0, 45, 315]
- NCV = 10
- SCORING = ['accuracy', 'balanced_accuracy', 'f1']
- REFIT_SCORING = balanced_accuracy
- PARAM_GRID = None
- DATASET_PATH = ../../experiment_dataset/2021-11-29_mac
- TRAIN_CSV_PATH = ../out/csv
- TEST_CSV_PATH = ../out/csv/experiment
- INPUT_PKL_PATH = ../out/ml_model_result
- OUTPUT_PKL_PATH = ../out/ml_model_fitting_result

## Loaded CSV
### Training Data
- hoge

### Test Data
- 2021-11-26_raspi_16000Hz_w1_N2^12_overlap80.csv

## Pkl File
../out/ml_model_fitting_result/ExtraTreesClassifier_ClusterCentroids_2021-11-04_no0.sav## Evaluation
- accuracy score: 0.4647887323943662
- balanced accuracy score: 0.5538720538720538
- f1 score: 0.5681818181818182
- confusion matrix:
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 8 | 36 |
| Actual Positive | 2 | 25 |

      