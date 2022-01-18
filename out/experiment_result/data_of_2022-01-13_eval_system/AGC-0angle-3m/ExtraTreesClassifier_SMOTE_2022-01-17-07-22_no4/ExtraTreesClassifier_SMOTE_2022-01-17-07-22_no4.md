# ExtraTreesClassifier_SMOTE_2022-01-17-07-22_no4
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
- resampler = SMOTE
- estimator = ExtraTreesClassifier

### Arguments for hyperparameter search
- resampler = SMOTE
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
	- k_neighbors = 5
	- n_jobs = -1
	- n_features_in_ = 36
	- sampling_strategy_ = OrderedDict([(1, 45)])
	- nn_k_ = NearestNeighbors(n_neighbors=6)

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
	- oob_decision_function_ = [[0.         1.        ]
 [0.5        0.5       ]
 [0.93333333 0.06666667]
 [1.         0.        ]
 [1.         0.        ]
 [0.68421053 0.31578947]
 [0.         1.        ]
 [0.84210526 0.15789474]
 [0.94444444 0.05555556]
 [1.         0.        ]
 [0.95238095 0.04761905]
 [0.94444444 0.05555556]
 [0.21428571 0.78571429]
 [0.82352941 0.17647059]
 [1.         0.        ]
 [1.         0.        ]
 [1.         0.        ]
 [0.90909091 0.09090909]
 [0.47058824 0.52941176]
 [0.9047619  0.0952381 ]
 [0.95833333 0.04166667]
 [1.         0.        ]
 [1.         0.        ]
 [0.84210526 0.15789474]
 [0.46666667 0.53333333]
 [0.15789474 0.84210526]
 [0.17647059 0.82352941]
 [0.68181818 0.31818182]
 [1.         0.        ]
 [1.         0.        ]
 [0.95454545 0.04545455]
 [1.         0.        ]
 [1.         0.        ]
 [1.         0.        ]
 [1.         0.        ]
 [0.66666667 0.33333333]
 [0.75       0.25      ]
 [0.26315789 0.73684211]
 [0.05       0.95      ]
 [0.55       0.45      ]
 [0.4375     0.5625    ]
 [1.         0.        ]
 [0.94117647 0.05882353]
 [1.         0.        ]
 [1.         0.        ]
 [0.94736842 0.05263158]
 [0.9375     0.0625    ]
 [0.94736842 0.05263158]
 [0.72222222 0.27777778]
 [0.11764706 0.88235294]
 [0.         1.        ]
 [1.         0.        ]
 [0.77777778 0.22222222]
 [1.         0.        ]
 [1.         0.        ]
 [1.         0.        ]
 [1.         0.        ]
 [0.93333333 0.06666667]
 [1.         0.        ]
 [1.         0.        ]
 [0.69230769 0.30769231]
 [0.         1.        ]
 [0.2        0.8       ]
 [0.73684211 0.26315789]
 [0.29411765 0.70588235]
 [1.         0.        ]
 [1.         0.        ]
 [1.         0.        ]
 [1.         0.        ]
 [1.         0.        ]
 [0.9375     0.0625    ]
 [0.75       0.25      ]
 [0.94444444 0.05555556]
 [0.17647059 0.82352941]
 [0.         1.        ]
 [0.         1.        ]
 [0.0625     0.9375    ]
 [0.         1.        ]
 [0.09090909 0.90909091]
 [0.         1.        ]
 [0.         1.        ]
 [0.         1.        ]
 [0.15789474 0.84210526]
 [0.11764706 0.88235294]
 [0.         1.        ]
 [0.         1.        ]
 [0.         1.        ]
 [0.06666667 0.93333333]
 [0.41176471 0.58823529]
 [0.         1.        ]
 [0.10526316 0.89473684]
 [0.         1.        ]
 [0.         1.        ]
 [0.25       0.75      ]
 [0.         1.        ]
 [0.         1.        ]
 [0.23809524 0.76190476]
 [0.05555556 0.94444444]
 [0.         1.        ]
 [0.         1.        ]
 [0.0625     0.9375    ]
 [0.         1.        ]
 [0.0625     0.9375    ]
 [0.11111111 0.88888889]
 [0.05555556 0.94444444]
 [0.         1.        ]
 [0.         1.        ]
 [0.125      0.875     ]
 [0.         1.        ]
 [0.         1.        ]
 [0.         1.        ]
 [0.2        0.8       ]
 [0.04761905 0.95238095]
 [0.11764706 0.88235294]
 [0.         1.        ]
 [0.2        0.8       ]
 [0.         1.        ]
 [0.         1.        ]
 [0.05882353 0.94117647]
 [0.         1.        ]]
	- oob_score_ = 0.9833333333333333

#### Importance of features
- gp_auc_max = 0.1650955706554923
- gp_max_val_max = 0.07509278478166728
- diff_std = 0.06861083483723332
- gp_max_val_mean = 0.06476317260159614
- gp_auc_min = 0.0562548167526684
- high_power = 0.05257900263948327
- tdoa_mean = 0.050897247053800436
- gp_auc_mean = 0.04713166278245946
- hlbr = 0.045464934697533724
- gp_max_val_min = 0.04411202652261946
- diff_auc = 0.03381521577681119
- gp_max_val_std = 0.03343574535501452
- gp_max_ix_mean = 0.03301423315067253
- srmr = 0.028940150265628396
- coe1[1] = 0.02028952388735546
- tdoa_min = 0.01849959804210802
- coe1[0] = 0.017373648908676757
- gp_max_ix_std = 0.014287603278470189
- gp_auc_std = 0.01426909263573331
- gp_auc_range = 0.01421724315248429
- tdoa_std = 0.012042703871407033
- gp_max_ix_range = 0.011689921314958183
- coe3[3] = 0.011441365445417398
- low_power = 0.010875721027912236
- ac_std = 0.010439107091919708
- ac_auc = 0.009434725899748577
- coe3[2] = 0.008493177282568038
- tdoa_range = 0.007111734085418298
- gp_max_ix_min = 0.005462184873949578
- ratio_max_to_10ms_ave_peaks = 0.004257398392552455
- ratio_max_to_9th_ave_peaks = 0.0034226190476190485
- tdoa_max = 0.0026807224194882063
- gp_max_ix_max = 0.0026433294735604975
- gp_max_val_range = 0.001861181995972285
- coe3[0] = 0.0
- coe3[1] = 0.0

## Evaluation
cv = 8
### robot-1
#### accuracy
- Mean = 0.96875
- Standard deviation = 0.024717149916606476
- Max = 0.99
- 75% = 0.98
- Median = 0.98
- 25% = 0.9724999999999999
- Min = 0.91

#### f1
- Mean = 0.921480246239553
- Standard deviation = 0.061325960450230706
- Max = 0.9743589743589743
- 75% = 0.9523809523809523
- Median = 0.9500000000000001
- 25% = 0.9267425320056899
- Min = 0.7804878048780488

#### precision
- Mean = 0.9276578813343519
- Standard deviation = 0.07054379718625331
- Max = 1.0
- 75% = 0.9624999999999999
- Median = 0.9455882352941176
- 25% = 0.9090909090909091
- Min = 0.7619047619047619

#### recall
- Mean = 0.91875
- Standard deviation = 0.0747391296443837
- Max = 1.0
- 75% = 0.9624999999999999
- Median = 0.95
- 25% = 0.875
- Min = 0.8

#### facing_probas
- Mean = [0.75229167 0.28354167 0.019375   0.00645833 0.00833333]
- Standard deviation = [0.03413553 0.07078644 0.01216032 0.00561728 0.00606676]
- Max = [0.80166667 0.44166667 0.03333333 0.01833333 0.02      ]
- 75% = [0.78458333 0.29958333 0.03166667 0.00875    0.01208333]
- Median = [0.74166667 0.28333333 0.02166667 0.00583333 0.0075    ]
- 25% = [0.7275     0.24208333 0.00625    0.0025     0.00333333]
- Min = [0.70833333 0.19666667 0.00333333 0.         0.        ]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 78.5 | 1.5 |
| Actual Positive | 1.625 | 18.375 |

### robot-2
#### accuracy
- Mean = 0.9312499999999999
- Standard deviation = 0.012686114456365236
- Max = 0.95
- 75% = 0.94
- Median = 0.935
- 25% = 0.92
- Min = 0.91

#### f1
- Mean = 0.7946270443661335
- Standard deviation = 0.04869340422367025
- Max = 0.8571428571428571
- 75% = 0.8333333333333334
- Median = 0.8117647058823529
- 25% = 0.7499999999999999
- Min = 0.7096774193548387

#### precision
- Mean = 0.9760416666666667
- Standard deviation = 0.03095345407938255
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 0.9375
- Min = 0.9333333333333333

#### recall
- Mean = 0.675
- Standard deviation = 0.075
- Max = 0.75
- 75% = 0.75
- Median = 0.7
- 25% = 0.6
- Min = 0.55

#### facing_probas
- Mean = [0.38875    0.64604167 0.10104167 0.01083333 0.00354167]
- Standard deviation = [0.06159202 0.0516528  0.02473383 0.00812233 0.003674  ]
- Max = [0.49666667 0.73166667 0.13166667 0.025      0.01166667]
- 75% = [0.41583333 0.68791667 0.12333333 0.01458333 0.005     ]
- Median = [0.37       0.64416667 0.1025     0.0075     0.00333333]
- 25% = [0.34083333 0.59375    0.07958333 0.00458333 0.        ]
- Min = [0.32       0.585      0.06333333 0.00333333 0.        ]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 79.625 | 0.375 |
| Actual Positive | 6.5 | 13.5 |

### robot-3
#### accuracy
- Mean = 0.985
- Standard deviation = 0.007071067811865481
- Max = 1.0
- 75% = 0.99
- Median = 0.98
- 25% = 0.98
- Min = 0.98

#### f1
- Mean = 0.9613529014844804
- Standard deviation = 0.01829066671140122
- Max = 1.0
- 75% = 0.9743589743589743
- Median = 0.9500000000000001
- 25% = 0.9473684210526316
- Min = 0.9473684210526316

#### precision
- Mean = 0.9875
- Standard deviation = 0.021650635094610987
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 0.9875
- Min = 0.95

#### recall
- Mean = 0.9375
- Standard deviation = 0.033071891388307365
- Max = 1.0
- 75% = 0.95
- Median = 0.95
- 25% = 0.9
- Min = 0.9

#### facing_probas
- Mean = [0.03       0.42333333 0.85416667 0.21583333 0.02375   ]
- Standard deviation = [0.00912871 0.07683406 0.05600719 0.04919491 0.0129837 ]
- Max = [0.04166667 0.57       0.93333333 0.30333333 0.04833333]
- 75% = [0.03791667 0.47583333 0.88333333 0.24708333 0.02958333]
- Median = [0.02916667 0.40166667 0.87416667 0.22083333 0.02583333]
- 25% = [0.02458333 0.35916667 0.82458333 0.175      0.01083333]
- Min = [0.01333333 0.33666667 0.75       0.14333333 0.00833333]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 79.75 | 0.25 |
| Actual Positive | 1.25 | 18.75 |

### robot-4
#### accuracy
- Mean = 0.9325
- Standard deviation = 0.022220486043288946
- Max = 0.97
- 75% = 0.945
- Median = 0.93
- 25% = 0.9175
- Min = 0.9

#### f1
- Mean = 0.8506429740472294
- Standard deviation = 0.04220303392566949
- Max = 0.9230769230769231
- 75% = 0.8690476190476191
- Median = 0.851063829787234
- 25% = 0.8092705167173253
- Min = 0.8

#### precision
- Mean = 0.7817207159312423
- Standard deviation = 0.08532469948030715
- Max = 0.9473684210526315
- 75% = 0.8295454545454546
- Median = 0.7567340067340067
- 25% = 0.7314814814814814
- Min = 0.6666666666666666

#### recall
- Mean = 0.94375
- Standard deviation = 0.05266343608235224
- Max = 1.0
- 75% = 1.0
- Median = 0.95
- 25% = 0.9
- Min = 0.85

#### facing_probas
- Mean = [0.001875   0.01833333 0.32291667 0.81895833 0.14375   ]
- Standard deviation = [0.00154504 0.00986013 0.05760106 0.03976439 0.08282658]
- Max = [0.005      0.03833333 0.42166667 0.865      0.31666667]
- 75% = [0.00208333 0.02375    0.35291667 0.8525     0.19208333]
- Median = [0.00166667 0.01666667 0.31666667 0.82666667 0.09416667]
- 25% = [0.00125    0.01208333 0.28791667 0.79208333 0.085     ]
- Min = [0.         0.005      0.245      0.745      0.07333333]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 74.375 | 5.625 |
| Actual Positive | 1.125 | 18.875 |

### robot-5
#### accuracy
- Mean = 0.9125000000000001
- Standard deviation = 0.020463381929681116
- Max = 0.95
- 75% = 0.93
- Median = 0.905
- 25% = 0.8975
- Min = 0.89

#### f1
- Mean = 0.7146613119916791
- Standard deviation = 0.08163619293510728
- Max = 0.8571428571428571
- 75% = 0.787878787878788
- Median = 0.6881720430107527
- 25% = 0.6551724137931034
- Min = 0.6206896551724138

#### precision
- Mean = 1.0
- Standard deviation = 0.0
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 1.0
- Min = 1.0

#### recall
- Mean = 0.5625
- Standard deviation = 0.10231690964840562
- Max = 0.75
- 75% = 0.65
- Median = 0.525
- 25% = 0.4875
- Min = 0.45

#### facing_probas
- Mean = [0.00104167 0.00145833 0.03208333 0.60208333 0.71333333]
- Standard deviation = [0.00219493 0.00175545 0.01964529 0.06135479 0.03068659]
- Max = [0.00666667 0.005      0.07       0.69       0.765     ]
- 75% = [4.16666667e-04 2.08333333e-03 4.04166667e-02 6.70416667e-01
 7.24583333e-01]
- Median = [0.         0.00083333 0.02583333 0.5775     0.70916667]
- 25% = [0.      0.      0.01625 0.55    0.69125]
- Min = [0.         0.         0.01166667 0.52666667 0.67666667]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 80.0 | 0.0 |
| Actual Positive | 8.75 | 11.25 |

### robot-6
#### accuracy
- Mean = 0.8075
- Standard deviation = 0.03307189138830737
- Max = 0.85
- 75% = 0.8325
- Median = 0.81
- 25% = 0.795
- Min = 0.74

#### f1
- Mean = 0.8931236958562219
- Standard deviation = 0.0205327982326922
- Max = 0.9189189189189189
- 75% = 0.9085887384176763
- Median = 0.8950276243093923
- 25% = 0.8857677902621723
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
- Mean = 0.8075
- Standard deviation = 0.03307189138830737
- Max = 0.85
- 75% = 0.8325
- Median = 0.81
- 25% = 0.795
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
| Actual Positive | 19.25 | 80.75 |

