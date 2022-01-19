# ExtraTreesClassifier_SMOTETomek_2022-01-18-18-40_no6
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
	- min_samples_split = 2
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
- gp_max_val_mean = 0.23120913037579707
- gp_max_val_max = 0.20479336902413825
- gp_auc_max = 0.09607059607059609
- srmr = 0.08833313507313048
- gp_auc_mean = 0.07026049939843045
- hlbr = 0.06913086913086915
- diff_auc = 0.050178266178266186
- diff_std = 0.039587572920906255
- high_power = 0.037025474525474535
- gp_max_val_min = 0.03065015070812173
- ac_std = 0.020565652296421533
- ac_auc = 0.017790986790986795
- gp_max_val_std = 0.011478507247738017
- gp_auc_min = 0.0064713064713064735
- gp_auc_std = 0.006419753086419757
- ratio_max_to_9th_ave_peaks = 0.006043956043956046
- gp_max_val_range = 0.004195631528964862
- coe3[2] = 0.0038217338217338232
- ratio_max_to_10ms_ave_peaks = 0.0034093067426400757
- gp_max_ix_range = 0.0012820512820512823
- tdoa_min = 0.0012820512820512823
- low_power = 0.0
- coe1[0] = 0.0
- coe1[1] = 0.0
- coe3[0] = 0.0
- coe3[1] = 0.0
- coe3[3] = 0.0
- gp_max_ix_std = 0.0
- gp_max_ix_min = 0.0
- gp_max_ix_max = 0.0
- gp_max_ix_mean = 0.0
- gp_auc_range = 0.0
- tdoa_std = 0.0
- tdoa_range = 0.0
- tdoa_max = 0.0
- tdoa_mean = 0.0

## Evaluation
cv = 8
### robot-1
#### accuracy
- Mean = 0.9873737373737373
- Standard deviation = 0.01655918819268182
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 0.9696969696969697
- Min = 0.9595959595959596

#### f1
- Mean = 0.9711945031712473
- Standard deviation = 0.037685211816132026
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 0.9302325581395349
- Min = 0.9090909090909091

#### precision
- Mean = 0.9465579710144927
- Standard deviation = 0.06978165868391814
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 0.8695652173913043
- Min = 0.8333333333333334

#### recall
- Mean = 1.0
- Standard deviation = 0.0
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 1.0
- Min = 1.0

#### facing_probas
- Mean = [0.93625    0.80458333 0.02041667 0.         0.        ]
- Standard deviation = [0.06184518 0.09133177 0.01934249 0.         0.        ]
- Max = [0.99666667 0.91       0.05166667 0.         0.        ]
- 75% = [0.98666667 0.86416667 0.03625    0.         0.        ]
- Median = [0.9575     0.825      0.01666667 0.         0.        ]
- 25% = [0.90833333 0.76916667 0.00166667 0.         0.        ]
- Min = [0.82166667 0.6        0.         0.         0.        ]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 78.0 | 1.25 |
| Actual Positive | 0.0 | 20.0 |

### robot-2
#### accuracy
- Mean = 0.9835984848484849
- Standard deviation = 0.018170446605234848
- Max = 1.0
- 75% = 1.0
- Median = 0.9899494949494949
- 25% = 0.9747474747474747
- Min = 0.9494949494949495

#### f1
- Mean = 0.9572737050272352
- Standard deviation = 0.048344335240672054
- Max = 1.0
- 75% = 1.0
- Median = 0.975609756097561
- 25% = 0.9342105263157895
- Min = 0.8648648648648648

#### precision
- Mean = 0.973797852474323
- Standard deviation = 0.026432353466383576
- Max = 1.0
- 75% = 1.0
- Median = 0.9761904761904762
- 25% = 0.9503968253968254
- Min = 0.9411764705882353

#### recall
- Mean = 0.94375
- Standard deviation = 0.07680128579652816
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 0.8875
- Min = 0.8

#### facing_probas
- Mean = [9.66875000e-01 9.72291667e-01 9.18333333e-01 2.00000000e-02
 2.08333333e-04]
- Standard deviation = [0.01579903 0.02066494 0.05650713 0.01416667 0.0005512 ]
- Max = [0.98333333 0.99666667 0.98333333 0.04333333 0.00166667]
- 75% = [0.98208333 0.98333333 0.97333333 0.02708333 0.        ]
- Median = [0.96833333 0.97916667 0.925      0.01333333 0.        ]
- 25% = [0.95791667 0.96833333 0.875      0.01       0.        ]
- Min = [0.93833333 0.93       0.81333333 0.005      0.        ]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 78.75 | 0.5 |
| Actual Positive | 1.125 | 18.875 |

### robot-3
#### accuracy
- Mean = 0.8841035353535354
- Standard deviation = 0.029089108806352976
- Max = 0.9191919191919192
- 75% = 0.9017424242424242
- Median = 0.8939393939393939
- 25% = 0.8721212121212121
- Min = 0.8282828282828283

#### f1
- Mean = 0.5807498180633185
- Standard deviation = 0.1568069311789462
- Max = 0.7499999999999999
- 75% = 0.6774193548387096
- Median = 0.6436781609195402
- 25% = 0.5285714285714287
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
- Mean = 0.42499999999999993
- Standard deviation = 0.1436140661634507
- Max = 0.6
- 75% = 0.5125
- Median = 0.475
- 25% = 0.36250000000000004
- Min = 0.15

#### facing_probas
- Mean = [0.469375   0.93395833 0.95583333 0.87041667 0.16375   ]
- Standard deviation = [0.12297509 0.03199324 0.01998263 0.0519799  0.09964433]
- Max = [0.65333333 0.98333333 0.98833333 0.935      0.39333333]
- 75% = [0.545      0.95416667 0.96916667 0.90791667 0.17875   ]
- Median = [0.46166667 0.94083333 0.95333333 0.885      0.14916667]
- 25% = [0.44166667 0.90958333 0.93916667 0.84333333 0.1225    ]
- Min = [0.20166667 0.885      0.92833333 0.78333333 0.02      ]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 79.25 | 0.0 |
| Actual Positive | 11.5 | 8.5 |

### robot-4
#### accuracy
- Mean = 0.971010101010101
- Standard deviation = 0.042995433303676826
- Max = 1.0
- 75% = 0.98989898989899
- Median = 0.984949494949495
- 25% = 0.9799494949494949
- Min = 0.8585858585858586

#### f1
- Mean = 0.8968458590169117
- Standard deviation = 0.18233538119696435
- Max = 1.0
- 75% = 0.972972972972973
- Median = 0.9601706970128023
- 25% = 0.9466374269005848
- Min = 0.4166666666666667

#### precision
- Mean = 1.0
- Standard deviation = 0.0
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 1.0
- Min = 1.0

#### recall
- Mean = 0.85
- Standard deviation = 0.22425623453041782
- Max = 1.0
- 75% = 0.9473684210526315
- Median = 0.9236842105263158
- 25% = 0.8986842105263158
- Min = 0.2631578947368421

#### facing_probas
- Mean = [2.19298246e-04 3.88377193e-02 9.07521930e-01 9.75372807e-01
 7.99298246e-01]
- Standard deviation = [0.00058021 0.0190282  0.05835148 0.01133946 0.14999828]
- Max = [0.00175439 0.06491228 0.97894737 0.99473684 0.93859649]
- 75% = [0.         0.05491228 0.94940789 0.98094298 0.86855263]
- Median = [0.         0.03859649 0.92105263 0.97807018 0.84035088]
- 25% = [0.         0.02368421 0.88059211 0.96936404 0.80942982]
- Min = [0.         0.01       0.78070175 0.95614035 0.41929825]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 80.0 | 0.0 |
| Actual Positive | 2.875 | 16.375 |

### robot-5
#### accuracy
- Mean = 0.9962121212121212
- Standard deviation = 0.007030005508623765
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 0.9974747474747475
- Min = 0.9797979797979798

#### f1
- Mean = 0.9909988385598142
- Standard deviation = 0.01663689587778955
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 0.9939024390243902
- Min = 0.9523809523809523

#### precision
- Mean = 0.9826839826839827
- Standard deviation = 0.031885107927827366
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 0.9880952380952381
- Min = 0.9090909090909091

#### recall
- Mean = 1.0
- Standard deviation = 0.0
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 1.0
- Min = 1.0

#### facing_probas
- Mean = [1.04166667e-03 2.08333333e-04 9.04166667e-02 9.64166667e-01
 9.84583333e-01]
- Standard deviation = [0.00165359 0.0005512  0.03229368 0.02211083 0.00599479]
- Max = [0.005      0.00166667 0.13833333 0.99666667 0.99333333]
- 75% = [0.00166667 0.         0.12666667 0.98375    0.98875   ]
- Median = [0.         0.         0.07583333 0.96416667 0.98583333]
- 25% = [0.         0.         0.06458333 0.94833333 0.97958333]
- Min = [0.         0.         0.05166667 0.92666667 0.975     ]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 78.875 | 0.375 |
| Actual Positive | 0.0 | 20.0 |

### robot-6
#### accuracy
- Mean = 0.84375
- Standard deviation = 0.05969794042648512
- Max = 0.9090909090909091
- 75% = 0.8815909090909091
- Median = 0.8643434343434344
- 25% = 0.8181818181818182
- Min = 0.7070707070707071

#### f1
- Mean = 0.9140658805671212
- Standard deviation = 0.03672352471618497
- Max = 0.9523809523809523
- 75% = 0.9370626386755418
- Median = 0.9272304562627144
- 25% = 0.9
- Min = 0.8284023668639052

#### precision
- Mean = 1.0
- Standard deviation = 0.0
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 1.0
- Min = 1.0

#### recall
- Mean = 0.84375
- Standard deviation = 0.05969794042648512
- Max = 0.9090909090909091
- 75% = 0.8815909090909091
- Median = 0.8643434343434344
- 25% = 0.8181818181818182
- Min = 0.7070707070707071

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
| Actual Positive | 15.5 | 83.75 |

