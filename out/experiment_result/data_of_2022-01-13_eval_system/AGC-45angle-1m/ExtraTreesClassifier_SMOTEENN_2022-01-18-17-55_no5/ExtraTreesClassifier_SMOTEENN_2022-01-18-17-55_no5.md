# ExtraTreesClassifier_SMOTEENN_2022-01-18-17-55_no5
## Constants
- CSV_PATH = ../out/csv/experiment
- OUTPUT_PATH = ../out/experiment_result/data_of_2022-01-13_eval_system/AGC-45angle-1m
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
- DISTANCE = [1]
- AGC_STATUS = ['AGC']

## Loaded CSV
- 2021-12-27_AGC.csv
- 2022-01-10_NoAGC.csv
- 2022-01-13_raspi_48000Hz_w1_N2^12_overlap80.csv

## Estimator
### Type
- resampler = SMOTEENN
- estimator = ExtraTreesClassifier

### Arguments for hyperparameter search
- resampler = SMOTEENN
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
	- enn = None
	- n_jobs = -1
	- n_features_in_ = 36
	- sampling_strategy_ = auto
	- smote_ = SMOTE(n_jobs=-1, random_state=42)
	- enn_ = EditedNearestNeighbours(n_jobs=-1, sampling_strategy='all')

- best_estimator
	- base_estimator = ExtraTreeClassifier()
	- n_estimators = 10
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
- gp_max_ix_std = 0.19999999999999996
- gp_max_val_max = 0.09999999999999998
- gp_max_val_mean = 0.09999999999999998
- gp_max_ix_range = 0.09999999999999998
- gp_max_ix_mean = 0.09999999999999998
- gp_auc_mean = 0.09999999999999998
- tdoa_range = 0.09999999999999998
- tdoa_min = 0.09999999999999998
- coe3[2] = 0.07407407407407406
- gp_max_val_std = 0.025925925925925918
- low_power = 0.0
- high_power = 0.0
- hlbr = 0.0
- coe1[0] = 0.0
- coe1[1] = 0.0
- coe3[0] = 0.0
- coe3[1] = 0.0
- coe3[3] = 0.0
- ratio_max_to_10ms_ave_peaks = 0.0
- ratio_max_to_9th_ave_peaks = 0.0
- ac_std = 0.0
- ac_auc = 0.0
- diff_std = 0.0
- diff_auc = 0.0
- srmr = 0.0
- gp_max_val_range = 0.0
- gp_max_val_min = 0.0
- gp_max_ix_min = 0.0
- gp_max_ix_max = 0.0
- gp_auc_std = 0.0
- gp_auc_range = 0.0
- gp_auc_min = 0.0
- gp_auc_max = 0.0
- tdoa_std = 0.0
- tdoa_max = 0.0
- tdoa_mean = 0.0

## Evaluation
cv = 8
### robot-1
#### accuracy
- Mean = 0.8977272727272727
- Standard deviation = 0.06914536146511649
- Max = 1.0
- 75% = 0.9419191919191919
- Median = 0.8939393939393939
- 25% = 0.8661616161616161
- Min = 0.797979797979798

#### f1
- Mean = 0.5925073780677229
- Standard deviation = 0.36357104469942964
- Max = 1.0
- 75% = 0.8375
- Median = 0.6846846846846847
- 25% = 0.4655172413793104
- Min = 0.0

#### precision
- Mean = 0.7060049019607844
- Standard deviation = 0.41395090664157386
- Max = 1.0
- 75% = 1.0
- Median = 0.9416666666666667
- 25% = 0.5735294117647058
- Min = 0.0

#### recall
- Mean = 0.53125
- Standard deviation = 0.3552617872780578
- Max = 1.0
- 75% = 0.7625
- Median = 0.575
- 25% = 0.3375
- Min = 0.0

#### facing_probas
- Mean = [0.824375 0.718125 0.34625  0.01875  0.050625]
- Standard deviation = [0.15148097 0.15960767 0.28674629 0.02986951 0.05162591]
- Max = [0.995 0.91  0.795 0.075 0.125]
- 75% = [0.98125 0.86    0.55875 0.02375 0.11   ]
- Median = [0.84   0.6925 0.2325 0.     0.03  ]
- 25% = [0.6725  0.65625 0.14125 0.      0.     ]
- Min = [0.635 0.395 0.    0.    0.   ]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 78.25 | 0.75 |
| Actual Positive | 9.375 | 10.625 |

### robot-2
#### accuracy
- Mean = 0.9053030303030303
- Standard deviation = 0.07247738706346549
- Max = 0.98989898989899
- 75% = 0.9595959595959596
- Median = 0.9292929292929293
- 25% = 0.8712121212121212
- Min = 0.7878787878787878

#### f1
- Mean = 0.7949340894228207
- Standard deviation = 0.1284922901238311
- Max = 0.975609756097561
- 75% = 0.8947368421052632
- Median = 0.8250000000000001
- 25% = 0.7035749751737834
- Min = 0.6037735849056605

#### precision
- Mean = 0.7798430735930735
- Standard deviation = 0.1814292969788595
- Max = 0.9523809523809523
- 75% = 0.9444444444444444
- Median = 0.825
- 25% = 0.7045454545454546
- Min = 0.48484848484848486

#### recall
- Mean = 0.83125
- Standard deviation = 0.07880950133074056
- Max = 1.0
- 75% = 0.85
- Median = 0.825
- 25% = 0.8
- Min = 0.7

#### facing_probas
- Mean = [0.895    0.90875  0.874375 0.106875 0.038125]
- Standard deviation = [0.07390873 0.06702378 0.08712195 0.11741852 0.0300975 ]
- Max = [1.    1.    1.    0.355 0.08 ]
- 75% = [0.94375 0.95875 0.93    0.12875 0.06375]
- Median = [0.8975 0.92   0.895  0.055  0.04  ]
- 25% = [0.8275 0.85   0.7825 0.03   0.005 ]
- Min = [0.8   0.815 0.755 0.005 0.   ]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 73.0 | 6.0 |
| Actual Positive | 3.375 | 16.625 |

### robot-3
#### accuracy
- Mean = 0.8535353535353536
- Standard deviation = 0.0505050505050505
- Max = 0.9292929292929293
- 75% = 0.8888888888888888
- Median = 0.8535353535353536
- 25% = 0.797979797979798
- Min = 0.797979797979798

#### f1
- Mean = 0.39097823472823473
- Standard deviation = 0.2946655093746385
- Max = 0.787878787878788
- 75% = 0.6160714285714286
- Median = 0.42592592592592593
- 25% = 0.125
- Min = 0.0

#### precision
- Mean = 0.6875
- Standard deviation = 0.42847841252506524
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 0.375
- Min = 0.0

#### recall
- Mean = 0.2875
- Standard deviation = 0.23815698604072064
- Max = 0.65
- 75% = 0.45
- Median = 0.275
- 25% = 0.07500000000000001
- Min = 0.0

#### facing_probas
- Mean = [0.636875 0.860625 0.93125  0.85875  0.413125]
- Standard deviation = [0.23048776 0.11745844 0.04567206 0.07257539 0.27223539]
- Max = [0.98  1.    0.995 0.96  0.8  ]
- 75% = [0.79125 0.93875 0.96375 0.90625 0.665  ]
- Median = [0.5875 0.8925 0.93   0.8575 0.33  ]
- 25% = [0.52125 0.77875 0.90375 0.815   0.205  ]
- Min = [0.27  0.63  0.855 0.73  0.085]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 78.75 | 0.25 |
| Actual Positive | 14.25 | 5.75 |

### robot-4
#### accuracy
- Mean = 0.9608585858585859
- Standard deviation = 0.025968388637882756
- Max = 0.98989898989899
- 75% = 0.98989898989899
- Median = 0.9595959595959596
- 25% = 0.9444444444444444
- Min = 0.9191919191919192

#### f1
- Mean = 0.8846931285261457
- Standard deviation = 0.08009463908964623
- Max = 0.972972972972973
- 75% = 0.972972972972973
- Median = 0.8856209150326797
- 25% = 0.8299120234604105
- Min = 0.7647058823529413

#### precision
- Mean = 0.9759803921568627
- Standard deviation = 0.04558296406379487
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 0.9852941176470589
- Min = 0.8666666666666667

#### recall
- Mean = 0.8157894736842104
- Standard deviation = 0.1176877882894626
- Max = 0.9473684210526315
- 75% = 0.9473684210526315
- Median = 0.8157894736842105
- 25% = 0.7236842105263157
- Min = 0.631578947368421

#### facing_probas
- Mean = [0.00723684 0.10855263 0.93486842 0.93157895 0.79342105]
- Standard deviation = [0.01017081 0.14144431 0.05977436 0.05913738 0.12052948]
- Max = [0.02631579 0.38947368 1.         0.99473684 0.96315789]
- 75% = [0.01315789 0.13552632 0.97236842 0.98421053 0.91052632]
- Median = [0.         0.03684211 0.94210526 0.94210526 0.76315789]
- 25% = [0.         0.01578947 0.92105263 0.90526316 0.68684211]
- Min = [0.         0.         0.8        0.80526316 0.64736842]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 79.625 | 0.375 |
| Actual Positive | 3.5 | 15.5 |

### robot-5
#### accuracy
- Mean = 0.9898989898989898
- Standard deviation = 0.0112932726136353
- Max = 1.0
- 75% = 1.0
- Median = 0.994949494949495
- 25% = 0.9797979797979798
- Min = 0.9696969696969697

#### f1
- Mean = 0.9741284083389345
- Standard deviation = 0.029399291367360237
- Max = 1.0
- 75% = 1.0
- Median = 0.9871794871794872
- 25% = 0.9511278195488722
- Min = 0.9189189189189189

#### precision
- Mean = 0.9886363636363636
- Standard deviation = 0.030065355807552176
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 1.0
- Min = 0.9090909090909091

#### recall
- Mean = 0.9625
- Standard deviation = 0.05448623679425842
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 0.9375
- Min = 0.85

#### facing_probas
- Mean = [0.045    0.00625  0.12     0.925    0.936875]
- Standard deviation = [0.03172144 0.01023169 0.13688499 0.05190135 0.05905175]
- Max = [0.09  0.03  0.395 0.995 1.   ]
- 75% = [0.075  0.0075 0.17   0.985  0.985 ]
- Median = [0.0325 0.     0.0575 0.9075 0.9625]
- 25% = [0.02375 0.      0.015   0.88125 0.87125]
- Min = [0.    0.    0.    0.865 0.855]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 78.75 | 0.25 |
| Actual Positive | 0.75 | 19.25 |

### robot-6
#### accuracy
- Mean = 0.6843434343434344
- Standard deviation = 0.10433297101067472
- Max = 0.8383838383838383
- 75% = 0.7348484848484849
- Median = 0.702020202020202
- 25% = 0.6414141414141414
- Min = 0.5151515151515151

#### f1
- Mean = 0.8078957796182649
- Standard deviation = 0.0759776218130886
- Max = 0.9120879120879121
- 75% = 0.8468095712861415
- Median = 0.8249154691462384
- 25% = 0.7797637920101458
- Min = 0.6799999999999999

#### precision
- Mean = 1.0
- Standard deviation = 0.0
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 1.0
- Min = 1.0

#### recall
- Mean = 0.6843434343434344
- Standard deviation = 0.10433297101067472
- Max = 0.8383838383838383
- 75% = 0.7348484848484849
- Median = 0.702020202020202
- 25% = 0.6414141414141414
- Min = 0.5151515151515151

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
| Actual Positive | 31.25 | 67.75 |

