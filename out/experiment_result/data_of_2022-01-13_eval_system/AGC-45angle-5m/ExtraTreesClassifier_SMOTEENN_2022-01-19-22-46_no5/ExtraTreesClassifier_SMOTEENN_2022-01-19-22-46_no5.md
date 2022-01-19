# ExtraTreesClassifier_SMOTEENN_2022-01-19-22-46_no5
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
- resampler = SMOTEENN
- estimator = ExtraTreesClassifier

### Arguments for hyperparameter search
- resampler = SMOTEENN
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
	- smote = None
	- enn = None
	- n_jobs = -1
	- n_features_in_ = 36
	- sampling_strategy_ = auto
	- smote_ = SMOTE(n_jobs=-1, random_state=42)
	- enn_ = EditedNearestNeighbours(n_jobs=-1, sampling_strategy='all')

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
- gp_auc_mean = 0.2286363636363636
- high_power = 0.20545454545454542
- gp_max_val_max = 0.09999999999999998
- gp_max_val_mean = 0.09999999999999998
- gp_auc_min = 0.09999999999999998
- ac_auc = 0.07954545454545454
- hlbr = 0.050909090909090904
- tdoa_std = 0.03571428571428571
- coe1[1] = 0.03221590909090908
- ac_std = 0.016874999999999998
- gp_max_val_range = 0.011249999999999998
- gp_max_val_std = 0.010285714285714287
- diff_std = 0.009204545454545455
- gp_auc_max = 0.008999999999999996
- tdoa_min = 0.005454545454545457
- tdoa_range = 0.005454545454545456
- low_power = 0.0
- coe1[0] = 0.0
- coe3[0] = 0.0
- coe3[1] = 0.0
- coe3[2] = 0.0
- coe3[3] = 0.0
- ratio_max_to_10ms_ave_peaks = 0.0
- ratio_max_to_9th_ave_peaks = 0.0
- diff_auc = 0.0
- srmr = 0.0
- gp_max_val_min = 0.0
- gp_max_ix_std = 0.0
- gp_max_ix_range = 0.0
- gp_max_ix_min = 0.0
- gp_max_ix_max = 0.0
- gp_max_ix_mean = 0.0
- gp_auc_std = 0.0
- gp_auc_range = 0.0
- tdoa_max = 0.0
- tdoa_mean = 0.0

## Evaluation
cv = 8
### robot-1
#### accuracy
- Mean = 0.9425
- Standard deviation = 0.018540496217739122
- Max = 0.97
- 75% = 0.96
- Median = 0.94
- 25% = 0.9275
- Min = 0.92

#### f1
- Mean = 0.8623881524115047
- Standard deviation = 0.04350214222350318
- Max = 0.9268292682926829
- 75% = 0.9047619047619048
- Median = 0.8541033434650456
- 25% = 0.8333333333333333
- Min = 0.787878787878788

#### precision
- Mean = 0.8501683501683502
- Standard deviation = 0.11019576939084613
- Max = 1.0
- 75% = 0.9285714285714286
- Median = 0.8636363636363636
- 25% = 0.7341269841269841
- Min = 0.7142857142857143

#### recall
- Mean = 0.90625
- Standard deviation = 0.12358574958303242
- Max = 1.0
- 75% = 1.0
- Median = 0.95
- 25% = 0.8999999999999999
- Min = 0.65

#### facing_probas
- Mean = [0.93875  0.765    0.23625  0.07375  0.038125]
- Standard deviation = [0.07728802 0.14570947 0.135341   0.05845671 0.06056698]
- Max = [1.    0.965 0.5   0.19  0.195]
- 75% = [1.      0.875   0.305   0.085   0.03125]
- Median = [0.9875 0.8025 0.235  0.055  0.02  ]
- 25% = [0.875   0.6675  0.1275  0.0425  0.00375]
- Min = [0.785 0.52  0.07  0.    0.   ]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 76.125 | 3.875 |
| Actual Positive | 1.875 | 18.125 |

### robot-2
#### accuracy
- Mean = 0.88
- Standard deviation = 0.06892024376045111
- Max = 0.97
- 75% = 0.93
- Median = 0.885
- 25% = 0.83
- Min = 0.76

#### f1
- Mean = 0.5394549815173385
- Standard deviation = 0.3289295376131972
- Max = 0.9230769230769231
- 75% = 0.8432494279176203
- Median = 0.575
- 25% = 0.2608695652173913
- Min = 0.0

#### precision
- Mean = 0.8278227620332883
- Standard deviation = 0.32426488010679744
- Max = 1.0
- 75% = 1.0
- Median = 0.9736842105263157
- 25% = 0.891025641025641
- Min = 0.0

#### recall
- Mean = 0.48125
- Standard deviation = 0.36223050327105255
- Max = 0.95
- 75% = 0.8625
- Median = 0.425
- 25% = 0.15
- Min = 0.0

#### facing_probas
- Mean = [0.758125 0.748125 0.581875 0.2525   0.026875]
- Standard deviation = [0.173996   0.14181717 0.18328491 0.20636739 0.0442957 ]
- Max = [0.93  0.895 0.83  0.7   0.135]
- 75% = [0.915   0.85625 0.76    0.3275  0.02125]
- Median = [0.835  0.8175 0.585  0.2175 0.0075]
- 25% = [0.58375 0.62125 0.39875 0.1025  0.     ]
- Min = [0.49  0.505 0.33  0.005 0.   ]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 78.375 | 1.625 |
| Actual Positive | 10.375 | 9.625 |

### robot-3
#### accuracy
- Mean = 0.9299999999999999
- Standard deviation = 0.04242640687119285
- Max = 1.0
- 75% = 0.955
- Median = 0.925
- 25% = 0.915
- Min = 0.85

#### f1
- Mean = 0.7681641391200215
- Standard deviation = 0.16991513153523446
- Max = 1.0
- 75% = 0.8725868725868725
- Median = 0.7762923351158646
- 25% = 0.7291666666666665
- Min = 0.4

#### precision
- Mean = 0.9910714285714286
- Standard deviation = 0.02362277956307669
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 1.0
- Min = 0.9285714285714286

#### recall
- Mean = 0.65625
- Standard deviation = 0.21130176880471208
- Max = 1.0
- 75% = 0.775
- Median = 0.65
- 25% = 0.575
- Min = 0.25

#### facing_probas
- Mean = [0.310625 0.838125 0.90875  0.82375  0.205   ]
- Standard deviation = [0.19739614 0.10632901 0.11799762 0.13471614 0.16524603]
- Max = [0.665 0.985 1.    0.985 0.54 ]
- 75% = [0.46    0.93125 0.99125 0.95375 0.3125 ]
- Median = [0.3    0.83   0.9625 0.8225 0.145 ]
- 25% = [0.12375 0.77125 0.89    0.71875 0.06   ]
- Min = [0.065 0.65  0.69  0.62  0.05 ]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 79.875 | 0.125 |
| Actual Positive | 6.875 | 13.125 |

### robot-4
#### accuracy
- Mean = 0.89375
- Standard deviation = 0.05194648688795037
- Max = 0.94
- 75% = 0.9225000000000001
- Median = 0.915
- 25% = 0.89
- Min = 0.77

#### f1
- Mean = 0.7170977520363753
- Standard deviation = 0.126257128348939
- Max = 0.8421052631578948
- 75% = 0.8027027027027028
- Median = 0.7731152204836415
- 25% = 0.6684027777777777
- Min = 0.4390243902439024

#### precision
- Mean = 0.7826053338001868
- Standard deviation = 0.14922882400209156
- Max = 0.9166666666666666
- 75% = 0.8839869281045751
- Median = 0.8284313725490196
- 25% = 0.7718750000000001
- Min = 0.42857142857142855

#### recall
- Mean = 0.66875
- Standard deviation = 0.12484365222148862
- Max = 0.8
- 75% = 0.7625
- Median = 0.725
- 25% = 0.55
- Min = 0.45

#### facing_probas
- Mean = [0.05625  0.30125  0.831875 0.945    0.730625]
- Standard deviation = [0.07540516 0.15513603 0.13327456 0.05804093 0.13431394]
- Max = [0.24  0.595 0.965 1.    0.9  ]
- 75% = [0.05875 0.39    0.93875 1.      0.8475 ]
- Median = [0.02   0.26   0.8875 0.97   0.7525]
- 25% = [0.01375 0.18625 0.755   0.89    0.64375]
- Min = [0.    0.13  0.58  0.85  0.495]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 76.0 | 4.0 |
| Actual Positive | 6.625 | 13.375 |

### robot-5
#### accuracy
- Mean = 0.9475
- Standard deviation = 0.029474565306378975
- Max = 0.97
- 75% = 0.97
- Median = 0.96
- 25% = 0.9375
- Min = 0.88

#### f1
- Mean = 0.8450339075339075
- Standard deviation = 0.11125925107437967
- Max = 0.9230769230769231
- 75% = 0.9189189189189189
- Median = 0.8918918918918919
- 25% = 0.8277027027027027
- Min = 0.5714285714285715

#### precision
- Mean = 0.9635497291021672
- Standard deviation = 0.04084787812202372
- Max = 1.0
- 75% = 1.0
- Median = 0.9736842105263157
- 25% = 0.9402573529411764
- Min = 0.8823529411764706

#### recall
- Mean = 0.7687499999999999
- Standard deviation = 0.1477698802192111
- Max = 0.9
- 75% = 0.85
- Median = 0.825
- 25% = 0.75
- Min = 0.4

#### facing_probas
- Mean = [0.05875  0.056875 0.250625 0.853125 0.825625]
- Standard deviation = [0.09225474 0.08283785 0.18037179 0.1353915  0.12375473]
- Max = [0.28  0.255 0.635 0.98  0.975]
- 75% = [0.0675 0.075  0.345  0.9675 0.9525]
- Median = [0.01   0.015  0.2125 0.925  0.83  ]
- 25% = [0.      0.      0.10875 0.73125 0.73   ]
- Min = [0.   0.   0.05 0.62 0.62]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 79.375 | 0.625 |
| Actual Positive | 4.625 | 15.375 |

### robot-6
#### accuracy
- Mean = 0.69625
- Standard deviation = 0.11936681909140409
- Max = 0.85
- 75% = 0.82
- Median = 0.69
- 25% = 0.6
- Min = 0.54

#### f1
- Mean = 0.8150260925001602
- Standard deviation = 0.0839603902749272
- Max = 0.9189189189189189
- 75% = 0.9010989010989011
- Median = 0.8155312587608634
- 25% = 0.7493987493987494
- Min = 0.7012987012987013

#### precision
- Mean = 1.0
- Standard deviation = 0.0
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 1.0
- Min = 1.0

#### recall
- Mean = 0.69625
- Standard deviation = 0.11936681909140409
- Max = 0.85
- 75% = 0.82
- Median = 0.69
- 25% = 0.6
- Min = 0.54

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
| Actual Positive | 30.375 | 69.625 |

