# ExtraTreesClassifier_NoResampler_2022-04-12-21-29_no0
## Constants
- CSV_PATH = ../out/csv/experiment
- OUTPUT_PATH = ../out/experiment_result/data_of_2022-03-23_eval_system/AGC-30deg-0angle-3m
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
- AGC_STATUS = ['AGC-30deg']
- ANGLES = [30, 60, 90, 120, 150]

## Loaded CSV
- 2022-03-23_raspi_48000Hz_w1_N2^12_overlap80_all.csv

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
	- min_samples_split = 5
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
- gp_max_val_max = 0.10214136544406074
- gp_auc_max = 0.08664017786555278
- gp_auc_range = 0.06484547029194469
- gp_max_val_min = 0.063056057099382
- gp_max_val_range = 0.0624150531792488
- gp_max_val_std = 0.054582232592041
- ratio_max_to_9th_ave_peaks = 0.051054891592302976
- gp_max_val_mean = 0.048542278119163326
- tdoa_std = 0.04778202598452836
- ac_std = 0.038686389963387205
- high_power = 0.03756086352259463
- diff_auc = 0.03714393087043858
- gp_max_ix_std = 0.03493248403497824
- gp_max_ix_mean = 0.034187560098772725
- gp_auc_mean = 0.029983388704318926
- hlbr = 0.02839930173271384
- ac_auc = 0.025902584247605286
- gp_auc_std = 0.022333670826924203
- diff_std = 0.021924609810479383
- gp_auc_min = 0.01576615375565928
- coe1[1] = 0.015614530397139096
- ratio_max_to_10ms_ave_peaks = 0.014967066593995066
- low_power = 0.010547617520094582
- tdoa_min = 0.00802675585284281
- srmr = 0.007656859269762504
- coe3[3] = 0.007272727272727275
- coe1[0] = 0.0071428571428571435
- gp_max_ix_max = 0.0061879297173414805
- tdoa_range = 0.005761904761904762
- tdoa_mean = 0.004942791762013731
- coe3[2] = 0.003998469973224538
- coe3[0] = 0.0
- coe3[1] = 0.0
- gp_max_ix_range = 0.0
- gp_max_ix_min = 0.0
- tdoa_max = 0.0

## Evaluation
cv = 8
### robot-1
#### accuracy
- Mean = 0.84375
- Standard deviation = 0.02781074432660872
- Max = 0.88
- 75% = 0.8625
- Median = 0.855
- 25% = 0.8175
- Min = 0.8

#### f1
- Mean = 0.42682156480149114
- Standard deviation = 0.18474195523322498
- Max = 0.6
- 75% = 0.5670362903225807
- Median = 0.5247311827956989
- 25% = 0.3113354037267081
- Min = 0.09090909090909091

#### precision
- Mean = 0.7233901515151515
- Standard deviation = 0.11703101160031797
- Max = 0.9
- 75% = 0.8045454545454546
- Median = 0.7386363636363636
- 25% = 0.65625
- Min = 0.5

#### recall
- Mean = 0.31875
- Standard deviation = 0.1539835624344365
- Max = 0.45
- 75% = 0.45
- Median = 0.4
- 25% = 0.2125
- Min = 0.05

#### facing_probas
- Mean = [0.36927083 0.10302083 0.03119792 0.00822917 0.00854167]
- Standard deviation = [0.10337444 0.03981715 0.02520096 0.00860432 0.0093053 ]
- Max = [0.49791667 0.16833333 0.07875    0.0225     0.0275    ]
- 75% = [0.46145833 0.13541667 0.0496875  0.015      0.013125  ]
- Median = [0.383125   0.09770833 0.028125   0.00666667 0.00666667]
- 25% = [0.27729167 0.0815625  0.00875    0.         0.        ]
- Min = [0.20416667 0.0425     0.         0.         0.        ]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 78.0 | 2.0 |
| Actual Positive | 13.625 | 6.375 |

### robot-2
#### accuracy
- Mean = 0.81
- Standard deviation = 0.01936491673103706
- Max = 0.83
- 75% = 0.8225
- Median = 0.815
- 25% = 0.805
- Min = 0.77

#### f1
- Mean = 0.323612517265066
- Standard deviation = 0.11325454525954488
- Max = 0.48888888888888893
- 75% = 0.41640543364681293
- Median = 0.339031339031339
- 25% = 0.2309782608695652
- Min = 0.16000000000000003

#### precision
- Mean = 0.6053434065934066
- Standard deviation = 0.1214769135059571
- Max = 0.75
- 75% = 0.6785714285714286
- Median = 0.6666666666666666
- 25% = 0.5138461538461538
- Min = 0.4

#### recall
- Mean = 0.25
- Standard deviation = 0.14142135623730953
- Max = 0.55
- 75% = 0.3125
- Median = 0.225
- 25% = 0.1375
- Min = 0.1

#### facing_probas
- Mean = [0.20723958 0.36958333 0.21171875 0.03208333 0.015625  ]
- Standard deviation = [0.07051489 0.0966267  0.05465939 0.0157495  0.01455801]
- Max = [0.32416667 0.56708333 0.29875    0.0575     0.05083333]
- 75% = [0.2596875  0.41510417 0.25989583 0.04760417 0.01708333]
- Median = [0.20166667 0.33270833 0.19791667 0.02729167 0.01375   ]
- 25% = [0.155625   0.29385417 0.17947917 0.01895833 0.00625   ]
- Min = [0.1025     0.2725     0.1175     0.01166667 0.        ]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 76.0 | 4.0 |
| Actual Positive | 15.0 | 5.0 |

### robot-3
#### accuracy
- Mean = 0.7849999999999999
- Standard deviation = 0.02499999999999999
- Max = 0.84
- 75% = 0.7925
- Median = 0.78
- 25% = 0.77
- Min = 0.75

#### f1
- Mean = 0.3943754114549045
- Standard deviation = 0.10861850792665195
- Max = 0.5555555555555556
- 75% = 0.4599489795918367
- Median = 0.4222222222222223
- 25% = 0.32165898617511524
- Min = 0.21428571428571425

#### precision
- Mean = 0.44926201671891325
- Standard deviation = 0.07928826983470674
- Max = 0.625
- 75% = 0.475
- Median = 0.43189655172413793
- 25% = 0.39375000000000004
- Min = 0.36363636363636365

#### recall
- Mean = 0.36875
- Standard deviation = 0.14128318194321643
- Max = 0.6
- 75% = 0.4625
- Median = 0.375
- 25% = 0.275
- Min = 0.15

#### facing_probas
- Mean = [0.14369792 0.35989583 0.46770833 0.21380208 0.05651042]
- Standard deviation = [0.042705   0.11166837 0.05390361 0.07864864 0.0169647 ]
- Max = [0.245      0.61583333 0.56708333 0.38125    0.08666667]
- 75% = [0.1478125  0.38697917 0.506875   0.234375   0.06354167]
- Median = [0.13791667 0.34770833 0.46083333 0.20395833 0.05416667]
- 25% = [0.11645833 0.28208333 0.42822917 0.1653125  0.0478125 ]
- Min = [0.10083333 0.23416667 0.39833333 0.10166667 0.0325    ]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 71.125 | 8.875 |
| Actual Positive | 12.625 | 7.375 |

### robot-4
#### accuracy
- Mean = 0.8225
- Standard deviation = 0.02331844763272202
- Max = 0.87
- 75% = 0.8325
- Median = 0.82
- 25% = 0.8075000000000001
- Min = 0.79

#### f1
- Mean = 0.36998118248118245
- Standard deviation = 0.0923530100815825
- Max = 0.5185185185185185
- 75% = 0.42953667953667946
- Median = 0.3973063973063973
- 25% = 0.2767857142857143
- Min = 0.24999999999999997

#### precision
- Mean = 0.6841669360051713
- Standard deviation = 0.1637158463048929
- Max = 1.0
- 75% = 0.75
- Median = 0.7321428571428572
- 25% = 0.5288461538461539
- Min = 0.47058823529411764

#### recall
- Mean = 0.26875
- Standard deviation = 0.08992184106211348
- Max = 0.4
- 75% = 0.35
- Median = 0.275
- 25% = 0.1875
- Min = 0.15

#### facing_probas
- Mean = [0.02213542 0.2334375  0.43604167 0.43234375 0.24484375]
- Standard deviation = [0.01475264 0.09172743 0.06420927 0.08097066 0.06781624]
- Max = [0.04833333 0.41791667 0.54625    0.55583333 0.33416667]
- 75% = [0.03260417 0.25052083 0.47364583 0.48802083 0.29854167]
- Median = [0.01729167 0.19708333 0.4425     0.43041667 0.25479167]
- 25% = [0.0090625  0.18833333 0.370625   0.3940625  0.20260417]
- Min = [0.00666667 0.11833333 0.3575     0.27791667 0.12791667]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 76.875 | 3.125 |
| Actual Positive | 14.625 | 5.375 |

### robot-5
#### accuracy
- Mean = 0.84375
- Standard deviation = 0.027357585785299104
- Max = 0.89
- 75% = 0.8625
- Median = 0.845
- 25% = 0.8175
- Min = 0.81

#### f1
- Mean = 0.3995592918269685
- Standard deviation = 0.19230162507895876
- Max = 0.6857142857142857
- 75% = 0.5072302558398221
- Median = 0.4641025641025641
- 25% = 0.2309782608695652
- Min = 0.09523809523809523

#### precision
- Mean = 0.8140782828282829
- Standard deviation = 0.11700245674318303
- Max = 1.0
- 75% = 0.8636363636363636
- Median = 0.788888888888889
- 25% = 0.7375
- Min = 0.6666666666666666

#### recall
- Mean = 0.29375
- Standard deviation = 0.17399263633843817
- Max = 0.6
- 75% = 0.375
- Median = 0.32499999999999996
- 25% = 0.1375
- Min = 0.05

#### facing_probas
- Mean = [0.01270833 0.00869792 0.17671875 0.30447917 0.42765625]
- Standard deviation = [0.01228107 0.01485964 0.05961299 0.08379035 0.11591198]
- Max = [0.0275     0.04666667 0.25833333 0.445      0.6175    ]
- 75% = [0.02541667 0.0090625  0.23947917 0.3546875  0.51322917]
- Median = [0.01125    0.00208333 0.15958333 0.31354167 0.43270833]
- 25% = [0.         0.         0.1221875  0.2596875  0.31145833]
- Min = [0.         0.         0.10875    0.17208333 0.28458333]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 78.5 | 1.5 |
| Actual Positive | 14.125 | 5.875 |

### robot-6
#### accuracy
- Mean = 0.30000000000000004
- Standard deviation = 0.0792148975887743
- Max = 0.4
- 75% = 0.3625
- Median = 0.33
- 25% = 0.225
- Min = 0.17

#### f1
- Mean = 0.4556446241244563
- Standard deviation = 0.09680726554636272
- Max = 0.5714285714285715
- 75% = 0.5320953198797768
- Median = 0.49624060150375937
- 25% = 0.367264664382181
- Min = 0.2905982905982906

#### precision
- Mean = 1.0
- Standard deviation = 0.0
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 1.0
- Min = 1.0

#### recall
- Mean = 0.30000000000000004
- Standard deviation = 0.0792148975887743
- Max = 0.4
- 75% = 0.3625
- Median = 0.33
- 25% = 0.225
- Min = 0.17

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
| Actual Positive | 70.0 | 30.0 |

