# ExtraTreesClassifier_NoResampler_2022-01-19-00-36_no0
## Constants
- CSV_PATH = ../out/csv/experiment
- OUTPUT_PATH = ../out/experiment_result/data_of_2022-01-13_eval_system/AGC-45angle-5m
- FEATURE_ATTRBS = ['low_power', 'high_power', 'hlbr', 'coe1[0]', 'coe1[1]', 'coe3[0]', 'coe3[1]', 'coe3[2]', 'coe3[3]', 'ratio_max_to_10ms_ave_peaks', 'ratio_max_to_9th_ave_peaks', 'ac_std', 'ac_auc', 'diff_std', 'diff_auc', 'srmr', 'gp_max_val_std', 'gp_max_val_range', 'gp_max_val_min', 'gp_max_val_max', 'gp_max_val_mean', 'gp_max_ix_std', 'gp_max_ix_range', 'gp_max_ix_min', 'gp_max_ix_max', 'gp_max_ix_mean', 'gp_auc_std', 'gp_auc_range', 'gp_auc_min', 'gp_auc_max', 'gp_auc_mean', 'tdoa_std', 'tdoa_range', 'tdoa_min', 'tdoa_max', 'tdoa_mean']
- LABEL_ATTRB = ['facing2']
- FACING_DOV_ANGLES = [1, 2]
- NCV = 8
- SCORING = ['accuracy', 'balanced_accuracy', 'f1']
- REFIT_SCORING = balanced_accuracy
- PARAM_GRID = [{'est__n_estimators': range(10, 400, 20), 'est__min_samples_split': [2, 5, 10], 'est__min_samples_leaf': [1, 5, 10], 'est__max_features': ['sqrt', 'log2', None], 'est__bootstrap': [False], 'est__n_jobs': [-1], 'est__random_state': [42], 'est__max_samples': [0.01, 0.5, 0.09]}, {'est__n_estimators': range(10, 400, 20), 'est__min_samples_split': [2, 5, 10], 'est__min_samples_leaf': [1, 5, 10], 'est__max_features': ['sqrt', 'log2', None], 'est__bootstrap': [True], 'est__oob_score': [True, False], 'est__n_jobs': [-1], 'est__random_state': [42], 'est__max_samples': [0.01, 0.5, 0.09]}]
- HP_SET_SESSION = ['trial1', 'trial21']
- TRAIN_SET_SESSION = None
- TEST_SET_SESSION = None
- DISTANCE = [5]
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
	- min_samples_leaf = 10
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
- gp_max_val_mean = 0.2127690761035784
- diff_auc = 0.12736185166047925
- gp_auc_mean = 0.1
- gp_max_val_max = 0.09874583173488358
- gp_max_ix_min = 0.07638435280849543
- hlbr = 0.07457088366179275
- diff_std = 0.06781739431861286
- coe1[0] = 0.06386395883843948
- gp_max_val_min = 0.05200311074869379
- tdoa_min = 0.03947992484874112
- ratio_max_to_9th_ave_peaks = 0.036136041161560516
- gp_max_ix_std = 0.02542911633820725
- coe3[3] = 0.01822265732320939
- tdoa_mean = 0.0037471791057304077
- gp_max_val_range = 0.0010493572686729315
- gp_max_ix_range = 0.0009959571517101002
- ac_std = 0.000965123204870835
- ac_auc = 0.0004581837223219698
- low_power = 0.0
- high_power = 0.0
- coe1[1] = 0.0
- coe3[0] = 0.0
- coe3[1] = 0.0
- coe3[2] = 0.0
- ratio_max_to_10ms_ave_peaks = 0.0
- srmr = 0.0
- gp_max_val_std = 0.0
- gp_max_ix_max = 0.0
- gp_max_ix_mean = 0.0
- gp_auc_std = 0.0
- gp_auc_range = 0.0
- gp_auc_min = 0.0
- gp_auc_max = 0.0
- tdoa_std = 0.0
- tdoa_range = 0.0
- tdoa_max = 0.0

## Evaluation
cv = 8
### robot-1
#### accuracy
- Mean = 0.9512499999999999
- Standard deviation = 0.012686114456365262
- Max = 0.97
- 75% = 0.96
- Median = 0.955
- 25% = 0.94
- Min = 0.93

#### f1
- Mean = 0.8803830604320201
- Standard deviation = 0.030991852675707757
- Max = 0.9302325581395349
- 75% = 0.9022727272727273
- Median = 0.8832658569500675
- 25% = 0.85
- Min = 0.8372093023255814

#### precision
- Mean = 0.8655860666158148
- Standard deviation = 0.04566166028327011
- Max = 0.9444444444444444
- 75% = 0.8960526315789474
- Median = 0.8597826086956522
- 25% = 0.8458333333333333
- Min = 0.782608695652174

#### recall
- Mean = 0.9
- Standard deviation = 0.06123724356957946
- Max = 1.0
- 75% = 0.925
- Median = 0.875
- 25% = 0.85
- Min = 0.85

#### facing_probas
- Mean = [0.90487016 0.72658548 0.30204051 0.14264126 0.11438661]
- Standard deviation = [0.02951628 0.02951603 0.0427565  0.01659065 0.04158558]
- Max = [0.95398448 0.76160745 0.37819999 0.16373748 0.16790645]
- 75% = [0.92342732 0.74434345 0.32890653 0.15582706 0.14819123]
- Median = [0.90806146 0.74001169 0.28760092 0.14544787 0.1226302 ]
- 25% = [0.88643648 0.71461544 0.28230747 0.13440687 0.09341023]
- Min = [0.85177427 0.66522432 0.2318225  0.11026671 0.03537037]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 77.125 | 2.875 |
| Actual Positive | 2.0 | 18.0 |

### robot-2
#### accuracy
- Mean = 0.9349999999999999
- Standard deviation = 0.04873397172404479
- Max = 0.97
- 75% = 0.96
- Median = 0.955
- 25% = 0.9375
- Min = 0.81

#### f1
- Mean = 0.805965700020578
- Standard deviation = 0.19530719098738183
- Max = 0.9189189189189189
- 75% = 0.9011904761904762
- Median = 0.8834688346883468
- 25% = 0.8402027027027027
- Min = 0.29629629629629634

#### precision
- Mean = 0.8655700916730329
- Standard deviation = 0.12472284393948646
- Max = 1.0
- 75% = 0.925
- Median = 0.8729946524064172
- 25% = 0.8553571428571428
- Min = 0.5714285714285714

#### recall
- Mean = 0.775
- Standard deviation = 0.22499999999999998
- Max = 0.95
- 75% = 0.9
- Median = 0.85
- 25% = 0.7875000000000001
- Min = 0.2

#### facing_probas
- Mean = [0.76702247 0.78355777 0.64444878 0.33248544 0.10368171]
- Standard deviation = [0.02671997 0.02881571 0.03068395 0.06991941 0.03733441]
- Max = [0.80959607 0.81885004 0.67786375 0.50060383 0.15126962]
- 75% = [0.78890156 0.80710791 0.67034241 0.33336628 0.13239406]
- Median = [0.76640192 0.7917154  0.65974611 0.31539587 0.10488879]
- 25% = [0.74588204 0.75930222 0.6068761  0.29581901 0.08853404]
- Min = [0.72649009 0.7307362  0.60441285 0.25293766 0.032892  ]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 78.0 | 2.0 |
| Actual Positive | 4.5 | 15.5 |

### robot-3
#### accuracy
- Mean = 0.95875
- Standard deviation = 0.020879116360612567
- Max = 0.98
- 75% = 0.9724999999999999
- Median = 0.96
- 25% = 0.9575
- Min = 0.91

#### f1
- Mean = 0.8814125885433186
- Standard deviation = 0.07131438657025935
- Max = 0.9473684210526316
- 75% = 0.9291497975708503
- Median = 0.888888888888889
- 25% = 0.8809523809523809
- Min = 0.7096774193548387

#### precision
- Mean = 0.993421052631579
- Standard deviation = 0.017406258625424956
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 1.0
- Min = 0.9473684210526315

#### recall
- Mean = 0.8
- Standard deviation = 0.10897247358851683
- Max = 0.9
- 75% = 0.9
- Median = 0.8
- 25% = 0.7875000000000001
- Min = 0.55

#### facing_probas
- Mean = [0.40369817 0.81193519 0.83652091 0.79448768 0.26967327]
- Standard deviation = [0.027873   0.04653645 0.03930573 0.02089895 0.03969483]
- Max = [0.45427198 0.88948955 0.90516155 0.82192345 0.34026215]
- 75% = [0.41452954 0.84047306 0.86039603 0.81158758 0.28785012]
- Median = [0.40251136 0.80041362 0.83760658 0.79714948 0.26957992]
- 25% = [0.38303676 0.77986018 0.81496359 0.78382216 0.24035333]
- Min = [0.365801   0.74984777 0.76849527 0.75167271 0.21164025]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 79.875 | 0.125 |
| Actual Positive | 4.0 | 16.0 |

### robot-4
#### accuracy
- Mean = 0.92375
- Standard deviation = 0.030796712486887277
- Max = 0.96
- 75% = 0.95
- Median = 0.935
- 25% = 0.8975
- Min = 0.87

#### f1
- Mean = 0.7933191918486036
- Standard deviation = 0.08475002324093889
- Max = 0.9
- 75% = 0.8608058608058607
- Median = 0.8220211161387632
- 25% = 0.7173423423423424
- Min = 0.6486486486486486

#### precision
- Mean = 0.8649912925696595
- Standard deviation = 0.09824525038586233
- Max = 1.0
- 75% = 0.925
- Median = 0.868421052631579
- 25% = 0.8005514705882353
- Min = 0.7058823529411765

#### recall
- Mean = 0.7375
- Standard deviation = 0.09921567416492216
- Max = 0.9
- 75% = 0.8125
- Median = 0.725
- 25% = 0.65
- Min = 0.6

#### facing_probas
- Mean = [0.12317609 0.3600626  0.76206055 0.89821642 0.68230756]
- Standard deviation = [0.03727532 0.05877153 0.03574738 0.03000634 0.0335156 ]
- Max = [0.17485966 0.42873466 0.82345584 0.93695469 0.75500096]
- 75% = [0.15025777 0.41912804 0.78245968 0.92215942 0.6943314 ]
- Median = [0.12674045 0.35623022 0.76970697 0.89778835 0.67802829]
- 25% = [0.09593707 0.3327327  0.72936865 0.88021843 0.6643339 ]
- Min = [0.06103719 0.24241389 0.70688121 0.844514   0.63900728]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 77.625 | 2.375 |
| Actual Positive | 5.25 | 14.75 |

### robot-5
#### accuracy
- Mean = 0.9725
- Standard deviation = 0.012990381056766592
- Max = 0.99
- 75% = 0.9824999999999999
- Median = 0.97
- 25% = 0.9675
- Min = 0.95

#### f1
- Mean = 0.9256918050242826
- Standard deviation = 0.03808784883801394
- Max = 0.975609756097561
- 75% = 0.9544287548138639
- Median = 0.920997920997921
- 25% = 0.9114114114114114
- Min = 0.8571428571428571

#### precision
- Mean = 0.981516290726817
- Standard deviation = 0.023906198011234808
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 0.9523809523809523
- Min = 0.9473684210526315

#### recall
- Mean = 0.8812500000000001
- Standard deviation = 0.08267972847076846
- Max = 1.0
- 75% = 0.925
- Median = 0.875
- 25% = 0.8375
- Min = 0.75

#### facing_probas
- Mean = [0.09408529 0.13377907 0.34278207 0.83895782 0.79875592]
- Standard deviation = [0.03443406 0.04949777 0.04761693 0.02927453 0.03477553]
- Max = [0.14949734 0.20336499 0.42095623 0.8659196  0.8687768 ]
- 75% = [0.12310219 0.17095779 0.36396688 0.86160127 0.81270715]
- Median = [0.09018618 0.14058814 0.34836727 0.84468277 0.78905397]
- 25% = [0.06602528 0.10088096 0.29719284 0.83184169 0.77928463]
- Min = [0.04613604 0.05314911 0.2777241  0.77071176 0.7513736 ]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 79.625 | 0.375 |
| Actual Positive | 2.375 | 17.625 |

### robot-6
#### accuracy
- Mean = 0.8187500000000001
- Standard deviation = 0.06029873547596168
- Max = 0.89
- 75% = 0.8725
- Median = 0.8300000000000001
- 25% = 0.7675000000000001
- Min = 0.72

#### f1
- Mean = 0.8991215841011291
- Standard deviation = 0.03686980280026299
- Max = 0.9417989417989417
- 75% = 0.9319035157583342
- Median = 0.9068100358422939
- 25% = 0.8684514637904468
- Min = 0.8372093023255813

#### precision
- Mean = 1.0
- Standard deviation = 0.0
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 1.0
- Min = 1.0

#### recall
- Mean = 0.8187500000000001
- Standard deviation = 0.06029873547596168
- Max = 0.89
- 75% = 0.8725
- Median = 0.8300000000000001
- 25% = 0.7675000000000001
- Min = 0.72

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
| Actual Positive | 18.125 | 81.875 |

