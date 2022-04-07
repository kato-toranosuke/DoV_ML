# ExtraTreesClassifier_RandomOverSampler_2022-01-20-12-40_no3
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
	- n_estimators = 10
	- estimator_params = ('criterion', 'max_depth', 'min_samples_split', 'min_samples_leaf', 'min_weight_fraction_leaf', 'max_features', 'max_leaf_nodes', 'min_impurity_decrease', 'random_state', 'ccp_alpha')
	- bootstrap = True
	- oob_score = True
	- n_jobs = -1
	- random_state = 42
	- verbose = 0
	- warm_start = False
	- class_weight = None
	- max_samples = 0.5
	- criterion = gini
	- max_depth = None
	- min_samples_split = 2
	- min_samples_leaf = 5
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
	- oob_decision_function_ = [[0.08333333 0.91666667]
 [0.09722222 0.90277778]
 [0.         1.        ]
 [0.48888889 0.51111111]
 [0.05555556 0.94444444]
 [0.01388889 0.98611111]
 [0.49050708 0.50949292]
 [0.68453381 0.31546619]
 [0.51465674 0.48534326]
 [0.71626984 0.28373016]
 [0.90404583 0.09595417]
 [0.92857143 0.07142857]
 [0.93233083 0.06766917]
 [0.95166488 0.04833512]
 [1.         0.        ]
 [0.16111111 0.83888889]
 [0.44940476 0.55059524]
 [0.3468254  0.6531746 ]
 [0.1        0.9       ]
 [0.01041667 0.98958333]
 [0.025      0.975     ]
 [0.16315359 0.83684641]
 [0.30634921 0.69365079]
 [0.24666667 0.75333333]
 [0.26805556 0.73194444]
 [0.33492063 0.66507937]
 [0.04       0.96      ]
 [0.86395677 0.13604323]
 [0.94285714 0.05714286]
 [0.92445399 0.07554601]
 [0.70770677 0.29229323]
 [0.83249791 0.16750209]
 [0.69047619 0.30952381]
 [0.36904762 0.63095238]
 [0.23511905 0.76488095]
 [0.08333333 0.91666667]
 [0.01041667 0.98958333]
 [0.15312792 0.84687208]
 [0.2203159  0.7796841 ]
 [0.17013889 0.82986111]
 [0.22685185 0.77314815]
 [0.20915033 0.79084967]
 [0.61515694 0.38484306]
 [0.56251167 0.43748833]
 [0.61298699 0.38701301]
 [0.98611111 0.01388889]
 [0.57910401 0.42089599]
 [0.98057644 0.01942356]
 [0.61666667 0.38333333]
 [0.32947368 0.67052632]
 [0.3670068  0.6329932 ]
 [0.19642857 0.80357143]
 [0.05272109 0.94727891]
 [0.09722222 0.90277778]
 [0.13095238 0.86904762]
 [0.03571429 0.96428571]
 [0.12301587 0.87698413]
 [0.         1.        ]
 [0.19714286 0.80285714]
 [0.09791667 0.90208333]
 [0.98684211 0.01315789]
 [0.63888889 0.36111111]
 [0.8245614  0.1754386 ]
 [0.96741855 0.03258145]
 [0.97207304 0.02792696]
 [1.         0.        ]
 [0.55082454 0.44917546]
 [0.76111111 0.23888889]
 [0.89214107 0.10785893]
 [0.28011204 0.71988796]
 [0.2654902  0.7345098 ]
 [0.24019608 0.75980392]
 [0.05788982 0.94211018]
 [0.26437908 0.73562092]
 [0.29       0.71      ]
 [0.79010025 0.20989975]
 [0.88095238 0.11904762]
 [0.92857143 0.07142857]]
	- oob_score_ = 0.9230769230769231

#### Importance of features
- gp_auc_mean = 0.16833895509524802
- gp_auc_min = 0.14294467224866664
- gp_max_val_max = 0.11365333843225753
- gp_max_ix_range = 0.09958235081429143
- gp_max_val_mean = 0.09309769417475727
- high_power = 0.07832250661632703
- diff_std = 0.06524652963088275
- gp_max_val_std = 0.052560646900269535
- gp_max_val_min = 0.043847841648252464
- gp_max_ix_max = 0.04027815163750562
- gp_max_ix_std = 0.02613636363636363
- tdoa_std = 0.017988858112103573
- tdoa_range = 0.01775963517070767
- gp_max_ix_mean = 0.016067475673079014
- tdoa_max = 0.01236034434727269
- low_power = 0.005540756526371876
- coe1[0] = 0.004494680851063836
- gp_max_val_range = 0.0017791984845794192
- hlbr = 0.0
- coe1[1] = 0.0
- coe3[0] = 0.0
- coe3[1] = 0.0
- coe3[2] = 0.0
- coe3[3] = 0.0
- ratio_max_to_10ms_ave_peaks = 0.0
- ratio_max_to_9th_ave_peaks = 0.0
- ac_std = 0.0
- ac_auc = 0.0
- diff_auc = 0.0
- srmr = 0.0
- gp_max_ix_min = 0.0
- gp_auc_std = 0.0
- gp_auc_range = 0.0
- gp_auc_max = 0.0
- tdoa_min = 0.0
- tdoa_mean = 0.0

## Evaluation
cv = 8
### robot-1
#### accuracy
- Mean = 0.9612499999999999
- Standard deviation = 0.012686114456365286
- Max = 0.99
- 75% = 0.9624999999999999
- Median = 0.96
- 25% = 0.95
- Min = 0.95

#### f1
- Mean = 0.9045410687001725
- Standard deviation = 0.032995101190002055
- Max = 0.975609756097561
- 75% = 0.9111295681063123
- Median = 0.9023809523809524
- 25% = 0.8780487804878048
- Min = 0.8648648648648648

#### precision
- Mean = 0.8880851352398667
- Standard deviation = 0.0363110302865887
- Max = 0.9523809523809523
- 75% = 0.9102941176470588
- Median = 0.866600790513834
- 25% = 0.862012987012987
- Min = 0.8571428571428571

#### recall
- Mean = 0.9249999999999999
- Standard deviation = 0.061237243569579436
- Max = 1.0
- 75% = 0.9624999999999999
- Median = 0.925
- 25% = 0.9
- Min = 0.8

#### facing_probas
- Mean = [0.9151476  0.70488315 0.28100267 0.08474203 0.06418157]
- Standard deviation = [0.01936682 0.05080792 0.06106147 0.04106489 0.0424986 ]
- Max = [0.94258547 0.82366026 0.40762247 0.16620797 0.15987302]
- 75% = [0.92882932 0.71057962 0.31172393 0.10320819 0.07548944]
- Median = [0.91633837 0.69199565 0.26896978 0.07916689 0.0530168 ]
- 25% = [0.89557143 0.67913079 0.23943816 0.0570896  0.03400487]
- Min = [0.89127109 0.64969597 0.19921554 0.03401316 0.0222619 ]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 77.625 | 2.375 |
| Actual Positive | 1.5 | 18.5 |

### robot-2
#### accuracy
- Mean = 0.93375
- Standard deviation = 0.06040229714174783
- Max = 0.99
- 75% = 0.9624999999999999
- Median = 0.945
- 25% = 0.94
- Min = 0.78

#### f1
- Mean = 0.7952518666093762
- Standard deviation = 0.24589548860326604
- Max = 0.9743589743589743
- 75% = 0.9007823613086771
- Median = 0.8640243902439024
- 25% = 0.8480263157894736
- Min = 0.15384615384615383

#### precision
- Mean = 0.8404761904761904
- Standard deviation = 0.20053115095767332
- Max = 1.0
- 75% = 0.9583333333333333
- Median = 0.873015873015873
- 25% = 0.85
- Min = 0.3333333333333333

#### recall
- Mean = 0.76875
- Standard deviation = 0.25609751560684846
- Max = 0.95
- 75% = 0.8625
- Median = 0.85
- 25% = 0.8375
- Min = 0.1

#### facing_probas
- Mean = [0.8451849  0.88753519 0.69907317 0.37549332 0.05126733]
- Standard deviation = [0.0346705  0.03200071 0.05464674 0.09711063 0.0460163 ]
- Max = [0.89181025 0.93787465 0.82968959 0.60035191 0.15823665]
- 75% = [0.87547546 0.91200707 0.70317165 0.38068185 0.05679701]
- Median = [0.84603715 0.88979275 0.69243315 0.36544733 0.04263121]
- 25% = [0.81143979 0.85379367 0.67036926 0.34310359 0.01909656]
- Min = [0.80229796 0.84936111 0.6347619  0.23225919 0.00678571]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 78.0 | 2.0 |
| Actual Positive | 4.625 | 15.375 |

### robot-3
#### accuracy
- Mean = 0.9337500000000001
- Standard deviation = 0.01494782592887672
- Max = 0.95
- 75% = 0.9424999999999999
- Median = 0.935
- 25% = 0.93
- Min = 0.9

#### f1
- Mean = 0.8064935925230043
- Standard deviation = 0.05893204450635532
- Max = 0.8648648648648648
- 75% = 0.8412162162162162
- Median = 0.8171701112877583
- 25% = 0.796969696969697
- Min = 0.6666666666666666

#### precision
- Mean = 0.9544424019607843
- Standard deviation = 0.039541089714313235
- Max = 1.0
- 75% = 1.0
- Median = 0.9411764705882353
- 25% = 0.9364583333333334
- Min = 0.8823529411764706

#### recall
- Mean = 0.70625
- Standard deviation = 0.09164298936634488
- Max = 0.8
- 75% = 0.7625
- Median = 0.725
- 25% = 0.6875
- Min = 0.5

#### facing_probas
- Mean = [0.36802504 0.75504929 0.79067658 0.79072539 0.22126754]
- Standard deviation = [0.0587142  0.02405502 0.05185968 0.05485065 0.06240128]
- Max = [0.50091793 0.79043074 0.87513138 0.90597009 0.37228247]
- 75% = [0.38437351 0.76752887 0.82755832 0.81918044 0.22363999]
- Median = [0.36424734 0.75516744 0.78450853 0.77666908 0.21195406]
- 25% = [0.32354299 0.73991984 0.75537905 0.75293578 0.17949432]
- Min = [0.2961891  0.72166484 0.71882295 0.7288315  0.15658196]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 79.25 | 0.75 |
| Actual Positive | 5.875 | 14.125 |

### robot-4
#### accuracy
- Mean = 0.7975000000000001
- Standard deviation = 0.07378177281686853
- Max = 0.88
- 75% = 0.86
- Median = 0.795
- 25% = 0.785
- Min = 0.63

#### f1
- Mean = 0.25299783642386536
- Standard deviation = 0.22004753153302914
- Max = 0.5714285714285715
- 75% = 0.4615384615384615
- Median = 0.26473859844271413
- 25% = 0.0
- Min = 0.0

#### precision
- Mean = 0.4734848484848485
- Standard deviation = 0.43649448269727387
- Max = 1.0
- 75% = 1.0
- Median = 0.3939393939393939
- 25% = 0.0
- Min = 0.0

#### recall
- Mean = 0.175
- Standard deviation = 0.15
- Max = 0.4
- 75% = 0.3
- Median = 0.2
- 25% = 0.0
- Min = 0.0

#### facing_probas
- Mean = [0.08798587 0.56952442 0.73404163 0.88588613 0.6164787 ]
- Standard deviation = [0.05719874 0.07738409 0.05436603 0.0341268  0.08006185]
- Max = [0.22169048 0.69119633 0.82710072 0.94109596 0.72896118]
- 75% = [0.09822844 0.63446719 0.77568413 0.91030736 0.70392036]
- Median = [0.07053634 0.53211099 0.7117152  0.87884652 0.58533324]
- 25% = [0.06526689 0.51460121 0.70734554 0.85669246 0.56768315]
- Min = [0.01267857 0.47512363 0.64741087 0.84472619 0.51203584]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 76.25 | 3.75 |
| Actual Positive | 16.5 | 3.5 |

### robot-5
#### accuracy
- Mean = 0.95625
- Standard deviation = 0.054529235277968095
- Max = 1.0
- 75% = 0.99
- Median = 0.99
- 25% = 0.93
- Min = 0.83

#### f1
- Mean = 0.8417578798013581
- Standard deviation = 0.2341500365229194
- Max = 1.0
- 75% = 0.9743589743589743
- Median = 0.9743589743589743
- 25% = 0.787878787878788
- Min = 0.2608695652173913

#### precision
- Mean = 1.0
- Standard deviation = 0.0
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 1.0
- Min = 1.0

#### recall
- Mean = 0.78125
- Standard deviation = 0.27264617638984046
- Max = 1.0
- 75% = 0.95
- Median = 0.95
- 25% = 0.65
- Min = 0.15

#### facing_probas
- Mean = [0.06140109 0.08692033 0.33862147 0.84224711 0.69401042]
- Standard deviation = [0.04520627 0.05210746 0.08670299 0.05388162 0.05537038]
- Max = [0.15987302 0.20396465 0.54697613 0.9263784  0.75123736]
- 75% = [0.07368646 0.09392387 0.35327642 0.8956047  0.74562377]
- Median = [0.05782488 0.07394248 0.31544961 0.829162   0.7051345 ]
- 25% = [0.03401208 0.06453737 0.27819004 0.80339286 0.65845586]
- Min = [0.00488095 0.01327381 0.25638004 0.76696825 0.59223687]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 80.0 | 0.0 |
| Actual Positive | 4.375 | 15.625 |

### robot-6
#### accuracy
- Mean = 0.67125
- Standard deviation = 0.1415483574613284
- Max = 0.78
- 75% = 0.7525
- Median = 0.71
- 25% = 0.6775
- Min = 0.31

#### f1
- Mean = 0.7928604825236765
- Standard deviation = 0.12338454174544801
- Max = 0.8764044943820225
- 75% = 0.8587662337662337
- Median = 0.8302493415877141
- 25% = 0.8077416595380668
- Min = 0.47328244274809156

#### precision
- Mean = 1.0
- Standard deviation = 0.0
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 1.0
- Min = 1.0

#### recall
- Mean = 0.67125
- Standard deviation = 0.1415483574613284
- Max = 0.78
- 75% = 0.7525
- Median = 0.71
- 25% = 0.6775
- Min = 0.31

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
| Actual Positive | 32.875 | 67.125 |

