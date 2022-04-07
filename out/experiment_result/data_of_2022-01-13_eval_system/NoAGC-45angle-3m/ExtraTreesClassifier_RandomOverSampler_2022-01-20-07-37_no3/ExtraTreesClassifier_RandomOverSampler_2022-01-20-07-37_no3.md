# ExtraTreesClassifier_RandomOverSampler_2022-01-20-07-37_no3
## Constants
- CSV_PATH = ../out/csv/experiment
- OUTPUT_PATH = ../out/experiment_result/data_of_2022-01-13_eval_system/NoAGC-45angle-3m
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
- AGC_STATUS = ['NoAGC']

## Loaded CSV
- 2021-12-27_AGC.csv
- 2022-01-10_NoAGC.csv
- 2022-01-13_raspi_48000Hz_w1_N2^12_overlap80.csv

## Estimator
### Type
- resampler = RandomOverSampler
- estimator = ExtraTreesClassifier

### Arguments for hyperparameter search
- resampler = RandomOverSampler
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
	- shrinkage = None
	- n_features_in_ = 36
	- sampling_strategy_ = OrderedDict([(0, 3)])
	- shrinkage_ = None
	- sample_indices_ = [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23
 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47
 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71
 72 73 74 61 29 13]

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
- gp_max_val_mean = 0.13650045064446684
- gp_auc_max = 0.11872875326463918
- gp_auc_min = 0.11317568651494346
- gp_auc_mean = 0.10576677258690562
- gp_max_val_min = 0.08464636577996902
- gp_max_val_max = 0.08160312559339444
- high_power = 0.06176508195608447
- coe1[0] = 0.03601469039672519
- diff_auc = 0.03590900327742433
- srmr = 0.03576836722972971
- coe3[3] = 0.03401594593455336
- low_power = 0.02230658509903793
- coe1[1] = 0.017599099967955025
- tdoa_max = 0.016485130230863336
- diff_std = 0.01332300178454025
- hlbr = 0.010774387366642105
- gp_max_ix_max = 0.009552495992918315
- tdoa_range = 0.008604825908960917
- coe3[2] = 0.007443515002457604
- gp_max_val_range = 0.006308375272162873
- gp_auc_range = 0.006032026721681893
- gp_max_ix_mean = 0.0056647673314339985
- gp_max_ix_range = 0.005604529486108432
- gp_max_val_std = 0.00515986071541627
- ratio_max_to_10ms_ave_peaks = 0.004802481469148137
- gp_auc_std = 0.00471085746947816
- tdoa_std = 0.0044760312151616456
- ac_std = 0.004059829059829059
- ratio_max_to_9th_ave_peaks = 0.001410854940266705
- gp_max_ix_std = 0.0009324009324009316
- tdoa_mean = 0.0008547008547008548
- coe3[0] = 0.0
- coe3[1] = 0.0
- ac_auc = 0.0
- gp_max_ix_min = 0.0
- tdoa_min = 0.0

## Evaluation
cv = 8
### robot-1
#### accuracy
- Mean = 0.99125
- Standard deviation = 0.009270248108869587
- Max = 1.0
- 75% = 1.0
- Median = 0.995
- 25% = 0.98
- Min = 0.98

#### f1
- Mean = 0.9790940766550522
- Standard deviation = 0.022082640350559308
- Max = 1.0
- 75% = 1.0
- Median = 0.9878048780487805
- 25% = 0.9523809523809523
- Min = 0.9523809523809523

#### precision
- Mean = 0.95995670995671
- Standard deviation = 0.0421800330517426
- Max = 1.0
- 75% = 1.0
- Median = 0.9761904761904762
- 25% = 0.9090909090909091
- Min = 0.9090909090909091

#### recall
- Mean = 1.0
- Standard deviation = 0.0
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 1.0
- Min = 1.0

#### facing_probas
- Mean = [0.98354167 0.78145833 0.03645833 0.00166667 0.00104167]
- Standard deviation = [0.01437198 0.03495471 0.02544653 0.00220479 0.00165359]
- Max = [0.99666667 0.85       0.1        0.00666667 0.005     ]
- 75% = [0.99416667 0.79291667 0.03875    0.00208333 0.00166667]
- Median = [9.92500000e-01 7.77500000e-01 2.91666667e-02 8.33333333e-04
 0.00000000e+00]
- 25% = [0.96958333 0.76       0.02083333 0.         0.        ]
- Min = [0.95833333 0.735      0.015      0.         0.        ]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 79.125 | 0.875 |
| Actual Positive | 0.0 | 20.0 |

### robot-2
#### accuracy
- Mean = 0.99125
- Standard deviation = 0.009270248108869587
- Max = 1.0
- 75% = 1.0
- Median = 0.995
- 25% = 0.98
- Min = 0.98

#### f1
- Mean = 0.9770580296896088
- Standard deviation = 0.024385035087169545
- Max = 1.0
- 75% = 1.0
- Median = 0.9871794871794872
- 25% = 0.9473684210526316
- Min = 0.9473684210526316

#### precision
- Mean = 1.0
- Standard deviation = 0.0
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 1.0
- Min = 1.0

#### recall
- Mean = 0.9562499999999999
- Standard deviation = 0.04635124054434789
- Max = 1.0
- 75% = 1.0
- Median = 0.975
- 25% = 0.9
- Min = 0.9

#### facing_probas
- Mean = [0.97625    0.97395833 0.89       0.070625   0.00125   ]
- Standard deviation = [0.02243432 0.01241464 0.05106505 0.06285973 0.00273227]
- Max = [1.         0.99166667 0.97833333 0.22333333 0.00833333]
- 75% = [9.94166667e-01 9.85833333e-01 9.23750000e-01 7.75000000e-02
 4.16666667e-04]
- Median = [0.98416667 0.97083333 0.89416667 0.05666667 0.        ]
- 25% = [0.96375    0.96625    0.84166667 0.03416667 0.        ]
- Min = [0.93333333 0.95333333 0.82166667 0.00833333 0.        ]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 80.0 | 0.0 |
| Actual Positive | 0.875 | 19.125 |

### robot-3
#### accuracy
- Mean = 0.9875
- Standard deviation = 0.012990381056766592
- Max = 1.0
- 75% = 1.0
- Median = 0.99
- 25% = 0.98
- Min = 0.96

#### f1
- Mean = 0.9665429599640126
- Standard deviation = 0.035787185879553964
- Max = 1.0
- 75% = 1.0
- Median = 0.9743589743589743
- 25% = 0.9473684210526316
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
- Mean = 0.9375
- Standard deviation = 0.06495190528383288
- Max = 1.0
- 75% = 1.0
- Median = 0.95
- 25% = 0.9
- Min = 0.8

#### facing_probas
- Mean = [0.16895833 0.91916667 0.97604167 0.906875   0.07104167]
- Standard deviation = [0.06299216 0.03866703 0.02193642 0.04409143 0.05292118]
- Max = [0.27       0.96166667 1.         0.95333333 0.18166667]
- 75% = [0.21416667 0.94625    0.99375    0.94583333 0.09625   ]
- Median = [0.1625     0.9325     0.9825     0.92166667 0.06916667]
- 25% = [0.11458333 0.89708333 0.96625    0.87708333 0.02458333]
- Min = [0.07833333 0.84666667 0.93666667 0.82666667 0.01166667]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 80.0 | 0.0 |
| Actual Positive | 1.25 | 18.75 |

### robot-4
#### accuracy
- Mean = 0.945
- Standard deviation = 0.023979157616563572
- Max = 0.97
- 75% = 0.9624999999999999
- Median = 0.955
- 25% = 0.9275
- Min = 0.9

#### f1
- Mean = 0.8359137355847882
- Standard deviation = 0.0862681709447259
- Max = 0.9230769230769231
- 75% = 0.9007823613086771
- Median = 0.873015873015873
- 25% = 0.7784090909090909
- Min = 0.6666666666666666

#### precision
- Mean = 0.9864766081871346
- Standard deviation = 0.023434605412149787
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 0.9868421052631579
- Min = 0.9444444444444444

#### recall
- Mean = 0.7375
- Standard deviation = 0.13169567191065923
- Max = 0.9
- 75% = 0.85
- Median = 0.775
- 25% = 0.6375
- Min = 0.5

#### facing_probas
- Mean = [6.25000000e-04 2.47916667e-01 9.42083333e-01 9.79375000e-01
 7.88125000e-01]
- Standard deviation = [0.00115995 0.07793226 0.04541284 0.0215048  0.07136291]
- Max = [0.00333333 0.36833333 0.98       0.99833333 0.88333333]
- 75% = [4.16666667e-04 2.92500000e-01 9.75416667e-01 9.97083333e-01
 8.40416667e-01]
- Median = [0.     0.245  0.9725 0.99   0.795 ]
- 25% = [0.         0.215      0.90875    0.96583333 0.74333333]
- Min = [0.         0.135      0.865      0.93833333 0.68333333]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 79.75 | 0.25 |
| Actual Positive | 5.25 | 14.75 |

### robot-5
#### accuracy
- Mean = 0.9975
- Standard deviation = 0.004330127018922197
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 0.9975
- Min = 0.99

#### f1
- Mean = 0.9935897435897436
- Standard deviation = 0.011102889792108196
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 0.9935897435897436
- Min = 0.9743589743589743

#### precision
- Mean = 1.0
- Standard deviation = 0.0
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 1.0
- Min = 1.0

#### recall
- Mean = 0.9875
- Standard deviation = 0.021650635094610987
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 0.9875
- Min = 0.95

#### facing_probas
- Mean = [0.00375    0.003125   0.105625   0.95395833 0.95791667]
- Standard deviation = [0.00462106 0.00385839 0.05625424 0.02995294 0.02601749]
- Max = [0.015      0.01166667 0.22333333 0.985      0.98333333]
- 75% = [0.005      0.00416667 0.13166667 0.97541667 0.97583333]
- Median = [0.00166667 0.00166667 0.08333333 0.96416667 0.96416667]
- 25% = [0.00125    0.         0.06125    0.945      0.95416667]
- Min = [0.         0.         0.05333333 0.89       0.905     ]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 80.0 | 0.0 |
| Actual Positive | 0.25 | 19.75 |

### robot-6
#### accuracy
- Mean = 0.9237500000000001
- Standard deviation = 0.02825663638864326
- Max = 0.96
- 75% = 0.95
- Median = 0.925
- 25% = 0.905
- Min = 0.88

#### f1
- Mean = 0.9601387834087075
- Standard deviation = 0.015325177219622454
- Max = 0.9795918367346939
- 75% = 0.9743589743589743
- Median = 0.960975873050143
- 25% = 0.9501094213136098
- Min = 0.9361702127659575

#### precision
- Mean = 1.0
- Standard deviation = 0.0
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 1.0
- Min = 1.0

#### recall
- Mean = 0.9237500000000001
- Standard deviation = 0.02825663638864326
- Max = 0.96
- 75% = 0.95
- Median = 0.925
- 25% = 0.905
- Min = 0.88

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
| Actual Positive | 7.625 | 92.375 |

