# ExtraTreesClassifier_SMOTE_2022-04-15-10-32_no4
## Constants
- CSV_PATH = ../out/csv/experiment
- OUTPUT_PATH = ../out/experiment_result/data_of_2022-03-23_eval_system/AGC-15deg-0angle-3and5m
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
- DISTANCE = [3, 5]
- AGC_STATUS = ['AGC-15deg']
- ANGLES = [60, 75, 90, 105, 120]

## Loaded CSV
- 2022-03-23_raspi_48000Hz_w1_N2^12_overlap80_all.csv

## Estimator
### Type
- resampler = SMOTE
- estimator = ExtraTreesClassifier

### Arguments for hyperparameter search
- resampler = SMOTE
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
	- k_neighbors = 5
	- n_jobs = -1
	- n_features_in_ = 36
	- sampling_strategy_ = OrderedDict([(1, 90)])
	- nn_k_ = NearestNeighbors(n_neighbors=6)

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
	- oob_decision_function_ = [[0.4        0.6       ]
 [0.5        0.5       ]
 [0.5        0.5       ]
 [0.5        0.5       ]
 [0.5        0.5       ]
 [0.5        0.5       ]
 [0.5        0.5       ]
 [0.5        0.5       ]
 [0.5        0.5       ]
 [0.4        0.6       ]
 [0.5        0.5       ]
 [0.66666667 0.33333333]
 [0.6        0.4       ]
 [0.44444444 0.55555556]
 [0.6        0.4       ]
 [0.6        0.4       ]
 [0.5        0.5       ]
 [0.4        0.6       ]
 [0.6        0.4       ]
 [0.5        0.5       ]
 [0.4        0.6       ]
 [0.5        0.5       ]
 [0.4        0.6       ]
 [0.5        0.5       ]
 [0.6        0.4       ]
 [0.5        0.5       ]
 [0.5        0.5       ]
 [0.5        0.5       ]
 [0.5        0.5       ]
 [0.6        0.4       ]
 [0.8        0.2       ]
 [0.7        0.3       ]
 [0.55555556 0.44444444]
 [0.6        0.4       ]
 [0.4        0.6       ]
 [0.6        0.4       ]
 [0.6        0.4       ]
 [0.5        0.5       ]
 [0.6        0.4       ]
 [0.4        0.6       ]
 [0.5        0.5       ]
 [0.33333333 0.66666667]
 [0.5        0.5       ]
 [0.5        0.5       ]
 [0.5        0.5       ]
 [0.6        0.4       ]
 [0.6        0.4       ]
 [0.4        0.6       ]
 [0.6        0.4       ]
 [0.5        0.5       ]
 [0.4        0.6       ]
 [0.6        0.4       ]
 [0.4        0.6       ]
 [0.7        0.3       ]
 [0.5        0.5       ]
 [0.4        0.6       ]
 [0.4        0.6       ]
 [0.5        0.5       ]
 [0.6        0.4       ]
 [0.5        0.5       ]
 [0.7        0.3       ]
 [0.5        0.5       ]
 [0.5        0.5       ]
 [0.5        0.5       ]
 [0.4        0.6       ]
 [0.44444444 0.55555556]
 [0.4        0.6       ]
 [0.5        0.5       ]
 [0.5        0.5       ]
 [0.33333333 0.66666667]
 [0.5        0.5       ]
 [0.4        0.6       ]
 [0.4        0.6       ]
 [0.4        0.6       ]
 [0.5        0.5       ]
 [0.6        0.4       ]
 [0.7        0.3       ]
 [0.6        0.4       ]
 [0.7        0.3       ]
 [0.7        0.3       ]
 [0.6        0.4       ]
 [0.6        0.4       ]
 [0.6        0.4       ]
 [0.7        0.3       ]
 [0.6        0.4       ]
 [0.6        0.4       ]
 [0.55555556 0.44444444]
 [0.7        0.3       ]
 [0.5        0.5       ]
 [0.6        0.4       ]
 [0.6        0.4       ]
 [0.7        0.3       ]
 [0.7        0.3       ]
 [0.7        0.3       ]
 [0.55555556 0.44444444]
 [0.7        0.3       ]
 [0.6        0.4       ]
 [0.7        0.3       ]
 [0.6        0.4       ]
 [0.5        0.5       ]
 [0.6        0.4       ]
 [0.6        0.4       ]
 [0.6        0.4       ]
 [0.5        0.5       ]
 [0.6        0.4       ]
 [0.6        0.4       ]
 [0.5        0.5       ]
 [0.5        0.5       ]
 [0.7        0.3       ]
 [0.5        0.5       ]
 [0.4        0.6       ]
 [0.5        0.5       ]
 [0.4        0.6       ]
 [0.6        0.4       ]
 [0.5        0.5       ]
 [0.5        0.5       ]
 [0.5        0.5       ]
 [0.5        0.5       ]
 [0.4        0.6       ]
 [0.6        0.4       ]
 [0.7        0.3       ]
 [0.6        0.4       ]
 [0.7        0.3       ]
 [0.5        0.5       ]
 [0.5        0.5       ]
 [0.6        0.4       ]
 [0.6        0.4       ]
 [0.6        0.4       ]
 [0.5        0.5       ]
 [0.4        0.6       ]
 [0.4        0.6       ]
 [0.5        0.5       ]
 [0.4        0.6       ]
 [0.5        0.5       ]
 [0.5        0.5       ]
 [0.6        0.4       ]
 [0.66666667 0.33333333]
 [0.6        0.4       ]
 [0.5        0.5       ]
 [0.6        0.4       ]
 [0.44444444 0.55555556]
 [0.6        0.4       ]
 [0.5        0.5       ]
 [0.6        0.4       ]
 [0.6        0.4       ]
 [0.5        0.5       ]
 [0.5        0.5       ]
 [0.5        0.5       ]
 [0.5        0.5       ]
 [0.6        0.4       ]
 [0.7        0.3       ]
 [0.66666667 0.33333333]
 [0.5        0.5       ]
 [0.5        0.5       ]
 [0.5        0.5       ]
 [0.5        0.5       ]
 [0.6        0.4       ]
 [0.4        0.6       ]
 [0.5        0.5       ]
 [0.5        0.5       ]
 [0.5        0.5       ]
 [0.5        0.5       ]
 [0.5        0.5       ]
 [0.6        0.4       ]
 [0.6        0.4       ]
 [0.5        0.5       ]
 [0.4        0.6       ]
 [0.5        0.5       ]
 [0.44444444 0.55555556]
 [0.5        0.5       ]
 [0.5        0.5       ]
 [0.4        0.6       ]
 [0.5        0.5       ]
 [0.5        0.5       ]
 [0.71428571 0.28571429]
 [0.4        0.6       ]
 [0.5        0.5       ]
 [0.5        0.5       ]
 [0.5        0.5       ]
 [0.5        0.5       ]
 [0.5        0.5       ]
 [0.6        0.4       ]
 [0.5        0.5       ]
 [0.4        0.6       ]
 [0.5        0.5       ]
 [0.5        0.5       ]
 [0.6        0.4       ]
 [0.4        0.6       ]
 [0.5        0.5       ]
 [0.6        0.4       ]
 [0.5        0.5       ]
 [0.5        0.5       ]
 [0.5        0.5       ]
 [0.4        0.6       ]
 [0.5        0.5       ]
 [0.5        0.5       ]
 [0.5        0.5       ]
 [0.5        0.5       ]
 [0.5        0.5       ]
 [0.5        0.5       ]
 [0.5        0.5       ]
 [0.4        0.6       ]
 [0.6        0.4       ]
 [0.4        0.6       ]
 [0.4        0.6       ]
 [0.5        0.5       ]
 [0.5        0.5       ]
 [0.5        0.5       ]
 [0.6        0.4       ]
 [0.5        0.5       ]
 [0.6        0.4       ]
 [0.6        0.4       ]
 [0.6        0.4       ]
 [0.44444444 0.55555556]
 [0.6        0.4       ]
 [0.5        0.5       ]
 [0.4        0.6       ]
 [0.5        0.5       ]
 [0.5        0.5       ]
 [0.55555556 0.44444444]
 [0.55555556 0.44444444]
 [0.6        0.4       ]
 [0.6        0.4       ]
 [0.5        0.5       ]
 [0.4        0.6       ]
 [0.5        0.5       ]
 [0.5        0.5       ]
 [0.5        0.5       ]
 [0.6        0.4       ]
 [0.6        0.4       ]
 [0.6        0.4       ]
 [0.6        0.4       ]
 [0.5        0.5       ]
 [0.5        0.5       ]
 [0.5        0.5       ]
 [0.7        0.3       ]
 [0.5        0.5       ]
 [0.44444444 0.55555556]
 [0.4        0.6       ]
 [0.6        0.4       ]]
	- oob_score_ = 0.5

#### Importance of features
- low_power = 0.2
- gp_max_val_std = 0.2
- gp_max_val_max = 0.2
- gp_max_ix_std = 0.2
- tdoa_mean = 0.2
- high_power = 0.0
- hlbr = 0.0
- coe1[0] = 0.0
- coe1[1] = 0.0
- coe3[0] = 0.0
- coe3[1] = 0.0
- coe3[2] = 0.0
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
- gp_max_val_mean = 0.0
- gp_max_ix_range = 0.0
- gp_max_ix_min = 0.0
- gp_max_ix_max = 0.0
- gp_max_ix_mean = 0.0
- gp_auc_std = 0.0
- gp_auc_range = 0.0
- gp_auc_min = 0.0
- gp_auc_max = 0.0
- gp_auc_mean = 0.0
- tdoa_std = 0.0
- tdoa_range = 0.0
- tdoa_min = 0.0
- tdoa_max = 0.0

## Evaluation
cv = 8
### robot-1
#### accuracy
- Mean = 0.6881250000000001
- Standard deviation = 0.08215600632333585
- Max = 0.8
- 75% = 0.75875
- Median = 0.6875
- 25% = 0.6325000000000001
- Min = 0.555

#### f1
- Mean = 0.22463131213630255
- Standard deviation = 0.10858822152221093
- Max = 0.3582089552238806
- 75% = 0.30695676274944567
- Median = 0.22740681147760794
- 25% = 0.18804331249046818
- Min = 0.0

#### precision
- Mean = 0.22312859801947843
- Standard deviation = 0.12239779461117518
- Max = 0.4444444444444444
- 75% = 0.2800480769230769
- Median = 0.2290701266604881
- 25% = 0.15817139216310927
- Min = 0.0

#### recall
- Mean = 0.25
- Standard deviation = 0.14306903927824496
- Max = 0.525
- 75% = 0.30625
- Median = 0.25
- 25% = 0.1875
- Min = 0.0

#### facing_probas
- Mean = [0.47      0.4284375 0.4325    0.43625   0.4546875]
- Standard deviation = [0.05235098 0.06373698 0.0626124  0.06730295 0.07341489]
- Max = [0.545  0.505  0.4825 0.52   0.56  ]
- 75% = [0.49875  0.48     0.474375 0.475    0.49375 ]
- Median = [0.4725  0.42875 0.45125 0.46    0.46125]
- 25% = [0.455625 0.4125   0.425    0.42125  0.44375 ]
- Min = [0.3575 0.29   0.2775 0.295  0.3   ]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 127.625 | 32.375 |
| Actual Positive | 30.0 | 10.0 |

### robot-2
#### accuracy
- Mean = 0.761875
- Standard deviation = 0.03151760420780745
- Max = 0.8
- 75% = 0.78125
- Median = 0.775
- 25% = 0.74375
- Min = 0.695

#### f1
- Mean = 0.23125610118476614
- Standard deviation = 0.11884480847354668
- Max = 0.36111111111111116
- 75% = 0.3226102941176471
- Median = 0.2683319903303787
- 25% = 0.15389991613083592
- Min = 0.0

#### precision
- Mean = 0.29821090367965364
- Standard deviation = 0.13592204794223825
- Max = 0.42857142857142855
- 75% = 0.4088541666666667
- Median = 0.3333333333333333
- 25% = 0.2597402597402597
- Min = 0.0

#### recall
- Mean = 0.196875
- Standard deviation = 0.10711960313126631
- Max = 0.325
- 75% = 0.28125
- Median = 0.225
- 25% = 0.13125
- Min = 0.0

#### facing_probas
- Mean = [0.4740625 0.4996875 0.41875   0.4609375 0.45375  ]
- Standard deviation = [0.04656879 0.04684478 0.04680411 0.05018618 0.05448624]
- Max = [0.5475 0.575  0.4825 0.525  0.505 ]
- 75% = [0.489375 0.52625  0.45     0.481875 0.48625 ]
- Median = [0.475   0.49375 0.42    0.4725  0.465  ]
- 25% = [0.46875  0.488125 0.400625 0.454375 0.45125 ]
- Min = [0.3725 0.4025 0.32   0.3425 0.32  ]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 144.5 | 15.5 |
| Actual Positive | 32.125 | 7.875 |

### robot-3
#### accuracy
- Mean = 0.778125
- Standard deviation = 0.025973243443975207
- Max = 0.8
- 75% = 0.8
- Median = 0.7875000000000001
- 25% = 0.77
- Min = 0.73

#### f1
- Mean = 0.04383116883116883
- Standard deviation = 0.07085025956990501
- Max = 0.2121212121212121
- 75% = 0.05844155844155844
- Median = 0.0
- 25% = 0.0
- Min = 0.0

#### precision
- Mean = 0.15865384615384615
- Standard deviation = 0.21538246908271266
- Max = 0.5
- 75% = 0.3269230769230769
- Median = 0.0
- 25% = 0.0
- Min = 0.0

#### recall
- Mean = 0.03125
- Standard deviation = 0.05694020986965186
- Max = 0.175
- 75% = 0.03125
- Median = 0.0
- 25% = 0.0
- Min = 0.0

#### facing_probas
- Mean = [0.48      0.464375  0.426875  0.4678125 0.4553125]
- Standard deviation = [0.04687083 0.04464705 0.04534159 0.044729   0.04471153]
- Max = [0.555  0.5325 0.48   0.54   0.515 ]
- 75% = [0.508125 0.486875 0.46375  0.4825   0.47375 ]
- Median = [0.47875 0.4675  0.425   0.4675  0.46125]
- 25% = [0.464375 0.44875  0.4125   0.46     0.45375 ]
- Min = [0.3825 0.37   0.33   0.3725 0.35  ]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 154.375 | 5.625 |
| Actual Positive | 38.75 | 1.25 |

### robot-4
#### accuracy
- Mean = 0.7581249999999999
- Standard deviation = 0.025116914121762673
- Max = 0.8
- 75% = 0.775
- Median = 0.7525
- 25% = 0.74125
- Min = 0.725

#### f1
- Mean = 0.03895058507472695
- Standard deviation = 0.039880774988673526
- Max = 0.11538461538461538
- 75% = 0.050585284280936456
- Median = 0.03540100250626567
- 25% = 0.0
- Min = 0.0

#### precision
- Mean = 0.09849877450980392
- Standard deviation = 0.11742334974811584
- Max = 0.3333333333333333
- 75% = 0.125
- Median = 0.06066176470588235
- 25% = 0.0
- Min = 0.0

#### recall
- Mean = 0.025
- Standard deviation = 0.025
- Max = 0.075
- 75% = 0.03125
- Median = 0.025
- 25% = 0.0
- Min = 0.0

#### facing_probas
- Mean = [0.4734375 0.4646875 0.426875  0.4425    0.44875  ]
- Standard deviation = [0.04979548 0.04588432 0.04881006 0.04930771 0.04244482]
- Max = [0.5325 0.53   0.4875 0.5175 0.5025]
- 75% = [0.494375 0.491875 0.47125  0.4575   0.4625  ]
- Median = [0.4825  0.47125 0.42125 0.44625 0.4575 ]
- 25% = [0.4725   0.450625 0.40875  0.436875 0.450625]
- Min = [0.3525 0.365  0.325  0.3325 0.345 ]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 150.625 | 9.375 |
| Actual Positive | 39.0 | 1.0 |

### robot-5
#### accuracy
- Mean = 0.785625
- Standard deviation = 0.023774658252012814
- Max = 0.805
- 75% = 0.79625
- Median = 0.795
- 25% = 0.785
- Min = 0.725

#### f1
- Mean = 0.01048352588789046
- Standard deviation = 0.01847785673345863
- Max = 0.04878048780487806
- 75% = 0.008771929824561403
- Median = 0.0
- 25% = 0.0
- Min = 0.0

#### precision
- Mean = 0.1323529411764706
- Standard deviation = 0.32850452799542174
- Max = 1.0
- 75% = 0.014705882352941176
- Median = 0.0
- 25% = 0.0
- Min = 0.0

#### recall
- Mean = 0.00625
- Standard deviation = 0.010825317547305485
- Max = 0.025
- 75% = 0.00625
- Median = 0.0
- 25% = 0.0
- Min = 0.0

#### facing_probas
- Mean = [0.4696875 0.4565625 0.444375  0.461875  0.445    ]
- Standard deviation = [0.05971858 0.04881306 0.05703275 0.04871393 0.04382137]
- Max = [0.535  0.5    0.5025 0.52   0.49  ]
- 75% = [0.495    0.491875 0.48125  0.484375 0.4675  ]
- Median = [0.49125 0.46375 0.46625 0.46625 0.45375]
- 25% = [0.46875  0.45125  0.425625 0.45625  0.44    ]
- Min = [0.325  0.3375 0.3125 0.35   0.3425]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 156.875 | 3.125 |
| Actual Positive | 39.75 | 0.25 |

### robot-6
#### accuracy
- Mean = 0.101875
- Standard deviation = 0.046766541191326096
- Max = 0.165
- 75% = 0.13375
- Median = 0.1
- 25% = 0.08875
- Min = 0.0

#### f1
- Mean = 0.18150078503165512
- Standard deviation = 0.08049118576584423
- Max = 0.2832618025751073
- 75% = 0.23588514897399238
- Median = 0.18178061530196904
- 25% = 0.16302371792161668
- Min = 0.0

#### precision
- Mean = 0.875
- Standard deviation = 0.33071891388307384
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 1.0
- Min = 0.0

#### recall
- Mean = 0.101875
- Standard deviation = 0.046766541191326096
- Max = 0.165
- 75% = 0.13375
- Median = 0.1
- 25% = 0.08875
- Min = 0.0

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
| Actual Positive | 179.625 | 20.375 |

