# ExtraTreesClassifier_SMOTE_2022-04-13-00-16_no0
## Constants
- CSV_PATH = ../out/csv/experiment
- OUTPUT_PATH = ../out/experiment_result/data_of_2022-03-23_eval_system/AGC-30deg-0angle-3m
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
- AGC_STATUS = ['AGC-30deg']
- ANGLES = [30, 60, 90, 120, 150]

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
	- max_features = log2
	- max_leaf_nodes = None
	- min_impurity_decrease = 0.0
	- ccp_alpha = 0.0
	- n_features_in_ = 36
	- n_outputs_ = 1
	- classes_ = [0 1]
	- n_classes_ = 2
	- base_estimator_ = ExtraTreeClassifier()
	- oob_decision_function_ = [[0.42857143 0.57142857]
 [0.16666667 0.83333333]
 [0.34782609 0.65217391]
 [0.39285714 0.60714286]
 [0.42857143 0.57142857]
 [0.37931034 0.62068966]
 [0.73076923 0.26923077]
 [0.57142857 0.42857143]
 [0.5        0.5       ]
 [0.82758621 0.17241379]
 [0.78571429 0.21428571]
 [0.82758621 0.17241379]
 [0.74074074 0.25925926]
 [0.80769231 0.19230769]
 [0.83333333 0.16666667]
 [0.67857143 0.32142857]
 [0.71428571 0.28571429]
 [0.65517241 0.34482759]
 [0.18518519 0.81481481]
 [0.42307692 0.57692308]
 [0.36666667 0.63333333]
 [0.53571429 0.46428571]
 [0.37931034 0.62068966]
 [0.44444444 0.55555556]
 [0.45454545 0.54545455]
 [0.67857143 0.32142857]
 [0.74074074 0.25925926]
 [0.79310345 0.20689655]
 [0.85714286 0.14285714]
 [0.77777778 0.22222222]
 [0.96666667 0.03333333]
 [0.85714286 0.14285714]
 [0.78571429 0.21428571]
 [0.44827586 0.55172414]
 [0.57142857 0.42857143]
 [0.68965517 0.31034483]
 [0.42307692 0.57692308]
 [0.4137931  0.5862069 ]
 [0.37931034 0.62068966]
 [0.5        0.5       ]
 [0.57692308 0.42307692]
 [0.30434783 0.69565217]
 [0.71428571 0.28571429]
 [0.72       0.28      ]
 [0.63333333 0.36666667]
 [0.92307692 0.07692308]
 [0.875      0.125     ]
 [0.85185185 0.14814815]
 [0.74074074 0.25925926]
 [0.59259259 0.40740741]
 [0.74074074 0.25925926]
 [0.65517241 0.34482759]
 [0.38461538 0.61538462]
 [0.27586207 0.72413793]
 [0.2962963  0.7037037 ]
 [0.23076923 0.76923077]
 [0.30769231 0.69230769]
 [0.24137931 0.75862069]
 [0.17241379 0.82758621]
 [0.20689655 0.79310345]
 [0.84       0.16      ]
 [0.86206897 0.13793103]
 [0.75       0.25      ]
 [0.81481481 0.18518519]
 [0.89655172 0.10344828]
 [0.85714286 0.14285714]
 [0.74074074 0.25925926]
 [0.67857143 0.32142857]
 [0.82758621 0.17241379]
 [0.48148148 0.51851852]
 [0.78571429 0.21428571]
 [0.68       0.32      ]
 [0.11111111 0.88888889]
 [0.33333333 0.66666667]
 [0.42307692 0.57692308]
 [0.25       0.75      ]
 [0.28       0.72      ]
 [0.34615385 0.65384615]
 [0.24137931 0.75862069]
 [0.11111111 0.88888889]
 [0.32142857 0.67857143]
 [0.2        0.8       ]
 [0.20689655 0.79310345]
 [0.30769231 0.69230769]
 [0.07407407 0.92592593]
 [0.17241379 0.82758621]
 [0.32       0.68      ]
 [0.34482759 0.65517241]
 [0.44444444 0.55555556]
 [0.34615385 0.65384615]
 [0.07142857 0.92857143]
 [0.14285714 0.85714286]
 [0.14285714 0.85714286]
 [0.28       0.72      ]
 [0.39285714 0.60714286]
 [0.07407407 0.92592593]
 [0.34482759 0.65517241]
 [0.22222222 0.77777778]
 [0.18518519 0.81481481]
 [0.03571429 0.96428571]
 [0.35714286 0.64285714]
 [0.16       0.84      ]
 [0.22222222 0.77777778]
 [0.08       0.92      ]
 [0.17857143 0.82142857]
 [0.21428571 0.78571429]
 [0.22222222 0.77777778]
 [0.03846154 0.96153846]
 [0.37931034 0.62068966]
 [0.30434783 0.69565217]
 [0.17857143 0.82142857]
 [0.28571429 0.71428571]
 [0.46666667 0.53333333]
 [0.10344828 0.89655172]
 [0.07692308 0.92307692]
 [0.28       0.72      ]
 [0.07692308 0.92307692]
 [0.10344828 0.89655172]
 [0.15384615 0.84615385]
 [0.21428571 0.78571429]]
	- oob_score_ = 0.8833333333333333

#### Importance of features
- gp_auc_max = 0.12670072751322753
- gp_max_val_max = 0.07477358906525575
- gp_max_ix_std = 0.06206018518518519
- gp_max_val_min = 0.059585537918871244
- gp_auc_min = 0.05437169312169313
- gp_max_val_mean = 0.052880291005291014
- tdoa_mean = 0.042645502645502646
- diff_std = 0.03817129629629631
- gp_max_ix_range = 0.03728240740740742
- low_power = 0.03473148148148149
- coe1[1] = 0.032028769841269844
- tdoa_range = 0.03170370370370371
- ac_std = 0.029259259259259266
- gp_auc_mean = 0.029017857142857147
- gp_auc_range = 0.027863756613756615
- tdoa_std = 0.026069223985890663
- gp_max_val_range = 0.024364417989417998
- gp_auc_std = 0.022740740740740745
- ac_auc = 0.02123611111111112
- tdoa_max = 0.02038359788359789
- diff_auc = 0.019917989417989425
- ratio_max_to_9th_ave_peaks = 0.0195408950617284
- coe3[2] = 0.018660714285714287
- gp_max_val_std = 0.01724801587301588
- srmr = 0.017212962962962965
- high_power = 0.010476190476190476
- gp_max_ix_max = 0.009548611111111107
- hlbr = 0.008839285714285716
- coe3[3] = 0.00814814814814815
- coe1[0] = 0.007259259259259266
- ratio_max_to_10ms_ave_peaks = 0.006111111111111111
- gp_max_ix_min = 0.006111111111111111
- tdoa_min = 0.0030555555555555557
- coe3[0] = 0.0
- coe3[1] = 0.0
- gp_max_ix_mean = 0.0

## Evaluation
cv = 8
### robot-1
#### accuracy
- Mean = 0.8825000000000001
- Standard deviation = 0.024366985862022433
- Max = 0.92
- 75% = 0.8975
- Median = 0.875
- 25% = 0.8674999999999999
- Min = 0.85

#### f1
- Mean = 0.7294958516917351
- Standard deviation = 0.05605581965300134
- Max = 0.8181818181818182
- 75% = 0.756728778467909
- Median = 0.7206764866339335
- 25% = 0.7
- Min = 0.65

#### precision
- Mean = 0.6791306451832768
- Standard deviation = 0.06004636093854313
- Max = 0.7727272727272727
- 75% = 0.7401315789473684
- Median = 0.6519230769230769
- 25% = 0.6374074074074074
- Min = 0.6

#### recall
- Mean = 0.79375
- Standard deviation = 0.08076779989575053
- Max = 0.9
- 75% = 0.85
- Median = 0.825
- 25% = 0.7375
- Min = 0.65

#### facing_probas
- Mean = [0.65625    0.39270833 0.22083333 0.14354167 0.13979167]
- Standard deviation = [0.04713861 0.07360243 0.06643188 0.05839543 0.05698707]
- Max = [0.74       0.56       0.36333333 0.22       0.20333333]
- 75% = [0.68833333 0.41916667 0.24916667 0.19083333 0.17958333]
- Median = [0.64583333 0.37083333 0.22       0.155      0.17333333]
- 25% = [0.62833333 0.35583333 0.15791667 0.10416667 0.07875   ]
- Min = [0.58833333 0.29666667 0.15166667 0.02833333 0.055     ]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 72.375 | 7.625 |
| Actual Positive | 4.125 | 15.875 |

### robot-2
#### accuracy
- Mean = 0.79625
- Standard deviation = 0.045808705504521735
- Max = 0.87
- 75% = 0.8274999999999999
- Median = 0.79
- 25% = 0.77
- Min = 0.73

#### f1
- Mean = 0.4846244597220761
- Standard deviation = 0.1280572953597933
- Max = 0.6666666666666667
- 75% = 0.5776843146956951
- Median = 0.4673913043478261
- 25% = 0.4173475801382778
- Min = 0.26666666666666666

#### precision
- Mean = 0.492489670854651
- Standard deviation = 0.11004644994599737
- Max = 0.6842105263157895
- 75% = 0.5740489130434783
- Median = 0.4760348583877996
- 25% = 0.3961538461538462
- Min = 0.34782608695652173

#### recall
- Mean = 0.49375
- Standard deviation = 0.15699820858850588
- Max = 0.7
- 75% = 0.65
- Median = 0.475
- 25% = 0.4
- Min = 0.2

#### facing_probas
- Mean = [0.5875     0.63645833 0.516875   0.34833333 0.17104167]
- Standard deviation = [0.05116015 0.04805551 0.04687037 0.07800463 0.06818041]
- Max = [0.68       0.71333333 0.58166667 0.48666667 0.30833333]
- 75% = [0.61       0.66083333 0.55541667 0.39541667 0.19875   ]
- Median = [0.5725     0.645      0.52166667 0.36166667 0.15833333]
- 25% = [0.55291667 0.6175     0.47291667 0.27833333 0.11458333]
- Min = [0.52       0.54166667 0.45333333 0.235      0.09333333]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 69.75 | 10.25 |
| Actual Positive | 10.125 | 9.875 |

### robot-3
#### accuracy
- Mean = 0.8075
- Standard deviation = 0.034550687402713116
- Max = 0.87
- 75% = 0.8225
- Median = 0.815
- 25% = 0.78
- Min = 0.75

#### f1
- Mean = 0.2851950881362646
- Standard deviation = 0.18189885652037746
- Max = 0.6060606060606061
- 75% = 0.37777777777777777
- Median = 0.3246187363834423
- 25% = 0.1548821548821549
- Min = 0.0

#### precision
- Mean = 0.5282967032967033
- Standard deviation = 0.30817062018236213
- Max = 1.0
- 75% = 0.7280219780219781
- Median = 0.5857142857142856
- 25% = 0.3571428571428571
- Min = 0.0

#### recall
- Mean = 0.21250000000000002
- Standard deviation = 0.15155444566227677
- Max = 0.5
- 75% = 0.3
- Median = 0.225
- 25% = 0.08750000000000001
- Min = 0.0

#### facing_probas
- Mean = [0.47083333 0.62416667 0.59520833 0.566875   0.27916667]
- Standard deviation = [0.05370961 0.04405647 0.02788166 0.04177018 0.09061901]
- Max = [0.54833333 0.69333333 0.64166667 0.63333333 0.49166667]
- 75% = [0.49333333 0.66       0.61416667 0.605      0.29625   ]
- Median = [0.4775     0.62416667 0.59166667 0.55416667 0.25833333]
- 25% = [0.465      0.59208333 0.58083333 0.53625    0.21833333]
- Min = [0.35       0.55333333 0.54666667 0.515      0.18333333]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 76.5 | 3.5 |
| Actual Positive | 15.75 | 4.25 |

### robot-4
#### accuracy
- Mean = 0.78375
- Standard deviation = 0.050233828243525305
- Max = 0.88
- 75% = 0.8125
- Median = 0.78
- 25% = 0.7525
- Min = 0.71

#### f1
- Mean = 0.5467994427124723
- Standard deviation = 0.1131353805949337
- Max = 0.7142857142857143
- 75% = 0.5916666666666668
- Median = 0.555
- 25% = 0.5247368421052632
- Min = 0.2926829268292683

#### precision
- Mean = 0.4772422341172341
- Standard deviation = 0.10773902740237702
- Max = 0.6818181818181818
- 75% = 0.5275000000000001
- Median = 0.4708333333333333
- 25% = 0.4263513513513514
- Min = 0.2857142857142857

#### recall
- Mean = 0.6625000000000001
- Standard deviation = 0.17455300054711176
- Max = 0.95
- 75% = 0.75
- Median = 0.675
- 25% = 0.625
- Min = 0.3

#### facing_probas
- Mean = [0.28020833 0.46541667 0.5775     0.67354167 0.53416667]
- Standard deviation = [0.07295088 0.07750336 0.03567796 0.0353105  0.06657807]
- Max = [0.39166667 0.63666667 0.615      0.74166667 0.7       ]
- 75% = [0.33583333 0.49041667 0.60833333 0.69375    0.53666667]
- Median = [0.28166667 0.44916667 0.58333333 0.67333333 0.52      ]
- 25% = [0.215      0.41958333 0.55791667 0.64666667 0.49625   ]
- Min = [0.18666667 0.36833333 0.50333333 0.62166667 0.46833333]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 65.125 | 14.875 |
| Actual Positive | 6.75 | 13.25 |

### robot-5
#### accuracy
- Mean = 0.85625
- Standard deviation = 0.03276335605520292
- Max = 0.91
- 75% = 0.8775
- Median = 0.85
- 25% = 0.8274999999999999
- Min = 0.82

#### f1
- Mean = 0.4457454194550969
- Standard deviation = 0.2112161895074585
- Max = 0.7111111111111111
- 75% = 0.6774193548387096
- Median = 0.39743589743589747
- 25% = 0.2854545454545455
- Min = 0.18181818181818182

#### precision
- Mean = 0.93
- Standard deviation = 0.12767145334803703
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 0.95
- Min = 0.64

#### recall
- Mean = 0.34375
- Standard deviation = 0.23377005261581307
- Max = 0.8
- 75% = 0.5125
- Median = 0.25
- 25% = 0.17500000000000002
- Min = 0.1

#### facing_probas
- Mean = [0.18354167 0.16791667 0.42       0.645      0.60229167]
- Standard deviation = [0.07491865 0.06086044 0.04972843 0.0529019  0.06271041]
- Max = [0.30833333 0.27       0.50166667 0.73833333 0.715     ]
- 75% = [0.22916667 0.19208333 0.44708333 0.66333333 0.61625   ]
- Median = [0.18166667 0.16583333 0.42333333 0.65       0.57416667]
- 25% = [0.13916667 0.12708333 0.38541667 0.63166667 0.56875   ]
- Min = [0.05333333 0.08166667 0.33833333 0.545      0.53166667]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 78.75 | 1.25 |
| Actual Positive | 13.125 | 6.875 |

### robot-6
#### accuracy
- Mean = 0.50125
- Standard deviation = 0.038222212128551654
- Max = 0.56
- 75% = 0.525
- Median = 0.505
- 25% = 0.475
- Min = 0.44

#### f1
- Mean = 0.6669104173431871
- Standard deviation = 0.034040211627378504
- Max = 0.717948717948718
- 75% = 0.6884825700615175
- Median = 0.6709643235605793
- 25% = 0.644020733061829
- Min = 0.6111111111111112

#### precision
- Mean = 1.0
- Standard deviation = 0.0
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 1.0
- Min = 1.0

#### recall
- Mean = 0.50125
- Standard deviation = 0.038222212128551654
- Max = 0.56
- 75% = 0.525
- Median = 0.505
- 25% = 0.475
- Min = 0.44

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
| Actual Positive | 49.875 | 50.125 |

