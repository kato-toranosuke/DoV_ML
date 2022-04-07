# ExtraTreesClassifier_SMOTETomek_2022-01-20-09-52_no6
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
	- max_features = sqrt
	- max_leaf_nodes = None
	- min_impurity_decrease = 0.0
	- ccp_alpha = 0.0
	- n_features_in_ = 36
	- n_outputs_ = 1
	- classes_ = [0 1]
	- n_classes_ = 2
	- base_estimator_ = ExtraTreeClassifier()

#### Importance of features
- gp_auc_max = 0.12751984866308516
- gp_max_val_max = 0.0952778711753962
- gp_max_val_mean = 0.09116302344567202
- gp_max_val_min = 0.08744438934465829
- gp_auc_min = 0.07838798602191459
- gp_auc_mean = 0.0724474626046831
- high_power = 0.06454002540250418
- coe1[0] = 0.048878307865538796
- diff_auc = 0.04649667725278435
- coe3[3] = 0.040050254552830525
- srmr = 0.03720351901444339
- diff_std = 0.0363736360949916
- coe1[1] = 0.02974661790733219
- gp_max_val_std = 0.022266606149089308
- low_power = 0.01757477844939145
- tdoa_range = 0.012910914207938048
- gp_max_ix_max = 0.011526251526251526
- tdoa_max = 0.010189036952293977
- hlbr = 0.009550023319020278
- coe3[2] = 0.007215124879103374
- gp_max_ix_range = 0.006809964726631394
- gp_max_ix_std = 0.005967808603972184
- gp_max_val_range = 0.004818594104308391
- gp_auc_std = 0.0047902494331065765
- ac_std = 0.0047461577223481995
- ac_auc = 0.0044444444444444444
- tdoa_mean = 0.0042658730158730155
- tdoa_min = 0.004040205825920111
- ratio_max_to_9th_ave_peaks = 0.00371787603930461
- tdoa_std = 0.003036414565826331
- gp_auc_range = 0.0025184240362811803
- gp_max_ix_mean = 0.0015873015873015873
- gp_max_ix_min = 0.0012698412698412696
- ratio_max_to_10ms_ave_peaks = 0.0012244897959183673
- coe3[0] = 0.0
- coe3[1] = 0.0

## Evaluation
cv = 8
### robot-1
#### accuracy
- Mean = 0.98
- Standard deviation = 0.008660254037844393
- Max = 1.0
- 75% = 0.98
- Median = 0.98
- 25% = 0.9775
- Min = 0.97

#### f1
- Mean = 0.9523708235421224
- Standard deviation = 0.020648888597870403
- Max = 1.0
- 75% = 0.9523809523809523
- Median = 0.9523809523809523
- 25% = 0.946843853820598
- Min = 0.9268292682926829

#### precision
- Mean = 0.9149727084509692
- Standard deviation = 0.03458453209715664
- Max = 1.0
- 75% = 0.9090909090909091
- Median = 0.9090909090909091
- 25% = 0.9080086580086579
- Min = 0.8695652173913043

#### recall
- Mean = 0.99375
- Standard deviation = 0.016535945694153707
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 1.0
- Min = 0.95

#### facing_probas
- Mean = [0.94875    0.72041667 0.04770833 0.003125   0.00166667]
- Standard deviation = [0.02226342 0.05729886 0.03179729 0.00428478 0.00220479]
- Max = [0.98166667 0.78666667 0.11       0.01166667 0.005     ]
- 75% = [0.96416667 0.78041667 0.06916667 0.00666667 0.00375   ]
- Median = [0.9475     0.72166667 0.04166667 0.         0.        ]
- 25% = [0.93458333 0.67416667 0.0225     0.         0.        ]
- Min = [0.91166667 0.63833333 0.00833333 0.         0.        ]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 78.125 | 1.875 |
| Actual Positive | 0.125 | 19.875 |

### robot-2
#### accuracy
- Mean = 0.9762500000000001
- Standard deviation = 0.011110243021644496
- Max = 1.0
- 75% = 0.98
- Median = 0.975
- 25% = 0.97
- Min = 0.96

#### f1
- Mean = 0.9359688636004426
- Standard deviation = 0.030778365004304545
- Max = 1.0
- 75% = 0.9473684210526316
- Median = 0.9331436699857752
- 25% = 0.9189189189189189
- Min = 0.888888888888889

#### precision
- Mean = 1.0
- Standard deviation = 0.0
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 1.0
- Min = 1.0

#### recall
- Mean = 0.88125
- Standard deviation = 0.05555121510822243
- Max = 1.0
- 75% = 0.9
- Median = 0.875
- 25% = 0.85
- Min = 0.8

#### facing_probas
- Mean = [9.21041667e-01 9.30625000e-01 8.17708333e-01 4.12500000e-02
 2.08333333e-04]
- Standard deviation = [0.02968512 0.0245365  0.05394144 0.04256327 0.0005512 ]
- Max = [0.97       0.98833333 0.92333333 0.13666667 0.00166667]
- 75% = [0.9325     0.935      0.84333333 0.05083333 0.        ]
- Median = [0.91916667 0.92333333 0.82       0.03       0.        ]
- 25% = [0.89375    0.91375    0.7675     0.00666667 0.        ]
- Min = [0.88833333 0.90833333 0.74833333 0.00333333 0.        ]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 80.0 | 0.0 |
| Actual Positive | 2.375 | 17.625 |

### robot-3
#### accuracy
- Mean = 0.9724999999999999
- Standard deviation = 0.013919410907075068
- Max = 1.0
- 75% = 0.98
- Median = 0.97
- 25% = 0.9675
- Min = 0.95

#### f1
- Mean = 0.9246906681117207
- Standard deviation = 0.039756241420053365
- Max = 1.0
- 75% = 0.9473684210526316
- Median = 0.9189189189189189
- 25% = 0.9114114114114114
- Min = 0.8571428571428571

#### precision
- Mean = 1.0
- Standard deviation = 0.0
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 1.0
- Min = 1.0

#### recall
- Mean = 0.8625
- Standard deviation = 0.06959705453537526
- Max = 1.0
- 75% = 0.9
- Median = 0.85
- 25% = 0.8375
- Min = 0.75

#### facing_probas
- Mean = [0.13020833 0.859375   0.92625    0.77       0.035625  ]
- Standard deviation = [0.06551313 0.02301777 0.02829348 0.07583791 0.03431813]
- Max = [0.28166667 0.905      0.985      0.905      0.10166667]
- 75% = [0.14291667 0.87125    0.93875    0.81416667 0.05833333]
- Median = [0.12416667 0.85       0.92333333 0.75916667 0.01916667]
- 25% = [0.09416667 0.84166667 0.905      0.72583333 0.00666667]
- Min = [0.04333333 0.835      0.88666667 0.64666667 0.005     ]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 80.0 | 0.0 |
| Actual Positive | 2.75 | 17.25 |

### robot-4
#### accuracy
- Mean = 0.94
- Standard deviation = 0.027386127875258286
- Max = 0.97
- 75% = 0.96
- Median = 0.95
- 25% = 0.9275
- Min = 0.88

#### f1
- Mean = 0.8221421302690652
- Standard deviation = 0.09744304552799238
- Max = 0.9189189189189189
- 75% = 0.8903508771929824
- Median = 0.861003861003861
- 25% = 0.7820855614973263
- Min = 0.6

#### precision
- Mean = 0.9642740429505136
- Standard deviation = 0.03781189648287904
- Max = 1.0
- 75% = 1.0
- Median = 0.9722222222222222
- 25% = 0.9380252100840336
- Min = 0.9

#### recall
- Mean = 0.7250000000000001
- Standard deviation = 0.1274754878398196
- Max = 0.85
- 75% = 0.8125
- Median = 0.775
- 25% = 0.65
- Min = 0.45

#### facing_probas
- Mean = [0.         0.19541667 0.866875   0.93020833 0.685     ]
- Standard deviation = [0.         0.06034478 0.04669224 0.02418731 0.06232197]
- Max = [0.         0.29666667 0.96666667 0.97666667 0.82166667]
- 75% = [0.         0.22875    0.87791667 0.94083333 0.71125   ]
- Median = [0.         0.17083333 0.85166667 0.93166667 0.65833333]
- 25% = [0.         0.14625    0.84291667 0.91625    0.64541667]
- Min = [0.         0.13833333 0.81166667 0.89666667 0.625     ]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 79.5 | 0.5 |
| Actual Positive | 5.5 | 14.5 |

### robot-5
#### accuracy
- Mean = 0.9925
- Standard deviation = 0.006614378277661482
- Max = 1.0
- 75% = 1.0
- Median = 0.99
- 25% = 0.99
- Min = 0.98

#### f1
- Mean = 0.9806005398110661
- Standard deviation = 0.01728156330172334
- Max = 1.0
- 75% = 1.0
- Median = 0.9743589743589743
- 25% = 0.9743589743589743
- Min = 0.9473684210526316

#### precision
- Mean = 1.0
- Standard deviation = 0.0
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 1.0
- Min = 1.0

#### recall
- Mean = 0.9625
- Standard deviation = 0.033071891388307385
- Max = 1.0
- 75% = 1.0
- Median = 0.95
- 25% = 0.95
- Min = 0.9

#### facing_probas
- Mean = [0.00625    0.00395833 0.08916667 0.874375   0.89083333]
- Standard deviation = [0.00531964 0.00526634 0.06803288 0.0469259  0.04154984]
- Max = [0.01666667 0.015      0.26333333 0.96166667 0.97      ]
- 75% = [0.00791667 0.005      0.09041667 0.89416667 0.91416667]
- Median = [0.00583333 0.00166667 0.06083333 0.88166667 0.88916667]
- 25% = [0.0025     0.         0.05541667 0.84208333 0.85375   ]
- Min = [0.         0.         0.03833333 0.80833333 0.84      ]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 80.0 | 0.0 |
| Actual Positive | 0.75 | 19.25 |

### robot-6
#### accuracy
- Mean = 0.885
- Standard deviation = 0.028284271247461926
- Max = 0.93
- 75% = 0.9025000000000001
- Median = 0.885
- 25% = 0.87
- Min = 0.83

#### f1
- Mean = 0.9387517648373851
- Standard deviation = 0.01601610975867528
- Max = 0.9637305699481865
- 75% = 0.9487462110774318
- Median = 0.9389845772824497
- 25% = 0.9304812834224598
- Min = 0.9071038251366119

#### precision
- Mean = 1.0
- Standard deviation = 0.0
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 1.0
- Min = 1.0

#### recall
- Mean = 0.885
- Standard deviation = 0.028284271247461926
- Max = 0.93
- 75% = 0.9025000000000001
- Median = 0.885
- 25% = 0.87
- Min = 0.83

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
| Actual Positive | 11.5 | 88.5 |

