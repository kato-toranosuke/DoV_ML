# ExtraTreesClassifier_NoResampler_2022-04-13-16-21_no0
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
- resampler = NoResampler
- estimator = ExtraTreesClassifier

### Arguments for hyperparameter search
- resampler = NoResampler
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
	- max_features = log2
	- max_leaf_nodes = None
	- min_impurity_decrease = 0.0
	- ccp_alpha = 0.0
	- n_features_in_ = 36
	- n_outputs_ = 1
	- classes_ = [0 1]
	- n_classes_ = 2
	- base_estimator_ = ExtraTreeClassifier()

#### Importance of features
- gp_auc_min = 0.15000000000000005
- gp_max_val_mean = 0.10520833333333333
- gp_max_val_range = 0.10000000000000002
- ratio_max_to_9th_ave_peaks = 0.09375000000000004
- coe3[2] = 0.08333333333333336
- gp_max_val_std = 0.06562499999999999
- tdoa_min = 0.06250000000000003
- hlbr = 0.06220238095238094
- gp_max_val_max = 0.054166666666666634
- gp_max_val_min = 0.04166666666666668
- gp_auc_range = 0.04166666666666668
- gp_max_ix_range = 0.03749999999999999
- ac_auc = 0.03154761904761904
- srmr = 0.031250000000000014
- ac_std = 0.028125000000000008
- tdoa_mean = 0.00624999999999998
- diff_auc = 0.005208333333333337
- low_power = 0.0
- high_power = 0.0
- coe1[0] = 0.0
- coe1[1] = 0.0
- coe3[0] = 0.0
- coe3[1] = 0.0
- coe3[3] = 0.0
- ratio_max_to_10ms_ave_peaks = 0.0
- diff_std = 0.0
- gp_max_ix_std = 0.0
- gp_max_ix_min = 0.0
- gp_max_ix_max = 0.0
- gp_max_ix_mean = 0.0
- gp_auc_std = 0.0
- gp_auc_max = 0.0
- gp_auc_mean = 0.0
- tdoa_std = 0.0
- tdoa_range = 0.0
- tdoa_max = 0.0

## Evaluation
cv = 8
### robot-1
#### accuracy
- Mean = 0.5148026315789473
- Standard deviation = 0.14244560547588184
- Max = 0.7368421052631579
- 75% = 0.5789473684210527
- Median = 0.5
- 25% = 0.39210526315789473
- Min = 0.35

#### f1
- Mean = 0.6684432266328817
- Standard deviation = 0.1199838597771787
- Max = 0.8484848484848484
- 75% = 0.7293625914315569
- Median = 0.666256157635468
- 25% = 0.5631868131868132
- Min = 0.5185185185185185

#### precision
- Mean = 1.0
- Standard deviation = 0.0
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 1.0
- Min = 1.0

#### recall
- Mean = 0.5148026315789473
- Standard deviation = 0.14244560547588184
- Max = 0.7368421052631579
- 75% = 0.5789473684210527
- Median = 0.5
- 25% = 0.39210526315789473
- Min = 0.35

#### facing_probas
- Mean = [0.54493421 0.16375    0.16111842 0.03539474 0.03648026]
- Standard deviation = [0.10590885 0.0718982  0.03754608 0.03166737 0.02928716]
- Max = [0.71578947 0.29473684 0.21052632 0.11       0.1       ]
- 75% = [0.61447368 0.21447368 0.19888158 0.03815789 0.05      ]
- Median = [0.56842105 0.11842105 0.15526316 0.02368421 0.0275    ]
- 25% = [0.4525     0.11039474 0.12763158 0.01447368 0.01447368]
- Min = [0.4        0.1        0.115      0.01       0.00526316]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 0.0 | 0.0 |
| Actual Positive | 9.375 | 9.875 |

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
| Actual Positive | 0.0 | 19.25 |

### robot-3
#### accuracy
- Mean = 0.993421052631579
- Standard deviation = 0.017406258625424956
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 1.0
- Min = 0.9473684210526315

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
| Actual Negative | 2.25 | 0.125 |
| Actual Positive | 0.0 | 16.875 |

### robot-4
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
| Actual Positive | 0.0 | 19.25 |

### robot-5
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
| Actual Positive | 0.0 | 19.25 |

### robot-6
#### accuracy
- Mean = 0.5148026315789473
- Standard deviation = 0.14244560547588184
- Max = 0.7368421052631579
- 75% = 0.5789473684210527
- Median = 0.5
- 25% = 0.39210526315789473
- Min = 0.35

#### f1
- Mean = 0.6684432266328817
- Standard deviation = 0.1199838597771787
- Max = 0.8484848484848484
- 75% = 0.7293625914315569
- Median = 0.666256157635468
- 25% = 0.5631868131868132
- Min = 0.5185185185185185

#### precision
- Mean = 1.0
- Standard deviation = 0.0
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 1.0
- Min = 1.0

#### recall
- Mean = 0.5148026315789473
- Standard deviation = 0.14244560547588184
- Max = 0.7368421052631579
- 75% = 0.5789473684210527
- Median = 0.5
- 25% = 0.39210526315789473
- Min = 0.35

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
| Actual Positive | 9.375 | 9.875 |

