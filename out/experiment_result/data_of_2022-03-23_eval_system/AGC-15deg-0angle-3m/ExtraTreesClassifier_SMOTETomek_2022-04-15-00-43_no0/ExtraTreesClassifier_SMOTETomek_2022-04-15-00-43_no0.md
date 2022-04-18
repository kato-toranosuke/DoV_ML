# ExtraTreesClassifier_SMOTETomek_2022-04-15-00-43_no0
## Constants
- CSV_PATH = ../out/csv/experiment
- OUTPUT_PATH = ../out/experiment_result/data_of_2022-03-23_eval_system/AGC-15deg-0angle-3m
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
- AGC_STATUS = ['AGC-15deg']
- ANGLES = [60, 75, 90, 105, 120]

## Loaded CSV
- 2022-03-23_raspi_48000Hz_w1_N2^12_overlap80_all.csv

## Estimator
### Type
- resampler = SMOTETomek
- estimator = ExtraTreesClassifier

### Arguments for hyperparameter search
- resampler = SMOTETomek
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
	- tomek = None
	- n_jobs = -1
	- n_features_in_ = 36
	- sampling_strategy_ = auto
	- smote_ = SMOTE(n_jobs=-1, random_state=42)
	- tomek_ = TomekLinks(n_jobs=-1, sampling_strategy='all')

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
	- max_samples = 0.09
	- criterion = gini
	- max_depth = None
	- min_samples_split = 5
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
	- oob_decision_function_ = [[0.36666667 0.63333333]
 [0.35833333 0.64166667]
 [0.41666667 0.58333333]
 [0.24074074 0.75925926]
 [0.57407407 0.42592593]
 [0.64583333 0.35416667]
 [0.63333333 0.36666667]
 [0.56666667 0.43333333]
 [0.54166667 0.45833333]
 [0.35185185 0.64814815]
 [0.46666667 0.53333333]
 [0.36111111 0.63888889]
 [0.41666667 0.58333333]
 [0.37037037 0.62962963]
 [0.36666667 0.63333333]
 [0.47222222 0.52777778]
 [0.48148148 0.51851852]
 [0.48148148 0.51851852]
 [0.62962963 0.37037037]
 [0.48148148 0.51851852]
 [0.65       0.35      ]
 [0.42592593 0.57407407]
 [0.40833333 0.59166667]
 [0.47222222 0.52777778]
 [0.38333333 0.61666667]
 [0.2962963  0.7037037 ]
 [0.45833333 0.54166667]
 [0.48333333 0.51666667]
 [0.43333333 0.56666667]
 [0.53703704 0.46296296]
 [0.53333333 0.46666667]
 [0.57407407 0.42592593]
 [0.45833333 0.54166667]
 [0.36666667 0.63333333]
 [0.41666667 0.58333333]
 [0.64583333 0.35416667]
 [0.43333333 0.56666667]
 [0.43333333 0.56666667]
 [0.60416667 0.39583333]
 [0.46296296 0.53703704]
 [0.45833333 0.54166667]
 [0.58333333 0.41666667]
 [0.66666667 0.33333333]
 [0.675      0.325     ]
 [0.63333333 0.36666667]
 [0.53703704 0.46296296]
 [0.54166667 0.45833333]
 [0.42592593 0.57407407]
 [0.42592593 0.57407407]
 [0.37037037 0.62962963]
 [0.33333333 0.66666667]
 [0.36666667 0.63333333]
 [0.41666667 0.58333333]
 [0.26666667 0.73333333]
 [0.39814815 0.60185185]
 [0.2962963  0.7037037 ]
 [0.27083333 0.72916667]
 [0.28333333 0.71666667]
 [0.43333333 0.56666667]
 [0.41666667 0.58333333]
 [0.5952381  0.4047619 ]
 [0.36666667 0.63333333]
 [0.38333333 0.61666667]
 [0.35185185 0.64814815]
 [0.33333333 0.66666667]
 [0.51851852 0.48148148]
 [0.42592593 0.57407407]
 [0.37037037 0.62962963]
 [0.48333333 0.51666667]
 [0.31481481 0.68518519]
 [0.48148148 0.51851852]
 [0.54761905 0.45238095]
 [0.38333333 0.61666667]
 [0.38333333 0.61666667]
 [0.45833333 0.54166667]
 [0.40833333 0.59166667]
 [0.39583333 0.60416667]
 [0.39583333 0.60416667]
 [0.36666667 0.63333333]
 [0.51851852 0.48148148]]
	- oob_score_ = 0.65

#### Importance of features
- gp_auc_mean = 0.20424242424242425
- high_power = 0.17529411764705885
- gp_max_ix_max = 0.13000000000000006
- coe1[0] = 0.1
- tdoa_mean = 0.07529411764705884
- low_power = 0.06999999999999997
- tdoa_std = 0.050909090909090904
- diff_auc = 0.04909090909090909
- coe3[2] = 0.04666666666666666
- gp_max_val_mean = 0.03636363636363636
- ac_std = 0.024705882352941164
- gp_auc_range = 0.024705882352941164
- tdoa_range = 0.012727272727272716
- hlbr = 0.0
- coe1[1] = 0.0
- coe3[0] = 0.0
- coe3[1] = 0.0
- coe3[3] = 0.0
- ratio_max_to_10ms_ave_peaks = 0.0
- ratio_max_to_9th_ave_peaks = 0.0
- ac_auc = 0.0
- diff_std = 0.0
- srmr = 0.0
- gp_max_val_std = 0.0
- gp_max_val_range = 0.0
- gp_max_val_min = 0.0
- gp_max_val_max = 0.0
- gp_max_ix_std = 0.0
- gp_max_ix_range = 0.0
- gp_max_ix_min = 0.0
- gp_max_ix_mean = 0.0
- gp_auc_std = 0.0
- gp_auc_min = 0.0
- gp_auc_max = 0.0
- tdoa_min = 0.0
- tdoa_max = 0.0

## Evaluation
cv = 8
### robot-1
#### accuracy
- Mean = 0.76125
- Standard deviation = 0.07338894671542846
- Max = 0.85
- 75% = 0.8125
- Median = 0.775
- 25% = 0.72
- Min = 0.64

#### f1
- Mean = 0.45925456279687643
- Standard deviation = 0.1716238650838694
- Max = 0.6938775510204082
- 75% = 0.6041666666666666
- Median = 0.44605475040257647
- 25% = 0.3340659340659341
- Min = 0.18749999999999997

#### precision
- Mean = 0.41773287564362616
- Standard deviation = 0.13330201808654593
- Max = 0.6
- 75% = 0.521551724137931
- Median = 0.4307692307692308
- 25% = 0.28308823529411764
- Min = 0.25

#### recall
- Mean = 0.53125
- Standard deviation = 0.2235194342780958
- Max = 0.85
- 75% = 0.7124999999999999
- Median = 0.55
- 25% = 0.375
- Min = 0.15

#### facing_probas
- Mean = [0.56477083 0.44186458 0.42147917 0.3303125  0.32422917]
- Standard deviation = [0.04947625 0.13295374 0.08439523 0.14260363 0.10752923]
- Max = [0.61966667 0.64991667 0.54541667 0.53875    0.4425    ]
- 75% = [0.605625   0.53208333 0.48733333 0.41875    0.411875  ]
- Median = [0.57570833 0.4575     0.44041667 0.36125    0.37004167]
- 25% = [0.5353125  0.358125   0.34239583 0.2359375  0.22197917]
- Min = [0.465      0.21583333 0.29833333 0.09083333 0.1675    ]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 65.5 | 14.5 |
| Actual Positive | 9.375 | 10.625 |

### robot-2
#### accuracy
- Mean = 0.70375
- Standard deviation = 0.037728470681966414
- Max = 0.76
- 75% = 0.72
- Median = 0.715
- 25% = 0.6975
- Min = 0.63

#### f1
- Mean = 0.22363228186841888
- Standard deviation = 0.11030896704903809
- Max = 0.36842105263157887
- 75% = 0.30047169811320756
- Median = 0.25863991081382387
- 25% = 0.16360294117647056
- Min = 0.0

#### precision
- Mean = 0.22577407972144814
- Standard deviation = 0.10512805357071307
- Max = 0.3888888888888889
- 75% = 0.2723684210526316
- Median = 0.2365967365967366
- 25% = 0.20238095238095238
- Min = 0.0

#### recall
- Mean = 0.23125
- Standard deviation = 0.12732217992164602
- Max = 0.4
- 75% = 0.3125
- Median = 0.275
- 25% = 0.1375
- Min = 0.0

#### facing_probas
- Mean = [0.58336458 0.5941875  0.55284375 0.46152083 0.41939583]
- Standard deviation = [0.063085   0.05229726 0.06764332 0.11009057 0.07744358]
- Max = [0.68266667 0.6925     0.66458333 0.66025    0.52375   ]
- 75% = [0.62635417 0.6159375  0.59072917 0.51758333 0.471875  ]
- Median = [0.59629167 0.5925     0.54283333 0.46479167 0.448125  ]
- 25% = [0.52114583 0.57179167 0.51364583 0.3909375  0.3515625 ]
- Min = [0.49833333 0.50541667 0.45416667 0.31208333 0.29708333]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 65.75 | 14.25 |
| Actual Positive | 15.375 | 4.625 |

### robot-3
#### accuracy
- Mean = 0.7150000000000001
- Standard deviation = 0.06670832032063169
- Max = 0.8
- 75% = 0.77
- Median = 0.71
- 25% = 0.6775
- Min = 0.59

#### f1
- Mean = 0.17823253360687719
- Standard deviation = 0.12899961358378745
- Max = 0.32786885245901637
- 75% = 0.29840425531914894
- Median = 0.22064777327935223
- 25% = 0.044117647058823525
- Min = 0.0

#### precision
- Mean = 0.19960156149180538
- Standard deviation = 0.15908419678729865
- Max = 0.5
- 75% = 0.26944444444444443
- Median = 0.23306233062330622
- 25% = 0.05357142857142857
- Min = 0.0

#### recall
- Mean = 0.19375
- Standard deviation = 0.16851835953390953
- Max = 0.5
- 75% = 0.3125
- Median = 0.175
- 25% = 0.037500000000000006
- Min = 0.0

#### facing_probas
- Mean = [0.57719792 0.59989583 0.58633333 0.53604167 0.54958333]
- Standard deviation = [0.06555697 0.0555093  0.07630955 0.11673639 0.04287223]
- Max = [0.681      0.70125    0.73166667 0.741      0.605     ]
- 75% = [0.62291667 0.62854167 0.61927083 0.5996875  0.58589583]
- Median = [0.57208333 0.598125   0.5875     0.54       0.55966667]
- 25% = [0.5249375  0.56822917 0.53529167 0.48133333 0.51197917]
- Min = [0.48833333 0.51041667 0.47208333 0.31708333 0.4775    ]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 67.625 | 12.375 |
| Actual Positive | 16.125 | 3.875 |

### robot-4
#### accuracy
- Mean = 0.7250000000000001
- Standard deviation = 0.08336666000266534
- Max = 0.81
- 75% = 0.785
- Median = 0.75
- 25% = 0.7025
- Min = 0.56

#### f1
- Mean = 0.22717755801507594
- Standard deviation = 0.16845562593315536
- Max = 0.5000000000000001
- 75% = 0.3443328550932568
- Median = 0.2638888888888889
- 25% = 0.07142857142857142
- Min = 0.0

#### precision
- Mean = 0.3210565476190476
- Standard deviation = 0.290016123256125
- Max = 1.0
- 75% = 0.33482142857142855
- Median = 0.32291666666666663
- 25% = 0.1875
- Min = 0.0

#### recall
- Mean = 0.3
- Standard deviation = 0.3102418411497714
- Max = 0.95
- 75% = 0.4125
- Median = 0.225
- 25% = 0.037500000000000006
- Min = 0.0

#### facing_probas
- Mean = [0.51986458 0.56146875 0.54872917 0.51344792 0.51623958]
- Standard deviation = [0.043654   0.0535152  0.06107408 0.12467404 0.04456835]
- Max = [0.6025     0.61916667 0.62833333 0.74508333 0.58875   ]
- 75% = [0.53902083 0.60552083 0.5860625  0.56145833 0.54327083]
- Median = [0.521875   0.58108333 0.56125    0.52333333 0.49833333]
- 25% = [0.49541667 0.51729167 0.50797917 0.44708333 0.4903125 ]
- Min = [0.44375    0.46916667 0.45416667 0.3        0.45333333]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 66.5 | 13.5 |
| Actual Positive | 14.0 | 6.0 |

### robot-5
#### accuracy
- Mean = 0.795
- Standard deviation = 0.021213203435596406
- Max = 0.83
- 75% = 0.805
- Median = 0.795
- 25% = 0.78
- Min = 0.76

#### f1
- Mean = 0.2768913378288379
- Standard deviation = 0.15867638213990354
- Max = 0.5142857142857143
- 75% = 0.4
- Median = 0.2895833333333333
- 25% = 0.19580419580419578
- Min = 0.0

#### precision
- Mean = 0.4354166666666667
- Standard deviation = 0.17842628029525245
- Max = 0.6
- 75% = 0.525
- Median = 0.48333333333333334
- 25% = 0.41250000000000003
- Min = 0.0

#### recall
- Mean = 0.21875
- Standard deviation = 0.14128318194321646
- Max = 0.45
- 75% = 0.3125
- Median = 0.225
- 25% = 0.125
- Min = 0.0

#### facing_probas
- Mean = [0.37854167 0.43842708 0.48271875 0.47004167 0.4988125 ]
- Standard deviation = [0.10454381 0.07558552 0.05848833 0.12895734 0.04569254]
- Max = [0.55708333 0.54041667 0.61916667 0.71866667 0.55958333]
- 75% = [0.42927083 0.47027083 0.49772917 0.5234375  0.53552083]
- Median = [0.42020833 0.45708333 0.46725    0.486875   0.50020833]
- 25% = [0.26989583 0.42895833 0.44135417 0.40177083 0.47177083]
- Min = [0.22916667 0.28208333 0.42458333 0.27958333 0.43      ]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 75.125 | 4.875 |
| Actual Positive | 15.625 | 4.375 |

### robot-6
#### accuracy
- Mean = 0.29500000000000004
- Standard deviation = 0.054083269131959835
- Max = 0.38
- 75% = 0.335
- Median = 0.29000000000000004
- 25% = 0.2675
- Min = 0.21

#### f1
- Mean = 0.4528891746369783
- Standard deviation = 0.06492557452387746
- Max = 0.5507246376811594
- 75% = 0.5018100807574492
- Median = 0.4495192307692308
- 25% = 0.42162093495934966
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
- Mean = 0.29500000000000004
- Standard deviation = 0.054083269131959835
- Max = 0.38
- 75% = 0.335
- Median = 0.29000000000000004
- 25% = 0.2675
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
| Actual Positive | 70.5 | 29.5 |

