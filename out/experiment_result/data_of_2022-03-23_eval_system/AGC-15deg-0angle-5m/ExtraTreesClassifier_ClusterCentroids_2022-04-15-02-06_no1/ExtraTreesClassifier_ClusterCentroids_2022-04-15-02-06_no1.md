# ExtraTreesClassifier_ClusterCentroids_2022-04-15-02-06_no1
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
- resampler = ClusterCentroids
- estimator = ExtraTreesClassifier

### Arguments for hyperparameter search
- resampler = ClusterCentroids
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
	- estimator = None
	- voting = auto
	- n_jobs = deprecated
	- n_features_in_ = 36
	- sampling_strategy_ = OrderedDict([(0, 15)])
	- estimator_ = KMeans(n_clusters=15, random_state=42)
	- voting_ = soft

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
- gp_auc_range = 0.14270156919901167
- gp_max_val_range = 0.10951678730626102
- gp_auc_max = 0.09494527257822004
- gp_max_val_max = 0.06769459445878437
- gp_max_ix_mean = 0.0434320987654321
- gp_max_ix_std = 0.04196676163342831
- gp_auc_std = 0.040649045909960345
- tdoa_std = 0.038465466632133294
- ac_auc = 0.03750264550264552
- ratio_max_to_10ms_ave_peaks = 0.03750264550264551
- tdoa_mean = 0.03094163860830528
- diff_auc = 0.027562914004942998
- gp_max_val_mean = 0.027321073987740665
- gp_auc_mean = 0.02393738977072311
- tdoa_max = 0.023684095860566454
- diff_std = 0.023400352733686073
- gp_max_ix_min = 0.022081531758002353
- coe3[3] = 0.0187970177970178
- srmr = 0.01737987502693385
- gp_max_val_min = 0.015516754850088183
- gp_max_ix_max = 0.015132922632922634
- hlbr = 0.013890923890923891
- gp_max_val_std = 0.013658810325476995
- tdoa_range = 0.012314814814814817
- ac_std = 0.011402580525387541
- gp_max_ix_range = 0.007500000000000002
- tdoa_min = 0.0074074074074074086
- high_power = 0.00738997821350763
- ratio_max_to_9th_ave_peaks = 0.007326599326599326
- coe3[2] = 0.006518518518518519
- low_power = 0.0059259259259259265
- gp_auc_min = 0.004309764309764311
- coe1[1] = 0.0022222222222222227
- coe1[0] = 0.0
- coe3[0] = 0.0
- coe3[1] = 0.0

## Evaluation
cv = 8
### robot-1
#### accuracy
- Mean = 0.7875000000000001
- Standard deviation = 0.05760859310901455
- Max = 0.84
- 75% = 0.825
- Median = 0.8
- 25% = 0.7825
- Min = 0.65

#### f1
- Mean = 0.332045032868986
- Standard deviation = 0.1423692866237771
- Max = 0.5
- 75% = 0.4725063938618926
- Median = 0.35416666666666663
- 25% = 0.2131782945736434
- Min = 0.09090909090909091

#### precision
- Mean = 0.5329570791527314
- Standard deviation = 0.22123018833816505
- Max = 1.0
- 75% = 0.5952380952380952
- Median = 0.5
- 25% = 0.4271978021978022
- Min = 0.17391304347826086

#### recall
- Mean = 0.28125
- Standard deviation = 0.15194057226429025
- Max = 0.55
- 75% = 0.4
- Median = 0.25
- 25% = 0.1875
- Min = 0.05

#### facing_probas
- Mean = [0.535625   0.55520833 0.43833333 0.44375    0.415625  ]
- Standard deviation = [0.09211609 0.16243896 0.112839   0.17945084 0.1954854 ]
- Max = [0.7        0.76166667 0.64       0.73833333 0.72833333]
- 75% = [0.57583333 0.6675     0.50875    0.54916667 0.55083333]
- Median = [0.5375     0.6275     0.43166667 0.44333333 0.43166667]
- 25% = [0.49416667 0.41708333 0.32416667 0.32583333 0.25208333]
- Min = [0.39       0.29333333 0.315      0.175      0.14833333]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 73.125 | 6.875 |
| Actual Positive | 14.375 | 5.625 |

### robot-2
#### accuracy
- Mean = 0.72875
- Standard deviation = 0.06954090522850562
- Max = 0.84
- 75% = 0.7575000000000001
- Median = 0.74
- 25% = 0.71
- Min = 0.6

#### f1
- Mean = 0.4364044758392749
- Standard deviation = 0.10654140065707125
- Max = 0.6521739130434783
- 75% = 0.4785148101793909
- Median = 0.43501611170784105
- 25% = 0.3624031007751938
- Min = 0.2857142857142857

#### precision
- Mean = 0.38333068870169273
- Standard deviation = 0.10142382484080513
- Max = 0.5769230769230769
- 75% = 0.42562724014336917
- Median = 0.39335887611749676
- 25% = 0.3233695652173913
- Min = 0.2413793103448276

#### recall
- Mean = 0.51875
- Standard deviation = 0.12732217992164602
- Max = 0.75
- 75% = 0.5750000000000001
- Median = 0.525
- 25% = 0.4
- Min = 0.35

#### facing_probas
- Mean = [0.57166667 0.86854167 0.83145833 0.62333333 0.5375    ]
- Standard deviation = [0.17243155 0.04013378 0.05388025 0.14128871 0.1327461 ]
- Max = [0.89833333 0.94333333 0.93666667 0.91333333 0.74333333]
- 75% = [0.655      0.90041667 0.85458333 0.67125    0.63958333]
- Median = [0.5075     0.85333333 0.81666667 0.59833333 0.55166667]
- 25% = [0.45       0.83708333 0.79333333 0.52       0.43      ]
- Min = [0.36666667 0.82166667 0.77       0.46166667 0.34166667]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 62.5 | 17.5 |
| Actual Positive | 9.625 | 10.375 |

### robot-3
#### accuracy
- Mean = 0.735
- Standard deviation = 0.05074445782546108
- Max = 0.82
- 75% = 0.76
- Median = 0.735
- 25% = 0.7075
- Min = 0.66

#### f1
- Mean = 0.3655372614161944
- Standard deviation = 0.08568376165973608
- Max = 0.5116279069767442
- 75% = 0.41228991596638653
- Median = 0.35448717948717945
- 25% = 0.3057692307692308
- Min = 0.23255813953488372

#### precision
- Mean = 0.36335585340161997
- Standard deviation = 0.10465688130818494
- Max = 0.5714285714285714
- 75% = 0.39588100686498856
- Median = 0.33289473684210524
- 25% = 0.3041666666666667
- Min = 0.21739130434782608

#### recall
- Mean = 0.38125
- Standard deviation = 0.10588171466310888
- Max = 0.55
- 75% = 0.4375
- Median = 0.35
- 25% = 0.3
- Min = 0.25

#### facing_probas
- Mean = [0.550625   0.70083333 0.74375    0.58625    0.58395833]
- Standard deviation = [0.09036937 0.04995832 0.07126705 0.12085847 0.15888924]
- Max = [0.68666667 0.77       0.82166667 0.74833333 0.73833333]
- 75% = [0.60583333 0.73125    0.785      0.67541667 0.6975    ]
- Median = [0.54666667 0.70166667 0.76833333 0.60416667 0.64916667]
- 25% = [0.46333333 0.67708333 0.73041667 0.50708333 0.53666667]
- Min = [0.44166667 0.62       0.59       0.40333333 0.28833333]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 65.875 | 14.125 |
| Actual Positive | 12.375 | 7.625 |

### robot-4
#### accuracy
- Mean = 0.745
- Standard deviation = 0.048476798574163316
- Max = 0.81
- 75% = 0.7925
- Median = 0.74
- 25% = 0.7124999999999999
- Min = 0.67

#### f1
- Mean = 0.30155121749198405
- Standard deviation = 0.08329948945748718
- Max = 0.4324324324324324
- 75% = 0.36456400742115025
- Median = 0.3148148148148148
- 25% = 0.2305986696230599
- Min = 0.18181818181818185

#### precision
- Mean = 0.3643290870724948
- Standard deviation = 0.1263594210413769
- Max = 0.5714285714285714
- 75% = 0.4779411764705882
- Median = 0.3218390804597701
- 25% = 0.2884615384615385
- Min = 0.19047619047619047

#### recall
- Mean = 0.28125
- Standard deviation = 0.10879309490955758
- Max = 0.45
- 75% = 0.4
- Median = 0.225
- 25% = 0.2
- Min = 0.15

#### facing_probas
- Mean = [0.553125   0.65583333 0.74666667 0.74541667 0.653125  ]
- Standard deviation = [0.08431273 0.06091889 0.07103403 0.09113387 0.05968923]
- Max = [0.70333333 0.73       0.83833333 0.87833333 0.76166667]
- 75% = [0.6325     0.705      0.81083333 0.81708333 0.67833333]
- Median = [0.505      0.66333333 0.7475     0.7375     0.65916667]
- 25% = [0.48916667 0.61708333 0.69083333 0.68791667 0.6075    ]
- Min = [0.465      0.53833333 0.64333333 0.6        0.565     ]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 68.875 | 11.125 |
| Actual Positive | 14.375 | 5.625 |

### robot-5
#### accuracy
- Mean = 0.7537499999999999
- Standard deviation = 0.03533323506275646
- Max = 0.81
- 75% = 0.78
- Median = 0.755
- 25% = 0.72
- Min = 0.71

#### f1
- Mean = 0.30641425350433815
- Standard deviation = 0.1047693174613484
- Max = 0.425531914893617
- 75% = 0.41776315789473684
- Median = 0.31904069767441856
- 25% = 0.2101449275362319
- Min = 0.15384615384615383

#### precision
- Mean = 0.3928715205889119
- Standard deviation = 0.11819798446132226
- Max = 0.6666666666666666
- 75% = 0.4236111111111111
- Median = 0.3637566137566137
- 25% = 0.32608695652173914
- Min = 0.25

#### recall
- Mean = 0.30000000000000004
- Standard deviation = 0.15206906325745548
- Max = 0.5
- 75% = 0.42500000000000004
- Median = 0.3
- 25% = 0.17500000000000002
- Min = 0.1

#### facing_probas
- Mean = [0.46375    0.56       0.53395833 0.65958333 0.650625  ]
- Standard deviation = [0.16597304 0.18249429 0.10468517 0.1310872  0.14792063]
- Max = [0.765      0.755      0.705      0.82166667 0.82833333]
- 75% = [0.57416667 0.70541667 0.58583333 0.75833333 0.755     ]
- Median = [0.42333333 0.61583333 0.54416667 0.68416667 0.68333333]
- 25% = [0.34125    0.46416667 0.44833333 0.56625    0.58458333]
- Min = [0.23666667 0.22833333 0.36833333 0.445      0.39833333]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 69.375 | 10.625 |
| Actual Positive | 14.0 | 6.0 |

### robot-6
#### accuracy
- Mean = 0.3525
- Standard deviation = 0.05517019122678478
- Max = 0.45
- 75% = 0.4025
- Median = 0.325
- 25% = 0.315
- Min = 0.29

#### f1
- Mean = 0.5188458682661118
- Standard deviation = 0.05912935957872922
- Max = 0.6206896551724138
- 75% = 0.5739614994934145
- Median = 0.4905445431761221
- 25% = 0.479020979020979
- Min = 0.44961240310077516

#### precision
- Mean = 1.0
- Standard deviation = 0.0
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 1.0
- Min = 1.0

#### recall
- Mean = 0.3525
- Standard deviation = 0.05517019122678478
- Max = 0.45
- 75% = 0.4025
- Median = 0.325
- 25% = 0.315
- Min = 0.29

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
| Actual Positive | 64.75 | 35.25 |

