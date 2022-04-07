# ExtraTreesClassifier_ClusterCentroids_2022-01-20-06-14_no1
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
	- sampling_strategy_ = OrderedDict([(1, 36)])
	- estimator_ = KMeans(n_clusters=36, random_state=42)
	- voting_ = soft

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
- gp_max_val_mean = 0.21742656182549017
- gp_max_val_max = 0.2111652139171519
- diff_auc = 0.06942239896887152
- srmr = 0.06528348844138318
- gp_auc_min = 0.05203573508084787
- high_power = 0.051804265565875474
- gp_auc_mean = 0.04887620988498181
- coe3[2] = 0.041475963887966476
- coe1[1] = 0.03065255874705185
- gp_auc_std = 0.02987860111588141
- coe1[0] = 0.02854080785115266
- tdoa_mean = 0.024461152882205513
- diff_std = 0.019379883892079015
- low_power = 0.017664280164280167
- gp_auc_max = 0.017442073856802548
- gp_max_val_min = 0.014911616161616162
- tdoa_std = 0.014389847324483437
- gp_max_ix_std = 0.0125
- tdoa_max = 0.009814814814814816
- ac_std = 0.006759259259259259
- ratio_max_to_10ms_ave_peaks = 0.004373599363840094
- coe3[3] = 0.004181184668989552
- hlbr = 0.0029629629629629632
- gp_max_ix_max = 0.002962962962962963
- gp_auc_range = 0.0005952380952380964
- ratio_max_to_9th_ave_peaks = 0.0004528985507246391
- gp_max_val_range = 0.0003086419753086433
- tdoa_range = 0.0002777777777777768
- coe3[0] = 0.0
- coe3[1] = 0.0
- ac_auc = 0.0
- gp_max_val_std = 0.0
- gp_max_ix_range = 0.0
- gp_max_ix_min = 0.0
- gp_max_ix_mean = 0.0
- tdoa_min = 0.0

## Evaluation
cv = 8
### robot-1
#### accuracy
- Mean = 0.98625
- Standard deviation = 0.008569568250501312
- Max = 1.0
- 75% = 0.99
- Median = 0.99
- 25% = 0.98
- Min = 0.97

#### f1
- Mean = 0.9671791859114605
- Standard deviation = 0.01988885563277107
- Max = 1.0
- 75% = 0.975609756097561
- Median = 0.975609756097561
- 25% = 0.9523809523809523
- Min = 0.9302325581395349

#### precision
- Mean = 0.9371588556371164
- Standard deviation = 0.03711532284633058
- Max = 1.0
- 75% = 0.9523809523809523
- Median = 0.9523809523809523
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
- Mean = [9.73125e-01 7.63125e-01 2.93750e-02 1.87500e-03 6.25000e-04]
- Standard deviation = [0.01748884 0.08971962 0.00768013 0.00242061 0.00165359]
- Max = [0.995 0.86  0.04  0.005 0.005]
- 75% = [0.98625 0.84375 0.03625 0.005   0.     ]
- Median = [0.9775 0.7825 0.0275 0.     0.    ]
- 25% = [0.9625  0.71    0.02375 0.      0.     ]
- Min = [0.94  0.605 0.02  0.    0.   ]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 78.625 | 1.375 |
| Actual Positive | 0.0 | 20.0 |

### robot-2
#### accuracy
- Mean = 0.98625
- Standard deviation = 0.008569568250501312
- Max = 1.0
- 75% = 0.99
- Median = 0.99
- 25% = 0.98
- Min = 0.97

#### f1
- Mean = 0.9638864573075099
- Standard deviation = 0.023212746960289708
- Max = 1.0
- 75% = 0.9743589743589743
- Median = 0.9743589743589743
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
- Mean = 0.9312499999999999
- Standard deviation = 0.04284784125250652
- Max = 1.0
- 75% = 0.95
- Median = 0.95
- 25% = 0.9
- Min = 0.85

#### facing_probas
- Mean = [0.973125 0.96     0.830625 0.049375 0.001875]
- Standard deviation = [0.02344375 0.02061553 0.05923668 0.03431813 0.00496078]
- Max = [1.    0.995 0.905 0.115 0.015]
- 75% = [0.99125 0.97125 0.87375 0.07125 0.     ]
- Median = [0.98   0.9625 0.85   0.0425 0.    ]
- 25% = [0.95875 0.9475  0.79    0.025   0.     ]
- Min = [0.935 0.925 0.725 0.    0.   ]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 80.0 | 0.0 |
| Actual Positive | 1.375 | 18.625 |

### robot-3
#### accuracy
- Mean = 0.98375
- Standard deviation = 0.017984368212422715
- Max = 1.0
- 75% = 1.0
- Median = 0.99
- 25% = 0.975
- Min = 0.95

#### f1
- Mean = 0.9552647644752907
- Standard deviation = 0.05102563007007202
- Max = 1.0
- 75% = 1.0
- Median = 0.9743589743589743
- 25% = 0.932748538011696
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
- Mean = 0.91875
- Standard deviation = 0.08992184106211348
- Max = 1.0
- 75% = 1.0
- Median = 0.95
- 25% = 0.875
- Min = 0.75

#### facing_probas
- Mean = [0.206875 0.93875  0.97625  0.890625 0.0625  ]
- Standard deviation = [0.0861299  0.03425547 0.0238157  0.05210791 0.03856812]
- Max = [0.32  0.975 1.    0.96  0.135]
- 75% = [0.27    0.97125 0.9925  0.93625 0.08125]
- Median = [0.22   0.9475 0.99   0.8975 0.06  ]
- 25% = [0.135   0.91125 0.95375 0.8425  0.035  ]
- Min = [0.085 0.88  0.935 0.815 0.01 ]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 80.0 | 0.0 |
| Actual Positive | 1.625 | 18.375 |

### robot-4
#### accuracy
- Mean = 0.9624999999999999
- Standard deviation = 0.01561249499599601
- Max = 0.99
- 75% = 0.9724999999999999
- Median = 0.96
- 25% = 0.95
- Min = 0.94

#### f1
- Mean = 0.8971431426879588
- Standard deviation = 0.04538572460234148
- Max = 0.9743589743589743
- 75% = 0.926031294452347
- Median = 0.888888888888889
- 25% = 0.8728222996515679
- Min = 0.8235294117647058

#### precision
- Mean = 0.9821428571428572
- Standard deviation = 0.047245559126153414
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 1.0
- Min = 0.8571428571428571

#### recall
- Mean = 0.83125
- Standard deviation = 0.07880950133074058
- Max = 0.95
- 75% = 0.9
- Median = 0.825
- 25% = 0.7875000000000001
- Min = 0.7

#### facing_probas
- Mean = [0.0025   0.18     0.936875 0.98125  0.81625 ]
- Standard deviation = [0.00661438 0.08455767 0.04278854 0.02042517 0.05383714]
- Max = [0.02  0.315 0.985 1.    0.89 ]
- 75% = [0.      0.21875 0.97125 1.      0.86375]
- Median = [0.     0.1775 0.9575 0.99   0.8125]
- 25% = [0.      0.13875 0.89125 0.9625  0.75875]
- Min = [0.    0.02  0.875 0.95  0.755]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 79.625 | 0.375 |
| Actual Positive | 3.375 | 16.625 |

### robot-5
#### accuracy
- Mean = 0.995
- Standard deviation = 0.010000000000000009
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 0.9975
- Min = 0.97

#### f1
- Mean = 0.9868160843770599
- Standard deviation = 0.026875873608300863
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 0.9939024390243902
- Min = 0.9189189189189189

#### precision
- Mean = 0.9940476190476191
- Standard deviation = 0.01574851970871782
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 1.0
- Min = 0.9523809523809523

#### recall
- Mean = 0.98125
- Standard deviation = 0.04960783708246108
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 1.0
- Min = 0.85

#### facing_probas
- Mean = [0.01     0.003125 0.11375  0.941875 0.955625]
- Standard deviation = [0.01089725 0.00347985 0.06771955 0.03490501 0.0231081 ]
- Max = [0.03  0.01  0.24  0.985 0.995]
- 75% = [0.02    0.005   0.16125 0.96375 0.96875]
- Median = [0.005  0.0025 0.095  0.955  0.9575]
- 25% = [0.      0.      0.0575  0.92    0.93375]
- Min = [0.    0.    0.035 0.875 0.925]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 79.875 | 0.125 |
| Actual Positive | 0.375 | 19.625 |

### robot-6
#### accuracy
- Mean = 0.9325
- Standard deviation = 0.02989565185775348
- Max = 0.98
- 75% = 0.9475
- Median = 0.93
- 25% = 0.9175
- Min = 0.88

#### f1
- Mean = 0.9648233744498751
- Standard deviation = 0.01601927085665525
- Max = 0.98989898989899
- 75% = 0.9729970171123554
- Median = 0.9637305699481865
- 25% = 0.9569698952879582
- Min = 0.9361702127659575

#### precision
- Mean = 1.0
- Standard deviation = 0.0
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 1.0
- Min = 1.0

#### recall
- Mean = 0.9325
- Standard deviation = 0.02989565185775348
- Max = 0.98
- 75% = 0.9475
- Median = 0.93
- 25% = 0.9175
- Min = 0.88

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
| Actual Positive | 6.75 | 93.25 |

