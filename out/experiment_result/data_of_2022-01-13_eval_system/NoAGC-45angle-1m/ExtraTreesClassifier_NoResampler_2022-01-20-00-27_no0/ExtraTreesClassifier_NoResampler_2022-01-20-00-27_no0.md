# ExtraTreesClassifier_NoResampler_2022-01-20-00-27_no0
## Constants
- CSV_PATH = ../out/csv/experiment
- OUTPUT_PATH = ../out/experiment_result/data_of_2022-01-13_eval_system/NoAGC-45angle-1m
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
- AGC_STATUS = ['NoAGC']

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
	- n_estimators = 150
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
- gp_max_val_mean = 0.10992980531225968
- gp_auc_max = 0.09744285409423112
- gp_max_val_max = 0.08000966889599755
- gp_auc_mean = 0.0692012268496942
- gp_auc_min = 0.060328697545357975
- gp_max_val_min = 0.05577118452518879
- gp_max_ix_range = 0.04704463880037024
- gp_max_ix_std = 0.04684814534893547
- tdoa_range = 0.04469270661892822
- tdoa_min = 0.03960777930955754
- tdoa_std = 0.03601468973609196
- hlbr = 0.029836456894748165
- gp_max_ix_min = 0.029256890336056822
- tdoa_mean = 0.02667576097259639
- srmr = 0.025178397006827478
- gp_max_val_std = 0.01854302132304602
- gp_max_ix_mean = 0.0168348523481007
- diff_std = 0.015373778710146871
- diff_auc = 0.015185978594409053
- gp_auc_range = 0.014614153915214504
- gp_max_val_range = 0.014207759802017026
- ratio_max_to_10ms_ave_peaks = 0.01295812209195035
- high_power = 0.011751819202330165
- ratio_max_to_9th_ave_peaks = 0.01125476280131957
- coe1[1] = 0.011241594713463074
- gp_auc_std = 0.010148033090773388
- low_power = 0.008999955808687012
- coe3[3] = 0.00844126817815016
- coe1[0] = 0.006337981435679947
- ac_auc = 0.006084349764352713
- ac_std = 0.005546818143583644
- tdoa_max = 0.005533884318187567
- coe3[2] = 0.005356051343935366
- gp_max_ix_max = 0.0037469121678113683
- coe3[0] = 0.0
- coe3[1] = 0.0

## Evaluation
cv = 8
### robot-1
#### accuracy
- Mean = 0.9937499999999999
- Standard deviation = 0.009921567416492224
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 0.99
- Min = 0.97

#### f1
- Mean = 0.9847560975609756
- Standard deviation = 0.024198944918273714
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 0.975609756097561
- Min = 0.9268292682926829

#### precision
- Mean = 0.9761904761904762
- Standard deviation = 0.033671751485073696
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 0.9523809523809523
- Min = 0.9047619047619048

#### recall
- Mean = 0.99375
- Standard deviation = 0.016535945694153707
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 1.0
- Min = 0.95

#### facing_probas
- Mean = [9.38000000e-01 7.51000000e-01 3.51666667e-02 5.83333333e-04
 4.20833333e-03]
- Standard deviation = [0.03282149 0.08515346 0.01463064 0.0007592  0.0080587 ]
- Max = [0.981      0.87       0.06033333 0.002      0.02533333]
- 75% = [9.53166667e-01 8.37750000e-01 4.38333333e-02 9.16666667e-04
 2.50000000e-03]
- Median = [9.44500000e-01 7.23166667e-01 3.20000000e-02 1.66666667e-04
 1.50000000e-03]
- 25% = [0.9345  0.68725 0.02275 0.      0.     ]
- Min = [0.86066667 0.63766667 0.01933333 0.         0.        ]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 79.5 | 0.5 |
| Actual Positive | 0.125 | 19.875 |

### robot-2
#### accuracy
- Mean = 0.98375
- Standard deviation = 0.009921567416492224
- Max = 0.99
- 75% = 0.99
- Median = 0.99
- 25% = 0.98
- Min = 0.96

#### f1
- Mean = 0.9583164642375168
- Standard deviation = 0.02481768511391406
- Max = 0.9743589743589743
- 75% = 0.9743589743589743
- Median = 0.9743589743589743
- 25% = 0.9473684210526316
- Min = 0.9

#### precision
- Mean = 0.9875
- Standard deviation = 0.03307189138830738
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 1.0
- Min = 0.9

#### recall
- Mean = 0.93125
- Standard deviation = 0.02420614591379632
- Max = 0.95
- 75% = 0.95
- Median = 0.95
- 25% = 0.9
- Min = 0.9

#### facing_probas
- Mean = [0.93025    0.95670833 0.90495833 0.06170833 0.02475   ]
- Standard deviation = [0.01391417 0.00913546 0.02544244 0.02185777 0.00496586]
- Max = [0.94       0.96966667 0.95433333 0.099      0.03166667]
- 75% = [0.93841667 0.96358333 0.92408333 0.08058333 0.02941667]
- Median = [0.93633333 0.9595     0.89533333 0.05616667 0.02466667]
- 25% = [0.931      0.94791667 0.88566667 0.04691667 0.02116667]
- Min = [0.897      0.94233333 0.875      0.033      0.01666667]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 79.75 | 0.25 |
| Actual Positive | 1.375 | 18.625 |

### robot-3
#### accuracy
- Mean = 0.8975
- Standard deviation = 0.02331844763272206
- Max = 0.92
- 75% = 0.9125000000000001
- Median = 0.91
- 25% = 0.8825000000000001
- Min = 0.86

#### f1
- Mean = 0.6465998545392315
- Standard deviation = 0.11318474637833086
- Max = 0.7499999999999999
- 75% = 0.719758064516129
- Median = 0.7096774193548387
- 25% = 0.5809018567639257
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
- Mean = 0.4875
- Standard deviation = 0.1165922381636102
- Max = 0.6
- 75% = 0.5625
- Median = 0.55
- 25% = 0.4125
- Min = 0.3

#### facing_probas
- Mean = [0.3645     0.93441667 0.93104167 0.70604167 0.258875  ]
- Standard deviation = [0.09498187 0.04480816 0.04574095 0.06493703 0.09534454]
- Max = [0.52066667 0.98233333 0.985      0.81933333 0.44233333]
- 75% = [0.40766667 0.97225    0.95983333 0.73058333 0.28833333]
- Median = [0.35533333 0.9485     0.9405     0.69716667 0.22316667]
- 25% = [0.30258333 0.90391667 0.917      0.66825    0.21541667]
- Min = [0.20966667 0.85466667 0.835      0.616      0.12466667]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 80.0 | 0.0 |
| Actual Positive | 10.25 | 9.75 |

### robot-4
#### accuracy
- Mean = 0.9675
- Standard deviation = 0.014790199457749054
- Max = 0.99
- 75% = 0.98
- Median = 0.965
- 25% = 0.96
- Min = 0.94

#### f1
- Mean = 0.9097763517268161
- Standard deviation = 0.04448064466364686
- Max = 0.9743589743589743
- 75% = 0.9473684210526316
- Median = 0.9039039039039038
- 25% = 0.888888888888889
- Min = 0.8235294117647058

#### precision
- Mean = 1.0
- Standard deviation = 0.0
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 1.0
- Min = 1.0

#### recall
- Mean = 0.8375
- Standard deviation = 0.0739509972887452
- Max = 0.95
- 75% = 0.9
- Median = 0.825
- 25% = 0.8
- Min = 0.7

#### facing_probas
- Mean = [0.006625   0.188375   0.80579167 0.94858333 0.90120833]
- Standard deviation = [0.00413131 0.0535297  0.07262268 0.02123202 0.04468375]
- Max = [0.01433333 0.28866667 0.93033333 0.98666667 0.97466667]
- 75% = [0.00975    0.21141667 0.84283333 0.95925    0.91725   ]
- Median = [0.00483333 0.185      0.81166667 0.94833333 0.90583333]
- 25% = [0.00358333 0.15983333 0.75625    0.9415     0.89408333]
- Min = [0.00166667 0.09733333 0.697      0.907      0.802     ]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 80.0 | 0.0 |
| Actual Positive | 3.25 | 16.75 |

### robot-5
#### accuracy
- Mean = 0.98
- Standard deviation = 0.013228756555322964
- Max = 0.99
- 75% = 0.99
- Median = 0.985
- 25% = 0.9775
- Min = 0.95

#### f1
- Mean = 0.9532902970225716
- Standard deviation = 0.028882277266851837
- Max = 0.975609756097561
- 75% = 0.975609756097561
- Median = 0.9639953542392566
- 25% = 0.946843853820598
- Min = 0.888888888888889

#### precision
- Mean = 0.9121588556371165
- Standard deviation = 0.05109295422896557
- Max = 0.9523809523809523
- 75% = 0.9523809523809523
- Median = 0.9307359307359306
- 25% = 0.8992094861660078
- Min = 0.8

#### recall
- Mean = 1.0
- Standard deviation = 0.0
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 1.0
- Min = 1.0

#### facing_probas
- Mean = [0.01441667 0.00745833 0.088875   0.96229167 0.95775   ]
- Standard deviation = [0.01140754 0.00661005 0.05179633 0.03579666 0.02248441]
- Max = [0.03733333 0.02033333 0.17633333 0.99166667 0.98366667]
- 75% = [0.01866667 0.01266667 0.11566667 0.98916667 0.97633333]
- Median = [0.01233333 0.005      0.09233333 0.9755     0.96416667]
- 25% = [0.00391667 0.00216667 0.04041667 0.95566667 0.943     ]
- Min = [0.003      0.         0.017      0.88433333 0.91333333]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 78.0 | 2.0 |
| Actual Positive | 0.0 | 20.0 |

### robot-6
#### accuracy
- Mean = 0.85
- Standard deviation = 0.018708286933869722
- Max = 0.87
- 75% = 0.87
- Median = 0.85
- 25% = 0.8374999999999999
- Min = 0.82

#### f1
- Mean = 0.9188080894775413
- Standard deviation = 0.010959813221685863
- Max = 0.9304812834224598
- 75% = 0.9304812834224598
- Median = 0.9188873305282843
- 25% = 0.9115585649798053
- Min = 0.9010989010989011

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
- Standard deviation = 0.018708286933869722
- Max = 0.87
- 75% = 0.87
- Median = 0.85
- 25% = 0.8374999999999999
- Min = 0.82

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
| Actual Positive | 15.0 | 85.0 |

