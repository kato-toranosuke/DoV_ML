# ExtraTreesClassifier_RandomOverSampler_2022-01-19-02-42_no3
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
	- sampling_strategy_ = OrderedDict([(0, 3)])
	- shrinkage_ = None
	- sample_indices_ = [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23
 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47
 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71
 72 73 74 61 29 13]

- best_estimator
	- base_estimator = ExtraTreeClassifier()
	- n_estimators = 10
	- estimator_params = ('criterion', 'max_depth', 'min_samples_split', 'min_samples_leaf', 'min_weight_fraction_leaf', 'max_features', 'max_leaf_nodes', 'min_impurity_decrease', 'random_state', 'ccp_alpha')
	- bootstrap = True
	- oob_score = True
	- n_jobs = -1
	- random_state = 42
	- verbose = 0
	- warm_start = False
	- class_weight = None
	- max_samples = 0.5
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
	- oob_decision_function_ = [[0.         1.        ]
 [0.         1.        ]
 [0.         1.        ]
 [0.16666667 0.83333333]
 [0.02380952 0.97619048]
 [0.3015873  0.6984127 ]
 [0.80952381 0.19047619]
 [0.40136054 0.59863946]
 [0.34183673 0.65816327]
 [1.         0.        ]
 [1.         0.        ]
 [1.         0.        ]
 [1.         0.        ]
 [1.         0.        ]
 [1.         0.        ]
 [0.03703704 0.96296296]
 [0.83333333 0.16666667]
 [0.05555556 0.94444444]
 [0.         1.        ]
 [0.         1.        ]
 [0.25       0.75      ]
 [0.08333333 0.91666667]
 [0.0952381  0.9047619 ]
 [0.         1.        ]
 [0.95833333 0.04166667]
 [0.71428571 0.28571429]
 [0.26666667 0.73333333]
 [1.         0.        ]
 [1.         0.        ]
 [1.         0.        ]
 [1.         0.        ]
 [1.         0.        ]
 [1.         0.        ]
 [0.69444444 0.30555556]
 [0.38244048 0.61755952]
 [0.32993197 0.67006803]
 [0.0625     0.9375    ]
 [0.         1.        ]
 [0.         1.        ]
 [0.08333333 0.91666667]
 [0.         1.        ]
 [0.         1.        ]
 [0.61564626 0.38435374]
 [0.27380952 0.72619048]
 [0.58994709 0.41005291]
 [1.         0.        ]
 [1.         0.        ]
 [1.         0.        ]
 [0.66666667 0.33333333]
 [0.6        0.4       ]
 [0.76190476 0.23809524]
 [0.08333333 0.91666667]
 [0.         1.        ]
 [0.05555556 0.94444444]
 [0.         1.        ]
 [0.         1.        ]
 [0.         1.        ]
 [0.         1.        ]
 [0.         1.        ]
 [0.05952381 0.94047619]
 [1.         0.        ]
 [1.         0.        ]
 [1.         0.        ]
 [1.         0.        ]
 [1.         0.        ]
 [1.         0.        ]
 [0.82993197 0.17006803]
 [1.         0.        ]
 [0.85714286 0.14285714]
 [0.14285714 0.85714286]
 [0.         1.        ]
 [0.         1.        ]
 [0.07142857 0.92857143]
 [0.         1.        ]
 [0.22857143 0.77142857]
 [1.         0.        ]
 [1.         0.        ]
 [1.         0.        ]]
	- oob_score_ = 0.9230769230769231

#### Importance of features
- gp_max_val_max = 0.18792860398544703
- gp_auc_min = 0.12658187428912385
- high_power = 0.10216217269621986
- gp_auc_mean = 0.0726100796900908
- gp_max_val_std = 0.05441882200693783
- diff_std = 0.05422521889525457
- gp_max_ix_std = 0.051864163257354365
- gp_max_val_mean = 0.049227043864140646
- tdoa_min = 0.041944403145339794
- coe1[0] = 0.041276455026455015
- tdoa_range = 0.03658536585365855
- diff_auc = 0.035224419334588836
- tdoa_max = 0.032462346413000394
- srmr = 0.03227236756629069
- gp_auc_max = 0.032012427227944465
- gp_max_ix_max = 0.025319165291320313
- gp_auc_std = 0.010086206896551726
- gp_auc_range = 0.009185390681565136
- gp_max_ix_range = 0.0036129928782352
- coe3[3] = 0.0010004810004810025
- low_power = 0.0
- hlbr = 0.0
- coe1[1] = 0.0
- coe3[0] = 0.0
- coe3[1] = 0.0
- coe3[2] = 0.0
- ratio_max_to_10ms_ave_peaks = 0.0
- ratio_max_to_9th_ave_peaks = 0.0
- ac_std = 0.0
- ac_auc = 0.0
- gp_max_val_range = 0.0
- gp_max_val_min = 0.0
- gp_max_ix_min = 0.0
- gp_max_ix_mean = 0.0
- tdoa_std = 0.0
- tdoa_mean = 0.0

## Evaluation
cv = 8
### robot-1
#### accuracy
- Mean = 0.96875
- Standard deviation = 0.014523687548277826
- Max = 0.99
- 75% = 0.98
- Median = 0.97
- 25% = 0.96
- Min = 0.94

#### f1
- Mean = 0.9274366129525936
- Standard deviation = 0.03166061726178691
- Max = 0.975609756097561
- 75% = 0.9523809523809523
- Median = 0.9302325581395349
- 25% = 0.9068181818181817
- Min = 0.8695652173913044

#### precision
- Mean = 0.8765321634886852
- Standard deviation = 0.05232199199387558
- Max = 0.9523809523809523
- 75% = 0.9090909090909091
- Median = 0.8847826086956522
- 25% = 0.8605072463768115
- Min = 0.7692307692307693

#### recall
- Mean = 0.9875
- Standard deviation = 0.03307189138830738
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 1.0
- Min = 0.9

#### facing_probas
- Mean = [0.99001935 0.84205357 0.15827679 0.0588006  0.01030208]
- Standard deviation = [0.00885656 0.06360808 0.04935765 0.04341059 0.00670794]
- Max = [1.         0.91575    0.245      0.14958333 0.025     ]
- 75% = [0.998125   0.8934375  0.17681548 0.0725     0.0121875 ]
- Median = [0.99128571 0.85842262 0.13708333 0.050625   0.00916667]
- 25% = [0.98325    0.811      0.12379762 0.02404762 0.005625  ]
- Min = [0.97375    0.73291667 0.11316667 0.011      0.002     ]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 77.125 | 2.875 |
| Actual Positive | 0.25 | 19.75 |

### robot-2
#### accuracy
- Mean = 0.96875
- Standard deviation = 0.014523687548277826
- Max = 0.99
- 75% = 0.98
- Median = 0.97
- 25% = 0.96
- Min = 0.94

#### f1
- Mean = 0.9149189943694588
- Standard deviation = 0.043190333396326185
- Max = 0.9743589743589743
- 75% = 0.9473684210526316
- Median = 0.9189189189189189
- 25% = 0.8972222222222223
- Min = 0.8235294117647058

#### precision
- Mean = 0.9875
- Standard deviation = 0.03307189138830738
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 1.0
- Min = 0.9

#### recall
- Mean = 0.85625
- Standard deviation = 0.07261843774138907
- Max = 0.95
- 75% = 0.9
- Median = 0.875
- 25% = 0.8375
- Min = 0.7

#### facing_probas
- Mean = [0.9189628  0.91085565 0.7225878  0.1686131  0.01291667]
- Standard deviation = [0.03223547 0.03512209 0.05937881 0.08180187 0.01697629]
- Max = [0.951      0.95666667 0.79416667 0.29       0.055     ]
- 75% = [0.94721726 0.93992857 0.78188095 0.25458333 0.014375  ]
- Median = [0.93425    0.90823214 0.71404167 0.14297619 0.0075    ]
- 25% = [0.88495833 0.89425    0.69893155 0.10992262 0.001875  ]
- Min = [0.86766667 0.85166667 0.60379762 0.04916667 0.        ]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 79.75 | 0.25 |
| Actual Positive | 2.875 | 17.125 |

### robot-3
#### accuracy
- Mean = 0.97125
- Standard deviation = 0.01763341997458237
- Max = 0.99
- 75% = 0.99
- Median = 0.975
- 25% = 0.95
- Min = 0.95

#### f1
- Mean = 0.9200991043096306
- Standard deviation = 0.05180236015191925
- Max = 0.9743589743589743
- 75% = 0.9743589743589743
- Median = 0.9331436699857752
- 25% = 0.8571428571428571
- Min = 0.8571428571428571

#### precision
- Mean = 1.0
- Standard deviation = 0.0
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 1.0
- Min = 1.0

#### recall
- Mean = 0.85625
- Standard deviation = 0.08816709987291177
- Max = 0.95
- 75% = 0.95
- Median = 0.875
- 25% = 0.75
- Min = 0.75

#### facing_probas
- Mean = [0.29310268 0.93170833 0.9620253  0.93040476 0.11501488]
- Standard deviation = [0.05260367 0.05050674 0.03309914 0.03674528 0.06866604]
- Max = [0.37267857 0.995      0.99428571 0.985      0.265     ]
- 75% = [0.33010417 0.96604167 0.98666667 0.95443452 0.14238095]
- Median = [0.27708929 0.94329167 0.97125    0.933375   0.094375  ]
- 25% = [0.24805655 0.9134375  0.9506875  0.90625    0.06552083]
- Min = [0.23791667 0.82316667 0.88916667 0.86708333 0.04333333]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 80.0 | 0.0 |
| Actual Positive | 2.875 | 17.125 |

### robot-4
#### accuracy
- Mean = 0.9187500000000001
- Standard deviation = 0.025217801252290013
- Max = 0.95
- 75% = 0.9325
- Median = 0.93
- 25% = 0.905
- Min = 0.87

#### f1
- Mean = 0.7684513419807537
- Standard deviation = 0.07121084161518562
- Max = 0.8571428571428571
- 75% = 0.8212669683257918
- Median = 0.793939393939394
- 25% = 0.7211302211302213
- Min = 0.6285714285714286

#### precision
- Mean = 0.8995693419068032
- Standard deviation = 0.10067040799085031
- Max = 1.0
- 75% = 1.0
- Median = 0.9282051282051282
- 25% = 0.8227554179566563
- Min = 0.7333333333333333

#### recall
- Mean = 0.675
- Standard deviation = 0.075
- Max = 0.8
- 75% = 0.7124999999999999
- Median = 0.675
- 25% = 0.6375
- Min = 0.55

#### facing_probas
- Mean = [0.02137649 0.27976042 0.89394048 0.98007292 0.75576488]
- Standard deviation = [0.02330096 0.07116745 0.05211185 0.00964837 0.04646118]
- Max = [0.08166667 0.45416667 0.95916667 0.995      0.84666667]
- 75% = [0.01803571 0.285125   0.93860119 0.985125   0.78852679]
- Median = [0.01479167 0.26529167 0.90516667 0.98354167 0.74275   ]
- 25% = [0.00934524 0.24389583 0.84445833 0.9719375  0.7245    ]
- Min = [0.005      0.20591667 0.8215     0.96458333 0.69708333]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 78.375 | 1.625 |
| Actual Positive | 6.5 | 13.5 |

### robot-5
#### accuracy
- Mean = 0.9824999999999999
- Standard deviation = 0.01561249499599601
- Max = 1.0
- 75% = 0.9924999999999999
- Median = 0.99
- 25% = 0.9675
- Min = 0.96

#### f1
- Mean = 0.9526280501890259
- Standard deviation = 0.04362123206118847
- Max = 1.0
- 75% = 0.9817073170731707
- Median = 0.9743589743589743
- 25% = 0.9114114114114114
- Min = 0.888888888888889

#### precision
- Mean = 0.9940476190476191
- Standard deviation = 0.01574851970871782
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 1.0
- Min = 0.9523809523809523

#### recall
- Mean = 0.91875
- Standard deviation = 0.08267972847076845
- Max = 1.0
- 75% = 1.0
- Median = 0.95
- 25% = 0.8375
- Min = 0.8

#### facing_probas
- Mean = [0.01171875 0.010625   0.24137649 0.94775446 0.91763095]
- Standard deviation = [0.01244857 0.01133264 0.06346152 0.01959636 0.04884446]
- Max = [0.04125    0.03333333 0.35434524 0.9802381  0.96988095]
- 75% = [0.01416667 0.01375    0.291125   0.95729167 0.9515625 ]
- Median = [0.00875    0.00583333 0.23425    0.95564881 0.944875  ]
- 25% = [0.00375    0.00375    0.1931875  0.9303125  0.86179167]
- Min = [0.         0.         0.15508333 0.91675    0.85083333]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 79.875 | 0.125 |
| Actual Positive | 1.625 | 18.375 |

### robot-6
#### accuracy
- Mean = 0.8587499999999999
- Standard deviation = 0.03655047879303362
- Max = 0.91
- 75% = 0.88
- Median = 0.865
- 25% = 0.8525
- Min = 0.78

#### f1
- Mean = 0.92358399690203
- Standard deviation = 0.02157186555397817
- Max = 0.9528795811518325
- 75% = 0.9361702127659575
- Median = 0.9276062331090794
- 25% = 0.9203243433809272
- Min = 0.8764044943820225

#### precision
- Mean = 1.0
- Standard deviation = 0.0
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 1.0
- Min = 1.0

#### recall
- Mean = 0.8587499999999999
- Standard deviation = 0.03655047879303362
- Max = 0.91
- 75% = 0.88
- Median = 0.865
- 25% = 0.8525
- Min = 0.78

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
| Actual Positive | 14.125 | 85.875 |

