# ExtraTreesClassifier_ClusterCentroids_2022-01-17-05-18_no1
## Constants
- CSV_PATH = ../out/csv/experiment
- OUTPUT_PATH = ../out/experiment_result/data_of_2022-01-13_eval_system/AGC-0angle-3m
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
- DISTANCE = [3]
- AGC_STATUS = ['AGC']

## Loaded CSV
- 2021-12-27_AGC.csv
- 2022-01-10_NoAGC.csv
- 2022-01-13_raspi_48000Hz_w1_N2^12_overlap80.csv

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
	- sampling_strategy_ = OrderedDict([(0, 15)])
	- estimator_ = KMeans(n_clusters=15, random_state=42)
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
	- min_samples_split = 2
	- min_samples_leaf = 1
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
- gp_max_val_max = 0.2625555555555556
- gp_auc_min = 0.1816666666666667
- diff_auc = 0.17647058823529413
- gp_auc_max = 0.10805228758169937
- srmr = 0.07647058823529414
- coe1[1] = 0.05475113122171948
- gp_auc_std = 0.031474358974358976
- gp_max_val_std = 0.023473856209150337
- gp_max_ix_mean = 0.02138888888888889
- gp_auc_mean = 0.019111111111111117
- gp_max_val_mean = 0.014640522875816991
- tdoa_mean = 0.012500000000000004
- gp_max_val_min = 0.0058333333333333345
- gp_auc_range = 0.0058333333333333345
- ratio_max_to_10ms_ave_peaks = 0.005777777777777782
- low_power = 0.0
- high_power = 0.0
- hlbr = 0.0
- coe1[0] = 0.0
- coe3[0] = 0.0
- coe3[1] = 0.0
- coe3[2] = 0.0
- coe3[3] = 0.0
- ratio_max_to_9th_ave_peaks = 0.0
- ac_std = 0.0
- ac_auc = 0.0
- diff_std = 0.0
- gp_max_val_range = 0.0
- gp_max_ix_std = 0.0
- gp_max_ix_range = 0.0
- gp_max_ix_min = 0.0
- gp_max_ix_max = 0.0
- tdoa_std = 0.0
- tdoa_range = 0.0
- tdoa_min = 0.0
- tdoa_max = 0.0

## Evaluation
cv = 8
### robot-1
#### accuracy
- Mean = 0.9299999999999999
- Standard deviation = 0.041231056256176596
- Max = 0.97
- 75% = 0.96
- Median = 0.95
- 25% = 0.9075
- Min = 0.84

#### f1
- Mean = 0.8523364454154099
- Standard deviation = 0.07176305340854201
- Max = 0.9302325581395349
- 75% = 0.9090909090909091
- Median = 0.8834688346883468
- 25% = 0.8054267161410018
- Min = 0.7142857142857143

#### precision
- Mean = 0.7683648503129388
- Standard deviation = 0.10164425181862784
- Max = 0.8695652173913043
- 75% = 0.8392857142857143
- Median = 0.8166666666666667
- 25% = 0.7036637931034483
- Min = 0.5555555555555556

#### recall
- Mean = 0.96875
- Standard deviation = 0.05555121510822243
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 0.975
- Min = 0.85

#### facing_probas
- Mean = [0.960625 0.579375 0.01875  0.008125 0.015625]
- Standard deviation = [0.03643809 0.18395715 0.03218598 0.01477699 0.02799972]
- Max = [0.995 0.795 0.1   0.045 0.085]
- 75% = [0.98625 0.7425  0.015   0.0075  0.015  ]
- Median = [0.975  0.5825 0.005  0.     0.    ]
- 25% = [0.94875 0.5     0.      0.      0.     ]
- Min = [0.9   0.195 0.    0.    0.   ]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 73.625 | 6.375 |
| Actual Positive | 0.625 | 19.375 |

### robot-2
#### accuracy
- Mean = 0.78125
- Standard deviation = 0.07061117121249301
- Max = 0.9
- 75% = 0.8125
- Median = 0.795
- 25% = 0.7575000000000001
- Min = 0.66

#### f1
- Mean = 0.5020432286389733
- Standard deviation = 0.16634158844093136
- Max = 0.7222222222222223
- 75% = 0.5864361702127661
- Median = 0.5623100303951367
- 25% = 0.4601063829787234
- Min = 0.15

#### precision
- Mean = 0.4703230218855219
- Standard deviation = 0.1799631082098427
- Max = 0.8125
- 75% = 0.5252525252525252
- Median = 0.4907407407407407
- 25% = 0.41782407407407407
- Min = 0.15

#### recall
- Mean = 0.55
- Standard deviation = 0.17677669529663687
- Max = 0.7
- 75% = 0.6625
- Median = 0.625
- 25% = 0.5125000000000001
- Min = 0.15

#### facing_probas
- Mean = [0.659375 0.85875  0.165    0.00875  0.013125]
- Standard deviation = [0.13737352 0.07857123 0.11056672 0.01268611 0.02135086]
- Max = [0.915 0.975 0.3   0.04  0.065]
- 75% = [0.705   0.91375 0.26875 0.01    0.02   ]
- Median = [0.6375 0.86   0.17   0.005  0.    ]
- 25% = [0.595   0.81875 0.06375 0.      0.     ]
- Min = [0.425 0.715 0.01  0.    0.   ]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 67.125 | 12.875 |
| Actual Positive | 9.0 | 11.0 |

### robot-3
#### accuracy
- Mean = 0.8025
- Standard deviation = 0.09270248108869578
- Max = 0.96
- 75% = 0.8525
- Median = 0.81
- 25% = 0.77
- Min = 0.65

#### f1
- Mean = 0.41418219841555065
- Standard deviation = 0.2479127028076162
- Max = 0.8947368421052632
- 75% = 0.5091277890466531
- Median = 0.4056695992179863
- 25% = 0.3068910256410256
- Min = 0.058823529411764705

#### precision
- Mean = 0.524639468718416
- Standard deviation = 0.2869644898694179
- Max = 0.9444444444444444
- 75% = 0.7301587301587302
- Median = 0.5419580419580419
- 25% = 0.4013157894736842
- Min = 0.07142857142857142

#### recall
- Mean = 0.35
- Standard deviation = 0.2318404623873926
- Max = 0.85
- 75% = 0.38749999999999996
- Median = 0.32499999999999996
- 25% = 0.25
- Min = 0.05

#### facing_probas
- Mean = [0.040625 0.901875 0.97875  0.615625 0.014375]
- Standard deviation = [0.03395194 0.08234597 0.02803458 0.2213515  0.01445629]
- Max = [0.11  0.965 1.    0.925 0.04 ]
- 75% = [0.05375 0.95    1.      0.7875  0.02625]
- Median = [0.04  0.94  0.99  0.605 0.01 ]
- 25% = [0.015   0.90625 0.975   0.505   0.     ]
- Min = [0.    0.715 0.92  0.29  0.   ]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 73.25 | 6.75 |
| Actual Positive | 13.0 | 7.0 |

### robot-4
#### accuracy
- Mean = 0.79375
- Standard deviation = 0.08350711047569542
- Max = 0.88
- 75% = 0.855
- Median = 0.815
- 25% = 0.77
- Min = 0.62

#### f1
- Mean = 0.5525054550269414
- Standard deviation = 0.20064468533350452
- Max = 0.75
- 75% = 0.6754049445865302
- Median = 0.6196990424076607
- 25% = 0.5099667774086378
- Min = 0.13636363636363635

#### precision
- Mean = 0.47966956403489147
- Standard deviation = 0.16846467627309453
- Max = 0.6428571428571429
- 75% = 0.6097475455820477
- Median = 0.5303970223325062
- 25% = 0.4381559220389805
- Min = 0.125

#### recall
- Mean = 0.65625
- Standard deviation = 0.2542605700850999
- Max = 0.95
- 75% = 0.7875
- Median = 0.725
- 25% = 0.6124999999999999
- Min = 0.15

#### facing_probas
- Mean = [0.025    0.061875 0.741875 0.96125  0.26875 ]
- Standard deviation = [0.03807887 0.06299492 0.1473927  0.0183286  0.16691596]
- Max = [0.11  0.205 0.955 1.    0.535]
- 75% = [0.0375  0.0775  0.8575  0.965   0.37375]
- Median = [0.     0.06   0.75   0.955  0.2925]
- 25% = [0.     0.0075 0.61   0.9525 0.09  ]
- Min = [0.    0.    0.51  0.94  0.055]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 66.25 | 13.75 |
| Actual Positive | 6.875 | 13.125 |

### robot-5
#### accuracy
- Mean = 0.86125
- Standard deviation = 0.03218598297395933
- Max = 0.91
- 75% = 0.8775
- Median = 0.86
- 25% = 0.8474999999999999
- Min = 0.8

#### f1
- Mean = 0.44390910761878505
- Standard deviation = 0.20544226241442803
- Max = 0.7096774193548387
- 75% = 0.5555555555555556
- Median = 0.4615384615384615
- 25% = 0.38333333333333336
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
- Mean = 0.30625
- Standard deviation = 0.16092991486979666
- Max = 0.55
- 75% = 0.38749999999999996
- Median = 0.3
- 25% = 0.2375
- Min = 0.0

#### facing_probas
- Mean = [0.015    0.029375 0.048125 0.8775   0.938125]
- Standard deviation = [0.02136001 0.04626267 0.02370885 0.0792149  0.04636388]
- Max = [0.055 0.135 0.09  1.    0.99 ]
- 75% = [0.02625 0.04    0.055   0.91375 0.97625]
- Median = [0.     0.     0.055  0.8875 0.9525]
- 25% = [0.      0.      0.04125 0.8475  0.91   ]
- Min = [0.    0.    0.01  0.71  0.865]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 80.0 | 0.0 |
| Actual Positive | 13.875 | 6.125 |

### robot-6
#### accuracy
- Mean = 0.5662499999999999
- Standard deviation = 0.14755825120947996
- Max = 0.76
- 75% = 0.645
- Median = 0.605
- 25% = 0.5249999999999999
- Min = 0.28

#### f1
- Mean = 0.710644953115048
- Standard deviation = 0.1323601007795276
- Max = 0.8636363636363636
- 75% = 0.7838966130613134
- Median = 0.7535916750795992
- 25% = 0.6848737570453192
- Min = 0.43750000000000006

#### precision
- Mean = 1.0
- Standard deviation = 0.0
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 1.0
- Min = 1.0

#### recall
- Mean = 0.5662499999999999
- Standard deviation = 0.14755825120947996
- Max = 0.76
- 75% = 0.645
- Median = 0.605
- 25% = 0.5249999999999999
- Min = 0.28

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
| Actual Positive | 43.375 | 56.625 |

