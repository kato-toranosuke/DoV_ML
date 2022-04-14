# ExtraTreesClassifier_RandomOverSampler_2022-04-13-17-47_no3
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
- resampler = RandomOverSampler
- estimator = ExtraTreesClassifier

### Arguments for hyperparameter search
- resampler = RandomOverSampler
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
	- shrinkage = None
	- n_features_in_ = 36
	- sampling_strategy_ = OrderedDict([(1, 9)])
	- shrinkage_ = None
	- sample_indices_ = [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14  2  0  2  2  0  0  2  1  2]

- best_estimator
	- base_estimator = ExtraTreeClassifier()
	- n_estimators = 50
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
	- min_samples_split = 10
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
- coe3[2] = 0.11716797488226059
- gp_max_ix_mean = 0.08246477052359404
- tdoa_mean = 0.08022465507001589
- gp_auc_mean = 0.07187211291060108
- gp_max_ix_std = 0.06016361416361417
- gp_auc_max = 0.058611703483645985
- gp_max_val_min = 0.049011327607966275
- gp_max_val_max = 0.04631999382039308
- gp_max_val_mean = 0.04625453584216472
- gp_auc_min = 0.04623524275985737
- hlbr = 0.03778655819579162
- tdoa_range = 0.03333333333333334
- gp_max_val_std = 0.03290155535898571
- gp_max_ix_range = 0.03229102167182663
- ac_std = 0.02736445466328105
- tdoa_std = 0.02697069597069598
- coe3[3] = 0.02673370355135062
- gp_max_val_range = 0.023927728202074547
- gp_auc_range = 0.020349206349206353
- diff_auc = 0.017139393939393944
- gp_max_ix_min = 0.013918495297805644
- coe1[1] = 0.008951048951048951
- ratio_max_to_9th_ave_peaks = 0.008713286713286717
- tdoa_min = 0.0071428571428571435
- ratio_max_to_10ms_ave_peaks = 0.005952380952380952
- high_power = 0.005428824049513705
- srmr = 0.005256410256410255
- low_power = 0.0049019607843137246
- gp_auc_std = 0.002000000000000001
- ac_auc = 0.0006111535523300239
- coe1[0] = 0.0
- coe3[0] = 0.0
- coe3[1] = 0.0
- diff_std = 0.0
- gp_max_ix_max = 0.0
- tdoa_max = 0.0

## Evaluation
cv = 8
### robot-1
#### accuracy
- Mean = 0.5855263157894737
- Standard deviation = 0.08084345873318756
- Max = 0.6842105263157895
- 75% = 0.6447368421052632
- Median = 0.6052631578947368
- 25% = 0.513157894736842
- Min = 0.47368421052631576

#### f1
- Mean = 0.7352612360294508
- Standard deviation = 0.06531057143347593
- Max = 0.8125000000000001
- 75% = 0.7837701612903226
- Median = 0.7537634408602151
- 25% = 0.6779556650246306
- Min = 0.6428571428571429

#### precision
- Mean = 1.0
- Standard deviation = 0.0
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 1.0
- Min = 1.0

#### recall
- Mean = 0.5855263157894737
- Standard deviation = 0.08084345873318756
- Max = 0.6842105263157895
- 75% = 0.6447368421052632
- Median = 0.6052631578947368
- 25% = 0.513157894736842
- Min = 0.47368421052631576

#### facing_probas
- Mean = [0.5932782  0.23017638 0.23116802 0.11244403 0.03797442]
- Standard deviation = [0.07539647 0.08904547 0.09164352 0.11524638 0.01995769]
- Max = [0.69886967 0.37004595 0.37421721 0.29921888 0.060401  ]
- 75% = [0.64832018 0.31201504 0.28970029 0.17338241 0.05743693]
- Median = [0.57911529 0.22377277 0.20415079 0.06311612 0.03973977]
- 25% = [0.54918338 0.14784482 0.15291374 0.01831871 0.01728613]
- Min = [0.46172598 0.11467419 0.13115288 0.00831579 0.01547201]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 0.0 | 0.0 |
| Actual Positive | 7.875 | 11.125 |

### robot-2
#### accuracy
- Mean = 0.9802631578947368
- Standard deviation = 0.05221877587627483
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 1.0
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
| Actual Negative | 2.0 | 0.375 |
| Actual Positive | 0.0 | 16.625 |

### robot-3
#### accuracy
- Mean = 0.9802631578947367
- Standard deviation = 0.025480153593469872
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 0.9473684210526315
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
| Actual Negative | 6.75 | 0.375 |
| Actual Positive | 0.0 | 11.875 |

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
| Actual Positive | 0.0 | 19.0 |

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
| Actual Positive | 0.0 | 19.0 |

### robot-6
#### accuracy
- Mean = 0.5855263157894737
- Standard deviation = 0.08084345873318756
- Max = 0.6842105263157895
- 75% = 0.6447368421052632
- Median = 0.6052631578947368
- 25% = 0.513157894736842
- Min = 0.47368421052631576

#### f1
- Mean = 0.7352612360294508
- Standard deviation = 0.06531057143347593
- Max = 0.8125000000000001
- 75% = 0.7837701612903226
- Median = 0.7537634408602151
- 25% = 0.6779556650246306
- Min = 0.6428571428571429

#### precision
- Mean = 1.0
- Standard deviation = 0.0
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 1.0
- Min = 1.0

#### recall
- Mean = 0.5855263157894737
- Standard deviation = 0.08084345873318756
- Max = 0.6842105263157895
- 75% = 0.6447368421052632
- Median = 0.6052631578947368
- 25% = 0.513157894736842
- Min = 0.47368421052631576

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
| Actual Positive | 7.875 | 11.125 |

