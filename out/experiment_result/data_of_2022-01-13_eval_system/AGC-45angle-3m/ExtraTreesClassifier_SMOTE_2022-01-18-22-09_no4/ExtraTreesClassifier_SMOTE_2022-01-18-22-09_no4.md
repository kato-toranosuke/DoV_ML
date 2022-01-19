# ExtraTreesClassifier_SMOTE_2022-01-18-22-09_no4
## Constants
- CSV_PATH = ../out/csv/experiment
- OUTPUT_PATH = ../out/experiment_result/data_of_2022-01-13_eval_system/AGC-45angle-3m
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
	- sampling_strategy_ = OrderedDict([(0, 3)])
	- nn_k_ = NearestNeighbors(n_neighbors=6)

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
- gp_max_val_mean = 0.2475437055814246
- gp_max_val_max = 0.14139738836380497
- gp_auc_max = 0.11265088347485423
- gp_auc_mean = 0.10417087380983932
- gp_auc_min = 0.0931477069547059
- srmr = 0.05852063934116357
- high_power = 0.0387288116903825
- diff_auc = 0.03705178495941576
- gp_max_val_min = 0.023472222222222235
- coe1[1] = 0.02270013028867835
- hlbr = 0.021971830985915493
- gp_max_val_std = 0.018722800613198122
- ratio_max_to_10ms_ave_peaks = 0.012097674834743805
- gp_auc_range = 0.010400795359409501
- low_power = 0.00950482181063388
- diff_std = 0.00916666666666666
- tdoa_std = 0.009027777777777779
- tdoa_mean = 0.009011742526922793
- gp_max_ix_mean = 0.004968465327393084
- gp_max_ix_range = 0.0035398230088495566
- tdoa_min = 0.0031068140824238393
- tdoa_max = 0.0025678533071897955
- gp_max_ix_max = 0.002473947621006448
- coe3[3] = 0.0021634615384615386
- coe1[0] = 0.0009985207100591694
- ac_std = 0.0008928571428571437
- coe3[0] = 0.0
- coe3[1] = 0.0
- coe3[2] = 0.0
- ratio_max_to_9th_ave_peaks = 0.0
- ac_auc = 0.0
- gp_max_val_range = 0.0
- gp_max_ix_std = 0.0
- gp_max_ix_min = 0.0
- gp_auc_std = 0.0
- tdoa_range = 0.0

## Evaluation
cv = 8
### robot-1
#### accuracy
- Mean = 0.96125
- Standard deviation = 0.020271593425283552
- Max = 0.98
- 75% = 0.97
- Median = 0.97
- 25% = 0.96
- Min = 0.91

#### f1
- Mean = 0.9125829873338179
- Standard deviation = 0.03859763179207478
- Max = 0.9523809523809523
- 75% = 0.9302325581395349
- Median = 0.926654740608229
- 25% = 0.9090909090909091
- Min = 0.8163265306122449

#### precision
- Mean = 0.8526846026747392
- Standard deviation = 0.07100096892579691
- Max = 0.9473684210526315
- 75% = 0.8794466403162056
- Median = 0.8695652173913043
- 25% = 0.8333333333333334
- Min = 0.6896551724137931

#### recall
- Mean = 0.9875
- Standard deviation = 0.03307189138830738
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 1.0
- Min = 0.9

#### facing_probas
- Mean = [0.99145833 0.94119792 0.13932292 0.00598958 0.01369792]
- Standard deviation = [0.00712914 0.03652045 0.05057823 0.00337177 0.01310587]
- Max = [1.         0.9925     0.22583333 0.01       0.04458333]
- 75% = [0.995625   0.96104167 0.16291667 0.00833333 0.01625   ]
- Median = [0.995      0.94916667 0.12895833 0.0075     0.01      ]
- 25% = [0.98625    0.9290625  0.09979167 0.0040625  0.00625   ]
- Min = [0.9775     0.86166667 0.07833333 0.         0.        ]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 76.375 | 3.625 |
| Actual Positive | 0.25 | 19.75 |

### robot-2
#### accuracy
- Mean = 0.96125
- Standard deviation = 0.020271593425283552
- Max = 0.98
- 75% = 0.97
- Median = 0.97
- 25% = 0.96
- Min = 0.91

#### f1
- Mean = 0.889801205404336
- Standard deviation = 0.07042267783122715
- Max = 0.9473684210526316
- 75% = 0.9208965062623599
- Median = 0.9189189189189189
- 25% = 0.888888888888889
- Min = 0.7096774193548387

#### precision
- Mean = 0.9880952380952381
- Standard deviation = 0.031497039417435604
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 1.0
- Min = 0.9047619047619048

#### recall
- Mean = 0.8187500000000001
- Standard deviation = 0.11162856937182343
- Max = 0.95
- 75% = 0.8625
- Median = 0.85
- 25% = 0.8
- Min = 0.55

#### facing_probas
- Mean = [0.93515625 0.97380208 0.73161458 0.01854167 0.00114583]
- Standard deviation = [0.03195112 0.01760317 0.06323095 0.01172234 0.0017148 ]
- Max = [0.995      1.         0.80416667 0.04583333 0.005     ]
- 75% = [0.95447917 0.98708333 0.79052083 0.02010417 0.001875  ]
- Median = [0.9375     0.974375   0.728125   0.01458333 0.        ]
- 25% = [0.90697917 0.96197917 0.70854167 0.0109375  0.        ]
- Min = [0.88875    0.94875    0.59958333 0.0075     0.        ]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 79.75 | 0.25 |
| Actual Positive | 3.625 | 16.375 |

### robot-3
#### accuracy
- Mean = 0.9837499999999999
- Standard deviation = 0.008569568250501312
- Max = 1.0
- 75% = 0.99
- Median = 0.98
- 25% = 0.98
- Min = 0.97

#### f1
- Mean = 0.9571388189809242
- Standard deviation = 0.023110473286739423
- Max = 1.0
- 75% = 0.9743589743589743
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
- Mean = 0.91875
- Standard deviation = 0.04284784125250652
- Max = 1.0
- 75% = 0.95
- Median = 0.9
- 25% = 0.9
- Min = 0.85

#### facing_probas
- Mean = [0.15526042 0.99354167 0.99234375 0.96510417 0.06989583]
- Standard deviation = [0.02009627 0.0071261  0.00580326 0.02043552 0.04977674]
- Max = [0.17791667 1.         1.         1.         0.17375   ]
- 75% = [0.169375   0.9990625  0.99625    0.97802083 0.08677083]
- Median = [0.16333333 0.99583333 0.993125   0.96354167 0.07208333]
- 25% = [0.1375     0.9909375  0.98729167 0.95125    0.02979167]
- Min = [0.12       0.9775     0.98333333 0.93583333 0.005     ]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 80.0 | 0.0 |
| Actual Positive | 1.625 | 18.375 |

### robot-4
#### accuracy
- Mean = 0.94875
- Standard deviation = 0.02087911636061256
- Max = 0.99
- 75% = 0.96
- Median = 0.95
- 25% = 0.93
- Min = 0.92

#### f1
- Mean = 0.8664559493827786
- Standard deviation = 0.05070094372669931
- Max = 0.9743589743589743
- 75% = 0.888888888888889
- Median = 0.8648648648648648
- 25% = 0.8270794246404003
- Min = 0.8000000000000002

#### precision
- Mean = 0.9167477517322719
- Standard deviation = 0.08115174640189637
- Max = 1.0
- 75% = 1.0
- Median = 0.9411764705882353
- 25% = 0.8339598997493733
- Min = 0.8

#### recall
- Mean = 0.825
- Standard deviation = 0.04999999999999997
- Max = 0.95
- 75% = 0.8125
- Median = 0.8
- 25% = 0.8
- Min = 0.8

#### facing_probas
- Mean = [0.001875   0.14489583 0.97411458 0.99473958 0.77229167]
- Standard deviation = [0.00233854 0.04107219 0.01184103 0.00581447 0.05424394]
- Max = [0.00625    0.20708333 1.         1.         0.83708333]
- 75% = [0.003125   0.16520833 0.9790625  1.         0.79625   ]
- Median = [6.25000000e-04 1.55000000e-01 9.70416667e-01 9.97500000e-01
 7.72291667e-01]
- 25% = [0.         0.12552083 0.96739583 0.98916667 0.765     ]
- Min = [0.         0.06583333 0.95875    0.98625    0.64916667]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 78.375 | 1.625 |
| Actual Positive | 3.5 | 16.5 |

### robot-5
#### accuracy
- Mean = 0.98375
- Standard deviation = 0.016535945694153707
- Max = 1.0
- 75% = 1.0
- Median = 0.99
- 25% = 0.9675
- Min = 0.96

#### f1
- Mean = 0.9556768306768306
- Standard deviation = 0.045913066515716625
- Max = 1.0
- 75% = 1.0
- Median = 0.9743589743589743
- 25% = 0.9114114114114114
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
- Mean = 0.91875
- Standard deviation = 0.08267972847076845
- Max = 1.0
- 75% = 1.0
- Median = 0.95
- 25% = 0.8375
- Min = 0.8

#### facing_probas
- Mean = [8.33333333e-04 9.37500000e-04 1.49166667e-01 9.90885417e-01
 9.92031250e-01]
- Standard deviation = [0.00166667 0.00173993 0.02741147 0.00843284 0.00842511]
- Max = [0.005      0.005      0.20416667 1.         1.        ]
- 75% = [4.16666667e-04 6.25000000e-04 1.62083333e-01 1.00000000e+00
 9.97812500e-01]
- Median = [0.         0.         0.14625    0.99125    0.99708333]
- 25% = [0.         0.         0.13104167 0.98427083 0.985625  ]
- Min = [0.         0.         0.10916667 0.9775     0.975     ]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 80.0 | 0.0 |
| Actual Positive | 1.625 | 18.375 |

### robot-6
#### accuracy
- Mean = 0.89375
- Standard deviation = 0.03314268395890713
- Max = 0.96
- 75% = 0.905
- Median = 0.89
- 25% = 0.8775
- Min = 0.84

#### f1
- Mean = 0.9435733061459787
- Standard deviation = 0.018351327691918037
- Max = 0.9795918367346939
- 75% = 0.950109649122807
- Median = 0.9417989417989417
- 25% = 0.9347479804300831
- Min = 0.9130434782608696

#### precision
- Mean = 1.0
- Standard deviation = 0.0
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 1.0
- Min = 1.0

#### recall
- Mean = 0.89375
- Standard deviation = 0.03314268395890713
- Max = 0.96
- 75% = 0.905
- Median = 0.89
- 25% = 0.8775
- Min = 0.84

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
| Actual Positive | 10.625 | 89.375 |

