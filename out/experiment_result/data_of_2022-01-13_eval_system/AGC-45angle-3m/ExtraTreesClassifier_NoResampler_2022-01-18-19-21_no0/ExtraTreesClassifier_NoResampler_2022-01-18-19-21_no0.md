# ExtraTreesClassifier_NoResampler_2022-01-18-19-21_no0
## Constants
- CSV_PATH = ../out/csv/experiment
- OUTPUT_PATH = ../out/experiment_result/data_of_2022-01-13_eval_system/AGC-45angle-3m
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
- AGC_STATUS = ['AGC']

## Loaded CSV
- 2021-12-27_AGC.csv
- 2022-01-10_NoAGC.csv
- 2022-01-13_raspi_48000Hz_w1_N2^12_overlap80.csv

## Estimator
### Type
- resampler = NoResampler
- estimator = ExtraTreesClassifier

### Arguments for hyperparameter search
- resampler = NoResampler
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

#### Importance of features
- gp_auc_mean = 0.19522839913942508
- gp_auc_min = 0.1516305698948827
- gp_max_val_mean = 0.13164228062206448
- gp_auc_max = 0.08770384426683142
- diff_auc = 0.07889209899156442
- high_power = 0.07210559387430353
- gp_max_val_max = 0.047428286458915975
- coe1[1] = 0.041227318690783304
- coe1[0] = 0.034496872565571005
- ratio_max_to_10ms_ave_peaks = 0.028856077601815945
- tdoa_mean = 0.020381981233072572
- srmr = 0.019093920889794138
- coe3[3] = 0.013941459137592491
- tdoa_std = 0.012366289494837073
- gp_max_val_min = 0.010897069670491555
- gp_max_val_range = 0.010042041315821636
- gp_max_val_std = 0.008219354010145752
- gp_max_ix_max = 0.007900317426183546
- low_power = 0.005751756859585518
- ac_std = 0.005539143279172822
- tdoa_min = 0.0044313146233382564
- gp_auc_std = 0.0031332527639765435
- gp_max_ix_range = 0.0022323500865088423
- tdoa_range = 0.0021404971686768285
- tdoa_max = 0.0018371968711491198
- gp_max_ix_min = 0.0018211869606251322
- gp_max_ix_mean = 0.001059526102870354
- hlbr = 0.0
- coe3[0] = 0.0
- coe3[1] = 0.0
- coe3[2] = 0.0
- ratio_max_to_9th_ave_peaks = 0.0
- ac_auc = 0.0
- diff_std = 0.0
- gp_max_ix_std = 0.0
- gp_auc_range = 0.0

## Evaluation
cv = 8
### robot-1
#### accuracy
- Mean = 0.9575
- Standard deviation = 0.026339134382131833
- Max = 0.98
- 75% = 0.97
- Median = 0.965
- 25% = 0.96
- Min = 0.89

#### f1
- Mean = 0.8852437625192237
- Standard deviation = 0.10119496807802968
- Max = 0.9523809523809523
- 75% = 0.9302325581395349
- Median = 0.919661733615222
- 25% = 0.9068181818181817
- Min = 0.6206896551724138

#### precision
- Mean = 0.8855566534914361
- Standard deviation = 0.05010174576221395
- Max = 1.0
- 75% = 0.9022727272727273
- Median = 0.8695652173913043
- 25% = 0.8605072463768115
- Min = 0.8333333333333334

#### recall
- Mean = 0.91875
- Standard deviation = 0.18016919131749468
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 0.975
- Min = 0.45

#### facing_probas
- Mean = [0.99515625 0.94776042 0.18057292 0.00901042 0.01744792]
- Standard deviation = [0.00452586 0.02425982 0.11337965 0.00713199 0.01667635]
- Max = [1.         0.98083333 0.44041667 0.025      0.055     ]
- 75% = [0.998125   0.96135417 0.20020833 0.0125     0.0196875 ]
- Median = [0.99625    0.95166667 0.15416667 0.006875   0.00895833]
- 25% = [0.99375    0.94270833 0.10125    0.003125   0.0065625 ]
- Min = [0.98625 0.8925  0.0675  0.0025  0.005  ]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 77.375 | 2.625 |
| Actual Positive | 1.625 | 18.375 |

### robot-2
#### accuracy
- Mean = 0.9575
- Standard deviation = 0.026339134382131833
- Max = 0.98
- 75% = 0.97
- Median = 0.965
- 25% = 0.96
- Min = 0.89

#### f1
- Mean = 0.8957770851346702
- Standard deviation = 0.04583272221176606
- Max = 0.9473684210526316
- 75% = 0.9189189189189189
- Median = 0.9094594594594594
- 25% = 0.888888888888889
- Min = 0.7843137254901961

#### precision
- Mean = 0.9431451612903226
- Standard deviation = 0.1172874292112695
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 0.975
- Min = 0.6451612903225806

#### recall
- Mean = 0.86875
- Standard deviation = 0.060917464655056014
- Max = 1.0
- 75% = 0.9
- Median = 0.85
- 25% = 0.8375
- Min = 0.8

#### facing_probas
- Mean = [0.94682292 0.97692708 0.73489583 0.02635417 0.00223958]
- Standard deviation = [0.01181626 0.01211192 0.0618472  0.02380453 0.00381277]
- Max = [0.97       0.99041667 0.83791667 0.07916667 0.01166667]
- 75% = [0.95333333 0.98645833 0.7621875  0.026875   0.0028125 ]
- Median = [0.94520833 0.98041667 0.73895833 0.01729167 0.        ]
- 25% = [0.93895833 0.971875   0.70072917 0.0096875  0.        ]
- Min = [0.93083333 0.955      0.62       0.00833333 0.        ]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 78.375 | 1.625 |
| Actual Positive | 2.625 | 17.375 |

### robot-3
#### accuracy
- Mean = 0.9775
- Standard deviation = 0.012990381056766592
- Max = 1.0
- 75% = 0.9824999999999999
- Median = 0.98
- 25% = 0.9675
- Min = 0.96

#### f1
- Mean = 0.9394740641451168
- Standard deviation = 0.03649660403037961
- Max = 1.0
- 75% = 0.9560897435897436
- Median = 0.9473684210526316
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
- Mean = 0.89375
- Standard deviation = 0.06817945071647319
- Max = 1.0
- 75% = 0.95
- Median = 0.9
- 25% = 0.8375
- Min = 0.8

#### facing_probas
- Mean = [0.1740625  0.99510417 0.99755208 0.97598958 0.07854167]
- Standard deviation = [0.02759355 0.00479506 0.00250379 0.01563047 0.06547702]
- Max = [0.20333333 1.         1.         0.99208333 0.24083333]
- 75% = [0.193125   1.         1.         0.99041667 0.0834375 ]
- Median = [0.18125    0.995      0.998125   0.98020833 0.05583333]
- 25% = [0.1659375 0.99375   0.995     0.9640625 0.0509375]
- Min = [0.11375    0.98583333 0.99416667 0.94666667 0.00666667]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 79.875 | 0.125 |
| Actual Positive | 2.125 | 17.875 |

### robot-4
#### accuracy
- Mean = 0.93375
- Standard deviation = 0.026896793489187495
- Max = 0.96
- 75% = 0.96
- Median = 0.94
- 25% = 0.9175
- Min = 0.88

#### f1
- Mean = 0.8345980122295913
- Standard deviation = 0.0716252473946557
- Max = 0.9047619047619048
- 75% = 0.9047619047619048
- Median = 0.8528708133971292
- 25% = 0.7891891891891893
- Min = 0.7

#### precision
- Mean = 0.824374257278669
- Standard deviation = 0.056921258350706806
- Max = 0.8888888888888888
- 75% = 0.8636363636363636
- Median = 0.8435828877005347
- 25% = 0.7979166666666667
- Min = 0.7

#### recall
- Mean = 0.85
- Standard deviation = 0.10606601717798211
- Max = 0.95
- 75% = 0.95
- Median = 0.875
- 25% = 0.775
- Min = 0.7

#### facing_probas
- Mean = [0.00416667 0.16348958 0.97567708 0.99734375 0.8009375 ]
- Standard deviation = [0.00670562 0.06878722 0.0161763  0.00484991 0.06205108]
- Max = [0.01833333 0.27833333 0.99       1.         0.87833333]
- 75% = [0.005      0.20010417 0.99       1.         0.8634375 ]
- Median = [0.         0.15916667 0.976875   1.         0.795625  ]
- 25% = [0.         0.12125    0.9721875  0.99697917 0.76927083]
- Min = [0.         0.0575     0.93791667 0.985      0.69875   ]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 76.375 | 3.625 |
| Actual Positive | 3.0 | 17.0 |

### robot-5
#### accuracy
- Mean = 0.96375
- Standard deviation = 0.012183492931011215
- Max = 0.98
- 75% = 0.97
- Median = 0.97
- 25% = 0.9575
- Min = 0.94

#### f1
- Mean = 0.8990756568155949
- Standard deviation = 0.037875744797519116
- Max = 0.9473684210526316
- 75% = 0.9189189189189189
- Median = 0.9189189189189189
- 25% = 0.8809523809523809
- Min = 0.8235294117647058

#### precision
- Mean = 1.0
- Standard deviation = 0.0
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 1.0
- Min = 1.0

#### recall
- Mean = 0.81875
- Standard deviation = 0.06091746465505603
- Max = 0.9
- 75% = 0.85
- Median = 0.85
- 25% = 0.7875000000000001
- Min = 0.7

#### facing_probas
- Mean = [0.0034375  0.00307292 0.23546875 0.99453125 0.99651042]
- Standard deviation = [0.00543965 0.00532347 0.05491172 0.00646652 0.00379566]
- Max = [0.015      0.0125     0.32916667 1.         1.        ]
- 75% = [0.004375   0.00302083 0.26625    1.         1.        ]
- Median = [0.         0.         0.23479167 0.99833333 0.996875  ]
- 25% = [0.         0.         0.21427083 0.98875    0.995     ]
- Min = [0.         0.         0.14125    0.98458333 0.98833333]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 80.0 | 0.0 |
| Actual Positive | 3.625 | 16.375 |

### robot-6
#### accuracy
- Mean = 0.87
- Standard deviation = 0.038405728739343024
- Max = 0.91
- 75% = 0.89
- Median = 0.89
- 25% = 0.8625
- Min = 0.8

#### f1
- Mean = 0.9300202592889798
- Standard deviation = 0.022448814290192857
- Max = 0.9528795811518325
- 75% = 0.9417989417989417
- Median = 0.9417989417989417
- 25% = 0.9258845656518162
- Min = 0.888888888888889

#### precision
- Mean = 1.0
- Standard deviation = 0.0
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 1.0
- Min = 1.0

#### recall
- Mean = 0.87
- Standard deviation = 0.038405728739343024
- Max = 0.91
- 75% = 0.89
- Median = 0.89
- 25% = 0.8625
- Min = 0.8

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
| Actual Positive | 13.0 | 87.0 |

