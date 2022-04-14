# ExtraTreesClassifier_SMOTEENN_2022-04-12-20-02_no5
## Constants
- CSV_PATH = ../out/csv/experiment
- OUTPUT_PATH = ../out/experiment_result/data_of_2022-03-23_eval_system/AGC-30deg-0angle-1m
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
- DISTANCE = [1]
- AGC_STATUS = ['AGC-30deg']
- ANGLES = [30, 60, 90, 120, 150]

## Loaded CSV
- 2022-03-23_raspi_48000Hz_w1_N2^12_overlap80_all.csv

## Estimator
### Type
- resampler = SMOTEENN
- estimator = ExtraTreesClassifier

### Arguments for hyperparameter search
- resampler = SMOTEENN
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
	- enn = None
	- n_jobs = -1
	- n_features_in_ = 36
	- sampling_strategy_ = auto
	- smote_ = SMOTE(n_jobs=-1, random_state=42)
	- enn_ = EditedNearestNeighbours(n_jobs=-1, sampling_strategy='all')

- best_estimator
	- base_estimator = ExtraTreeClassifier()
	- n_estimators = 30
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
- gp_auc_min = 0.08256376339709673
- ac_std = 0.06670212375073487
- coe1[0] = 0.060052289960677324
- gp_max_val_range = 0.05774959047071621
- diff_auc = 0.05407794000446979
- coe1[1] = 0.05273112743872978
- gp_auc_range = 0.051566319929846505
- gp_max_val_max = 0.04688783010767661
- gp_auc_std = 0.046399176954732516
- tdoa_max = 0.04504486331569665
- coe3[2] = 0.040800240054869694
- gp_max_ix_range = 0.037117717132337025
- gp_max_val_min = 0.03541187593270926
- gp_max_val_mean = 0.03403880070546738
- tdoa_mean = 0.033917045700671444
- coe3[3] = 0.03293433235867446
- gp_auc_max = 0.026058520142949966
- high_power = 0.024049823633156973
- tdoa_range = 0.023909069325735992
- gp_max_val_std = 0.021846707818930042
- gp_auc_mean = 0.02064973092750871
- ac_auc = 0.019801060118089096
- tdoa_min = 0.01807374338624339
- gp_max_ix_min = 0.01621463477366255
- low_power = 0.013863168724279834
- gp_max_ix_std = 0.009336419753086418
- ratio_max_to_10ms_ave_peaks = 0.007275132275132274
- gp_max_ix_max = 0.004798571541627092
- srmr = 0.004326499118165786
- diff_std = 0.004243827160493827
- ratio_max_to_9th_ave_peaks = 0.0038800705467372134
- tdoa_std = 0.0025462962962962965
- hlbr = 0.0011316872427983538
- coe3[0] = 0.0
- coe3[1] = 0.0
- gp_max_ix_mean = 0.0

## Evaluation
cv = 8
### robot-1
#### accuracy
- Mean = 0.96875
- Standard deviation = 0.015360257159305647
- Max = 0.99
- 75% = 0.9824999999999999
- Median = 0.965
- 25% = 0.9575
- Min = 0.95

#### f1
- Mean = 0.9206741106985905
- Standard deviation = 0.036871795791228124
- Max = 0.9743589743589743
- 75% = 0.9541160593792173
- Median = 0.9039039039039038
- 25% = 0.888888888888889
- Min = 0.8837209302325583

#### precision
- Mean = 0.9532608695652174
- Standard deviation = 0.08121682105748974
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 0.9565217391304348
- Min = 0.8

#### recall
- Mean = 0.8999999999999999
- Standard deviation = 0.07071067811865472
- Max = 1.0
- 75% = 0.95
- Median = 0.925
- 25% = 0.8375
- Min = 0.8

#### facing_probas
- Mean = [0.79875    0.16020833 0.09020833 0.06541667 0.121875  ]
- Standard deviation = [0.08640083 0.12823437 0.07097749 0.05144948 0.05933332]
- Max = [0.985      0.38833333 0.20833333 0.16166667 0.21      ]
- 75% = [0.83291667 0.20083333 0.13166667 0.09958333 0.16      ]
- Median = [0.78       0.1375     0.065      0.05416667 0.12583333]
- 25% = [0.72458333 0.06208333 0.04041667 0.01791667 0.0875    ]
- Min = [0.715      0.02333333 0.01166667 0.00666667 0.03      ]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 78.875 | 1.125 |
| Actual Positive | 2.0 | 18.0 |

### robot-2
#### accuracy
- Mean = 0.855
- Standard deviation = 0.057227615711297995
- Max = 0.93
- 75% = 0.8925000000000001
- Median = 0.875
- 25% = 0.8225
- Min = 0.76

#### f1
- Mean = 0.6033983942694805
- Standard deviation = 0.19151838083194658
- Max = 0.8205128205128205
- 75% = 0.7072649572649573
- Median = 0.65625
- 25% = 0.5727387729285263
- Min = 0.14285714285714288

#### precision
- Mean = 0.6759457024050552
- Standard deviation = 0.21786993905130442
- Max = 0.9166666666666666
- 75% = 0.8355263157894737
- Median = 0.777511961722488
- 25% = 0.5320208728652751
- Min = 0.25

#### recall
- Mean = 0.59375
- Standard deviation = 0.24165768661476503
- Max = 0.95
- 75% = 0.725
- Median = 0.625
- 25% = 0.4875
- Min = 0.1

#### facing_probas
- Mean = [0.31416667 0.73041667 0.66208333 0.239375   0.054375  ]
- Standard deviation = [0.26538363 0.13360064 0.20034475 0.22015925 0.0449918 ]
- Max = [0.89833333 0.97166667 0.95       0.71166667 0.14      ]
- 75% = [0.4425     0.82833333 0.8225     0.35583333 0.07      ]
- Median = [0.22416667 0.68666667 0.665      0.14416667 0.04333333]
- 25% = [0.11041667 0.6125     0.51958333 0.07333333 0.02708333]
- Min = [0.05166667 0.595      0.36833333 0.03833333 0.        ]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 73.625 | 6.375 |
| Actual Positive | 8.125 | 11.875 |

### robot-3
#### accuracy
- Mean = 0.78375
- Standard deviation = 0.03903123748998999
- Max = 0.85
- 75% = 0.805
- Median = 0.785
- 25% = 0.7625
- Min = 0.72

#### f1
- Mean = 0.16996826371826373
- Standard deviation = 0.21120954839875808
- Max = 0.5945945945945946
- 75% = 0.24053030303030304
- Median = 0.08333333333333334
- 25% = 0.0
- Min = 0.0

#### precision
- Mean = 0.3130252100840336
- Standard deviation = 0.3557312687145668
- Max = 1.0
- 75% = 0.5367647058823529
- Median = 0.17857142857142858
- 25% = 0.0
- Min = 0.0

#### recall
- Mean = 0.15625000000000003
- Standard deviation = 0.21713690957550266
- Max = 0.55
- 75% = 0.2
- Median = 0.05
- 25% = 0.0
- Min = 0.0

#### facing_probas
- Mean = [0.19395833 0.458125   0.42270833 0.33208333 0.22541667]
- Standard deviation = [0.21794963 0.25579999 0.27594778 0.25529089 0.2157911 ]
- Max = [0.71833333 0.93333333 0.89666667 0.89166667 0.75333333]
- 75% = [0.235      0.58375    0.60083333 0.39416667 0.24166667]
- Median = [0.0875     0.39583333 0.4        0.29416667 0.16833333]
- 25% = [0.06166667 0.27166667 0.18583333 0.15416667 0.09916667]
- Min = [0.025      0.155      0.08166667 0.04       0.02333333]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 75.25 | 4.75 |
| Actual Positive | 16.875 | 3.125 |

### robot-4
#### accuracy
- Mean = 0.7637499999999999
- Standard deviation = 0.061428311876528065
- Max = 0.85
- 75% = 0.81
- Median = 0.76
- 25% = 0.725
- Min = 0.66

#### f1
- Mean = 0.3919122543737797
- Standard deviation = 0.147756118774469
- Max = 0.6666666666666665
- 75% = 0.42906976744186043
- Median = 0.3514705882352941
- 25% = 0.29017857142857145
- Min = 0.2162162162162162

#### precision
- Mean = 0.41396145414687613
- Standard deviation = 0.13421395875587
- Max = 0.6
- 75% = 0.525
- Median = 0.38928571428571423
- 25% = 0.3233695652173913
- Min = 0.23529411764705882

#### recall
- Mean = 0.39375000000000004
- Standard deviation = 0.17929985359726316
- Max = 0.75
- 75% = 0.45
- Median = 0.35
- 25% = 0.275
- Min = 0.2

#### facing_probas
- Mean = [0.0825     0.18104167 0.21104167 0.590625   0.56270833]
- Standard deviation = [0.08545629 0.24755181 0.25872006 0.18844749 0.21918399]
- Max = [0.26666667 0.81833333 0.84166667 0.955      0.94166667]
- 75% = [0.09708333 0.14458333 0.2275     0.68708333 0.75166667]
- Median = [0.05166667 0.115      0.11166667 0.59333333 0.4875    ]
- 25% = [0.02708333 0.04583333 0.04125    0.41041667 0.37583333]
- Min = [0.00333333 0.01166667 0.00833333 0.36333333 0.31833333]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 68.5 | 11.5 |
| Actual Positive | 12.125 | 7.875 |

### robot-5
#### accuracy
- Mean = 0.7887500000000001
- Standard deviation = 0.04313858481684349
- Max = 0.87
- 75% = 0.8025
- Median = 0.785
- 25% = 0.755
- Min = 0.74

#### f1
- Mean = 0.24653132992327365
- Standard deviation = 0.23168061718533578
- Max = 0.6285714285714286
- 75% = 0.4625
- Median = 0.16112531969309463
- 25% = 0.053571428571428575
- Min = 0.0

#### precision
- Mean = 0.3242559523809524
- Standard deviation = 0.2626679475018626
- Max = 0.7333333333333333
- 75% = 0.5041666666666667
- Median = 0.30952380952380953
- 25% = 0.09375
- Min = 0.0

#### recall
- Mean = 0.21250000000000002
- Standard deviation = 0.20879116360612585
- Max = 0.55
- 75% = 0.41250000000000003
- Median = 0.125
- 25% = 0.037500000000000006
- Min = 0.0

#### facing_probas
- Mean = [0.07333333 0.11479167 0.07145833 0.61979167 0.50770833]
- Standard deviation = [0.06273843 0.19187025 0.12625327 0.18263967 0.23632889]
- Max = [0.185      0.615      0.4        0.94833333 0.98      ]
- 75% = [0.11458333 0.09166667 0.05916667 0.72041667 0.65958333]
- Median = [0.07166667 0.04083333 0.01583333 0.62666667 0.43083333]
- 25% = [0.00916667 0.01791667 0.00916667 0.49666667 0.34      ]
- Min = [0.         0.         0.         0.315      0.19833333]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 74.625 | 5.375 |
| Actual Positive | 15.75 | 4.25 |

### robot-6
#### accuracy
- Mean = 0.45125000000000004
- Standard deviation = 0.09955369154380968
- Max = 0.62
- 75% = 0.5525
- Median = 0.39
- 25% = 0.37
- Min = 0.36

#### f1
- Mean = 0.6156143975859402
- Standard deviation = 0.09134442603381172
- Max = 0.7654320987654321
- 75% = 0.7117452440033085
- Median = 0.5610766045548654
- 25% = 0.5401459854014599
- Min = 0.5294117647058824

#### precision
- Mean = 1.0
- Standard deviation = 0.0
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 1.0
- Min = 1.0

#### recall
- Mean = 0.45125000000000004
- Standard deviation = 0.09955369154380968
- Max = 0.62
- 75% = 0.5525
- Median = 0.39
- 25% = 0.37
- Min = 0.36

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
| Actual Positive | 54.875 | 45.125 |

