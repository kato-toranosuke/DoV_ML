# ExtraTreesClassifier_ClusterCentroids_2022-01-18-20-05_no1
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
- gp_auc_mean = 0.1674955971548511
- diff_auc = 0.14330880618168987
- gp_max_val_mean = 0.1185423334651946
- gp_auc_min = 0.09824606032844017
- high_power = 0.09599205633030361
- gp_max_val_max = 0.07685328034646906
- coe1[0] = 0.055778826656121855
- gp_max_val_min = 0.04371106086193242
- coe1[1] = 0.04133936159215618
- diff_std = 0.015080048111368274
- gp_auc_max = 0.014341379754653015
- hlbr = 0.014285714285714282
- srmr = 0.013828022769292932
- gp_max_ix_mean = 0.013196621643826609
- coe3[3] = 0.013115564068800753
- gp_max_ix_max = 0.011472667117828414
- gp_max_val_range = 0.011222633927457594
- coe3[2] = 0.011079320045202082
- ac_auc = 0.009824292528134321
- tdoa_std = 0.0066666666666666645
- ac_std = 0.004637681159420288
- ratio_max_to_9th_ave_peaks = 0.0041025641025641
- gp_max_val_std = 0.004075064369182017
- gp_max_ix_std = 0.0036493971977842915
- tdoa_mean = 0.003225806451612903
- tdoa_max = 0.0024853801169590676
- ratio_max_to_10ms_ave_peaks = 0.0024437927663734115
- low_power = 0.0
- coe3[0] = 0.0
- coe3[1] = 0.0
- gp_max_ix_range = 0.0
- gp_max_ix_min = 0.0
- gp_auc_std = 0.0
- gp_auc_range = 0.0
- tdoa_range = 0.0
- tdoa_min = 0.0

## Evaluation
cv = 8
### robot-1
#### accuracy
- Mean = 0.955
- Standard deviation = 0.02872281323269013
- Max = 1.0
- 75% = 0.97
- Median = 0.965
- 25% = 0.9375
- Min = 0.9

#### f1
- Mean = 0.8963022038360065
- Standard deviation = 0.06940488322053431
- Max = 1.0
- 75% = 0.9302325581395349
- Median = 0.919661733615222
- 25% = 0.8649398704902869
- Min = 0.75

#### precision
- Mean = 0.8377500619348446
- Standard deviation = 0.07998979425887631
- Max = 1.0
- 75% = 0.8695652173913043
- Median = 0.8514492753623188
- 25% = 0.764423076923077
- Min = 0.7407407407407407

#### recall
- Mean = 0.96875
- Standard deviation = 0.08267972847076846
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 1.0
- Min = 0.75

#### facing_probas
- Mean = [0.99401042 0.933125   0.12177083 0.00911458 0.00932292]
- Standard deviation = [0.00553923 0.02251254 0.09042477 0.01001829 0.00868512]
- Max = [1.         0.96458333 0.31916667 0.0325     0.0275    ]
- 75% = [1.        0.945     0.155     0.0103125 0.0134375]
- Median = [0.994375   0.93458333 0.11020833 0.00708333 0.00833333]
- 25% = [0.99020833 0.92364583 0.04260417 0.001875   0.001875  ]
- Min = [0.985      0.88916667 0.0275     0.         0.        ]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 76.125 | 3.875 |
| Actual Positive | 0.625 | 19.375 |

### robot-2
#### accuracy
- Mean = 0.9524999999999999
- Standard deviation = 0.029474565306378975
- Max = 0.99
- 75% = 0.97
- Median = 0.965
- 25% = 0.9375
- Min = 0.89

#### f1
- Mean = 0.868670192199604
- Standard deviation = 0.07940058394908305
- Max = 0.9743589743589743
- 75% = 0.9189189189189189
- Median = 0.9039039039039038
- 25% = 0.8146167557932263
- Min = 0.717948717948718

#### precision
- Mean = 0.9671052631578947
- Standard deviation = 0.08703129312712471
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 1.0
- Min = 0.7368421052631579

#### recall
- Mean = 0.79375
- Standard deviation = 0.09499177595981664
- Max = 0.95
- 75% = 0.85
- Median = 0.825
- 25% = 0.7
- Min = 0.65

#### facing_probas
- Mean = [0.93296875 0.97317708 0.66572917 0.03317708 0.00135417]
- Standard deviation = [0.03765157 0.01585516 0.05972294 0.02930913 0.00186048]
- Max = [0.96958333 0.995      0.72375    0.10166667 0.005     ]
- 75% = [0.95895833 0.98552083 0.71083333 0.03875    0.00270833]
- Median = [0.94395833 0.97625    0.690625   0.02708333 0.        ]
- 25% = [0.9259375  0.96333333 0.63052083 0.00989583 0.        ]
- Min = [0.84666667 0.94333333 0.54708333 0.0075     0.        ]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 79.375 | 0.625 |
| Actual Positive | 4.125 | 15.875 |

### robot-3
#### accuracy
- Mean = 0.9875
- Standard deviation = 0.01299038105676659
- Max = 1.0
- 75% = 1.0
- Median = 0.99
- 25% = 0.9775
- Min = 0.97

#### f1
- Mean = 0.9665718349928877
- Standard deviation = 0.034908652039283165
- Max = 1.0
- 75% = 1.0
- Median = 0.9736842105263158
- 25% = 0.9402560455192035
- Min = 0.9189189189189189

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
- Standard deviation = 0.0649519052838329
- Max = 1.0
- 75% = 1.0
- Median = 0.95
- 25% = 0.8875
- Min = 0.85

#### facing_probas
- Mean = [0.16401042 0.98109375 0.993125   0.95020833 0.0553125 ]
- Standard deviation = [0.04852017 0.01800841 0.00662421 0.01849479 0.04229616]
- Max = [0.2175  1.      1.      0.97    0.13125]
- 75% = [0.19770833 0.9978125  1.         0.9653125  0.08510417]
- Median = [0.17729167 0.984375   0.99458333 0.953125   0.0475    ]
- 25% = [0.14302083 0.97166667 0.98625    0.94270833 0.01614583]
- Min = [0.06291667 0.94708333 0.98416667 0.91166667 0.01291667]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 80.0 | 0.0 |
| Actual Positive | 1.25 | 18.75 |

### robot-4
#### accuracy
- Mean = 0.94
- Standard deviation = 0.014999999999999966
- Max = 0.96
- 75% = 0.9524999999999999
- Median = 0.94
- 25% = 0.9275
- Min = 0.92

#### f1
- Mean = 0.8544179415649249
- Standard deviation = 0.040184984570699564
- Max = 0.9090909090909091
- 75% = 0.8835365853658536
- Median = 0.8571428571428572
- 25% = 0.8333333333333334
- Min = 0.7894736842105262

#### precision
- Mean = 0.827521645021645
- Standard deviation = 0.03822492284473096
- Max = 0.9
- 75% = 0.8392857142857143
- Median = 0.8257575757575758
- 25% = 0.8136363636363637
- Min = 0.76

#### recall
- Mean = 0.8875000000000001
- Standard deviation = 0.0739509972887452
- Max = 1.0
- 75% = 0.9125
- Median = 0.9
- 25% = 0.875
- Min = 0.75

#### facing_probas
- Mean = [0.00369792 0.18708333 0.96692708 0.99588542 0.83171875]
- Standard deviation = [0.00607904 0.05832701 0.02264703 0.00436227 0.06434413]
- Max = [0.01916667 0.3025     0.995      1.         0.9025    ]
- 75% = [0.00385417 0.21552083 0.9871875  1.         0.87604167]
- Median = [0.00125    0.16354167 0.96583333 0.9975     0.846875  ]
- 25% = [0.         0.14083333 0.958125   0.9915625  0.80729167]
- Min = [0.         0.1275     0.92166667 0.99       0.69166667]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 76.25 | 3.75 |
| Actual Positive | 2.25 | 17.75 |

### robot-5
#### accuracy
- Mean = 0.9624999999999999
- Standard deviation = 0.010897247358851694
- Max = 0.98
- 75% = 0.97
- Median = 0.96
- 25% = 0.96
- Min = 0.94

#### f1
- Mean = 0.8955364032763413
- Standard deviation = 0.033804228210008606
- Max = 0.9473684210526316
- 75% = 0.9189189189189189
- Median = 0.888888888888889
- 25% = 0.888888888888889
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
- Mean = 0.8125
- Standard deviation = 0.05448623679425843
- Max = 0.9
- 75% = 0.85
- Median = 0.8
- 25% = 0.8
- Min = 0.7

#### facing_probas
- Mean = [0.00328125 0.0028125  0.241875   0.98984375 0.99411458]
- Standard deviation = [0.00736698 0.00323253 0.05861539 0.01377671 0.00551764]
- Max = [0.0225     0.00875    0.32333333 1.         1.        ]
- 75% = [9.37500000e-04 5.31250000e-03 2.92708333e-01 9.98125000e-01
 9.99062500e-01]
- Median = [0.         0.00125    0.24458333 0.99729167 0.99479167]
- 25% = [0.         0.         0.19239583 0.9871875  0.99177083]
- Min = [0.         0.         0.15708333 0.95791667 0.985     ]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 80.0 | 0.0 |
| Actual Positive | 3.75 | 16.25 |

### robot-6
#### accuracy
- Mean = 0.88
- Standard deviation = 0.025495097567963948
- Max = 0.92
- 75% = 0.8925000000000001
- Median = 0.885
- 25% = 0.8674999999999999
- Min = 0.83

#### f1
- Mean = 0.9359732677630721
- Standard deviation = 0.014524672449194675
- Max = 0.9583333333333334
- 75% = 0.9431913116123642
- Median = 0.9389845772824497
- 25% = 0.9290437582657696
- Min = 0.9071038251366119

#### precision
- Mean = 1.0
- Standard deviation = 0.0
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 1.0
- Min = 1.0

#### recall
- Mean = 0.88
- Standard deviation = 0.025495097567963948
- Max = 0.92
- 75% = 0.8925000000000001
- Median = 0.885
- 25% = 0.8674999999999999
- Min = 0.83

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
| Actual Positive | 12.0 | 88.0 |

