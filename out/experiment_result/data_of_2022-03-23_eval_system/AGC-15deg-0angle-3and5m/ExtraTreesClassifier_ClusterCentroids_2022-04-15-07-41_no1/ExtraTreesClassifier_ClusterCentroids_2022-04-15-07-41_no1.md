# ExtraTreesClassifier_ClusterCentroids_2022-04-15-07-41_no1
## Constants
- CSV_PATH = ../out/csv/experiment
- OUTPUT_PATH = ../out/experiment_result/data_of_2022-03-23_eval_system/AGC-15deg-0angle-3and5m
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
- DISTANCE = [3, 5]
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
	- sampling_strategy_ = OrderedDict([(0, 30)])
	- estimator_ = KMeans(n_clusters=30, random_state=42)
	- voting_ = soft

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
	- max_features = log2
	- max_leaf_nodes = None
	- min_impurity_decrease = 0.0
	- ccp_alpha = 0.0
	- n_features_in_ = 36
	- n_outputs_ = 1
	- classes_ = [0 1]
	- n_classes_ = 2
	- base_estimator_ = ExtraTreeClassifier()
	- oob_decision_function_ = [[0.67857143 0.32142857]
 [0.53571429 0.46428571]
 [0.57692308 0.42307692]
 [0.56666667 0.43333333]
 [0.4137931  0.5862069 ]
 [0.4137931  0.5862069 ]
 [0.67857143 0.32142857]
 [0.71428571 0.28571429]
 [0.61538462 0.38461538]
 [0.63333333 0.36666667]
 [0.57692308 0.42307692]
 [0.67857143 0.32142857]
 [0.58333333 0.41666667]
 [0.60714286 0.39285714]
 [0.63333333 0.36666667]
 [0.48148148 0.51851852]
 [0.71428571 0.28571429]
 [0.51724138 0.48275862]
 [0.48148148 0.51851852]
 [0.42857143 0.57142857]
 [0.62068966 0.37931034]
 [0.65517241 0.34482759]
 [0.55555556 0.44444444]
 [0.65517241 0.34482759]
 [0.63636364 0.36363636]
 [0.75       0.25      ]
 [0.64285714 0.35714286]
 [0.21428571 0.78571429]
 [0.60714286 0.39285714]
 [0.72       0.28      ]
 [0.37931034 0.62068966]
 [0.35714286 0.64285714]
 [0.35714286 0.64285714]
 [0.60714286 0.39285714]
 [0.65384615 0.34615385]
 [0.73333333 0.26666667]
 [0.15384615 0.84615385]
 [0.27586207 0.72413793]
 [0.22222222 0.77777778]
 [0.67857143 0.32142857]
 [0.65384615 0.34615385]
 [0.62962963 0.37037037]
 [0.2962963  0.7037037 ]
 [0.46153846 0.53846154]
 [0.2        0.8       ]
 [0.52       0.48      ]
 [0.57692308 0.42307692]
 [0.48275862 0.51724138]
 [0.44827586 0.55172414]
 [0.37931034 0.62068966]
 [0.37037037 0.62962963]
 [0.73076923 0.26923077]
 [0.62962963 0.37037037]
 [0.44827586 0.55172414]
 [0.32142857 0.67857143]
 [0.28       0.72      ]
 [0.24       0.76      ]
 [0.51724138 0.48275862]
 [0.53571429 0.46428571]
 [0.64285714 0.35714286]]
	- oob_score_ = 0.6833333333333333

#### Importance of features
- tdoa_max = 0.11481481481481483
- gp_max_ix_std = 0.10092592592592592
- hlbr = 0.08518518518518518
- tdoa_min = 0.06898148148148149
- tdoa_mean = 0.05277777777777777
- ratio_max_to_9th_ave_peaks = 0.04583333333333333
- gp_auc_range = 0.04583333333333333
- gp_max_ix_min = 0.0425925925925926
- tdoa_std = 0.03703703703703704
- low_power = 0.03333333333333333
- coe3[2] = 0.03333333333333333
- coe3[3] = 0.03333333333333333
- gp_max_ix_range = 0.03333333333333333
- gp_auc_mean = 0.029629629629629627
- ac_std = 0.028703703703703707
- gp_max_val_std = 0.026388888888888885
- ratio_max_to_10ms_ave_peaks = 0.020833333333333336
- gp_auc_std = 0.020833333333333336
- diff_std = 0.020833333333333332
- ac_auc = 0.01851851851851852
- gp_max_val_range = 0.01851851851851852
- gp_max_val_max = 0.01851851851851852
- gp_auc_max = 0.01851851851851852
- gp_max_val_min = 0.014814814814814814
- coe1[0] = 0.0125
- coe1[1] = 0.0125
- gp_max_ix_max = 0.006944444444444444
- gp_max_val_mean = 0.0046296296296296285
- high_power = 0.0
- coe3[0] = 0.0
- coe3[1] = 0.0
- diff_auc = 0.0
- srmr = 0.0
- gp_max_ix_mean = 0.0
- gp_auc_min = 0.0
- tdoa_range = 0.0

## Evaluation
cv = 8
### robot-1
#### accuracy
- Mean = 0.7749999999999999
- Standard deviation = 0.04190763653560051
- Max = 0.83
- 75% = 0.815
- Median = 0.7775000000000001
- 25% = 0.7475
- Min = 0.705

#### f1
- Mean = 0.3239178896297539
- Standard deviation = 0.11829177411876637
- Max = 0.46875
- 75% = 0.42546583850931674
- Median = 0.33024691358024694
- 25% = 0.2390941928313421
- Min = 0.15384615384615385

#### precision
- Mean = 0.4114805609814293
- Standard deviation = 0.14905083659258347
- Max = 0.625
- 75% = 0.5550974512743628
- Median = 0.40922619047619047
- 25% = 0.26700898587933247
- Min = 0.2

#### recall
- Mean = 0.271875
- Standard deviation = 0.10265042316035526
- Max = 0.4
- 75% = 0.35624999999999996
- Median = 0.30000000000000004
- 25% = 0.18125000000000002
- Min = 0.125

#### facing_probas
- Mean = [0.51270833 0.4459375  0.5590625  0.5240625  0.53666667]
- Standard deviation = [0.0409432  0.05252882 0.05253709 0.05042947 0.05556528]
- Max = [0.6        0.53166667 0.64166667 0.5825     0.605     ]
- 75% = [0.53208333 0.475625   0.59770833 0.57208333 0.58208333]
- Median = [0.49625    0.44416667 0.5625     0.53375    0.53916667]
- 25% = [0.480625   0.40020833 0.516875   0.48708333 0.50895833]
- Min = [0.475      0.3775     0.47583333 0.4325     0.44083333]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 144.125 | 15.875 |
| Actual Positive | 29.125 | 10.875 |

### robot-2
#### accuracy
- Mean = 0.71375
- Standard deviation = 0.04768057780690163
- Max = 0.795
- 75% = 0.735
- Median = 0.7175
- 25% = 0.69625
- Min = 0.625

#### f1
- Mean = 0.3247647564274031
- Standard deviation = 0.09572792410585892
- Max = 0.4186046511627907
- 75% = 0.40101010101010104
- Median = 0.3709150326797386
- 25% = 0.2619969040247678
- Min = 0.14705882352941174

#### precision
- Mean = 0.32071519654287656
- Standard deviation = 0.08215231211087684
- Max = 0.47058823529411764
- 75% = 0.35206337509211494
- Median = 0.321078431372549
- 25% = 0.28308823529411764
- Min = 0.17857142857142858

#### recall
- Mean = 0.37187499999999996
- Standard deviation = 0.1729511762752714
- Max = 0.625
- 75% = 0.50625
- Median = 0.4125
- 25% = 0.19375
- Min = 0.125

#### facing_probas
- Mean = [0.51260417 0.5828125  0.600625   0.51895833 0.50197917]
- Standard deviation = [0.04310524 0.02870449 0.06485929 0.03823981 0.02918731]
- Max = [0.57833333 0.63583333 0.70416667 0.57833333 0.53333333]
- 75% = [0.53770833 0.598125   0.64083333 0.54520833 0.51666667]
- Median = [0.51083333 0.57166667 0.60291667 0.51166667 0.51      ]
- 25% = [0.48354167 0.56125    0.56979167 0.49395833 0.49583333]
- Min = [0.45416667 0.5525     0.4925     0.47       0.43583333]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 127.875 | 32.125 |
| Actual Positive | 25.125 | 14.875 |

### robot-3
#### accuracy
- Mean = 0.6325
- Standard deviation = 0.10767427733679015
- Max = 0.77
- 75% = 0.72125
- Median = 0.64
- 25% = 0.585
- Min = 0.455

#### f1
- Mean = 0.22422175586805368
- Standard deviation = 0.11520625277368833
- Max = 0.33128834355828224
- 75% = 0.3012862259850212
- Median = 0.284990253411306
- 25% = 0.17575187969924813
- Min = 0.0

#### precision
- Mean = 0.18800217700623512
- Standard deviation = 0.08532068406697191
- Max = 0.3023255813953488
- 75% = 0.2355614973262032
- Median = 0.21160794941282746
- 25% = 0.16761363636363635
- Min = 0.0

#### recall
- Mean = 0.321875
- Standard deviation = 0.21376005093328362
- Max = 0.675
- 75% = 0.4375
- Median = 0.325
- 25% = 0.2
- Min = 0.0

#### facing_probas
- Mean = [0.50604167 0.5665625  0.61270833 0.5340625  0.530625  ]
- Standard deviation = [0.03390589 0.02889888 0.06567855 0.03353439 0.03618709]
- Max = [0.56833333 0.6075     0.73       0.575      0.58333333]
- 75% = [0.514375   0.59458333 0.641875   0.56791667 0.55604167]
- Median = [0.4975     0.5575     0.60666667 0.53291667 0.53708333]
- 25% = [0.486875   0.54708333 0.58083333 0.50395833 0.50375   ]
- Min = [0.46       0.52166667 0.5125     0.48583333 0.47666667]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 113.625 | 46.375 |
| Actual Positive | 27.125 | 12.875 |

### robot-4
#### accuracy
- Mean = 0.73875
- Standard deviation = 0.03388860427931489
- Max = 0.775
- 75% = 0.755
- Median = 0.75
- 25% = 0.7375
- Min = 0.655

#### f1
- Mean = 0.13242032927157832
- Standard deviation = 0.09316200828357267
- Max = 0.3098591549295775
- 75% = 0.1622718052738337
- Median = 0.11686256781193488
- 25% = 0.08563829787234042
- Min = 0.0

#### precision
- Mean = 0.1839171860845248
- Standard deviation = 0.1005128079286073
- Max = 0.3548387096774194
- 75% = 0.23809523809523808
- Median = 0.16875
- 25% = 0.1391941391941392
- Min = 0.0

#### recall
- Mean = 0.10937500000000001
- Standard deviation = 0.08472151069828725
- Max = 0.275
- 75% = 0.14375
- Median = 0.0875
- 25% = 0.0625
- Min = 0.0

#### facing_probas
- Mean = [0.52125    0.55375    0.59375    0.54260417 0.53458333]
- Standard deviation = [0.03246259 0.03202104 0.06544055 0.03920751 0.03108568]
- Max = [0.57833333 0.5975     0.69833333 0.60916667 0.58416667]
- 75% = [0.533125   0.58479167 0.64020833 0.57666667 0.55416667]
- Median = [0.51833333 0.545      0.59       0.525      0.5425    ]
- 25% = [0.505      0.529375   0.56145833 0.51479167 0.50833333]
- Min = [0.47416667 0.5075     0.495      0.4925     0.48916667]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 143.375 | 16.625 |
| Actual Positive | 35.625 | 4.375 |

### robot-5
#### accuracy
- Mean = 0.760625
- Standard deviation = 0.017036266463048778
- Max = 0.79
- 75% = 0.7725
- Median = 0.7575000000000001
- 25% = 0.7475
- Min = 0.74

#### f1
- Mean = 0.2069085568287387
- Standard deviation = 0.12622346140297036
- Max = 0.35135135135135137
- 75% = 0.31052631578947365
- Median = 0.234375
- 25% = 0.12518853695324283
- Min = 0.0

#### precision
- Mean = 0.2803383095662507
- Standard deviation = 0.14700299215982093
- Max = 0.45
- 75% = 0.37683823529411764
- Median = 0.3472222222222222
- 25% = 0.21022727272727273
- Min = 0.0

#### recall
- Mean = 0.171875
- Standard deviation = 0.11688502630790654
- Max = 0.325
- 75% = 0.25
- Median = 0.1875
- 25% = 0.08125
- Min = 0.0

#### facing_probas
- Mean = [0.48833333 0.52645833 0.55385417 0.52541667 0.52614583]
- Standard deviation = [0.04065223 0.0377532  0.05507403 0.04103691 0.04166029]
- Max = [0.54333333 0.56916667 0.65666667 0.60416667 0.58166667]
- 75% = [0.51583333 0.54979167 0.57708333 0.54604167 0.55375   ]
- Median = [0.50208333 0.53208333 0.55875    0.52041667 0.54041667]
- 25% = [0.46395833 0.51270833 0.52125    0.50166667 0.48833333]
- Min = [0.415      0.44333333 0.47666667 0.4575     0.455     ]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 145.25 | 14.75 |
| Actual Positive | 33.125 | 6.875 |

### robot-6
#### accuracy
- Mean = 0.24937499999999999
- Standard deviation = 0.052406911519378825
- Max = 0.325
- 75% = 0.27625
- Median = 0.245
- 25% = 0.22375
- Min = 0.16

#### f1
- Mean = 0.3963777542277721
- Standard deviation = 0.06734653866963064
- Max = 0.4905660377358491
- 75% = 0.4321653189577718
- Median = 0.3935483870967742
- 25% = 0.3655500455419492
- Min = 0.2758620689655173

#### precision
- Mean = 1.0
- Standard deviation = 0.0
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 1.0
- Min = 1.0

#### recall
- Mean = 0.24937499999999999
- Standard deviation = 0.052406911519378825
- Max = 0.325
- 75% = 0.27625
- Median = 0.245
- 25% = 0.22375
- Min = 0.16

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
| Actual Positive | 150.125 | 49.875 |

