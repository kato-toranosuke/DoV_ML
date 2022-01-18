# ExtraTreesClassifier_RandomOverSampler_2022-01-17-11-43_no3
## Constants
- CSV_PATH = ../out/csv/experiment
- OUTPUT_PATH = ../out/experiment_result/data_of_2022-01-13_eval_system/AGC-0angle-5m
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
- AGC_STATUS = ['AGC']

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
	- sampling_strategy_ = OrderedDict([(1, 45)])
	- shrinkage_ = None
	- sample_indices_ = [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23
 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47
 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71
 72 73 74 26 18 62 74 50 37 62 24 26 49 12 26 50 50 37 24 18 37 37 12 25
 24  6 37 61 73 25  6 61 24  0 61 49 25 62 61 38  0 50 50 74 49 61 61 74]

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
- gp_auc_max = 0.11702845091547491
- gp_max_val_mean = 0.1099476758789109
- gp_auc_min = 0.1014485373106331
- high_power = 0.10019510523426846
- gp_auc_mean = 0.0966612484376819
- gp_max_val_min = 0.0832284911714549
- gp_max_val_max = 0.04791935873768546
- ratio_max_to_9th_ave_peaks = 0.034454024139908945
- hlbr = 0.030237042528912978
- diff_auc = 0.029261216260869877
- srmr = 0.02500261581668351
- ratio_max_to_10ms_ave_peaks = 0.023710731033924497
- diff_std = 0.023078628404897158
- tdoa_max = 0.015180436403925269
- coe3[2] = 0.014792979250945174
- gp_auc_std = 0.014636736846491928
- gp_max_ix_max = 0.0129412521244349
- gp_auc_range = 0.010816792241961979
- ac_auc = 0.010586879016135168
- tdoa_mean = 0.010506618937014987
- low_power = 0.009444220815598823
- tdoa_range = 0.008807778535136805
- gp_max_ix_range = 0.008732510730885629
- gp_max_val_std = 0.008248011385121583
- coe3[3] = 0.007742178662357734
- coe1[0] = 0.007607209875206141
- gp_max_ix_min = 0.007132706913828185
- tdoa_std = 0.006338454916603445
- gp_max_val_range = 0.0053461088239391144
- tdoa_min = 0.005215754565152391
- gp_max_ix_mean = 0.00407045863507541
- coe1[1] = 0.0038049365531669915
- gp_max_ix_std = 0.003518824685043962
- ac_std = 0.0023560242106677584
- coe3[0] = 0.0
- coe3[1] = 0.0

## Evaluation
cv = 8
### robot-1
#### accuracy
- Mean = 0.9500000000000001
- Standard deviation = 0.02345207879911712
- Max = 0.98
- 75% = 0.965
- Median = 0.955
- 25% = 0.93
- Min = 0.91

#### f1
- Mean = 0.8553858375165676
- Standard deviation = 0.07853412061421147
- Max = 0.9473684210526316
- 75% = 0.9154135338345865
- Median = 0.873015873015873
- 25% = 0.796969696969697
- Min = 0.7096774193548387

#### precision
- Mean = 0.9746212121212121
- Standard deviation = 0.04728480566364105
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 0.9833333333333334
- Min = 0.8636363636363636

#### recall
- Mean = 0.775
- Standard deviation = 0.12990381056766578
- Max = 0.95
- 75% = 0.9
- Median = 0.775
- 25% = 0.6875
- Min = 0.55

#### facing_probas
- Mean = [6.82466104e-01 1.71197090e-01 6.41245040e-03 2.88988095e-03
 3.49702381e-04]
- Standard deviation = [0.07367323 0.03312288 0.0036262  0.002935   0.00047287]
- Max = [0.83732143 0.22367989 0.01218254 0.00904762 0.00125   ]
- 75% = [0.71141088 0.19798562 0.00868899 0.00350298 0.00074405]
- Median = [0.67285648 0.1685506  0.00484921 0.00215278 0.        ]
- 25% = [0.65175463 0.14415063 0.00364583 0.00083333 0.        ]
- Min = [0.56464484 0.12681283 0.00263889 0.         0.        ]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 79.5 | 0.5 |
| Actual Positive | 4.5 | 15.5 |

### robot-2
#### accuracy
- Mean = 0.9099999999999999
- Standard deviation = 0.022360679774997873
- Max = 0.95
- 75% = 0.9175
- Median = 0.905
- 25% = 0.8975
- Min = 0.88

#### f1
- Mean = 0.7212573585066016
- Standard deviation = 0.07902089692302934
- Max = 0.8571428571428571
- 75% = 0.7585139318885448
- Median = 0.7096774193548387
- 25% = 0.6718749999999999
- Min = 0.6206896551724138

#### precision
- Mean = 0.9409722222222222
- Standard deviation = 0.08383816991423358
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 0.8958333333333333
- Min = 0.7777777777777778

#### recall
- Mean = 0.59375
- Standard deviation = 0.10135796712641783
- Max = 0.75
- 75% = 0.7
- Median = 0.55
- 25% = 0.5375000000000001
- Min = 0.45

#### facing_probas
- Mean = [0.30407722 0.59067303 0.08711516 0.01034854 0.00066667]
- Standard deviation = [0.06480748 0.04686816 0.03984483 0.00961324 0.00176383]
- Max = [0.3874795  0.66650661 0.15810119 0.03472817 0.00533333]
- 75% = [0.34637649 0.61749835 0.11009392 0.009729   0.        ]
- Median = [0.31590509 0.58703968 0.07029431 0.00781746 0.        ]
- 25% = [0.27171594 0.5652667  0.06196627 0.00625    0.        ]
- Min = [0.17500595 0.51441667 0.04062963 0.00092593 0.        ]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 79.125 | 0.875 |
| Actual Positive | 8.125 | 11.875 |

### robot-3
#### accuracy
- Mean = 0.97375
- Standard deviation = 0.025950674365033368
- Max = 1.0
- 75% = 1.0
- Median = 0.98
- 25% = 0.955
- Min = 0.93

#### f1
- Mean = 0.9314018218623482
- Standard deviation = 0.0685727972031309
- Max = 1.0
- 75% = 1.0
- Median = 0.9486842105263158
- 25% = 0.8833333333333333
- Min = 0.8205128205128205

#### precision
- Mean = 0.9537006578947369
- Standard deviation = 0.0549863224895475
- Max = 1.0
- 75% = 1.0
- Median = 0.975
- 25% = 0.928125
- Min = 0.8421052631578947

#### recall
- Mean = 0.9125
- Standard deviation = 0.08926785535678562
- Max = 1.0
- 75% = 1.0
- Median = 0.925
- 25% = 0.875
- Min = 0.75

#### facing_probas
- Mean = [0.01740881 0.46012938 0.74241832 0.21050752 0.00422313]
- Standard deviation = [0.01085382 0.03365715 0.07965319 0.04043865 0.00125008]
- Max = [0.04338294 0.50455026 0.85531019 0.27206481 0.00622817]
- 75% = [0.02011706 0.48883631 0.80590311 0.2424289  0.00513228]
- Median = [0.01336012 0.46237864 0.74189881 0.21607903 0.00421627]
- 25% = [0.01112517 0.42661177 0.69039964 0.1695119  0.00307143]
- Min = [0.00638889 0.41705291 0.6112791  0.15606349 0.0025    ]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 79.125 | 0.875 |
| Actual Positive | 1.75 | 18.25 |

### robot-4
#### accuracy
- Mean = 0.9075
- Standard deviation = 0.0323071199583002
- Max = 0.97
- 75% = 0.9175
- Median = 0.905
- 25% = 0.8875
- Min = 0.86

#### f1
- Mean = 0.7606077983496714
- Standard deviation = 0.09217067706978872
- Max = 0.9189189189189189
- 75% = 0.8042763157894738
- Median = 0.7629937629937629
- 25% = 0.7134615384615385
- Min = 0.588235294117647

#### precision
- Mean = 0.7914489041230528
- Standard deviation = 0.10250698609528035
- Max = 1.0
- 75% = 0.8398692810457515
- Median = 0.763157894736842
- 25% = 0.7107142857142857
- Min = 0.6785714285714286

#### recall
- Mean = 0.7437499999999999
- Standard deviation = 0.12358574958303242
- Max = 0.95
- 75% = 0.8125
- Median = 0.725
- 25% = 0.7
- Min = 0.5

#### facing_probas
- Mean = [0.00133639 0.0170391  0.37547908 0.71255969 0.17293411]
- Standard deviation = [0.00150247 0.00662916 0.03731666 0.0560617  0.03603118]
- Max = [0.004      0.02873677 0.46225066 0.81114616 0.23921296]
- 75% = [0.00257788 0.02027447 0.38152315 0.74627712 0.1919494 ]
- Median = [6.48148148e-04 1.58399471e-02 3.76863757e-01 7.05192791e-01
 1.70417328e-01]
- 25% = [0.         0.01245453 0.3449547  0.68622685 0.14060433]
- Min = [0.         0.00805556 0.3353254  0.60978439 0.1263836 ]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 75.875 | 4.125 |
| Actual Positive | 5.125 | 14.875 |

### robot-5
#### accuracy
- Mean = 0.8987499999999999
- Standard deviation = 0.02204399011068549
- Max = 0.94
- 75% = 0.91
- Median = 0.9
- 25% = 0.8875
- Min = 0.86

#### f1
- Mean = 0.6537342839933955
- Standard deviation = 0.10014337174151702
- Max = 0.8235294117647058
- 75% = 0.7096774193548387
- Median = 0.6666666666666666
- 25% = 0.6083743842364533
- Min = 0.4615384615384615

#### precision
- Mean = 1.0
- Standard deviation = 0.0
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 1.0
- Min = 1.0

#### recall
- Mean = 0.49375
- Standard deviation = 0.11021995055342748
- Max = 0.7
- 75% = 0.55
- Median = 0.5
- 25% = 0.4375
- Min = 0.3

#### facing_probas
- Mean = [0.         0.00074306 0.00878629 0.40139492 0.56759805]
- Standard deviation = [0.         0.00129961 0.00417557 0.0722128  0.03685707]
- Max = [0.         0.004      0.01445767 0.55755754 0.63849802]
- 75% = [0.         0.00090278 0.01270188 0.43709458 0.58969709]
- Median = [0.         0.         0.00873016 0.37238757 0.55785351]
- 25% = [0.         0.         0.004375   0.34990278 0.53525926]
- Min = [0.         0.         0.00375    0.32519974 0.53074206]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 80.0 | 0.0 |
| Actual Positive | 10.125 | 9.875 |

### robot-6
#### accuracy
- Mean = 0.7037499999999999
- Standard deviation = 0.05383713866839508
- Max = 0.75
- 75% = 0.74
- Median = 0.715
- 25% = 0.705
- Min = 0.57

#### f1
- Mean = 0.8248753744031116
- Standard deviation = 0.03936713499791851
- Max = 0.8571428571428571
- 75% = 0.8505747126436781
- Median = 0.8338093295253637
- 25% = 0.8269490293781792
- Min = 0.7261146496815287

#### precision
- Mean = 1.0
- Standard deviation = 0.0
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 1.0
- Min = 1.0

#### recall
- Mean = 0.7037499999999999
- Standard deviation = 0.05383713866839508
- Max = 0.75
- 75% = 0.74
- Median = 0.715
- 25% = 0.705
- Min = 0.57

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
| Actual Positive | 29.625 | 70.375 |

