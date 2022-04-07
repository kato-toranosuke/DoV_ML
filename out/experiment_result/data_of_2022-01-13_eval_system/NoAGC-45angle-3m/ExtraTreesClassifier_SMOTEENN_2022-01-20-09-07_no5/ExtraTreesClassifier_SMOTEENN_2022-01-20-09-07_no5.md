# ExtraTreesClassifier_SMOTEENN_2022-01-20-09-07_no5
## Constants
- CSV_PATH = ../out/csv/experiment
- OUTPUT_PATH = ../out/experiment_result/data_of_2022-01-13_eval_system/NoAGC-45angle-3m
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
- DISTANCE = [3]
- AGC_STATUS = ['NoAGC']

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
- coe1[0] = 0.145
- coe3[3] = 0.1041507936507936
- gp_max_val_max = 0.09999999999999998
- ac_std = 0.0952991452991453
- diff_std = 0.08697863247863247
- diff_auc = 0.08533333333333333
- coe3[2] = 0.08523809523809521
- gp_max_val_mean = 0.07127777777777777
- gp_auc_min = 0.053333333333333316
- gp_max_val_range = 0.032444444444444435
- ratio_max_to_10ms_ave_peaks = 0.02502976190476191
- gp_max_val_std = 0.02077777777777777
- coe1[1] = 0.019206349206349203
- gp_max_ix_max = 0.015277777777777776
- gp_max_ix_mean = 0.014666666666666661
- gp_auc_max = 0.014666666666666661
- high_power = 0.013749999999999995
- srmr = 0.009166666666666665
- tdoa_max = 0.007638888888888888
- gp_auc_std = 0.000763888888888888
- low_power = 0.0
- hlbr = 0.0
- coe3[0] = 0.0
- coe3[1] = 0.0
- ratio_max_to_9th_ave_peaks = 0.0
- ac_auc = 0.0
- gp_max_val_min = 0.0
- gp_max_ix_std = 0.0
- gp_max_ix_range = 0.0
- gp_max_ix_min = 0.0
- gp_auc_range = 0.0
- gp_auc_mean = 0.0
- tdoa_std = 0.0
- tdoa_range = 0.0
- tdoa_min = 0.0
- tdoa_mean = 0.0

## Evaluation
cv = 8
### robot-1
#### accuracy
- Mean = 0.9475
- Standard deviation = 0.05804093383121948
- Max = 1.0
- 75% = 0.9724999999999999
- Median = 0.965
- 25% = 0.955
- Min = 0.8

#### f1
- Mean = 0.8012627288943078
- Standard deviation = 0.30599549417628863
- Max = 1.0
- 75% = 0.9272844272844272
- Median = 0.9039039039039038
- 25% = 0.8771929824561404
- Min = 0.0

#### precision
- Mean = 0.8497474747474747
- Standard deviation = 0.32403772370361783
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 0.904040404040404
- Min = 0.0

#### recall
- Mean = 0.7625
- Standard deviation = 0.29869507863371303
- Max = 1.0
- 75% = 0.8875
- Median = 0.825
- 25% = 0.8
- Min = 0.0

#### facing_probas
- Mean = [0.921875 0.84     0.263125 0.073125 0.0375  ]
- Standard deviation = [0.05061728 0.10691702 0.21533314 0.11929317 0.04451123]
- Max = [0.985 0.965 0.72  0.37  0.135]
- 75% = [0.96875 0.90875 0.3775  0.09125 0.0575 ]
- Median = [0.92   0.855  0.18   0.01   0.0225]
- 25% = [0.87625 0.81625 0.11125 0.      0.     ]
- Min = [0.86  0.595 0.04  0.    0.   ]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 79.5 | 0.5 |
| Actual Positive | 4.75 | 15.25 |

### robot-2
#### accuracy
- Mean = 0.8999999999999999
- Standard deviation = 0.11180339887498948
- Max = 0.98
- 75% = 0.9475
- Median = 0.935
- 25% = 0.9175
- Min = 0.61

#### f1
- Mean = 0.7376166436259504
- Standard deviation = 0.2858348826368495
- Max = 0.9473684210526316
- 75% = 0.8682692307692308
- Median = 0.825
- 25% = 0.7728658536585366
- Min = 0.0

#### precision
- Mean = 0.7928258145363408
- Standard deviation = 0.3093409779212739
- Max = 1.0
- 75% = 0.9605263157894737
- Median = 0.8916666666666666
- 25% = 0.8279761904761904
- Min = 0.0

#### recall
- Mean = 0.7
- Standard deviation = 0.2817356917396161
- Max = 0.9
- 75% = 0.8625
- Median = 0.825
- 25% = 0.6749999999999999
- Min = 0.0

#### facing_probas
- Mean = [0.92125  0.940625 0.8875   0.2575   0.055625]
- Standard deviation = [0.04948169 0.0516864  0.09516433 0.26870058 0.07350329]
- Max = [0.985 0.985 0.99  0.805 0.235]
- 75% = [0.95875 0.98125 0.9675  0.45125 0.0675 ]
- Median = [0.935  0.97   0.915  0.1175 0.035 ]
- 25% = [0.88125 0.905   0.83875 0.0425  0.     ]
- Min = [0.845 0.845 0.705 0.015 0.   ]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 76.0 | 4.0 |
| Actual Positive | 6.0 | 14.0 |

### robot-3
#### accuracy
- Mean = 0.8162499999999999
- Standard deviation = 0.03870965641800504
- Max = 0.87
- 75% = 0.8374999999999999
- Median = 0.825
- 25% = 0.7925
- Min = 0.75

#### f1
- Mean = 0.2262888906111412
- Standard deviation = 0.21633094743160203
- Max = 0.588235294117647
- 75% = 0.3252818035426731
- Median = 0.22134387351778656
- 25% = 0.0
- Min = 0.0

#### precision
- Mean = 0.5892857142857143
- Standard deviation = 0.46531479359983513
- Max = 1.0
- 75% = 1.0
- Median = 0.8571428571428572
- 25% = 0.0
- Min = 0.0

#### recall
- Mean = 0.15625
- Standard deviation = 0.17036266463048763
- Max = 0.5
- 75% = 0.19999999999999998
- Median = 0.125
- 25% = 0.0
- Min = 0.0

#### facing_probas
- Mean = [0.550625 0.913125 0.895625 0.69875  0.275625]
- Standard deviation = [0.25199749 0.07805997 0.08486892 0.24488199 0.25167486]
- Max = [0.91  0.985 0.995 0.995 0.765]
- 75% = [0.7075  0.96875 0.9525  0.91    0.3975 ]
- Median = [0.575  0.9575 0.94   0.7375 0.2525]
- 25% = [0.48625 0.8625  0.8325  0.5925  0.035  ]
- Min = [0.06  0.78  0.75  0.27  0.005]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 78.5 | 1.5 |
| Actual Positive | 16.875 | 3.125 |

### robot-4
#### accuracy
- Mean = 0.7125
- Standard deviation = 0.05141740950300784
- Max = 0.8
- 75% = 0.725
- Median = 0.69
- 25% = 0.6775
- Min = 0.67

#### f1
- Mean = 0.05025783040488924
- Standard deviation = 0.059529627913529726
- Max = 0.16666666666666669
- 75% = 0.07486631016042782
- Median = 0.028571428571428574
- 25% = 0.0
- Min = 0.0

#### precision
- Mean = 0.0983058608058608
- Standard deviation = 0.15947469600332131
- Max = 0.5
- 75% = 0.09340659340659341
- Median = 0.03333333333333333
- 25% = 0.0
- Min = 0.0

#### recall
- Mean = 0.037500000000000006
- Standard deviation = 0.0414578098794425
- Max = 0.1
- 75% = 0.0625
- Median = 0.025
- 25% = 0.0
- Min = 0.0

#### facing_probas
- Mean = [0.16875  0.6525   0.90125  0.816875 0.676875]
- Standard deviation = [0.18816133 0.2896226  0.07606535 0.17075087 0.20877526]
- Max = [0.575 0.93  0.975 0.99  0.885]
- 75% = [0.23    0.85625 0.96    0.93375 0.8475 ]
- Median = [0.1275 0.765  0.9425 0.89   0.725 ]
- 25% = [0.      0.59    0.84875 0.74375 0.61875]
- Min = [0.    0.115 0.775 0.525 0.275]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 70.5 | 9.5 |
| Actual Positive | 19.25 | 0.75 |

### robot-5
#### accuracy
- Mean = 0.86875
- Standard deviation = 0.03689088640843427
- Max = 0.92
- 75% = 0.8875
- Median = 0.875
- 25% = 0.8525
- Min = 0.8

#### f1
- Mean = 0.48043263843579415
- Standard deviation = 0.22983995491960044
- Max = 0.7499999999999999
- 75% = 0.6059907834101383
- Median = 0.544973544973545
- 25% = 0.41137123745819393
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
- Mean = 0.34375
- Standard deviation = 0.18445443204217132
- Max = 0.6
- 75% = 0.4375
- Median = 0.375
- 25% = 0.2625
- Min = 0.0

#### facing_probas
- Mean = [0.065    0.15875  0.5275   0.765    0.820625]
- Standard deviation = [0.06712861 0.16472989 0.24392622 0.17277153 0.13335661]
- Max = [0.18  0.515 0.935 0.94  0.955]
- 75% = [0.1     0.24    0.61375 0.88625 0.9375 ]
- Median = [0.05   0.1225 0.57   0.8175 0.845 ]
- 25% = [0.     0.015  0.4675 0.7225 0.78  ]
- Min = [0.   0.   0.08 0.43 0.57]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 80.0 | 0.0 |
| Actual Positive | 13.125 | 6.875 |

### robot-6
#### accuracy
- Mean = 0.39999999999999997
- Standard deviation = 0.15652475842498528
- Max = 0.53
- 75% = 0.4825
- Median = 0.445
- 25% = 0.4125
- Min = 0.0

#### f1
- Mean = 0.5479597960206526
- Standard deviation = 0.21058803460274145
- Max = 0.6928104575163399
- 75% = 0.6509160166878287
- Median = 0.6159003831417624
- 25% = 0.5839497416151586
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
- Mean = 0.39999999999999997
- Standard deviation = 0.15652475842498528
- Max = 0.53
- 75% = 0.4825
- Median = 0.445
- 25% = 0.4125
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
| Actual Negative | 0.0 | 0.0 |
| Actual Positive | 60.0 | 40.0 |

