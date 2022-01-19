# ExtraTreesClassifier_SMOTETomek_2022-01-19-23-31_no6
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
	- n_estimators = 70
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
- gp_max_val_min = 0.11506472418948815
- gp_max_val_mean = 0.10830408926545937
- gp_max_val_max = 0.10021361491689312
- gp_auc_max = 0.08994669753351814
- gp_auc_min = 0.085347252700557
- srmr = 0.08272716697193755
- gp_auc_mean = 0.07780672821504325
- high_power = 0.05917109352865213
- diff_std = 0.047942852983223906
- diff_auc = 0.039874439043582455
- gp_max_val_std = 0.01861750927543876
- hlbr = 0.01531706647470194
- gp_max_val_range = 0.013590289834983681
- gp_auc_range = 0.012994495848956093
- gp_auc_std = 0.011751058919329052
- coe1[0] = 0.010579646517383445
- coe1[1] = 0.0098563079458477
- coe3[3] = 0.009739288152817964
- tdoa_min = 0.009271113057416973
- tdoa_range = 0.009118999064857625
- gp_max_ix_min = 0.008663585601429704
- gp_max_ix_range = 0.0069096930968394615
- tdoa_mean = 0.006378162848958061
- gp_max_ix_mean = 0.006370975099446526
- coe3[2] = 0.0062692784606188795
- tdoa_max = 0.005791202143289257
- ac_std = 0.0057515691752144955
- low_power = 0.005049847525216982
- gp_max_ix_std = 0.00485423954689322
- gp_max_ix_max = 0.004399133734195264
- ratio_max_to_9th_ave_peaks = 0.004030229783067649
- ac_auc = 0.004022988505747127
- ratio_max_to_10ms_ave_peaks = 0.0025531631450844737
- tdoa_std = 0.0017214968939106869
- coe3[0] = 0.0
- coe3[1] = 0.0

## Evaluation
cv = 8
### robot-1
#### accuracy
- Mean = 0.9724999999999999
- Standard deviation = 0.019202864369671536
- Max = 0.99
- 75% = 0.99
- Median = 0.98
- 25% = 0.9575
- Min = 0.94

#### f1
- Mean = 0.9375270747376101
- Standard deviation = 0.04130295864698246
- Max = 0.975609756097561
- 75% = 0.975609756097561
- Median = 0.9529211571185479
- 25% = 0.904040404040404
- Min = 0.8695652173913044

#### precision
- Mean = 0.885206641184902
- Standard deviation = 0.07219385458779005
- Max = 0.9523809523809523
- 75% = 0.9523809523809523
- Median = 0.9109730848861284
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
- Mean = [9.95000000e-01 8.70714286e-01 7.72321429e-02 3.48214286e-03
 5.35714286e-04]
- Standard deviation = [0.00242226 0.03451929 0.01654631 0.00243375 0.00092788]
- Max = [0.99928571 0.93142857 0.11357143 0.00714286 0.00285714]
- 75% = [9.96607143e-01 8.94285714e-01 8.21428571e-02 5.89285714e-03
 7.14285714e-04]
- Median = [0.99464286 0.86464286 0.07428571 0.00285714 0.        ]
- 25% = [0.99375    0.85285714 0.06464286 0.00125    0.        ]
- Min = [9.91428571e-01 8.17857143e-01 6.00000000e-02 7.14285714e-04
 0.00000000e+00]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 77.25 | 2.75 |
| Actual Positive | 0.0 | 20.0 |

### robot-2
#### accuracy
- Mean = 0.9724999999999999
- Standard deviation = 0.019202864369671536
- Max = 0.99
- 75% = 0.99
- Median = 0.98
- 25% = 0.9575
- Min = 0.94

#### f1
- Mean = 0.9232394967689086
- Standard deviation = 0.05696742757094957
- Max = 0.9743589743589743
- 75% = 0.9743589743589743
- Median = 0.9466389466389467
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
- Mean = 0.8625
- Standard deviation = 0.09601432184835759
- Max = 0.95
- 75% = 0.95
- Median = 0.8999999999999999
- 25% = 0.7875000000000001
- Min = 0.7

#### facing_probas
- Mean = [0.95357143 0.96330357 0.7925     0.06901786 0.001875  ]
- Standard deviation = [0.0218325  0.01795664 0.06061967 0.03876594 0.00112585]
- Max = [0.98214286 0.99142857 0.87071429 0.13714286 0.00357143]
- 75% = [0.97553571 0.97589286 0.84035714 0.08607143 0.00285714]
- Median = [0.95035714 0.96464286 0.80035714 0.07642857 0.00178571]
- 25% = [0.93678571 0.94892857 0.73964286 0.03517857 0.00125   ]
- Min = [0.925      0.935      0.70857143 0.01857143 0.        ]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 80.0 | 0.0 |
| Actual Positive | 2.75 | 17.25 |

### robot-3
#### accuracy
- Mean = 0.9562499999999999
- Standard deviation = 0.031598061649411334
- Max = 0.99
- 75% = 0.99
- Median = 0.96
- 25% = 0.9325
- Min = 0.91

#### f1
- Mean = 0.8679673689161356
- Standard deviation = 0.10423476472732285
- Max = 0.9743589743589743
- 75% = 0.9743589743589743
- Median = 0.888888888888889
- 25% = 0.7950664136622391
- Min = 0.7096774193548387

#### precision
- Mean = 1.0
- Standard deviation = 0.0
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 1.0
- Min = 1.0

#### recall
- Mean = 0.78125
- Standard deviation = 0.15799030824705668
- Max = 0.95
- 75% = 0.95
- Median = 0.8
- 25% = 0.6625
- Min = 0.55

#### facing_probas
- Mean = [0.31991071 0.98366071 0.98446429 0.96946429 0.04125   ]
- Standard deviation = [0.1095174  0.01475323 0.01829028 0.0116044  0.01154378]
- Max = [0.50571429 0.99714286 0.99928571 0.98357143 0.05714286]
- 75% = [0.39303571 0.99142857 0.99553571 0.98160714 0.05142857]
- Median = [0.3        0.99107143 0.99428571 0.96892857 0.04      ]
- 25% = [0.23875    0.98321429 0.98125    0.96196429 0.03089286]
- Min = [0.17071429 0.95285714 0.94785714 0.95142857 0.02642857]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 80.0 | 0.0 |
| Actual Positive | 4.375 | 15.625 |

### robot-4
#### accuracy
- Mean = 0.93125
- Standard deviation = 0.02027159342528355
- Max = 0.98
- 75% = 0.9325
- Median = 0.925
- 25% = 0.92
- Min = 0.91

#### f1
- Mean = 0.8019772340592775
- Standard deviation = 0.06070871841147086
- Max = 0.9473684210526316
- 75% = 0.8139904610492845
- Median = 0.7886762360446571
- 25% = 0.7550675675675675
- Min = 0.7499999999999999

#### precision
- Mean = 0.9424019607843137
- Standard deviation = 0.07601003533068974
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 0.8700980392156863
- Min = 0.8235294117647058

#### recall
- Mean = 0.70625
- Standard deviation = 0.09164298936634489
- Max = 0.9
- 75% = 0.75
- Median = 0.7
- 25% = 0.6375
- Min = 0.6

#### facing_probas
- Mean = [0.00205357 0.26330357 0.93116071 0.99517857 0.80651786]
- Standard deviation = [0.00232657 0.06480046 0.05125957 0.00351291 0.09375421]
- Max = [0.00714286 0.37428571 0.98857143 1.         0.88642857]
- 75% = [0.00267857 0.29571429 0.95964286 0.99875    0.86982143]
- Median = [0.00107143 0.26964286 0.94607143 0.99428571 0.84142857]
- 25% = [5.35714286e-04 2.38571429e-01 9.27142857e-01 9.92857143e-01
 7.85714286e-01]
- Min = [0.         0.13285714 0.81285714 0.98928571 0.58071429]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 79.0 | 1.0 |
| Actual Positive | 5.875 | 14.125 |

### robot-5
#### accuracy
- Mean = 0.9874999999999999
- Standard deviation = 0.014790199457749053
- Max = 1.0
- 75% = 1.0
- Median = 0.995
- 25% = 0.9775
- Min = 0.96

#### f1
- Mean = 0.9670792422717969
- Standard deviation = 0.03928936068481246
- Max = 1.0
- 75% = 1.0
- Median = 0.9878048780487805
- 25% = 0.9402560455192035
- Min = 0.8947368421052632

#### precision
- Mean = 0.9871031746031746
- Standard deviation = 0.022425901895748657
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 0.9880952380952381
- Min = 0.9444444444444444

#### recall
- Mean = 0.95
- Standard deviation = 0.06614378277661477
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 0.8875
- Min = 0.85

#### facing_probas
- Mean = [6.25000000e-04 2.32142857e-03 1.76250000e-01 9.70535714e-01
 9.75625000e-01]
- Standard deviation = [0.00075233 0.00314914 0.07298112 0.00915255 0.01510777]
- Max = [0.00214286 0.00928571 0.31       0.98642857 0.99142857]
- 75% = [8.92857143e-04 2.50000000e-03 1.97500000e-01 9.75892857e-01
 9.84821429e-01]
- Median = [3.57142857e-04 7.14285714e-04 1.50714286e-01 9.69285714e-01
 9.79285714e-01]
- 25% = [0.00000000e+00 5.35714286e-04 1.29464286e-01 9.64285714e-01
 9.72142857e-01]
- Min = [0.         0.         0.09357143 0.95714286 0.94142857]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 79.75 | 0.25 |
| Actual Positive | 1.0 | 19.0 |

### robot-6
#### accuracy
- Mean = 0.86
- Standard deviation = 0.036742346141747685
- Max = 0.93
- 75% = 0.88
- Median = 0.865
- 25% = 0.8274999999999999
- Min = 0.81

#### f1
- Mean = 0.9243142265303957
- Standard deviation = 0.021112311904368287
- Max = 0.9637305699481865
- 75% = 0.9361702127659575
- Median = 0.9276062331090794
- 25% = 0.9056025941271842
- Min = 0.8950276243093923

#### precision
- Mean = 1.0
- Standard deviation = 0.0
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 1.0
- Min = 1.0

#### recall
- Mean = 0.86
- Standard deviation = 0.036742346141747685
- Max = 0.93
- 75% = 0.88
- Median = 0.865
- 25% = 0.8274999999999999
- Min = 0.81

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
| Actual Positive | 14.0 | 86.0 |

