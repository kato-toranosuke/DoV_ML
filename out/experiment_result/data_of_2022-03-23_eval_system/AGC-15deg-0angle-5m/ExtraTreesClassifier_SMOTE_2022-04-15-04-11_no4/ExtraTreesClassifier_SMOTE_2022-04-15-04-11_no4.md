# ExtraTreesClassifier_SMOTE_2022-04-15-04-11_no4
## Constants
- CSV_PATH = ../out/csv/experiment
- OUTPUT_PATH = ../out/experiment_result/data_of_2022-03-23_eval_system/AGC-15deg-0angle-5m
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
- DISTANCE = [5]
- AGC_STATUS = ['AGC-15deg']
- ANGLES = [60, 75, 90, 105, 120]

## Loaded CSV
- 2022-03-23_raspi_48000Hz_w1_N2^12_overlap80_all.csv

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
	- sampling_strategy_ = OrderedDict([(1, 45)])
	- nn_k_ = NearestNeighbors(n_neighbors=6)

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
	- min_samples_split = 2
	- min_samples_leaf = 10
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
- gp_max_ix_mean = 0.09574428059876769
- ratio_max_to_9th_ave_peaks = 0.09136353338476526
- tdoa_std = 0.06014912497346129
- tdoa_mean = 0.058700511004229926
- gp_auc_min = 0.05546211179849206
- gp_auc_std = 0.05541154172216088
- gp_max_ix_std = 0.05284260527707132
- tdoa_max = 0.04194486047657279
- gp_max_val_min = 0.03819530781317934
- gp_max_val_max = 0.036336122668558034
- diff_std = 0.035734074198150674
- gp_auc_mean = 0.03459870667139278
- gp_max_val_std = 0.03113191751369784
- high_power = 0.029907074493442168
- low_power = 0.02474640471127027
- hlbr = 0.022346146140238887
- coe1[0] = 0.022042302203509036
- gp_auc_max = 0.02070732198598141
- gp_max_val_mean = 0.02016942897127148
- diff_auc = 0.01867901029415359
- gp_max_ix_min = 0.018272695327444632
- gp_max_ix_max = 0.01764916787765455
- tdoa_range = 0.016148492557568644
- gp_max_ix_range = 0.015941076571382003
- srmr = 0.014982810835111646
- gp_auc_range = 0.013490223392888594
- tdoa_min = 0.010767929824293074
- coe3[2] = 0.00979466860675061
- ac_std = 0.008528524793066613
- gp_max_val_range = 0.008158974142857397
- coe3[3] = 0.0071363499318587
- ac_auc = 0.006417862677746753
- ratio_max_to_10ms_ave_peaks = 0.00443404555730038
- coe1[1] = 0.002064791003709802
- coe3[0] = 0.0
- coe3[1] = 0.0

## Evaluation
cv = 8
### robot-1
#### accuracy
- Mean = 0.8125
- Standard deviation = 0.012990381056766545
- Max = 0.84
- 75% = 0.82
- Median = 0.81
- 25% = 0.8
- Min = 0.8

#### f1
- Mean = 0.24839099753874339
- Standard deviation = 0.19511136461456488
- Max = 0.47058823529411764
- 75% = 0.39032258064516123
- Median = 0.3647214854111406
- 25% = 0.0
- Min = 0.0

#### precision
- Mean = 0.38822150072150075
- Standard deviation = 0.31253204319224925
- Max = 0.8333333333333334
- 75% = 0.5785714285714285
- Median = 0.5505050505050505
- 25% = 0.0
- Min = 0.0

#### recall
- Mean = 0.1875
- Standard deviation = 0.15155444566227677
- Max = 0.4
- 75% = 0.3
- Median = 0.25
- 25% = 0.0
- Min = 0.0

#### facing_probas
- Mean = [0.40839045 0.35717377 0.30906676 0.2661918  0.24654949]
- Standard deviation = [0.03925135 0.04659971 0.04332488 0.04611985 0.04266439]
- Max = [0.47364634 0.40768132 0.37593935 0.34160934 0.30813344]
- 75% = [0.43967632 0.39060062 0.33463372 0.29289345 0.27673916]
- Median = [0.40575319 0.37573066 0.30010908 0.25744343 0.24156208]
- 25% = [0.37394177 0.33116747 0.27518783 0.22847664 0.21533327]
- Min = [0.35225589 0.2744923  0.25143091 0.20470434 0.18346747]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 77.5 | 2.5 |
| Actual Positive | 16.25 | 3.75 |

### robot-2
#### accuracy
- Mean = 0.8162499999999999
- Standard deviation = 0.08859140759689961
- Max = 0.91
- 75% = 0.87
- Median = 0.83
- 25% = 0.8075
- Min = 0.61

#### f1
- Mean = 0.5944999270424512
- Standard deviation = 0.1400889621493065
- Max = 0.7906976744186046
- 75% = 0.6719052224371374
- Median = 0.6099033816425121
- 25% = 0.5041908446163766
- Min = 0.3389830508474576

#### precision
- Mean = 0.568152522296544
- Standard deviation = 0.14953509803329773
- Max = 0.7391304347826086
- 75% = 0.6927083333333334
- Median = 0.5854700854700855
- 25% = 0.5149572649572649
- Min = 0.2564102564102564

#### recall
- Mean = 0.6499999999999999
- Standard deviation = 0.1541103500742244
- Max = 0.85
- 75% = 0.775
- Median = 0.6499999999999999
- 25% = 0.5375000000000001
- Min = 0.4

#### facing_probas
- Mean = [0.5162032  0.60803498 0.5154892  0.55593805 0.39049962]
- Standard deviation = [0.04335331 0.03416807 0.0318932  0.04292695 0.03676604]
- Max = [0.60684978 0.67092145 0.56906708 0.60192988 0.4666976 ]
- 75% = [0.52952606 0.62416302 0.5384252  0.57855465 0.4093436 ]
- Median = [0.51270506 0.6096475  0.5097411  0.56149589 0.38042689]
- 25% = [0.4798206  0.58925672 0.49066189 0.54940864 0.36866333]
- Min = [0.46443119 0.54812607 0.47202218 0.45484649 0.33790697]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 68.625 | 11.375 |
| Actual Positive | 7.0 | 13.0 |

### robot-3
#### accuracy
- Mean = 0.7987500000000001
- Standard deviation = 0.02087911636061256
- Max = 0.82
- 75% = 0.82
- Median = 0.8
- 25% = 0.7875000000000001
- Min = 0.76

#### f1
- Mean = 0.11483423983423985
- Standard deviation = 0.10451494365326591
- Max = 0.29629629629629634
- 75% = 0.18181818181818182
- Median = 0.12937062937062938
- 25% = 0.0
- Min = 0.0

#### precision
- Mean = 0.46726190476190477
- Standard deviation = 0.4482798914864586
- Max = 1.0
- 75% = 1.0
- Median = 0.369047619047619
- 25% = 0.0
- Min = 0.0

#### recall
- Mean = 0.06875
- Standard deviation = 0.06584783595532961
- Max = 0.2
- 75% = 0.1
- Median = 0.07500000000000001
- 25% = 0.0
- Min = 0.0

#### facing_probas
- Mean = [0.44827249 0.52049529 0.48542292 0.50305911 0.37349745]
- Standard deviation = [0.04481609 0.02846282 0.02548332 0.03626848 0.03720663]
- Max = [0.50504529 0.56303564 0.52910624 0.54859878 0.42656244]
- 75% = [0.48631215 0.53896909 0.50214642 0.53091425 0.40376176]
- Median = [0.4559794  0.51662555 0.48449169 0.50658312 0.37524772]
- 25% = [0.40533192 0.4991758  0.47236902 0.4901408  0.34306727]
- Min = [0.3835984  0.48188871 0.43921331 0.42895923 0.31969831]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 78.5 | 1.5 |
| Actual Positive | 18.625 | 1.375 |

### robot-4
#### accuracy
- Mean = 0.6725
- Standard deviation = 0.0631961232988227
- Max = 0.81
- 75% = 0.705
- Median = 0.645
- 25% = 0.6275
- Min = 0.61

#### f1
- Mean = 0.4077226875341299
- Standard deviation = 0.12811041452837005
- Max = 0.5483870967741935
- 75% = 0.5136476426799008
- Median = 0.43186475409836067
- 25% = 0.3678092399403875
- Min = 0.13636363636363635

#### precision
- Mean = 0.324192427437774
- Standard deviation = 0.11206451541466311
- Max = 0.5263157894736842
- 75% = 0.38690476190476186
- Median = 0.31762749445676275
- 25% = 0.27665505226480835
- Min = 0.125

#### recall
- Mean = 0.5812499999999999
- Standard deviation = 0.21350863565673403
- Max = 0.85
- 75% = 0.725
- Median = 0.625
- 25% = 0.475
- Min = 0.15

#### facing_probas
- Mean = [0.41739907 0.50376467 0.50594364 0.56338781 0.4545018 ]
- Standard deviation = [0.04645367 0.03761824 0.02333229 0.03015743 0.02747567]
- Max = [0.48099055 0.57965549 0.54396199 0.60177086 0.52023467]
- 75% = [0.46308049 0.51580255 0.52396921 0.58515723 0.46165413]
- Median = [0.41100314 0.4950796  0.50429109 0.56713759 0.44710166]
- 25% = [0.38658118 0.48054722 0.48626644 0.55036431 0.43358137]
- Min = [0.34906484 0.45078898 0.47392904 0.50833902 0.430677  ]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 55.625 | 24.375 |
| Actual Positive | 8.375 | 11.625 |

### robot-5
#### accuracy
- Mean = 0.7925
- Standard deviation = 0.014790199457749053
- Max = 0.81
- 75% = 0.8
- Median = 0.8
- 25% = 0.7875000000000001
- Min = 0.76

#### f1
- Mean = 0.04302536231884059
- Standard deviation = 0.061178196062755597
- Max = 0.1739130434782609
- 75% = 0.08423913043478262
- Median = 0.0
- 25% = 0.0
- Min = 0.0

#### precision
- Mean = 0.15625
- Standard deviation = 0.2298757967782699
- Max = 0.6666666666666666
- 75% = 0.2708333333333333
- Median = 0.0
- 25% = 0.0
- Min = 0.0

#### recall
- Mean = 0.025
- Standard deviation = 0.03535533905932738
- Max = 0.1
- 75% = 0.05
- Median = 0.0
- 25% = 0.0
- Min = 0.0

#### facing_probas
- Mean = [0.32296184 0.40305735 0.44203664 0.53733093 0.41853937]
- Standard deviation = [0.05321012 0.05304145 0.02115953 0.04259922 0.04080254]
- Max = [0.40287463 0.50865028 0.46555959 0.58481026 0.48872625]
- 75% = [0.37199422 0.42263745 0.45785639 0.55786052 0.45111254]
- Median = [0.31888728 0.40256329 0.4520208  0.55551207 0.41406091]
- 25% = [0.28058317 0.36154523 0.41997229 0.53201683 0.37893532]
- Min = [0.25221178 0.34019202 0.41128426 0.4372018  0.37125358]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 78.75 | 1.25 |
| Actual Positive | 19.5 | 0.5 |

### robot-6
#### accuracy
- Mean = 0.3025
- Standard deviation = 0.048412291827592706
- Max = 0.36
- 75% = 0.3425
- Median = 0.31
- 25% = 0.275
- Min = 0.21

#### f1
- Mean = 0.4623189781388802
- Standard deviation = 0.05848268922043045
- Max = 0.5294117647058824
- 75% = 0.5102266445550028
- Median = 0.4729265023022673
- 25% = 0.43129960317460325
- Min = 0.34710743801652894

#### precision
- Mean = 1.0
- Standard deviation = 0.0
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 1.0
- Min = 1.0

#### recall
- Mean = 0.3025
- Standard deviation = 0.048412291827592706
- Max = 0.36
- 75% = 0.3425
- Median = 0.31
- 25% = 0.275
- Min = 0.21

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
| Actual Positive | 69.75 | 30.25 |

