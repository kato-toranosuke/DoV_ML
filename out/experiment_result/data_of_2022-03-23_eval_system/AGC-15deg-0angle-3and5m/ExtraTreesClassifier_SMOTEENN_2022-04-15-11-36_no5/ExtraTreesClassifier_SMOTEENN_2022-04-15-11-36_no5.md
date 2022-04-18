# ExtraTreesClassifier_SMOTEENN_2022-04-15-11-36_no5
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
	- oob_decision_function_ = [[0.5        0.5       ]
 [0.33333333 0.66666667]
 [0.55555556 0.44444444]
 [0.5        0.5       ]
 [0.5        0.5       ]
 [0.55555556 0.44444444]
 [0.55555556 0.44444444]
 [0.44444444 0.55555556]
 [0.44444444 0.55555556]
 [0.5        0.5       ]
 [0.625      0.375     ]
 [0.44444444 0.55555556]
 [0.28571429 0.71428571]
 [0.44444444 0.55555556]
 [0.5        0.5       ]
 [0.4        0.6       ]
 [0.4        0.6       ]
 [0.44444444 0.55555556]
 [0.44444444 0.55555556]
 [0.6        0.4       ]
 [0.5        0.5       ]
 [0.55555556 0.44444444]
 [0.66666667 0.33333333]
 [0.66666667 0.33333333]
 [0.66666667 0.33333333]
 [0.44444444 0.55555556]
 [0.5        0.5       ]
 [0.55555556 0.44444444]
 [0.55555556 0.44444444]
 [0.55555556 0.44444444]
 [0.66666667 0.33333333]
 [0.66666667 0.33333333]
 [0.625      0.375     ]
 [0.7        0.3       ]
 [0.44444444 0.55555556]]
	- oob_score_ = 0.34285714285714286

#### Importance of features
- diff_auc = 0.25
- gp_max_val_std = 0.125
- gp_max_val_max = 0.125
- gp_max_ix_std = 0.125
- tdoa_min = 0.125
- coe1[0] = 0.09375
- gp_max_ix_min = 0.09375
- gp_max_val_mean = 0.031249999999999997
- tdoa_mean = 0.031249999999999997
- low_power = 0.0
- high_power = 0.0
- hlbr = 0.0
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
- srmr = 0.0
- gp_max_val_range = 0.0
- gp_max_val_min = 0.0
- gp_max_ix_range = 0.0
- gp_max_ix_max = 0.0
- gp_max_ix_mean = 0.0
- gp_auc_std = 0.0
- gp_auc_range = 0.0
- gp_auc_min = 0.0
- gp_auc_max = 0.0
- gp_auc_mean = 0.0
- tdoa_std = 0.0
- tdoa_range = 0.0
- tdoa_max = 0.0

## Evaluation
cv = 8
### robot-1
#### accuracy
- Mean = 0.683125
- Standard deviation = 0.05857353818064946
- Max = 0.79
- 75% = 0.71875
- Median = 0.6825
- 25% = 0.6325000000000001
- Min = 0.605

#### f1
- Mean = 0.22696654535334254
- Standard deviation = 0.09768462868955996
- Max = 0.3870967741935484
- 75% = 0.28028921313183947
- Median = 0.2515822784810126
- 25% = 0.1685870224378411
- Min = 0.05555555555555556

#### precision
- Mean = 0.2375128122687217
- Standard deviation = 0.11641424263795985
- Max = 0.4375
- 75% = 0.31407232704402516
- Median = 0.24295922656578395
- 25% = 0.14619883040935672
- Min = 0.0625

#### recall
- Mean = 0.2375
- Standard deviation = 0.11792476415070755
- Max = 0.45
- 75% = 0.29375
- Median = 0.2375
- 25% = 0.16249999999999998
- Min = 0.05

#### facing_probas
- Mean = [0.4646875 0.476875  0.43      0.4628125 0.4628125]
- Standard deviation = [0.08201027 0.09942609 0.07733854 0.1111266  0.11278047]
- Max = [0.575  0.615  0.5525 0.6125 0.625 ]
- 75% = [0.525    0.555625 0.48875  0.5425   0.541875]
- Median = [0.47375 0.485   0.445   0.50375 0.4975 ]
- 25% = [0.395    0.415625 0.3475   0.38375  0.349375]
- Min = [0.335  0.29   0.3225 0.2725 0.3025]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 127.125 | 32.875 |
| Actual Positive | 30.5 | 9.5 |

### robot-2
#### accuracy
- Mean = 0.705625
- Standard deviation = 0.05881313097429859
- Max = 0.79
- 75% = 0.7525
- Median = 0.7175
- 25% = 0.64
- Min = 0.63

#### f1
- Mean = 0.1786403996579416
- Standard deviation = 0.11053878758826949
- Max = 0.3243243243243243
- 75% = 0.2886516853932585
- Median = 0.16204051012753187
- 25% = 0.10208333333333333
- Min = 0.0

#### precision
- Mean = 0.19259014376501588
- Standard deviation = 0.10622501086759316
- Max = 0.35294117647058826
- 75% = 0.24642857142857144
- Median = 0.22077922077922077
- 25% = 0.1328804347826087
- Min = 0.0

#### recall
- Mean = 0.18125
- Standard deviation = 0.12732217992164602
- Max = 0.35
- 75% = 0.3125
- Median = 0.15
- 25% = 0.075
- Min = 0.0

#### facing_probas
- Mean = [0.5046875 0.4971875 0.43625   0.5146875 0.46125  ]
- Standard deviation = [0.07013867 0.10909742 0.09140398 0.08279717 0.12133373]
- Max = [0.6275 0.6575 0.5825 0.63   0.62  ]
- 75% = [0.539375 0.558125 0.49625  0.568125 0.5675  ]
- Median = [0.48625 0.49875 0.4375  0.515   0.47375]
- 25% = [0.443125 0.400625 0.3525   0.478125 0.3625  ]
- Min = [0.4325 0.3625 0.3075 0.3625 0.2725]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 133.875 | 26.125 |
| Actual Positive | 32.75 | 7.25 |

### robot-3
#### accuracy
- Mean = 0.756875
- Standard deviation = 0.022070554478761988
- Max = 0.79
- 75% = 0.77
- Median = 0.755
- 25% = 0.74625
- Min = 0.72

#### f1
- Mean = 0.07099398830848955
- Standard deviation = 0.07575655910534188
- Max = 0.21875
- 75% = 0.12823275862068967
- Median = 0.04313543599257885
- 25% = 0.0
- Min = 0.0

#### precision
- Mean = 0.13020833333333331
- Standard deviation = 0.11260658102903837
- Max = 0.2916666666666667
- 75% = 0.22916666666666666
- Median = 0.1388888888888889
- 25% = 0.0
- Min = 0.0

#### recall
- Mean = 0.053125000000000006
- Standard deviation = 0.060515364784490884
- Max = 0.175
- 75% = 0.1
- Median = 0.025
- 25% = 0.0
- Min = 0.0

#### facing_probas
- Mean = [0.48      0.4678125 0.4178125 0.4990625 0.4496875]
- Standard deviation = [0.05108204 0.10550057 0.09271459 0.07419292 0.11329881]
- Max = [0.575  0.62   0.5825 0.6175 0.6275]
- 75% = [0.509375 0.5425   0.480625 0.555    0.53375 ]
- Median = [0.46625 0.47    0.38375 0.4825  0.45625]
- 25% = [0.445625 0.365    0.344375 0.46     0.3725  ]
- Min = [0.4175 0.3275 0.3125 0.37   0.2825]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 149.25 | 10.75 |
| Actual Positive | 37.875 | 2.125 |

### robot-4
#### accuracy
- Mean = 0.724375
- Standard deviation = 0.03282886496667225
- Max = 0.785
- 75% = 0.74
- Median = 0.725
- 25% = 0.69875
- Min = 0.675

#### f1
- Mean = 0.1549354744426583
- Standard deviation = 0.08788880387117878
- Max = 0.35294117647058826
- 75% = 0.17723880597014924
- Median = 0.1336675020885547
- 25% = 0.10457984052341035
- Min = 0.04444444444444445

#### precision
- Mean = 0.20270287325514308
- Standard deviation = 0.06839427228203505
- Max = 0.3333333333333333
- 75% = 0.24128540305010893
- Median = 0.19375
- 25% = 0.16073781291172595
- Min = 0.1111111111111111

#### recall
- Mean = 0.13749999999999998
- Standard deviation = 0.09921567416492214
- Max = 0.375
- 75% = 0.15625
- Median = 0.1
- 25% = 0.09375
- Min = 0.025

#### facing_probas
- Mean = [0.46875   0.4840625 0.4459375 0.4921875 0.461875 ]
- Standard deviation = [0.0638602  0.11256205 0.0758899  0.07858552 0.10591676]
- Max = [0.5775 0.6625 0.595  0.61   0.585 ]
- 75% = [0.501875 0.57     0.48     0.52875  0.54    ]
- Median = [0.47    0.4975  0.435   0.49    0.49875]
- 25% = [0.4075   0.393125 0.385    0.45     0.38875 ]
- Min = [0.385  0.3175 0.3625 0.3575 0.2825]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 139.375 | 20.625 |
| Actual Positive | 34.5 | 5.5 |

### robot-5
#### accuracy
- Mean = 0.749375
- Standard deviation = 0.043115941077517955
- Max = 0.785
- 75% = 0.78125
- Median = 0.76
- 25% = 0.7424999999999999
- Min = 0.645

#### f1
- Mean = 0.06705445806326638
- Standard deviation = 0.06105012733951589
- Max = 0.20224719101123595
- 75% = 0.08202750239846499
- Median = 0.05810276679841897
- 25% = 0.030612244897959186
- Min = 0.0

#### precision
- Mean = 0.11331568389839067
- Standard deviation = 0.0684771961692796
- Max = 0.1836734693877551
- 75% = 0.1600877192982456
- Median = 0.14358974358974358
- 25% = 0.08333333333333333
- Min = 0.0

#### recall
- Mean = 0.05625
- Standard deviation = 0.06817945071647322
- Max = 0.225
- 75% = 0.05625
- Median = 0.037500000000000006
- 25% = 0.018750000000000003
- Min = 0.0

#### facing_probas
- Mean = [0.4703125 0.4759375 0.4453125 0.4928125 0.4653125]
- Standard deviation = [0.08231454 0.11328847 0.04804681 0.06094872 0.11046378]
- Max = [0.61   0.655  0.56   0.5925 0.635 ]
- 75% = [0.53375  0.53625  0.445625 0.53875  0.528125]
- Median = [0.47375 0.4875  0.42875 0.48625 0.47875]
- 25% = [0.389375 0.401875 0.414375 0.463125 0.411875]
- Min = [0.3575 0.315  0.405  0.38   0.295 ]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 147.625 | 12.375 |
| Actual Positive | 37.75 | 2.25 |

### robot-6
#### accuracy
- Mean = 0.133125
- Standard deviation = 0.07141154931101833
- Max = 0.25
- 75% = 0.17625000000000002
- Median = 0.1375
- 25% = 0.09
- Min = 0.015

#### f1
- Mean = 0.22787506290523474
- Standard deviation = 0.11281008522129475
- Max = 0.4
- 75% = 0.2995386761077138
- Median = 0.24073000038665274
- 25% = 0.1646655231560892
- Min = 0.02955665024630542

#### precision
- Mean = 1.0
- Standard deviation = 0.0
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 1.0
- Min = 1.0

#### recall
- Mean = 0.133125
- Standard deviation = 0.07141154931101833
- Max = 0.25
- 75% = 0.17625000000000002
- Median = 0.1375
- 25% = 0.09
- Min = 0.015

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
| Actual Positive | 173.375 | 26.625 |

