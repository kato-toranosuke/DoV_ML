# ExtraTreesClassifier_RandomUnderSampler_2022-04-12-22-52_no2
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
- resampler = RandomUnderSampler
- estimator = ExtraTreesClassifier

### Arguments for hyperparameter search
- resampler = RandomUnderSampler
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
	- replacement = False
	- n_features_in_ = 36
	- sampling_strategy_ = OrderedDict([(0, 15)])
	- sample_indices_ = [ 3  8 45 57 16 66 42 60 15 69 58 62 40  6 64  0  1  2 18 19 20 36 37 38
 54 55 56 72 73 74]

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
- gp_auc_max = 0.1256612878090123
- gp_max_val_min = 0.10004286872093601
- gp_max_val_mean = 0.09368037499622645
- gp_max_val_max = 0.09195717355420223
- gp_auc_mean = 0.053078409343789996
- gp_auc_min = 0.051596722267231894
- ratio_max_to_10ms_ave_peaks = 0.0411610747593424
- coe1[1] = 0.03559091264402567
- srmr = 0.03453483214998379
- ac_auc = 0.03150354878165192
- coe1[0] = 0.03129500129968047
- low_power = 0.03037438214618728
- diff_std = 0.028789997379215036
- diff_auc = 0.02282054160730631
- hlbr = 0.02277462828679348
- high_power = 0.022282389029223037
- gp_max_val_range = 0.01847834537909627
- gp_max_ix_mean = 0.01841925214702015
- coe3[3] = 0.018168678657243066
- tdoa_mean = 0.017487539108537627
- ratio_max_to_9th_ave_peaks = 0.0147661735898221
- gp_auc_std = 0.013631669449097517
- ac_std = 0.013486801113744123
- tdoa_range = 0.012254737904532709
- gp_max_val_std = 0.011211531022078008
- coe3[2] = 0.010837645789948287
- gp_max_ix_std = 0.007393159962465448
- gp_auc_range = 0.005990213730151811
- tdoa_max = 0.005898683174572982
- gp_max_ix_min = 0.0056029478104861535
- gp_max_ix_range = 0.005069849450698494
- gp_max_ix_max = 0.004158626935696996
- coe3[0] = 0.0
- coe3[1] = 0.0
- tdoa_std = 0.0
- tdoa_min = 0.0

## Evaluation
cv = 8
### robot-1
#### accuracy
- Mean = 0.87
- Standard deviation = 0.02872281323269017
- Max = 0.92
- 75% = 0.8825000000000001
- Median = 0.875
- 25% = 0.855
- Min = 0.82

#### f1
- Mean = 0.6546659466184968
- Standard deviation = 0.04616249396407457
- Max = 0.7647058823529412
- 75% = 0.656025824964132
- Median = 0.6407624633431086
- 25% = 0.6250000000000001
- Min = 0.6111111111111112

#### precision
- Mean = 0.7412405303030304
- Standard deviation = 0.13663392706431057
- Max = 0.9285714285714286
- 75% = 0.8522727272727273
- Median = 0.7366071428571428
- 25% = 0.6458333333333333
- Min = 0.5357142857142857

#### recall
- Mean = 0.6125
- Standard deviation = 0.09270248108869578
- Max = 0.75
- 75% = 0.7
- Median = 0.6000000000000001
- 25% = 0.5375000000000001
- Min = 0.5

#### facing_probas
- Mean = [0.60611219 0.37238492 0.17712186 0.07598661 0.05437641]
- Standard deviation = [0.07229941 0.08324201 0.05494528 0.05070348 0.02702839]
- Max = [0.73921296 0.52245767 0.28012434 0.18490873 0.09256151]
- 75% = [0.64959788 0.42160235 0.20305109 0.10080737 0.07710549]
- Median = [0.58826058 0.35365906 0.17485417 0.06144345 0.05622354]
- 25% = [0.56510351 0.30698859 0.15037715 0.03924934 0.02912004]
- Min = [0.5072004  0.27120569 0.10220172 0.02141534 0.01985185]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 74.75 | 5.25 |
| Actual Positive | 7.75 | 12.25 |

### robot-2
#### accuracy
- Mean = 0.78625
- Standard deviation = 0.08014635050955221
- Max = 0.88
- 75% = 0.855
- Median = 0.81
- 25% = 0.7124999999999999
- Min = 0.66

#### f1
- Mean = 0.4846206125758026
- Standard deviation = 0.16700726923992718
- Max = 0.7272727272727272
- 75% = 0.6056910569105691
- Median = 0.4780361757105943
- 25% = 0.40777777777777774
- Min = 0.1904761904761905

#### precision
- Mean = 0.5107742924504939
- Standard deviation = 0.2125222667677035
- Max = 0.8571428571428571
- 75% = 0.6710526315789473
- Median = 0.5248447204968945
- 25% = 0.345
- Min = 0.18181818181818182

#### recall
- Mean = 0.5
- Standard deviation = 0.18708286933869708
- Max = 0.8
- 75% = 0.6125
- Median = 0.55
- 25% = 0.33749999999999997
- Min = 0.2

#### facing_probas
- Mean = [0.55688525 0.61200967 0.50871172 0.2257567  0.09534912]
- Standard deviation = [0.06468508 0.04817518 0.05295485 0.07728629 0.05612382]
- Max = [0.64168254 0.66199272 0.62008333 0.3699623  0.21594775]
- 75% = [0.60904613 0.65008896 0.53609524 0.2662328  0.11712864]
- Median = [0.56451091 0.63499537 0.50134458 0.23233466 0.08176918]
- 25% = [0.52679563 0.57546528 0.46198876 0.15840592 0.04924008]
- Min = [0.43303968 0.52034524 0.45282341 0.11557209 0.04035053]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 68.625 | 11.375 |
| Actual Positive | 10.0 | 10.0 |

### robot-3
#### accuracy
- Mean = 0.79375
- Standard deviation = 0.039350190596742995
- Max = 0.87
- 75% = 0.81
- Median = 0.79
- 25% = 0.78
- Min = 0.72

#### f1
- Mean = 0.3547595774989392
- Standard deviation = 0.2301038863367667
- Max = 0.723404255319149
- 75% = 0.5032051282051282
- Median = 0.39814814814814814
- 25% = 0.1875
- Min = 0.0

#### precision
- Mean = 0.3982134154831523
- Standard deviation = 0.1988876703318147
- Max = 0.6296296296296297
- 75% = 0.537593984962406
- Median = 0.47916666666666663
- 25% = 0.25
- Min = 0.0

#### recall
- Mean = 0.35624999999999996
- Standard deviation = 0.27207248574598647
- Max = 0.85
- 75% = 0.5125
- Median = 0.35
- 25% = 0.1625
- Min = 0.0

#### facing_probas
- Mean = [0.45658507 0.66178175 0.63551968 0.5424504  0.20870337]
- Standard deviation = [0.09511849 0.03941136 0.04671389 0.05732423 0.06280119]
- Max = [0.60881481 0.71851786 0.72222487 0.63116601 0.32636111]
- 75% = [0.5018254  0.68441617 0.65923132 0.58321362 0.23961491]
- Median = [0.45680754 0.66697454 0.63337037 0.54506349 0.21816667]
- 25% = [0.40953009 0.63953935 0.60285301 0.50564881 0.16039269]
- Min = [0.29850595 0.602125   0.57269444 0.45958532 0.11826984]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 72.25 | 7.75 |
| Actual Positive | 12.875 | 7.125 |

### robot-4
#### accuracy
- Mean = 0.8187500000000001
- Standard deviation = 0.028034576865007235
- Max = 0.86
- 75% = 0.835
- Median = 0.8200000000000001
- 25% = 0.805
- Min = 0.77

#### f1
- Mean = 0.45479233410267894
- Standard deviation = 0.10141863743481203
- Max = 0.5714285714285715
- 75% = 0.541025641025641
- Median = 0.4692640692640693
- 25% = 0.3938992042440318
- Min = 0.2758620689655173

#### precision
- Mean = 0.5756410256410256
- Standard deviation = 0.11298382799420206
- Max = 0.8
- 75% = 0.6166666666666667
- Median = 0.5672514619883041
- 25% = 0.5149572649572649
- Min = 0.42105263157894735

#### recall
- Mean = 0.3875
- Standard deviation = 0.11110243021644486
- Max = 0.55
- 75% = 0.4625
- Median = 0.4
- 25% = 0.32499999999999996
- Min = 0.2

#### facing_probas
- Mean = [0.17504225 0.53685359 0.6081546  0.64444874 0.53898917]
- Standard deviation = [0.05461175 0.05474683 0.04981353 0.02768503 0.05278877]
- Max = [0.28015212 0.6175377  0.7048373  0.69013492 0.6137672 ]
- 75% = [0.21460913 0.58700513 0.62733714 0.66503191 0.57224421]
- Median = [0.15548512 0.52994015 0.60978472 0.64059656 0.53931845]
- 25% = [0.14164468 0.50503935 0.57557606 0.62280556 0.511813  ]
- Min = [0.1015086  0.45615079 0.54307937 0.60872024 0.4507209 ]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 74.125 | 5.875 |
| Actual Positive | 12.25 | 7.75 |

### robot-5
#### accuracy
- Mean = 0.9125000000000001
- Standard deviation = 0.030310889132455356
- Max = 0.96
- 75% = 0.93
- Median = 0.915
- 25% = 0.905
- Min = 0.85

#### f1
- Mean = 0.756938825330771
- Standard deviation = 0.09933859655791151
- Max = 0.888888888888889
- 75% = 0.8073170731707318
- Median = 0.7842377260981912
- 25% = 0.7342342342342342
- Min = 0.5454545454545455

#### precision
- Mean = 0.8398723159832495
- Standard deviation = 0.09271031220238782
- Max = 1.0
- 75% = 0.8895833333333334
- Median = 0.8348416289592759
- 25% = 0.7919254658385093
- Min = 0.6923076923076923

#### recall
- Mean = 0.7
- Standard deviation = 0.1322875655532295
- Max = 0.85
- 75% = 0.8125
- Median = 0.7
- 25% = 0.6625
- Min = 0.45

#### facing_probas
- Mean = [0.08603224 0.10784086 0.42360061 0.55106696 0.65562351]
- Standard deviation = [0.04236566 0.0457199  0.0626022  0.0485735  0.04296601]
- Max = [0.14650595 0.1969914  0.52634854 0.61840476 0.71455754]
- 75% = [0.12536045 0.13096825 0.45992642 0.58197685 0.69639881]
- Median = [0.08134755 0.09796329 0.43456713 0.56787765 0.64954993]
- 25% = [0.04714451 0.0725167  0.39180721 0.49712831 0.62123892]
- Min = [0.03269048 0.05774339 0.32086905 0.48426984 0.59905622]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 77.25 | 2.75 |
| Actual Positive | 6.0 | 14.0 |

### robot-6
#### accuracy
- Mean = 0.51125
- Standard deviation = 0.055551215108222446
- Max = 0.59
- 75% = 0.5525
- Median = 0.515
- 25% = 0.4825
- Min = 0.41

#### f1
- Mean = 0.6747745893727729
- Standard deviation = 0.049480915894228185
- Max = 0.7421383647798743
- 75% = 0.7117452440033085
- Median = 0.6795084110520352
- 25% = 0.6508228371793693
- Min = 0.5815602836879432

#### precision
- Mean = 1.0
- Standard deviation = 0.0
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 1.0
- Min = 1.0

#### recall
- Mean = 0.51125
- Standard deviation = 0.055551215108222446
- Max = 0.59
- 75% = 0.5525
- Median = 0.515
- 25% = 0.4825
- Min = 0.41

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
| Actual Positive | 48.875 | 51.125 |

