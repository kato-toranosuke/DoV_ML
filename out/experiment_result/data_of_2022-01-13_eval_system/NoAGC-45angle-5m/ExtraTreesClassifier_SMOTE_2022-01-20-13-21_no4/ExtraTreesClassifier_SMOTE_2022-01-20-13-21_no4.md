# ExtraTreesClassifier_SMOTE_2022-01-20-13-21_no4
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
	- sampling_strategy_ = OrderedDict([(0, 3)])
	- nn_k_ = NearestNeighbors(n_neighbors=6)

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
	- min_samples_split = 10
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
	- oob_decision_function_ = [[0.         1.        ]
 [0.14880952 0.85119048]
 [0.         1.        ]
 [0.         1.        ]
 [0.875      0.125     ]
 [0.94444444 0.05555556]
 [0.92857143 0.07142857]
 [1.         0.        ]
 [1.         0.        ]
 [1.         0.        ]
 [0.32312925 0.67687075]
 [0.28571429 0.71428571]
 [0.         1.        ]
 [0.         1.        ]
 [0.         1.        ]
 [0.11111111 0.88888889]
 [0.875      0.125     ]
 [0.55555556 0.44444444]
 [1.         0.        ]
 [1.         0.        ]
 [0.95833333 0.04166667]
 [0.89583333 0.10416667]
 [0.31122449 0.68877551]
 [0.63333333 0.36666667]
 [0.         1.        ]
 [0.         1.        ]
 [0.         1.        ]
 [0.125      0.875     ]
 [1.         0.        ]
 [0.67517007 0.32482993]
 [1.         0.        ]
 [1.         0.        ]
 [1.         0.        ]
 [1.         0.        ]
 [0.39732143 0.60267857]
 [0.1547619  0.8452381 ]
 [0.         1.        ]
 [0.30612245 0.69387755]
 [0.         1.        ]
 [0.14285714 0.85714286]
 [1.         0.        ]
 [1.         0.        ]
 [1.         0.        ]
 [1.         0.        ]
 [1.         0.        ]
 [1.         0.        ]
 [0.10714286 0.89285714]
 [0.32142857 0.67857143]
 [0.16190476 0.83809524]
 [0.33333333 0.66666667]
 [0.04761905 0.95238095]
 [0.         1.        ]
 [0.66836735 0.33163265]
 [0.95833333 0.04166667]
 [1.         0.        ]
 [0.16666667 0.83333333]
 [0.         1.        ]
 [0.38888889 0.61111111]
 [0.2        0.8       ]
 [0.96875    0.03125   ]
 [0.83333333 0.16666667]
 [0.         1.        ]
 [0.         1.        ]
 [0.11111111 0.88888889]
 [0.39285714 0.60714286]
 [1.         0.        ]
 [0.77380952 0.22619048]
 [0.         1.        ]
 [0.         1.        ]
 [0.         1.        ]
 [1.         0.        ]
 [1.         0.        ]
 [0.82142857 0.17857143]
 [0.02857143 0.97142857]
 [0.13333333 0.86666667]
 [1.         0.        ]
 [0.9375     0.0625    ]
 [1.         0.        ]]
	- oob_score_ = 0.9615384615384616

#### Importance of features
- srmr = 0.35851275032612906
- gp_max_val_mean = 0.17402602191319005
- gp_max_val_max = 0.15505895291687147
- gp_auc_mean = 0.08008291305864815
- gp_auc_max = 0.07989976620643555
- tdoa_min = 0.06690448343079922
- gp_max_val_min = 0.04615801289605763
- ratio_max_to_10ms_ave_peaks = 0.011675980839416056
- coe3[2] = 0.010437275985663085
- gp_auc_min = 0.00674074074074075
- gp_auc_range = 0.004889515749882467
- ac_auc = 0.003439153439153442
- diff_std = 0.002174432497013144
- low_power = 0.0
- high_power = 0.0
- hlbr = 0.0
- coe1[0] = 0.0
- coe1[1] = 0.0
- coe3[0] = 0.0
- coe3[1] = 0.0
- coe3[3] = 0.0
- ratio_max_to_9th_ave_peaks = 0.0
- ac_std = 0.0
- diff_auc = 0.0
- gp_max_val_std = 0.0
- gp_max_val_range = 0.0
- gp_max_ix_std = 0.0
- gp_max_ix_range = 0.0
- gp_max_ix_min = 0.0
- gp_max_ix_max = 0.0
- gp_max_ix_mean = 0.0
- gp_auc_std = 0.0
- tdoa_std = 0.0
- tdoa_range = 0.0
- tdoa_max = 0.0
- tdoa_mean = 0.0

## Evaluation
cv = 8
### robot-1
#### accuracy
- Mean = 0.95625
- Standard deviation = 0.032379584617471535
- Max = 0.99
- 75% = 0.9824999999999999
- Median = 0.965
- 25% = 0.9375
- Min = 0.89

#### f1
- Mean = 0.9020502121765188
- Standard deviation = 0.06571621940117554
- Max = 0.975609756097561
- 75% = 0.9564024390243903
- Median = 0.9157955865272938
- 25% = 0.8588383838383837
- Min = 0.7755102040816326

#### precision
- Mean = 0.853749906702493
- Standard deviation = 0.10216200808642187
- Max = 0.9523809523809523
- 75% = 0.950595238095238
- Median = 0.8841991341991342
- 25% = 0.78375
- Min = 0.6551724137931034

#### recall
- Mean = 0.9624999999999999
- Standard deviation = 0.021650635094610987
- Max = 1.0
- 75% = 0.9624999999999999
- Median = 0.95
- 25% = 0.95
- Min = 0.95

#### facing_probas
- Mean = [0.9131994  0.67379437 0.03901326 0.00602083 0.00404167]
- Standard deviation = [0.02033158 0.12214856 0.03235988 0.00744619 0.00501785]
- Max = [0.94690476 0.83428571 0.10102273 0.019      0.014     ]
- 75% = [0.9225     0.78682089 0.05364583 0.0115625  0.00625   ]
- Median = [0.91458333 0.64875    0.02825    0.00145833 0.00166667]
- 25% = [0.9        0.60464583 0.01458333 0.         0.        ]
- Min = [0.87785714 0.45208333 0.005      0.         0.        ]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 76.375 | 3.625 |
| Actual Positive | 0.75 | 19.25 |

### robot-2
#### accuracy
- Mean = 0.96
- Standard deviation = 0.028284271247461898
- Max = 0.99
- 75% = 0.9824999999999999
- Median = 0.965
- 25% = 0.9475
- Min = 0.9

#### f1
- Mean = 0.882135133296124
- Standard deviation = 0.09569718522319375
- Max = 0.9743589743589743
- 75% = 0.9541160593792173
- Median = 0.9068278805120911
- 25% = 0.8487394957983193
- Min = 0.6666666666666666

#### precision
- Mean = 0.9930555555555556
- Standard deviation = 0.01837327299350411
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 1.0
- Min = 0.9444444444444444

#### recall
- Mean = 0.8062499999999999
- Standard deviation = 0.14238482187368146
- Max = 0.95
- 75% = 0.9125
- Median = 0.85
- 25% = 0.7375
- Min = 0.5

#### facing_probas
- Mean = [0.86705357 0.93970833 0.69032698 0.06794995 0.00807576]
- Standard deviation = [0.03701393 0.03464122 0.13380276 0.07278156 0.01228067]
- Max = [0.93097619 0.97375    0.90265152 0.21590909 0.0365    ]
- 75% = [0.87875    0.96135417 0.82166071 0.10014286 0.01369318]
- Median = [0.86120833 0.95175    0.63783333 0.04166667 0.        ]
- 25% = [0.856875   0.930625   0.61083333 0.006875   0.        ]
- Min = [0.79553571 0.85666667 0.48458333 0.         0.        ]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 79.875 | 0.125 |
| Actual Positive | 3.875 | 16.125 |

### robot-3
#### accuracy
- Mean = 0.94875
- Standard deviation = 0.010532687216470433
- Max = 0.96
- 75% = 0.96
- Median = 0.95
- 25% = 0.94
- Min = 0.93

#### f1
- Mean = 0.8566573926868044
- Standard deviation = 0.03182543843403449
- Max = 0.888888888888889
- 75% = 0.888888888888889
- Median = 0.8648648648648648
- 25% = 0.8308823529411765
- Min = 0.8

#### precision
- Mean = 0.9691482843137256
- Standard deviation = 0.03093639196614605
- Max = 1.0
- 75% = 1.0
- Median = 0.9705882352941176
- 25% = 0.9402573529411764
- Min = 0.9333333333333333

#### recall
- Mean = 0.76875
- Standard deviation = 0.04284784125250656
- Max = 0.8
- 75% = 0.8
- Median = 0.8
- 25% = 0.7375
- Min = 0.7

#### facing_probas
- Mean = [0.23822795 0.93082589 0.93559226 0.84663515 0.10797078]
- Standard deviation = [0.11997987 0.03598236 0.02086025 0.09209586 0.08028004]
- Max = [0.40690476 0.9875     0.95333333 0.96982143 0.21424242]
- 75% = [0.36510768 0.95625    0.94854167 0.95529708 0.20448214]
- Median = [0.199375   0.93625    0.9465     0.79770833 0.06675   ]
- 25% = [0.140625   0.9028125  0.93151786 0.7840625  0.04625   ]
- Min = [0.09666667 0.86785714 0.8965     0.739      0.02      ]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 79.5 | 0.5 |
| Actual Positive | 4.625 | 15.375 |

### robot-4
#### accuracy
- Mean = 0.8225
- Standard deviation = 0.04892596447695232
- Max = 0.87
- 75% = 0.8425
- Median = 0.84
- 25% = 0.825
- Min = 0.7

#### f1
- Mean = 0.31766160570508395
- Standard deviation = 0.18409909587968784
- Max = 0.5714285714285715
- 75% = 0.451058201058201
- Median = 0.33333333333333337
- 25% = 0.2194616977225673
- Min = 0.0

#### precision
- Mean = 0.8020833333333333
- Standard deviation = 0.3279182549728582
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 0.7291666666666666
- Min = 0.0

#### recall
- Mean = 0.21875
- Standard deviation = 0.15194057226429022
- Max = 0.5
- 75% = 0.3125
- Median = 0.2
- 25% = 0.125
- Min = 0.0

#### facing_probas
- Mean = [0.00870076 0.54469318 0.92706399 0.96909375 0.75731953]
- Standard deviation = [0.0105883  0.05355701 0.02052093 0.02038992 0.09127258]
- Max = [0.02602273 0.6460119  0.95666667 0.995      0.88595238]
- 75% = [0.01664583 0.56111607 0.94       0.98479167 0.8592684 ]
- Median = [0.0025     0.54566667 0.93182738 0.97208333 0.725625  ]
- 25% = [0.         0.52394886 0.9075     0.9619375  0.68104167]
- Min = [0.         0.44458333 0.89452381 0.9325     0.64375   ]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 77.875 | 2.125 |
| Actual Positive | 15.625 | 4.375 |

### robot-5
#### accuracy
- Mean = 0.9762500000000001
- Standard deviation = 0.03276335605520289
- Max = 1.0
- 75% = 1.0
- Median = 0.99
- 25% = 0.9724999999999999
- Min = 0.9

#### f1
- Mean = 0.927486986697513
- Standard deviation = 0.10813139292378542
- Max = 1.0
- 75% = 1.0
- Median = 0.9743589743589743
- 25% = 0.924812030075188
- Min = 0.6666666666666666

#### precision
- Mean = 1.0
- Standard deviation = 0.0
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 1.0
- Min = 1.0

#### recall
- Mean = 0.8812500000000001
- Standard deviation = 0.16381678027601446
- Max = 1.0
- 75% = 1.0
- Median = 0.95
- 25% = 0.8625
- Min = 0.5

#### facing_probas
- Mean = [0.00604451 0.01149337 0.2354191  0.9175119  0.93034226]
- Standard deviation = [0.00827439 0.0136147  0.11716846 0.0359673  0.01342261]
- Max = [0.01958333 0.03511364 0.45863095 0.96785714 0.94333333]
- 75% = [0.01207955 0.01970833 0.31372511 0.95722024 0.93822917]
- Median = [0.         0.005      0.18145833 0.89875    0.93491071]
- 25% = [0.       0.       0.146625 0.88975  0.9275  ]
- Min = [0.     0.     0.1125 0.88   0.9   ]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 80.0 | 0.0 |
| Actual Positive | 2.375 | 17.625 |

### robot-6
#### accuracy
- Mean = 0.7275
- Standard deviation = 0.04322904116447646
- Max = 0.78
- 75% = 0.7525
- Median = 0.74
- 25% = 0.71
- Min = 0.63

#### f1
- Mean = 0.8415102570702335
- Standard deviation = 0.02987695958959811
- Max = 0.8764044943820225
- 75% = 0.8587662337662337
- Median = 0.8505367464905037
- 25% = 0.8304093567251462
- Min = 0.7730061349693252

#### precision
- Mean = 1.0
- Standard deviation = 0.0
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 1.0
- Min = 1.0

#### recall
- Mean = 0.7275
- Standard deviation = 0.04322904116447646
- Max = 0.78
- 75% = 0.7525
- Median = 0.74
- 25% = 0.71
- Min = 0.63

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
| Actual Positive | 27.25 | 72.75 |

