# ExtraTreesClassifier_RandomUnderSampler_2022-04-13-17-18_no2
## Constants
- CSV_PATH = ../out/csv/experiment
- OUTPUT_PATH = ../out/experiment_result/data_of_2022-03-23_eval_system/AGC-15deg-0angle-1m
- FEATURE_ATTRBS = ['low_power', 'high_power', 'hlbr', 'coe1[0]', 'coe1[1]', 'coe3[0]', 'coe3[1]', 'coe3[2]', 'coe3[3]', 'ratio_max_to_10ms_ave_peaks', 'ratio_max_to_9th_ave_peaks', 'ac_std', 'ac_auc', 'diff_std', 'diff_auc', 'srmr', 'gp_max_val_std', 'gp_max_val_range', 'gp_max_val_min', 'gp_max_val_max', 'gp_max_val_mean', 'gp_max_ix_std', 'gp_max_ix_range', 'gp_max_ix_min', 'gp_max_ix_max', 'gp_max_ix_mean', 'gp_auc_std', 'gp_auc_range', 'gp_auc_min', 'gp_auc_max', 'gp_auc_mean', 'tdoa_std', 'tdoa_range', 'tdoa_min', 'tdoa_max', 'tdoa_mean']
- LABEL_ATTRB = ['facing']
- FACING_DOV_ANGLES = [1]
- NCV = 8
- SCORING = ['accuracy', 'balanced_accuracy', 'f1']
- REFIT_SCORING = balanced_accuracy
- PARAM_GRID = [{'est__n_estimators': range(10, 400, 20), 'est__min_samples_split': [2, 5, 10], 'est__min_samples_leaf': [1, 5, 10], 'est__max_features': ['sqrt', 'log2', None], 'est__bootstrap': [False], 'est__n_jobs': [-1], 'est__random_state': [42], 'est__max_samples': [0.01, 0.5, 0.09]}, {'est__n_estimators': range(10, 400, 20), 'est__min_samples_split': [2, 5, 10], 'est__min_samples_leaf': [1, 5, 10], 'est__max_features': ['sqrt', 'log2', None], 'est__bootstrap': [True], 'est__oob_score': [True, False], 'est__n_jobs': [-1], 'est__random_state': [42], 'est__max_samples': [0.01, 0.5, 0.09]}]
- HP_SET_SESSION = ['trial1', 'trial21']
- TRAIN_SET_SESSION = None
- TEST_SET_SESSION = None
- DISTANCE = [1]
- AGC_STATUS = ['AGC-15deg']
- ANGLES = [60, 75, 90, 105, 120]

## Loaded CSV
- 2022-03-23_raspi_48000Hz_w1_N2^12_overlap80_all.csv

## Estimator
### Type
- resampler = RandomUnderSampler
- estimator = ExtraTreesClassifier

### Arguments for hyperparameter search
- resampler = RandomUnderSampler
- estimator = ExtraTreesClassifier
- param_grid = 
	- {'est__n_estimators': range(10, 400, 20), 'est__min_samples_split': [2, 5, 10], 'est__min_samples_leaf': [1, 5, 10], 'est__max_features': ['sqrt', 'log2', None], 'est__bootstrap': [False], 'est__n_jobs': [-1], 'est__random_state': [42], 'est__max_samples': [0.01, 0.5, 0.09]}
	- {'est__n_estimators': range(10, 400, 20), 'est__min_samples_split': [2, 5, 10], 'est__min_samples_leaf': [1, 5, 10], 'est__max_features': ['sqrt', 'log2', None], 'est__bootstrap': [True], 'est__oob_score': [True, False], 'est__n_jobs': [-1], 'est__random_state': [42], 'est__max_samples': [0.01, 0.5, 0.09]}

- scoring = ['accuracy', 'balanced_accuracy', 'f1']
- refit = balanced_accuracy
- cv = 8

### Parameters of the best estimator
#### The best hyper-parameters
- best_resampler
	- sampling_strategy = auto
	- random_state = 42
	- replacement = False
	- n_features_in_ = 36
	- sampling_strategy_ = OrderedDict([(0, 3)])
	- sample_indices_ = [13 12  3  0  1  2]

- best_estimator
	- base_estimator = ExtraTreeClassifier()
	- n_estimators = 10
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
	- min_samples_leaf = 1
	- min_weight_fraction_leaf = 0.0
	- max_features = sqrt
	- max_leaf_nodes = None
	- min_impurity_decrease = 0.0
	- ccp_alpha = 0.0
	- n_features_in_ = 36
	- n_outputs_ = 1
	- classes_ = [0 1]
	- n_classes_ = 2
	- base_estimator_ = ExtraTreeClassifier()

#### Importance of features
- gp_max_val_range = 0.1
- gp_auc_min = 0.1
- gp_auc_max = 0.1
- gp_auc_mean = 0.1
- tdoa_min = 0.1
- gp_max_ix_range = 0.06666666666666667
- low_power = 0.05
- coe1[1] = 0.05
- coe3[2] = 0.05
- diff_auc = 0.05
- gp_max_val_mean = 0.05
- gp_max_ix_std = 0.05
- gp_max_ix_mean = 0.05
- ratio_max_to_9th_ave_peaks = 0.03333333333333333
- ac_std = 0.03333333333333333
- gp_max_val_std = 0.016666666666666666
- high_power = 0.0
- hlbr = 0.0
- coe1[0] = 0.0
- coe3[0] = 0.0
- coe3[1] = 0.0
- coe3[3] = 0.0
- ratio_max_to_10ms_ave_peaks = 0.0
- ac_auc = 0.0
- diff_std = 0.0
- srmr = 0.0
- gp_max_val_min = 0.0
- gp_max_val_max = 0.0
- gp_max_ix_min = 0.0
- gp_max_ix_max = 0.0
- gp_auc_std = 0.0
- gp_auc_range = 0.0
- tdoa_std = 0.0
- tdoa_range = 0.0
- tdoa_max = 0.0
- tdoa_mean = 0.0

## Evaluation
cv = 8
### robot-1
#### accuracy
- Mean = 0.8233552631578948
- Standard deviation = 0.13158840426541815
- Max = 0.9473684210526315
- 75% = 0.9078947368421053
- Median = 0.8723684210526316
- 25% = 0.7894736842105263
- Min = 0.5789473684210527

#### f1
- Mean = 0.8969457937199873
- Standard deviation = 0.08565421006574442
- Max = 0.972972972972973
- 75% = 0.9515765765765766
- Median = 0.9316816816816816
- 25% = 0.8792626728110599
- Min = 0.7333333333333334

#### precision
- Mean = 1.0
- Standard deviation = 0.0
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 1.0
- Min = 1.0

#### recall
- Mean = 0.8233552631578948
- Standard deviation = 0.13158840426541815
- Max = 0.9473684210526315
- 75% = 0.9078947368421053
- Median = 0.8723684210526316
- 25% = 0.7894736842105263
- Min = 0.5789473684210527

#### facing_probas
- Mean = [0.81733553 0.50092105 0.56625    0.29259868 0.11421053]
- Standard deviation = [0.07805931 0.09366564 0.056885   0.0956506  0.12764975]
- Max = [0.91052632 0.59473684 0.63       0.43684211 0.44      ]
- 75% = [0.87111842 0.56710526 0.61710526 0.35657895 0.09868421]
- Median = [0.85263158 0.54842105 0.58421053 0.28947368 0.07368421]
- 25% = [0.75131579 0.44605263 0.51315789 0.23782895 0.05921053]
- Min = [0.67894737 0.33684211 0.47368421 0.11578947 0.        ]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 0.0 | 0.0 |
| Actual Positive | 3.375 | 15.75 |

### robot-2
#### accuracy
- Mean = 1.0
- Standard deviation = 0.0
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 1.0
- Min = 1.0

#### f1
- Mean = 0.0
- Standard deviation = 0.0
- Max = 0.0
- 75% = 0.0
- Median = 0.0
- 25% = 0.0
- Min = 0.0

#### precision
- Mean = 0.0
- Standard deviation = 0.0
- Max = 0.0
- 75% = 0.0
- Median = 0.0
- 25% = 0.0
- Min = 0.0

#### recall
- Mean = 0.0
- Standard deviation = 0.0
- Max = 0.0
- 75% = 0.0
- Median = 0.0
- 25% = 0.0
- Min = 0.0

#### facing_probas
- Mean = [nan nan nan nan nan]
- Standard deviation = [nan nan nan nan nan]
- Max = [nan nan nan nan nan]
- 75% = [nan nan nan nan nan]
- Median = [nan nan nan nan nan]
- 25% = [nan nan nan nan nan]
- Min = [nan nan nan nan nan]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 0.0 | 0.0 |
| Actual Positive | 0.0 | 19.125 |

### robot-3
#### accuracy
- Mean = 0.9542763157894736
- Standard deviation = 0.04875417270301774
- Max = 1.0
- 75% = 1.0
- Median = 0.9486842105263158
- 25% = 0.9473684210526315
- Min = 0.8421052631578947

#### f1
- Mean = 0.0
- Standard deviation = 0.0
- Max = 0.0
- 75% = 0.0
- Median = 0.0
- 25% = 0.0
- Min = 0.0

#### precision
- Mean = 0.0
- Standard deviation = 0.0
- Max = 0.0
- 75% = 0.0
- Median = 0.0
- 25% = 0.0
- Min = 0.0

#### recall
- Mean = 0.0
- Standard deviation = 0.0
- Max = 0.0
- 75% = 0.0
- Median = 0.0
- 25% = 0.0
- Min = 0.0

#### facing_probas
- Mean = [nan nan nan nan nan]
- Standard deviation = [nan nan nan nan nan]
- Max = [nan nan nan nan nan]
- 75% = [nan nan nan nan nan]
- Median = [nan nan nan nan nan]
- 25% = [nan nan nan nan nan]
- Min = [nan nan nan nan nan]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 11.125 | 0.875 |
| Actual Positive | 0.0 | 7.125 |

### robot-4
#### accuracy
- Mean = 0.986842105263158
- Standard deviation = 0.03481251725084988
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 1.0
- Min = 0.8947368421052632

#### f1
- Mean = 0.0
- Standard deviation = 0.0
- Max = 0.0
- 75% = 0.0
- Median = 0.0
- 25% = 0.0
- Min = 0.0

#### precision
- Mean = 0.0
- Standard deviation = 0.0
- Max = 0.0
- 75% = 0.0
- Median = 0.0
- 25% = 0.0
- Min = 0.0

#### recall
- Mean = 0.0
- Standard deviation = 0.0
- Max = 0.0
- 75% = 0.0
- Median = 0.0
- 25% = 0.0
- Min = 0.0

#### facing_probas
- Mean = [nan nan nan nan nan]
- Standard deviation = [nan nan nan nan nan]
- Max = [nan nan nan nan nan]
- 75% = [nan nan nan nan nan]
- Median = [nan nan nan nan nan]
- 25% = [nan nan nan nan nan]
- Min = [nan nan nan nan nan]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 2.125 | 0.25 |
| Actual Positive | 0.0 | 16.75 |

### robot-5
#### accuracy
- Mean = 0.9875
- Standard deviation = 0.03307189138830738
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 1.0
- Min = 0.9

#### f1
- Mean = 0.0
- Standard deviation = 0.0
- Max = 0.0
- 75% = 0.0
- Median = 0.0
- 25% = 0.0
- Min = 0.0

#### precision
- Mean = 0.0
- Standard deviation = 0.0
- Max = 0.0
- 75% = 0.0
- Median = 0.0
- 25% = 0.0
- Min = 0.0

#### recall
- Mean = 0.0
- Standard deviation = 0.0
- Max = 0.0
- 75% = 0.0
- Median = 0.0
- 25% = 0.0
- Min = 0.0

#### facing_probas
- Mean = [nan nan nan nan nan]
- Standard deviation = [nan nan nan nan nan]
- Max = [nan nan nan nan nan]
- 75% = [nan nan nan nan nan]
- Median = [nan nan nan nan nan]
- 25% = [nan nan nan nan nan]
- Min = [nan nan nan nan nan]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 2.25 | 0.25 |
| Actual Positive | 0.0 | 16.625 |

### robot-6
#### accuracy
- Mean = 0.8233552631578948
- Standard deviation = 0.13158840426541815
- Max = 0.9473684210526315
- 75% = 0.9078947368421053
- Median = 0.8723684210526316
- 25% = 0.7894736842105263
- Min = 0.5789473684210527

#### f1
- Mean = 0.8969457937199873
- Standard deviation = 0.08565421006574442
- Max = 0.972972972972973
- 75% = 0.9515765765765766
- Median = 0.9316816816816816
- 25% = 0.8792626728110599
- Min = 0.7333333333333334

#### precision
- Mean = 1.0
- Standard deviation = 0.0
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 1.0
- Min = 1.0

#### recall
- Mean = 0.8233552631578948
- Standard deviation = 0.13158840426541815
- Max = 0.9473684210526315
- 75% = 0.9078947368421053
- Median = 0.8723684210526316
- 25% = 0.7894736842105263
- Min = 0.5789473684210527

#### facing_probas
- Mean = -100.0
- Standard deviation = 0.0
- Max = -100
- 75% = -100.0
- Median = -100.0
- 25% = -100.0
- Min = -100

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 0.0 | 0.0 |
| Actual Positive | 3.375 | 15.75 |

