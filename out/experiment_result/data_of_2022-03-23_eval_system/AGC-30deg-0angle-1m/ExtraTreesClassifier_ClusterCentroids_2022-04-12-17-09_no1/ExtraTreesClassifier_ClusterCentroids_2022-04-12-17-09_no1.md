# ExtraTreesClassifier_ClusterCentroids_2022-04-12-17-09_no1
## Constants
- CSV_PATH = ../out/csv/experiment
- OUTPUT_PATH = ../out/experiment_result/data_of_2022-03-23_eval_system/AGC-30deg-0angle-1m
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
- DISTANCE = [1]
- AGC_STATUS = ['AGC-30deg']
- ANGLES = [30, 60, 90, 120, 150]

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
	- oob_decision_function_ = [[0.78125    0.21875   ]
 [0.98148148 0.01851852]
 [1.         0.        ]
 [0.91666667 0.08333333]
 [0.52083333 0.47916667]
 [0.95833333 0.04166667]
 [1.         0.        ]
 [1.         0.        ]
 [0.51666667 0.48333333]
 [0.52380952 0.47619048]
 [0.43333333 0.56666667]
 [0.60714286 0.39285714]
 [1.         0.        ]
 [1.         0.        ]
 [0.97222222 0.02777778]
 [0.         1.        ]
 [0.         1.        ]
 [0.125      0.875     ]
 [0.         1.        ]
 [0.         1.        ]
 [0.         1.        ]
 [0.59722222 0.40277778]
 [0.25       0.75      ]
 [0.17857143 0.82142857]
 [0.16666667 0.83333333]
 [0.5        0.5       ]
 [0.         1.        ]
 [0.57407407 0.42592593]
 [0.22222222 0.77777778]
 [0.33333333 0.66666667]]
	- oob_score_ = 0.8666666666666667

#### Importance of features
- gp_max_val_max = 0.19922360248447207
- gp_auc_min = 0.16901893287435454
- gp_max_val_mean = 0.09004758128469467
- gp_max_ix_max = 0.0881340579710145
- gp_auc_max = 0.08510730759766065
- gp_max_ix_range = 0.0772578428842436
- gp_max_ix_std = 0.07544359446419503
- tdoa_range = 0.06367521367521367
- tdoa_max = 0.05714285714285715
- gp_max_val_range = 0.0496822282099344
- diff_std = 0.023809523809523808
- coe1[1] = 0.01904761904761904
- coe1[0] = 0.0024096385542168755
- low_power = 0.0
- high_power = 0.0
- hlbr = 0.0
- coe3[0] = 0.0
- coe3[1] = 0.0
- coe3[2] = 0.0
- coe3[3] = 0.0
- ratio_max_to_10ms_ave_peaks = 0.0
- ratio_max_to_9th_ave_peaks = 0.0
- ac_std = 0.0
- ac_auc = 0.0
- diff_auc = 0.0
- srmr = 0.0
- gp_max_val_std = 0.0
- gp_max_val_min = 0.0
- gp_max_ix_min = 0.0
- gp_max_ix_mean = 0.0
- gp_auc_std = 0.0
- gp_auc_range = 0.0
- gp_auc_mean = 0.0
- tdoa_std = 0.0
- tdoa_min = 0.0
- tdoa_mean = 0.0

## Evaluation
cv = 8
### robot-1
#### accuracy
- Mean = 0.9924999999999999
- Standard deviation = 0.009682458365518551
- Max = 1.0
- 75% = 1.0
- Median = 0.995
- 25% = 0.99
- Min = 0.97

#### f1
- Mean = 0.9816636851520573
- Standard deviation = 0.02277641047745863
- Max = 1.0
- 75% = 1.0
- Median = 0.9871794871794872
- 25% = 0.9743589743589743
- Min = 0.9302325581395349

#### precision
- Mean = 0.9836956521739131
- Standard deviation = 0.043137249636922684
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 1.0
- Min = 0.8695652173913043

#### recall
- Mean = 0.98125
- Standard deviation = 0.024206145913796374
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 0.95
- Min = 0.95

#### facing_probas
- Mean = [0.91141667 0.1964375  0.14415625 0.0630625  0.16090625]
- Standard deviation = [0.04398475 0.08305768 0.08144337 0.04234522 0.06967399]
- Max = [0.96    0.38625 0.34    0.155   0.251  ]
- 75% = [0.93616667 0.20145833 0.14810417 0.081125   0.21      ]
- Median = [0.930125   0.17958333 0.12616667 0.0525     0.16270833]
- 25% = [0.89566667 0.1579375  0.1001875  0.040625   0.139375  ]
- Min = [0.83075    0.08133333 0.06041667 0.01083333 0.01      ]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 79.625 | 0.375 |
| Actual Positive | 0.375 | 19.625 |

### robot-2
#### accuracy
- Mean = 0.785
- Standard deviation = 0.07681145747868609
- Max = 0.89
- 75% = 0.84
- Median = 0.805
- 25% = 0.7075
- Min = 0.67

#### f1
- Mean = 0.5554710273170544
- Standard deviation = 0.21659603386098444
- Max = 0.7755102040816326
- 75% = 0.6836734693877551
- Median = 0.6399036531513449
- 25% = 0.4934426229508197
- Min = 0.0625

#### precision
- Mean = 0.4543040112163325
- Standard deviation = 0.17514379088567614
- Max = 0.6551724137931034
- 75% = 0.5718390804597702
- Median = 0.5075757575757576
- 25% = 0.37125435540069684
- Min = 0.08333333333333333

#### recall
- Mean = 0.7312500000000001
- Standard deviation = 0.2882463139400051
- Max = 1.0
- 75% = 0.9125
- Median = 0.825
- 25% = 0.7
- Min = 0.05

#### facing_probas
- Mean = [0.5701875  0.94552083 0.92938542 0.38688021 0.0595625 ]
- Standard deviation = [0.16693377 0.04654172 0.01839596 0.16886357 0.03838474]
- Max = [0.88    0.99375 0.9645  0.755   0.119  ]
- 75% = [0.6325     0.9703125  0.943125   0.44558333 0.08354167]
- Median = [0.58291667 0.95466667 0.92366667 0.33741667 0.06041667]
- 25% = [0.43925    0.9430625  0.9144375  0.29098958 0.036875  ]
- Min = [0.31466667 0.83075    0.90716667 0.16666667 0.005     ]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 63.875 | 16.125 |
| Actual Positive | 5.375 | 14.625 |

### robot-3
#### accuracy
- Mean = 0.80125
- Standard deviation = 0.05348773223833667
- Max = 0.87
- 75% = 0.84
- Median = 0.805
- 25% = 0.77
- Min = 0.71

#### f1
- Mean = 0.31946351955687724
- Standard deviation = 0.2117419032185679
- Max = 0.5806451612903226
- 75% = 0.4482758620689655
- Median = 0.39763001974983536
- 25% = 0.1607142857142857
- Min = 0.0

#### precision
- Mean = 0.45487743817485193
- Standard deviation = 0.31735887495862686
- Max = 0.8888888888888888
- 75% = 0.7045454545454546
- Median = 0.4602272727272727
- 25% = 0.25862068965517243
- Min = 0.0

#### recall
- Mean = 0.2625
- Standard deviation = 0.18157298807917438
- Max = 0.5
- 75% = 0.41250000000000003
- Median = 0.3
- 25% = 0.11249999999999999
- Min = 0.0

#### facing_probas
- Mean = [0.33878125 0.839375   0.80967187 0.58258333 0.39282812]
- Standard deviation = [0.18167954 0.09245032 0.07357522 0.10622319 0.17485003]
- Max = [0.75875 0.97    0.9     0.74875 0.76125]
- 75% = [0.41645833 0.9215625  0.86747917 0.678      0.443875  ]
- Median = [0.25791667 0.841      0.8203125  0.5775     0.331625  ]
- 25% = [0.21966667 0.76925    0.761375   0.47854167 0.30716667]
- Min = [0.1625     0.69125    0.6735     0.44708333 0.14729167]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 74.875 | 5.125 |
| Actual Positive | 14.75 | 5.25 |

### robot-4
#### accuracy
- Mean = 0.735
- Standard deviation = 0.04898979485566356
- Max = 0.83
- 75% = 0.7625
- Median = 0.73
- 25% = 0.6975
- Min = 0.67

#### f1
- Mean = 0.4486389581561613
- Standard deviation = 0.1086940913307265
- Max = 0.5818181818181818
- 75% = 0.5351153039832284
- Median = 0.4728291316526611
- 25% = 0.37777777777777777
- Min = 0.2666666666666666

#### precision
- Mean = 0.39134172437303366
- Standard deviation = 0.10690694766892325
- Max = 0.6
- 75% = 0.44516806722689073
- Median = 0.3895405669599218
- 25% = 0.32
- Min = 0.24

#### recall
- Mean = 0.55
- Standard deviation = 0.17320508075688776
- Max = 0.8
- 75% = 0.7124999999999999
- Median = 0.525
- 25% = 0.425
- Min = 0.3

#### facing_probas
- Mean = [0.12816667 0.62675    0.50383854 0.83357812 0.85928646]
- Standard deviation = [0.10353424 0.15706097 0.17158286 0.06744303 0.07338796]
- Max = [0.36625    0.88625    0.84625    0.93541667 0.955     ]
- 75% = [0.1489375  0.7420625  0.575      0.881125   0.92520833]
- Median = [0.103      0.57004167 0.46641667 0.831      0.86670833]
- 25% = [0.064      0.48816667 0.384      0.80494792 0.78817708]
- Min = [0.0225     0.45958333 0.305625   0.70158333 0.75858333]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 62.5 | 17.5 |
| Actual Positive | 9.0 | 11.0 |

### robot-5
#### accuracy
- Mean = 0.76125
- Standard deviation = 0.05372092236736074
- Max = 0.87
- 75% = 0.78
- Median = 0.77
- 25% = 0.725
- Min = 0.68

#### f1
- Mean = 0.15876732963354195
- Standard deviation = 0.20935655969037772
- Max = 0.6829268292682926
- 75% = 0.16895604395604394
- Median = 0.08012820512820512
- 25% = 0.044117647058823525
- Min = 0.0

#### precision
- Mean = 0.23288690476190474
- Standard deviation = 0.21144440488962335
- Max = 0.6666666666666666
- 75% = 0.34375
- Median = 0.20833333333333331
- 25% = 0.05357142857142857
- Min = 0.0

#### recall
- Mean = 0.1375
- Standard deviation = 0.21758618981911512
- Max = 0.7
- 75% = 0.1125
- Median = 0.05
- 25% = 0.037500000000000006
- Min = 0.0

#### facing_probas
- Mean = [0.05376042 0.41610938 0.19479167 0.93985417 0.77915625]
- Standard deviation = [0.04672681 0.16957226 0.12170218 0.04034964 0.10727355]
- Max = [0.16    0.78125 0.4625  1.      0.92625]
- 75% = [0.06610417 0.48441667 0.20977083 0.973375   0.84658333]
- Median = [0.04875    0.36333333 0.1765     0.93583333 0.82775   ]
- 25% = [0.01854167 0.30744792 0.12252083 0.91783333 0.7       ]
- Min = [0.005      0.20666667 0.0525     0.863      0.59466667]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 73.375 | 6.625 |
| Actual Positive | 17.25 | 2.75 |

### robot-6
#### accuracy
- Mean = 0.5325
- Standard deviation = 0.08181534085976785
- Max = 0.64
- 75% = 0.5974999999999999
- Median = 0.535
- 25% = 0.4875
- Min = 0.37

#### f1
- Mean = 0.6910850227617342
- Standard deviation = 0.07239723254317516
- Max = 0.7804878048780487
- 75% = 0.7479617982762637
- Median = 0.6970545794075206
- 25% = 0.655450752766189
- Min = 0.5401459854014599

#### precision
- Mean = 1.0
- Standard deviation = 0.0
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 1.0
- Min = 1.0

#### recall
- Mean = 0.5325
- Standard deviation = 0.08181534085976785
- Max = 0.64
- 75% = 0.5974999999999999
- Median = 0.535
- 25% = 0.4875
- Min = 0.37

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
| Actual Positive | 46.75 | 53.25 |

