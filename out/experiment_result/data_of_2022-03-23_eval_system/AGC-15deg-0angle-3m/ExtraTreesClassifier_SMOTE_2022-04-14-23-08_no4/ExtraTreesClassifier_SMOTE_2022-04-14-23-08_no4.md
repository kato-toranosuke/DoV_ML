# ExtraTreesClassifier_SMOTE_2022-04-14-23-08_no4
## Constants
- CSV_PATH = ../out/csv/experiment
- OUTPUT_PATH = ../out/experiment_result/data_of_2022-03-23_eval_system/AGC-15deg-0angle-3m
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
- AGC_STATUS = ['AGC-15deg']
- ANGLES = [60, 75, 90, 105, 120]

## Loaded CSV
- 2022-03-23_raspi_48000Hz_w1_N2^12_overlap80_all.csv

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
	- oob_decision_function_ = [[0.39285714 0.60714286]
 [0.3        0.7       ]
 [0.26086957 0.73913043]
 [0.46428571 0.53571429]
 [0.57142857 0.42857143]
 [0.31034483 0.68965517]
 [0.5        0.5       ]
 [0.57142857 0.42857143]
 [0.375      0.625     ]
 [0.5862069  0.4137931 ]
 [0.46428571 0.53571429]
 [0.48275862 0.51724138]
 [0.37037037 0.62962963]
 [0.73076923 0.26923077]
 [0.6        0.4       ]
 [0.35714286 0.64285714]
 [0.5        0.5       ]
 [0.34482759 0.65517241]
 [0.62962963 0.37037037]
 [0.57692308 0.42307692]
 [0.33333333 0.66666667]
 [0.60714286 0.39285714]
 [0.4137931  0.5862069 ]
 [0.44444444 0.55555556]
 [0.54545455 0.45454545]
 [0.5        0.5       ]
 [0.37037037 0.62962963]
 [0.48275862 0.51724138]
 [0.57142857 0.42857143]
 [0.59259259 0.40740741]
 [0.4        0.6       ]
 [0.35714286 0.64285714]
 [0.60714286 0.39285714]
 [0.37931034 0.62068966]
 [0.32142857 0.67857143]
 [0.34482759 0.65517241]
 [0.30769231 0.69230769]
 [0.27586207 0.72413793]
 [0.34482759 0.65517241]
 [0.43333333 0.56666667]
 [0.46153846 0.53846154]
 [0.43478261 0.56521739]
 [0.42857143 0.57142857]
 [0.48       0.52      ]
 [0.43333333 0.56666667]
 [0.69230769 0.30769231]
 [0.75       0.25      ]
 [0.7037037  0.2962963 ]
 [0.66666667 0.33333333]
 [0.51851852 0.48148148]
 [0.7037037  0.2962963 ]
 [0.34482759 0.65517241]
 [0.07692308 0.92307692]
 [0.20689655 0.79310345]
 [0.25925926 0.74074074]
 [0.34615385 0.65384615]
 [0.65384615 0.34615385]
 [0.34482759 0.65517241]
 [0.68965517 0.31034483]
 [0.62068966 0.37931034]
 [0.84       0.16      ]
 [0.72413793 0.27586207]
 [0.82142857 0.17857143]
 [0.62962963 0.37037037]
 [0.48275862 0.51724138]
 [0.64285714 0.35714286]
 [0.44444444 0.55555556]
 [0.39285714 0.60714286]
 [0.37931034 0.62068966]
 [0.48148148 0.51851852]
 [0.39285714 0.60714286]
 [0.64       0.36      ]
 [0.33333333 0.66666667]
 [0.6        0.4       ]
 [0.46153846 0.53846154]
 [0.42857143 0.57142857]
 [0.24       0.76      ]
 [0.34615385 0.65384615]
 [0.31034483 0.68965517]
 [0.48148148 0.51851852]
 [0.46428571 0.53571429]
 [0.48       0.52      ]
 [0.51724138 0.48275862]
 [0.34615385 0.65384615]
 [0.44444444 0.55555556]
 [0.31034483 0.68965517]
 [0.32       0.68      ]
 [0.34482759 0.65517241]
 [0.2962963  0.7037037 ]
 [0.34615385 0.65384615]
 [0.35714286 0.64285714]
 [0.25       0.75      ]
 [0.5        0.5       ]
 [0.32       0.68      ]
 [0.39285714 0.60714286]
 [0.48148148 0.51851852]
 [0.62068966 0.37931034]
 [0.2962963  0.7037037 ]
 [0.37037037 0.62962963]
 [0.35714286 0.64285714]
 [0.39285714 0.60714286]
 [0.32       0.68      ]
 [0.37037037 0.62962963]
 [0.24       0.76      ]
 [0.35714286 0.64285714]
 [0.28571429 0.71428571]
 [0.2962963  0.7037037 ]
 [0.38461538 0.61538462]
 [0.27586207 0.72413793]
 [0.30434783 0.69565217]
 [0.32142857 0.67857143]
 [0.60714286 0.39285714]
 [0.53333333 0.46666667]
 [0.24137931 0.75862069]
 [0.15384615 0.84615385]
 [0.48       0.52      ]
 [0.30769231 0.69230769]
 [0.27586207 0.72413793]
 [0.34615385 0.65384615]
 [0.39285714 0.60714286]]
	- oob_score_ = 0.65

#### Importance of features
- gp_max_val_range = 0.06775793650793652
- gp_auc_range = 0.05921693121693121
- gp_max_val_std = 0.058413202317964215
- gp_max_ix_mean = 0.05353395061728395
- gp_auc_mean = 0.053197908793146884
- gp_auc_max = 0.05146972369194591
- gp_auc_std = 0.04238095238095239
- coe3[3] = 0.04032716049382716
- gp_max_val_mean = 0.03744488536155202
- gp_max_val_max = 0.036413139329805985
- low_power = 0.0357936507936508
- tdoa_std = 0.03448412698412698
- tdoa_mean = 0.03421847442680776
- diff_auc = 0.03392261904761905
- ac_std = 0.03232804232804233
- gp_max_val_min = 0.030787037037037036
- ratio_max_to_9th_ave_peaks = 0.028518518518518512
- srmr = 0.027898001175778946
- coe1[0] = 0.025826719576719573
- coe3[2] = 0.025796296296296296
- coe1[1] = 0.024166666666666666
- ac_auc = 0.02325
- gp_max_ix_std = 0.02152469135802469
- high_power = 0.01948148148148148
- gp_auc_min = 0.018939594356261025
- diff_std = 0.018904320987654325
- ratio_max_to_10ms_ave_peaks = 0.017824074074074072
- gp_max_ix_range = 0.015436507936507938
- tdoa_range = 0.010185185185185186
- tdoa_max = 0.009341269841269841
- gp_max_ix_max = 0.007545351473922904
- hlbr = 0.003671579743008315
- coe3[0] = 0.0
- coe3[1] = 0.0
- gp_max_ix_min = 0.0
- tdoa_min = 0.0

## Evaluation
cv = 8
### robot-1
#### accuracy
- Mean = 0.75375
- Standard deviation = 0.05786568499551352
- Max = 0.82
- 75% = 0.79
- Median = 0.765
- 25% = 0.7275
- Min = 0.63

#### f1
- Mean = 0.49395237904503403
- Standard deviation = 0.10173032692787129
- Max = 0.5909090909090908
- 75% = 0.5491071428571429
- Median = 0.5253061224489796
- 25% = 0.48330914368650213
- Min = 0.24489795918367346

#### precision
- Mean = 0.4261065084340946
- Standard deviation = 0.10080864713007325
- Max = 0.5454545454545454
- 75% = 0.4836309523809524
- Median = 0.44080459770114944
- 25% = 0.3892045454545454
- Min = 0.20689655172413793

#### recall
- Mean = 0.59375
- Standard deviation = 0.11301963325015704
- Max = 0.65
- 75% = 0.65
- Median = 0.65
- 25% = 0.6
- Min = 0.3

#### facing_probas
- Mean = [0.57354167 0.48541667 0.394375   0.35208333 0.27166667]
- Standard deviation = [0.04112513 0.07589169 0.07350802 0.04945361 0.03580425]
- Max = [0.67       0.585      0.52833333 0.42       0.33333333]
- 75% = [0.58791667 0.53333333 0.43       0.38208333 0.29666667]
- Median = [0.5575     0.51       0.38416667 0.35583333 0.26916667]
- 25% = [0.54541667 0.44583333 0.34708333 0.33041667 0.24875   ]
- Min = [0.53666667 0.32833333 0.28666667 0.255      0.22      ]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 63.5 | 16.5 |
| Actual Positive | 8.125 | 11.875 |

### robot-2
#### accuracy
- Mean = 0.74125
- Standard deviation = 0.045944939873722786
- Max = 0.81
- 75% = 0.78
- Median = 0.75
- 25% = 0.69
- Min = 0.68

#### f1
- Mean = 0.10231249225814446
- Standard deviation = 0.13374269009155823
- Max = 0.4074074074074075
- 75% = 0.1588628762541806
- Median = 0.04166666666666667
- 25% = 0.0
- Min = 0.0

#### precision
- Mean = 0.19669117647058823
- Standard deviation = 0.22727392190408127
- Max = 0.6666666666666666
- 75% = 0.32598039215686275
- Median = 0.125
- 25% = 0.0
- Min = 0.0

#### recall
- Mean = 0.1
- Standard deviation = 0.17500000000000004
- Max = 0.55
- 75% = 0.1
- Median = 0.025
- 25% = 0.0
- Min = 0.0

#### facing_probas
- Mean = [0.61270833 0.50895833 0.51395833 0.51520833 0.319375  ]
- Standard deviation = [0.04189883 0.05569596 0.05738477 0.06474543 0.06166631]
- Max = [0.67333333 0.63833333 0.58333333 0.65333333 0.42      ]
- 75% = [0.64708333 0.52041667 0.56541667 0.53208333 0.36541667]
- Median = [0.605      0.4875     0.51083333 0.5175     0.32      ]
- 25% = [0.58583333 0.47541667 0.48833333 0.48666667 0.27083333]
- Min = [0.55666667 0.45166667 0.40833333 0.42166667 0.22      ]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 72.125 | 7.875 |
| Actual Positive | 18.0 | 2.0 |

### robot-3
#### accuracy
- Mean = 0.70625
- Standard deviation = 0.09150648884095601
- Max = 0.81
- 75% = 0.785
- Median = 0.73
- 25% = 0.6325000000000001
- Min = 0.57

#### f1
- Mean = 0.16905045447011013
- Standard deviation = 0.12566088537214898
- Max = 0.37837837837837834
- 75% = 0.25435540069686413
- Median = 0.17458521870286575
- 25% = 0.07142857142857142
- Min = 0.0

#### precision
- Mean = 0.30439277525526337
- Standard deviation = 0.3114609141839523
- Max = 1.0
- 75% = 0.4338235294117647
- Median = 0.19717261904761904
- 25% = 0.0967741935483871
- Min = 0.0

#### recall
- Mean = 0.16249999999999998
- Standard deviation = 0.12183492931011204
- Max = 0.35
- 75% = 0.25
- Median = 0.2
- 25% = 0.037500000000000006
- Min = 0.0

#### facing_probas
- Mean = [0.61479167 0.56729167 0.57291667 0.61125    0.510625  ]
- Standard deviation = [0.02117122 0.06255518 0.0634251  0.05626543 0.05981997]
- Max = [0.65333333 0.67666667 0.65666667 0.71       0.59166667]
- 75% = [0.62833333 0.60208333 0.62875    0.64583333 0.5475    ]
- Median = [0.61666667 0.56916667 0.58333333 0.60583333 0.51833333]
- 25% = [0.59708333 0.54208333 0.52       0.57875    0.47916667]
- Min = [0.58333333 0.45       0.48166667 0.51666667 0.41      ]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 67.375 | 12.625 |
| Actual Positive | 16.75 | 3.25 |

### robot-4
#### accuracy
- Mean = 0.7025
- Standard deviation = 0.04235268586524354
- Max = 0.76
- 75% = 0.7275
- Median = 0.705
- 25% = 0.6849999999999999
- Min = 0.62

#### f1
- Mean = 0.28833302177650955
- Standard deviation = 0.1430025966974849
- Max = 0.456140350877193
- 75% = 0.3695014662756598
- Median = 0.34275248560962845
- 25% = 0.25357142857142856
- Min = 0.0

#### precision
- Mean = 0.25600192816617495
- Standard deviation = 0.11806109084084139
- Max = 0.3684210526315789
- 75% = 0.33783783783783783
- Median = 0.2928571428571428
- 25% = 0.24022988505747125
- Min = 0.0

#### recall
- Mean = 0.35
- Standard deviation = 0.2076655965729519
- Max = 0.65
- 75% = 0.45
- Median = 0.375
- 25% = 0.25
- Min = 0.0

#### facing_probas
- Mean = [0.456875   0.48875    0.543125   0.57229167 0.48354167]
- Standard deviation = [0.05209791 0.05720182 0.05052803 0.06088433 0.04479457]
- Max = [0.53       0.58666667 0.60166667 0.69666667 0.55833333]
- 75% = [0.47833333 0.51958333 0.58166667 0.605      0.5075    ]
- Median = [0.47       0.47166667 0.5425     0.55916667 0.4775    ]
- 25% = [0.44291667 0.45375    0.5275     0.53916667 0.455     ]
- Min = [0.34       0.42       0.43166667 0.48333333 0.41166667]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 63.25 | 16.75 |
| Actual Positive | 13.0 | 7.0 |

### robot-5
#### accuracy
- Mean = 0.79
- Standard deviation = 0.03162277660168379
- Max = 0.83
- 75% = 0.8125
- Median = 0.79
- 25% = 0.78
- Min = 0.72

#### f1
- Mean = 0.223275316706726
- Standard deviation = 0.08806358814307945
- Max = 0.29629629629629634
- 75% = 0.2689655172413793
- Median = 0.2554347826086956
- 25% = 0.22023809523809523
- Min = 0.0

#### precision
- Mean = 0.47385912698412697
- Standard deviation = 0.285776726360186
- Max = 1.0
- 75% = 0.6160714285714286
- Median = 0.4222222222222222
- 25% = 0.34375
- Min = 0.0

#### recall
- Mean = 0.15625
- Standard deviation = 0.06343057228182637
- Max = 0.2
- 75% = 0.2
- Median = 0.175
- 25% = 0.15
- Min = 0.0

#### facing_probas
- Mean = [0.30270833 0.35166667 0.44166667 0.52875    0.46895833]
- Standard deviation = [0.08591799 0.07247126 0.07800908 0.06553598 0.05923668]
- Max = [0.43666667 0.485      0.56666667 0.63333333 0.57666667]
- 75% = [0.3625     0.37958333 0.51166667 0.58083333 0.48833333]
- Median = [0.30333333 0.3425     0.42666667 0.51       0.44583333]
- 25% = [0.22708333 0.31666667 0.3775     0.47166667 0.42291667]
- Min = [0.17666667 0.225      0.33333333 0.45333333 0.415     ]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 75.875 | 4.125 |
| Actual Positive | 16.875 | 3.125 |

### robot-6
#### accuracy
- Mean = 0.2725
- Standard deviation = 0.04408798022137099
- Max = 0.32
- 75% = 0.3025
- Median = 0.28
- 25% = 0.26
- Min = 0.17

#### f1
- Mean = 0.42630921982807873
- Standard deviation = 0.0572348985130194
- Max = 0.48484848484848486
- 75% = 0.464474456840869
- Median = 0.437404626747238
- 25% = 0.41269841269841273
- Min = 0.2905982905982906

#### precision
- Mean = 1.0
- Standard deviation = 0.0
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 1.0
- Min = 1.0

#### recall
- Mean = 0.2725
- Standard deviation = 0.04408798022137099
- Max = 0.32
- 75% = 0.3025
- Median = 0.28
- 25% = 0.26
- Min = 0.17

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
| Actual Positive | 72.75 | 27.25 |

