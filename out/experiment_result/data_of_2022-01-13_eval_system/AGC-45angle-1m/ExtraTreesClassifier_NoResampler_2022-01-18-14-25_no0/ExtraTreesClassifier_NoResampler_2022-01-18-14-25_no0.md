# ExtraTreesClassifier_NoResampler_2022-01-18-14-25_no0
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
- high_power = 0.1331374402267573
- gp_auc_max = 0.12128705784992799
- gp_max_val_mean = 0.07045155556581052
- gp_max_ix_range = 0.06117245443148827
- gp_max_val_max = 0.059185560211681976
- gp_auc_mean = 0.05797245469084628
- srmr = 0.04823326627872828
- diff_auc = 0.04700068134004931
- tdoa_min = 0.0439129209101714
- gp_max_ix_std = 0.0427420886356602
- gp_auc_min = 0.04205877176458063
- diff_std = 0.04070258104782126
- hlbr = 0.03866541225925999
- ratio_max_to_10ms_ave_peaks = 0.031409470740815404
- gp_max_ix_min = 0.02644956076355369
- tdoa_mean = 0.024965462455359855
- gp_max_val_min = 0.02351049721414704
- coe1[1] = 0.012640208345488095
- ac_auc = 0.010757852356921628
- coe1[0] = 0.008995251155338875
- tdoa_std = 0.008929875917055406
- tdoa_range = 0.00698164905653922
- gp_max_ix_max = 0.006774238633994735
- gp_max_ix_mean = 0.006593062682806273
- coe3[3] = 0.0046247293636219365
- coe3[2] = 0.004309087296724132
- gp_max_val_std = 0.002670940170940172
- gp_auc_range = 0.0026709401709401714
- ratio_max_to_9th_ave_peaks = 0.002281097584460159
- ac_std = 0.0020759847148736042
- low_power = 0.0019841878394509984
- gp_auc_std = 0.0018293721552268573
- tdoa_max = 0.0016025641025641027
- gp_max_val_range = 0.0014217220663944082
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
- Mean = [0.94375    0.801875   0.06541667 0.00104167 0.00479167]
- Standard deviation = [0.02457627 0.08281689 0.03522497 0.00185171 0.00818355]
- Max = [0.97166667 0.90333333 0.13166667 0.005      0.025     ]
- 75% = [9.67500000e-01 8.80833333e-01 7.75000000e-02 8.33333333e-04
 5.83333333e-03]
- Median = [0.94583333 0.8075     0.0525     0.         0.        ]
- 25% = [0.92625    0.74291667 0.04       0.         0.        ]
- Min = [0.905      0.67833333 0.03       0.         0.        ]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 79.125 | 0.0 |
| Actual Positive | 0.0 | 20.0 |

### robot-2
#### accuracy
- Mean = 0.9974873737373737
- Standard deviation = 0.0043520696107655745
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 0.9975
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
- Mean = [0.95875    0.95666667 0.94       0.02895833 0.015625  ]
- Standard deviation = [0.01703244 0.02081666 0.0163936  0.01043956 0.00946255]
- Max = [0.985      0.98       0.95833333 0.04       0.03666667]
- 75% = [0.96791667 0.97458333 0.955      0.03708333 0.01666667]
- Median = [0.96083333 0.95583333 0.94416667 0.03333333 0.01333333]
- 25% = [0.95375    0.95125    0.92625    0.02166667 0.01166667]
- Min = [0.93       0.91166667 0.915      0.01       0.00166667]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 78.875 | 0.25 |
| Actual Positive | 0.0 | 20.0 |

### robot-3
#### accuracy
- Mean = 0.8978409090909091
- Standard deviation = 0.023979154292374284
- Max = 0.9292929292929293
- 75% = 0.9122979797979798
- Median = 0.904040404040404
- 25% = 0.8863636363636364
- Min = 0.8484848484848485

#### f1
- Mean = 0.6520023149820147
- Standard deviation = 0.11506064610987633
- Max = 0.787878787878788
- 75% = 0.719758064516129
- Median = 0.6881720430107527
- 25% = 0.6083743842364533
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
- Mean = 0.49374999999999997
- Standard deviation = 0.1184205957593526
- Max = 0.65
- 75% = 0.5625
- Median = 0.525
- 25% = 0.4375
- Min = 0.25

#### facing_probas
- Mean = [0.49354167 0.94041667 0.96833333 0.90291667 0.171875  ]
- Standard deviation = [0.05853796 0.02212261 0.01346291 0.03293249 0.08377979]
- Max = [0.605      0.975      0.98833333 0.965      0.315     ]
- 75% = [0.52791667 0.95791667 0.97666667 0.91916667 0.245     ]
- Median = [0.48083333 0.93666667 0.96833333 0.9075     0.15583333]
- 25% = [0.45208333 0.93083333 0.96333333 0.87125    0.09      ]
- Min = [0.41833333 0.9        0.94166667 0.86166667 0.07833333]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 79.125 | 0.0 |
| Actual Positive | 10.125 | 9.875 |

### robot-4
#### accuracy
- Mean = 0.9735353535353535
- Standard deviation = 0.009952442777174643
- Max = 0.98989898989899
- 75% = 0.9797979797979798
- Median = 0.9747474747474747
- 25% = 0.9672727272727273
- Min = 0.9595959595959596

#### f1
- Mean = 0.9257649456178868
- Standard deviation = 0.02911906606814843
- Max = 0.972972972972973
- 75% = 0.9444444444444444
- Median = 0.9293650793650794
- 25% = 0.9079365079365079
- Min = 0.8823529411764706

#### precision
- Mean = 1.0
- Standard deviation = 0.0
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 1.0
- Min = 1.0

#### recall
- Mean = 0.8631578947368421
- Standard deviation = 0.050482437087502295
- Max = 0.9473684210526315
- 75% = 0.8947368421052632
- Median = 0.868421052631579
- 25% = 0.831578947368421
- Min = 0.7894736842105263

#### facing_probas
- Mean = [2.19298246e-04 1.88596491e-02 9.45175439e-01 9.85394737e-01
 8.16107456e-01]
- Standard deviation = [0.00058021 0.0134113  0.0361117  0.00799919 0.04669246]
- Max = [0.00175439 0.04035088 0.98421053 1.         0.86491228]
- 75% = [0.         0.02675439 0.96973684 0.98947368 0.8622807 ]
- Median = [0.         0.01929825 0.95964912 0.98719298 0.82105263]
- 25% = [0.         0.01052632 0.92631579 0.97938596 0.78703947]
- Min = [0.         0.         0.86666667 0.97368421 0.72280702]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 80.0 | 0.0 |
| Actual Positive | 2.625 | 16.5 |

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
- Mean = [2.68750000e-02 8.33333333e-04 8.68750000e-02 9.81250000e-01
 9.86666667e-01]
- Standard deviation = [0.02107258 0.00166667 0.05488269 0.01209769 0.00853913]
- Max = [0.06       0.005      0.16166667 0.99666667 0.99833333]
- 75% = [4.04166667e-02 4.16666667e-04 1.32916667e-01 9.90833333e-01
 9.92500000e-01]
- Median = [0.02416667 0.         0.09333333 0.9825     0.98833333]
- 25% = [0.00708333 0.         0.02833333 0.97541667 0.98125   ]
- Min = [0.00333333 0.         0.01833333 0.96       0.97333333]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 79.125 | 0.0 |
| Actual Positive | 0.0 | 20.0 |

### robot-6
#### accuracy
- Mean = 0.8713762626262627
- Standard deviation = 0.020027588964033442
- Max = 0.898989898989899
- 75% = 0.8813131313131313
- Median = 0.8743939393939394
- 25% = 0.8661616161616161
- Min = 0.8282828282828283

#### f1
- Mean = 0.9311442659823457
- Standard deviation = 0.011547507545746745
- Max = 0.9468085106382979
- 75% = 0.9369070208728653
- Median = 0.9329825771951008
- 25% = 0.9282755581668626
- Min = 0.9060773480662984

#### precision
- Mean = 1.0
- Standard deviation = 0.0
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 1.0
- Min = 1.0

#### recall
- Mean = 0.8713762626262627
- Standard deviation = 0.020027588964033442
- Max = 0.898989898989899
- 75% = 0.8813131313131313
- Median = 0.8743939393939394
- 25% = 0.8661616161616161
- Min = 0.8282828282828283

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
| Actual Positive | 12.75 | 86.375 |

