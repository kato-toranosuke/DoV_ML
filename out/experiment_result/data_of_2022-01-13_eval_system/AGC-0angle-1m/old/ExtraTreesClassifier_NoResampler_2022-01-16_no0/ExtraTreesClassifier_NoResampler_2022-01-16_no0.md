# ExtraTreesClassifier_NoResampler_2022-01-16_no0
## Constants
- CSV_PATH = ../out/csv/experiment
- OUTPUT_PATH = ../out/experiment_result/data_of_2022-01-13_eval_system/AGC-0angle-1m
- FEATURE_ATTRBS = ['low_power', 'high_power', 'hlbr', 'coe1[0]', 'coe1[1]', 'coe3[0]', 'coe3[1]', 'coe3[2]', 'coe3[3]', 'ratio_max_to_10ms_ave_peaks', 'ratio_max_to_9th_ave_peaks', 'ac_std', 'ac_auc', 'diff_std', 'diff_auc', 'srmr', 'gp_max_val_std', 'gp_max_val_range', 'gp_max_val_min', 'gp_max_val_max', 'gp_max_val_mean', 'gp_max_ix_std', 'gp_max_ix_range', 'gp_max_ix_min', 'gp_max_ix_max', 'gp_max_ix_mean', 'gp_auc_std', 'gp_auc_range', 'gp_auc_min', 'gp_auc_max', 'gp_auc_mean', 'tdoa_std', 'tdoa_range', 'tdoa_min', 'tdoa_max', 'tdoa_mean']
- LABEL_ATTRB = ['facing']
- FACING_DOV_ANGLES = [1]
- NCV = 8
- SCORING = ['accuracy', 'balanced_accuracy', 'f1']
- REFIT_SCORING = balanced_accuracy
- PARAM_GRID = [{'est__n_estimators': range(50, 1001, 50), 'est__min_samples_split': [2, 5, 10], 'est__min_samples_leaf': [1, 5, 10], 'est__max_features': ['sqrt', 'log2', None], 'est__bootstrap': [False], 'est__n_jobs': [-1], 'est__random_state': [42], 'est__max_samples': [0.01, 0.5, 0.09]}, {'est__n_estimators': range(50, 1001, 50), 'est__min_samples_split': [2, 5, 10], 'est__min_samples_leaf': [1, 5, 10], 'est__max_features': ['sqrt', 'log2', None], 'est__bootstrap': [True], 'est__oob_score': [True, False], 'est__n_jobs': [-1], 'est__random_state': [42], 'est__max_samples': [0.01, 0.5, 0.09]}]
- HP_SET_SESSION = ['trial1', 'trial21']
- TRAIN_SET_SESSION = None
- TEST_SET_SESSION = None
- DISTANCE = [1]
- AGC_STATUS = ['AGC']

## Loaded CSV
- 2021-12-27_AGC.csv
- 2022-01-10_NoAGC.csv
- 2022-01-13_raspi_48000Hz_w1_N2^12_overlap80.csv

## Estimator
### Type
- resampler = NoResampler
- estimator = ExtraTreesClassifier

### Arguments for hyperparameter search
- resampler = NoResampler
- estimator = ExtraTreesClassifier
- param_grid = 
	- {'est__n_estimators': range(50, 1001, 50), 'est__min_samples_split': [2, 5, 10], 'est__min_samples_leaf': [1, 5, 10], 'est__max_features': ['sqrt', 'log2', None], 'est__bootstrap': [False], 'est__n_jobs': [-1], 'est__random_state': [42], 'est__max_samples': [0.01, 0.5, 0.09]}
	- {'est__n_estimators': range(50, 1001, 50), 'est__min_samples_split': [2, 5, 10], 'est__min_samples_leaf': [1, 5, 10], 'est__max_features': ['sqrt', 'log2', None], 'est__bootstrap': [True], 'est__oob_score': [True, False], 'est__n_jobs': [-1], 'est__random_state': [42], 'est__max_samples': [0.01, 0.5, 0.09]}

- scoring = ['accuracy', 'balanced_accuracy', 'f1']
- refit = balanced_accuracy
- cv = 8

### Parameters of the best estimator
#### The best hyper-parameters
- best_resampler

- best_estimator
	- base_estimator = ExtraTreeClassifier()
	- n_estimators = 100
	- estimator_params = ('criterion', 'max_depth', 'min_samples_split', 'min_samples_leaf', 'min_weight_fraction_leaf', 'max_features', 'max_leaf_nodes', 'min_impurity_decrease', 'random_state', 'ccp_alpha')
	- bootstrap = False
	- oob_score = False
	- n_jobs = -1
	- random_state = 42
	- verbose = 0
	- warm_start = False
	- class_weight = None
	- max_samples = 0.01
	- criterion = gini
	- max_depth = None
	- min_samples_split = 2
	- min_samples_leaf = 5
	- min_weight_fraction_leaf = 0.0
	- max_features = None
	- max_leaf_nodes = None
	- min_impurity_decrease = 0.0
	- ccp_alpha = 0.0
	- n_features_in_ = 36
	- n_outputs_ = 1
	- classes_ = [0 1]
	- n_classes_ = 2
	- base_estimator_ = ExtraTreeClassifier()

#### Importance of features
- gp_max_val_min = 0.2059980002474149
- gp_max_val_mean = 0.15759356347278572
- gp_auc_min = 0.15283596935747842
- gp_auc_mean = 0.12097919134344634
- gp_max_val_max = 0.07136480703234276
- gp_auc_max = 0.06876696797794733
- gp_auc_range = 0.02230075963845493
- hlbr = 0.019292811079597433
- diff_std = 0.018574846020083937
- gp_max_val_range = 0.017951979534805273
- high_power = 0.017638392748959397
- gp_auc_std = 0.01672458860015337
- diff_auc = 0.015451049730478538
- gp_max_val_std = 0.013363073410281949
- srmr = 0.01167217947260995
- gp_max_ix_range = 0.010003636650091878
- ratio_max_to_9th_ave_peaks = 0.009445363031430716
- coe1[0] = 0.005562741076231011
- ac_auc = 0.005104300719280884
- gp_max_ix_std = 0.004573335849280282
- tdoa_std = 0.004499386494097333
- coe3[2] = 0.004257194700721679
- coe1[1] = 0.003652042251315369
- coe3[3] = 0.0034892905904210358
- gp_max_ix_min = 0.0032849403043011148
- gp_max_ix_max = 0.003044078747339618
- tdoa_max = 0.0029507756406019054
- tdoa_range = 0.0028658267761699475
- ratio_max_to_10ms_ave_peaks = 0.0019788756442843413
- low_power = 0.0019256285710814083
- gp_max_ix_mean = 0.0013150104582125882
- tdoa_mean = 0.0005844155844155848
- ac_std = 0.0005437962202136403
- tdoa_min = 0.00041118102366942427
- coe3[0] = 0.0
- coe3[1] = 0.0

## Evaluation
cv = 8
### robot-1
#### accuracy
- Mean = 0.6933199317738792
- Standard deviation = 0.14827470372425847

#### f1
- Mean = 0.6933199317738792
- Standard deviation = 0.1482747037242585

#### precision
- Mean = 0.6933199317738792
- Standard deviation = 0.14827470372425847

#### recall
- Mean = 0.6933199317738792
- Standard deviation = 0.14827470372425847

#### facing_probas
- Mean = -100.0
- Standard deviation = 0.0

#### Confusion Matrix|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 0 | 0 |
| Actual Positive | 10 | 22 |

### robot-2
#### accuracy
- Mean = 0.6933199317738792
- Standard deviation = 0.14827470372425847

#### f1
- Mean = 0.6933199317738792
- Standard deviation = 0.1482747037242585

#### precision
- Mean = 0.6933199317738792
- Standard deviation = 0.14827470372425847

#### recall
- Mean = 0.6933199317738792
- Standard deviation = 0.14827470372425847

#### facing_probas
- Mean = -100.0
- Standard deviation = 0.0

#### Confusion Matrix|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 0 | 0 |
| Actual Positive | 10 | 22 |

### robot-3
#### accuracy
- Mean = 0.6933199317738792
- Standard deviation = 0.14827470372425847

#### f1
- Mean = 0.6933199317738792
- Standard deviation = 0.1482747037242585

#### precision
- Mean = 0.6933199317738792
- Standard deviation = 0.14827470372425847

#### recall
- Mean = 0.6933199317738792
- Standard deviation = 0.14827470372425847

#### facing_probas
- Mean = -100.0
- Standard deviation = 0.0

#### Confusion Matrix|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 0 | 0 |
| Actual Positive | 10 | 22 |

### robot-4
#### accuracy
- Mean = 0.6933199317738792
- Standard deviation = 0.14827470372425847

#### f1
- Mean = 0.6933199317738792
- Standard deviation = 0.1482747037242585

#### precision
- Mean = 0.6933199317738792
- Standard deviation = 0.14827470372425847

#### recall
- Mean = 0.6933199317738792
- Standard deviation = 0.14827470372425847

#### facing_probas
- Mean = -100.0
- Standard deviation = 0.0

#### Confusion Matrix|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 0 | 0 |
| Actual Positive | 10 | 22 |

### robot-5
#### accuracy
- Mean = 0.6933199317738792
- Standard deviation = 0.14827470372425847

#### f1
- Mean = 0.6933199317738792
- Standard deviation = 0.1482747037242585

#### precision
- Mean = 0.6933199317738792
- Standard deviation = 0.14827470372425847

#### recall
- Mean = 0.6933199317738792
- Standard deviation = 0.14827470372425847

#### facing_probas
- Mean = -100.0
- Standard deviation = 0.0

#### Confusion Matrix|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 0 | 0 |
| Actual Positive | 10 | 22 |

