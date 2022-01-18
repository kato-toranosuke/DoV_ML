# ExtraTreesClassifier_RandomUnderSampler_2022-01-17-11-01_no2
## Constants
- CSV_PATH = ../out/csv/experiment
- OUTPUT_PATH = ../out/experiment_result/data_of_2022-01-13_eval_system/AGC-0angle-5m
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
- AGC_STATUS = ['AGC']

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
	- sampling_strategy_ = OrderedDict([(0, 15)])
	- sample_indices_ = [ 3  8 45 57 16 66 42 60 15 69 58 62 40  6 64  0  1  2 18 19 20 36 37 38
 54 55 56 72 73 74]

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
	- max_samples = 0.5
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
	- oob_decision_function_ = [[0.45833333 0.54166667]
 [0.86956522 0.13043478]
 [0.91666667 0.08333333]
 [0.25       0.75      ]
 [0.5        0.5       ]
 [0.94117647 0.05882353]
 [1.         0.        ]
 [0.94117647 0.05882353]
 [0.78571429 0.21428571]
 [0.72222222 0.27777778]
 [0.         1.        ]
 [0.875      0.125     ]
 [0.35       0.65      ]
 [0.73333333 0.26666667]
 [1.         0.        ]
 [0.5        0.5       ]
 [0.36842105 0.63157895]
 [0.1        0.9       ]
 [0.35294118 0.64705882]
 [0.07142857 0.92857143]
 [0.10526316 0.89473684]
 [0.2        0.8       ]
 [0.4        0.6       ]
 [0.3        0.7       ]
 [0.81818182 0.18181818]
 [0.26086957 0.73913043]
 [0.11111111 0.88888889]
 [0.125      0.875     ]
 [0.33333333 0.66666667]
 [0.41176471 0.58823529]]
	- oob_score_ = 0.8

#### Importance of features
- gp_max_val_min = 0.19136904761904763
- gp_max_val_mean = 0.12182539682539682
- gp_auc_mean = 0.11786571067821067
- gp_auc_max = 0.09412202380952381
- srmr = 0.08820861678004535
- gp_max_val_max = 0.07616642616642616
- high_power = 0.03333333333333333
- ac_auc = 0.030778769841269846
- gp_auc_range = 0.030086580086580085
- gp_auc_min = 0.02829861111111111
- gp_max_ix_range = 0.0253968253968254
- gp_auc_std = 0.022332251082251082
- hlbr = 0.022287414965986393
- ratio_max_to_9th_ave_peaks = 0.01956569664902998
- coe3[3] = 0.019356511544011544
- gp_max_val_range = 0.01707175925925926
- low_power = 0.014790764790764792
- coe3[2] = 0.012003968253968256
- gp_max_val_std = 0.01111111111111111
- ac_std = 0.007812499999999999
- tdoa_min = 0.00744047619047619
- gp_max_ix_max = 0.003348214285714286
- ratio_max_to_10ms_ave_peaks = 0.0024242424242424255
- tdoa_max = 0.001763668430335099
- coe1[0] = 0.0012400793650793646
- coe1[1] = 0.0
- coe3[0] = 0.0
- coe3[1] = 0.0
- diff_std = 0.0
- diff_auc = 0.0
- gp_max_ix_std = 0.0
- gp_max_ix_min = 0.0
- gp_max_ix_mean = 0.0
- tdoa_std = 0.0
- tdoa_range = 0.0
- tdoa_mean = 0.0

## Evaluation
cv = 8
### robot-1
#### accuracy
- Mean = 0.9462499999999999
- Standard deviation = 0.03425547401511179
- Max = 0.99
- 75% = 0.9724999999999999
- Median = 0.95
- 25% = 0.9325
- Min = 0.88

#### f1
- Mean = 0.8750160281072774
- Standard deviation = 0.06845201737002439
- Max = 0.9743589743589743
- 75% = 0.926031294452347
- Median = 0.8837209302325583
- 25% = 0.8197747183979975
- Min = 0.7599999999999999

#### precision
- Mean = 0.8736513687600644
- Standard deviation = 0.13920112252485975
- Max = 1.0
- 75% = 1.0
- Median = 0.9130434782608696
- 25% = 0.7954911433172303
- Min = 0.6333333333333333

#### recall
- Mean = 0.8999999999999999
- Standard deviation = 0.08291561975888499
- Max = 0.95
- 75% = 0.95
- Median = 0.95
- 25% = 0.8875
- Min = 0.7

#### facing_probas
- Mean = [0.79020833 0.30354167 0.08145833 0.031875   0.02666667]
- Standard deviation = [0.08941336 0.06672101 0.03354555 0.01997285 0.02215789]
- Max = [0.92166667 0.38       0.15333333 0.06333333 0.075     ]
- 75% = [0.85583333 0.35333333 0.09       0.04375    0.03333333]
- Median = [0.79833333 0.32       0.0775     0.03416667 0.025     ]
- 25% = [0.7225     0.28291667 0.05125    0.01416667 0.01041667]
- Min = [0.65       0.18333333 0.04833333 0.005      0.        ]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 76.625 | 3.375 |
| Actual Positive | 2.0 | 18.0 |

### robot-2
#### accuracy
- Mean = 0.8625
- Standard deviation = 0.03596873642484543
- Max = 0.92
- 75% = 0.9
- Median = 0.85
- 25% = 0.83
- Min = 0.82

#### f1
- Mean = 0.6234856017905334
- Standard deviation = 0.17416602182477642
- Max = 0.8333333333333333
- 75% = 0.7135416666666666
- Median = 0.6737588652482269
- 25% = 0.5744416873449132
- Min = 0.2608695652173913

#### precision
- Mean = 0.7124338438192928
- Standard deviation = 0.1523723360638346
- Max = 1.0
- 75% = 0.7648809523809523
- Median = 0.6574675324675325
- 25% = 0.6218323586744638
- Min = 0.5294117647058824

#### recall
- Mean = 0.6625
- Standard deviation = 0.28476964374736297
- Max = 1.0
- 75% = 0.9125
- Median = 0.7
- 25% = 0.5
- Min = 0.15

#### facing_probas
- Mean = [0.50708333 0.70708333 0.27229167 0.073125   0.02979167]
- Standard deviation = [0.08344888 0.11739579 0.05273056 0.04375942 0.02589291]
- Max = [0.63333333 0.85833333 0.36166667 0.15666667 0.07666667]
- 75% = [0.54958333 0.83375    0.31333333 0.09916667 0.04958333]
- Median = [0.51166667 0.67583333 0.27416667 0.0575     0.02583333]
- 25% = [0.48041667 0.65041667 0.22041667 0.0425     0.00625   ]
- Min = [0.32666667 0.51333333 0.20666667 0.02333333 0.        ]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 73.0 | 7.0 |
| Actual Positive | 6.75 | 13.25 |

### robot-3
#### accuracy
- Mean = 0.905
- Standard deviation = 0.03741657386773942
- Max = 0.98
- 75% = 0.915
- Median = 0.9
- 25% = 0.895
- Min = 0.84

#### f1
- Mean = 0.706635551948052
- Standard deviation = 0.17147611554921607
- Max = 0.9500000000000001
- 75% = 0.7906565656565656
- Median = 0.7325396825396826
- 25% = 0.6656249999999999
- Min = 0.33333333333333337

#### precision
- Mean = 0.8642708333333333
- Standard deviation = 0.09197055452320353
- Max = 1.0
- 75% = 0.9249999999999999
- Median = 0.8833333333333333
- 25% = 0.799375
- Min = 0.7083333333333334

#### recall
- Mean = 0.65625
- Standard deviation = 0.2429473965697101
- Max = 0.95
- 75% = 0.875
- Median = 0.65
- 25% = 0.525
- Min = 0.2

#### facing_probas
- Mean = [0.108125   0.76166667 0.86375    0.39479167 0.071875  ]
- Standard deviation = [0.03167146 0.08084622 0.05315563 0.06381091 0.04281288]
- Max = [0.14666667 0.86666667 0.945      0.48166667 0.15      ]
- 75% = [0.14       0.8125     0.91083333 0.43       0.09375   ]
- Median = [0.10666667 0.77416667 0.8575     0.41083333 0.06333333]
- 25% = [0.09375    0.73916667 0.82791667 0.36708333 0.045     ]
- Min = [0.05333333 0.58166667 0.785      0.28666667 0.01666667]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 77.375 | 2.625 |
| Actual Positive | 6.875 | 13.125 |

### robot-4
#### accuracy
- Mean = 0.9337500000000001
- Standard deviation = 0.04151430476353904
- Max = 0.97
- 75% = 0.955
- Median = 0.94
- 25% = 0.9375
- Min = 0.83

#### f1
- Mean = 0.8242901949095787
- Standard deviation = 0.11502057654505268
- Max = 0.9268292682926829
- 75% = 0.8882663150955833
- Median = 0.85
- 25% = 0.828548644338118
- Min = 0.5405405405405405

#### precision
- Mean = 0.8673786181139123
- Standard deviation = 0.12024291174826517
- Max = 1.0
- 75% = 0.9285714285714286
- Median = 0.873015873015873
- 25% = 0.85
- Min = 0.5882352941176471

#### recall
- Mean = 0.79375
- Standard deviation = 0.13792547806696193
- Max = 0.95
- 75% = 0.8625
- Median = 0.85
- 25% = 0.7625000000000001
- Min = 0.5

#### facing_probas
- Mean = [0.03083333 0.09520833 0.59041667 0.82416667 0.37395833]
- Standard deviation = [0.02409472 0.04166198 0.08849729 0.02426703 0.08044122]
- Max = [0.07166667 0.17333333 0.71833333 0.86166667 0.51      ]
- 75% = [0.0425     0.11583333 0.66416667 0.84916667 0.42541667]
- Median = [0.03583333 0.09833333 0.57416667 0.815      0.35083333]
- 25% = [0.00541667 0.06583333 0.53166667 0.805      0.32833333]
- Min = [0.00166667 0.02833333 0.45       0.79166667 0.27166667]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 77.5 | 2.5 |
| Actual Positive | 4.125 | 15.875 |

### robot-5
#### accuracy
- Mean = 0.95625
- Standard deviation = 0.024462982238476146
- Max = 0.99
- 75% = 0.97
- Median = 0.96
- 25% = 0.95
- Min = 0.9

#### f1
- Mean = 0.8783103158103158
- Standard deviation = 0.06892649172439151
- Max = 0.9743589743589743
- 75% = 0.9189189189189189
- Median = 0.888888888888889
- 25% = 0.8571428571428571
- Min = 0.7222222222222223

#### precision
- Mean = 0.9765625
- Standard deviation = 0.062009796353076345
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 1.0
- Min = 0.8125

#### recall
- Mean = 0.8
- Standard deviation = 0.08291561975888498
- Max = 0.95
- 75% = 0.85
- Median = 0.8
- 25% = 0.75
- Min = 0.65

#### facing_probas
- Mean = [0.02291667 0.02770833 0.08125    0.59979167 0.79395833]
- Standard deviation = [0.01879624 0.02328772 0.04376984 0.08096826 0.05316338]
- Max = [0.06       0.075      0.15833333 0.8        0.9       ]
- 75% = [0.02916667 0.04208333 0.09125    0.60375    0.8275    ]
- Median = [0.02583333 0.02333333 0.07333333 0.57833333 0.7825    ]
- 25% = [0.00458333 0.00958333 0.055      0.55541667 0.74958333]
- Min = [0.         0.         0.02666667 0.525      0.735     ]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 79.625 | 0.375 |
| Actual Positive | 4.0 | 16.0 |

### robot-6
#### accuracy
- Mean = 0.7625000000000001
- Standard deviation = 0.050435602504580034
- Max = 0.83
- 75% = 0.8025
- Median = 0.765
- 25% = 0.7375
- Min = 0.66

#### f1
- Mean = 0.8642999088149741
- Standard deviation = 0.03315741706063492
- Max = 0.9071038251366119
- 75% = 0.8904235727440148
- Median = 0.8668464304057524
- 25% = 0.8489136934422962
- Min = 0.7951807228915663

#### precision
- Mean = 1.0
- Standard deviation = 0.0
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 1.0
- Min = 1.0

#### recall
- Mean = 0.7625000000000001
- Standard deviation = 0.050435602504580034
- Max = 0.83
- 75% = 0.8025
- Median = 0.765
- 25% = 0.7375
- Min = 0.66

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
| Actual Positive | 23.75 | 76.25 |

