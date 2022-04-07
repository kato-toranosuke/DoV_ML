# ExtraTreesClassifier_SMOTETomek_2022-01-20-14-56_no6
## Constants
- CSV_PATH = ../out/csv/experiment
- OUTPUT_PATH = ../out/experiment_result/data_of_2022-01-13_eval_system/NoAGC-45angle-5m
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
- AGC_STATUS = ['NoAGC']

## Loaded CSV
- 2021-12-27_AGC.csv
- 2022-01-10_NoAGC.csv
- 2022-01-13_raspi_48000Hz_w1_N2^12_overlap80.csv

## Estimator
### Type
- resampler = SMOTETomek
- estimator = ExtraTreesClassifier

### Arguments for hyperparameter search
- resampler = SMOTETomek
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
	- smote = None
	- tomek = None
	- n_jobs = -1
	- n_features_in_ = 36
	- sampling_strategy_ = auto
	- smote_ = SMOTE(n_jobs=-1, random_state=42)
	- tomek_ = TomekLinks(n_jobs=-1, sampling_strategy='all')

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

#### Importance of features
- gp_auc_mean = 0.33498189724333716
- srmr = 0.126718479888669
- gp_max_val_mean = 0.11190511276718175
- gp_auc_min = 0.09720127085866798
- gp_max_val_min = 0.08838259441707719
- gp_max_val_max = 0.062122647467475076
- gp_auc_max = 0.060973222180118754
- hlbr = 0.017014441497200126
- ratio_max_to_9th_ave_peaks = 0.015357378781873442
- gp_auc_std = 0.013256704980842917
- gp_auc_range = 0.011264367816091954
- tdoa_max = 0.010114942528735632
- high_power = 0.008888888888888892
- coe3[2] = 0.007812876778394023
- ratio_max_to_10ms_ave_peaks = 0.005517241379310344
- gp_max_ix_std = 0.004597701149425288
- gp_max_ix_range = 0.004597701149425288
- tdoa_mean = 0.004597701149425288
- diff_auc = 0.003448275862068966
- diff_std = 0.0032567049808429126
- ac_auc = 0.0031701890989988897
- gp_max_val_std = 0.002758620689655175
- gp_max_ix_max = 0.00206103844629409
- low_power = 0.0
- coe1[0] = 0.0
- coe1[1] = 0.0
- coe3[0] = 0.0
- coe3[1] = 0.0
- coe3[3] = 0.0
- ac_std = 0.0
- gp_max_val_range = 0.0
- gp_max_ix_min = 0.0
- gp_max_ix_mean = 0.0
- tdoa_std = 0.0
- tdoa_range = 0.0
- tdoa_min = 0.0

## Evaluation
cv = 8
### robot-1
#### accuracy
- Mean = 0.97125
- Standard deviation = 0.01763341997458237
- Max = 0.99
- 75% = 0.9824999999999999
- Median = 0.98
- 25% = 0.9575
- Min = 0.94

#### f1
- Mean = 0.9344884230886351
- Standard deviation = 0.0375528456724781
- Max = 0.975609756097561
- 75% = 0.9581881533101044
- Median = 0.9523809523809523
- 25% = 0.904040404040404
- Min = 0.8695652173913044

#### precision
- Mean = 0.8793248418248418
- Standard deviation = 0.06505843629465645
- Max = 0.9523809523809523
- 75% = 0.9199134199134199
- Median = 0.9090909090909091
- 25% = 0.8250000000000001
- Min = 0.7692307692307693

#### recall
- Mean = 1.0
- Standard deviation = 0.0
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 1.0
- Min = 1.0

#### facing_probas
- Mean = [0.9675   0.78125  0.005625 0.00375  0.0025  ]
- Standard deviation = [0.02277608 0.08713316 0.00634306 0.00695971 0.00433013]
- Max = [0.995 0.89  0.015 0.02  0.01 ]
- 75% = [0.97875 0.84875 0.01125 0.0025  0.0025 ]
- Median = [0.9725 0.785  0.0025 0.     0.    ]
- 25% = [0.96375 0.7475  0.      0.      0.     ]
- Min = [0.92  0.595 0.    0.    0.   ]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 77.125 | 2.875 |
| Actual Positive | 0.0 | 20.0 |

### robot-2
#### accuracy
- Mean = 0.97
- Standard deviation = 0.01999999999999999
- Max = 0.99
- 75% = 0.9824999999999999
- Median = 0.98
- 25% = 0.9575
- Min = 0.93

#### f1
- Mean = 0.9155917182232972
- Standard deviation = 0.06162016750706364
- Max = 0.9743589743589743
- 75% = 0.9541160593792173
- Median = 0.9473684210526316
- 25% = 0.8809523809523809
- Min = 0.787878787878788

#### precision
- Mean = 1.0
- Standard deviation = 0.0
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 1.0
- Min = 1.0

#### recall
- Mean = 0.8500000000000001
- Standard deviation = 0.09999999999999998
- Max = 0.95
- 75% = 0.9125
- Median = 0.9
- 25% = 0.7875000000000001
- Min = 0.65

#### facing_probas
- Mean = [9.29375e-01 9.63750e-01 7.80000e-01 5.12500e-02 6.25000e-04]
- Standard deviation = [0.03395194 0.02341874 0.0627495  0.03772847 0.00165359]
- Max = [0.97  0.995 0.87  0.125 0.005]
- 75% = [0.95375 0.98625 0.8375  0.07625 0.     ]
- Median = [0.94   0.965  0.76   0.0425 0.    ]
- 25% = [0.90625 0.93875 0.7425  0.02125 0.     ]
- Min = [0.875 0.935 0.68  0.01  0.   ]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 80.0 | 0.0 |
| Actual Positive | 3.0 | 17.0 |

### robot-3
#### accuracy
- Mean = 0.9824999999999999
- Standard deviation = 0.013919410907075068
- Max = 1.0
- 75% = 0.9924999999999999
- Median = 0.985
- 25% = 0.97
- Min = 0.96

#### f1
- Mean = 0.9535277352992372
- Standard deviation = 0.03804937366375316
- Max = 1.0
- 75% = 0.9817073170731707
- Median = 0.9608636977058029
- 25% = 0.9220374220374221
- Min = 0.888888888888889

#### precision
- Mean = 0.987468671679198
- Standard deviation = 0.021741042071300114
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 0.9880952380952381
- Min = 0.9473684210526315

#### recall
- Mean = 0.925
- Standard deviation = 0.07071067811865475
- Max = 1.0
- 75% = 1.0
- Median = 0.925
- 25% = 0.8875
- Min = 0.8

#### facing_probas
- Mean = [0.126875 0.961875 0.976875 0.92625  0.065625]
- Standard deviation = [0.05595408 0.0210561  0.01579903 0.06208613 0.03803268]
- Max = [0.19  0.99  0.995 0.995 0.12 ]
- 75% = [0.16375 0.975   0.99    0.97    0.09125]
- Median = [0.145  0.97   0.98   0.9425 0.0725]
- 25% = [0.1075  0.95125 0.97125 0.90375 0.03   ]
- Min = [0.03  0.92  0.945 0.825 0.015]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 79.75 | 0.25 |
| Actual Positive | 1.5 | 18.5 |

### robot-4
#### accuracy
- Mean = 0.89
- Standard deviation = 0.043011626335213125
- Max = 0.94
- 75% = 0.915
- Median = 0.895
- 25% = 0.88
- Min = 0.79

#### f1
- Mean = 0.6331901719674286
- Standard deviation = 0.17496112839312974
- Max = 0.8235294117647058
- 75% = 0.7424242424242425
- Median = 0.65625
- 25% = 0.6083743842364533
- Min = 0.2222222222222222

#### precision
- Mean = 0.887706043956044
- Standard deviation = 0.18244538008621183
- Max = 1.0
- 75% = 1.0
- Median = 0.9615384615384616
- 25% = 0.8958333333333333
- Min = 0.42857142857142855

#### recall
- Mean = 0.5
- Standard deviation = 0.1620185174601965
- Max = 0.7
- 75% = 0.6125
- Median = 0.525
- 25% = 0.4375
- Min = 0.15

#### facing_probas
- Mean = [0.00125 0.4325  0.97375 0.99125 0.8175 ]
- Standard deviation = [0.00330719 0.15280707 0.01980372 0.00856957 0.08732125]
- Max = [0.01  0.69  0.995 1.    0.895]
- 75% = [0.      0.5125  0.9875  1.      0.88625]
- Median = [0.     0.4475 0.9775 0.9925 0.855 ]
- 25% = [0.      0.36375 0.965   0.985   0.78125]
- Min = [0.    0.18  0.93  0.975 0.635]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 79.0 | 1.0 |
| Actual Positive | 10.0 | 10.0 |

### robot-5
#### accuracy
- Mean = 0.98875
- Standard deviation = 0.012686114456365286
- Max = 1.0
- 75% = 1.0
- Median = 0.99
- 25% = 0.9875
- Min = 0.96

#### f1
- Mean = 0.9699167791273055
- Standard deviation = 0.03508587193944191
- Max = 1.0
- 75% = 1.0
- Median = 0.9743589743589743
- 25% = 0.9676113360323887
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
- Mean = 0.9437500000000001
- Standard deviation = 0.06343057228182636
- Max = 1.0
- 75% = 1.0
- Median = 0.95
- 25% = 0.9375
- Min = 0.8

#### facing_probas
- Mean = [0.00125  0.       0.163125 0.96     0.9675  ]
- Standard deviation = [0.00330719 0.         0.0972091  0.04616546 0.02926175]
- Max = [0.01 0.   0.38 1.   1.  ]
- 75% = [0.      0.      0.18375 0.99    0.98625]
- Median = [0.     0.     0.15   0.98   0.9825]
- 25% = [0.      0.      0.1     0.95625 0.95   ]
- Min = [0.    0.    0.05  0.865 0.91 ]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 80.0 | 0.0 |
| Actual Positive | 1.125 | 18.875 |

### robot-6
#### accuracy
- Mean = 0.84375
- Standard deviation = 0.044703886855619164
- Max = 0.89
- 75% = 0.8825000000000001
- Median = 0.855
- 25% = 0.8175
- Min = 0.77

#### f1
- Mean = 0.9146072093426183
- Standard deviation = 0.02668962669959219
- Max = 0.9417989417989417
- 75% = 0.9375773950242036
- Median = 0.9217623808416647
- 25% = 0.8994289924479646
- Min = 0.8700564971751412

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
- Standard deviation = 0.044703886855619164
- Max = 0.89
- 75% = 0.8825000000000001
- Median = 0.855
- 25% = 0.8175
- Min = 0.77

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

