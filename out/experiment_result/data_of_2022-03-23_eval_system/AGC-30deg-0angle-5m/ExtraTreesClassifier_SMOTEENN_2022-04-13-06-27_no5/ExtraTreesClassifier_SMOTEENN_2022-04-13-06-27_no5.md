# ExtraTreesClassifier_SMOTEENN_2022-04-13-06-27_no5
## Constants
- CSV_PATH = ../out/csv/experiment
- OUTPUT_PATH = ../out/experiment_result/data_of_2022-03-23_eval_system/AGC-30deg-0angle-5m
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
- DISTANCE = [5]
- AGC_STATUS = ['AGC-30deg']
- ANGLES = [30, 60, 90, 120, 150]

## Loaded CSV
- 2022-03-23_raspi_48000Hz_w1_N2^12_overlap80_all.csv

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
	- n_estimators = 30
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
	- oob_decision_function_ = [[0.85       0.15      ]
 [0.9047619  0.0952381 ]
 [0.76923077 0.23076923]
 [0.95       0.05      ]
 [0.94736842 0.05263158]
 [0.29411765 0.70588235]
 [1.         0.        ]
 [1.         0.        ]
 [0.77777778 0.22222222]
 [0.58823529 0.41176471]
 [0.21052632 0.78947368]
 [0.6        0.4       ]
 [1.         0.        ]
 [0.92857143 0.07142857]
 [1.         0.        ]
 [0.5        0.5       ]
 [1.         0.        ]
 [1.         0.        ]
 [0.77777778 0.22222222]
 [1.         0.        ]
 [0.80952381 0.19047619]
 [0.35       0.65      ]
 [0.55       0.45      ]
 [0.10526316 0.89473684]
 [0.33333333 0.66666667]
 [0.4        0.6       ]
 [0.16666667 0.83333333]
 [0.0625     0.9375    ]
 [0.29411765 0.70588235]
 [0.05555556 0.94444444]
 [0.14285714 0.85714286]
 [0.06666667 0.93333333]
 [0.2173913  0.7826087 ]]
	- oob_score_ = 0.9090909090909091

#### Importance of features
- gp_auc_mean = 0.12258778258778259
- coe3[3] = 0.08670899470899471
- ac_auc = 0.07636363636363637
- gp_auc_min = 0.07504273504273504
- coe3[2] = 0.07325198707016889
- gp_auc_max = 0.0698989898989899
- coe1[0] = 0.0591957671957672
- diff_std = 0.05586566968385151
- hlbr = 0.04990633608815427
- gp_max_val_max = 0.04126984126984126
- low_power = 0.035555555555555556
- gp_max_val_mean = 0.03487603305785124
- high_power = 0.03333333333333333
- diff_auc = 0.023151515151515156
- tdoa_range = 0.02222222222222222
- gp_max_val_range = 0.01861471861471862
- gp_max_ix_max = 0.017777777777777778
- tdoa_max = 0.017777777777777778
- coe1[1] = 0.015555555555555553
- ratio_max_to_10ms_ave_peaks = 0.015488215488215488
- gp_max_val_std = 0.014545454545454547
- gp_auc_range = 0.010774410774410773
- gp_max_val_min = 0.007936507936507938
- ratio_max_to_9th_ave_peaks = 0.007619047619047621
- ac_std = 0.007407407407407407
- srmr = 0.007272727272727273
- coe3[0] = 0.0
- coe3[1] = 0.0
- gp_max_ix_std = 0.0
- gp_max_ix_range = 0.0
- gp_max_ix_min = 0.0
- gp_max_ix_mean = 0.0
- gp_auc_std = 0.0
- tdoa_std = 0.0
- tdoa_min = 0.0
- tdoa_mean = 0.0

## Evaluation
cv = 8
### robot-1
#### accuracy
- Mean = 0.7949999999999999
- Standard deviation = 0.05291502622129182
- Max = 0.85
- 75% = 0.8325
- Median = 0.815
- 25% = 0.775
- Min = 0.69

#### f1
- Mean = 0.5244435485263523
- Standard deviation = 0.11099015601950035
- Max = 0.6666666666666666
- 75% = 0.6184012066365008
- Median = 0.5593495934959349
- 25% = 0.4
- Min = 0.3673469387755102

#### precision
- Mean = 0.5051137437587294
- Standard deviation = 0.10813020399400582
- Max = 0.631578947368421
- 75% = 0.5785714285714285
- Median = 0.543778801843318
- 25% = 0.44999999999999996
- Min = 0.3103448275862069

#### recall
- Mean = 0.575
- Standard deviation = 0.16201851746019652
- Max = 0.8
- 75% = 0.65
- Median = 0.6
- 25% = 0.45
- Min = 0.3

#### facing_probas
- Mean = [0.61041667 0.34208333 0.303125   0.22520833 0.19958333]
- Standard deviation = [0.13160798 0.23162132 0.22854376 0.27489573 0.24779549]
- Max = [0.845      0.805      0.79       0.89666667 0.8       ]
- 75% = [0.68375    0.44666667 0.37875    0.29       0.26708333]
- Median = [0.6125     0.26916667 0.22833333 0.11666667 0.09166667]
- 25% = [0.54125    0.17708333 0.12875    0.03916667 0.03458333]
- Min = [0.38666667 0.075      0.07833333 0.015      0.        ]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 68.0 | 12.0 |
| Actual Positive | 8.5 | 11.5 |

### robot-2
#### accuracy
- Mean = 0.7725
- Standard deviation = 0.03699662146737187
- Max = 0.82
- 75% = 0.8
- Median = 0.785
- 25% = 0.75
- Min = 0.71

#### f1
- Mean = 0.30995228395138014
- Standard deviation = 0.14059052026737295
- Max = 0.4324324324324324
- 75% = 0.40906362545018005
- Median = 0.3798627002288329
- 25% = 0.25974025974025977
- Min = 0.0

#### precision
- Mean = 0.4438073195679687
- Standard deviation = 0.25877038791610246
- Max = 1.0
- 75% = 0.5
- Median = 0.4297385620915033
- 25% = 0.3458222811671088
- Min = 0.0

#### recall
- Mean = 0.29375
- Standard deviation = 0.16476782908080084
- Max = 0.5
- 75% = 0.41250000000000003
- Median = 0.35
- 25% = 0.17500000000000002
- Min = 0.0

#### facing_probas
- Mean = [0.70416667 0.6475     0.57333333 0.34416667 0.26854167]
- Standard deviation = [0.12435668 0.17511504 0.15299555 0.2388427  0.2612117 ]
- Max = [0.87833333 0.885      0.77666667 0.875      0.86666667]
- 75% = [0.78958333 0.76916667 0.68208333 0.41583333 0.35541667]
- Median = [0.71666667 0.68583333 0.59833333 0.25666667 0.14833333]
- 25% = [0.61541667 0.5625     0.44958333 0.16833333 0.10625   ]
- Min = [0.515      0.29666667 0.33333333 0.115      0.015     ]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 71.375 | 8.625 |
| Actual Positive | 14.125 | 5.875 |

### robot-3
#### accuracy
- Mean = 0.775
- Standard deviation = 0.06383572667401854
- Max = 0.88
- 75% = 0.8075
- Median = 0.77
- 25% = 0.73
- Min = 0.69

#### f1
- Mean = 0.3138338854450483
- Standard deviation = 0.21352707626681128
- Max = 0.6111111111111112
- 75% = 0.5117096018735364
- Median = 0.28526645768025083
- 25% = 0.14052287581699346
- Min = 0.0

#### precision
- Mean = 0.4095996102474761
- Standard deviation = 0.29378991274856203
- Max = 1.0
- 75% = 0.5180288461538461
- Median = 0.34959349593495936
- 25% = 0.25
- Min = 0.0

#### recall
- Mean = 0.29375
- Standard deviation = 0.24165768661476505
- Max = 0.75
- 75% = 0.4375
- Median = 0.22499999999999998
- 25% = 0.1
- Min = 0.0

#### facing_probas
- Mean = [0.44208333 0.549375   0.58583333 0.49333333 0.26604167]
- Standard deviation = [0.18817056 0.17752922 0.12866839 0.18700676 0.23719416]
- Max = [0.84666667 0.84666667 0.735      0.89166667 0.835     ]
- 75% = [0.5225     0.645      0.70291667 0.53666667 0.32541667]
- Median = [0.39583333 0.5575     0.605      0.44333333 0.17583333]
- 25% = [0.31625    0.42916667 0.50583333 0.38375    0.12083333]
- Min = [0.21333333 0.25666667 0.38       0.28       0.03666667]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 71.625 | 8.375 |
| Actual Positive | 14.125 | 5.875 |

### robot-4
#### accuracy
- Mean = 0.7775
- Standard deviation = 0.06495190528383289
- Max = 0.84
- 75% = 0.82
- Median = 0.795
- 25% = 0.7675000000000001
- Min = 0.62

#### f1
- Mean = 0.40689500094827435
- Standard deviation = 0.192558766232636
- Max = 0.64
- 75% = 0.5413279132791328
- Median = 0.4554655870445344
- 25% = 0.32445054945054946
- Min = 0.0

#### precision
- Mean = 0.43824477707749765
- Standard deviation = 0.23128111818902825
- Max = 0.8333333333333334
- 75% = 0.5388888888888889
- Median = 0.48249299719887956
- 25% = 0.35468750000000004
- Min = 0.0

#### recall
- Mean = 0.4375
- Standard deviation = 0.24968730444297724
- Max = 0.8
- 75% = 0.6000000000000001
- Median = 0.425
- 25% = 0.2875
- Min = 0.0

#### facing_probas
- Mean = [0.28479167 0.41583333 0.57020833 0.63875    0.451875  ]
- Standard deviation = [0.25285102 0.23452375 0.10567389 0.16705735 0.21146552]
- Max = [0.88166667 0.88333333 0.74166667 0.89       0.89333333]
- 75% = [0.33291667 0.5275     0.65458333 0.75625    0.57      ]
- Median = [0.19833333 0.3425     0.56083333 0.6325     0.4075    ]
- 25% = [0.11583333 0.23166667 0.50041667 0.54791667 0.30166667]
- Min = [0.05833333 0.14833333 0.39166667 0.38166667 0.20666667]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 69.0 | 11.0 |
| Actual Positive | 11.25 | 8.75 |

### robot-5
#### accuracy
- Mean = 0.84625
- Standard deviation = 0.05194648688795037
- Max = 0.91
- 75% = 0.8925000000000001
- Median = 0.85
- 25% = 0.82
- Min = 0.75

#### f1
- Mean = 0.4330559713366412
- Standard deviation = 0.24948522327982955
- Max = 0.7428571428571429
- 75% = 0.6603415559772295
- Median = 0.45806451612903226
- 25% = 0.24403927068723702
- Min = 0.0

#### precision
- Mean = 0.7041125541125541
- Standard deviation = 0.3444853305850988
- Max = 1.0
- 75% = 0.9318181818181818
- Median = 0.861904761904762
- 25% = 0.6136363636363636
- Min = 0.0

#### recall
- Mean = 0.3375
- Standard deviation = 0.220439901106855
- Max = 0.65
- 75% = 0.525
- Median = 0.325
- 25% = 0.15
- Min = 0.0

#### facing_probas
- Mean = [0.26333333 0.32020833 0.56270833 0.69583333 0.70666667]
- Standard deviation = [0.26822203 0.26246089 0.13336442 0.16855184 0.16277967]
- Max = [0.85666667 0.86333333 0.725      0.92166667 0.87666667]
- 75% = [0.35625    0.40916667 0.68416667 0.8325     0.83041667]
- Median = [0.12166667 0.235      0.57       0.7125     0.7475    ]
- 25% = [0.10333333 0.15083333 0.47041667 0.58458333 0.63291667]
- Min = [0.01833333 0.03166667 0.32833333 0.445      0.35166667]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 77.875 | 2.125 |
| Actual Positive | 13.25 | 6.75 |

### robot-6
#### accuracy
- Mean = 0.3875
- Standard deviation = 0.0960143218483576
- Max = 0.52
- 75% = 0.4525
- Median = 0.39
- 25% = 0.3175
- Min = 0.24

#### f1
- Mean = 0.5516012798546523
- Standard deviation = 0.1007408351131352
- Max = 0.6842105263157895
- 75% = 0.6221015826278985
- Median = 0.5610766045548654
- 25% = 0.48155545112781956
- Min = 0.3870967741935484

#### precision
- Mean = 1.0
- Standard deviation = 0.0
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 1.0
- Min = 1.0

#### recall
- Mean = 0.3875
- Standard deviation = 0.0960143218483576
- Max = 0.52
- 75% = 0.4525
- Median = 0.39
- 25% = 0.3175
- Min = 0.24

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
| Actual Positive | 61.25 | 38.75 |

