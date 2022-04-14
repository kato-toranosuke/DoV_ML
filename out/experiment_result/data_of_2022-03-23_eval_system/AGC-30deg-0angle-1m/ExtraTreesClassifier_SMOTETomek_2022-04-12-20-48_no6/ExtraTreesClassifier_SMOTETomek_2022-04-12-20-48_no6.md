# ExtraTreesClassifier_SMOTETomek_2022-04-12-20-48_no6
## Constants
- CSV_PATH = ../out/csv/experiment
- OUTPUT_PATH = ../out/experiment_result/data_of_2022-03-23_eval_system/AGC-30deg-0angle-1m
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
- AGC_STATUS = ['AGC-30deg']
- ANGLES = [30, 60, 90, 120, 150]

## Loaded CSV
- 2022-03-23_raspi_48000Hz_w1_N2^12_overlap80_all.csv

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
	- n_estimators = 10
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
	- max_features = log2
	- max_leaf_nodes = None
	- min_impurity_decrease = 0.0
	- ccp_alpha = 0.0
	- n_features_in_ = 36
	- n_outputs_ = 1
	- classes_ = [0 1]
	- n_classes_ = 2
	- base_estimator_ = ExtraTreeClassifier()
	- oob_decision_function_ = [[0.5        0.5       ]
 [0.1        0.9       ]
 [0.625      0.375     ]
 [0.44444444 0.55555556]
 [0.44444444 0.55555556]
 [0.75       0.25      ]
 [0.9        0.1       ]
 [0.8        0.2       ]
 [0.75       0.25      ]
 [0.88888889 0.11111111]
 [0.8        0.2       ]
 [0.77777778 0.22222222]
 [1.         0.        ]
 [0.66666667 0.33333333]
 [0.8        0.2       ]
 [0.22222222 0.77777778]
 [0.55555556 0.44444444]
 [0.44444444 0.55555556]
 [0.77777778 0.22222222]
 [0.8        0.2       ]
 [0.9        0.1       ]
 [0.66666667 0.33333333]
 [0.8        0.2       ]
 [0.66666667 0.33333333]
 [0.8        0.2       ]
 [0.11111111 0.88888889]
 [0.33333333 0.66666667]
 [0.6        0.4       ]
 [0.6        0.4       ]
 [0.88888889 0.11111111]
 [0.9        0.1       ]
 [0.88888889 0.11111111]
 [1.         0.        ]
 [0.9        0.1       ]
 [0.9        0.1       ]
 [0.625      0.375     ]
 [0.8        0.2       ]
 [0.8        0.2       ]
 [0.66666667 0.33333333]
 [0.6        0.4       ]
 [0.875      0.125     ]
 [0.25       0.75      ]
 [0.33333333 0.66666667]
 [0.2        0.8       ]
 [0.4        0.6       ]
 [0.33333333 0.66666667]
 [0.83333333 0.16666667]
 [0.66666667 0.33333333]
 [0.66666667 0.33333333]
 [0.77777778 0.22222222]
 [0.88888889 0.11111111]
 [0.8        0.2       ]
 [1.         0.        ]
 [0.9        0.1       ]
 [0.875      0.125     ]
 [0.55555556 0.44444444]
 [0.125      0.875     ]
 [0.1        0.9       ]
 [0.4        0.6       ]
 [0.2        0.8       ]
 [0.125      0.875     ]
 [0.6        0.4       ]
 [0.4        0.6       ]
 [0.55555556 0.44444444]
 [0.3        0.7       ]
 [0.11111111 0.88888889]
 [0.77777778 0.22222222]
 [0.11111111 0.88888889]
 [0.3        0.7       ]
 [0.33333333 0.66666667]
 [0.11111111 0.88888889]
 [0.85714286 0.14285714]
 [0.2        0.8       ]
 [0.4        0.6       ]
 [0.57142857 0.42857143]
 [0.3        0.7       ]
 [0.25       0.75      ]
 [0.25       0.75      ]
 [0.3        0.7       ]
 [0.22222222 0.77777778]
 [0.22222222 0.77777778]
 [0.5        0.5       ]
 [0.22222222 0.77777778]
 [0.22222222 0.77777778]
 [0.22222222 0.77777778]
 [0.33333333 0.66666667]
 [0.22222222 0.77777778]
 [0.44444444 0.55555556]
 [0.625      0.375     ]
 [0.42857143 0.57142857]
 [0.11111111 0.88888889]
 [0.33333333 0.66666667]
 [0.375      0.625     ]
 [0.5        0.5       ]
 [0.55555556 0.44444444]
 [0.2        0.8       ]
 [0.2        0.8       ]
 [0.2        0.8       ]]
	- oob_score_ = 0.7755102040816326

#### Importance of features
- coe1[0] = 0.13571428571428573
- gp_max_val_range = 0.1
- gp_max_ix_max = 0.1
- tdoa_mean = 0.08114285714285714
- srmr = 0.07738095238095237
- gp_auc_max = 0.06428571428571431
- tdoa_std = 0.0630952380952381
- ratio_max_to_10ms_ave_peaks = 0.05714285714285714
- gp_max_val_max = 0.05714285714285714
- low_power = 0.042857142857142864
- gp_max_val_std = 0.04000000000000001
- gp_max_ix_std = 0.03749999999999999
- diff_std = 0.03599999999999999
- ac_auc = 0.03333333333333333
- gp_max_ix_range = 0.025000000000000005
- gp_auc_mean = 0.01666666666666666
- ratio_max_to_9th_ave_peaks = 0.016071428571428577
- tdoa_range = 0.008333333333333338
- hlbr = 0.008333333333333331
- high_power = 0.0
- coe1[1] = 0.0
- coe3[0] = 0.0
- coe3[1] = 0.0
- coe3[2] = 0.0
- coe3[3] = 0.0
- ac_std = 0.0
- diff_auc = 0.0
- gp_max_val_min = 0.0
- gp_max_val_mean = 0.0
- gp_max_ix_min = 0.0
- gp_max_ix_mean = 0.0
- gp_auc_std = 0.0
- gp_auc_range = 0.0
- gp_auc_min = 0.0
- tdoa_min = 0.0
- tdoa_max = 0.0

## Evaluation
cv = 8
### robot-1
#### accuracy
- Mean = 0.95625
- Standard deviation = 0.04240798863421842
- Max = 1.0
- 75% = 0.99
- Median = 0.975
- 25% = 0.9275
- Min = 0.87

#### f1
- Mean = 0.8934140787788458
- Standard deviation = 0.09601464812994198
- Max = 1.0
- 75% = 0.9743589743589743
- Median = 0.9331436699857752
- 25% = 0.815406976744186
- Min = 0.7450980392156863

#### precision
- Mean = 0.9244389901823282
- Standard deviation = 0.13758050468715116
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 0.9456521739130435
- Min = 0.6129032258064516

#### recall
- Mean = 0.8875
- Standard deviation = 0.11659223816361018
- Max = 1.0
- 75% = 0.95
- Median = 0.925
- 25% = 0.8875
- Min = 0.6

#### facing_probas
- Mean = [0.716875 0.18     0.14     0.126875 0.196875]
- Standard deviation = [0.04716576 0.06103278 0.07980445 0.07627817 0.10046571]
- Max = [0.78  0.285 0.315 0.25  0.355]
- 75% = [0.75    0.2275  0.165   0.18    0.24125]
- Median = [0.7375 0.16   0.12   0.12   0.2025]
- 25% = [0.67375 0.14    0.08875 0.08125 0.17125]
- Min = [0.635 0.105 0.05  0.02  0.005]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 77.875 | 2.125 |
| Actual Positive | 2.25 | 17.75 |

### robot-2
#### accuracy
- Mean = 0.8275
- Standard deviation = 0.04054318685056713
- Max = 0.89
- 75% = 0.8625
- Median = 0.82
- 25% = 0.805
- Min = 0.76

#### f1
- Mean = 0.5857781568150232
- Standard deviation = 0.12749563280209966
- Max = 0.7555555555555556
- 75% = 0.6504545454545454
- Median = 0.6204081632653062
- 25% = 0.5568181818181818
- Min = 0.3225806451612903

#### precision
- Mean = 0.562723354231975
- Standard deviation = 0.10195019534387562
- Max = 0.7333333333333333
- 75% = 0.63875
- Median = 0.5375
- 25% = 0.5015673981191223
- Min = 0.4166666666666667

#### recall
- Mean = 0.6375
- Standard deviation = 0.18498310733685927
- Max = 0.85
- 75% = 0.7625
- Median = 0.7
- 25% = 0.5375000000000001
- Min = 0.25

#### facing_probas
- Mean = [0.4275   0.70375  0.66     0.29375  0.115625]
- Standard deviation = [0.12867109 0.05200661 0.06093029 0.09102713 0.08221304]
- Max = [0.71  0.775 0.77  0.485 0.295]
- 75% = [0.49    0.7225  0.68625 0.33    0.1425 ]
- Median = [0.3875 0.715  0.6725 0.2625 0.0975]
- 25% = [0.3275  0.69875 0.61375 0.22    0.07125]
- Min = [0.295 0.59  0.575 0.21  0.   ]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 70.0 | 10.0 |
| Actual Positive | 7.25 | 12.75 |

### robot-3
#### accuracy
- Mean = 0.7925
- Standard deviation = 0.023318447632722027
- Max = 0.82
- 75% = 0.8125
- Median = 0.795
- 25% = 0.7775000000000001
- Min = 0.75

#### f1
- Mean = 0.2796360497606785
- Standard deviation = 0.14706954648930912
- Max = 0.4375
- 75% = 0.4181985294117647
- Median = 0.3147605083088954
- 25% = 0.13712374581939799
- Min = 0.08000000000000002

#### precision
- Mean = 0.4233100233100233
- Standard deviation = 0.1375872398107654
- Max = 0.5833333333333334
- 75% = 0.5549242424242424
- Median = 0.41666666666666663
- 25% = 0.3269230769230769
- Min = 0.2

#### recall
- Mean = 0.21875
- Standard deviation = 0.12732217992164602
- Max = 0.35
- 75% = 0.35
- Median = 0.25
- 25% = 0.08750000000000001
- Min = 0.05

#### facing_probas
- Mean = [0.234375 0.58     0.563125 0.466875 0.293125]
- Standard deviation = [0.07522622 0.0582559  0.07881694 0.0881383  0.12121617]
- Max = [0.4   0.65  0.67  0.615 0.515]
- 75% = [0.2475  0.6125  0.61375 0.5225  0.32   ]
- Median = [0.215  0.6075 0.5825 0.4575 0.2525]
- 25% = [0.205   0.555   0.53125 0.395   0.23   ]
- Min = [0.125 0.465 0.42  0.345 0.155]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 74.875 | 5.125 |
| Actual Positive | 15.625 | 4.375 |

### robot-4
#### accuracy
- Mean = 0.73
- Standard deviation = 0.051478150704935006
- Max = 0.81
- 75% = 0.765
- Median = 0.73
- 25% = 0.705
- Min = 0.65

#### f1
- Mean = 0.28567444306805645
- Standard deviation = 0.13108981142229564
- Max = 0.5217391304347826
- 75% = 0.3392857142857143
- Median = 0.26556991774383076
- 25% = 0.18658536585365854
- Min = 0.12903225806451613

#### precision
- Mean = 0.3055542496718967
- Standard deviation = 0.1243888272060159
- Max = 0.5333333333333333
- 75% = 0.3403846153846154
- Median = 0.29705882352941176
- 25% = 0.21853146853146854
- Min = 0.14285714285714285

#### recall
- Mean = 0.28125
- Standard deviation = 0.15194057226429022
- Max = 0.6
- 75% = 0.325
- Median = 0.275
- 25% = 0.15
- Min = 0.1

#### facing_probas
- Mean = [0.1375   0.39375  0.39375  0.5975   0.670625]
- Standard deviation = [0.08951257 0.12383835 0.11154455 0.05477226 0.06663508]
- Max = [0.325 0.64  0.54  0.665 0.75 ]
- 75% = [0.165   0.4575  0.495   0.63375 0.735  ]
- Median = [0.12  0.38  0.385 0.61  0.685]
- 25% = [0.08125 0.335   0.3325  0.5775  0.61375]
- Min = [0.02 0.21 0.2  0.48 0.56]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 67.375 | 12.625 |
| Actual Positive | 14.375 | 5.625 |

### robot-5
#### accuracy
- Mean = 0.77875
- Standard deviation = 0.06050568155140474
- Max = 0.86
- 75% = 0.8175
- Median = 0.8
- 25% = 0.725
- Min = 0.68

#### f1
- Mean = 0.3764918414918415
- Standard deviation = 0.20931211987191478
- Max = 0.68
- 75% = 0.517948717948718
- Median = 0.4428904428904429
- 25% = 0.2142857142857143
- Min = 0.0

#### precision
- Mean = 0.421474358974359
- Standard deviation = 0.23516563577430408
- Max = 0.8
- 75% = 0.5455128205128205
- Median = 0.5
- 25% = 0.25
- Min = 0.0

#### recall
- Mean = 0.36250000000000004
- Standard deviation = 0.24206145913796356
- Max = 0.85
- 75% = 0.4625
- Median = 0.375
- 25% = 0.1875
- Min = 0.0

#### facing_probas
- Mean = [0.134375 0.24     0.153125 0.66     0.661875]
- Standard deviation = [0.07468423 0.14230249 0.07520545 0.10301699 0.07365195]
- Max = [0.265 0.52  0.28  0.85  0.82 ]
- 75% = [0.18125 0.295   0.21875 0.71375 0.7    ]
- Median = [0.1175 0.2475 0.13   0.655  0.635 ]
- 25% = [0.1     0.15875 0.09875 0.58875 0.6125 ]
- Min = [0.    0.03  0.045 0.5   0.585]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 70.625 | 9.375 |
| Actual Positive | 12.75 | 7.25 |

### robot-6
#### accuracy
- Mean = 0.47750000000000004
- Standard deviation = 0.04465142774872939
- Max = 0.55
- 75% = 0.515
- Median = 0.46499999999999997
- 25% = 0.44
- Min = 0.42

#### f1
- Mean = 0.6451367984288542
- Standard deviation = 0.040554136042274085
- Max = 0.7096774193548387
- 75% = 0.6798251309353763
- Median = 0.6346691519105312
- 25% = 0.6111111111111112
- Min = 0.5915492957746479

#### precision
- Mean = 1.0
- Standard deviation = 0.0
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 1.0
- Min = 1.0

#### recall
- Mean = 0.47750000000000004
- Standard deviation = 0.04465142774872939
- Max = 0.55
- 75% = 0.515
- Median = 0.46499999999999997
- 25% = 0.44
- Min = 0.42

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
| Actual Positive | 52.25 | 47.75 |

