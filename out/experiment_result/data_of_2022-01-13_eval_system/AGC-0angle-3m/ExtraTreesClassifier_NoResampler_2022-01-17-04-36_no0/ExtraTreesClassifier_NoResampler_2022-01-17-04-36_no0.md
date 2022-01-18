# ExtraTreesClassifier_NoResampler_2022-01-17-04-36_no0
## Constants
- CSV_PATH = ../out/csv/experiment
- OUTPUT_PATH = ../out/experiment_result/data_of_2022-01-13_eval_system/AGC-0angle-3m
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
	- n_estimators = 250
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

#### Importance of features
- gp_auc_max = 0.10055738534587051
- gp_max_val_max = 0.09927367729400952
- gp_auc_mean = 0.08377751159688125
- high_power = 0.07364171826937006
- gp_auc_min = 0.06997783194431346
- gp_max_val_mean = 0.06818162201861082
- gp_max_val_min = 0.058377035692389515
- diff_auc = 0.04309414466133926
- diff_std = 0.04023768793114763
- hlbr = 0.02791967701262213
- gp_max_ix_mean = 0.024361781088231147
- coe1[1] = 0.023489514239266616
- coe1[0] = 0.02302312435988126
- gp_auc_std = 0.020191156594971598
- tdoa_mean = 0.020000941183537117
- srmr = 0.019441559482846357
- low_power = 0.01886350760700249
- tdoa_std = 0.01636981721211405
- gp_max_ix_std = 0.015215965238119801
- coe3[3] = 0.01389822644603542
- ac_std = 0.013769418762775192
- coe3[2] = 0.013307073441372953
- gp_max_val_range = 0.012533403674128028
- gp_max_val_std = 0.012470717060074032
- gp_auc_range = 0.01224905644652462
- gp_max_ix_range = 0.011229113714715104
- gp_max_ix_max = 0.011048386872567517
- tdoa_max = 0.009540855742196151
- ratio_max_to_9th_ave_peaks = 0.009482551224395824
- tdoa_range = 0.008047115082013593
- ratio_max_to_10ms_ave_peaks = 0.0078438835398132
- ac_auc = 0.00730401193916591
- gp_max_ix_min = 0.006000799125485139
- tdoa_min = 0.00527972815621284
- coe3[0] = 0.0
- coe3[1] = 0.0

## Evaluation
cv = 8
### robot-1
#### accuracy
- Mean = 0.95
- Standard deviation = 0.015811388300841864
- Max = 0.97
- 75% = 0.96
- Median = 0.955
- 25% = 0.945
- Min = 0.92

#### f1
- Mean = 0.8576959007880061
- Standard deviation = 0.05290694525755013
- Max = 0.9189189189189189
- 75% = 0.8947368421052632
- Median = 0.873015873015873
- 25% = 0.8428571428571429
- Min = 0.7499999999999999

#### precision
- Mean = 0.9777777777777779
- Standard deviation = 0.028867513459481294
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 0.9444444444444444
- Min = 0.9333333333333333

#### recall
- Mean = 0.76875
- Standard deviation = 0.08267972847076846
- Max = 0.85
- 75% = 0.85
- Median = 0.775
- 25% = 0.7375
- Min = 0.6

#### facing_probas
- Mean = [0.64729167 0.19231875 0.00901458 0.00323333 0.00354792]
- Standard deviation = [0.04233147 0.04117022 0.00094907 0.00193855 0.00265142]
- Max = [0.70678333 0.24561667 0.0101     0.0079     0.0102    ]
- 75% = [0.68515    0.2183625  0.00971667 0.00343333 0.00342917]
- Median = [0.64331667 0.201325   0.00945833 0.00279167 0.00309167]
- 25% = [0.61659167 0.17375833 0.00803333 0.0021625  0.0020875 ]
- Min = [0.58261667 0.1216     0.00753333 0.00106667 0.00086667]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 79.625 | 0.375 |
| Actual Positive | 4.625 | 15.375 |

### robot-2
#### accuracy
- Mean = 0.9175
- Standard deviation = 0.018540496217739132
- Max = 0.95
- 75% = 0.9325
- Median = 0.91
- 25% = 0.9
- Min = 0.9

#### f1
- Mean = 0.7359882369370034
- Standard deviation = 0.07144533497926979
- Max = 0.8571428571428571
- 75% = 0.7967914438502675
- Median = 0.7096774193548387
- 25% = 0.6666666666666666
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
- Mean = 0.5875
- Standard deviation = 0.09270248108869578
- Max = 0.75
- 75% = 0.6625
- Median = 0.55
- 25% = 0.5
- Min = 0.5

#### facing_probas
- Mean = [0.279275   0.55895208 0.06764167 0.00605    0.0025375 ]
- Standard deviation = [0.05442786 0.04155386 0.01803691 0.00280135 0.00117623]
- Max = [0.36578333 0.62461667 0.10466667 0.0103     0.0046    ]
- 75% = [0.3165375  0.58818333 0.076275   0.00902917 0.0034375 ]
- Median = [0.276725   0.543825   0.06411667 0.00500833 0.00203333]
- 25% = [0.25122083 0.530575   0.0586     0.00373333 0.00184583]
- Min = [0.1902     0.50271667 0.041      0.00256667 0.0009    ]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 80.0 | 0.0 |
| Actual Positive | 8.25 | 11.75 |

### robot-3
#### accuracy
- Mean = 0.9862500000000001
- Standard deviation = 0.013169567191065936
- Max = 1.0
- 75% = 0.9924999999999999
- Median = 0.99
- 25% = 0.985
- Min = 0.96

#### f1
- Mean = 0.9631554631554631
- Standard deviation = 0.03655391624540726
- Max = 1.0
- 75% = 0.9807692307692307
- Median = 0.9743589743589743
- 25% = 0.9604989604989604
- Min = 0.888888888888889

#### precision
- Mean = 1.0
- Standard deviation = 0.0
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 1.0
- Min = 1.0

#### recall
- Mean = 0.93125
- Standard deviation = 0.0658478359553296
- Max = 1.0
- 75% = 0.9624999999999999
- Median = 0.95
- 25% = 0.9249999999999999
- Min = 0.8

#### facing_probas
- Mean = [0.0189     0.311325   0.76925833 0.11251458 0.008875  ]
- Standard deviation = [0.00568248 0.04490894 0.06254126 0.02093338 0.00305157]
- Max = [0.0311     0.39871667 0.83115    0.13828333 0.01446667]
- 75% = [0.0210875  0.33580833 0.826925   0.13022917 0.01060417]
- Median = [0.01730833 0.31340833 0.78515833 0.11525833 0.00878333]
- 25% = [0.01495   0.2684375 0.7357375 0.1006625 0.0066875]
- Min = [0.01236667 0.25771667 0.64418333 0.06975    0.0042    ]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 80.0 | 0.0 |
| Actual Positive | 1.375 | 18.625 |

### robot-4
#### accuracy
- Mean = 0.95375
- Standard deviation = 0.01408678458698082
- Max = 0.98
- 75% = 0.9624999999999999
- Median = 0.95
- 25% = 0.94
- Min = 0.94

#### f1
- Mean = 0.8760964912280702
- Standard deviation = 0.04055456589173023
- Max = 0.9473684210526316
- 75% = 0.9018218623481782
- Median = 0.8717948717948718
- 25% = 0.8333333333333334
- Min = 0.8333333333333334

#### precision
- Mean = 0.9367233187134503
- Standard deviation = 0.03103306808552647
- Max = 1.0
- 75% = 0.9451754385964912
- Median = 0.9375
- 25% = 0.9268092105263158
- Min = 0.8947368421052632

#### recall
- Mean = 0.825
- Standard deviation = 0.06123724356957946
- Max = 0.9
- 75% = 0.8625
- Median = 0.85
- 25% = 0.75
- Min = 0.75

#### facing_probas
- Mean = [0.001725   0.01659583 0.21406875 0.67743333 0.10475625]
- Standard deviation = [0.00073697 0.00983127 0.03561297 0.06571372 0.05362874]
- Max = [0.00256667 0.03471667 0.2736     0.76841667 0.18628333]
- 75% = [0.00225417 0.02030833 0.23717917 0.72026667 0.154825  ]
- Median = [0.0019     0.0167     0.20889167 0.70715    0.08166667]
- 25% = [0.00129167 0.0091625  0.18874167 0.6120625  0.06937917]
- Min = [2.50000000e-04 2.70000000e-03 1.68116667e-01 5.71500000e-01
 3.14500000e-02]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 78.875 | 1.125 |
| Actual Positive | 3.5 | 16.5 |

### robot-5
#### accuracy
- Mean = 0.9175
- Standard deviation = 0.012990381056766568
- Max = 0.94
- 75% = 0.92
- Median = 0.92
- 25% = 0.9175
- Min = 0.89

#### f1
- Mean = 0.7379870607864947
- Standard deviation = 0.05314974660734454
- Max = 0.8235294117647058
- 75% = 0.7499999999999999
- Median = 0.7499999999999999
- 25% = 0.7399193548387096
- Min = 0.6206896551724138

#### precision
- Mean = 1.0
- Standard deviation = 0.0
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 1.0
- Min = 1.0

#### recall
- Mean = 0.5874999999999999
- Standard deviation = 0.06495190528383288
- Max = 0.7
- 75% = 0.6
- Median = 0.6
- 25% = 0.5875
- Min = 0.45

#### facing_probas
- Mean = [0.00062292 0.00184583 0.02237917 0.41944583 0.602625  ]
- Standard deviation = [0.00057463 0.00113922 0.00718529 0.0389691  0.04765851]
- Max = [0.00153333 0.0037     0.03633333 0.50643333 0.69128333]
- 75% = [0.0010375  0.00279167 0.0246375  0.42372917 0.61066667]
- Median = [4.00000000e-04 1.63333333e-03 2.25250000e-02 4.09583333e-01
 6.06691667e-01]
- 25% = [1.66666667e-04 9.50000000e-04 1.72208333e-02 4.02004167e-01
 5.94650000e-01]
- Min = [0.00000000e+00 2.00000000e-04 1.12833333e-02 3.71566667e-01
 5.04033333e-01]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 80.0 | 0.0 |
| Actual Positive | 8.25 | 11.75 |

### robot-6
#### accuracy
- Mean = 0.74
- Standard deviation = 0.047434164902525694
- Max = 0.81
- 75% = 0.7725
- Median = 0.73
- 25% = 0.71
- Min = 0.68

#### f1
- Mean = 0.8497262256630812
- Standard deviation = 0.03113327198634249
- Max = 0.8950276243093923
- 75% = 0.8714841788046208
- Median = 0.8439306358381503
- 25% = 0.8302879291251384
- Min = 0.8095238095238095

#### precision
- Mean = 1.0
- Standard deviation = 0.0
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 1.0
- Min = 1.0

#### recall
- Mean = 0.74
- Standard deviation = 0.047434164902525694
- Max = 0.81
- 75% = 0.7725
- Median = 0.73
- 25% = 0.71
- Min = 0.68

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
| Actual Positive | 26.0 | 74.0 |

