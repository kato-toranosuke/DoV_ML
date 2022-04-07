# ExtraTreesClassifier_SMOTETomek_2022-01-20-04-50_no6
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
	- n_estimators = 50
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
- gp_auc_max = 0.11540251725985874
- gp_max_val_max = 0.11159207911654874
- gp_auc_min = 0.08996064373888962
- gp_max_val_mean = 0.08047413579239299
- hlbr = 0.05576563904804753
- gp_max_ix_std = 0.05518407685323497
- gp_max_ix_range = 0.050181470124564795
- tdoa_range = 0.048080719058472124
- gp_auc_mean = 0.04722094303545918
- gp_max_val_min = 0.046218871544918716
- srmr = 0.03063509176469359
- gp_max_ix_min = 0.029369411938587855
- tdoa_std = 0.027820589108921004
- gp_max_val_std = 0.023381574781954288
- gp_auc_range = 0.021946837314388557
- gp_auc_std = 0.01596893624754991
- high_power = 0.015746617106111055
- gp_max_val_range = 0.013470667985099223
- diff_std = 0.012842937809649554
- tdoa_min = 0.01123000544135138
- coe1[0] = 0.01116173224886836
- tdoa_mean = 0.009721361076199786
- low_power = 0.009312336409110604
- gp_max_ix_mean = 0.009064324361153196
- coe1[1] = 0.0075579331063202046
- ac_auc = 0.007311827956989247
- ratio_max_to_9th_ave_peaks = 0.007089999606128638
- diff_auc = 0.007087978989507004
- coe3[2] = 0.006490921265114814
- ratio_max_to_10ms_ave_peaks = 0.005679782583008389
- ac_std = 0.004966465178446745
- gp_max_ix_max = 0.00464329332241047
- coe3[3] = 0.004025286541415575
- tdoa_max = 0.003392992284633154
- coe3[0] = 0.0
- coe3[1] = 0.0

## Evaluation
cv = 8
### robot-1
#### accuracy
- Mean = 0.98875
- Standard deviation = 0.007806247497998005
- Max = 1.0
- 75% = 0.9924999999999999
- Median = 0.99
- 25% = 0.98
- Min = 0.98

#### f1
- Mean = 0.9716183634508411
- Standard deviation = 0.019915995292695197
- Max = 1.0
- 75% = 0.9817073170731707
- Median = 0.9749843652282677
- 25% = 0.9500000000000001
- Min = 0.9473684210526316

#### precision
- Mean = 0.9755952380952381
- Standard deviation = 0.02441927559138814
- Max = 1.0
- 75% = 1.0
- Median = 0.9761904761904762
- 25% = 0.9517857142857142
- Min = 0.95

#### recall
- Mean = 0.96875
- Standard deviation = 0.03479852726768764
- Max = 1.0
- 75% = 1.0
- Median = 0.975
- 25% = 0.95
- Min = 0.9

#### facing_probas
- Mean = [9.41875e-01 6.79500e-01 8.70000e-02 2.50000e-04 7.50000e-04]
- Standard deviation = [0.03927288 0.12461741 0.06972984 0.00066144 0.00108972]
- Max = [0.984 0.851 0.263 0.002 0.003]
- 75% = [0.96825 0.79175 0.082   0.      0.00125]
- Median = [0.952  0.6815 0.0715 0.     0.    ]
- 25% = [0.92875 0.6085  0.0465  0.      0.     ]
- Min = [0.857 0.489 0.032 0.    0.   ]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 79.5 | 0.5 |
| Actual Positive | 0.625 | 19.375 |

### robot-2
#### accuracy
- Mean = 0.96375
- Standard deviation = 0.009921567416492224
- Max = 0.98
- 75% = 0.97
- Median = 0.965
- 25% = 0.9575
- Min = 0.95

#### f1
- Mean = 0.9109358814481661
- Standard deviation = 0.021475318455150355
- Max = 0.9473684210526316
- 75% = 0.924015009380863
- Median = 0.9118404118404118
- 25% = 0.8995016611295681
- Min = 0.8780487804878048

#### precision
- Mean = 0.9078291083439824
- Standard deviation = 0.06296882595733057
- Max = 1.0
- 75% = 0.9605263157894737
- Median = 0.8841991341991342
- 25% = 0.862012987012987
- Min = 0.8260869565217391

#### recall
- Mean = 0.91875
- Standard deviation = 0.03479852726768762
- Max = 0.95
- 75% = 0.95
- Median = 0.925
- 25% = 0.9
- Min = 0.85

#### facing_probas
- Mean = [0.933375 0.9445   0.912875 0.073    0.029125]
- Standard deviation = [0.01553172 0.01171537 0.01681099 0.04907392 0.01356869]
- Max = [0.951 0.965 0.946 0.192 0.05 ]
- 75% = [0.94825 0.951   0.92    0.077   0.03725]
- Median = [0.938  0.943  0.9125 0.064  0.0315]
- 25% = [0.91675 0.93825 0.90125 0.051   0.0215 ]
- Min = [0.91  0.926 0.891 0.02  0.005]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 78.0 | 2.0 |
| Actual Positive | 1.625 | 18.375 |

### robot-3
#### accuracy
- Mean = 0.8725
- Standard deviation = 0.03561951712193755
- Max = 0.92
- 75% = 0.89
- Median = 0.875
- 25% = 0.8574999999999999
- Min = 0.82

#### f1
- Mean = 0.5072795532354356
- Standard deviation = 0.20782040339006014
- Max = 0.7647058823529412
- 75% = 0.6160714285714286
- Median = 0.544973544973545
- 25% = 0.4343434343434343
- Min = 0.18181818181818182

#### precision
- Mean = 0.9910714285714286
- Standard deviation = 0.02362277956307669
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 1.0
- Min = 0.9285714285714286

#### recall
- Mean = 0.36875
- Standard deviation = 0.1869784412706449
- Max = 0.65
- 75% = 0.45
- Median = 0.375
- 25% = 0.2875
- Min = 0.1

#### facing_probas
- Mean = [0.454375 0.90925  0.928375 0.663    0.2985  ]
- Standard deviation = [0.19183061 0.04110277 0.03905105 0.10378704 0.1590841 ]
- Max = [0.747 0.956 0.992 0.81  0.569]
- 75% = [0.56375 0.94025 0.9525  0.71675 0.33875]
- Median = [0.4375 0.9315 0.932  0.654  0.261 ]
- 25% = [0.27    0.86975 0.9065  0.6215  0.19175]
- Min = [0.236 0.843 0.867 0.477 0.119]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 79.875 | 0.125 |
| Actual Positive | 12.625 | 7.375 |

### robot-4
#### accuracy
- Mean = 0.9675
- Standard deviation = 0.012990381056766592
- Max = 0.99
- 75% = 0.9724999999999999
- Median = 0.97
- 25% = 0.9575
- Min = 0.95

#### f1
- Mean = 0.9117158886093417
- Standard deviation = 0.03886215012747646
- Max = 0.9743589743589743
- 75% = 0.9319640564826701
- Median = 0.920997920997921
- 25% = 0.8809523809523809
- Min = 0.8571428571428571

#### precision
- Mean = 0.981516290726817
- Standard deviation = 0.03374017971778822
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 0.9868421052631579
- Min = 0.9047619047619048

#### recall
- Mean = 0.85625
- Standard deviation = 0.07680128579652816
- Max = 0.95
- 75% = 0.9125
- Median = 0.875
- 25% = 0.7875000000000001
- Min = 0.75

#### facing_probas
- Mean = [0.01575  0.236375 0.829375 0.954    0.90075 ]
- Standard deviation = [0.00965337 0.09883185 0.07793417 0.02405722 0.0289903 ]
- Max = [0.029 0.334 0.952 0.985 0.958]
- 75% = [0.02525 0.30725 0.86325 0.972   0.9165 ]
- Median = [0.012  0.2915 0.824  0.958  0.8945]
- 25% = [0.00975 0.16075 0.77025 0.9445  0.87575]
- Min = [0.001 0.08  0.717 0.909 0.868]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 79.625 | 0.375 |
| Actual Positive | 2.875 | 17.125 |

### robot-5
#### accuracy
- Mean = 0.98625
- Standard deviation = 0.008569568250501312
- Max = 1.0
- 75% = 0.99
- Median = 0.99
- 25% = 0.98
- Min = 0.97

#### f1
- Mean = 0.9659871124810149
- Standard deviation = 0.021821025728948718
- Max = 1.0
- 75% = 0.975609756097561
- Median = 0.975609756097561
- 25% = 0.9517857142857142
- Min = 0.9230769230769231

#### precision
- Mean = 0.9519978924584187
- Standard deviation = 0.022834245305907032
- Max = 1.0
- 75% = 0.9523809523809523
- Median = 0.9523809523809523
- 25% = 0.9493421052631579
- Min = 0.9090909090909091

#### recall
- Mean = 0.98125
- Standard deviation = 0.03479852726768764
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 0.9875
- Min = 0.9

#### facing_probas
- Mean = [0.0295   0.030375 0.101125 0.959375 0.944125]
- Standard deviation = [0.01355544 0.03216729 0.08419685 0.02080828 0.02708061]
- Max = [0.048 0.087 0.286 0.996 0.992]
- 75% = [0.0375  0.052   0.13825 0.9685  0.95925]
- Median = [0.03   0.0195 0.0765 0.9635 0.941 ]
- 25% = [2.400e-02 7.500e-04 3.500e-02 9.390e-01 9.285e-01]
- Min = [0.002 0.    0.023 0.932 0.906]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 79.0 | 1.0 |
| Actual Positive | 0.375 | 19.625 |

### robot-6
#### accuracy
- Mean = 0.8187499999999999
- Standard deviation = 0.04166458328124739
- Max = 0.87
- 75% = 0.845
- Median = 0.83
- 25% = 0.8
- Min = 0.74

#### f1
- Mean = 0.8997571447458763
- Standard deviation = 0.025607463164460338
- Max = 0.9304812834224598
- 75% = 0.915965404394577
- Median = 0.9070711896798853
- 25% = 0.8887848425258296
- Min = 0.8505747126436781

#### precision
- Mean = 1.0
- Standard deviation = 0.0
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 1.0
- Min = 1.0

#### recall
- Mean = 0.8187499999999999
- Standard deviation = 0.04166458328124739
- Max = 0.87
- 75% = 0.845
- Median = 0.83
- 25% = 0.8
- Min = 0.74

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
| Actual Positive | 18.125 | 81.875 |

