# ExtraTreesClassifier_RandomUnderSampler_2022-04-15-08-37_no2
## Constants
- CSV_PATH = ../out/csv/experiment
- OUTPUT_PATH = ../out/experiment_result/data_of_2022-03-23_eval_system/AGC-15deg-0angle-3and5m
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
- DISTANCE = [3, 5]
- AGC_STATUS = ['AGC-15deg']
- ANGLES = [60, 75, 90, 105, 120]

## Loaded CSV
- 2022-03-23_raspi_48000Hz_w1_N2^12_overlap80_all.csv

## Estimator
### Type
- resampler = RandomUnderSampler
- estimator = ExtraTreesClassifier

### Arguments for hyperparameter search
- resampler = RandomUnderSampler
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
	- replacement = False
	- n_features_in_ = 36
	- sampling_strategy_ = OrderedDict([(0, 30)])
	- sample_indices_ = [ 56  59   7  70  32  79  91  13  52 131  24  77  14  45 110 112 136   3
 109 128  80  57  40  88  54  18  21 141  94 121   0   1   2  15  16  17
  33  34  35  48  49  50  66  67  68  81  82  83  99 100 101 114 115 116
 132 133 134 147 148 149]

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
	- max_features = None
	- max_leaf_nodes = None
	- min_impurity_decrease = 0.0
	- ccp_alpha = 0.0
	- n_features_in_ = 36
	- n_outputs_ = 1
	- classes_ = [0 1]
	- n_classes_ = 2
	- base_estimator_ = ExtraTreeClassifier()
	- oob_decision_function_ = [[0.5        0.5       ]
 [0.44444444 0.55555556]
 [0.2        0.8       ]
 [0.4        0.6       ]
 [0.5        0.5       ]
 [0.33333333 0.66666667]
 [0.55555556 0.44444444]
 [0.44444444 0.55555556]
 [0.44444444 0.55555556]
 [0.4        0.6       ]
 [0.75       0.25      ]
 [0.66666667 0.33333333]
 [0.16666667 0.83333333]
 [0.66666667 0.33333333]
 [0.6        0.4       ]
 [0.6        0.4       ]
 [0.7        0.3       ]
 [0.11111111 0.88888889]
 [0.66666667 0.33333333]
 [0.3        0.7       ]
 [0.5        0.5       ]
 [0.44444444 0.55555556]
 [0.22222222 0.77777778]
 [0.44444444 0.55555556]
 [0.77777778 0.22222222]
 [0.33333333 0.66666667]
 [0.4        0.6       ]
 [0.33333333 0.66666667]
 [0.22222222 0.77777778]
 [0.55555556 0.44444444]
 [0.55555556 0.44444444]
 [0.3        0.7       ]
 [0.375      0.625     ]
 [0.8        0.2       ]
 [0.55555556 0.44444444]
 [0.8        0.2       ]
 [0.2        0.8       ]
 [0.2        0.8       ]
 [0.375      0.625     ]
 [0.25       0.75      ]
 [0.33333333 0.66666667]
 [0.44444444 0.55555556]
 [0.125      0.875     ]
 [0.1        0.9       ]
 [0.3        0.7       ]
 [0.22222222 0.77777778]
 [0.5        0.5       ]
 [0.3        0.7       ]
 [0.1        0.9       ]
 [0.3        0.7       ]
 [0.375      0.625     ]
 [0.75       0.25      ]
 [0.5        0.5       ]
 [0.4        0.6       ]
 [0.2        0.8       ]
 [0.11111111 0.88888889]
 [0.11111111 0.88888889]
 [0.5        0.5       ]
 [0.77777778 0.22222222]
 [0.7        0.3       ]]
	- oob_score_ = 0.55

#### Importance of features
- hlbr = 0.2111111111111111
- high_power = 0.1
- ac_auc = 0.1
- diff_auc = 0.1
- gp_max_val_max = 0.1
- gp_auc_max = 0.1
- tdoa_std = 0.1
- gp_max_val_range = 0.05555555555555556
- coe3[3] = 0.04444444444444444
- ac_std = 0.04444444444444444
- tdoa_min = 0.04444444444444444
- low_power = 0.0
- coe1[0] = 0.0
- coe1[1] = 0.0
- coe3[0] = 0.0
- coe3[1] = 0.0
- coe3[2] = 0.0
- ratio_max_to_10ms_ave_peaks = 0.0
- ratio_max_to_9th_ave_peaks = 0.0
- diff_std = 0.0
- srmr = 0.0
- gp_max_val_std = 0.0
- gp_max_val_min = 0.0
- gp_max_val_mean = 0.0
- gp_max_ix_std = 0.0
- gp_max_ix_range = 0.0
- gp_max_ix_min = 0.0
- gp_max_ix_max = 0.0
- gp_max_ix_mean = 0.0
- gp_auc_std = 0.0
- gp_auc_range = 0.0
- gp_auc_min = 0.0
- gp_auc_mean = 0.0
- tdoa_range = 0.0
- tdoa_max = 0.0
- tdoa_mean = 0.0

## Evaluation
cv = 8
### robot-1
#### accuracy
- Mean = 0.7581249999999999
- Standard deviation = 0.014776988021921124
- Max = 0.78
- 75% = 0.77
- Median = 0.76
- 25% = 0.7475
- Min = 0.735

#### f1
- Mean = 0.3596212187525777
- Standard deviation = 0.07801880616203237
- Max = 0.48837209302325585
- 75% = 0.4279454022988506
- Median = 0.34401408450704224
- 25% = 0.3006060606060606
- Min = 0.24242424242424246

#### precision
- Mean = 0.3786834048832907
- Standard deviation = 0.048699929899663534
- Max = 0.45652173913043476
- 75% = 0.4094414893617021
- Median = 0.38585607940446653
- 25% = 0.3410714285714286
- Min = 0.3076923076923077

#### recall
- Mean = 0.35
- Standard deviation = 0.10752906583803283
- Max = 0.525
- 75% = 0.4375
- Median = 0.32499999999999996
- 25% = 0.26875000000000004
- Min = 0.2

#### facing_probas
- Mean = [0.5259375 0.43625   0.526875  0.4046875 0.386875 ]
- Standard deviation = [0.06722092 0.09159183 0.06526089 0.09288297 0.09574339]
- Max = [0.6425 0.5825 0.595  0.5625 0.56  ]
- 75% = [0.56125  0.475625 0.570625 0.443125 0.4275  ]
- Median = [0.52125 0.4375  0.5625  0.43375 0.40875]
- 25% = [0.471875 0.39875  0.481875 0.33375  0.330625]
- Min = [0.445 0.255 0.39  0.24  0.22 ]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 137.625 | 22.375 |
| Actual Positive | 26.0 | 14.0 |

### robot-2
#### accuracy
- Mean = 0.7424999999999999
- Standard deviation = 0.028613807855648987
- Max = 0.78
- 75% = 0.76
- Median = 0.75
- 25% = 0.73
- Min = 0.68

#### f1
- Mean = 0.21228632478632478
- Standard deviation = 0.08751625667589592
- Max = 0.35714285714285715
- 75% = 0.26190476190476186
- Median = 0.1912087912087912
- 25% = 0.14047619047619048
- Min = 0.1111111111111111

#### precision
- Mean = 0.2759334415584416
- Standard deviation = 0.06126109800815707
- Max = 0.375
- 75% = 0.3352272727272727
- Median = 0.2583333333333333
- 25% = 0.22402597402597402
- Min = 0.2

#### recall
- Mean = 0.1875
- Standard deviation = 0.10458250331675945
- Max = 0.375
- 75% = 0.2625
- Median = 0.15000000000000002
- 25% = 0.1
- Min = 0.075

#### facing_probas
- Mean = [0.569375  0.606875  0.708125  0.5       0.4346875]
- Standard deviation = [0.05113936 0.06956056 0.06724198 0.08263247 0.07374404]
- Max = [0.63   0.7125 0.805  0.5875 0.55  ]
- 75% = [0.608125 0.656875 0.74625  0.565625 0.4775  ]
- Median = [0.5875  0.61875 0.72875 0.5325  0.4575 ]
- 25% = [0.516875 0.5375   0.675625 0.43875  0.375625]
- Min = [0.49   0.5175 0.585  0.345  0.32  ]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 141.0 | 19.0 |
| Actual Positive | 32.5 | 7.5 |

### robot-3
#### accuracy
- Mean = 0.566875
- Standard deviation = 0.0891255259451522
- Max = 0.69
- 75% = 0.64125
- Median = 0.575
- 25% = 0.52
- Min = 0.41

#### f1
- Mean = 0.2987952567783202
- Standard deviation = 0.02948723343778317
- Max = 0.34375
- 75% = 0.3210258078507916
- Median = 0.3047409579667644
- 25% = 0.2754761904761905
- Min = 0.2526315789473684

#### precision
- Mean = 0.22740045888569574
- Standard deviation = 0.021767247094255166
- Max = 0.25757575757575757
- 75% = 0.25
- Median = 0.22218614718614718
- 25% = 0.2152822842310188
- Min = 0.19090909090909092

#### recall
- Mean = 0.46875
- Standard deviation = 0.12854352375751957
- Max = 0.7
- 75% = 0.53125
- Median = 0.4875
- 25% = 0.39375
- Min = 0.275

#### facing_probas
- Mean = [0.5325    0.579375  0.7109375 0.5325    0.4878125]
- Standard deviation = [0.04196353 0.05564606 0.06812142 0.05752717 0.06777072]
- Max = [0.6125 0.645  0.7925 0.5975 0.58  ]
- 75% = [0.556875 0.618125 0.75     0.574375 0.53625 ]
- Median = [0.5325  0.6025  0.7325  0.55875 0.51375]
- 25% = [0.49875  0.5175   0.673125 0.470625 0.413125]
- Min = [0.48   0.4975 0.5775 0.45   0.3975]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 94.625 | 65.375 |
| Actual Positive | 21.25 | 18.75 |

### robot-4
#### accuracy
- Mean = 0.78125
- Standard deviation = 0.015360257159305647
- Max = 0.795
- 75% = 0.79125
- Median = 0.785
- 25% = 0.77875
- Min = 0.745

#### f1
- Mean = 0.1557382678393317
- Standard deviation = 0.08024523911237053
- Max = 0.3076923076923077
- 75% = 0.19807692307692307
- Median = 0.15642237982663515
- 25% = 0.08750000000000002
- Min = 0.045454545454545456

#### precision
- Mean = 0.3477976190476191
- Standard deviation = 0.07117770927886019
- Max = 0.42857142857142855
- 75% = 0.4041666666666667
- Median = 0.37857142857142856
- 25% = 0.2725
- Min = 0.25

#### recall
- Mean = 0.109375
- Standard deviation = 0.07064159097160821
- Max = 0.25
- 75% = 0.1375
- Median = 0.1
- 25% = 0.05
- Min = 0.025

#### facing_probas
- Mean = [0.5046875 0.57375   0.7053125 0.6096875 0.5159375]
- Standard deviation = [0.04729293 0.07005578 0.0689592  0.07952434 0.08478776]
- Max = [0.575  0.6625 0.81   0.7075 0.6325]
- 75% = [0.54375  0.633125 0.746875 0.659375 0.575625]
- Median = [0.5125  0.59625 0.71125 0.63375 0.52   ]
- 25% = [0.456875 0.491875 0.66875  0.5525   0.459375]
- Min = [0.44   0.48   0.5925 0.465  0.375 ]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 151.875 | 8.125 |
| Actual Positive | 35.625 | 4.375 |

### robot-5
#### accuracy
- Mean = 0.79
- Standard deviation = 0.009354143466934863
- Max = 0.81
- 75% = 0.79125
- Median = 0.79
- 25% = 0.785
- Min = 0.775

#### f1
- Mean = 0.0690760751571674
- Standard deviation = 0.06038122282778148
- Max = 0.1739130434782609
- 75% = 0.09646739130434784
- Median = 0.08336951801997394
- 25% = 0.0
- Min = 0.0

#### precision
- Mean = 0.2353670634920635
- Standard deviation = 0.21909321305415486
- Max = 0.6666666666666666
- 75% = 0.34375
- Median = 0.25396825396825395
- 25% = 0.0
- Min = 0.0

#### recall
- Mean = 0.040625
- Standard deviation = 0.03521696146745201
- Max = 0.1
- 75% = 0.05625
- Median = 0.05
- 25% = 0.0
- Min = 0.0

#### facing_probas
- Mean = [0.3721875 0.426875  0.6134375 0.5153125 0.4675   ]
- Standard deviation = [0.0669239  0.07893579 0.07022216 0.08689467 0.08154753]
- Max = [0.48   0.5525 0.7025 0.615  0.565 ]
- 75% = [0.41625  0.481875 0.655    0.583125 0.543125]
- Median = [0.36125 0.4425  0.61625 0.5475  0.4825 ]
- 25% = [0.340625 0.35875  0.59625  0.45     0.41125 ]
- Min = [0.2675 0.295  0.4575 0.345  0.3175]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 156.375 | 3.625 |
| Actual Positive | 38.375 | 1.625 |

### robot-6
#### accuracy
- Mean = 0.23125
- Standard deviation = 0.04284784125250653
- Max = 0.285
- 75% = 0.2625
- Median = 0.24
- 25% = 0.21125
- Min = 0.15

#### f1
- Mean = 0.3736197575298451
- Standard deviation = 0.05792512876431702
- Max = 0.44357976653696496
- 75% = 0.41582302212223476
- Median = 0.38686072038377106
- 25% = 0.34855087500864634
- Min = 0.2608695652173913

#### precision
- Mean = 1.0
- Standard deviation = 0.0
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 1.0
- Min = 1.0

#### recall
- Mean = 0.23125
- Standard deviation = 0.04284784125250653
- Max = 0.285
- 75% = 0.2625
- Median = 0.24
- 25% = 0.21125
- Min = 0.15

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
| Actual Positive | 153.75 | 46.25 |

