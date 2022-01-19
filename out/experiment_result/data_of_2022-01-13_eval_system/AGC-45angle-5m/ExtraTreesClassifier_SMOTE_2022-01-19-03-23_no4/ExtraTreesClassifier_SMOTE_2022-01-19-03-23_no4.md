# ExtraTreesClassifier_SMOTE_2022-01-19-03-23_no4
## Constants
- CSV_PATH = ../out/csv/experiment
- OUTPUT_PATH = ../out/experiment_result/data_of_2022-01-13_eval_system/AGC-45angle-5m
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
- DISTANCE = [5]
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
	- oob_decision_function_ = [[0.02857143 0.97142857]
 [0.         1.        ]
 [0.33333333 0.66666667]
 [0.         1.        ]
 [0.14444444 0.85555556]
 [0.14444444 0.85555556]
 [0.74285714 0.25714286]
 [0.6        0.4       ]
 [0.71428571 0.28571429]
 [1.         0.        ]
 [1.         0.        ]
 [1.         0.        ]
 [1.         0.        ]
 [1.         0.        ]
 [1.         0.        ]
 [0.27777778 0.72222222]
 [0.         1.        ]
 [0.         1.        ]
 [0.         1.        ]
 [0.08333333 0.91666667]
 [0.08333333 0.91666667]
 [0.05       0.95      ]
 [0.05714286 0.94285714]
 [0.08       0.92      ]
 [0.88333333 0.11666667]
 [0.14285714 0.85714286]
 [1.         0.        ]
 [1.         0.        ]
 [1.         0.        ]
 [1.         0.        ]
 [1.         0.        ]
 [1.         0.        ]
 [1.         0.        ]
 [0.33333333 0.66666667]
 [0.10833333 0.89166667]
 [0.12380952 0.87619048]
 [0.03571429 0.96428571]
 [0.04081633 0.95918367]
 [0.21428571 0.78571429]
 [0.0625     0.9375    ]
 [0.         1.        ]
 [0.0952381  0.9047619 ]
 [0.74285714 0.25714286]
 [0.7        0.3       ]
 [0.68888889 0.31111111]
 [1.         0.        ]
 [1.         0.        ]
 [0.64285714 0.35714286]
 [0.7        0.3       ]
 [0.8        0.2       ]
 [0.5        0.5       ]
 [0.         1.        ]
 [0.         1.        ]
 [0.         1.        ]
 [0.         1.        ]
 [0.         1.        ]
 [0.         1.        ]
 [0.03333333 0.96666667]
 [0.         1.        ]
 [0.         1.        ]
 [1.         0.        ]
 [1.         0.        ]
 [1.         0.        ]
 [1.         0.        ]
 [1.         0.        ]
 [1.         0.        ]
 [0.71428571 0.28571429]
 [0.7        0.3       ]
 [0.92857143 0.07142857]
 [0.35510204 0.64489796]
 [0.25714286 0.74285714]
 [0.32142857 0.67857143]
 [0.02857143 0.97142857]
 [0.         1.        ]
 [0.2        0.8       ]
 [0.92857143 0.07142857]
 [1.         0.        ]
 [1.         0.        ]]
	- oob_score_ = 0.9871794871794872

#### Importance of features
- gp_auc_mean = 0.19351120732475835
- coe1[0] = 0.1151893205661528
- gp_auc_min = 0.11056238185255197
- gp_max_val_max = 0.10684094453717127
- gp_max_val_mean = 0.04153423362362392
- srmr = 0.0407592248681602
- gp_max_val_std = 0.04029055690072637
- gp_max_ix_range = 0.040155774128334355
- tdoa_max = 0.03655953576609752
- tdoa_range = 0.03631961259079903
- gp_max_ix_std = 0.03505141513522883
- gp_max_val_min = 0.033990626046200206
- gp_max_ix_mean = 0.03211457151227975
- gp_auc_range = 0.02890316205533597
- tdoa_min = 0.027781800851729425
- diff_auc = 0.02718446601941748
- gp_auc_max = 0.01830790568654646
- gp_max_val_range = 0.016830072713815612
- gp_max_ix_min = 0.011101321585903075
- low_power = 0.0045076282940360625
- high_power = 0.00250423794113114
- hlbr = 0.0
- coe1[1] = 0.0
- coe3[0] = 0.0
- coe3[1] = 0.0
- coe3[2] = 0.0
- coe3[3] = 0.0
- ratio_max_to_10ms_ave_peaks = 0.0
- ratio_max_to_9th_ave_peaks = 0.0
- ac_std = 0.0
- ac_auc = 0.0
- diff_std = 0.0
- gp_max_ix_max = 0.0
- gp_auc_std = 0.0
- tdoa_std = 0.0
- tdoa_mean = 0.0

## Evaluation
cv = 8
### robot-1
#### accuracy
- Mean = 0.975
- Standard deviation = 0.011180339887498959
- Max = 0.99
- 75% = 0.9824999999999999
- Median = 0.975
- 25% = 0.9675
- Min = 0.96

#### f1
- Mean = 0.9415309248796202
- Standard deviation = 0.024678424876971677
- Max = 0.975609756097561
- 75% = 0.9581881533101044
- Median = 0.9401162790697675
- 25% = 0.9249471458773784
- Min = 0.9090909090909091

#### precision
- Mean = 0.8962062394127611
- Standard deviation = 0.04834313923840444
- Max = 0.9523809523809523
- 75% = 0.950595238095238
- Median = 0.8893280632411067
- 25% = 0.8605072463768115
- Min = 0.8333333333333334

#### recall
- Mean = 0.99375
- Standard deviation = 0.016535945694153707
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 1.0
- Min = 0.95

#### facing_probas
- Mean = [0.98916667 0.85983333 0.14560417 0.04877083 0.00820833]
- Standard deviation = [0.00748888 0.04544183 0.04217228 0.02966581 0.00399696]
- Max = [1.         0.9135     0.21166667 0.11475    0.01333333]
- 75% = [0.99375    0.89552083 0.16897917 0.05375    0.0115625 ]
- Median = [0.9895     0.87279167 0.135375   0.04920833 0.007625  ]
- 25% = [0.9815     0.821625   0.12016667 0.035      0.007     ]
- Min = [0.98       0.78283333 0.08       0.00333333 0.        ]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 77.625 | 2.375 |
| Actual Positive | 0.125 | 19.875 |

### robot-2
#### accuracy
- Mean = 0.975
- Standard deviation = 0.011180339887498959
- Max = 0.99
- 75% = 0.9824999999999999
- Median = 0.975
- 25% = 0.9675
- Min = 0.96

#### f1
- Mean = 0.9327127481732744
- Standard deviation = 0.032023536013454576
- Max = 0.9743589743589743
- 75% = 0.9560897435897436
- Median = 0.9331436699857752
- 25% = 0.9114114114114114
- Min = 0.888888888888889

#### precision
- Mean = 0.99375
- Standard deviation = 0.016535945694153707
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 1.0
- Min = 0.95

#### recall
- Mean = 0.88125
- Standard deviation = 0.060917464655056
- Max = 0.95
- 75% = 0.95
- Median = 0.875
- 25% = 0.8375
- Min = 0.8

#### facing_probas
- Mean = [0.91796875 0.92396875 0.75585417 0.18857292 0.00239583]
- Standard deviation = [0.0325804  0.03822689 0.05155813 0.0634486  0.0040705 ]
- Max = [0.95625 0.9825  0.84125 0.275   0.0125 ]
- 75% = [0.93425    0.9583125  0.80341667 0.22708333 0.00333333]
- Median = [0.92583333 0.91925    0.741625   0.19816667 0.        ]
- 25% = [0.912375   0.900125   0.71475    0.15222917 0.        ]
- Min = [0.84833333 0.86166667 0.69333333 0.0815     0.        ]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 79.875 | 0.125 |
| Actual Positive | 2.375 | 17.625 |

### robot-3
#### accuracy
- Mean = 0.9624999999999999
- Standard deviation = 0.02487468592766548
- Max = 0.99
- 75% = 0.9824999999999999
- Median = 0.97
- 25% = 0.945
- Min = 0.92

#### f1
- Mean = 0.8911182315787579
- Standard deviation = 0.07928977460372545
- Max = 0.9743589743589743
- 75% = 0.9541160593792173
- Median = 0.9189189189189189
- 25% = 0.8398268398268398
- Min = 0.7499999999999999

#### precision
- Mean = 1.0
- Standard deviation = 0.0
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 1.0
- Min = 1.0

#### recall
- Mean = 0.8125
- Standard deviation = 0.12437342963832748
- Max = 0.95
- 75% = 0.9125
- Median = 0.85
- 25% = 0.725
- Min = 0.6

#### facing_probas
- Mean = [0.3255625  0.9231756  0.9496875  0.93208333 0.08527083]
- Standard deviation = [0.05452622 0.04443236 0.02272624 0.03587149 0.0360909 ]
- Max = [0.3945     0.99125    0.985      0.975      0.14633333]
- 75% = [0.36460417 0.9449375  0.958125   0.94916667 0.0998125 ]
- Median = [0.33370833 0.91570238 0.9525     0.9425     0.083     ]
- 25% = [0.2925     0.901625   0.94791667 0.92725    0.0690625 ]
- Min = [0.23533333 0.85       0.89833333 0.84666667 0.03283333]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 80.0 | 0.0 |
| Actual Positive | 3.75 | 16.25 |

### robot-4
#### accuracy
- Mean = 0.90625
- Standard deviation = 0.019960899278339134
- Max = 0.94
- 75% = 0.92
- Median = 0.91
- 25% = 0.8875
- Min = 0.88

#### f1
- Mean = 0.738895121287942
- Standard deviation = 0.06758977370023209
- Max = 0.8333333333333334
- 75% = 0.7853658536585366
- Median = 0.760731319554849
- 25% = 0.6798245614035088
- Min = 0.625

#### precision
- Mean = 0.8316518754937873
- Standard deviation = 0.06956802803028814
- Max = 0.9375
- 75% = 0.8667582417582418
- Median = 0.8284313725490196
- 25% = 0.7904761904761906
- Min = 0.7222222222222222

#### recall
- Mean = 0.675
- Standard deviation = 0.10307764064044152
- Max = 0.8
- 75% = 0.7625
- Median = 0.675
- 25% = 0.625
- Min = 0.5

#### facing_probas
- Mean = [0.01283333 0.28285417 0.88446875 0.98675    0.75568899]
- Standard deviation = [0.01400992 0.04821432 0.04433568 0.0113624  0.08289874]
- Max = [0.04666667 0.34266667 0.93833333 0.997      0.87      ]
- 75% = [0.014      0.32258333 0.907875   0.99541667 0.80175   ]
- Median = [0.0075     0.28825    0.890625   0.992      0.77558929]
- 25% = [0.00475    0.25783333 0.8775     0.98116667 0.72058333]
- Min = [0.         0.18733333 0.78466667 0.96666667 0.57833333]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 77.125 | 2.875 |
| Actual Positive | 6.5 | 13.5 |

### robot-5
#### accuracy
- Mean = 0.9674999999999999
- Standard deviation = 0.013919410907075068
- Max = 0.99
- 75% = 0.98
- Median = 0.965
- 25% = 0.9575
- Min = 0.95

#### f1
- Mean = 0.9115894704710494
- Standard deviation = 0.04116380260912662
- Max = 0.9743589743589743
- 75% = 0.9480263157894737
- Median = 0.9089068825910931
- 25% = 0.8809523809523809
- Min = 0.8571428571428571

#### precision
- Mean = 0.9802266081871345
- Standard deviation = 0.025565129242042597
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 0.9493421052631579
- Min = 0.9444444444444444

#### recall
- Mean = 0.85625
- Standard deviation = 0.07680128579652816
- Max = 0.95
- 75% = 0.9125
- Median = 0.875
- 25% = 0.7875000000000001
- Min = 0.75

#### facing_probas
- Mean = [0.00677083 0.00552083 0.23483036 0.94486458 0.91308333]
- Standard deviation = [0.01465126 0.00578758 0.04960619 0.02571937 0.03648849]
- Max = [0.045   0.0175  0.30575 0.98375 0.9625 ]
- 75% = [0.003125   0.00875    0.27925    0.959875   0.93704167]
- Median = [0.         0.00416667 0.23529167 0.94666667 0.92708333]
- 25% = [0.         0.         0.19414881 0.93666667 0.885625  ]
- Min = [0.         0.         0.15533333 0.89033333 0.84833333]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 79.625 | 0.375 |
| Actual Positive | 2.875 | 17.125 |

### robot-6
#### accuracy
- Mean = 0.84375
- Standard deviation = 0.027810744326608735
- Max = 0.88
- 75% = 0.8625
- Median = 0.85
- 25% = 0.8274999999999999
- Min = 0.79

#### f1
- Mean = 0.915005203815251
- Standard deviation = 0.016511886099777606
- Max = 0.9361702127659575
- 75% = 0.9261687079523893
- Median = 0.9188873305282843
- 25% = 0.9056025941271842
- Min = 0.8826815642458101

#### precision
- Mean = 1.0
- Standard deviation = 0.0
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 1.0
- Min = 1.0

#### recall
- Mean = 0.84375
- Standard deviation = 0.027810744326608735
- Max = 0.88
- 75% = 0.8625
- Median = 0.85
- 25% = 0.8274999999999999
- Min = 0.79

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
| Actual Positive | 15.625 | 84.375 |

