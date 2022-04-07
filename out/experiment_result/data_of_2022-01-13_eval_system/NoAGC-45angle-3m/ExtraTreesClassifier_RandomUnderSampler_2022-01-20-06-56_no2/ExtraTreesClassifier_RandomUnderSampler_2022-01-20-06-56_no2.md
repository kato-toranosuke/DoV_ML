# ExtraTreesClassifier_RandomUnderSampler_2022-01-20-06-56_no2
## Constants
- CSV_PATH = ../out/csv/experiment
- OUTPUT_PATH = ../out/experiment_result/data_of_2022-01-13_eval_system/NoAGC-45angle-3m
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
- DISTANCE = [3]
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
	- sample_indices_ = [ 6  7  8  9 10 11 12 13 14 24 25 26 27 28 29 30 31 32 42 43 44 45 46 47
 48 49 50 60 61 62 63 64 65 66 67 68 69 72  4 22 57 53 15 54 51 33 35 17
 34 21 37 18 59  0 52  5 20  1 73 39  2 56 71  3 70 41 58 19 40 36 38 16]

- best_estimator
	- base_estimator = ExtraTreeClassifier()
	- n_estimators = 90
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

#### Importance of features
- gp_max_val_mean = 0.12521024107954085
- gp_max_val_max = 0.11349725534059824
- gp_auc_mean = 0.09563913040069481
- gp_auc_max = 0.09147617635849586
- gp_max_val_min = 0.07526228126878069
- gp_auc_min = 0.07499631937302405
- srmr = 0.05974098667332926
- diff_auc = 0.046404858388149874
- diff_std = 0.037465226351791225
- coe1[0] = 0.03530236086893382
- low_power = 0.029875449071473232
- high_power = 0.027183415534374582
- coe1[1] = 0.023240180069744754
- ac_std = 0.0192584690963916
- ac_auc = 0.01921510122454344
- coe3[3] = 0.01841395573999534
- coe3[2] = 0.013478515741326112
- tdoa_mean = 0.009048064418434788
- gp_max_ix_max = 0.008030872770642782
- ratio_max_to_10ms_ave_peaks = 0.0070018447286683515
- gp_max_ix_mean = 0.006669523546855082
- tdoa_min = 0.006551442517913121
- gp_max_val_std = 0.006385821828432419
- tdoa_range = 0.006348003874520328
- gp_auc_std = 0.006292273541612101
- tdoa_max = 0.006282105050142316
- tdoa_std = 0.006120657563727089
- gp_max_ix_min = 0.005564264847353084
- gp_max_ix_std = 0.004501055819292534
- gp_auc_range = 0.0036348098924114834
- gp_max_val_range = 0.0036287746955006046
- gp_max_ix_range = 0.0032712358052648435
- hlbr = 0.0030415001057702566
- ratio_max_to_9th_ave_peaks = 0.001967826412270857
- coe3[0] = 0.0
- coe3[1] = 0.0

## Evaluation
cv = 8
### robot-1
#### accuracy
- Mean = 0.9862500000000001
- Standard deviation = 0.011110243021644496
- Max = 1.0
- 75% = 1.0
- Median = 0.98
- 25% = 0.98
- Min = 0.97

#### f1
- Mean = 0.967469545957918
- Standard deviation = 0.026153267498684175
- Max = 1.0
- 75% = 1.0
- Median = 0.9523809523809523
- 25% = 0.9523809523809523
- Min = 0.9302325581395349

#### precision
- Mean = 0.9382411067193677
- Standard deviation = 0.04944415607513539
- Max = 1.0
- 75% = 1.0
- Median = 0.9090909090909091
- 25% = 0.9090909090909091
- Min = 0.8695652173913043

#### recall
- Mean = 1.0
- Standard deviation = 0.0
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 1.0
- Min = 1.0

#### facing_probas
- Mean = [9.63888889e-01 7.92916667e-01 4.00694444e-02 3.05555556e-03
 6.25000000e-04]
- Standard deviation = [0.01919684 0.05322671 0.01647912 0.00409192 0.00093943]
- Max = [0.98611111 0.86444444 0.07       0.01166667 0.00277778]
- 75% = [0.98166667 0.83486111 0.05277778 0.00513889 0.00111111]
- Median = [9.66944444e-01 8.06388889e-01 3.66666667e-02 5.55555556e-04
 0.00000000e+00]
- 25% = [0.94777778 0.75805556 0.02777778 0.         0.        ]
- Min = [0.93       0.70555556 0.01833333 0.         0.        ]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 78.625 | 1.375 |
| Actual Positive | 0.0 | 20.0 |

### robot-2
#### accuracy
- Mean = 0.9862500000000001
- Standard deviation = 0.011110243021644496
- Max = 1.0
- 75% = 1.0
- Median = 0.98
- 25% = 0.98
- Min = 0.97

#### f1
- Mean = 0.9635490753911806
- Standard deviation = 0.029633416274002414
- Max = 1.0
- 75% = 1.0
- Median = 0.9473684210526316
- 25% = 0.9473684210526316
- Min = 0.9189189189189189

#### precision
- Mean = 1.0
- Standard deviation = 0.0
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 1.0
- Min = 1.0

#### recall
- Mean = 0.93125
- Standard deviation = 0.055551215108222425
- Max = 1.0
- 75% = 1.0
- Median = 0.9
- 25% = 0.9
- Min = 0.85

#### facing_probas
- Mean = [0.95368056 0.94861111 0.85631944 0.07694444 0.00145833]
- Standard deviation = [0.02927617 0.02658843 0.03492379 0.04712326 0.00173333]
- Max = [0.99277778 0.98333333 0.90444444 0.14277778 0.00444444]
- 75% = [0.98638889 0.98083333 0.88652778 0.11791667 0.00263889]
- Median = [9.45000000e-01 9.36388889e-01 8.58333333e-01 7.13888889e-02
 5.55555556e-04]
- 25% = [0.93166667 0.92888889 0.82888889 0.03541667 0.        ]
- Min = [0.91111111 0.91388889 0.80666667 0.01444444 0.        ]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 80.0 | 0.0 |
| Actual Positive | 1.375 | 18.625 |

### robot-3
#### accuracy
- Mean = 0.99375
- Standard deviation = 0.009921567416492224
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 0.99
- Min = 0.97

#### f1
- Mean = 0.9834546084546085
- Standard deviation = 0.02669050919803191
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 0.9743589743589743
- Min = 0.9189189189189189

#### precision
- Mean = 1.0
- Standard deviation = 0.0
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 1.0
- Min = 1.0

#### recall
- Mean = 0.96875
- Standard deviation = 0.04960783708246108
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 0.95
- Min = 0.85

#### facing_probas
- Mean = [0.15819444 0.88       0.94840278 0.86020833 0.07861111]
- Standard deviation = [0.05288057 0.03963179 0.0242168  0.05788314 0.04868249]
- Max = [0.22722222 0.95833333 0.98555556 0.95222222 0.14222222]
- 75% = [0.21319444 0.90097222 0.96805556 0.91222222 0.12069444]
- Median = [0.14388889 0.87583333 0.94527778 0.84861111 0.08138889]
- 25% = [0.12458333 0.84930556 0.92680556 0.82458333 0.02958333]
- Min = [0.07388889 0.83111111 0.915      0.77055556 0.01611111]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 80.0 | 0.0 |
| Actual Positive | 0.625 | 19.375 |

### robot-4
#### accuracy
- Mean = 0.955
- Standard deviation = 0.018708286933869705
- Max = 0.98
- 75% = 0.9724999999999999
- Median = 0.95
- 25% = 0.94
- Min = 0.93

#### f1
- Mean = 0.8740925910430555
- Standard deviation = 0.055154335677561075
- Max = 0.9473684210526316
- 75% = 0.926031294452347
- Median = 0.8611111111111112
- 25% = 0.8308823529411765
- Min = 0.8

#### precision
- Mean = 0.9760416666666667
- Standard deviation = 0.03095345407938255
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 0.9375
- Min = 0.9333333333333333

#### recall
- Mean = 0.79375
- Standard deviation = 0.0768012857965282
- Max = 0.9
- 75% = 0.8625
- Median = 0.775
- 25% = 0.7375
- Min = 0.7

#### facing_probas
- Mean = [0.00256944 0.19611111 0.90236111 0.95979167 0.73548611]
- Standard deviation = [0.00259001 0.0507741  0.04403084 0.02625689 0.07686189]
- Max = [0.00722222 0.24277778 0.96555556 0.99277778 0.82444444]
- 75% = [0.00472222 0.2325     0.94513889 0.99194444 0.79472222]
- Median = [0.00111111 0.21888889 0.88916667 0.94972222 0.76      ]
- 25% = [8.33333333e-04 1.79305556e-01 8.64583333e-01 9.37777778e-01
 6.69166667e-01]
- Min = [0.         0.08888889 0.85388889 0.92944444 0.59944444]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 79.625 | 0.375 |
| Actual Positive | 4.125 | 15.875 |

### robot-5
#### accuracy
- Mean = 0.9962500000000001
- Standard deviation = 0.0048412291827592754
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 0.99
- Min = 0.99

#### f1
- Mean = 0.9903846153846154
- Standard deviation = 0.012413408160921218
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 0.9743589743589743
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
- Mean = 0.98125
- Standard deviation = 0.024206145913796374
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 0.95
- Min = 0.95

#### facing_probas
- Mean = [0.00208333 0.00256944 0.0925     0.90909722 0.91784722]
- Standard deviation = [0.00120281 0.00192325 0.02984787 0.04267207 0.02554414]
- Max = [0.00444444 0.00555556 0.13555556 0.96666667 0.96388889]
- 75% = [0.00236111 0.00375    0.11791667 0.95833333 0.93263889]
- Median = [0.00222222 0.0025     0.09611111 0.89277778 0.91861111]
- 25% = [0.00152778 0.00097222 0.06236111 0.87319444 0.89819444]
- Min = [0.         0.         0.05222222 0.85888889 0.87722222]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 80.0 | 0.0 |
| Actual Positive | 0.375 | 19.625 |

### robot-6
#### accuracy
- Mean = 0.935
- Standard deviation = 0.023452078799117114
- Max = 0.97
- 75% = 0.9524999999999999
- Median = 0.935
- 25% = 0.91
- Min = 0.91

#### f1
- Mean = 0.9662566794806917
- Standard deviation = 0.012507706530618385
- Max = 0.9847715736040609
- 75% = 0.9756671899529042
- Median = 0.9663461538461539
- 25% = 0.9528795811518325
- Min = 0.9528795811518325

#### precision
- Mean = 1.0
- Standard deviation = 0.0
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 1.0
- Min = 1.0

#### recall
- Mean = 0.935
- Standard deviation = 0.023452078799117114
- Max = 0.97
- 75% = 0.9524999999999999
- Median = 0.935
- 25% = 0.91
- Min = 0.91

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
| Actual Positive | 6.5 | 93.5 |

