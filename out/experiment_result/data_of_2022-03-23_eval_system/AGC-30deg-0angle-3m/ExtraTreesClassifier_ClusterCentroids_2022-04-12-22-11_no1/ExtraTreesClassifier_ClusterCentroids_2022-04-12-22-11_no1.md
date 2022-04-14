# ExtraTreesClassifier_ClusterCentroids_2022-04-12-22-11_no1
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
	- oob_decision_function_ = [[0.125      0.875     ]
 [0.77777778 0.22222222]
 [0.83333333 0.16666667]
 [1.         0.        ]
 [1.         0.        ]
 [0.5        0.5       ]
 [0.85714286 0.14285714]
 [1.         0.        ]
 [0.8        0.2       ]
 [1.         0.        ]
 [1.         0.        ]
 [0.85714286 0.14285714]
 [0.8        0.2       ]
 [0.66666667 0.33333333]
 [0.83333333 0.16666667]
 [0.         1.        ]
 [0.         1.        ]
 [0.         1.        ]
 [0.         1.        ]
 [0.         1.        ]
 [0.14285714 0.85714286]
 [0.66666667 0.33333333]
 [0.2        0.8       ]
 [0.14285714 0.85714286]
 [0.16666667 0.83333333]
 [0.2        0.8       ]
 [0.5        0.5       ]
 [0.         1.        ]
 [0.5        0.5       ]
 [0.42857143 0.57142857]]
	- oob_score_ = 0.8666666666666667

#### Importance of features
- gp_max_val_mean = 0.2
- gp_max_val_max = 0.15558035714285715
- gp_auc_max = 0.15454545454545454
- gp_max_val_min = 0.0765625
- gp_max_ix_min = 0.0765625
- gp_auc_mean = 0.0765625
- gp_max_ix_std = 0.045454545454545456
- gp_max_ix_max = 0.04285714285714285
- hlbr = 0.041558441558441565
- ratio_max_to_10ms_ave_peaks = 0.03683035714285714
- ratio_max_to_9th_ave_peaks = 0.03463203463203463
- ac_std = 0.0234375
- diff_std = 0.01388888888888889
- tdoa_std = 0.011111111111111117
- ac_auc = 0.010416666666666666
- low_power = 0.0
- high_power = 0.0
- coe1[0] = 0.0
- coe1[1] = 0.0
- coe3[0] = 0.0
- coe3[1] = 0.0
- coe3[2] = 0.0
- coe3[3] = 0.0
- diff_auc = 0.0
- srmr = 0.0
- gp_max_val_std = 0.0
- gp_max_val_range = 0.0
- gp_max_ix_range = 0.0
- gp_max_ix_mean = 0.0
- gp_auc_std = 0.0
- gp_auc_range = 0.0
- gp_auc_min = 0.0
- tdoa_range = 0.0
- tdoa_min = 0.0
- tdoa_max = 0.0
- tdoa_mean = 0.0

## Evaluation
cv = 8
### robot-1
#### accuracy
- Mean = 0.8512500000000001
- Standard deviation = 0.05840323193111834
- Max = 0.93
- 75% = 0.9025000000000001
- Median = 0.85
- 25% = 0.8225
- Min = 0.76

#### f1
- Mean = 0.6773688957744686
- Standard deviation = 0.09765996215948938
- Max = 0.8108108108108107
- 75% = 0.7418207681365575
- Median = 0.6927609427609427
- 25% = 0.6472549019607843
- Min = 0.5

#### precision
- Mean = 0.6392918323243276
- Standard deviation = 0.159601391488134
- Max = 0.8823529411764706
- 75% = 0.7892156862745098
- Median = 0.5958333333333333
- 25% = 0.5320208728652751
- Min = 0.42857142857142855

#### recall
- Mean = 0.75
- Standard deviation = 0.1
- Max = 0.95
- 75% = 0.775
- Median = 0.725
- 25% = 0.7
- Min = 0.6

#### facing_probas
- Mean = [0.774375 0.369375 0.220625 0.2125   0.208125]
- Standard deviation = [0.05730606 0.13366089 0.0887566  0.13372079 0.129106  ]
- Max = [0.91  0.675 0.395 0.49  0.4  ]
- 75% = [0.77625 0.40125 0.2625  0.305   0.31125]
- Median = [0.765  0.3425 0.1925 0.1375 0.19  ]
- 25% = [0.74875 0.26625 0.14375 0.12    0.09625]
- Min = [0.715 0.235 0.14  0.085 0.045]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 70.125 | 9.875 |
| Actual Positive | 5.0 | 15.0 |

### robot-2
#### accuracy
- Mean = 0.7749999999999999
- Standard deviation = 0.06224949798994365
- Max = 0.86
- 75% = 0.835
- Median = 0.77
- 25% = 0.72
- Min = 0.68

#### f1
- Mean = 0.4463905659557833
- Standard deviation = 0.1355859030206593
- Max = 0.6666666666666666
- 75% = 0.5174825174825175
- Median = 0.4358974358974359
- 25% = 0.36923583662714093
- Min = 0.23809523809523808

#### precision
- Mean = 0.45467772359219727
- Standard deviation = 0.14405246486117693
- Max = 0.6363636363636364
- 75% = 0.6194331983805668
- Median = 0.40283400809716596
- 25% = 0.36778846153846156
- Min = 0.22727272727272727

#### recall
- Mean = 0.45624999999999993
- Standard deviation = 0.15499495959546553
- Max = 0.7
- 75% = 0.6
- Median = 0.42500000000000004
- 25% = 0.36250000000000004
- Min = 0.25

#### facing_probas
- Mean = [0.759375 0.8075   0.66375  0.260625 0.19125 ]
- Standard deviation = [0.13046641 0.0595294  0.09545123 0.13347372 0.11823573]
- Max = [0.895 0.89  0.775 0.57  0.46 ]
- 75% = [0.8675 0.8475 0.76   0.29   0.22  ]
- Median = [0.795  0.815  0.675  0.2425 0.18  ]
- 25% = [0.705   0.7775  0.5925  0.17375 0.09625]
- Min = [0.54  0.71  0.505 0.095 0.065]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 68.375 | 11.625 |
| Actual Positive | 10.875 | 9.125 |

### robot-3
#### accuracy
- Mean = 0.7424999999999999
- Standard deviation = 0.02436698586202243
- Max = 0.78
- 75% = 0.7625
- Median = 0.74
- 25% = 0.725
- Min = 0.71

#### f1
- Mean = 0.3455453002123491
- Standard deviation = 0.12074572485090201
- Max = 0.5084745762711865
- 75% = 0.4492682926829268
- Median = 0.3493840985442329
- 25% = 0.2571428571428571
- Min = 0.14285714285714288

#### precision
- Mean = 0.3495650183150183
- Standard deviation = 0.06110460351652725
- Max = 0.42857142857142855
- 75% = 0.4
- Median = 0.358974358974359
- 25% = 0.31666666666666665
- Min = 0.25

#### recall
- Mean = 0.38125
- Standard deviation = 0.20757152381769517
- Max = 0.75
- 75% = 0.4875
- Median = 0.375
- 25% = 0.2
- Min = 0.1

#### facing_probas
- Mean = [0.53625  0.768125 0.8225   0.5625   0.20875 ]
- Standard deviation = [0.07498958 0.05899881 0.05662376 0.11355065 0.1432164 ]
- Max = [0.635 0.875 0.92  0.79  0.51 ]
- 75% = [0.6225  0.8075  0.8475  0.61625 0.26375]
- Median = [0.5075 0.7575 0.8125 0.565  0.1875]
- 25% = [0.4825  0.7175  0.80125 0.48    0.09875]
- Min = [0.43  0.695 0.72  0.385 0.045]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 66.625 | 13.375 |
| Actual Positive | 12.375 | 7.625 |

### robot-4
#### accuracy
- Mean = 0.7237499999999999
- Standard deviation = 0.04211220131980754
- Max = 0.79
- 75% = 0.7575000000000001
- Median = 0.71
- 25% = 0.695
- Min = 0.67

#### f1
- Mean = 0.25234831238667554
- Standard deviation = 0.1674961554293185
- Max = 0.47619047619047616
- 75% = 0.37625418060200666
- Median = 0.27922077922077926
- 25% = 0.10252100840336134
- Min = 0.0

#### precision
- Mean = 0.2535973894526526
- Standard deviation = 0.16187707106248458
- Max = 0.47368421052631576
- 75% = 0.36363636363636365
- Median = 0.27884615384615385
- 25% = 0.1238095238095238
- Min = 0.0

#### recall
- Mean = 0.25625
- Standard deviation = 0.1775484088917724
- Max = 0.5
- 75% = 0.41250000000000003
- Median = 0.275
- 25% = 0.08750000000000001
- Min = 0.0

#### facing_probas
- Mean = [0.2425   0.568125 0.80625  0.780625 0.515625]
- Standard deviation = [0.12121778 0.10597575 0.05972594 0.05902529 0.11893899]
- Max = [0.435 0.735 0.905 0.86  0.69 ]
- 75% = [0.3275  0.63375 0.8425  0.825   0.60125]
- Median = [0.2275 0.585  0.7875 0.7775 0.495 ]
- 25% = [0.17375 0.475   0.75375 0.7675  0.46375]
- Min = [0.045 0.415 0.745 0.65  0.285]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 67.25 | 12.75 |
| Actual Positive | 14.875 | 5.125 |

### robot-5
#### accuracy
- Mean = 0.8374999999999999
- Standard deviation = 0.021065374432940872
- Max = 0.86
- 75% = 0.8525
- Median = 0.845
- 25% = 0.825
- Min = 0.8

#### f1
- Mean = 0.3187904124860647
- Standard deviation = 0.14864964851004545
- Max = 0.4615384615384615
- 75% = 0.4153846153846154
- Median = 0.3666666666666667
- 25% = 0.2834782608695653
- Min = 0.0

#### precision
- Mean = 0.8083333333333333
- Standard deviation = 0.3273419890233726
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 0.7666666666666667
- Min = 0.0

#### recall
- Mean = 0.2
- Standard deviation = 0.09682458365518543
- Max = 0.3
- 75% = 0.2625
- Median = 0.225
- 25% = 0.17500000000000002
- Min = 0.0

#### facing_probas
- Mean = [0.251875 0.204375 0.49     0.766875 0.728125]
- Standard deviation = [0.14828051 0.08865091 0.10494046 0.05623264 0.04069225]
- Max = [0.475 0.32  0.615 0.85  0.8  ]
- 75% = [0.355   0.29625 0.59375 0.8     0.76   ]
- Median = [0.235  0.19   0.4875 0.7775 0.71  ]
- 25% = [0.15125 0.12875 0.43    0.74    0.695  ]
- Min = [0.055 0.095 0.295 0.66  0.685]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 79.75 | 0.25 |
| Actual Positive | 16.0 | 4.0 |

### robot-6
#### accuracy
- Mean = 0.40875000000000006
- Standard deviation = 0.04456385867493972
- Max = 0.48
- 75% = 0.45
- Median = 0.405
- 25% = 0.3675
- Min = 0.35

#### f1
- Mean = 0.5788866353419815
- Standard deviation = 0.04474567696770421
- Max = 0.6486486486486487
- 75% = 0.6206896551724138
- Median = 0.5764944275582573
- 25% = 0.5374624302275655
- Min = 0.5185185185185185

#### precision
- Mean = 1.0
- Standard deviation = 0.0
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 1.0
- Min = 1.0

#### recall
- Mean = 0.40875000000000006
- Standard deviation = 0.04456385867493972
- Max = 0.48
- 75% = 0.45
- Median = 0.405
- 25% = 0.3675
- Min = 0.35

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
| Actual Positive | 59.125 | 40.875 |

