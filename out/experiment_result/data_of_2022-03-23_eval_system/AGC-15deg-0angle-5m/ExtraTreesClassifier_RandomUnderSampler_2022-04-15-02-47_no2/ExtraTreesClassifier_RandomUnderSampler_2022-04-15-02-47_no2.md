# ExtraTreesClassifier_RandomUnderSampler_2022-04-15-02-47_no2
## Constants
- CSV_PATH = ../out/csv/experiment
- OUTPUT_PATH = ../out/experiment_result/data_of_2022-03-23_eval_system/AGC-15deg-0angle-5m
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
	- sampling_strategy_ = OrderedDict([(0, 15)])
	- sample_indices_ = [ 3  8 45 57 16 66 42 60 15 69 58 62 40  6 64  0  1  2 18 19 20 36 37 38
 54 55 56 72 73 74]

- best_estimator
	- base_estimator = ExtraTreeClassifier()
	- n_estimators = 50
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
	- oob_decision_function_ = [[0.40425532 0.59574468]
 [0.56818182 0.43181818]
 [0.5625     0.4375    ]
 [0.42857143 0.57142857]
 [0.6        0.4       ]
 [0.58333333 0.41666667]
 [0.41304348 0.58695652]
 [0.55319149 0.44680851]
 [0.51162791 0.48837209]
 [0.53333333 0.46666667]
 [0.34       0.66      ]
 [0.47727273 0.52272727]
 [0.47619048 0.52380952]
 [0.43181818 0.56818182]
 [0.55555556 0.44444444]
 [0.47727273 0.52272727]
 [0.55555556 0.44444444]
 [0.53191489 0.46808511]
 [0.48888889 0.51111111]
 [0.41860465 0.58139535]
 [0.44186047 0.55813953]
 [0.40425532 0.59574468]
 [0.38297872 0.61702128]
 [0.39534884 0.60465116]
 [0.45       0.55      ]
 [0.58139535 0.41860465]
 [0.39130435 0.60869565]
 [0.60869565 0.39130435]
 [0.48888889 0.51111111]
 [0.55555556 0.44444444]]
	- oob_score_ = 0.6

#### Importance of features
- gp_max_val_std = 0.09999999999999998
- gp_auc_min = 0.08749999999999998
- ratio_max_to_10ms_ave_peaks = 0.08124999999999999
- tdoa_range = 0.08124999999999999
- low_power = 0.07499999999999998
- gp_max_val_max = 0.05624999999999999
- diff_auc = 0.04999999999999999
- srmr = 0.04999999999999999
- gp_max_val_range = 0.04999999999999999
- hlbr = 0.031249999999999993
- coe3[3] = 0.024999999999999994
- ratio_max_to_9th_ave_peaks = 0.024999999999999994
- ac_std = 0.024999999999999994
- ac_auc = 0.024999999999999994
- gp_max_val_min = 0.024999999999999994
- gp_max_ix_mean = 0.024999999999999994
- gp_auc_std = 0.024999999999999994
- gp_auc_range = 0.024999999999999994
- gp_auc_mean = 0.024999999999999994
- tdoa_std = 0.024999999999999994
- tdoa_min = 0.024999999999999994
- tdoa_mean = 0.024999999999999994
- diff_std = 0.018749999999999996
- tdoa_max = 0.018749999999999996
- high_power = 0.0
- coe1[0] = 0.0
- coe1[1] = 0.0
- coe3[0] = 0.0
- coe3[1] = 0.0
- coe3[2] = 0.0
- gp_max_val_mean = 0.0
- gp_max_ix_std = 0.0
- gp_max_ix_range = 0.0
- gp_max_ix_min = 0.0
- gp_max_ix_max = 0.0
- gp_auc_max = 0.0

## Evaluation
cv = 8
### robot-1
#### accuracy
- Mean = 0.78625
- Standard deviation = 0.06283659363778402
- Max = 0.85
- 75% = 0.825
- Median = 0.805
- 25% = 0.7725
- Min = 0.64

#### f1
- Mean = 0.323602501847938
- Standard deviation = 0.16370762517505577
- Max = 0.5294117647058824
- 75% = 0.4292929292929293
- Median = 0.37254901960784315
- 25% = 0.2652519893899204
- Min = 0.0

#### precision
- Mean = 0.46150703871292104
- Standard deviation = 0.26169791804420117
- Max = 0.8571428571428571
- 75% = 0.6488095238095238
- Median = 0.5192307692307692
- 25% = 0.2540849673202614
- Min = 0.0

#### recall
- Mean = 0.275
- Standard deviation = 0.15206906325745548
- Max = 0.45
- 75% = 0.375
- Median = 0.32499999999999996
- 25% = 0.17500000000000002
- Min = 0.0

#### facing_probas
- Mean = [0.48375  0.468625 0.46325  0.45425  0.451625]
- Standard deviation = [0.02416997 0.02543097 0.02325269 0.02369995 0.02521873]
- Max = [0.529 0.503 0.501 0.491 0.508]
- 75% = [0.502   0.4925  0.477   0.47425 0.4575 ]
- Median = [0.4755 0.466  0.4595 0.449  0.4515]
- 25% = [0.466   0.45625 0.45375 0.43575 0.437  ]
- Min = [0.454 0.421 0.421 0.423 0.42 ]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 73.125 | 6.875 |
| Actual Positive | 14.5 | 5.5 |

### robot-2
#### accuracy
- Mean = 0.74
- Standard deviation = 0.0264575131106459
- Max = 0.77
- 75% = 0.76
- Median = 0.745
- 25% = 0.73
- Min = 0.68

#### f1
- Mean = 0.3737643673789185
- Standard deviation = 0.07227340527536373
- Max = 0.5000000000000001
- 75% = 0.40143084260731315
- Median = 0.3636977058029689
- 25% = 0.32692307692307687
- Min = 0.2727272727272727

#### precision
- Mean = 0.36290136191007244
- Standard deviation = 0.05083132880553882
- Max = 0.4117647058823529
- 75% = 0.3932291666666667
- Median = 0.3810483870967742
- 25% = 0.35526315789473684
- Min = 0.25

#### recall
- Mean = 0.4
- Standard deviation = 0.13228756555322954
- Max = 0.65
- 75% = 0.4125
- Median = 0.35
- 25% = 0.3
- Min = 0.3

#### facing_probas
- Mean = [0.55525  0.6125   0.618625 0.56825  0.49875 ]
- Standard deviation = [0.02838463 0.02365375 0.02634833 0.02047407 0.02831409]
- Max = [0.59  0.655 0.654 0.604 0.54 ]
- 75% = [0.57775 0.62825 0.637   0.583   0.5175 ]
- Median = [0.562  0.6065 0.618  0.565  0.4975]
- 25% = [0.531  0.5945 0.606  0.551  0.479 ]
- Min = [0.507 0.581 0.567 0.544 0.453]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 66.0 | 14.0 |
| Actual Positive | 12.0 | 8.0 |

### robot-3
#### accuracy
- Mean = 0.71
- Standard deviation = 0.05477225575051663
- Max = 0.79
- 75% = 0.755
- Median = 0.7
- 25% = 0.6849999999999999
- Min = 0.61

#### f1
- Mean = 0.3749151384817947
- Standard deviation = 0.077739296853887
- Max = 0.4918032786885247
- 75% = 0.405825885468388
- Median = 0.36549165120593696
- 25% = 0.34195804195804197
- Min = 0.25806451612903225

#### precision
- Mean = 0.3474718092386633
- Standard deviation = 0.06373307024967229
- Max = 0.46153846153846156
- 75% = 0.3709103840682788
- Median = 0.3647450110864745
- 25% = 0.30851619644723094
- Min = 0.22857142857142856

#### recall
- Mean = 0.45625
- Standard deviation = 0.1775484088917724
- Max = 0.75
- 75% = 0.55
- Median = 0.42500000000000004
- 25% = 0.33749999999999997
- Min = 0.2

#### facing_probas
- Mean = [0.509375 0.586625 0.599625 0.554125 0.499625]
- Standard deviation = [0.02890042 0.03108833 0.02653741 0.01641217 0.03496404]
- Max = [0.555 0.656 0.646 0.586 0.566]
- 75% = [0.5325  0.5995  0.6125  0.56375 0.5075 ]
- Median = [0.51   0.5815 0.597  0.551  0.491 ]
- 25% = [0.4895  0.5595  0.58525 0.54125 0.4805 ]
- Min = [0.464 0.556 0.556 0.535 0.461]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 61.875 | 18.125 |
| Actual Positive | 10.875 | 9.125 |

### robot-4
#### accuracy
- Mean = 0.705
- Standard deviation = 0.030822070014844875
- Max = 0.77
- 75% = 0.72
- Median = 0.7
- 25% = 0.6875
- Min = 0.66

#### f1
- Mean = 0.26147753437548044
- Standard deviation = 0.07203165623637198
- Max = 0.4390243902439024
- 75% = 0.268796992481203
- Median = 0.23558758314855877
- 25% = 0.2192982456140351
- Min = 0.20000000000000004

#### precision
- Mean = 0.2622159090909091
- Standard deviation = 0.06812809707821105
- Max = 0.42857142857142855
- 75% = 0.273989898989899
- Median = 0.24404761904761904
- 25% = 0.21875
- Min = 0.2

#### recall
- Mean = 0.2625
- Standard deviation = 0.07806247497997998
- Max = 0.45
- 75% = 0.2625
- Median = 0.25
- 25% = 0.2
- Min = 0.2

#### facing_probas
- Mean = [0.4795   0.5725   0.594875 0.598375 0.5505  ]
- Standard deviation = [0.03694252 0.02324866 0.02435384 0.02225386 0.02915905]
- Max = [0.547 0.627 0.638 0.635 0.603]
- 75% = [0.4975  0.57925 0.61175 0.612   0.57225]
- Median = [0.4655 0.567  0.5875 0.595  0.541 ]
- 25% = [0.455   0.55575 0.579   0.5815  0.53625]
- Min = [0.434 0.551 0.563 0.57  0.503]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 65.25 | 14.75 |
| Actual Positive | 14.75 | 5.25 |

### robot-5
#### accuracy
- Mean = 0.78125
- Standard deviation = 0.027585095613392414
- Max = 0.81
- 75% = 0.8
- Median = 0.79
- 25% = 0.775
- Min = 0.72

#### f1
- Mean = 0.11908519721019721
- Standard deviation = 0.09453944911304012
- Max = 0.29629629629629634
- 75% = 0.16071428571428573
- Median = 0.10795454545454546
- 25% = 0.0625
- Min = 0.0

#### precision
- Mean = 0.26413690476190477
- Standard deviation = 0.19741674016059255
- Max = 0.5714285714285714
- 75% = 0.40625
- Median = 0.25
- 25% = 0.125
- Min = 0.0

#### recall
- Mean = 0.08125000000000002
- Standard deviation = 0.06584783595532961
- Max = 0.2
- 75% = 0.1125
- Median = 0.07500000000000001
- 25% = 0.037500000000000006
- Min = 0.0

#### facing_probas
- Mean = [0.446375 0.501125 0.515375 0.577875 0.53275 ]
- Standard deviation = [0.03742305 0.02244124 0.01484872 0.02418387 0.03157036]
- Max = [0.48  0.542 0.548 0.613 0.593]
- 75% = [0.4745  0.5145  0.51825 0.59375 0.5475 ]
- Median = [0.459  0.4915 0.515  0.579  0.5215]
- 25% = [0.43475 0.4835  0.5075  0.5535  0.508  ]
- Min = [0.362 0.478 0.494 0.547 0.5  ]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 76.5 | 3.5 |
| Actual Positive | 18.375 | 1.625 |

### robot-6
#### accuracy
- Mean = 0.29500000000000004
- Standard deviation = 0.045552167895721495
- Max = 0.39
- 75% = 0.3125
- Median = 0.28500000000000003
- 25% = 0.2775
- Min = 0.22

#### f1
- Mean = 0.45371837474158266
- Standard deviation = 0.053514816418977054
- Max = 0.5611510791366906
- 75% = 0.4761739532731899
- Median = 0.4435562015503876
- 25% = 0.43442421259842523
- Min = 0.36065573770491804

#### precision
- Mean = 1.0
- Standard deviation = 0.0
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 1.0
- Min = 1.0

#### recall
- Mean = 0.29500000000000004
- Standard deviation = 0.045552167895721495
- Max = 0.39
- 75% = 0.3125
- Median = 0.28500000000000003
- 25% = 0.2775
- Min = 0.22

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
| Actual Positive | 70.5 | 29.5 |

