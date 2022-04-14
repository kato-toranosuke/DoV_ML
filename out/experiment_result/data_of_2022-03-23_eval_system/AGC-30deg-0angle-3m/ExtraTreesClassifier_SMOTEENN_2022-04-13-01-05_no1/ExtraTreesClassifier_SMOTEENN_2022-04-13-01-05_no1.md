# ExtraTreesClassifier_SMOTEENN_2022-04-13-01-05_no1
## Constants
- CSV_PATH = ../out/csv/experiment
- OUTPUT_PATH = ../out/experiment_result/data_of_2022-03-23_eval_system/AGC-30deg-0angle-3m
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
- DISTANCE = [3]
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
	- min_samples_split = 10
	- min_samples_leaf = 1
	- min_weight_fraction_leaf = 0.0
	- max_features = None
	- max_leaf_nodes = None
	- min_impurity_decrease = 0.0
	- ccp_alpha = 0.0
	- n_features_in_ = 36
	- n_outputs_ = 1
	- classes_ = [0 1]
	- n_classes_ = 2
	- base_estimator_ = ExtraTreeClassifier()

#### Importance of features
- ac_std = 0.1669077134986226
- ac_auc = 0.1197530864197531
- gp_auc_max = 0.11750949667616334
- gp_max_val_max = 0.11164013876135088
- coe3[3] = 0.0927469135802469
- gp_max_val_mean = 0.07191358024691356
- gp_auc_mean = 0.06666666666666667
- coe3[2] = 0.061913580246913576
- gp_auc_min = 0.05416666666666666
- gp_max_val_min = 0.04022038567493113
- coe1[0] = 0.03141025641025641
- ratio_max_to_10ms_ave_peaks = 0.01666666666666667
- low_power = 0.016666666666666663
- diff_std = 0.016666666666666663
- gp_max_val_std = 0.00909090909090909
- tdoa_mean = 0.006060606060606059
- high_power = 0.0
- hlbr = 0.0
- coe1[1] = 0.0
- coe3[0] = 0.0
- coe3[1] = 0.0
- ratio_max_to_9th_ave_peaks = 0.0
- diff_auc = 0.0
- srmr = 0.0
- gp_max_val_range = 0.0
- gp_max_ix_std = 0.0
- gp_max_ix_range = 0.0
- gp_max_ix_min = 0.0
- gp_max_ix_max = 0.0
- gp_max_ix_mean = 0.0
- gp_auc_std = 0.0
- gp_auc_range = 0.0
- tdoa_std = 0.0
- tdoa_range = 0.0
- tdoa_min = 0.0
- tdoa_max = 0.0

## Evaluation
cv = 8
### robot-1
#### accuracy
- Mean = 0.82875
- Standard deviation = 0.030593095626301022
- Max = 0.89
- 75% = 0.8425
- Median = 0.825
- 25% = 0.8075000000000001
- Min = 0.79

#### f1
- Mean = 0.47875874125874124
- Standard deviation = 0.20353242785019368
- Max = 0.717948717948718
- 75% = 0.6045454545454545
- Median = 0.5227272727272727
- 25% = 0.4242424242424242
- Min = 0.0

#### precision
- Mean = 0.5323067283593599
- Standard deviation = 0.21669883278988797
- Max = 0.7368421052631579
- 75% = 0.673076923076923
- Median = 0.5692307692307692
- 25% = 0.5252747252747253
- Min = 0.0

#### recall
- Mean = 0.4625
- Standard deviation = 0.24206145913796354
- Max = 0.85
- 75% = 0.625
- Median = 0.42500000000000004
- 25% = 0.35
- Min = 0.0

#### facing_probas
- Mean = [0.54174281 0.26083557 0.12714294 0.09187781 0.06324091]
- Standard deviation = [0.15548736 0.08985227 0.06475237 0.0751218  0.05410958]
- Max = [0.80311111 0.38840873 0.20407011 0.19984127 0.14502778]
- 75% = [0.61466518 0.34713211 0.1714542  0.15305688 0.11943783]
- Median = [0.5574084  0.2506422  0.16299735 0.08436839 0.0410291 ]
- 25% = [0.45206349 0.19980919 0.06519114 0.02143519 0.01159524]
- Min = [0.25386177 0.11456349 0.02272487 0.00714286 0.01074074]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 73.625 | 6.375 |
| Actual Positive | 10.75 | 9.25 |

### robot-2
#### accuracy
- Mean = 0.78125
- Standard deviation = 0.04858947931394203
- Max = 0.86
- 75% = 0.8150000000000001
- Median = 0.78
- 25% = 0.75
- Min = 0.71

#### f1
- Mean = 0.3623528448661427
- Standard deviation = 0.20465939195490165
- Max = 0.5957446808510639
- 75% = 0.5101351351351351
- Median = 0.4606606606606607
- 25% = 0.19341216216216214
- Min = 0.0

#### precision
- Mean = 0.4117878540305011
- Standard deviation = 0.2554769334622672
- Max = 0.875
- 75% = 0.5359477124183006
- Median = 0.45529411764705885
- 25% = 0.2181372549019608
- Min = 0.0

#### recall
- Mean = 0.35
- Standard deviation = 0.22220486043288973
- Max = 0.7
- 75% = 0.5125
- Median = 0.375
- 25% = 0.17500000000000002
- Min = 0.0

#### facing_probas
- Mean = [0.53164732 0.5851102  0.43748437 0.19869593 0.06975761]
- Standard deviation = [0.21262235 0.2180745  0.18085186 0.10528378 0.0615734 ]
- Max = [0.89362037 0.8909537  0.7992037  0.34769907 0.19618783]
- 75% = [0.64546792 0.7325916  0.50638194 0.26147404 0.10468618]
- Median = [0.51839683 0.65306548 0.3781875  0.20799206 0.05173942]
- 25% = [0.36654464 0.41661293 0.31322272 0.12662169 0.01733631]
- Min = [0.23450794 0.26240741 0.23770701 0.05074074 0.00907407]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 71.125 | 8.875 |
| Actual Positive | 13.0 | 7.0 |

### robot-3
#### accuracy
- Mean = 0.7775
- Standard deviation = 0.010897247358851694
- Max = 0.8
- 75% = 0.7825
- Median = 0.77
- 25% = 0.77
- Min = 0.77

#### f1
- Mean = 0.17889583394270925
- Standard deviation = 0.16440127101381602
- Max = 0.46511627906976744
- 75% = 0.2817836812144212
- Median = 0.17752234993614305
- 25% = 0.0
- Min = 0.0

#### precision
- Mean = 0.23075475249388294
- Standard deviation = 0.18429002582711157
- Max = 0.43478260869565216
- 75% = 0.37987012987012986
- Median = 0.30952380952380953
- 25% = 0.0
- Min = 0.0

#### recall
- Mean = 0.15625
- Standard deviation = 0.16476782908080084
- Max = 0.5
- 75% = 0.225
- Median = 0.125
- 25% = 0.0
- Min = 0.0

#### facing_probas
- Mean = [0.38723925 0.56976802 0.52540708 0.497917   0.11817171]
- Standard deviation = [0.1395777  0.17712043 0.20334622 0.14907677 0.08262418]
- Max = [0.64962037 0.85899074 0.81486772 0.7472619  0.26991534]
- 75% = [0.45615724 0.6763869  0.63635714 0.58690972 0.13694726]
- Median = [0.39877348 0.61671627 0.54914352 0.49715939 0.0944914 ]
- 25% = [0.30097222 0.43263128 0.36216865 0.41535714 0.06134954]
- Min = [0.17328704 0.2977381  0.24243254 0.23972222 0.02907407]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 74.625 | 5.375 |
| Actual Positive | 16.875 | 3.125 |

### robot-4
#### accuracy
- Mean = 0.76375
- Standard deviation = 0.04948168853222372
- Max = 0.83
- 75% = 0.7875000000000001
- Median = 0.775
- 25% = 0.75
- Min = 0.68

#### f1
- Mean = 0.424601029002349
- Standard deviation = 0.09700672610612358
- Max = 0.5306122448979592
- 75% = 0.48986486486486486
- Median = 0.4843597262952102
- 25% = 0.3334441489361702
- Min = 0.25806451612903225

#### precision
- Mean = 0.4356434699043725
- Standard deviation = 0.09545869730770039
- Max = 0.6153846153846154
- 75% = 0.47610294117647056
- Median = 0.43247126436781613
- 25% = 0.362012987012987
- Min = 0.2962962962962963

#### recall
- Mean = 0.45625
- Standard deviation = 0.17577951388031543
- Max = 0.75
- 75% = 0.5750000000000001
- Median = 0.42500000000000004
- 25% = 0.36250000000000004
- Min = 0.2

#### facing_probas
- Mean = [0.0910043  0.3811875  0.47367865 0.6773545  0.42501364]
- Standard deviation = [0.05310844 0.13451012 0.1930977  0.12818428 0.12065421]
- Max = [0.18227712 0.59801852 0.77521164 0.88412302 0.67221495]
- 75% = [0.11416567 0.49329812 0.65000926 0.73825761 0.46852017]
- Median = [0.10453472 0.36825231 0.42597057 0.68128638 0.42808499]
- 25% = [0.06405324 0.295187   0.33496081 0.62764385 0.35007788]
- Min = [0.01       0.17513558 0.23003373 0.42925926 0.25464286]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 67.25 | 12.75 |
| Actual Positive | 10.875 | 9.125 |

### robot-5
#### accuracy
- Mean = 0.84
- Standard deviation = 0.033911649915626334
- Max = 0.89
- 75% = 0.87
- Median = 0.84
- 25% = 0.8175
- Min = 0.78

#### f1
- Mean = 0.434981684981685
- Standard deviation = 0.12196305391505113
- Max = 0.6666666666666667
- 75% = 0.5185185185185185
- Median = 0.41428571428571426
- 25% = 0.3625356125356125
- Min = 0.26666666666666666

#### precision
- Mean = 0.7501144688644689
- Standard deviation = 0.1993983628479981
- Max = 1.0
- 75% = 0.8846153846153846
- Median = 0.7916666666666667
- 25% = 0.5928571428571429
- Min = 0.4

#### recall
- Mean = 0.3125
- Standard deviation = 0.1053268721647045
- Max = 0.55
- 75% = 0.35
- Median = 0.3
- 25% = 0.2375
- Min = 0.2

#### facing_probas
- Mean = [0.05584598 0.09137583 0.2915482  0.60295354 0.56289931]
- Standard deviation = [0.04249254 0.07305683 0.09661572 0.16957417 0.11709517]
- Max = [0.12472619 0.19531746 0.51401852 0.82530556 0.76728704]
- 75% = [0.08457804 0.17012351 0.32345933 0.69591766 0.60680308]
- Median = [0.05097817 0.05392593 0.26009193 0.69169279 0.54462996]
- 25% = [0.02191187 0.02987649 0.2319666  0.50154927 0.48160549]
- Min = [0.         0.015      0.17758267 0.27532077 0.39573148]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 77.75 | 2.25 |
| Actual Positive | 13.75 | 6.25 |

### robot-6
#### accuracy
- Mean = 0.3475
- Standard deviation = 0.10304731922762474
- Max = 0.47
- 75% = 0.415
- Median = 0.375
- 25% = 0.3125
- Min = 0.13

#### f1
- Mean = 0.5063081434289963
- Standard deviation = 0.12412645874396046
- Max = 0.6394557823129251
- 75% = 0.5865198631156078
- Median = 0.5445114851275537
- 25% = 0.4753550543024227
- Min = 0.23008849557522126

#### precision
- Mean = 1.0
- Standard deviation = 0.0
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 1.0
- Min = 1.0

#### recall
- Mean = 0.3475
- Standard deviation = 0.10304731922762474
- Max = 0.47
- 75% = 0.415
- Median = 0.375
- 25% = 0.3125
- Min = 0.13

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
| Actual Positive | 65.25 | 34.75 |

