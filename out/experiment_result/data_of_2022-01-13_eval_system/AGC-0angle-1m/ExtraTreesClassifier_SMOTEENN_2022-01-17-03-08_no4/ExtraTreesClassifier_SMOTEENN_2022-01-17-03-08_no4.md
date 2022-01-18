# ExtraTreesClassifier_SMOTEENN_2022-01-17-03-08_no4
## Constants
- CSV_PATH = ../out/csv/experiment
- OUTPUT_PATH = ../out/experiment_result/data_of_2022-01-13_eval_system/AGC-0angle-1m
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
- AGC_STATUS = ['AGC']

## Loaded CSV
- 2021-12-27_AGC.csv
- 2022-01-10_NoAGC.csv
- 2022-01-13_raspi_48000Hz_w1_N2^12_overlap80.csv

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
	- max_features = log2
	- max_leaf_nodes = None
	- min_impurity_decrease = 0.0
	- ccp_alpha = 0.0
	- n_features_in_ = 36
	- n_outputs_ = 1
	- classes_ = [0 1]
	- n_classes_ = 2
	- base_estimator_ = ExtraTreeClassifier()

#### Importance of features
- gp_auc_max = 0.07165215428276572
- gp_max_val_mean = 0.061089042847531146
- gp_auc_min = 0.060796200058970955
- gp_max_ix_min = 0.05893578019443071
- gp_auc_mean = 0.05471618058988301
- gp_max_ix_range = 0.053966065592903824
- tdoa_min = 0.05225548552754434
- srmr = 0.04723606905997692
- gp_max_ix_std = 0.04597193947238338
- ac_std = 0.04440067582562118
- tdoa_std = 0.04432556846267918
- high_power = 0.04168844764626498
- hlbr = 0.03581579992479646
- ac_auc = 0.030772788281979446
- gp_max_val_min = 0.030743796764558004
- tdoa_range = 0.02949746320096665
- gp_max_val_max = 0.027122217307975812
- ratio_max_to_10ms_ave_peaks = 0.02394860149942329
- coe3[2] = 0.021995656266892715
- coe3[3] = 0.020601434652808486
- diff_auc = 0.020317213006898403
- gp_max_ix_mean = 0.017061157796451905
- gp_max_val_std = 0.015064338235294114
- ratio_max_to_9th_ave_peaks = 0.0144625350140056
- gp_auc_range = 0.01386554621848739
- tdoa_mean = 0.01270088901788785
- gp_auc_std = 0.012041976878470681
- diff_std = 0.011635548827374087
- tdoa_max = 0.007487412385768787
- low_power = 0.006613321799307957
- coe1[0] = 0.0052941176470588215
- coe1[1] = 0.0032284972812654483
- gp_max_val_range = 0.002696078431372548
- coe3[0] = 0.0
- coe3[1] = 0.0
- gp_max_ix_max = 0.0

## Evaluation
cv = 8
### robot-1
#### accuracy
- Mean = 0.8600000000000001
- Standard deviation = 0.0765395334023646
- Max = 0.9797979797979798
- 75% = 0.9024242424242425
- Median = 0.8434343434343434
- 25% = 0.8131313131313131
- Min = 0.7474747474747475

#### f1
- Mean = 0.568916049181993
- Standard deviation = 0.2849237300989257
- Max = 0.9500000000000001
- 75% = 0.7170014347202295
- Median = 0.5857771260997067
- 25% = 0.476958525345622
- Min = 0.09090909090909091

#### precision
- Mean = 0.6648133116883117
- Standard deviation = 0.22004323999143405
- Max = 0.95
- 75% = 0.8398268398268398
- Median = 0.6655844155844155
- 25% = 0.53125
- Min = 0.2727272727272727

#### recall
- Mean = 0.54375
- Standard deviation = 0.306632414300902
- Max = 0.95
- 75% = 0.725
- Median = 0.575
- 25% = 0.375
- Min = 0.05

#### facing_probas
- Mean = [0.55854167 0.2025     0.08708333 0.02208333 0.02666667]
- Standard deviation = [0.21510727 0.09083333 0.07536831 0.03493794 0.03802412]
- Max = [0.885      0.30666667 0.27       0.09333333 0.12333333]
- 75% = [0.65708333 0.27625    0.08833333 0.02125    0.02041667]
- Median = [0.57666667 0.215      0.0575     0.00333333 0.01416667]
- 25% = [0.45541667 0.15916667 0.0475     0.00125    0.00666667]
- Min = [0.21       0.02166667 0.01833333 0.         0.        ]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 74.375 | 4.75 |
| Actual Positive | 9.125 | 10.875 |

### robot-2
#### accuracy
- Mean = 0.8409974747474747
- Standard deviation = 0.05832505598494857
- Max = 0.93
- 75% = 0.8787878787878788
- Median = 0.8434343434343434
- 25% = 0.797979797979798
- Min = 0.7575757575757576

#### f1
- Mean = 0.4473419940811245
- Standard deviation = 0.2333344444974955
- Max = 0.787878787878788
- 75% = 0.6722007722007721
- Median = 0.3822843822843823
- 25% = 0.24565217391304348
- Min = 0.1739130434782609

#### precision
- Mean = 0.7404788838612368
- Standard deviation = 0.2610753306703602
- Max = 1.0
- 75% = 1.0
- Median = 0.7862745098039217
- 25% = 0.5961538461538461
- Min = 0.3

#### recall
- Mean = 0.35624999999999996
- Standard deviation = 0.2228192933746986
- Max = 0.65
- 75% = 0.6125
- Median = 0.275
- 25% = 0.15
- Min = 0.1

#### facing_probas
- Mean = [0.501875   0.57395833 0.54083333 0.03479167 0.03708333]
- Standard deviation = [0.14238894 0.15456691 0.15308177 0.05744827 0.044797  ]
- Max = [0.62833333 0.76166667 0.72333333 0.185      0.14166667]
- 75% = [0.61791667 0.6775     0.67208333 0.0225     0.03833333]
- Median = [0.54083333 0.62       0.5675     0.01416667 0.01916667]
- 25% = [0.44541667 0.50833333 0.42208333 0.00875    0.00875   ]
- Min = [0.19166667 0.28       0.26833333 0.         0.00166667]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 76.25 | 2.875 |
| Actual Positive | 12.875 | 7.125 |

### robot-3
#### accuracy
- Mean = 0.8876767676767676
- Standard deviation = 0.06159198068321213
- Max = 0.96
- 75% = 0.9191919191919192
- Median = 0.898989898989899
- 25% = 0.8863636363636364
- Min = 0.7373737373737373

#### f1
- Mean = 0.6987860687551091
- Standard deviation = 0.1438931855509605
- Max = 0.8947368421052632
- 75% = 0.7708978328173375
- Median = 0.7373527373527373
- 25% = 0.6642857142857143
- Min = 0.380952380952381

#### precision
- Mean = 0.7912946358766793
- Standard deviation = 0.17423239867946325
- Max = 0.9444444444444444
- 75% = 0.9071428571428571
- Median = 0.8284313725490196
- 25% = 0.7842105263157895
- Min = 0.36363636363636365

#### recall
- Mean = 0.6375
- Standard deviation = 0.14086784586980805
- Max = 0.85
- 75% = 0.7124999999999999
- Median = 0.675
- 25% = 0.5625
- Min = 0.4

#### facing_probas
- Mean = [0.13875    0.38333333 0.654375   0.24125    0.06125   ]
- Standard deviation = [0.06984979 0.14640128 0.08281479 0.09942805 0.0507359 ]
- Max = [0.26       0.56833333 0.82333333 0.39166667 0.13166667]
- 75% = [0.16666667 0.44916667 0.69291667 0.29833333 0.10708333]
- Median = [0.1425     0.42       0.63833333 0.25083333 0.05666667]
- 25% = [0.08208333 0.35916667 0.59041667 0.20333333 0.0075    ]
- Min = [0.04333333 0.04166667 0.55166667 0.04       0.00333333]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 75.25 | 3.875 |
| Actual Positive | 7.25 | 12.75 |

### robot-4
#### accuracy
- Mean = 0.885239898989899
- Standard deviation = 0.021417978828790027
- Max = 0.9090909090909091
- 75% = 0.9090909090909091
- Median = 0.8843939393939394
- 25% = 0.8686868686868687
- Min = 0.8484848484848485

#### f1
- Mean = 0.6868139540950602
- Standard deviation = 0.0548847286231325
- Max = 0.7755102040816326
- 75% = 0.7272727272727273
- Median = 0.6881720430107527
- 25% = 0.653846153846154
- Min = 0.6060606060606061

#### precision
- Mean = 0.744536607746547
- Standard deviation = 0.10909417967050382
- Max = 0.9166666666666666
- 75% = 0.8571428571428571
- Median = 0.7100840336134454
- 25% = 0.6538793103448276
- Min = 0.6

#### recall
- Mean = 0.6582236842105263
- Standard deviation = 0.11849732558315444
- Max = 0.95
- 75% = 0.6447368421052632
- Median = 0.631578947368421
- 25% = 0.618421052631579
- Min = 0.5263157894736842

#### facing_probas
- Mean = [0.02763158 0.02817982 0.27822368 0.59683114 0.25114035]
- Standard deviation = [0.0542638  0.03882616 0.14536775 0.11260285 0.12818677]
- Max = [0.16666667 0.11666667 0.54210526 0.84833333 0.47719298]
- 75% = [0.01842105 0.0377193  0.32938596 0.6245614  0.31631579]
- Median = [0.00087719 0.00789474 0.31403509 0.55438596 0.25350877]
- 25% = [0.         0.00131579 0.21144737 0.53552632 0.17324561]
- Min = [0.         0.         0.02807018 0.46842105 0.03508772]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 75.125 | 4.875 |
| Actual Positive | 6.5 | 12.625 |

### robot-5
#### accuracy
- Mean = 0.9105176767676768
- Standard deviation = 0.041924863845922415
- Max = 0.9595959595959596
- 75% = 0.9494949494949495
- Median = 0.9141414141414141
- 25% = 0.8917424242424242
- Min = 0.8282828282828283

#### f1
- Mean = 0.6921478270279177
- Standard deviation = 0.20014562434906683
- Max = 0.8947368421052632
- 75% = 0.859073359073359
- Median = 0.73719165085389
- 25% = 0.6296296296296295
- Min = 0.2608695652173913

#### precision
- Mean = 0.9767740429505136
- Standard deviation = 0.03027603742019623
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 0.9436274509803921
- Min = 0.9285714285714286

#### recall
- Mean = 0.575
- Standard deviation = 0.22360679774997896
- Max = 0.85
- 75% = 0.7625
- Median = 0.6000000000000001
- 25% = 0.4625
- Min = 0.15

#### facing_probas
- Mean = [0.04791667 0.025      0.05104167 0.47083333 0.63229167]
- Standard deviation = [0.04597516 0.04911014 0.04940576 0.09433245 0.12902933]
- Max = [0.15833333 0.15166667 0.16166667 0.63833333 0.72666667]
- 75% = [0.05375    0.01375    0.07291667 0.51958333 0.72041667]
- Median = [0.03916667 0.00333333 0.0275     0.45916667 0.67583333]
- 25% = [0.0125     0.         0.01625    0.42333333 0.61208333]
- Min = [0.00833333 0.         0.005      0.31166667 0.31333333]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 78.75 | 0.375 |
| Actual Positive | 8.5 | 11.5 |

### robot-6
#### accuracy
- Mean = 0.5534469696969697
- Standard deviation = 0.11489317820244788
- Max = 0.6868686868686869
- 75% = 0.6716919191919193
- Median = 0.5555555555555556
- 25% = 0.4722222222222222
- Min = 0.3434343434343434

#### f1
- Mean = 0.7052162006372686
- Standard deviation = 0.09928649896384863
- Max = 0.8143712574850299
- 75% = 0.8036036361012915
- Median = 0.7140688259109311
- 25% = 0.6414974019839396
- Min = 0.5112781954887218

#### precision
- Mean = 1.0
- Standard deviation = 0.0
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 1.0
- Min = 1.0

#### recall
- Mean = 0.5534469696969697
- Standard deviation = 0.11489317820244788
- Max = 0.6868686868686869
- 75% = 0.6716919191919193
- Median = 0.5555555555555556
- 25% = 0.4722222222222222
- Min = 0.3434343434343434

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
| Actual Positive | 44.25 | 54.875 |

