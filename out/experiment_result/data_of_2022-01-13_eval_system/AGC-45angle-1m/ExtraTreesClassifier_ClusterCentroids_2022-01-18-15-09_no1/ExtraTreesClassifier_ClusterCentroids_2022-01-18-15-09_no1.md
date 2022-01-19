# ExtraTreesClassifier_ClusterCentroids_2022-01-18-15-09_no1
## Constants
- CSV_PATH = ../out/csv/experiment
- OUTPUT_PATH = ../out/experiment_result/data_of_2022-01-13_eval_system/AGC-45angle-1m
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
	- sampling_strategy_ = OrderedDict([(1, 34)])
	- estimator_ = KMeans(n_clusters=34, random_state=42)
	- voting_ = soft

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
- gp_auc_max = 0.16788369235551032
- gp_auc_min = 0.08984448621308147
- gp_max_val_mean = 0.0856017404044858
- gp_max_val_max = 0.08293932905728749
- srmr = 0.06030394287134169
- gp_max_val_min = 0.05901810277482248
- gp_max_ix_std = 0.05236534979182037
- gp_auc_mean = 0.04966482566834843
- gp_max_ix_range = 0.043369322256790285
- high_power = 0.04304386796455949
- diff_auc = 0.03558819004172113
- ratio_max_to_10ms_ave_peaks = 0.034632361267423195
- diff_std = 0.025271335541846372
- hlbr = 0.024020257019948425
- gp_max_ix_min = 0.016634977223212517
- tdoa_range = 0.015262185985353812
- tdoa_min = 0.014248234944601727
- gp_max_ix_mean = 0.012770835377511919
- gp_max_val_std = 0.010508586071171565
- coe1[1] = 0.007617320712788408
- tdoa_max = 0.007194535312182369
- tdoa_mean = 0.007096949891067536
- gp_max_val_range = 0.00702032523664402
- coe1[0] = 0.006116227635835482
- gp_max_ix_max = 0.0060155122655122665
- gp_auc_std = 0.0059471134995448365
- gp_auc_range = 0.005085251491901107
- low_power = 0.004475638740344625
- coe3[2] = 0.004395120366987375
- tdoa_std = 0.004176937890132291
- coe3[3] = 0.004150326797385621
- ratio_max_to_9th_ave_peaks = 0.004038800395224544
- ac_auc = 0.0035240249946132305
- ac_std = 0.0001742919389978216
- coe3[0] = 0.0
- coe3[1] = 0.0

## Evaluation
cv = 8
### robot-1
#### accuracy
- Mean = 1.0
- Standard deviation = 0.0
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 1.0
- Min = 1.0

#### f1
- Mean = 1.0
- Standard deviation = 0.0
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 1.0
- Min = 1.0

#### precision
- Mean = 1.0
- Standard deviation = 0.0
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 1.0
- Min = 1.0

#### recall
- Mean = 1.0
- Standard deviation = 0.0
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 1.0
- Min = 1.0

#### facing_probas
- Mean = [0.96166667 0.71       0.04520833 0.         0.        ]
- Standard deviation = [0.03195048 0.10428993 0.01742917 0.         0.        ]
- Max = [0.98166667 0.81333333 0.07166667 0.         0.        ]
- 75% = [0.97625    0.80208333 0.06041667 0.         0.        ]
- Median = [0.97333333 0.73166667 0.04583333 0.         0.        ]
- 25% = [0.96625    0.67291667 0.0275     0.         0.        ]
- Min = [0.87833333 0.49666667 0.02333333 0.         0.        ]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 79.125 | 0.0 |
| Actual Positive | 0.0 | 20.0 |

### robot-2
#### accuracy
- Mean = 0.9974747474747475
- Standard deviation = 0.0043738656756789635
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 0.9974747474747475
- Min = 0.98989898989899

#### f1
- Mean = 0.9939024390243902
- Standard deviation = 0.010561285412005359
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 0.9939024390243902
- Min = 0.975609756097561

#### precision
- Mean = 0.9880952380952381
- Standard deviation = 0.020619652471058087
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 0.9880952380952381
- Min = 0.9523809523809523

#### recall
- Mean = 1.0
- Standard deviation = 0.0
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 1.0
- Min = 1.0

#### facing_probas
- Mean = [0.96541667 0.97020833 0.95041667 0.02145833 0.00520833]
- Standard deviation = [0.02429206 0.02235194 0.03085303 0.00709252 0.00496078]
- Max = [0.98833333 1.         0.985      0.03       0.01333333]
- 75% = [0.98333333 0.9875     0.97791667 0.02625    0.01      ]
- Median = [0.975      0.9775     0.95583333 0.02166667 0.00416667]
- 25% = [0.95791667 0.95041667 0.93083333 0.01916667 0.        ]
- Min = [0.91333333 0.935      0.90166667 0.00666667 0.        ]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 78.875 | 0.25 |
| Actual Positive | 0.0 | 20.0 |

### robot-3
#### accuracy
- Mean = 0.887689393939394
- Standard deviation = 0.04730920087520248
- Max = 0.95
- 75% = 0.9318181818181819
- Median = 0.8888888888888888
- 25% = 0.845959595959596
- Min = 0.8181818181818182

#### f1
- Mean = 0.5764873137264028
- Standard deviation = 0.23759709247526092
- Max = 0.8571428571428571
- 75% = 0.7967914438502675
- Median = 0.6140979689366786
- 25% = 0.38333333333333336
- Min = 0.18181818181818182

#### precision
- Mean = 1.0
- Standard deviation = 0.0
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 1.0
- Min = 1.0

#### recall
- Mean = 0.44375
- Standard deviation = 0.23377005261581307
- Max = 0.75
- 75% = 0.6625
- Median = 0.45
- 25% = 0.2375
- Min = 0.1

#### facing_probas
- Mean = [0.48458333 0.93145833 0.9675     0.870625   0.12895833]
- Standard deviation = [0.15805183 0.02853406 0.01047484 0.0358521  0.03004554]
- Max = [0.78833333 0.96166667 0.97833333 0.92333333 0.16166667]
- 75% = [0.56375    0.95416667 0.97708333 0.89458333 0.15416667]
- Median = [0.48583333 0.94166667 0.97       0.86666667 0.135     ]
- 25% = [0.35541667 0.90875    0.96       0.84541667 0.11458333]
- Min = [0.29       0.87833333 0.94666667 0.81833333 0.065     ]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 79.125 | 0.0 |
| Actual Positive | 11.125 | 8.875 |

### robot-4
#### accuracy
- Mean = 0.9672222222222222
- Standard deviation = 0.02353811706149264
- Max = 0.98989898989899
- 75% = 0.98989898989899
- Median = 0.9698989898989898
- 25% = 0.9570707070707071
- Min = 0.9191919191919192

#### f1
- Mean = 0.9020529219058631
- Standard deviation = 0.0780890686791026
- Max = 0.972972972972973
- 75% = 0.972972972972973
- Median = 0.9166666666666667
- 25% = 0.873885918003565
- Min = 0.7333333333333334

#### precision
- Mean = 1.0
- Standard deviation = 0.0
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 1.0
- Min = 1.0

#### recall
- Mean = 0.8302631578947368
- Standard deviation = 0.12235427196071254
- Max = 0.9473684210526315
- 75% = 0.9473684210526315
- Median = 0.8473684210526315
- 25% = 0.7763157894736842
- Min = 0.5789473684210527

#### facing_probas
- Mean = [8.33333333e-04 1.50438596e-02 8.96699561e-01 9.75778509e-01
 7.63563596e-01]
- Standard deviation = [0.00220479 0.01546095 0.05492934 0.01489036 0.098029  ]
- Max = [0.00666667 0.04666667 0.97017544 0.9877193  0.88947368]
- 75% = [0.         0.02236842 0.94210526 0.98640351 0.8372807 ]
- Median = [0.         0.00877193 0.89473684 0.98381579 0.77982456]
- 25% = [0.         0.00307018 0.86532895 0.96973684 0.70462719]
- Min = [0.         0.         0.80526316 0.94912281 0.56491228]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 80.0 | 0.0 |
| Actual Positive | 3.25 | 15.875 |

### robot-5
#### accuracy
- Mean = 1.0
- Standard deviation = 0.0
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 1.0
- Min = 1.0

#### f1
- Mean = 1.0
- Standard deviation = 0.0
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 1.0
- Min = 1.0

#### precision
- Mean = 1.0
- Standard deviation = 0.0
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 1.0
- Min = 1.0

#### recall
- Mean = 1.0
- Standard deviation = 0.0
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 1.0
- Min = 1.0

#### facing_probas
- Mean = [1.10416667e-02 2.08333333e-04 5.47916667e-02 9.57708333e-01
 9.71250000e-01]
- Standard deviation = [0.0070187  0.0005512  0.02867971 0.02743601 0.03113311]
- Max = [0.02166667 0.00166667 0.08833333 0.99666667 0.995     ]
- 75% = [0.01625    0.         0.08541667 0.9725     0.99041667]
- Median = [0.01       0.         0.05666667 0.96333333 0.9825    ]
- 25% = [0.00625    0.         0.02916667 0.94291667 0.96958333]
- Min = [0.         0.         0.015      0.90333333 0.89333333]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 79.125 | 0.0 |
| Actual Positive | 0.0 | 20.0 |

### robot-6
#### accuracy
- Mean = 0.8549116161616162
- Standard deviation = 0.03171170003227268
- Max = 0.91
- 75% = 0.8712121212121212
- Median = 0.8585858585858586
- 25% = 0.8358585858585859
- Min = 0.797979797979798

#### f1
- Mean = 0.9214656222997798
- Standard deviation = 0.01848143010820924
- Max = 0.9528795811518325
- 75% = 0.9311682650392328
- Median = 0.9239130434782609
- 25% = 0.9105852710825086
- Min = 0.8876404494382023

#### precision
- Mean = 1.0
- Standard deviation = 0.0
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 1.0
- Min = 1.0

#### recall
- Mean = 0.8549116161616162
- Standard deviation = 0.03171170003227268
- Max = 0.91
- 75% = 0.8712121212121212
- Median = 0.8585858585858586
- 25% = 0.8358585858585859
- Min = 0.797979797979798

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
| Actual Positive | 14.375 | 84.75 |

