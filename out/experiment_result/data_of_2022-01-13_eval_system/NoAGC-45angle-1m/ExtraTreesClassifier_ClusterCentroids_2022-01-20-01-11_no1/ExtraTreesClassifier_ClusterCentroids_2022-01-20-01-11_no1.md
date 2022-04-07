# ExtraTreesClassifier_ClusterCentroids_2022-01-20-01-11_no1
## Constants
- CSV_PATH = ../out/csv/experiment
- OUTPUT_PATH = ../out/experiment_result/data_of_2022-01-13_eval_system/NoAGC-45angle-1m
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
- DISTANCE = [1]
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
	- n_estimators = 150
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
- gp_auc_max = 0.09416690780003839
- gp_max_val_mean = 0.09290268263330544
- gp_auc_mean = 0.08670822846708126
- gp_max_val_min = 0.08638581917165519
- gp_auc_min = 0.07312439432075912
- gp_max_val_max = 0.06488502863038555
- hlbr = 0.038102186278525164
- gp_max_ix_std = 0.036388102747647665
- tdoa_std = 0.03477538503331732
- srmr = 0.034171355069331104
- tdoa_range = 0.029505358982042543
- gp_max_ix_min = 0.025556392385448684
- ratio_max_to_10ms_ave_peaks = 0.02393181816218748
- gp_max_ix_range = 0.023610333185323216
- gp_max_ix_mean = 0.022324824564169392
- diff_auc = 0.021084649004464998
- gp_auc_std = 0.02035804805794257
- diff_std = 0.01978709687781142
- tdoa_min = 0.018565358988789114
- gp_max_val_std = 0.018423250611181382
- gp_max_val_range = 0.017128443228394047
- low_power = 0.014358361024527583
- tdoa_mean = 0.014238149182330961
- high_power = 0.011362907004579502
- coe3[3] = 0.011256979165903125
- coe1[1] = 0.011248159992412866
- gp_auc_range = 0.010935642129720029
- coe3[2] = 0.009342559420359244
- coe1[0] = 0.008731320448065273
- ac_std = 0.008191441953934798
- ac_auc = 0.0049804921190260126
- gp_max_ix_max = 0.004806804790350239
- ratio_max_to_9th_ave_peaks = 0.004376529848752072
- tdoa_max = 0.004284988720237456
- coe3[0] = 0.0
- coe3[1] = 0.0

## Evaluation
cv = 8
### robot-1
#### accuracy
- Mean = 0.98625
- Standard deviation = 0.009921567416492224
- Max = 1.0
- 75% = 0.9924999999999999
- Median = 0.985
- 25% = 0.98
- Min = 0.97

#### f1
- Mean = 0.9653644547579079
- Standard deviation = 0.024601817816953715
- Max = 1.0
- 75% = 0.9807692307692307
- Median = 0.9621794871794872
- 25% = 0.949342105263158
- Min = 0.9268292682926829

#### precision
- Mean = 0.9755952380952381
- Standard deviation = 0.03410563654946855
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 0.95
- Min = 0.9047619047619048

#### recall
- Mean = 0.95625
- Standard deviation = 0.029973947020704494
- Max = 1.0
- 75% = 0.9624999999999999
- Median = 0.95
- 25% = 0.95
- Min = 0.9

#### facing_probas
- Mean = [9.29166667e-01 7.45375000e-01 4.70833333e-02 3.33333333e-04
 6.37500000e-03]
- Standard deviation = [0.04713043 0.09916995 0.0178666  0.00037268 0.00934291]
- Max = [0.97366667 0.89666667 0.068      0.001      0.02366667]
- 75% = [9.72333333e-01 8.18416667e-01 6.45833333e-02 6.66666667e-04
 6.83333333e-03]
- Median = [9.45000000e-01 7.63000000e-01 4.85000000e-02 1.66666667e-04
 1.16666667e-03]
- 25% = [0.90233333 0.65916667 0.03008333 0.         0.00091667]
- Min = [0.84233333 0.60533333 0.02366667 0.         0.        ]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 79.5 | 0.5 |
| Actual Positive | 0.875 | 19.125 |

### robot-2
#### accuracy
- Mean = 0.97
- Standard deviation = 0.012247448713915901
- Max = 0.99
- 75% = 0.98
- Median = 0.97
- 25% = 0.96
- Min = 0.95

#### f1
- Mean = 0.9264499883866917
- Standard deviation = 0.02918595184181972
- Max = 0.9743589743589743
- 75% = 0.9480263157894737
- Median = 0.9285309132161088
- 25% = 0.9035714285714286
- Min = 0.8780487804878048

#### precision
- Mean = 0.9181382928665538
- Standard deviation = 0.05474488461030098
- Max = 1.0
- 75% = 0.9624999999999999
- Median = 0.9023809523809524
- 25% = 0.8680830039525691
- Min = 0.8571428571428571

#### recall
- Mean = 0.9375
- Standard deviation = 0.033071891388307365
- Max = 1.0
- 75% = 0.95
- Median = 0.95
- 25% = 0.9
- Min = 0.9

#### facing_probas
- Mean = [0.93341667 0.95604167 0.89916667 0.05254167 0.022625  ]
- Standard deviation = [0.0191077  0.0153455  0.02025874 0.01864429 0.00659005]
- Max = [0.97133333 0.982      0.93433333 0.08633333 0.035     ]
- 75% = [0.94341667 0.966      0.91658333 0.0665     0.02633333]
- Median = [0.9315     0.9555     0.89       0.04966667 0.02183333]
- 25% = [0.92433333 0.94725    0.88216667 0.04016667 0.01941667]
- Min = [0.90666667 0.93366667 0.878      0.024      0.01133333]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 78.25 | 1.75 |
| Actual Positive | 1.25 | 18.75 |

### robot-3
#### accuracy
- Mean = 0.89
- Standard deviation = 0.0282842712474619
- Max = 0.94
- 75% = 0.905
- Median = 0.89
- 25% = 0.8674999999999999
- Min = 0.85

#### f1
- Mean = 0.6077040461041475
- Standard deviation = 0.13374508256249137
- Max = 0.8235294117647058
- 75% = 0.6875
- Median = 0.6206896551724138
- 25% = 0.5042735042735043
- Min = 0.4

#### precision
- Mean = 1.0
- Standard deviation = 0.0
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 1.0
- Min = 1.0

#### recall
- Mean = 0.45
- Standard deviation = 0.1414213562373095
- Max = 0.7
- 75% = 0.525
- Median = 0.45
- 25% = 0.33749999999999997
- Min = 0.25

#### facing_probas
- Mean = [0.34241667 0.911125   0.914375   0.64441667 0.233625  ]
- Standard deviation = [0.13974051 0.03837387 0.0441646  0.08037114 0.10034641]
- Max = [0.61433333 0.98566667 0.97633333 0.802      0.40233333]
- 75% = [0.41758333 0.933      0.94208333 0.69333333 0.29516667]
- Median = [0.274      0.90383333 0.91666667 0.624      0.18516667]
- 25% = [0.23283333 0.87758333 0.89033333 0.60541667 0.16591667]
- Min = [0.21333333 0.86466667 0.83766667 0.519      0.13133333]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 80.0 | 0.0 |
| Actual Positive | 11.0 | 9.0 |

### robot-4
#### accuracy
- Mean = 0.9562499999999999
- Standard deviation = 0.02117634293262176
- Max = 0.98
- 75% = 0.9724999999999999
- Median = 0.955
- 25% = 0.95
- Min = 0.91

#### f1
- Mean = 0.8739215810523111
- Standard deviation = 0.07129067018453981
- Max = 0.9473684210526316
- 75% = 0.926031294452347
- Median = 0.8768768768768769
- 25% = 0.8571428571428571
- Min = 0.7096774193548387

#### precision
- Mean = 0.9926470588235294
- Standard deviation = 0.019454053757827876
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 1.0
- Min = 0.9411764705882353

#### recall
- Mean = 0.7875000000000001
- Standard deviation = 0.10532687216470447
- Max = 0.9
- 75% = 0.8625
- Median = 0.8
- 25% = 0.75
- Min = 0.55

#### facing_probas
- Mean = [0.00545833 0.21579167 0.76679167 0.93579167 0.8695    ]
- Standard deviation = [0.00238011 0.05886093 0.08966697 0.0340938  0.05512788]
- Max = [0.01066667 0.32033333 0.892      0.97933333 0.93433333]
- 75% = [0.00583333 0.24616667 0.81566667 0.96891667 0.92025   ]
- Median = [0.00516667 0.20816667 0.77666667 0.9325     0.87116667]
- 25% = [0.00383333 0.18875    0.69533333 0.91508333 0.83958333]
- Min = [0.00266667 0.10866667 0.62033333 0.878      0.76066667]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 79.875 | 0.125 |
| Actual Positive | 4.25 | 15.75 |

### robot-5
#### accuracy
- Mean = 0.9824999999999999
- Standard deviation = 0.008291561975888507
- Max = 0.99
- 75% = 0.99
- Median = 0.985
- 25% = 0.9775
- Min = 0.97

#### f1
- Mean = 0.9581606366312833
- Standard deviation = 0.018966559246927233
- Max = 0.975609756097561
- 75% = 0.975609756097561
- Median = 0.9639953542392566
- 25% = 0.9450581395348838
- Min = 0.9302325581395349

#### precision
- Mean = 0.9259681441746659
- Standard deviation = 0.03538272390466288
- Max = 0.9523809523809523
- 75% = 0.9523809523809523
- Median = 0.9511904761904761
- 25% = 0.8992094861660078
- Min = 0.8695652173913043

#### recall
- Mean = 0.99375
- Standard deviation = 0.016535945694153707
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 1.0
- Min = 0.95

#### facing_probas
- Mean = [0.016375   0.01445833 0.08129167 0.96       0.95016667]
- Standard deviation = [0.01316502 0.00938814 0.04238725 0.02945995 0.02429506]
- Max = [0.04033333 0.032      0.14766667 0.99466667 0.98233333]
- 75% = [0.0215     0.01983333 0.12166667 0.97991667 0.97266667]
- Median = [0.017      0.014      0.0705     0.96366667 0.95133333]
- 25% = [0.00408333 0.007      0.0505     0.95041667 0.92475   ]
- Min = [0.001      0.003      0.01633333 0.89533333 0.91933333]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 78.375 | 1.625 |
| Actual Positive | 0.125 | 19.875 |

### robot-6
#### accuracy
- Mean = 0.825
- Standard deviation = 0.03905124837953326
- Max = 0.9
- 75% = 0.8425
- Median = 0.825
- 25% = 0.805
- Min = 0.76

#### f1
- Mean = 0.9036098870824374
- Standard deviation = 0.02336186410317642
- Max = 0.9473684210526316
- 75% = 0.9145123384253819
- Median = 0.9041013631177566
- 25% = 0.8919411092934968
- Min = 0.8636363636363636

#### precision
- Mean = 1.0
- Standard deviation = 0.0
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 1.0
- Min = 1.0

#### recall
- Mean = 0.825
- Standard deviation = 0.03905124837953326
- Max = 0.9
- 75% = 0.8425
- Median = 0.825
- 25% = 0.805
- Min = 0.76

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
| Actual Positive | 17.5 | 82.5 |

