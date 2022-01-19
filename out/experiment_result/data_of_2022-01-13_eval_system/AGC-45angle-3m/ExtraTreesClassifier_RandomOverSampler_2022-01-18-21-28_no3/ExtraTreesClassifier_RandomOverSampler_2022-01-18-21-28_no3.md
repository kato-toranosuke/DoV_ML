# ExtraTreesClassifier_RandomOverSampler_2022-01-18-21-28_no3
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
- resampler = RandomOverSampler
- estimator = ExtraTreesClassifier

### Arguments for hyperparameter search
- resampler = RandomOverSampler
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
	- shrinkage = None
	- n_features_in_ = 36
	- sampling_strategy_ = OrderedDict([(0, 3)])
	- shrinkage_ = None
	- sample_indices_ = [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23
 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47
 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71
 72 73 74 61 29 13]

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
- gp_max_val_mean = 0.21790380983072563
- gp_max_val_max = 0.15713467714890902
- gp_auc_min = 0.15289676530824414
- gp_auc_mean = 0.13801290419892592
- gp_auc_max = 0.0907221492992336
- diff_auc = 0.04860874037767491
- gp_max_val_min = 0.04454641738189647
- diff_std = 0.03500326971273706
- coe1[1] = 0.016752195037820772
- tdoa_mean = 0.015141113653699453
- high_power = 0.014173183277255672
- coe3[3] = 0.013192630848333742
- gp_max_val_std = 0.009907717571049371
- coe3[2] = 0.008816550727706391
- gp_max_val_range = 0.005705255553548855
- gp_max_ix_std = 0.005672923567660406
- gp_auc_std = 0.004708896134140659
- tdoa_std = 0.0045032367013791205
- tdoa_max = 0.004485645933014355
- srmr = 0.004214075010535188
- gp_max_ix_range = 0.0031605562579013905
- low_power = 0.0028318584070796474
- coe1[0] = 0.0009700476514635807
- gp_auc_range = 0.0009353804090646194
- hlbr = 0.0
- coe3[0] = 0.0
- coe3[1] = 0.0
- ratio_max_to_10ms_ave_peaks = 0.0
- ratio_max_to_9th_ave_peaks = 0.0
- ac_std = 0.0
- ac_auc = 0.0
- gp_max_ix_min = 0.0
- gp_max_ix_max = 0.0
- gp_max_ix_mean = 0.0
- tdoa_range = 0.0
- tdoa_min = 0.0

## Evaluation
cv = 8
### robot-1
#### accuracy
- Mean = 0.95875
- Standard deviation = 0.015360257159305623
- Max = 0.98
- 75% = 0.97
- Median = 0.96
- 25% = 0.955
- Min = 0.93

#### f1
- Mean = 0.9064571167525473
- Standard deviation = 0.03107357894043144
- Max = 0.9523809523809523
- 75% = 0.9302325581395349
- Median = 0.9090909090909091
- 25% = 0.8923913043478261
- Min = 0.851063829787234

#### precision
- Mean = 0.8406074400639618
- Standard deviation = 0.05597809780575162
- Max = 0.9090909090909091
- 75% = 0.8771739130434782
- Median = 0.8514492753623188
- 25% = 0.8173076923076923
- Min = 0.7407407407407407

#### recall
- Mean = 0.9875
- Standard deviation = 0.03307189138830738
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 1.0
- Min = 0.9

#### facing_probas
- Mean = [0.99296875 0.93661458 0.10973958 0.01432292 0.00833333]
- Standard deviation = [0.00637186 0.02978397 0.06510173 0.01599416 0.00587781]
- Max = [1.         0.97291667 0.27       0.045      0.0175    ]
- 75% = [0.9953125 0.959375  0.10875   0.0184375 0.01125  ]
- Median = [0.995      0.94020833 0.08958333 0.00875    0.00875   ]
- 25% = [0.99375    0.92322917 0.0765625  0.0025     0.005     ]
- Min = [0.9775     0.87833333 0.055      0.         0.        ]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 76.125 | 3.875 |
| Actual Positive | 0.25 | 19.75 |

### robot-2
#### accuracy
- Mean = 0.9575
- Standard deviation = 0.015612494995995985
- Max = 0.98
- 75% = 0.97
- Median = 0.96
- 25% = 0.9475
- Min = 0.93

#### f1
- Mean = 0.8807733885133266
- Standard deviation = 0.049325041174540805
- Max = 0.9473684210526316
- 75% = 0.9189189189189189
- Median = 0.888888888888889
- 25% = 0.8597285067873304
- Min = 0.787878787878788

#### precision
- Mean = 0.986842105263158
- Standard deviation = 0.03481251725084988
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 1.0
- Min = 0.8947368421052632

#### recall
- Mean = 0.8
- Standard deviation = 0.07905694150420949
- Max = 0.9
- 75% = 0.85
- Median = 0.825
- 25% = 0.775
- Min = 0.65

#### facing_probas
- Mean = [0.92869792 0.9690625  0.67458333 0.02994792 0.00578125]
- Standard deviation = [0.03363757 0.01567734 0.07028279 0.02037883 0.0078794 ]
- Max = [0.97541667 0.99       0.79625    0.07625    0.02      ]
- 75% = [0.95677083 0.979375   0.71041667 0.03625    0.0115625 ]
- Median = [0.93229167 0.96875    0.68145833 0.02416667 0.        ]
- 25% = [0.9071875  0.96166667 0.63145833 0.02       0.        ]
- Min = [0.87291667 0.93833333 0.56083333 0.00666667 0.        ]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 79.75 | 0.25 |
| Actual Positive | 4.0 | 16.0 |

### robot-3
#### accuracy
- Mean = 0.985
- Standard deviation = 0.011180339887498959
- Max = 1.0
- 75% = 0.9924999999999999
- Median = 0.985
- 25% = 0.9775
- Min = 0.97

#### f1
- Mean = 0.9601615785826312
- Standard deviation = 0.030221216568754244
- Max = 1.0
- 75% = 0.9807692307692307
- Median = 0.9608636977058029
- 25% = 0.9402560455192035
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
- Mean = 0.9249999999999999
- Standard deviation = 0.05590169943749474
- Max = 1.0
- 75% = 0.9624999999999999
- Median = 0.925
- 25% = 0.8875
- Min = 0.85

#### facing_probas
- Mean = [0.12744792 0.98744792 0.99604167 0.97130208 0.03723958]
- Standard deviation = [0.03308333 0.02193784 0.00341056 0.01848474 0.01947325]
- Max = [0.18416667 1.         1.         0.99625    0.0825    ]
- 75% = [0.1478125  1.         0.99875    0.9890625  0.03614583]
- Median = [0.11645833 0.995      0.995625   0.9725     0.0275    ]
- 25% = [0.10583333 0.9896875  0.995      0.9540625  0.02666667]
- Min = [0.08291667 0.93083333 0.98875    0.94416667 0.0225    ]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 80.0 | 0.0 |
| Actual Positive | 1.5 | 18.5 |

### robot-4
#### accuracy
- Mean = 0.9337500000000001
- Standard deviation = 0.011110243021644447
- Max = 0.95
- 75% = 0.9424999999999999
- Median = 0.93
- 25% = 0.9275
- Min = 0.92

#### f1
- Mean = 0.8290007569183689
- Standard deviation = 0.040359001824753174
- Max = 0.8837209302325583
- 75% = 0.8608058608058609
- Median = 0.8292682926829269
- 25% = 0.8081081081081081
- Min = 0.7499999999999999

#### precision
- Mean = 0.8550507721291137
- Standard deviation = 0.0639383392271954
- Max = 1.0
- 75% = 0.8854489164086687
- Median = 0.8221343873517787
- 25% = 0.8095238095238095
- Min = 0.8

#### recall
- Mean = 0.81875
- Standard deviation = 0.0998044963916957
- Max = 0.95
- 75% = 0.8625
- Median = 0.85
- 25% = 0.7875000000000001
- Min = 0.6

#### facing_probas
- Mean = [0.01046875 0.13239583 0.97953125 0.99432292 0.78229167]
- Standard deviation = [0.0198622  0.03374019 0.01689741 0.00589233 0.07616685]
- Max = [0.06125    0.20416667 1.         1.         0.86625   ]
- 75% = [0.009375   0.14635417 0.990625   1.         0.82145833]
- Median = [0.         0.12354167 0.98375    0.995625   0.80104167]
- 25% = [0.        0.119375  0.9715625 0.99      0.760625 ]
- Min = [0.         0.0775     0.945      0.98333333 0.605     ]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 77.0 | 3.0 |
| Actual Positive | 3.625 | 16.375 |

### robot-5
#### accuracy
- Mean = 0.97
- Standard deviation = 0.014142135623730963
- Max = 1.0
- 75% = 0.98
- Median = 0.96
- 25% = 0.96
- Min = 0.96

#### f1
- Mean = 0.9173976608187135
- Standard deviation = 0.03981737962396584
- Max = 1.0
- 75% = 0.9473684210526316
- Median = 0.888888888888889
- 25% = 0.888888888888889
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
- Mean = 0.8500000000000001
- Standard deviation = 0.07071067811865474
- Max = 1.0
- 75% = 0.9
- Median = 0.8
- 25% = 0.8
- Min = 0.8

#### facing_probas
- Mean = [1.87500000e-03 6.25000000e-04 2.10312500e-01 9.94947917e-01
 9.92604167e-01]
- Standard deviation = [0.00347985 0.00165359 0.05449131 0.00473443 0.00658066]
- Max = [0.01   0.005  0.2775 1.     1.    ]
- 75% = [0.00125  0.       0.253125 1.       1.      ]
- Median = [0.         0.         0.22666667 0.99541667 0.99041667]
- 25% = [0.         0.         0.15666667 0.9909375  0.99      ]
- Min = [0.         0.         0.13166667 0.9875     0.98      ]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 80.0 | 0.0 |
| Actual Positive | 3.0 | 17.0 |

### robot-6
#### accuracy
- Mean = 0.87625
- Standard deviation = 0.02057759704144293
- Max = 0.9
- 75% = 0.885
- Median = 0.88
- 25% = 0.87
- Min = 0.83

#### f1
- Mean = 0.9339142340480835
- Standard deviation = 0.011830400150826785
- Max = 0.9473684210526316
- 75% = 0.9389697648376261
- Median = 0.9361702127659575
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
- Mean = 0.87625
- Standard deviation = 0.02057759704144293
- Max = 0.9
- 75% = 0.885
- Median = 0.88
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
| Actual Positive | 12.375 | 87.625 |

