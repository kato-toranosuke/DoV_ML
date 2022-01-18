# ExtraTreesClassifier_RandomOverSampler_2022-01-17-01-36_no2
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
	- min_samples_leaf = 5
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
- gp_max_val_mean = 0.1746001999252883
- gp_max_val_min = 0.17100382408655446
- gp_auc_min = 0.1225403416557827
- gp_max_val_max = 0.08035204031737173
- gp_auc_mean = 0.07022749975534054
- gp_auc_max = 0.06601828026857764
- hlbr = 0.0564349955434678
- gp_auc_range = 0.037603417729465564
- gp_max_val_range = 0.032855107233084165
- gp_auc_std = 0.017753452397290297
- gp_max_val_std = 0.017533427455493644
- tdoa_min = 0.015128500186828679
- srmr = 0.012564959677662921
- tdoa_range = 0.011814982753702545
- tdoa_mean = 0.011480642345831692
- gp_max_ix_std = 0.010297172514443106
- ratio_max_to_10ms_ave_peaks = 0.009703966712598648
- gp_max_ix_range = 0.009299659334048811
- gp_max_ix_mean = 0.008711819802378768
- gp_max_ix_min = 0.007658842837418917
- tdoa_std = 0.007088098309350438
- gp_max_ix_max = 0.006201885769069819
- ratio_max_to_9th_ave_peaks = 0.006166524595788102
- ac_auc = 0.00558214973615707
- high_power = 0.005244780326198407
- diff_std = 0.005101202753806078
- tdoa_max = 0.0046622838662820475
- ac_std = 0.003914060387491996
- coe3[3] = 0.003652670143596713
- diff_auc = 0.0033036063431317146
- coe1[1] = 0.0019140742595264784
- coe3[2] = 0.0015600801252626758
- low_power = 0.0011948860676544873
- coe1[0] = 0.0008305647840531567
- coe3[0] = 0.0
- coe3[1] = 0.0

## Evaluation
cv = 8
### robot-1
#### accuracy
- Mean = 0.955820707070707
- Standard deviation = 0.03232768819902591
- Max = 1.0
- 75% = 0.9823484848484848
- Median = 0.9545454545454546
- 25% = 0.9368686868686869
- Min = 0.898989898989899

#### f1
- Mean = 0.9002890472483753
- Standard deviation = 0.06837723582070326
- Max = 1.0
- 75% = 0.9564024390243903
- Median = 0.89198606271777
- 25% = 0.8507978723404255
- Min = 0.7916666666666667

#### precision
- Mean = 0.8618296055796055
- Standard deviation = 0.10440243448333004
- Max = 1.0
- 75% = 0.950595238095238
- Median = 0.8773809523809524
- 25% = 0.7988215488215489
- Min = 0.6785714285714286

#### recall
- Mean = 0.95
- Standard deviation = 0.05
- Max = 1.0
- 75% = 1.0
- Median = 0.95
- 25% = 0.9375
- Min = 0.85

#### facing_probas
- Mean = [8.74928675e-01 1.12442109e-01 9.27482864e-03 6.22916667e-04
 2.75208333e-03]
- Standard deviation = [0.03836891 0.02086539 0.0067255  0.00077857 0.00393375]
- Max = [0.93074683 0.1434246  0.02327143 0.0022     0.00975   ]
- 75% = [0.88866704 0.12766889 0.01268636 0.0012125  0.00421667]
- Median = [8.73121555e-01 1.14756205e-01 6.26785714e-03 1.66666667e-04
 3.00000000e-04]
- 25% = [0.87073214 0.09840057 0.00414405 0.         0.        ]
- Min = [0.78998135 0.08183294 0.00298413 0.         0.        ]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 75.875 | 3.375 |
| Actual Positive | 1.0 | 19.0 |

### robot-2
#### accuracy
- Mean = 0.9091792929292929
- Standard deviation = 0.04051158155047068
- Max = 0.98
- 75% = 0.9420454545454546
- Median = 0.898989898989899
- 25% = 0.8762626262626263
- Min = 0.8585858585858586

#### f1
- Mean = 0.7146398817548199
- Standard deviation = 0.14993102046030865
- Max = 0.9473684210526316
- 75% = 0.8319327731092436
- Median = 0.7227799227799228
- 25% = 0.5983796296296297
- Min = 0.4999999999999999

#### precision
- Mean = 0.9174632352941177
- Standard deviation = 0.08806626562562848
- Max = 1.0
- 75% = 1.0
- Median = 0.9375
- 25% = 0.8583333333333334
- Min = 0.7647058823529411

#### recall
- Mean = 0.60625
- Standard deviation = 0.181034354474503
- Max = 0.9
- 75% = 0.7124999999999999
- Median = 0.65
- 25% = 0.4625
- Min = 0.35

#### facing_probas
- Mean = [0.53411047 0.69946381 0.53271117 0.00230734 0.0017892 ]
- Standard deviation = [0.10616639 0.07395005 0.08566543 0.00216734 0.00154772]
- Max = [0.73397879 0.79163676 0.63228286 0.0065619  0.00524098]
- 75% = [0.58720458 0.75490741 0.58778852 0.00366905 0.00238929]
- Median = [0.53424821 0.70358047 0.56560152 0.00184603 0.0013625 ]
- 25% = [4.85502670e-01 6.68292343e-01 4.89857089e-01 3.75000000e-04
 7.21428571e-04]
- Min = [0.35955317 0.57606389 0.37867857 0.         0.        ]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 78.125 | 1.125 |
| Actual Positive | 7.875 | 12.125 |

### robot-3
#### accuracy
- Mean = 0.9407575757575757
- Standard deviation = 0.02792376696570402
- Max = 0.9797979797979798
- 75% = 0.955
- Median = 0.9494949494949495
- 25% = 0.9191919191919192
- Min = 0.8888888888888888

#### f1
- Mean = 0.8501839590272882
- Standard deviation = 0.06374473368756439
- Max = 0.9473684210526316
- 75% = 0.8835758835758836
- Median = 0.8648648648648648
- 25% = 0.7973684210526317
- Min = 0.7441860465116279

#### precision
- Mean = 0.8882594113160138
- Standard deviation = 0.09906970486794238
- Max = 1.0
- 75% = 0.9558823529411764
- Median = 0.9179566563467492
- 25% = 0.8250000000000001
- Min = 0.6956521739130435

#### recall
- Mean = 0.8187500000000001
- Standard deviation = 0.04284784125250652
- Max = 0.9
- 75% = 0.85
- Median = 0.8
- 25% = 0.8
- Min = 0.75

#### facing_probas
- Mean = [0.04950269 0.32941455 0.78225902 0.12474106 0.0049498 ]
- Standard deviation = [0.03026672 0.14460327 0.05657349 0.04427556 0.00258559]
- Max = [0.1032688  0.49983027 0.85874708 0.19215079 0.00974167]
- 75% = [0.0696847  0.43608552 0.82482194 0.15629246 0.00565   ]
- Median = [0.05325139 0.40972327 0.79110994 0.11120593 0.00480238]
- 25% = [0.02115307 0.17237727 0.75039732 0.09468819 0.00350714]
- Min = [0.0099996  0.11944921 0.69108373 0.0637996  0.00155357]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 77.0 | 2.25 |
| Actual Positive | 3.625 | 16.375 |

### robot-4
#### accuracy
- Mean = 0.9219191919191919
- Standard deviation = 0.018008999099518905
- Max = 0.9595959595959596
- 75% = 0.9248484848484849
- Median = 0.9195959595959596
- 25% = 0.9090909090909091
- Min = 0.898989898989899

#### f1
- Mean = 0.7938979199403339
- Standard deviation = 0.05139393405732739
- Max = 0.8823529411764706
- 75% = 0.8130252100840336
- Median = 0.7950058072009292
- 25% = 0.7798102981029811
- Min = 0.6875

#### precision
- Mean = 0.8253770739064856
- Standard deviation = 0.0917712762610129
- Max = 1.0
- 75% = 0.867948717948718
- Median = 0.7981283422459893
- 25% = 0.7613636363636364
- Min = 0.7272727272727273

#### recall
- Mean = 0.7782894736842105
- Standard deviation = 0.08784065070852734
- Max = 0.85
- 75% = 0.844078947368421
- Median = 0.8157894736842105
- 25% = 0.7368421052631579
- Min = 0.5789473684210527

#### facing_probas
- Mean = [6.25000000e-05 7.75924185e-04 9.48912350e-02 7.32274644e-01
 9.75340382e-02]
- Standard deviation = [0.00016536 0.00107587 0.0636462  0.05738755 0.08541359]
- Max = [5.00000000e-04 3.31328321e-03 1.92312302e-01 7.89594264e-01
 2.67158768e-01]
- 75% = [0.         0.00079057 0.13876443 0.7646632  0.13810343]
- Median = [0.00000000e+00 3.92230576e-04 1.07633555e-01 7.55565714e-01
 6.77503968e-02]
- 25% = [0.         0.         0.02496011 0.72734078 0.02629678]
- Min = [0.         0.         0.01760652 0.6152619  0.01158271]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 76.5 | 3.5 |
| Actual Positive | 4.25 | 15.0 |

### robot-5
#### accuracy
- Mean = 0.9458333333333333
- Standard deviation = 0.016733013794223966
- Max = 0.9797979797979798
- 75% = 0.95
- Median = 0.9494949494949495
- 25% = 0.9368686868686869
- Min = 0.9191919191919192

#### f1
- Mean = 0.8421685061584442
- Standard deviation = 0.05449056078985624
- Max = 0.9473684210526316
- 75% = 0.8571428571428571
- Median = 0.8571428571428571
- 25% = 0.8146167557932263
- Min = 0.7499999999999999

#### precision
- Mean = 1.0
- Standard deviation = 0.0
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 1.0
- Min = 1.0

#### recall
- Mean = 0.73125
- Standard deviation = 0.08267972847076846
- Max = 0.9
- 75% = 0.75
- Median = 0.75
- 25% = 0.6875
- Min = 0.6

#### facing_probas
- Mean = [2.76557089e-03 8.85416667e-05 2.33772998e-02 4.38468132e-01
 6.91241053e-01]
- Standard deviation = [0.00246441 0.00015371 0.01829628 0.09462041 0.06134422]
- Max = [7.86147186e-03 3.75000000e-04 5.11202381e-02 6.09179545e-01
 7.64196825e-01]
- 75% = [3.65684524e-03 8.33333333e-05 3.71306548e-02 4.89909334e-01
 7.40172881e-01]
- Median = [0.00319286 0.         0.01936714 0.44869024 0.71641688]
- 25% = [3.75000000e-04 0.00000000e+00 8.15505952e-03 3.87626659e-01
 6.34933920e-01]
- Min = [0.         0.         0.00130357 0.28389048 0.58644444]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 79.25 | 0.0 |
| Actual Positive | 5.375 | 14.625 |

### robot-6
#### accuracy
- Mean = 0.7768813131313131
- Standard deviation = 0.06157055435602138
- Max = 0.87
- 75% = 0.842121212121212
- Median = 0.7474747474747475
- 25% = 0.73989898989899
- Min = 0.696969696969697

#### f1
- Mean = 0.8730942782604391
- Standard deviation = 0.03862716874448695
- Max = 0.9304812834224598
- 75% = 0.9142908054169636
- Median = 0.8554913294797689
- 25% = 0.8504420265215914
- Min = 0.8214285714285715

#### precision
- Mean = 1.0
- Standard deviation = 0.0
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 1.0
- Min = 1.0

#### recall
- Mean = 0.7768813131313131
- Standard deviation = 0.06157055435602138
- Max = 0.87
- 75% = 0.842121212121212
- Median = 0.7474747474747475
- 25% = 0.73989898989899
- Min = 0.696969696969697

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
| Actual Positive | 22.125 | 77.125 |

