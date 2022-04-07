# ExtraTreesClassifier_RandomUnderSampler_2022-01-20-11-59_no2
## Constants
- CSV_PATH = ../out/csv/experiment
- OUTPUT_PATH = ../out/experiment_result/data_of_2022-01-13_eval_system/NoAGC-45angle-5m
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
- AGC_STATUS = ['NoAGC']

## Loaded CSV
- 2021-12-27_AGC.csv
- 2022-01-10_NoAGC.csv
- 2022-01-13_raspi_48000Hz_w1_N2^12_overlap80.csv

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
	- sampling_strategy_ = OrderedDict([(1, 36)])
	- sample_indices_ = [ 2  3  4  8  9 10 14 15 16 20 21 22 29 30 31 32 33 34 41 42 43 44 45 46
 53 54 55 56 57 58 65 66 67 68 69 70 63 72  7 25 60 50 12 51 48 27 35 17
 28 24 37 18 62  0 49 11 23  1 73 39  5 59 71  6 64 47 61 19 40 36 38 13]

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
	- oob_decision_function_ = [[0.66666667 0.33333333]
 [0.94736842 0.05263158]
 [0.90909091 0.09090909]
 [0.42857143 0.57142857]
 [1.         0.        ]
 [0.68421053 0.31578947]
 [0.7        0.3       ]
 [0.76470588 0.23529412]
 [0.83333333 0.16666667]
 [0.9375     0.0625    ]
 [0.95652174 0.04347826]
 [0.88235294 0.11764706]
 [0.78571429 0.21428571]
 [0.58823529 0.41176471]
 [1.         0.        ]
 [1.         0.        ]
 [1.         0.        ]
 [1.         0.        ]
 [0.05882353 0.94117647]
 [0.15       0.85      ]
 [1.         0.        ]
 [1.         0.        ]
 [1.         0.        ]
 [1.         0.        ]
 [0.5        0.5       ]
 [0.47368421 0.52631579]
 [1.         0.        ]
 [1.         0.        ]
 [0.92307692 0.07692308]
 [0.83333333 0.16666667]
 [1.         0.        ]
 [1.         0.        ]
 [1.         0.        ]
 [1.         0.        ]
 [0.7826087  0.2173913 ]
 [0.77777778 0.22222222]
 [0.         1.        ]
 [0.05       0.95      ]
 [0.         1.        ]
 [0.23809524 0.76190476]
 [0.         1.        ]
 [0.15384615 0.84615385]
 [0.05882353 0.94117647]
 [0.11111111 0.88888889]
 [0.36363636 0.63636364]
 [0.2        0.8       ]
 [0.125      0.875     ]
 [0.29411765 0.70588235]
 [0.3125     0.6875    ]
 [0.35294118 0.64705882]
 [0.04545455 0.95454545]
 [0.05555556 0.94444444]
 [0.         1.        ]
 [0.15       0.85      ]
 [0.         1.        ]
 [0.88888889 0.11111111]
 [0.42857143 0.57142857]
 [0.28571429 0.71428571]
 [0.         1.        ]
 [0.         1.        ]
 [0.66666667 0.33333333]
 [0.         1.        ]
 [0.25       0.75      ]
 [0.05263158 0.94736842]
 [0.         1.        ]
 [0.35       0.65      ]
 [0.         1.        ]
 [0.16666667 0.83333333]
 [0.         1.        ]
 [0.05555556 0.94444444]
 [0.14285714 0.85714286]
 [0.         1.        ]]
	- oob_score_ = 0.9166666666666666

#### Importance of features
- srmr = 0.20429833802467418
- gp_auc_mean = 0.12156283630421778
- gp_auc_min = 0.11884560163767698
- gp_max_val_min = 0.11487548702188964
- gp_max_val_max = 0.08508815636917222
- gp_max_val_mean = 0.05900440947578902
- gp_auc_max = 0.04243023154828711
- gp_max_ix_min = 0.03161368215547782
- diff_std = 0.0290281747238269
- hlbr = 0.024105339105339116
- gp_auc_std = 0.020383787599482523
- ratio_max_to_9th_ave_peaks = 0.01781586063098969
- gp_max_val_std = 0.015089589049891506
- tdoa_range = 0.013549731931584484
- tdoa_min = 0.010231134683954713
- gp_max_ix_max = 0.00983016983016983
- coe1[0] = 0.009261641368664784
- high_power = 0.00886886333480761
- gp_max_ix_range = 0.008725071225071226
- gp_max_val_range = 0.008621933621933623
- ratio_max_to_10ms_ave_peaks = 0.008242866524600274
- diff_auc = 0.006852678571428573
- gp_auc_range = 0.006738977072310408
- low_power = 0.006563467492260064
- coe1[1] = 0.006415172129457844
- coe3[3] = 0.005833480021123042
- ac_auc = 0.0033369408369408374
- ac_std = 0.0027863777089783283
- coe3[0] = 0.0
- coe3[1] = 0.0
- coe3[2] = 0.0
- gp_max_ix_std = 0.0
- gp_max_ix_mean = 0.0
- tdoa_std = 0.0
- tdoa_max = 0.0
- tdoa_mean = 0.0

## Evaluation
cv = 8
### robot-1
#### accuracy
- Mean = 0.96875
- Standard deviation = 0.01763341997458237
- Max = 0.99
- 75% = 0.9824999999999999
- Median = 0.97
- 25% = 0.9575
- Min = 0.94

#### f1
- Mean = 0.9276900661259708
- Standard deviation = 0.03959149545787861
- Max = 0.975609756097561
- 75% = 0.9581881533101044
- Median = 0.9307359307359306
- 25% = 0.9027484143763214
- Min = 0.8636363636363635

#### precision
- Mean = 0.8759205015998495
- Standard deviation = 0.05820478679999822
- Max = 0.9523809523809523
- 75% = 0.9199134199134199
- Median = 0.8712121212121212
- 25% = 0.8315217391304348
- Min = 0.7916666666666666

#### recall
- Mean = 0.9875
- Standard deviation = 0.021650635094610987
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 0.9875
- Min = 0.95

#### facing_probas
- Mean = [0.933125   0.71291667 0.04729167 0.01625    0.00541667]
- Standard deviation = [0.0216095  0.09149131 0.02056388 0.01012937 0.0045453 ]
- Max = [0.96       0.86833333 0.08       0.03666667 0.015     ]
- 75% = [0.94875    0.755      0.06458333 0.01958333 0.00625   ]
- Median = [0.94083333 0.73916667 0.04416667 0.01583333 0.00416667]
- 25% = [0.91916667 0.64375    0.02791667 0.01083333 0.00291667]
- Min = [0.89166667 0.575      0.02333333 0.         0.        ]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 77.125 | 2.875 |
| Actual Positive | 0.25 | 19.75 |

### robot-2
#### accuracy
- Mean = 0.96875
- Standard deviation = 0.01763341997458237
- Max = 0.99
- 75% = 0.9824999999999999
- Median = 0.97
- 25% = 0.9575
- Min = 0.94

#### f1
- Mean = 0.9139635948846475
- Standard deviation = 0.050638776672655296
- Max = 0.9743589743589743
- 75% = 0.9541160593792173
- Median = 0.9181286549707603
- 25% = 0.8809523809523809
- Min = 0.8333333333333334

#### precision
- Mean = 0.9921875
- Standard deviation = 0.020669932117692115
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 1.0
- Min = 0.9375

#### recall
- Mean = 0.85
- Standard deviation = 0.07905694150420946
- Max = 0.95
- 75% = 0.9125
- Median = 0.8500000000000001
- 25% = 0.7875000000000001
- Min = 0.75

#### facing_probas
- Mean = [0.88541667 0.95541667 0.72791667 0.105625   0.005     ]
- Standard deviation = [0.0258971  0.02204399 0.07404836 0.0631683  0.00416667]
- Max = [0.92333333 0.97833333 0.85333333 0.19       0.01166667]
- 75% = [0.90291667 0.97208333 0.78666667 0.15375    0.0075    ]
- Median = [0.88833333 0.96333333 0.71666667 0.1225     0.005     ]
- 25% = [0.87041667 0.94125    0.65916667 0.03875    0.00125   ]
- Min = [0.84333333 0.91166667 0.64666667 0.01666667 0.        ]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 79.875 | 0.125 |
| Actual Positive | 3.0 | 17.0 |

### robot-3
#### accuracy
- Mean = 0.98
- Standard deviation = 0.016583123951777013
- Max = 1.0
- 75% = 0.9924999999999999
- Median = 0.985
- 25% = 0.96
- Min = 0.96

#### f1
- Mean = 0.9459857723577236
- Standard deviation = 0.04661881424106671
- Max = 1.0
- 75% = 0.9817073170731707
- Median = 0.9628048780487806
- 25% = 0.888888888888889
- Min = 0.888888888888889

#### precision
- Mean = 0.981845238095238
- Standard deviation = 0.023447772692042377
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 0.9523809523809523
- Min = 0.95

#### recall
- Mean = 0.91875
- Standard deviation = 0.09333240326917547
- Max = 1.0
- 75% = 1.0
- Median = 0.975
- 25% = 0.8
- Min = 0.8

#### facing_probas
- Mean = [0.18479167 0.938125   0.941875   0.88958333 0.08583333]
- Standard deviation = [0.03641426 0.02970266 0.02363551 0.07499884 0.03585271]
- Max = [0.22166667 0.97666667 0.965      0.965      0.14      ]
- 75% = [0.21333333 0.95916667 0.95333333 0.94916667 0.105     ]
- Median = [0.19833333 0.93916667 0.94833333 0.93333333 0.08666667]
- 25% = [0.16666667 0.92125    0.9425     0.80166667 0.06666667]
- Min = [0.10666667 0.885      0.88333333 0.78166667 0.03333333]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 79.625 | 0.375 |
| Actual Positive | 1.625 | 18.375 |

### robot-4
#### accuracy
- Mean = 0.85625
- Standard deviation = 0.032763356055202884
- Max = 0.91
- 75% = 0.875
- Median = 0.855
- 25% = 0.84
- Min = 0.81

#### f1
- Mean = 0.4126125306325529
- Standard deviation = 0.20824405129417523
- Max = 0.7096774193548387
- 75% = 0.5440613026819923
- Median = 0.4307692307692308
- 25% = 0.3238095238095238
- Min = 0.09523809523809523

#### precision
- Mean = 1.0
- Standard deviation = 0.0
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 1.0
- Min = 1.0

#### recall
- Mean = 0.28125
- Standard deviation = 0.16381678027601448
- Max = 0.55
- 75% = 0.375
- Median = 0.275
- 25% = 0.2
- Min = 0.05

#### facing_probas
- Mean = [0.00520833 0.53583333 0.92125    0.97666667 0.76854167]
- Standard deviation = [0.00555512 0.08499591 0.0169507  0.02567154 0.07231028]
- Max = [0.01666667 0.69666667 0.94833333 1.         0.87333333]
- 75% = [0.00666667 0.56083333 0.93       0.99208333 0.81      ]
- Median = [0.00333333 0.52166667 0.9225     0.99       0.78916667]
- 25% = [0.00125    0.50458333 0.91333333 0.96791667 0.72083333]
- Min = [0.         0.38833333 0.88666667 0.92666667 0.64      ]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 80.0 | 0.0 |
| Actual Positive | 14.375 | 5.625 |

### robot-5
#### accuracy
- Mean = 0.99875
- Standard deviation = 0.0033071891388307415
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 1.0
- Min = 0.99

#### f1
- Mean = 0.9967948717948718
- Standard deviation = 0.008479972150848053
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 1.0
- Min = 0.9743589743589743

#### precision
- Mean = 1.0
- Standard deviation = 0.0
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 1.0
- Min = 1.0

#### recall
- Mean = 0.99375
- Standard deviation = 0.016535945694153707
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 1.0
- Min = 0.95

#### facing_probas
- Mean = [0.00354167 0.00208333 0.18979167 0.94083333 0.91354167]
- Standard deviation = [0.00489029 0.00216506 0.04749589 0.05367081 0.03445445]
- Max = [0.01333333 0.00666667 0.26833333 0.99166667 0.96333333]
- 75% = [0.00708333 0.00333333 0.21041667 0.97958333 0.93875   ]
- Median = [0.         0.00166667 0.2        0.9725     0.91416667]
- 25% = [0.         0.         0.17416667 0.9025     0.89041667]
- Min = [0.         0.         0.10166667 0.855      0.86      ]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 80.0 | 0.0 |
| Actual Positive | 0.125 | 19.875 |

### robot-6
#### accuracy
- Mean = 0.80625
- Standard deviation = 0.039031237489989976
- Max = 0.86
- 75% = 0.8425
- Median = 0.8
- 25% = 0.785
- Min = 0.74

#### f1
- Mean = 0.8922144428244149
- Standard deviation = 0.02402816930716975
- Max = 0.924731182795699
- 75% = 0.9145123384253819
- Median = 0.8888545942776012
- 25% = 0.8795252974781429
- Min = 0.8505747126436781

#### precision
- Mean = 1.0
- Standard deviation = 0.0
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 1.0
- Min = 1.0

#### recall
- Mean = 0.80625
- Standard deviation = 0.039031237489989976
- Max = 0.86
- 75% = 0.8425
- Median = 0.8
- 25% = 0.785
- Min = 0.74

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
| Actual Positive | 19.375 | 80.625 |

