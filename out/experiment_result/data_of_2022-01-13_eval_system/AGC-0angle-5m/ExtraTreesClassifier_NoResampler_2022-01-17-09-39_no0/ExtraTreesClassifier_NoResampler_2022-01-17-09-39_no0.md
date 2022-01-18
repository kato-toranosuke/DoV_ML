# ExtraTreesClassifier_NoResampler_2022-01-17-09-39_no0
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
	- min_samples_split = 2
	- min_samples_leaf = 10
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
- gp_auc_min = 0.1760075328488777
- gp_max_val_mean = 0.16685456831722192
- gp_auc_mean = 0.15275399871901507
- gp_max_val_max = 0.13550210531549836
- gp_max_val_min = 0.1275787857419223
- gp_auc_max = 0.11556854154308441
- high_power = 0.05999240813017268
- hlbr = 0.017893425348168488
- gp_max_ix_max = 0.010622517735049472
- tdoa_max = 0.009694045769849937
- gp_max_ix_range = 0.006229592370793689
- srmr = 0.005801007851869207
- diff_std = 0.0034846789074079692
- tdoa_range = 0.0034100153063359737
- ratio_max_to_9th_ave_peaks = 0.002283605461775609
- coe1[1] = 0.0017600878825119262
- gp_auc_range = 0.0015944589363045562
- ac_std = 0.0012822039855374765
- gp_max_ix_std = 0.0010348711538211164
- low_power = 0.00031227224613739274
- coe1[0] = 0.00021746026031697836
- ac_auc = 0.00012181616832779581
- coe3[0] = 0.0
- coe3[1] = 0.0
- coe3[2] = 0.0
- coe3[3] = 0.0
- ratio_max_to_10ms_ave_peaks = 0.0
- diff_auc = 0.0
- gp_max_val_std = 0.0
- gp_max_val_range = 0.0
- gp_max_ix_min = 0.0
- gp_max_ix_mean = 0.0
- gp_auc_std = 0.0
- tdoa_std = 0.0
- tdoa_min = 0.0
- tdoa_mean = 0.0

## Evaluation
cv = 8
### robot-1
#### accuracy
- Mean = 0.90625
- Standard deviation = 0.015761900266148127
- Max = 0.93
- 75% = 0.92
- Median = 0.905
- 25% = 0.8975
- Min = 0.88

#### f1
- Mean = 0.6922142061901108
- Standard deviation = 0.06987596296051758
- Max = 0.787878787878788
- 75% = 0.7536764705882353
- Median = 0.6881720430107527
- 25% = 0.6551724137931034
- Min = 0.5714285714285715

#### precision
- Mean = 0.9910714285714286
- Standard deviation = 0.02362277956307669
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 1.0
- Min = 0.9285714285714286

#### recall
- Mean = 0.5375
- Standard deviation = 0.08569568250501305
- Max = 0.65
- 75% = 0.6125
- Median = 0.525
- 25% = 0.4875
- Min = 0.4

#### facing_probas
- Mean = [5.25065695e-01 1.13436165e-01 6.65703114e-03 3.64081458e-03
 5.13110640e-04]
- Standard deviation = [0.03856214 0.02640777 0.00214446 0.00267028 0.00037736]
- Max = [0.57946071 0.15577968 0.01088491 0.00793496 0.00117234]
- 75% = [0.5557817  0.13216958 0.00804005 0.00551106 0.00072869]
- Median = [5.24359644e-01 1.13400619e-01 5.88965587e-03 2.72179338e-03
 4.78021978e-04]
- 25% = [4.93545853e-01 9.70449572e-02 5.27751007e-03 1.53169576e-03
 2.29031385e-04]
- Min = [4.64775385e-01 6.83869258e-02 3.72807496e-03 3.37662338e-04
 0.00000000e+00]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 79.875 | 0.125 |
| Actual Positive | 9.25 | 10.75 |

### robot-2
#### accuracy
- Mean = 0.925
- Standard deviation = 0.01224744871391585
- Max = 0.94
- 75% = 0.94
- Median = 0.92
- 25% = 0.9175
- Min = 0.91

#### f1
- Mean = 0.778597545413185
- Standard deviation = 0.047123859844472274
- Max = 0.8421052631578948
- 75% = 0.8235294117647058
- Median = 0.7777777777777777
- 25% = 0.7509487666034156
- Min = 0.7096774193548387

#### precision
- Mean = 0.9459325396825398
- Standard deviation = 0.05624877521692255
- Max = 1.0
- 75% = 1.0
- Median = 0.9642857142857143
- 25% = 0.8854166666666666
- Min = 0.875

#### recall
- Mean = 0.66875
- Standard deviation = 0.07880950133074056
- Max = 0.8
- 75% = 0.7
- Median = 0.7
- 25% = 0.625
- Min = 0.55

#### facing_probas
- Mean = [0.25411836 0.55374242 0.07707697 0.0188681  0.00075405]
- Standard deviation = [0.04585359 0.04421097 0.01996149 0.01792643 0.00061069]
- Max = [0.3377928  0.60929657 0.11008611 0.0500117  0.00180983]
- 75% = [0.26852083 0.60123731 0.08700723 0.03340946 0.00115385]
- Median = [0.24327598 0.54969634 0.07076909 0.01023177 0.00085714]
- 25% = [2.27123812e-01 5.19631822e-01 6.70034989e-02 4.00905590e-03
 1.33928571e-04]
- Min = [0.19638326 0.48610206 0.05027737 0.00177077 0.        ]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 79.125 | 0.875 |
| Actual Positive | 6.625 | 13.375 |

### robot-3
#### accuracy
- Mean = 0.97375
- Standard deviation = 0.01932453104217537
- Max = 1.0
- 75% = 0.9824999999999999
- Median = 0.975
- 25% = 0.97
- Min = 0.93

#### f1
- Mean = 0.9267164201374727
- Standard deviation = 0.05910964128293012
- Max = 1.0
- 75% = 0.9541160593792173
- Median = 0.9331436699857752
- 25% = 0.9189189189189189
- Min = 0.787878787878788

#### precision
- Mean = 1.0
- Standard deviation = 0.0
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 1.0
- Min = 1.0

#### recall
- Mean = 0.86875
- Standard deviation = 0.0966226552108769
- Max = 1.0
- 75% = 0.9125
- Median = 0.875
- 25% = 0.85
- Min = 0.65

#### facing_probas
- Mean = [0.01116049 0.50508738 0.64789753 0.14564189 0.00276657]
- Standard deviation = [0.00468504 0.04675427 0.04212763 0.04272861 0.00163024]
- Max = [0.02210196 0.57701416 0.70416603 0.22249651 0.00496101]
- 75% = [0.01141526 0.55283879 0.68122598 0.16186515 0.00442205]
- Median = [0.01042147 0.49117826 0.64917592 0.13675272 0.00267819]
- 25% = [0.0095936  0.47300001 0.6164049  0.1240636  0.00132789]
- Min = [4.22520337e-03 4.45019357e-01 5.80981578e-01 7.86252991e-02
 4.68966534e-04]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 80.0 | 0.0 |
| Actual Positive | 2.625 | 17.375 |

### robot-4
#### accuracy
- Mean = 0.92
- Standard deviation = 0.018708286933869694
- Max = 0.96
- 75% = 0.9225000000000001
- Median = 0.92
- 25% = 0.91
- Min = 0.89

#### f1
- Mean = 0.7785642681087444
- Standard deviation = 0.061835468448895245
- Max = 0.9
- 75% = 0.7842401500938085
- Median = 0.7669683257918551
- 25% = 0.7647058823529412
- Min = 0.6666666666666667

#### precision
- Mean = 0.8650424137266243
- Standard deviation = 0.05936139231273257
- Max = 0.9285714285714286
- 75% = 0.9285714285714286
- Median = 0.8730769230769231
- 25% = 0.8045112781954887
- Min = 0.7894736842105263

#### recall
- Mean = 0.71875
- Standard deviation = 0.10879309490955755
- Max = 0.9
- 75% = 0.775
- Median = 0.7
- 25% = 0.65
- Min = 0.55

#### facing_probas
- Mean = [0.0014353  0.00949954 0.30945828 0.58627574 0.12158335]
- Standard deviation = [0.00095741 0.00667584 0.04402433 0.04171221 0.05199496]
- Max = [0.00302426 0.02420885 0.3743303  0.6382565  0.21940003]
- 75% = [0.00180768 0.01138479 0.34814148 0.62673553 0.14618416]
- Median = [0.00135126 0.00746815 0.29625326 0.58590734 0.11766195]
- 25% = [0.00080425 0.00515053 0.28077736 0.56056713 0.08575788]
- Min = [0.         0.00184965 0.2529675  0.51601134 0.05469746]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 77.625 | 2.375 |
| Actual Positive | 5.625 | 14.375 |

### robot-5
#### accuracy
- Mean = 0.90625
- Standard deviation = 0.019324531042175377
- Max = 0.94
- 75% = 0.9125000000000001
- Median = 0.91
- 25% = 0.8975
- Min = 0.87

#### f1
- Mean = 0.6885545637733526
- Standard deviation = 0.08465315916446318
- Max = 0.8235294117647058
- 75% = 0.719758064516129
- Median = 0.7096774193548387
- 25% = 0.6551724137931034
- Min = 0.5185185185185185

#### precision
- Mean = 1.0
- Standard deviation = 0.0
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 1.0
- Min = 1.0

#### recall
- Mean = 0.53125
- Standard deviation = 0.09662265521087691
- Max = 0.7
- 75% = 0.5625
- Median = 0.55
- 25% = 0.4875
- Min = 0.35

#### facing_probas
- Mean = [5.01913265e-04 6.18435989e-04 5.49598898e-03 3.31120319e-01
 5.33002060e-01]
- Standard deviation = [0.00043542 0.00035707 0.00409551 0.05366725 0.03973315]
- Max = [0.00119231 0.00113725 0.01470342 0.41668962 0.59940406]
- 75% = [0.00084478 0.000879   0.0065277  0.37670047 0.56151866]
- Median = [4.42176871e-04 6.80663087e-04 4.28695342e-03 3.30283059e-01
 5.30935939e-01]
- 25% = [6.84523810e-05 3.66341991e-04 2.42866173e-03 2.82479274e-01
 5.06114223e-01]
- Min = [0.         0.         0.00154745 0.26245573 0.4684503 ]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 80.0 | 0.0 |
| Actual Positive | 9.375 | 10.625 |

### robot-6
#### accuracy
- Mean = 0.665
- Standard deviation = 0.06726812023536854
- Max = 0.75
- 75% = 0.7024999999999999
- Median = 0.69
- 25% = 0.64
- Min = 0.52

#### f1
- Mean = 0.7967485170338853
- Standard deviation = 0.050795466265362195
- Max = 0.8571428571428571
- 75% = 0.8252493980048159
- Median = 0.8165266106442577
- 25% = 0.7803500846979108
- Min = 0.6842105263157895

#### precision
- Mean = 1.0
- Standard deviation = 0.0
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 1.0
- Min = 1.0

#### recall
- Mean = 0.665
- Standard deviation = 0.06726812023536854
- Max = 0.75
- 75% = 0.7024999999999999
- Median = 0.69
- 25% = 0.64
- Min = 0.52

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
| Actual Positive | 33.5 | 66.5 |

