# ExtraTreesClassifier_ClusterCentroids_2022-01-19-01-20_no1
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
	- sampling_strategy_ = OrderedDict([(1, 36)])
	- estimator_ = KMeans(n_clusters=36, random_state=42)
	- voting_ = soft

- best_estimator
	- base_estimator = ExtraTreeClassifier()
	- n_estimators = 30
	- estimator_params = ('criterion', 'max_depth', 'min_samples_split', 'min_samples_leaf', 'min_weight_fraction_leaf', 'max_features', 'max_leaf_nodes', 'min_impurity_decrease', 'random_state', 'ccp_alpha')
	- bootstrap = True
	- oob_score = True
	- n_jobs = -1
	- random_state = 42
	- verbose = 0
	- warm_start = False
	- class_weight = None
	- max_samples = 0.09
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
	- oob_decision_function_ = [[0.85714286 0.14285714]
 [0.96666667 0.03333333]
 [0.92       0.08      ]
 [0.82142857 0.17857143]
 [0.89285714 0.10714286]
 [0.82758621 0.17241379]
 [0.84615385 0.15384615]
 [0.96428571 0.03571429]
 [0.91666667 0.08333333]
 [0.96428571 0.03571429]
 [0.96428571 0.03571429]
 [0.89285714 0.10714286]
 [0.67857143 0.32142857]
 [0.8        0.2       ]
 [0.9        0.1       ]
 [1.         0.        ]
 [1.         0.        ]
 [0.96551724 0.03448276]
 [0.67857143 0.32142857]
 [0.69230769 0.30769231]
 [0.93333333 0.06666667]
 [0.89285714 0.10714286]
 [0.82758621 0.17241379]
 [0.88888889 0.11111111]
 [0.77272727 0.22727273]
 [0.82142857 0.17857143]
 [0.96296296 0.03703704]
 [1.         0.        ]
 [0.85714286 0.14285714]
 [0.85185185 0.14814815]
 [0.96666667 0.03333333]
 [0.86206897 0.13793103]
 [0.96428571 0.03571429]
 [0.92857143 0.07142857]
 [0.82142857 0.17857143]
 [0.85714286 0.14285714]
 [0.15384615 0.84615385]
 [0.13793103 0.86206897]
 [0.17857143 0.82142857]
 [0.10344828 0.89655172]
 [0.48148148 0.51851852]
 [0.125      0.875     ]
 [0.33333333 0.66666667]
 [0.07692308 0.92307692]
 [0.23333333 0.76666667]
 [0.19230769 0.80769231]
 [0.12       0.88      ]
 [0.21428571 0.78571429]
 [0.10714286 0.89285714]
 [0.11538462 0.88461538]
 [0.11111111 0.88888889]
 [0.10344828 0.89655172]
 [0.22222222 0.77777778]
 [0.4137931  0.5862069 ]
 [0.10714286 0.89285714]
 [0.11538462 0.88461538]
 [0.23076923 0.76923077]
 [0.55172414 0.44827586]
 [0.03333333 0.96666667]
 [0.06896552 0.93103448]
 [0.2173913  0.7826087 ]
 [0.07407407 0.92592593]
 [0.32142857 0.67857143]
 [0.07407407 0.92592593]
 [0.06666667 0.93333333]
 [0.14285714 0.85714286]
 [0.11111111 0.88888889]
 [0.17241379 0.82758621]
 [0.10344828 0.89655172]
 [0.07142857 0.92857143]
 [0.39285714 0.60714286]
 [0.18518519 0.81481481]]
	- oob_score_ = 0.9861111111111112

#### Importance of features
- gp_auc_max = 0.18333333333333332
- gp_auc_min = 0.12666666666666665
- gp_auc_mean = 0.10666666666666666
- srmr = 0.08333333333333333
- gp_max_val_mean = 0.07888888888888888
- gp_max_val_max = 0.06689814814814815
- gp_max_val_range = 0.058333333333333334
- gp_max_val_min = 0.043333333333333335
- low_power = 0.04083333333333334
- tdoa_mean = 0.04
- hlbr = 0.023333333333333334
- gp_max_val_std = 0.022361111111111113
- tdoa_max = 0.019999999999999997
- gp_auc_std = 0.01666666666666667
- ac_std = 0.016666666666666666
- diff_std = 0.016666666666666666
- coe3[3] = 0.0125
- gp_max_ix_range = 0.011851851851851853
- diff_auc = 0.008333333333333335
- coe1[0] = 0.008333333333333333
- gp_auc_range = 0.008333333333333333
- tdoa_min = 0.006666666666666668
- high_power = 0.0
- coe1[1] = 0.0
- coe3[0] = 0.0
- coe3[1] = 0.0
- coe3[2] = 0.0
- ratio_max_to_10ms_ave_peaks = 0.0
- ratio_max_to_9th_ave_peaks = 0.0
- ac_auc = 0.0
- gp_max_ix_std = 0.0
- gp_max_ix_min = 0.0
- gp_max_ix_max = 0.0
- gp_max_ix_mean = 0.0
- tdoa_std = 0.0
- tdoa_range = 0.0

## Evaluation
cv = 8
### robot-1
#### accuracy
- Mean = 0.945
- Standard deviation = 0.018027756377319924
- Max = 0.97
- 75% = 0.96
- Median = 0.945
- 25% = 0.9375
- Min = 0.91

#### f1
- Mean = 0.8763005394424216
- Standard deviation = 0.03721497574647003
- Max = 0.9302325581395349
- 75% = 0.9090909090909091
- Median = 0.8792270531400967
- 25% = 0.8468023255813953
- Min = 0.8163265306122449

#### precision
- Mean = 0.8034658151693383
- Standard deviation = 0.05349139031037627
- Max = 0.8695652173913043
- 75% = 0.8375
- Median = 0.8166666666666667
- 25% = 0.7792642140468228
- Min = 0.6896551724137931

#### recall
- Mean = 0.96875
- Standard deviation = 0.05555121510822243
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 0.975
- Min = 0.85

#### facing_probas
- Mean = [0.90645833 0.644375   0.21270833 0.07958333 0.04979167]
- Standard deviation = [0.01772548 0.03961567 0.07178739 0.02902047 0.02164161]
- Max = [0.94666667 0.69333333 0.32333333 0.14166667 0.10166667]
- 75% = [0.91166667 0.6775     0.29041667 0.08666667 0.05208333]
- Median = [0.90416667 0.65083333 0.17916667 0.0775     0.04416667]
- 25% = [0.89458333 0.61458333 0.14875    0.06708333 0.03791667]
- Min = [0.885      0.57833333 0.14       0.03166667 0.02833333]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 75.125 | 4.875 |
| Actual Positive | 0.625 | 19.375 |

### robot-2
#### accuracy
- Mean = 0.945
- Standard deviation = 0.018027756377319924
- Max = 0.97
- 75% = 0.96
- Median = 0.945
- 25% = 0.9375
- Min = 0.91

#### f1
- Mean = 0.8434821494712387
- Standard deviation = 0.060634748058317006
- Max = 0.9189189189189189
- 75% = 0.888888888888889
- Median = 0.8535714285714285
- 25% = 0.8203497615262321
- Min = 0.7096774193548387

#### precision
- Mean = 0.9665441176470588
- Standard deviation = 0.0585090398332987
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 0.9705882352941176
- Min = 0.85

#### recall
- Mean = 0.7562500000000001
- Standard deviation = 0.09164298936634487
- Max = 0.85
- 75% = 0.8125
- Median = 0.775
- 25% = 0.7375
- Min = 0.55

#### facing_probas
- Mean = [0.785625   0.77479167 0.61354167 0.21375    0.04458333]
- Standard deviation = [0.05590131 0.03609822 0.05949111 0.09293722 0.01779025]
- Max = [0.85666667 0.81666667 0.705      0.39166667 0.08666667]
- 75% = [0.81708333 0.80708333 0.65125    0.27333333 0.04375   ]
- Median = [0.79083333 0.78083333 0.6175     0.19916667 0.04      ]
- 25% = [0.76541667 0.73958333 0.59333333 0.14958333 0.03666667]
- Min = [0.66666667 0.72333333 0.49333333 0.08166667 0.025     ]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 79.375 | 0.625 |
| Actual Positive | 4.875 | 15.125 |

### robot-3
#### accuracy
- Mean = 0.9775
- Standard deviation = 0.02277608394786073
- Max = 1.0
- 75% = 0.99
- Median = 0.98
- 25% = 0.98
- Min = 0.92

#### f1
- Mean = 0.9360239541160593
- Standard deviation = 0.07258768940587242
- Max = 1.0
- 75% = 0.9743589743589743
- Median = 0.9473684210526316
- 25% = 0.9473684210526316
- Min = 0.7499999999999999

#### precision
- Mean = 1.0
- Standard deviation = 0.0
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 1.0
- Min = 1.0

#### recall
- Mean = 0.8875
- Standard deviation = 0.11388041973930374
- Max = 1.0
- 75% = 0.95
- Median = 0.9
- 25% = 0.9
- Min = 0.6

#### facing_probas
- Mean = [0.32354167 0.799375   0.86708333 0.78625    0.19895833]
- Standard deviation = [0.07764072 0.03855855 0.0450135  0.04678371 0.06569044]
- Max = [0.47       0.865      0.93       0.86       0.29166667]
- 75% = [0.36625    0.82208333 0.90041667 0.81291667 0.25791667]
- Median = [0.32666667 0.8        0.86916667 0.78833333 0.18416667]
- 25% = [0.26458333 0.78208333 0.835      0.76208333 0.15416667]
- Min = [0.22166667 0.74333333 0.80333333 0.69666667 0.1       ]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 80.0 | 0.0 |
| Actual Positive | 2.25 | 17.75 |

### robot-4
#### accuracy
- Mean = 0.94375
- Standard deviation = 0.016535945694153665
- Max = 0.97
- 75% = 0.9524999999999999
- Median = 0.945
- 25% = 0.9349999999999999
- Min = 0.92

#### f1
- Mean = 0.8378472595771357
- Standard deviation = 0.05278395105321692
- Max = 0.9189189189189189
- 75% = 0.8665413533834586
- Median = 0.8403361344537814
- 25% = 0.8120915032679739
- Min = 0.7499999999999999

#### precision
- Mean = 0.9774305555555556
- Standard deviation = 0.042773211787343474
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 0.9861111111111112
- Min = 0.875

#### recall
- Mean = 0.7374999999999999
- Standard deviation = 0.07806247497997998
- Max = 0.85
- 75% = 0.775
- Median = 0.725
- 25% = 0.7
- Min = 0.6

#### facing_probas
- Mean = [0.06041667 0.29       0.78229167 0.89229167 0.66291667]
- Standard deviation = [0.02316532 0.06244998 0.06700403 0.0224836  0.0698647 ]
- Max = [0.09333333 0.39       0.86833333 0.92333333 0.75666667]
- 75% = [0.08166667 0.31541667 0.82166667 0.90791667 0.715     ]
- Median = [0.06       0.30416667 0.78833333 0.89416667 0.67666667]
- 25% = [0.045      0.25791667 0.75625    0.87208333 0.62666667]
- Min = [0.02333333 0.16833333 0.65833333 0.86       0.53666667]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 79.625 | 0.375 |
| Actual Positive | 5.25 | 14.75 |

### robot-5
#### accuracy
- Mean = 0.99125
- Standard deviation = 0.007806247497998005
- Max = 1.0
- 75% = 1.0
- Median = 0.99
- 25% = 0.9875
- Min = 0.98

#### f1
- Mean = 0.9781659824984601
- Standard deviation = 0.01959302308138803
- Max = 1.0
- 75% = 1.0
- Median = 0.975609756097561
- 25% = 0.9688644688644689
- Min = 0.9473684210526316

#### precision
- Mean = 0.9767316017316017
- Standard deviation = 0.03253510284752689
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 0.9523809523809523
- Min = 0.9090909090909091

#### recall
- Mean = 0.98125
- Standard deviation = 0.03479852726768764
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 0.9875
- Min = 0.9

#### facing_probas
- Mean = [0.05333333 0.06229167 0.270625   0.81895833 0.82291667]
- Standard deviation = [0.02996526 0.02307803 0.05001345 0.04172444 0.05014389]
- Max = [0.11166667 0.09333333 0.325      0.88166667 0.88666667]
- 75% = [0.075      0.08333333 0.30958333 0.85458333 0.85833333]
- Median = [0.04083333 0.0625     0.27583333 0.81583333 0.835     ]
- 25% = [0.0325     0.045      0.26041667 0.78208333 0.78875   ]
- Min = [0.01666667 0.02666667 0.16166667 0.76166667 0.745     ]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 79.5 | 0.5 |
| Actual Positive | 0.375 | 19.625 |

### robot-6
#### accuracy
- Mean = 0.86625
- Standard deviation = 0.03533323506275641
- Max = 0.9
- 75% = 0.9
- Median = 0.875
- 25% = 0.8475
- Min = 0.81

#### f1
- Mean = 0.9279428988450995
- Standard deviation = 0.020564929325263985
- Max = 0.9473684210526316
- 75% = 0.9473684210526316
- Median = 0.9333257480942087
- 25% = 0.9173052931741223
- Min = 0.8950276243093923

#### precision
- Mean = 1.0
- Standard deviation = 0.0
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 1.0
- Min = 1.0

#### recall
- Mean = 0.86625
- Standard deviation = 0.03533323506275641
- Max = 0.9
- 75% = 0.9
- Median = 0.875
- 25% = 0.8475
- Min = 0.81

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
| Actual Positive | 13.375 | 86.625 |

