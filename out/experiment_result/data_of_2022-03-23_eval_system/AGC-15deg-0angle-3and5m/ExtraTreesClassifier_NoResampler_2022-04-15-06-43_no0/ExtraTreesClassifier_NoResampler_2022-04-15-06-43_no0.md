# ExtraTreesClassifier_NoResampler_2022-04-15-06-43_no0
## Constants
- CSV_PATH = ../out/csv/experiment
- OUTPUT_PATH = ../out/experiment_result/data_of_2022-03-23_eval_system/AGC-15deg-0angle-3and5m
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
- DISTANCE = [3, 5]
- AGC_STATUS = ['AGC-15deg']
- ANGLES = [60, 75, 90, 105, 120]

## Loaded CSV
- 2022-03-23_raspi_48000Hz_w1_N2^12_overlap80_all.csv

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
	- n_estimators = 70
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
- ratio_max_to_9th_ave_peaks = 0.05320128582710079
- diff_std = 0.04713284537394881
- hlbr = 0.04327770330804535
- srmr = 0.04293252450651554
- gp_max_val_min = 0.040025320046994634
- gp_max_val_std = 0.03956892485950794
- ratio_max_to_10ms_ave_peaks = 0.03854238350598645
- gp_auc_range = 0.03853396395369663
- gp_auc_min = 0.037933804279428995
- high_power = 0.037354990469953046
- low_power = 0.035908873327594036
- gp_auc_std = 0.034824962382232774
- diff_auc = 0.033164343143776726
- ac_auc = 0.03290995705605777
- gp_max_ix_std = 0.03236445705837403
- gp_auc_max = 0.031697296500660006
- coe1[1] = 0.03109272745407365
- gp_auc_mean = 0.030922743949186187
- coe1[0] = 0.028942018547749544
- coe3[2] = 0.027395873596054023
- gp_max_val_range = 0.027086293731257285
- tdoa_std = 0.025225676576606428
- gp_max_val_max = 0.025206936174379885
- gp_max_val_mean = 0.02515371278537558
- ac_std = 0.024245522192827343
- coe3[3] = 0.024168856266604487
- tdoa_mean = 0.019876450037981497
- tdoa_max = 0.016443926838113396
- gp_max_ix_max = 0.016353716956193413
- gp_max_ix_mean = 0.016109026011122685
- gp_max_ix_min = 0.012772584729671127
- tdoa_min = 0.012579264530090513
- gp_max_ix_range = 0.009758412032701863
- tdoa_range = 0.007292621990137568
- coe3[0] = 0.0
- coe3[1] = 0.0

## Evaluation
cv = 8
### robot-1
#### accuracy
- Mean = 0.7987500000000001
- Standard deviation = 0.020116846174288827
- Max = 0.82
- 75% = 0.8162499999999999
- Median = 0.8
- 25% = 0.79
- Min = 0.755

#### f1
- Mean = 0.1415274673699267
- Standard deviation = 0.08465162279112169
- Max = 0.24999999999999997
- 75% = 0.2220744680851064
- Median = 0.14250000000000002
- 25% = 0.047619047619047616
- Min = 0.03921568627450981

#### precision
- Mean = 0.5100243506493507
- Standard deviation = 0.21304190855329266
- Max = 0.75
- 75% = 0.7232142857142857
- Median = 0.5
- 25% = 0.39375000000000004
- Min = 0.09090909090909091

#### recall
- Mean = 0.084375
- Standard deviation = 0.051443992603607276
- Max = 0.15
- 75% = 0.13125
- Median = 0.0875
- 25% = 0.025
- Min = 0.025

#### facing_probas
- Mean = [0.2657937  0.19932178 0.17375358 0.12994404 0.09262982]
- Standard deviation = [0.03530009 0.03765335 0.04354032 0.04876    0.03745363]
- Max = [0.32990334 0.26665632 0.25031803 0.21433149 0.1828322 ]
- 75% = [0.28178738 0.21651598 0.18877236 0.15836412 0.09354468]
- Median = [0.26294501 0.18859269 0.16349632 0.12934184 0.08404216]
- 25% = [0.24399238 0.17346918 0.14507674 0.08626027 0.07467028]
- Min = [0.21534963 0.15110544 0.11641199 0.06737514 0.05512954]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 156.375 | 3.625 |
| Actual Positive | 36.625 | 3.375 |

### robot-2
#### accuracy
- Mean = 0.804375
- Standard deviation = 0.02006824294750287
- Max = 0.83
- 75% = 0.82
- Median = 0.81
- 25% = 0.79
- Min = 0.775

#### f1
- Mean = 0.3358504281608472
- Standard deviation = 0.09834227656555851
- Max = 0.47058823529411764
- 75% = 0.4129032258064516
- Median = 0.3497652582159625
- 25% = 0.24354066985645934
- Min = 0.2

#### precision
- Mean = 0.5237015040620354
- Standard deviation = 0.0992800368742586
- Max = 0.6428571428571429
- 75% = 0.6090909090909091
- Median = 0.5357142857142857
- 25% = 0.45483870967741935
- Min = 0.35294117647058826

#### recall
- Mean = 0.25625
- Standard deviation = 0.09499177595981666
- Max = 0.4
- 75% = 0.33125
- Median = 0.2625
- 25% = 0.16874999999999998
- Min = 0.125

#### facing_probas
- Mean = [0.27646779 0.39687764 0.27267653 0.25268603 0.14930499]
- Standard deviation = [0.08388122 0.04216732 0.04006955 0.03309978 0.02492908]
- Max = [0.41176205 0.47455201 0.33034141 0.30231973 0.20940023]
- 75% = [0.34872846 0.41262886 0.29677849 0.27794306 0.15166373]
- Median = [0.25527934 0.39457341 0.28509821 0.25793467 0.14253139]
- 25% = [0.19389668 0.37246071 0.24971124 0.21692584 0.13226516]
- Min = [0.18426516 0.32685969 0.20102126 0.21365774 0.1272381 ]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 150.625 | 9.375 |
| Actual Positive | 29.75 | 10.25 |

### robot-3
#### accuracy
- Mean = 0.79
- Standard deviation = 0.01887458608817689
- Max = 0.805
- 75% = 0.805
- Median = 0.8
- 25% = 0.77875
- Min = 0.75

#### f1
- Mean = 0.08947443728893509
- Standard deviation = 0.029477765754989123
- Max = 0.13793103448275865
- 75% = 0.09917920656634746
- Median = 0.09302325581395349
- 25% = 0.07886178861788619
- Min = 0.04347826086956522

#### precision
- Mean = 0.5077020202020202
- Standard deviation = 0.26990351561068304
- Max = 1.0
- 75% = 0.6666666666666666
- Median = 0.5333333333333333
- 25% = 0.26010101010101006
- Min = 0.16666666666666666

#### recall
- Mean = 0.053125000000000006
- Standard deviation = 0.023175620272173948
- Max = 0.1
- 75% = 0.05625
- Median = 0.05
- 25% = 0.043750000000000004
- Min = 0.025

#### facing_probas
- Mean = [0.23792427 0.34786632 0.31119228 0.28217699 0.20686628]
- Standard deviation = [0.03433464 0.05370064 0.03298081 0.04703566 0.01656199]
- Max = [0.28784807 0.45017489 0.36535402 0.33201134 0.24333333]
- 75% = [0.27733092 0.37220203 0.32779758 0.32310201 0.21029439]
- Median = [0.22212032 0.32447137 0.3004015  0.29925227 0.2086143 ]
- 25% = [0.20796329 0.32023696 0.29489332 0.24909701 0.19539757]
- Min = [0.20020621 0.27244388 0.26236565 0.19427239 0.18379861]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 155.875 | 4.125 |
| Actual Positive | 37.875 | 2.125 |

### robot-4
#### accuracy
- Mean = 0.784375
- Standard deviation = 0.03530558560624651
- Max = 0.825
- 75% = 0.805
- Median = 0.7925
- 25% = 0.77875
- Min = 0.7

#### f1
- Mean = 0.13070455655161795
- Standard deviation = 0.11138778229745855
- Max = 0.3137254901960785
- 75% = 0.2412854030501089
- Median = 0.07206632653061225
- 25% = 0.047696476964769655
- Min = 0.0

#### precision
- Mean = 0.40978535353535356
- Standard deviation = 0.3219823663084683
- Max = 1.0
- 75% = 0.5909090909090908
- Median = 0.3611111111111111
- 25% = 0.17083333333333334
- Min = 0.0

#### recall
- Mean = 0.084375
- Standard deviation = 0.07281987623581902
- Max = 0.2
- 75% = 0.15625
- Median = 0.05
- 25% = 0.025
- Min = 0.0

#### facing_probas
- Mean = [0.23686093 0.26646717 0.28337656 0.30213427 0.22654202]
- Standard deviation = [0.01976503 0.03235153 0.03505307 0.02163622 0.02551957]
- Max = [0.25959226 0.33000383 0.35751814 0.34048852 0.27067971]
- 75% = [0.2496194  0.2806526  0.29213202 0.31603295 0.23969636]
- Median = [0.24455506 0.26762798 0.28830938 0.30052884 0.21798484]
- 25% = [0.22565675 0.2451042  0.26224759 0.29055584 0.20817127]
- Min = [0.19666525 0.21414683 0.22982171 0.2705951  0.19461961]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 153.5 | 6.5 |
| Actual Positive | 36.625 | 3.375 |

### robot-5
#### accuracy
- Mean = 0.794375
- Standard deviation = 0.005266343608235228
- Max = 0.805
- 75% = 0.795
- Median = 0.795
- 25% = 0.7937500000000001
- Min = 0.785

#### f1
- Mean = 0.017467070019537408
- Standard deviation = 0.02257594926707082
- Max = 0.04878048780487806
- 75% = 0.044961240310077526
- Median = 0.0
- 25% = 0.0
- Min = 0.0

#### precision
- Mean = 0.19166666666666665
- Standard deviation = 0.3273419890233726
- Max = 1.0
- 75% = 0.23333333333333334
- Median = 0.0
- 25% = 0.0
- Min = 0.0

#### recall
- Mean = 0.009375000000000001
- Standard deviation = 0.012103072956898178
- Max = 0.025
- 75% = 0.025
- Median = 0.0
- 25% = 0.0
- Min = 0.0

#### facing_probas
- Mean = [0.11882437 0.14912902 0.22225083 0.23873521 0.18103045]
- Standard deviation = [0.01674743 0.02080447 0.03592597 0.02376394 0.02867784]
- Max = [0.13795762 0.17781264 0.28916837 0.29186536 0.249071  ]
- 75% = [0.13314658 0.16454457 0.23429656 0.24461288 0.18072233]
- Median = [0.12276786 0.15685367 0.21882993 0.23214024 0.1730467 ]
- 25% = [0.10766022 0.12476559 0.20614328 0.22736299 0.16530981]
- Min = [0.08971599 0.12111395 0.16771358 0.20621528 0.15038974]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 158.5 | 1.5 |
| Actual Positive | 39.625 | 0.375 |

### robot-6
#### accuracy
- Mean = 0.0975
- Standard deviation = 0.03020761493398643
- Max = 0.135
- 75% = 0.12625
- Median = 0.0975
- 25% = 0.075
- Min = 0.045

#### f1
- Mean = 0.1762838219445267
- Standard deviation = 0.050613982527111065
- Max = 0.2378854625550661
- 75% = 0.22418879056047197
- Median = 0.17744011292398387
- 25% = 0.13953488372093023
- Min = 0.0861244019138756

#### precision
- Mean = 1.0
- Standard deviation = 0.0
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 1.0
- Min = 1.0

#### recall
- Mean = 0.0975
- Standard deviation = 0.03020761493398643
- Max = 0.135
- 75% = 0.12625
- Median = 0.0975
- 25% = 0.075
- Min = 0.045

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
| Actual Positive | 180.5 | 19.5 |

