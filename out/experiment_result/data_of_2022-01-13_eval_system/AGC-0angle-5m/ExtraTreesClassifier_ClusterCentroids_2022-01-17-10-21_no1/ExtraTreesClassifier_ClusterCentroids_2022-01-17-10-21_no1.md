# ExtraTreesClassifier_ClusterCentroids_2022-01-17-10-21_no1
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
	- n_estimators = 50
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
	- oob_decision_function_ = [[0.94444444 0.05555556]
 [0.94594595 0.05405405]
 [1.         0.        ]
 [1.         0.        ]
 [0.9375     0.0625    ]
 [0.86206897 0.13793103]
 [0.83870968 0.16129032]
 [0.96666667 0.03333333]
 [0.88       0.12      ]
 [0.67741935 0.32258065]
 [1.         0.        ]
 [0.96551724 0.03448276]
 [0.96428571 0.03571429]
 [0.92307692 0.07692308]
 [0.93333333 0.06666667]
 [0.03448276 0.96551724]
 [0.17241379 0.82758621]
 [0.         1.        ]
 [0.11111111 0.88888889]
 [0.07692308 0.92307692]
 [0.16666667 0.83333333]
 [0.         1.        ]
 [0.03703704 0.96296296]
 [0.08823529 0.91176471]
 [0.04545455 0.95454545]
 [0.         1.        ]
 [0.03125    0.96875   ]
 [0.02702703 0.97297297]
 [0.03571429 0.96428571]
 [0.06896552 0.93103448]]
	- oob_score_ = 1.0

#### Importance of features
- gp_max_val_max = 0.24
- gp_auc_max = 0.12833333333333333
- gp_max_val_mean = 0.12
- gp_auc_mean = 0.12
- hlbr = 0.08
- gp_auc_min = 0.065
- gp_max_val_min = 0.06
- diff_std = 0.055
- diff_auc = 0.04
- srmr = 0.02
- gp_max_ix_mean = 0.02
- tdoa_std = 0.02
- tdoa_min = 0.02
- gp_max_val_std = 0.011666666666666665
- low_power = 0.0
- high_power = 0.0
- coe1[0] = 0.0
- coe1[1] = 0.0
- coe3[0] = 0.0
- coe3[1] = 0.0
- coe3[2] = 0.0
- coe3[3] = 0.0
- ratio_max_to_10ms_ave_peaks = 0.0
- ratio_max_to_9th_ave_peaks = 0.0
- ac_std = 0.0
- ac_auc = 0.0
- gp_max_val_range = 0.0
- gp_max_ix_std = 0.0
- gp_max_ix_range = 0.0
- gp_max_ix_min = 0.0
- gp_max_ix_max = 0.0
- gp_auc_std = 0.0
- gp_auc_range = 0.0
- tdoa_range = 0.0
- tdoa_max = 0.0
- tdoa_mean = 0.0

## Evaluation
cv = 8
### robot-1
#### accuracy
- Mean = 0.96875
- Standard deviation = 0.013635890143294655
- Max = 0.99
- 75% = 0.975
- Median = 0.965
- 25% = 0.96
- Min = 0.95

#### f1
- Mean = 0.9284807805794759
- Standard deviation = 0.02988276541896046
- Max = 0.975609756097561
- 75% = 0.9415768576290414
- Median = 0.919661733615222
- 25% = 0.9090909090909091
- Min = 0.888888888888889

#### precision
- Mean = 0.8679865424430642
- Standard deviation = 0.053002973908173046
- Max = 0.9523809523809523
- 75% = 0.8902691511387163
- Median = 0.8514492753623188
- 25% = 0.8333333333333334
- Min = 0.8

#### recall
- Mean = 1.0
- Standard deviation = 0.0
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 1.0
- Min = 1.0

#### facing_probas
- Mean = [0.93275  0.394875 0.048625 0.028875 0.011375]
- Standard deviation = [0.02791393 0.05387123 0.01089653 0.01274203 0.00823009]
- Max = [0.974 0.464 0.062 0.049 0.025]
- 75% = [0.94925 0.4315  0.05725 0.03625 0.0185 ]
- Median = [0.94   0.4085 0.049  0.028  0.01  ]
- 25% = [0.915   0.37625 0.04575 0.019   0.00375]
- Min = [0.881 0.295 0.025 0.011 0.001]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 76.875 | 3.125 |
| Actual Positive | 0.0 | 20.0 |

### robot-2
#### accuracy
- Mean = 0.93375
- Standard deviation = 0.024968730444297694
- Max = 0.96
- 75% = 0.95
- Median = 0.95
- 25% = 0.915
- Min = 0.89

#### f1
- Mean = 0.8328272868119719
- Standard deviation = 0.05497207338329711
- Max = 0.888888888888889
- 75% = 0.8695788812067882
- Median = 0.861003861003861
- 25% = 0.7976190476190477
- Min = 0.7317073170731706

#### precision
- Mean = 0.8653407014979905
- Standard deviation = 0.11167299329113929
- Max = 1.0
- 75% = 0.9558823529411764
- Median = 0.8836317135549872
- 25% = 0.7613636363636364
- Min = 0.7142857142857143

#### recall
- Mean = 0.8125
- Standard deviation = 0.059947894041408975
- Max = 0.95
- 75% = 0.8125
- Median = 0.8
- 25% = 0.7875000000000001
- Min = 0.75

#### facing_probas
- Mean = [0.678    0.869625 0.3275   0.086    0.01325 ]
- Standard deviation = [0.04480513 0.03400345 0.03185122 0.04328395 0.01032896]
- Max = [0.736 0.918 0.363 0.151 0.032]
- 75% = [0.71925 0.89575 0.34925 0.1125  0.021  ]
- Median = [0.684  0.8675 0.347  0.077  0.0105]
- 25% = [0.6335  0.8425  0.29725 0.05975 0.004  ]
- Min = [0.613 0.825 0.271 0.02  0.001]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 77.125 | 2.875 |
| Actual Positive | 3.75 | 16.25 |

### robot-3
#### accuracy
- Mean = 0.9475
- Standard deviation = 0.02384848003542362
- Max = 0.99
- 75% = 0.9624999999999999
- Median = 0.945
- 25% = 0.93
- Min = 0.91

#### f1
- Mean = 0.8615875893314917
- Standard deviation = 0.06902393942847052
- Max = 0.975609756097561
- 75% = 0.9102787456445993
- Median = 0.8546546546546546
- 25% = 0.8250000000000001
- Min = 0.7428571428571429

#### precision
- Mean = 0.894931961420932
- Standard deviation = 0.060007549307252245
- Max = 0.9523809523809523
- 75% = 0.9384191176470589
- Median = 0.9190476190476191
- 25% = 0.865909090909091
- Min = 0.76

#### recall
- Mean = 0.84375
- Standard deviation = 0.12608900626145006
- Max = 1.0
- 75% = 0.95
- Median = 0.875
- 25% = 0.7375
- Min = 0.65

#### facing_probas
- Mean = [0.059625 0.870875 0.958125 0.574375 0.028125]
- Standard deviation = [0.02033432 0.03554377 0.01405736 0.05351621 0.01106162]
- Max = [0.098 0.919 0.98  0.654 0.047]
- 75% = [0.066   0.88975 0.96625 0.618   0.03225]
- Median = [0.0535 0.878  0.959  0.5765 0.025 ]
- 25% = [0.04525 0.8625  0.95475 0.5315  0.02075]
- Min = [0.039 0.793 0.929 0.494 0.014]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 77.875 | 2.125 |
| Actual Positive | 3.125 | 16.875 |

### robot-4
#### accuracy
- Mean = 0.895
- Standard deviation = 0.030413812651491106
- Max = 0.94
- 75% = 0.9125000000000001
- Median = 0.905
- 25% = 0.87
- Min = 0.84

#### f1
- Mean = 0.7740579029913184
- Standard deviation = 0.05121045463728964
- Max = 0.8571428571428572
- 75% = 0.8065217391304348
- Median = 0.7742117117117118
- 25% = 0.7396745932415519
- Min = 0.6923076923076923

#### precision
- Mean = 0.697010593090408
- Standard deviation = 0.08832113395651
- Max = 0.8235294117647058
- 75% = 0.7526223776223776
- Median = 0.6992857142857143
- 25% = 0.6254480286738351
- Min = 0.5625

#### recall
- Mean = 0.8875
- Standard deviation = 0.07806247497997998
- Max = 0.95
- 75% = 0.95
- Median = 0.9
- 25% = 0.8875
- Min = 0.7

#### facing_probas
- Mean = [0.015625 0.059375 0.732    0.927375 0.45925 ]
- Standard deviation = [0.0100491  0.01651467 0.0395506  0.03261877 0.04183225]
- Max = [0.032 0.087 0.802 0.97  0.531]
- 75% = [0.02225 0.07075 0.76575 0.9505  0.477  ]
- Median = [0.018  0.057  0.7175 0.9295 0.45  ]
- 25% = [0.0065  0.0435  0.708   0.9105  0.43025]
- Min = [0.    0.041 0.674 0.864 0.404]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 71.75 | 8.25 |
| Actual Positive | 2.25 | 17.75 |

### robot-5
#### accuracy
- Mean = 0.9199999999999999
- Standard deviation = 0.032787192621509996
- Max = 0.97
- 75% = 0.9375
- Median = 0.92
- 25% = 0.9025000000000001
- Min = 0.87

#### f1
- Mean = 0.7366084140277689
- Standard deviation = 0.13133064453875518
- Max = 0.9189189189189189
- 75% = 0.8131313131313131
- Median = 0.7487781036168133
- 25% = 0.6751152073732719
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
- Mean = 0.6000000000000001
- Standard deviation = 0.16393596310755001
- Max = 0.85
- 75% = 0.6875
- Median = 0.6000000000000001
- 25% = 0.5125000000000001
- Min = 0.35

#### facing_probas
- Mean = [0.012    0.015625 0.047625 0.771875 0.8895  ]
- Standard deviation = [0.00966954 0.0129994  0.01366508 0.04263636 0.02011219]
- Max = [0.03  0.038 0.074 0.81  0.918]
- 75% = [0.02025 0.0255  0.0525  0.80275 0.8995 ]
- Median = [0.0075 0.014  0.0425 0.7895 0.8935]
- 25% = [0.00525 0.00275 0.03675 0.76125 0.88475]
- Min = [0.001 0.002 0.035 0.686 0.846]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 80.0 | 0.0 |
| Actual Positive | 8.0 | 12.0 |

### robot-6
#### accuracy
- Mean = 0.82875
- Standard deviation = 0.049101298353505886
- Max = 0.88
- 75% = 0.86
- Median = 0.855
- 25% = 0.8075
- Min = 0.73

#### f1
- Mean = 0.9055460892730207
- Standard deviation = 0.030200632619171185
- Max = 0.9361702127659575
- 75% = 0.924731182795699
- Median = 0.9218250508573089
- 25% = 0.8933383001179611
- Min = 0.8439306358381503

#### precision
- Mean = 1.0
- Standard deviation = 0.0
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 1.0
- Min = 1.0

#### recall
- Mean = 0.82875
- Standard deviation = 0.049101298353505886
- Max = 0.88
- 75% = 0.86
- Median = 0.855
- 25% = 0.8075
- Min = 0.73

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
| Actual Positive | 17.125 | 82.875 |

