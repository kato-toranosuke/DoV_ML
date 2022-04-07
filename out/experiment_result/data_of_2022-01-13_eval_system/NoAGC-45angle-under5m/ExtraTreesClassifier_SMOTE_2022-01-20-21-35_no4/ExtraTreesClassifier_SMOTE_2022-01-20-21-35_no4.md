# ExtraTreesClassifier_SMOTE_2022-01-20-21-35_no4
## Constants
- CSV_PATH = ../out/csv/experiment
- OUTPUT_PATH = ../out/experiment_result/data_of_2022-01-13_eval_system/NoAGC-45angle-under5m
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
- DISTANCE = [1, 3, 5]
- AGC_STATUS = ['NoAGC']

## Loaded CSV
- 2021-12-27_AGC.csv
- 2022-01-10_NoAGC.csv
- 2022-01-13_raspi_48000Hz_w1_N2^12_overlap80.csv

## Estimator
### Type
- resampler = SMOTE
- estimator = ExtraTreesClassifier

### Arguments for hyperparameter search
- resampler = SMOTE
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
	- k_neighbors = 5
	- n_jobs = -1
	- n_features_in_ = 36
	- sampling_strategy_ = OrderedDict([(0, 9)])
	- nn_k_ = NearestNeighbors(n_neighbors=6)

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
- gp_max_val_max = 0.10145511322931916
- gp_auc_mean = 0.08793103237500081
- gp_max_val_min = 0.0830825870876737
- gp_max_val_mean = 0.0729698483843038
- gp_auc_min = 0.07291898576225482
- gp_auc_max = 0.06722334741972388
- hlbr = 0.04662524900455623
- srmr = 0.04511906346596148
- diff_std = 0.03277224701304586
- diff_auc = 0.03154103224455996
- tdoa_mean = 0.02916582887082314
- gp_max_ix_mean = 0.028275111081059356
- tdoa_std = 0.02502476435821779
- low_power = 0.020622020916755548
- gp_auc_std = 0.02036754384074754
- gp_max_val_std = 0.019207575458662727
- ratio_max_to_10ms_ave_peaks = 0.017766290288155854
- high_power = 0.016665216698406687
- coe1[1] = 0.015439250305087375
- gp_max_ix_std = 0.014784017197761238
- tdoa_min = 0.014419908347773956
- gp_max_ix_min = 0.014095467084694653
- tdoa_range = 0.013891449502418904
- ac_auc = 0.01312747857375236
- coe3[3] = 0.013070482320816444
- coe3[2] = 0.011299562556594185
- gp_max_ix_range = 0.01126791626286985
- gp_auc_range = 0.009936531775686612
- coe1[0] = 0.009863238279464928
- ac_std = 0.008934104524725175
- gp_max_ix_max = 0.008815029488197033
- tdoa_max = 0.007997034907140297
- ratio_max_to_9th_ave_peaks = 0.007256157179469039
- gp_max_val_range = 0.007069514194319573
- coe3[0] = 0.0
- coe3[1] = 0.0

## Evaluation
cv = 8
### robot-1
#### accuracy
- Mean = 0.9791666666666666
- Standard deviation = 0.011755613316388228
- Max = 0.9966666666666667
- 75% = 0.9883333333333333
- Median = 0.9783333333333333
- 25% = 0.9691666666666666
- Min = 0.9633333333333334

#### f1
- Mean = 0.9477646227982719
- Standard deviation = 0.029837154695801452
- Max = 0.9915966386554621
- 75% = 0.9708333333333333
- Median = 0.9466666666666668
- 25% = 0.9220908702464036
- Min = 0.9075630252100839

#### precision
- Mean = 0.9481127957859401
- Standard deviation = 0.02904028371050968
- Max = 1.0
- 75% = 0.9708333333333333
- Median = 0.9327683615819209
- 25% = 0.9290450928381963
- Min = 0.9152542372881356

#### recall
- Mean = 0.9479166666666667
- Standard deviation = 0.037673211083385665
- Max = 1.0
- 75% = 0.9833333333333333
- Median = 0.95
- 25% = 0.9125
- Min = 0.9

#### facing_probas
- Mean = [0.93847222 0.7675     0.08159722 0.00645833 0.00222222]
- Standard deviation = [0.03079045 0.02770685 0.01097288 0.00508369 0.00168966]
- Max = [0.98333333 0.825      0.10055556 0.01388889 0.00555556]
- 75% = [0.96513889 0.77930556 0.08680556 0.01013889 0.00333333]
- Median = [0.93555556 0.76472222 0.07916667 0.00583333 0.00194444]
- 25% = [0.92166667 0.74652778 0.07194444 0.00111111 0.00097222]
- Min = [0.88055556 0.73555556 0.07       0.00111111 0.        ]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 236.875 | 3.125 |
| Actual Positive | 3.125 | 56.875 |

### robot-2
#### accuracy
- Mean = 0.9604166666666667
- Standard deviation = 0.009492321458245427
- Max = 0.9766666666666667
- 75% = 0.9641666666666667
- Median = 0.9633333333333334
- 25% = 0.9533333333333334
- Min = 0.9433333333333334

#### f1
- Mean = 0.8936013929239535
- Standard deviation = 0.026285564307817776
- Max = 0.9391304347826087
- 75% = 0.9046697218710493
- Median = 0.9008687180319883
- 25% = 0.8744318181818181
- Min = 0.8468468468468469

#### precision
- Mean = 0.9638740042791097
- Standard deviation = 0.022878952220955494
- Max = 1.0
- 75% = 0.9810314685314685
- Median = 0.9622641509433962
- 25% = 0.9555769230769231
- Min = 0.9215686274509803

#### recall
- Mean = 0.8333333333333333
- Standard deviation = 0.034359213546813844
- Max = 0.9
- 75% = 0.85
- Median = 0.8333333333333333
- 25% = 0.8125
- Min = 0.7833333333333333

#### facing_probas
- Mean = [0.915      0.94145833 0.82923611 0.16368056 0.02013889]
- Standard deviation = [0.02757565 0.02257692 0.03979009 0.04328072 0.00978058]
- Max = [0.95722222 0.97666667 0.89222222 0.22055556 0.04111111]
- 75% = [0.94180556 0.96291667 0.86111111 0.20583333 0.02069444]
- Median = [0.91111111 0.93694444 0.81333333 0.15861111 0.01833333]
- 25% = [0.89111111 0.92375    0.7975     0.13513889 0.0175    ]
- Min = [0.87666667 0.91       0.78277778 0.09333333 0.00388889]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 238.125 | 1.875 |
| Actual Positive | 10.0 | 50.0 |

### robot-3
#### accuracy
- Mean = 0.9345833333333333
- Standard deviation = 0.012353305900311315
- Max = 0.96
- 75% = 0.9375
- Median = 0.935
- 25% = 0.9291666666666667
- Min = 0.9133333333333333

#### f1
- Mean = 0.8035808648318379
- Standard deviation = 0.04431642536751607
- Max = 0.890909090909091
- 75% = 0.8175328383780697
- Median = 0.805940594059406
- 25% = 0.7847866419294991
- Min = 0.7234042553191489

#### precision
- Mean = 0.994593023255814
- Standard deviation = 0.009400463436327996
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 0.995
- Min = 0.9767441860465116

#### recall
- Mean = 0.6770833333333333
- Standard deviation = 0.06663410663216449
- Max = 0.8166666666666667
- 75% = 0.7
- Median = 0.675
- 25% = 0.6458333333333334
- Min = 0.5666666666666667

#### facing_probas
- Mean = [0.27375    0.88076389 0.91486111 0.79625    0.18097222]
- Standard deviation = [0.04543493 0.03629434 0.03527313 0.05007074 0.03608733]
- Max = [0.35888889 0.94722222 0.96       0.87222222 0.25333333]
- 75% = [0.28791667 0.90472222 0.95041667 0.83541667 0.18694444]
- Median = [0.24916667 0.87138889 0.91083333 0.78416667 0.17111111]
- 25% = [0.24541667 0.85486111 0.88555556 0.7525     0.15597222]
- Min = [0.235      0.82888889 0.86444444 0.73555556 0.14055556]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 239.75 | 0.25 |
| Actual Positive | 19.375 | 40.625 |

### robot-4
#### accuracy
- Mean = 0.9341666666666666
- Standard deviation = 0.01221906524884598
- Max = 0.9566666666666667
- 75% = 0.9391666666666667
- Median = 0.9333333333333333
- 25% = 0.9275
- Min = 0.9166666666666666

#### f1
- Mean = 0.8066360974401381
- Standard deviation = 0.04070180074315873
- Max = 0.8807339449541285
- 75% = 0.8231889469753547
- Median = 0.8058069381598794
- 25% = 0.7852358765288294
- Min = 0.7422680412371134

#### precision
- Mean = 0.9705282638948873
- Standard deviation = 0.019586520583330092
- Max = 1.0
- 75% = 0.9774560987185572
- Median = 0.9759001161440186
- 25% = 0.9683660933660934
- Min = 0.9285714285714286

#### recall
- Mean = 0.6916666666666667
- Standard deviation = 0.05527707983925668
- Max = 0.8
- 75% = 0.7083333333333333
- Median = 0.6916666666666667
- 25% = 0.6625
- Min = 0.6

#### facing_probas
- Mean = [0.00673611 0.27076389 0.86756944 0.93430556 0.77229167]
- Standard deviation = [0.00459332 0.03896019 0.04324951 0.04051534 0.05129679]
- Max = [0.01444444 0.35       0.94666667 0.98111111 0.85555556]
- 75% = [0.01       0.28402778 0.90027778 0.97222222 0.81027778]
- Median = [0.00472222 0.25916667 0.86111111 0.93611111 0.75166667]
- 25% = [0.00277778 0.25291667 0.83194444 0.90236111 0.73486111]
- Min = [0.00222222 0.21333333 0.80833333 0.87944444 0.71222222]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 238.75 | 1.25 |
| Actual Positive | 18.5 | 41.5 |

### robot-5
#### accuracy
- Mean = 0.9866666666666667
- Standard deviation = 0.006871842709362771
- Max = 1.0
- 75% = 0.9908333333333333
- Median = 0.985
- 25% = 0.98
- Min = 0.98

#### f1
- Mean = 0.9656001297830158
- Standard deviation = 0.01801210551941824
- Max = 1.0
- 75% = 0.9771676705420926
- Median = 0.9613117170228445
- 25% = 0.9482758620689654
- Min = 0.9473684210526316

#### precision
- Mean = 0.9892821812161835
- Standard deviation = 0.011678115167001945
- Max = 1.0
- 75% = 1.0
- Median = 0.9913793103448276
- 25% = 0.9821428571428571
- Min = 0.9672131147540983

#### recall
- Mean = 0.94375
- Standard deviation = 0.034295995069071515
- Max = 1.0
- 75% = 0.9708333333333333
- Median = 0.9333333333333333
- 25% = 0.9166666666666666
- Min = 0.9

#### facing_probas
- Mean = [0.00736111 0.00597222 0.14090278 0.91625    0.89444444]
- Standard deviation = [0.0043368  0.00338786 0.01726459 0.04775334 0.04434886]
- Max = [0.01444444 0.01166667 0.17       0.97666667 0.94666667]
- 75% = [0.00888889 0.00847222 0.15652778 0.96097222 0.93597222]
- Median = [0.00666667 0.00444444 0.13555556 0.91027778 0.8975    ]
- 25% = [0.00486111 0.00375    0.12875    0.86972222 0.86208333]
- Min = [0.00166667 0.00166667 0.11833333 0.86555556 0.81722222]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 239.375 | 0.625 |
| Actual Positive | 3.375 | 56.625 |

### robot-6
#### accuracy
- Mean = 0.81875
- Standard deviation = 0.034235195502744134
- Max = 0.86
- 75% = 0.8475
- Median = 0.8266666666666667
- 25% = 0.7833333333333333
- Min = 0.7733333333333333

#### f1
- Mean = 0.8999523918191925
- Standard deviation = 0.020786710425658102
- Max = 0.924731182795699
- 75% = 0.9174395768924148
- Median = 0.9050949050949051
- 25% = 0.8784928739759847
- Min = 0.8721804511278195

#### precision
- Mean = 1.0
- Standard deviation = 0.0
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 1.0
- Min = 1.0

#### recall
- Mean = 0.81875
- Standard deviation = 0.034235195502744134
- Max = 0.86
- 75% = 0.8475
- Median = 0.8266666666666667
- 25% = 0.7833333333333333
- Min = 0.7733333333333333

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
| Actual Positive | 54.375 | 245.625 |

