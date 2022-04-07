# ExtraTreesClassifier_RandomOverSampler_2022-01-20-02-34_no3
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
- resampler = RandomOverSampler
- estimator = ExtraTreesClassifier

### Arguments for hyperparameter search
- resampler = RandomOverSampler
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
	- shrinkage = None
	- n_features_in_ = 36
	- sampling_strategy_ = OrderedDict([(0, 3)])
	- shrinkage_ = None
	- sample_indices_ = [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23
 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47
 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71
 72 73 74 57 31 15]

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
- gp_max_val_mean = 0.10400830385989514
- gp_auc_max = 0.1010966003947919
- gp_max_val_max = 0.09548968082318005
- gp_auc_mean = 0.08162451712498384
- gp_max_val_min = 0.06362867548453367
- gp_max_ix_range = 0.05271419765724983
- tdoa_mean = 0.04073606451992607
- gp_auc_min = 0.03594178187098652
- srmr = 0.035063975359424134
- tdoa_range = 0.03324934024822148
- tdoa_min = 0.03133432609051143
- hlbr = 0.027439765782688103
- gp_max_ix_std = 0.026082446767051733
- tdoa_std = 0.024559668216369544
- gp_max_ix_mean = 0.023456145719434208
- gp_auc_range = 0.02249546438446405
- gp_max_ix_min = 0.021405786446272272
- gp_max_val_range = 0.019671007185545975
- diff_std = 0.015140274490299378
- coe1[1] = 0.013204887114736342
- gp_max_ix_max = 0.01256585475738991
- diff_auc = 0.012483307225533627
- ratio_max_to_9th_ave_peaks = 0.011695538866591498
- ratio_max_to_10ms_ave_peaks = 0.011324200886166697
- gp_auc_std = 0.011094134079523976
- high_power = 0.010808907999927874
- ac_std = 0.010587861683295254
- gp_max_val_std = 0.010469779033881596
- tdoa_max = 0.008875438590320767
- coe3[3] = 0.008844075314663552
- low_power = 0.006786244630047687
- coe1[0] = 0.0064722359695973475
- ac_auc = 0.005982304732304731
- coe3[2] = 0.0036672066901898073
- coe3[0] = 0.0
- coe3[1] = 0.0

## Evaluation
cv = 8
### robot-1
#### accuracy
- Mean = 0.9975
- Standard deviation = 0.004330127018922197
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 0.9975
- Min = 0.99

#### f1
- Mean = 0.9937460913070669
- Standard deviation = 0.010836600031997167
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 0.9939024390243902
- Min = 0.9743589743589743

#### precision
- Mean = 0.9940476190476191
- Standard deviation = 0.01574851970871782
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 1.0
- Min = 0.9523809523809523

#### recall
- Mean = 0.99375
- Standard deviation = 0.016535945694153707
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 1.0
- Min = 0.95

#### facing_probas
- Mean = [9.50000000e-01 7.84166667e-01 4.37500000e-02 2.08333333e-04
 1.87500000e-03]
- Standard deviation = [0.02029299 0.06936217 0.0174553  0.0005512  0.00376732]
- Max = [0.97166667 0.87333333 0.06166667 0.00166667 0.01166667]
- 75% = [0.96666667 0.84208333 0.05875    0.         0.00166667]
- Median = [0.95833333 0.79083333 0.04833333 0.         0.        ]
- 25% = [0.92916667 0.735      0.03583333 0.         0.        ]
- Min = [0.92166667 0.66       0.01333333 0.         0.        ]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 79.875 | 0.125 |
| Actual Positive | 0.125 | 19.875 |

### robot-2
#### accuracy
- Mean = 0.9875
- Standard deviation = 0.008291561975888507
- Max = 1.0
- 75% = 0.99
- Median = 0.99
- 25% = 0.9875
- Min = 0.97

#### f1
- Mean = 0.9672602764708027
- Standard deviation = 0.0225178257643873
- Max = 1.0
- 75% = 0.9743589743589743
- Median = 0.9743589743589743
- 25% = 0.9676113360323887
- Min = 0.9189189189189189

#### precision
- Mean = 1.0
- Standard deviation = 0.0
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 1.0
- Min = 1.0

#### recall
- Mean = 0.9375
- Standard deviation = 0.041457809879442496
- Max = 1.0
- 75% = 0.95
- Median = 0.95
- 25% = 0.9375
- Min = 0.85

#### facing_probas
- Mean = [0.945      0.95541667 0.92208333 0.10479167 0.02791667]
- Standard deviation = [0.02066599 0.0113269  0.02619041 0.06054405 0.01549529]
- Max = [0.99333333 0.97       0.95       0.245      0.05666667]
- 75% = [0.94958333 0.965      0.94541667 0.12208333 0.03708333]
- Median = [0.93916667 0.95916667 0.92666667 0.08       0.02333333]
- 25% = [0.935      0.94166667 0.91083333 0.06708333 0.01958333]
- Min = [0.92       0.94166667 0.87166667 0.04333333 0.00333333]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 80.0 | 0.0 |
| Actual Positive | 1.25 | 18.75 |

### robot-3
#### accuracy
- Mean = 0.895
- Standard deviation = 0.023979157616563593
- Max = 0.94
- 75% = 0.9125000000000001
- Median = 0.885
- 25% = 0.8775
- Min = 0.87

#### f1
- Mean = 0.6354738332732672
- Standard deviation = 0.10592837792857251
- Max = 0.8235294117647058
- 75% = 0.719758064516129
- Median = 0.5960591133004927
- 25% = 0.5582010582010583
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
- Mean = 0.475
- Standard deviation = 0.11989578808281798
- Max = 0.7
- 75% = 0.5625
- Median = 0.42500000000000004
- 25% = 0.3875
- Min = 0.35

#### facing_probas
- Mean = [0.39645833 0.931875   0.95416667 0.74083333 0.30166667]
- Standard deviation = [0.08478501 0.03877855 0.02933286 0.05496211 0.08962112]
- Max = [0.51333333 0.995      0.99333333 0.81       0.445     ]
- 75% = [0.47375    0.95       0.97416667 0.79208333 0.36333333]
- Median = [0.3775     0.9325     0.95333333 0.7475     0.28166667]
- 25% = [0.34       0.91833333 0.9425     0.68833333 0.24583333]
- Min = [0.27833333 0.85166667 0.89333333 0.66333333 0.165     ]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 80.0 | 0.0 |
| Actual Positive | 10.5 | 9.5 |

### robot-4
#### accuracy
- Mean = 0.9612499999999999
- Standard deviation = 0.011659223816361029
- Max = 0.98
- 75% = 0.97
- Median = 0.96
- 25% = 0.9575
- Min = 0.94

#### f1
- Mean = 0.8928188939798847
- Standard deviation = 0.036539004648461736
- Max = 0.9473684210526316
- 75% = 0.9199584199584199
- Median = 0.8918128654970761
- 25% = 0.8809523809523809
- Min = 0.8235294117647058

#### precision
- Mean = 0.9864766081871346
- Standard deviation = 0.023434605412149787
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 0.9868421052631579
- Min = 0.9444444444444444

#### recall
- Mean = 0.8187500000000001
- Standard deviation = 0.06584783595532963
- Max = 0.9
- 75% = 0.8625
- Median = 0.825
- 25% = 0.7875000000000001
- Min = 0.7

#### facing_probas
- Mean = [0.005      0.21520833 0.83916667 0.96       0.9275    ]
- Standard deviation = [0.00448764 0.08185963 0.07961714 0.02494438 0.02897556]
- Max = [0.01333333 0.33333333 0.91666667 0.99166667 0.96333333]
- 75% = [0.00541667 0.27166667 0.90166667 0.97458333 0.945     ]
- Median = [0.00333333 0.21666667 0.87083333 0.96583333 0.9375    ]
- 25% = [0.00291667 0.16833333 0.79125    0.95208333 0.92041667]
- Min = [0.         0.08166667 0.68666667 0.91666667 0.87333333]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 79.75 | 0.25 |
| Actual Positive | 3.625 | 16.375 |

### robot-5
#### accuracy
- Mean = 0.97875
- Standard deviation = 0.009270248108869587
- Max = 0.99
- 75% = 0.9824999999999999
- Median = 0.98
- 25% = 0.9775
- Min = 0.96

#### f1
- Mean = 0.9493108753602231
- Standard deviation = 0.021521305874887802
- Max = 0.975609756097561
- 75% = 0.9578754578754578
- Median = 0.9523809523809523
- 25% = 0.946843853820598
- Min = 0.9047619047619048

#### precision
- Mean = 0.915243271221532
- Standard deviation = 0.041024496015326206
- Max = 1.0
- 75% = 0.9199134199134199
- Median = 0.9090909090909091
- 25% = 0.8992094861660078
- Min = 0.8636363636363636

#### recall
- Mean = 0.9875
- Standard deviation = 0.021650635094610987
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 0.9875
- Min = 0.95

#### facing_probas
- Mean = [0.013125   0.00395833 0.12666667 0.98208333 0.97458333]
- Standard deviation = [0.00940735 0.00617665 0.05134307 0.01366133 0.01613205]
- Max = [0.03166667 0.02       0.22166667 0.99833333 0.99      ]
- 75% = [0.02       0.00333333 0.16708333 0.99208333 0.98333333]
- Median = [0.01       0.00166667 0.10416667 0.98833333 0.9825    ]
- 25% = [0.00708333 0.00125    0.09333333 0.97041667 0.97333333]
- Min = [0.00166667 0.         0.06166667 0.96166667 0.94166667]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 78.125 | 1.875 |
| Actual Positive | 0.25 | 19.75 |

### robot-6
#### accuracy
- Mean = 0.8425
- Standard deviation = 0.03072051431861125
- Max = 0.9
- 75% = 0.86
- Median = 0.845
- 25% = 0.81
- Min = 0.81

#### f1
- Mean = 0.9142185834380646
- Standard deviation = 0.017978996399124206
- Max = 0.9473684210526316
- 75% = 0.924731182795699
- Median = 0.9159175039661555
- 25% = 0.8950276243093923
- Min = 0.8950276243093923

#### precision
- Mean = 1.0
- Standard deviation = 0.0
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 1.0
- Min = 1.0

#### recall
- Mean = 0.8425
- Standard deviation = 0.03072051431861125
- Max = 0.9
- 75% = 0.86
- Median = 0.845
- 25% = 0.81
- Min = 0.81

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
| Actual Positive | 15.75 | 84.25 |

