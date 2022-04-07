# ExtraTreesClassifier_ClusterCentroids_2022-01-20-11-18_no1
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
- gp_auc_min = 0.1242175956780237
- gp_max_val_max = 0.1081735186131286
- gp_max_val_min = 0.10372425675728653
- gp_auc_mean = 0.09979086883976192
- gp_auc_max = 0.08924225201990574
- gp_max_val_mean = 0.08438280088943202
- high_power = 0.07016263626907153
- srmr = 0.04347181655044038
- diff_std = 0.03381404720291013
- hlbr = 0.02663206889031268
- tdoa_max = 0.025306696197254286
- gp_max_ix_max = 0.02293524427526424
- coe3[3] = 0.02246983608349037
- gp_max_ix_range = 0.02109634160837762
- coe1[0] = 0.016716261085962546
- diff_auc = 0.01532699572043696
- gp_auc_std = 0.012960423884771812
- tdoa_range = 0.012177531329329751
- gp_max_ix_mean = 0.011760312982269676
- gp_max_ix_min = 0.010096778755150158
- tdoa_min = 0.007702812030439055
- coe3[2] = 0.00740311531631263
- coe1[1] = 0.006250546682398996
- low_power = 0.006118233618233615
- tdoa_mean = 0.005726447135854837
- ac_std = 0.0031182658732075265
- ratio_max_to_10ms_ave_peaks = 0.0025589425037507146
- ac_auc = 0.0020868196893489
- gp_auc_range = 0.0013818181818181813
- gp_max_ix_std = 0.0012121067095941472
- ratio_max_to_9th_ave_peaks = 0.0010018389773491817
- tdoa_std = 0.0005478692162109249
- gp_max_val_range = 0.000432900432900433
- coe3[0] = 0.0
- coe3[1] = 0.0
- gp_max_val_std = 0.0

## Evaluation
cv = 8
### robot-1
#### accuracy
- Mean = 0.9674999999999999
- Standard deviation = 0.010897247358851694
- Max = 0.99
- 75% = 0.9724999999999999
- Median = 0.96
- 25% = 0.96
- Min = 0.96

#### f1
- Mean = 0.923295224344572
- Standard deviation = 0.0255113080783847
- Max = 0.975609756097561
- 75% = 0.9357696566998892
- Median = 0.9069264069264069
- 25% = 0.9047619047619048
- Min = 0.9047619047619048

#### precision
- Mean = 0.8773644833427442
- Standard deviation = 0.034255387388222674
- Max = 0.9523809523809523
- 75% = 0.8794466403162056
- Median = 0.8636363636363636
- 25% = 0.8636363636363636
- Min = 0.8333333333333334

#### recall
- Mean = 0.975
- Standard deviation = 0.025000000000000022
- Max = 1.0
- 75% = 1.0
- Median = 0.975
- 25% = 0.95
- Min = 0.95

#### facing_probas
- Mean = [0.94179167 0.73541667 0.031625   0.00496875 0.00325   ]
- Standard deviation = [0.02657014 0.0427796  0.01075129 0.0049627  0.00380332]
- Max = [0.98491667 0.82825    0.04708333 0.01475    0.012     ]
- 75% = [0.9538125  0.74516667 0.04239583 0.00539583 0.00485417]
- Median = [0.93429167 0.73279167 0.02883333 0.00308333 0.001875  ]
- 25% = [9.25333333e-01 7.18354167e-01 2.10000000e-02 2.12500000e-03
 2.50000000e-04]
- Min = [9.08750000e-01 6.65083333e-01 1.98333333e-02 2.50000000e-04
 0.00000000e+00]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 77.25 | 2.75 |
| Actual Positive | 0.5 | 19.5 |

### robot-2
#### accuracy
- Mean = 0.97
- Standard deviation = 0.011180339887498959
- Max = 0.99
- 75% = 0.9724999999999999
- Median = 0.97
- 25% = 0.9675
- Min = 0.95

#### f1
- Mean = 0.9197608539713802
- Standard deviation = 0.029579937463477576
- Max = 0.9743589743589743
- 75% = 0.926031294452347
- Median = 0.9189189189189189
- 25% = 0.9114114114114114
- Min = 0.8717948717948718

#### precision
- Mean = 0.986842105263158
- Standard deviation = 0.03481251725084988
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 1.0
- Min = 0.8947368421052632

#### recall
- Mean = 0.8625
- Standard deviation = 0.04145780987944248
- Max = 0.95
- 75% = 0.8625
- Median = 0.85
- 25% = 0.85
- Min = 0.8

#### facing_probas
- Mean = [0.89364583 0.9553125  0.72926042 0.05619792 0.0015    ]
- Standard deviation = [0.04109883 0.01819072 0.07118001 0.04583015 0.00136613]
- Max = [0.95416667 0.98875    0.865      0.17066667 0.0035    ]
- 75% = [0.92216667 0.96308333 0.76622917 0.06091667 0.0025625 ]
- Median = [0.89070833 0.95316667 0.72333333 0.038875   0.00145833]
- 25% = [0.87008333 0.945125   0.66502083 0.02877083 0.        ]
- Min = [0.82908333 0.92858333 0.64925    0.02008333 0.        ]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 79.75 | 0.25 |
| Actual Positive | 2.75 | 17.25 |

### robot-3
#### accuracy
- Mean = 0.975
- Standard deviation = 0.016583123951777013
- Max = 1.0
- 75% = 0.985
- Median = 0.97
- 25% = 0.96
- Min = 0.96

#### f1
- Mean = 0.9312865497076024
- Standard deviation = 0.046301425795652364
- Max = 1.0
- 75% = 0.9605263157894737
- Median = 0.9181286549707603
- 25% = 0.888888888888889
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
- Mean = 0.875
- Standard deviation = 0.08291561975888498
- Max = 1.0
- 75% = 0.925
- Median = 0.8500000000000001
- 25% = 0.8
- Min = 0.8

#### facing_probas
- Mean = [0.10173958 0.8976875  0.92779167 0.84713542 0.04654167]
- Standard deviation = [0.06477999 0.03769486 0.03685696 0.07177424 0.03300497]
- Max = [0.19708333 0.95916667 0.98858333 0.96883333 0.10341667]
- 75% = [0.16297917 0.91589583 0.94470833 0.88358333 0.07083333]
- Median = [0.08866667 0.89429167 0.92070833 0.82633333 0.03775   ]
- 25% = [0.03875    0.8730625  0.90285417 0.79495833 0.015875  ]
- Min = [0.02975    0.83675    0.87975    0.76991667 0.01375   ]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 80.0 | 0.0 |
| Actual Positive | 2.5 | 17.5 |

### robot-4
#### accuracy
- Mean = 0.915
- Standard deviation = 0.017320508075688766
- Max = 0.94
- 75% = 0.9225000000000001
- Median = 0.92
- 25% = 0.9075
- Min = 0.88

#### f1
- Mean = 0.7372864376689092
- Standard deviation = 0.058010476547475584
- Max = 0.8235294117647058
- 75% = 0.7704991087344029
- Median = 0.7499999999999999
- 25% = 0.704133064516129
- Min = 0.625

#### precision
- Mean = 0.9598214285714286
- Standard deviation = 0.057997545446146055
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 0.9255952380952381
- Min = 0.8333333333333334

#### recall
- Mean = 0.6000000000000001
- Standard deviation = 0.061237243569579436
- Max = 0.7
- 75% = 0.65
- Median = 0.6
- 25% = 0.55
- Min = 0.5

#### facing_probas
- Mean = [0.00272917 0.33878125 0.92622917 0.9666875  0.6505625 ]
- Standard deviation = [0.00235066 0.08571268 0.04021668 0.01826183 0.10276324]
- Max = [0.00791667 0.46066667 0.998      0.99925    0.81033333]
- 75% = [0.0040625  0.40804167 0.9379375  0.9748125  0.7195    ]
- Median = [0.00141667 0.33329167 0.91933333 0.95975    0.626     ]
- 25% = [0.00125    0.27904167 0.89622917 0.95266667 0.57441667]
- Min = [5.00000000e-04 1.99833333e-01 8.77000000e-01 9.47333333e-01
 5.15666667e-01]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 79.5 | 0.5 |
| Actual Positive | 8.0 | 12.0 |

### robot-5
#### accuracy
- Mean = 0.985
- Standard deviation = 0.008660254037844393
- Max = 1.0
- 75% = 0.99
- Median = 0.985
- 25% = 0.98
- Min = 0.97

#### f1
- Mean = 0.9605126381442171
- Standard deviation = 0.023406098654760253
- Max = 1.0
- 75% = 0.9743589743589743
- Median = 0.9608636977058029
- 25% = 0.9473684210526316
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
- Mean = 0.925
- Standard deviation = 0.043301270189221926
- Max = 1.0
- 75% = 0.95
- Median = 0.925
- 25% = 0.9
- Min = 0.85

#### facing_probas
- Mean = [0.00191667 0.00179167 0.09739583 0.9101875  0.89163542]
- Standard deviation = [0.00216025 0.00262434 0.07582824 0.04437787 0.04461864]
- Max = [0.00666667 0.00733333 0.26866667 0.99183333 0.96966667]
- 75% = [0.00225    0.002      0.1055625  0.92172917 0.90397917]
- Median = [1.25000000e-03 5.00000000e-04 7.45000000e-02 8.94791667e-01
 8.69583333e-01]
- 25% = [3.75000000e-04 0.00000000e+00 4.45000000e-02 8.76104167e-01
 8.60208333e-01]
- Min = [0.         0.         0.03108333 0.87025    0.857     ]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 80.0 | 0.0 |
| Actual Positive | 1.5 | 18.5 |

### robot-6
#### accuracy
- Mean = 0.8474999999999999
- Standard deviation = 0.03596873642484541
- Max = 0.91
- 75% = 0.8625
- Median = 0.835
- 25% = 0.8274999999999999
- Min = 0.8

#### f1
- Mean = 0.9170507299556583
- Standard deviation = 0.020820209937523763
- Max = 0.9528795811518325
- 75% = 0.926031294452347
- Median = 0.9100736516987408
- 25% = 0.9056025941271842
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
- Mean = 0.8474999999999999
- Standard deviation = 0.03596873642484541
- Max = 0.91
- 75% = 0.8625
- Median = 0.835
- 25% = 0.8274999999999999
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
| Actual Positive | 15.25 | 84.75 |

