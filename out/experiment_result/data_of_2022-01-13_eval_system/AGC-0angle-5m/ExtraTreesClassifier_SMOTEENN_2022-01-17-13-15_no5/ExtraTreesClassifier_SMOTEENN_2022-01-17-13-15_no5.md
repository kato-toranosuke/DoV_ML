# ExtraTreesClassifier_SMOTEENN_2022-01-17-13-15_no5
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
	- n_estimators = 50
	- estimator_params = ('criterion', 'max_depth', 'min_samples_split', 'min_samples_leaf', 'min_weight_fraction_leaf', 'max_features', 'max_leaf_nodes', 'min_impurity_decrease', 'random_state', 'ccp_alpha')
	- bootstrap = True
	- oob_score = True
	- n_jobs = -1
	- random_state = 42
	- verbose = 0
	- warm_start = False
	- class_weight = None
	- max_samples = 0.5
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
	- oob_decision_function_ = [[0.80645161 0.19354839]
 [0.89189189 0.10810811]
 [1.         0.        ]
 [0.96774194 0.03225806]
 [0.93548387 0.06451613]
 [0.51724138 0.48275862]
 [1.         0.        ]
 [0.44       0.56      ]
 [0.63333333 0.36666667]
 [0.64285714 0.35714286]
 [0.79310345 0.20689655]
 [0.97058824 0.02941176]
 [0.66666667 0.33333333]
 [0.60869565 0.39130435]
 [0.66666667 0.33333333]
 [0.91176471 0.08823529]
 [0.92       0.08      ]
 [1.         0.        ]
 [1.         0.        ]
 [0.07142857 0.92857143]
 [0.25       0.75      ]
 [0.06060606 0.93939394]
 [0.06451613 0.93548387]
 [0.06666667 0.93333333]
 [0.08695652 0.91304348]
 [0.29032258 0.70967742]
 [0.03571429 0.96428571]
 [0.03703704 0.96296296]
 [0.09677419 0.90322581]
 [0.07407407 0.92592593]
 [0.32142857 0.67857143]
 [0.07692308 0.92307692]
 [0.06451613 0.93548387]
 [0.03571429 0.96428571]
 [0.13333333 0.86666667]]
	- oob_score_ = 0.9714285714285714

#### Importance of features
- gp_auc_max = 0.07734102317435651
- gp_max_val_std = 0.07485107485107485
- gp_max_val_max = 0.07360521423021424
- tdoa_mean = 0.058961300604157746
- gp_auc_std = 0.05760525813218121
- gp_max_val_mean = 0.05725508906677738
- gp_auc_min = 0.05389744897959183
- gp_max_val_min = 0.05366859331145046
- hlbr = 0.041169580419580416
- coe3[2] = 0.04059906328239661
- gp_auc_mean = 0.03856363636363636
- diff_auc = 0.03671278456992742
- coe1[0] = 0.03072005772005772
- tdoa_max = 0.02863008420151278
- low_power = 0.027902897102897107
- ac_std = 0.026630851976306526
- gp_auc_range = 0.026582273987035894
- coe3[3] = 0.0237012987012987
- ratio_max_to_10ms_ave_peaks = 0.018673076923076928
- coe1[1] = 0.018141558441558438
- gp_max_ix_mean = 0.01759090909090909
- gp_max_ix_range = 0.016645202020202022
- high_power = 0.016371184371184372
- gp_max_val_range = 0.013758779681856603
- gp_max_ix_max = 0.010126498501498502
- srmr = 0.01
- gp_max_ix_min = 0.00974025974025974
- ac_auc = 0.009662087912087914
- diff_std = 0.00948051948051948
- tdoa_std = 0.007948717948717947
- ratio_max_to_9th_ave_peaks = 0.005019230769230769
- tdoa_min = 0.0044444444444444444
- gp_max_ix_std = 0.004000000000000001
- coe3[0] = 0.0
- coe3[1] = 0.0
- tdoa_range = 0.0

## Evaluation
cv = 8
### robot-1
#### accuracy
- Mean = 0.9475
- Standard deviation = 0.023848480035423624
- Max = 0.99
- 75% = 0.955
- Median = 0.95
- 25% = 0.9349999999999999
- Min = 0.91

#### f1
- Mean = 0.8793391530915003
- Standard deviation = 0.04821169334404141
- Max = 0.9743589743589743
- 75% = 0.8992248062015504
- Median = 0.8672150411280846
- 25% = 0.8511904761904762
- Min = 0.8163265306122449

#### precision
- Mean = 0.847989167988727
- Standard deviation = 0.1155509079784308
- Max = 1.0
- 75% = 0.9558823529411764
- Median = 0.8347826086956522
- 25% = 0.7554945054945055
- Min = 0.6896551724137931

#### recall
- Mean = 0.9375
- Standard deviation = 0.09601432184835759
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 0.9125
- Min = 0.75

#### facing_probas
- Mean = [0.80425  0.389875 0.1345   0.05525  0.036875]
- Standard deviation = [0.10512938 0.15607806 0.04711953 0.02489352 0.03281934]
- Max = [0.942 0.708 0.206 0.094 0.11 ]
- 75% = [0.868   0.4755  0.18175 0.07525 0.04125]
- Median = [0.8385 0.338  0.122  0.053  0.0225]
- 25% = [0.728   0.29075 0.10325 0.02975 0.01775]
- Min = [0.639 0.194 0.068 0.026 0.006]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 76.0 | 4.0 |
| Actual Positive | 1.25 | 18.75 |

### robot-2
#### accuracy
- Mean = 0.8825000000000001
- Standard deviation = 0.04968651728587948
- Max = 0.93
- 75% = 0.92
- Median = 0.905
- 25% = 0.86
- Min = 0.8

#### f1
- Mean = 0.6171688633749446
- Standard deviation = 0.24953839344062617
- Max = 0.8292682926829269
- 75% = 0.7658371040723982
- Median = 0.7187499999999999
- 25% = 0.5698757763975156
- Min = 0.0

#### precision
- Mean = 0.7430294486215538
- Standard deviation = 0.3190568287611631
- Max = 1.0
- 75% = 0.9464285714285714
- Median = 0.8630952380952381
- 25% = 0.7171052631578947
- Min = 0.0

#### recall
- Mean = 0.55625
- Standard deviation = 0.24423029603224902
- Max = 0.85
- 75% = 0.675
- Median = 0.625
- 25% = 0.5125000000000001
- Min = 0.0

#### facing_probas
- Mean = [0.519875 0.616375 0.312125 0.193    0.032375]
- Standard deviation = [0.12967212 0.12209723 0.09914817 0.11912913 0.03769263]
- Max = [0.711 0.751 0.464 0.476 0.112]
- 75% = [0.6015  0.7185  0.36675 0.21625 0.038  ]
- Median = [0.5395 0.6325 0.335  0.165  0.017 ]
- 25% = [0.452   0.57175 0.24975 0.107   0.00575]
- Min = [0.259 0.38  0.119 0.089 0.002]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 77.125 | 2.875 |
| Actual Positive | 8.875 | 11.125 |

### robot-3
#### accuracy
- Mean = 0.92625
- Standard deviation = 0.056554730129318095
- Max = 0.99
- 75% = 0.98
- Median = 0.935
- 25% = 0.8925000000000001
- Min = 0.84

#### f1
- Mean = 0.7463545299117461
- Standard deviation = 0.24863706182998893
- Max = 0.975609756097561
- 75% = 0.9480263157894737
- Median = 0.8405956977385549
- 25% = 0.6458333333333333
- Min = 0.33333333333333337

#### precision
- Mean = 0.9416515744228726
- Standard deviation = 0.09830143893878011
- Max = 1.0
- 75% = 1.0
- Median = 0.9761904761904762
- 25% = 0.9477941176470588
- Min = 0.6896551724137931

#### recall
- Mean = 0.7062499999999999
- Standard deviation = 0.316659813522335
- Max = 1.0
- 75% = 0.9624999999999999
- Median = 0.8500000000000001
- 25% = 0.5
- Min = 0.2

#### facing_probas
- Mean = [0.19075  0.558    0.725375 0.505875 0.11675 ]
- Standard deviation = [0.07491954 0.14315638 0.12058082 0.17164457 0.03998046]
- Max = [0.319 0.835 0.909 0.838 0.192]
- 75% = [0.212   0.644   0.7865  0.59175 0.144  ]
- Median = [0.174  0.517  0.754  0.5105 0.1095]
- 25% = [0.13575 0.44025 0.668   0.37775 0.08375]
- Min = [0.108 0.406 0.486 0.282 0.07 ]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 78.5 | 1.5 |
| Actual Positive | 5.875 | 14.125 |

### robot-4
#### accuracy
- Mean = 0.83875
- Standard deviation = 0.09239013746066188
- Max = 0.95
- 75% = 0.8925000000000001
- Median = 0.86
- 25% = 0.83
- Min = 0.63

#### f1
- Mean = 0.6840170958432553
- Standard deviation = 0.13122589079625227
- Max = 0.8717948717948718
- 75% = 0.7503128911138923
- Median = 0.7320574162679425
- 25% = 0.6298701298701297
- Min = 0.4390243902439024

#### precision
- Mean = 0.6128702131673269
- Standard deviation = 0.16356451233367314
- Max = 0.8947368421052632
- 75% = 0.6944444444444444
- Median = 0.6064516129032258
- 25% = 0.5357142857142857
- Min = 0.3508771929824561

#### recall
- Mean = 0.825
- Standard deviation = 0.175
- Max = 1.0
- 75% = 0.9624999999999999
- Median = 0.875
- 25% = 0.7375
- Min = 0.45

#### facing_probas
- Mean = [0.0435   0.140125 0.51725  0.802125 0.35    ]
- Standard deviation = [0.0211542  0.03610899 0.10252774 0.07902759 0.07713948]
- Max = [0.092 0.202 0.684 0.919 0.479]
- 75% = [0.0485 0.1505 0.5795 0.8515 0.3915]
- Median = [0.0405 0.1395 0.529  0.804  0.359 ]
- 25% = [0.0325  0.13075 0.458   0.74925 0.288  ]
- Min = [0.015 0.073 0.328 0.669 0.223]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 67.375 | 12.625 |
| Actual Positive | 3.5 | 16.5 |

### robot-5
#### accuracy
- Mean = 0.865
- Standard deviation = 0.028722813232690134
- Max = 0.9
- 75% = 0.8825000000000001
- Median = 0.87
- 25% = 0.8574999999999999
- Min = 0.8

#### f1
- Mean = 0.4752256045359493
- Standard deviation = 0.19293367605378775
- Max = 0.6666666666666666
- 75% = 0.583743842364532
- Median = 0.5185185185185185
- 25% = 0.45726495726495725
- Min = 0.0

#### precision
- Mean = 0.8571428571428572
- Standard deviation = 0.3273268353539886
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 0.9642857142857143
- Min = 0.0

#### recall
- Mean = 0.33125
- Standard deviation = 0.14128318194321646
- Max = 0.5
- 75% = 0.41250000000000003
- Median = 0.35
- 25% = 0.3
- Min = 0.0

#### facing_probas
- Mean = [0.03775  0.041125 0.133375 0.66425  0.627125]
- Standard deviation = [0.02508859 0.02448692 0.04332706 0.14195488 0.1263996 ]
- Max = [0.086 0.093 0.213 0.871 0.811]
- 75% = [0.04925 0.051   0.14975 0.738   0.711  ]
- Median = [0.037  0.03   0.1325 0.702  0.6425]
- 25% = [0.01425 0.02475 0.1115  0.59125 0.57675]
- Min = [0.008 0.017 0.056 0.422 0.39 ]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 79.875 | 0.125 |
| Actual Positive | 13.375 | 6.625 |

### robot-6
#### accuracy
- Mean = 0.67125
- Standard deviation = 0.07606535019310696
- Max = 0.77
- 75% = 0.7275
- Median = 0.685
- 25% = 0.6275000000000001
- Min = 0.55

#### f1
- Mean = 0.8007506798358766
- Standard deviation = 0.05585242980512613
- Max = 0.8700564971751412
- 75% = 0.8421926910299002
- Median = 0.8130459284305438
- 25% = 0.7703962703962705
- Min = 0.7096774193548387

#### precision
- Mean = 1.0
- Standard deviation = 0.0
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 1.0
- Min = 1.0

#### recall
- Mean = 0.67125
- Standard deviation = 0.07606535019310696
- Max = 0.77
- 75% = 0.7275
- Median = 0.685
- 25% = 0.6275000000000001
- Min = 0.55

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
| Actual Positive | 32.875 | 67.125 |

