# ExtraTreesClassifier_ClusterCentroids_2022-04-13-16-50_no1
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
- resampler = ClusterCentroids
- estimator = ExtraTreesClassifier

### Arguments for hyperparameter search
- resampler = ClusterCentroids
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
	- estimator = None
	- voting = auto
	- n_jobs = deprecated
	- n_features_in_ = 36
	- sampling_strategy_ = OrderedDict([(0, 2)])
	- estimator_ = KMeans(n_clusters=2, random_state=42)
	- voting_ = soft

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
	- min_samples_split = 5
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
- low_power = 0.0
- high_power = 0.0
- hlbr = 0.0
- coe1[0] = 0.0
- coe1[1] = 0.0
- coe3[0] = 0.0
- coe3[1] = 0.0
- coe3[2] = 0.0
- coe3[3] = 0.0
- ratio_max_to_10ms_ave_peaks = 0.0
- ratio_max_to_9th_ave_peaks = 0.0
- ac_std = 0.0
- ac_auc = 0.0
- diff_std = 0.0
- diff_auc = 0.0
- srmr = 0.0
- gp_max_val_std = 0.0
- gp_max_val_range = 0.0
- gp_max_val_min = 0.0
- gp_max_val_max = 0.0
- gp_max_val_mean = 0.0
- gp_max_ix_std = 0.0
- gp_max_ix_range = 0.0
- gp_max_ix_min = 0.0
- gp_max_ix_max = 0.0
- gp_max_ix_mean = 0.0
- gp_auc_std = 0.0
- gp_auc_range = 0.0
- gp_auc_min = 0.0
- gp_auc_max = 0.0
- gp_auc_mean = 0.0
- tdoa_std = 0.0
- tdoa_range = 0.0
- tdoa_min = 0.0
- tdoa_max = 0.0
- tdoa_mean = 0.0

## Evaluation
cv = 8
### robot-1
#### accuracy
- Mean = 0.7697368421052632
- Standard deviation = 0.30227381599105635
- Max = 1.0
- 75% = 0.9473684210526315
- Median = 0.868421052631579
- 25% = 0.7763157894736842
- Min = 0.0

#### f1
- Mean = 0.816939236792178
- Standard deviation = 0.3123703743729309
- Max = 1.0
- 75% = 0.972972972972973
- Median = 0.9293650793650794
- 25% = 0.873885918003565
- Min = 0.0

#### precision
- Mean = 0.875
- Standard deviation = 0.33071891388307384
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 1.0
- Min = 0.0

#### recall
- Mean = 0.7697368421052632
- Standard deviation = 0.30227381599105635
- Max = 1.0
- 75% = 0.9473684210526315
- Median = 0.868421052631579
- 25% = 0.7763157894736842
- Min = 0.0

#### facing_probas
- Mean = [0.74967105 0.53667763 0.53985746 0.29095395 0.18585526]
- Standard deviation = [0.11450346 0.12124098 0.06168109 0.15078631 0.14922577]
- Max = [0.88684211 0.72763158 0.65789474 0.525      0.5       ]
- 75% = [0.83881579 0.63914474 0.57247807 0.38059211 0.23223684]
- Median = [0.76118421 0.51381579 0.53815789 0.28026316 0.10657895]
- 25% = [0.70032895 0.46842105 0.49901316 0.16447368 0.09276316]
- Min = [0.5        0.37105263 0.43815789 0.08026316 0.05      ]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 0.0 | 0.0 |
| Actual Positive | 4.5 | 14.625 |

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
- Mean = 0.9736842105263157
- Standard deviation = 0.026315789473684237
- Max = 1.0
- 75% = 1.0
- Median = 0.9736842105263157
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
| Actual Negative | 9.0 | 0.5 |
| Actual Positive | 0.0 | 9.625 |

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
| Actual Positive | 0.0 | 19.125 |

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
| Actual Positive | 0.0 | 19.125 |

### robot-6
#### accuracy
- Mean = 0.7697368421052632
- Standard deviation = 0.30227381599105635
- Max = 1.0
- 75% = 0.9473684210526315
- Median = 0.868421052631579
- 25% = 0.7763157894736842
- Min = 0.0

#### f1
- Mean = 0.816939236792178
- Standard deviation = 0.3123703743729309
- Max = 1.0
- 75% = 0.972972972972973
- Median = 0.9293650793650794
- 25% = 0.873885918003565
- Min = 0.0

#### precision
- Mean = 0.875
- Standard deviation = 0.33071891388307384
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 1.0
- Min = 0.0

#### recall
- Mean = 0.7697368421052632
- Standard deviation = 0.30227381599105635
- Max = 1.0
- 75% = 0.9473684210526315
- Median = 0.868421052631579
- 25% = 0.7763157894736842
- Min = 0.0

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
| Actual Negative | 2 | 2 |
| Actual Positive | 6 | 14 |

