# ExtraTreesClassifier_SMOTETomek_2022-01-17-08-58_no6
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
- resampler = SMOTETomek
- estimator = ExtraTreesClassifier

### Arguments for hyperparameter search
- resampler = SMOTETomek
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
	- tomek = None
	- n_jobs = -1
	- n_features_in_ = 36
	- sampling_strategy_ = auto
	- smote_ = SMOTE(n_jobs=-1, random_state=42)
	- tomek_ = TomekLinks(n_jobs=-1, sampling_strategy='all')

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
	- max_features = log2
	- max_leaf_nodes = None
	- min_impurity_decrease = 0.0
	- ccp_alpha = 0.0
	- n_features_in_ = 36
	- n_outputs_ = 1
	- classes_ = [0 1]
	- n_classes_ = 2
	- base_estimator_ = ExtraTreeClassifier()
	- oob_decision_function_ = [[0.05555556 0.94444444]
 [0.         1.        ]
 [0.08333333 0.91666667]
 [0.78571429 0.21428571]
 [1.         0.        ]
 [0.94736842 0.05263158]
 [0.9047619  0.0952381 ]
 [1.         0.        ]
 [0.5        0.5       ]
 [0.375      0.625     ]
 [0.14285714 0.85714286]
 [0.83333333 0.16666667]
 [0.35714286 0.64285714]
 [0.88235294 0.11764706]
 [0.85       0.15      ]
 [0.90909091 0.09090909]
 [0.94117647 0.05882353]
 [1.         0.        ]
 [1.         0.        ]
 [0.95       0.05      ]
 [0.91666667 0.08333333]
 [0.52380952 0.47619048]
 [0.88888889 0.11111111]
 [0.42105263 0.57894737]
 [0.07142857 0.92857143]
 [0.05263158 0.94736842]
 [0.23529412 0.76470588]
 [0.95238095 0.04761905]
 [0.92307692 0.07692308]
 [0.625      0.375     ]
 [0.95454545 0.04545455]
 [0.94117647 0.05882353]
 [0.9375     0.0625    ]
 [0.44444444 0.55555556]
 [0.56521739 0.43478261]
 [0.16666667 0.83333333]
 [0.125      0.875     ]
 [0.05263158 0.94736842]
 [0.3        0.7       ]
 [0.         1.        ]
 [1.         0.        ]
 [1.         0.        ]
 [0.9375     0.0625    ]
 [1.         0.        ]
 [1.         0.        ]
 [0.78947368 0.21052632]
 [0.9375     0.0625    ]
 [0.76470588 0.23529412]
 [0.0625     0.9375    ]
 [0.58823529 0.41176471]
 [0.63636364 0.36363636]
 [0.33333333 0.66666667]
 [0.         1.        ]
 [0.04761905 0.95238095]
 [0.27777778 0.72222222]
 [0.         1.        ]
 [0.         1.        ]
 [0.07142857 0.92857143]
 [0.05882353 0.94117647]
 [0.05882353 0.94117647]
 [0.07692308 0.92307692]
 [0.23076923 0.76923077]
 [0.25       0.75      ]
 [0.05263158 0.94736842]
 [0.         1.        ]
 [0.2        0.8       ]
 [0.10526316 0.89473684]
 [0.10526316 0.89473684]
 [0.         1.        ]
 [0.05555556 0.94444444]
 [0.46666667 0.53333333]
 [0.         1.        ]
 [0.         1.        ]
 [0.11764706 0.88235294]
 [0.05882353 0.94117647]
 [0.05       0.95      ]
 [0.         1.        ]
 [0.06666667 0.93333333]
 [0.14285714 0.85714286]
 [0.3        0.7       ]]
	- oob_score_ = 0.875

#### Importance of features
- gp_auc_max = 0.15377883702922182
- gp_max_val_mean = 0.09978189760661124
- gp_max_val_max = 0.07074989179068109
- srmr = 0.060373802567915295
- hlbr = 0.05510874739528215
- coe1[0] = 0.047054983136854495
- gp_auc_mean = 0.04494250187818548
- low_power = 0.04432973894571943
- gp_max_val_min = 0.0432109667813733
- gp_auc_min = 0.0359737702380133
- diff_auc = 0.03348856890238246
- high_power = 0.028608658068278593
- gp_auc_std = 0.025549958051236107
- diff_std = 0.021915332141472944
- coe1[1] = 0.01976856655315186
- tdoa_mean = 0.019536528258332773
- gp_auc_range = 0.019245257790377786
- gp_max_val_std = 0.01828397992030788
- tdoa_std = 0.016115894007557943
- gp_max_ix_std = 0.015981695312400592
- gp_max_ix_range = 0.015897175048586187
- gp_max_ix_mean = 0.015048542425863872
- ac_std = 0.01246862078413215
- ratio_max_to_9th_ave_peaks = 0.012191601465007095
- tdoa_max = 0.012190026161864327
- coe3[2] = 0.012117267073407424
- gp_max_ix_max = 0.011657011027381401
- tdoa_min = 0.011075646039414156
- ratio_max_to_10ms_ave_peaks = 0.010627950022686865
- coe3[3] = 0.009590477740071676
- ac_auc = 0.002207471911345462
- gp_max_val_range = 0.0007407407407407407
- tdoa_range = 0.00038789318414212163
- coe3[0] = 0.0
- coe3[1] = 0.0
- gp_max_ix_min = 0.0

## Evaluation
cv = 8
### robot-1
#### accuracy
- Mean = 0.955
- Standard deviation = 0.023452078799117117
- Max = 0.99
- 75% = 0.97
- Median = 0.965
- 25% = 0.93
- Min = 0.92

#### f1
- Mean = 0.8826494305152841
- Standard deviation = 0.06679159770759087
- Max = 0.9743589743589743
- 75% = 0.9268292682926829
- Median = 0.9115384615384616
- 25% = 0.8303030303030303
- Min = 0.7777777777777777

#### precision
- Mean = 0.911486528822055
- Standard deviation = 0.0719883636707203
- Max = 1.0
- 75% = 0.9605263157894737
- Median = 0.9047619047619048
- 25% = 0.89375
- Min = 0.76

#### recall
- Mean = 0.86875
- Standard deviation = 0.11439378261076953
- Max = 0.95
- 75% = 0.95
- Median = 0.925
- 25% = 0.85
- Min = 0.65

#### facing_probas
- Mean = [0.74416667 0.35083333 0.03645833 0.016875   0.0175    ]
- Standard deviation = [0.07175382 0.09501462 0.02299513 0.01949782 0.02074983]
- Max = [0.82       0.55166667 0.075      0.05166667 0.06666667]
- 75% = [0.80041667 0.36708333 0.04208333 0.02958333 0.02375   ]
- Median = [0.76833333 0.33166667 0.03       0.0075     0.01166667]
- 25% = [0.70708333 0.29458333 0.02416667 0.         0.00125   ]
- Min = [0.62       0.24166667 0.00833333 0.         0.        ]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 78.125 | 1.875 |
| Actual Positive | 2.625 | 17.375 |

### robot-2
#### accuracy
- Mean = 0.9237500000000001
- Standard deviation = 0.021176342932621755
- Max = 0.96
- 75% = 0.9325
- Median = 0.93
- 25% = 0.9075
- Min = 0.89

#### f1
- Mean = 0.7663983286374179
- Standard deviation = 0.07367993361115577
- Max = 0.888888888888889
- 75% = 0.8058823529411765
- Median = 0.787878787878788
- 25% = 0.6989247311827957
- Min = 0.6666666666666666

#### precision
- Mean = 0.9724358974358974
- Standard deviation = 0.05248195582338748
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 0.9833333333333334
- Min = 0.8461538461538461

#### recall
- Mean = 0.6375
- Standard deviation = 0.09270248108869578
- Max = 0.8
- 75% = 0.7
- Median = 0.65
- 25% = 0.55
- Min = 0.5

#### facing_probas
- Mean = [0.41958333 0.64166667 0.15354167 0.01395833 0.013125  ]
- Standard deviation = [0.1004426  0.05198825 0.04104907 0.01178327 0.01237261]
- Max = [0.64       0.71833333 0.23166667 0.04166667 0.03833333]
- 75% = [0.44333333 0.68083333 0.17041667 0.01708333 0.02      ]
- Median = [0.40166667 0.62666667 0.1525     0.01       0.00833333]
- 25% = [0.33958333 0.60833333 0.13416667 0.00791667 0.00416667]
- Min = [0.31166667 0.565      0.08333333 0.         0.        ]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 79.625 | 0.375 |
| Actual Positive | 7.25 | 12.75 |

### robot-3
#### accuracy
- Mean = 0.97125
- Standard deviation = 0.01832859787326899
- Max = 0.99
- 75% = 0.99
- Median = 0.975
- 25% = 0.9575
- Min = 0.94

#### f1
- Mean = 0.9263959617618154
- Standard deviation = 0.049249345182792705
- Max = 0.975609756097561
- 75% = 0.9743589743589743
- Median = 0.9377289377289377
- 25% = 0.8945121951219512
- Min = 0.8333333333333334

#### precision
- Mean = 0.9379353924584187
- Standard deviation = 0.04582631449224571
- Max = 1.0
- 75% = 0.9642857142857142
- Median = 0.9424342105263157
- 25% = 0.9068181818181817
- Min = 0.8571428571428571

#### recall
- Mean = 0.91875
- Standard deviation = 0.07473912964438373
- Max = 1.0
- 75% = 0.9624999999999999
- Median = 0.925
- 25% = 0.9
- Min = 0.75

#### facing_probas
- Mean = [0.05666667 0.44270833 0.826875   0.31395833 0.04145833]
- Standard deviation = [0.03106892 0.10459558 0.0396726  0.05926012 0.02630533]
- Max = [0.11833333 0.64333333 0.88833333 0.40833333 0.1       ]
- 75% = [0.06875    0.49041667 0.8525     0.36625    0.04625   ]
- Median = [0.04833333 0.44833333 0.83416667 0.305      0.03333333]
- 25% = [0.03791667 0.35541667 0.79166667 0.26541667 0.02291667]
- Min = [0.015      0.295      0.77166667 0.23       0.015     ]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 78.75 | 1.25 |
| Actual Positive | 1.625 | 18.375 |

### robot-4
#### accuracy
- Mean = 0.9037499999999999
- Standard deviation = 0.0497336656601944
- Max = 0.98
- 75% = 0.9424999999999999
- Median = 0.905
- 25% = 0.8725
- Min = 0.82

#### f1
- Mean = 0.7881091088671863
- Standard deviation = 0.08944062440742116
- Max = 0.9500000000000001
- 75% = 0.842948717948718
- Median = 0.7815482502651113
- 25% = 0.7245605920444034
- Min = 0.6666666666666667

#### precision
- Mean = 0.7515374759327933
- Standard deviation = 0.1509296367991545
- Max = 0.95
- 75% = 0.9054276315789473
- Median = 0.7271062271062271
- 25% = 0.6385327635327636
- Min = 0.5294117647058824

#### recall
- Mean = 0.8500000000000001
- Standard deviation = 0.06123724356957944
- Max = 0.95
- 75% = 0.9
- Median = 0.85
- 25% = 0.8
- Min = 0.75

#### facing_probas
- Mean = [0.00645833 0.044375   0.408125   0.755      0.18625   ]
- Standard deviation = [0.00756626 0.02330262 0.0870043  0.05621141 0.08573113]
- Max = [0.02       0.09333333 0.56833333 0.855      0.36666667]
- 75% = [0.01166667 0.05708333 0.45666667 0.79458333 0.22541667]
- Median = [0.0025     0.0375     0.41083333 0.74083333 0.17416667]
- 25% = [0.         0.02791667 0.34125    0.71625    0.11291667]
- Min = [0.         0.01666667 0.29333333 0.67       0.09166667]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 73.375 | 6.625 |
| Actual Positive | 3.0 | 17.0 |

### robot-5
#### accuracy
- Mean = 0.91375
- Standard deviation = 0.03805834336909581
- Max = 0.96
- 75% = 0.95
- Median = 0.92
- 25% = 0.885
- Min = 0.85

#### f1
- Mean = 0.7049923730123953
- Standard deviation = 0.16654930571123638
- Max = 0.888888888888889
- 75% = 0.8571428571428571
- Median = 0.7487781036168133
- 25% = 0.59514687100894
- Min = 0.4

#### precision
- Mean = 1.0
- Standard deviation = 0.0
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 1.0
- Min = 1.0

#### recall
- Mean = 0.5687500000000001
- Standard deviation = 0.19029171684547913
- Max = 0.8
- 75% = 0.75
- Median = 0.6000000000000001
- 25% = 0.425
- Min = 0.25

#### facing_probas
- Mean = [0.01229167 0.00520833 0.07458333 0.60916667 0.70416667]
- Standard deviation = [0.01630732 0.00742731 0.03306927 0.09425512 0.06277163]
- Max = [0.05       0.02333333 0.145      0.79333333 0.78833333]
- 75% = [0.02       0.00666667 0.08916667 0.66208333 0.74583333]
- Median = [0.00416667 0.0025     0.06583333 0.5875     0.70583333]
- 25% = [0.         0.         0.04791667 0.57041667 0.67333333]
- Min = [0.         0.         0.03833333 0.445      0.58333333]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 80.0 | 0.0 |
| Actual Positive | 8.625 | 11.375 |

### robot-6
#### accuracy
- Mean = 0.76875
- Standard deviation = 0.04985917668794783
- Max = 0.82
- 75% = 0.81
- Median = 0.785
- 25% = 0.7475
- Min = 0.67

#### f1
- Mean = 0.8683351422859833
- Standard deviation = 0.03274502597218792
- Max = 0.9010989010989011
- 75% = 0.8950276243093923
- Median = 0.8795430293139164
- 25% = 0.8553296119085593
- Min = 0.8023952095808384

#### precision
- Mean = 1.0
- Standard deviation = 0.0
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 1.0
- Min = 1.0

#### recall
- Mean = 0.76875
- Standard deviation = 0.04985917668794783
- Max = 0.82
- 75% = 0.81
- Median = 0.785
- 25% = 0.7475
- Min = 0.67

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
| Actual Positive | 23.125 | 76.875 |

