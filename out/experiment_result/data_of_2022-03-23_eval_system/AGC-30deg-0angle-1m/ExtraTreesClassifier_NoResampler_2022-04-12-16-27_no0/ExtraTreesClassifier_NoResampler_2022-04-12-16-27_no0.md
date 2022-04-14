# ExtraTreesClassifier_NoResampler_2022-04-12-16-27_no0
## Constants
- CSV_PATH = ../out/csv/experiment
- OUTPUT_PATH = ../out/experiment_result/data_of_2022-03-23_eval_system/AGC-30deg-0angle-1m
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
- AGC_STATUS = ['AGC-30deg']
- ANGLES = [30, 60, 90, 120, 150]

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
	- n_estimators = 130
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
- gp_auc_min = 0.1332975594859735
- gp_max_val_min = 0.11971305740225571
- gp_max_val_mean = 0.11227959493107399
- gp_auc_mean = 0.10360529030907638
- gp_max_val_max = 0.05638408971160834
- gp_auc_max = 0.049840709518322646
- ratio_max_to_9th_ave_peaks = 0.03351087866197308
- gp_max_ix_std = 0.031659881883109156
- tdoa_std = 0.03136032297138445
- gp_max_ix_mean = 0.02264456853607673
- coe1[1] = 0.021548621264778967
- gp_auc_std = 0.021321116126287586
- gp_max_val_range = 0.020130336499518887
- diff_std = 0.01900472047935999
- tdoa_mean = 0.01867874975423643
- high_power = 0.017094306834482292
- diff_auc = 0.016074561442760493
- gp_max_ix_max = 0.014445423304768312
- coe1[0] = 0.014393028634787407
- gp_max_ix_min = 0.01390542155576255
- low_power = 0.013839639490366196
- tdoa_max = 0.013806312746682266
- tdoa_min = 0.012356736001398996
- gp_max_ix_range = 0.0116122720867587
- gp_max_val_std = 0.010619612086977797
- tdoa_range = 0.009528956864123904
- ac_std = 0.008725657317447524
- coe3[3] = 0.008507510266091863
- hlbr = 0.008494671118461632
- ac_auc = 0.008023872002857547
- srmr = 0.00728171592255296
- ratio_max_to_10ms_ave_peaks = 0.005759129441007056
- gp_auc_range = 0.005355963592826461
- coe3[2] = 0.005195711754850138
- coe3[0] = 0.0
- coe3[1] = 0.0

## Evaluation
cv = 8
### robot-1
#### accuracy
- Mean = 0.93875
- Standard deviation = 0.031399641717701154
- Max = 0.98
- 75% = 0.9724999999999999
- Median = 0.93
- 25% = 0.915
- Min = 0.9

#### f1
- Mean = 0.8090933337643864
- Standard deviation = 0.10912407255875192
- Max = 0.9473684210526316
- 75% = 0.926031294452347
- Median = 0.787878787878788
- 25% = 0.7291666666666665
- Min = 0.6666666666666666

#### precision
- Mean = 1.0
- Standard deviation = 0.0
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 1.0
- Min = 1.0

#### recall
- Mean = 0.69375
- Standard deviation = 0.15699820858850588
- Max = 0.9
- 75% = 0.8625
- Median = 0.65
- 25% = 0.575
- Min = 0.5

#### facing_probas
- Mean = [0.59424897 0.04943466 0.02255784 0.02071085 0.05014431]
- Standard deviation = [0.06468171 0.03229842 0.01786817 0.01248564 0.02487238]
- Max = [0.72139652 0.12459966 0.06700687 0.04516468 0.09904106]
- 75% = [0.62220807 0.05760012 0.02447123 0.02541243 0.06062676]
- Median = [0.58214072 0.03693544 0.01600649 0.01732265 0.045712  ]
- 25% = [0.56592987 0.02867808 0.0125918  0.01388389 0.03493838]
- Min = [0.48474222 0.0169736  0.0067964  0.0041888  0.01360043]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 80.0 | 0.0 |
| Actual Positive | 6.125 | 13.875 |

### robot-2
#### accuracy
- Mean = 0.8825000000000001
- Standard deviation = 0.07917543811056556
- Max = 0.97
- 75% = 0.94
- Median = 0.93
- 25% = 0.805
- Min = 0.75

#### f1
- Mean = 0.6103254025667819
- Standard deviation = 0.2977099791703965
- Max = 0.9230769230769231
- 75% = 0.8333333333333334
- Median = 0.793939393939394
- 25% = 0.31417624521072796
- Min = 0.13793103448275865

#### precision
- Mean = 0.7452563700918964
- Standard deviation = 0.2794799276701839
- Max = 1.0
- 75% = 0.9399671052631579
- Median = 0.9354166666666667
- 25% = 0.5238095238095238
- Min = 0.2222222222222222

#### recall
- Mean = 0.53125
- Standard deviation = 0.2925507434617113
- Max = 0.9
- 75% = 0.75
- Median = 0.675
- 25% = 0.225
- Min = 0.1

#### facing_probas
- Mean = [0.10361063 0.54925931 0.35492022 0.04987351 0.00406641]
- Standard deviation = [0.03867639 0.10283652 0.13065194 0.02017267 0.00223517]
- Max = [0.15486767 0.66801129 0.66721306 0.07933547 0.0076018 ]
- 75% = [0.13286241 0.64140915 0.3938911  0.0734773  0.00481509]
- Median = [0.10236989 0.58634791 0.31327244 0.03880449 0.00398993]
- 25% = [0.0815132  0.44620494 0.26225256 0.03363557 0.00300137]
- Min = [4.66576618e-02 3.98851801e-01 2.39164377e-01 2.84471917e-02
 1.19658120e-04]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 77.625 | 2.375 |
| Actual Positive | 9.375 | 10.625 |

### robot-3
#### accuracy
- Mean = 0.7825
- Standard deviation = 0.05717298313014635
- Max = 0.83
- 75% = 0.8125
- Median = 0.8
- 25% = 0.79
- Min = 0.64

#### f1
- Mean = 0.11976449476449474
- Standard deviation = 0.11132377860407608
- Max = 0.37037037037037035
- 75% = 0.15259740259740256
- Median = 0.09307359307359307
- 25% = 0.05769230769230768
- Min = 0.0

#### precision
- Mean = 0.43966450216450215
- Standard deviation = 0.3968844140653971
- Max = 1.0
- 75% = 0.7857142857142857
- Median = 0.3333333333333333
- 25% = 0.10227272727272727
- Min = 0.0

#### recall
- Mean = 0.08125
- Standard deviation = 0.07880950133074058
- Max = 0.25
- 75% = 0.1125
- Median = 0.05
- 25% = 0.037500000000000006
- Min = 0.0

#### facing_probas
- Mean = [0.02279497 0.34165989 0.30996421 0.15668775 0.08324813]
- Standard deviation = [0.01774825 0.06485363 0.05096396 0.03937434 0.03199255]
- Max = [0.05830815 0.46856716 0.41818223 0.22644002 0.16015919]
- 75% = [0.0325137  0.36788069 0.32245433 0.1850303  0.09188618]
- Median = [0.01701656 0.32779388 0.31293643 0.15179678 0.07158112]
- 25% = [0.00765068 0.29629945 0.28616129 0.13118098 0.05950996]
- Min = [0.00529411 0.25576725 0.23650412 0.10171581 0.05794383]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 76.625 | 3.375 |
| Actual Positive | 18.375 | 1.625 |

### robot-4
#### accuracy
- Mean = 0.8175
- Standard deviation = 0.06814506585219506
- Max = 0.93
- 75% = 0.8674999999999999
- Median = 0.78
- 25% = 0.7675000000000001
- Min = 0.75

#### f1
- Mean = 0.5225298747357571
- Standard deviation = 0.16895672857631683
- Max = 0.8
- 75% = 0.6197478991596639
- Median = 0.4880952380952381
- 25% = 0.39102564102564097
- Min = 0.3243243243243243

#### precision
- Mean = 0.573805503062469
- Standard deviation = 0.224426273544602
- Max = 0.9333333333333333
- 75% = 0.7321428571428571
- Median = 0.4564393939393939
- 25% = 0.4095394736842105
- Min = 0.35294117647058826

#### recall
- Mean = 0.4875
- Standard deviation = 0.1386317063301177
- Max = 0.7
- 75% = 0.5750000000000001
- Median = 0.5
- 25% = 0.375
- Min = 0.3

#### facing_probas
- Mean = [0.00925759 0.16463246 0.13629472 0.53281326 0.42956513]
- Standard deviation = [0.00738711 0.04613057 0.03716607 0.07915348 0.03036366]
- Max = [0.02552701 0.23081456 0.21323123 0.66298016 0.47563111]
- 75% = [0.01163816 0.20379945 0.15501431 0.58599527 0.45378175]
- Median = [0.00626893 0.15907631 0.1333679  0.5237384  0.42534158]
- 25% = [0.00378354 0.1302226  0.10756178 0.46718899 0.40900591]
- Min = [0.00258257 0.09655342 0.08506227 0.4366369  0.38908242]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 72.0 | 8.0 |
| Actual Positive | 10.25 | 9.75 |

### robot-5
#### accuracy
- Mean = 0.8425
- Standard deviation = 0.05471517157059822
- Max = 0.93
- 75% = 0.87
- Median = 0.825
- 25% = 0.8
- Min = 0.78

#### f1
- Mean = 0.4023214285714286
- Standard deviation = 0.27899426862115884
- Max = 0.8
- 75% = 0.6060606060606062
- Median = 0.38095238095238093
- 25% = 0.20083333333333334
- Min = 0.0

#### precision
- Mean = 0.5907051282051282
- Standard deviation = 0.3150279082948084
- Max = 1.0
- 75% = 0.7958333333333334
- Median = 0.6461538461538461
- 25% = 0.4375
- Min = 0.0

#### recall
- Mean = 0.31875
- Standard deviation = 0.24486922530199665
- Max = 0.7
- 75% = 0.5
- Median = 0.275
- 25% = 0.125
- Min = 0.0

#### facing_probas
- Mean = [0.00568506 0.05010993 0.0109259  0.46815095 0.52483122]
- Standard deviation = [0.007556   0.03287682 0.00693106 0.1351797  0.04183599]
- Max = [0.02515079 0.09880327 0.02813446 0.60769505 0.56942308]
- 75% = [0.00512511 0.0801105  0.01062221 0.55577442 0.55636145]
- Median = [0.00241026 0.04262111 0.00973504 0.52784928 0.54930495]
- 25% = [0.00199065 0.02463439 0.00781487 0.41405613 0.48507425]
- Min = [0.00093162 0.00786783 0.00312546 0.2387323  0.45994872]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 77.875 | 2.125 |
| Actual Positive | 13.625 | 6.375 |

### robot-6
#### accuracy
- Mean = 0.42250000000000004
- Standard deviation = 0.05952940449895331
- Max = 0.55
- 75% = 0.445
- Median = 0.415
- 25% = 0.3825
- Min = 0.35

#### f1
- Mean = 0.5916395573238753
- Standard deviation = 0.057057276063219316
- Max = 0.7096774193548387
- 75% = 0.6158675799086759
- Median = 0.5865547897312955
- 25% = 0.5532162505289886
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
- Mean = 0.42250000000000004
- Standard deviation = 0.05952940449895331
- Max = 0.55
- 75% = 0.445
- Median = 0.415
- 25% = 0.3825
- Min = 0.35

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
| Actual Positive | 57.75 | 42.25 |

