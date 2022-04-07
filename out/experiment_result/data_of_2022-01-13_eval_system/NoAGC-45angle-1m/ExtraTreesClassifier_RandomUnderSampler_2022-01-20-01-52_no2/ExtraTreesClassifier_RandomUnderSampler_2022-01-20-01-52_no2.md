# ExtraTreesClassifier_RandomUnderSampler_2022-01-20-01-52_no2
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
	- sampling_strategy_ = OrderedDict([(1, 36)])
	- sample_indices_ = [ 2  3  4  8  9 10 14 15 16 20 21 22 29 30 31 32 33 34 41 42 43 44 45 46
 53 54 55 56 57 58 65 66 67 68 69 70 63 72  7 25 60 50 12 51 48 27 35 17
 28 24 37 18 62  0 49 11 23  1 73 39  5 59 71  6 64 47 61 19 40 36 38 13]

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
- gp_max_val_mean = 0.104255532559241
- gp_auc_max = 0.08671424210279138
- gp_auc_mean = 0.07568286511458146
- gp_max_ix_std = 0.06894661482806667
- gp_max_ix_range = 0.06644843806518524
- gp_max_val_max = 0.060144347837610246
- srmr = 0.05328575790204358
- gp_auc_min = 0.04940352896601739
- gp_max_ix_min = 0.048477749710821735
- gp_max_val_min = 0.04843456487877999
- tdoa_min = 0.04624737407295547
- tdoa_mean = 0.03960551535671687
- hlbr = 0.03300166296951033
- gp_max_ix_mean = 0.029623208113647815
- tdoa_std = 0.02829081460423564
- tdoa_range = 0.0259559643402289
- diff_std = 0.01388922668828583
- tdoa_max = 0.01205573942332241
- high_power = 0.011735409652076319
- gp_max_val_std = 0.01117629016179741
- ratio_max_to_10ms_ave_peaks = 0.009179031703381088
- ratio_max_to_9th_ave_peaks = 0.008548348052881046
- diff_auc = 0.008529165647643786
- coe1[1] = 0.007526755651755652
- gp_auc_std = 0.007490835840509043
- coe3[3] = 0.006849995872502722
- gp_auc_range = 0.006515473502715105
- low_power = 0.006165824915824916
- coe3[2] = 0.005758686538256427
- gp_max_ix_max = 0.005685329696294609
- coe1[0] = 0.004616769547325103
- ac_std = 0.00418100358422939
- gp_max_val_range = 0.0030555555555555557
- ac_auc = 0.0025223765432098753
- coe3[0] = 0.0
- coe3[1] = 0.0

## Evaluation
cv = 8
### robot-1
#### accuracy
- Mean = 0.995
- Standard deviation = 0.0050000000000000044
- Max = 1.0
- 75% = 1.0
- Median = 0.995
- 25% = 0.99
- Min = 0.99

#### f1
- Mean = 0.9876485303314572
- Standard deviation = 0.012357405497320516
- Max = 1.0
- 75% = 1.0
- Median = 0.9878048780487805
- 25% = 0.975609756097561
- Min = 0.9743589743589743

#### precision
- Mean = 0.9821428571428572
- Standard deviation = 0.023053472298853697
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 0.9523809523809523
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
- Mean = [9.34166667e-01 7.46041667e-01 4.87500000e-02 8.33333333e-04
 8.33333333e-04]
- Standard deviation = [0.01852176 0.1017518  0.01786815 0.00220479 0.00117851]
- Max = [0.96166667 0.89       0.07833333 0.00666667 0.00333333]
- 75% = [0.94291667 0.82666667 0.05625    0.         0.00166667]
- Median = [0.93666667 0.73416667 0.05       0.         0.        ]
- 25% = [0.93       0.68125    0.03583333 0.         0.        ]
- Min = [0.89333333 0.60833333 0.02       0.         0.        ]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 79.625 | 0.375 |
| Actual Positive | 0.125 | 19.875 |

### robot-2
#### accuracy
- Mean = 0.98125
- Standard deviation = 0.007806247497998005
- Max = 0.99
- 75% = 0.99
- Median = 0.98
- 25% = 0.9775
- Min = 0.97

#### f1
- Mean = 0.9516952440492235
- Standard deviation = 0.02022948003813297
- Max = 0.9743589743589743
- 75% = 0.9743589743589743
- Median = 0.9486842105263158
- 25% = 0.9422336328626444
- Min = 0.9189189189189189

#### precision
- Mean = 0.981845238095238
- Standard deviation = 0.03341693385476843
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 0.9875
- Min = 0.9047619047619048

#### recall
- Mean = 0.925
- Standard deviation = 0.035355339059327355
- Max = 0.95
- 75% = 0.95
- Median = 0.95
- 25% = 0.9
- Min = 0.85

#### facing_probas
- Mean = [0.93604167 0.9525     0.89791667 0.08895833 0.03041667]
- Standard deviation = [0.00816231 0.02124591 0.00832291 0.05503747 0.01180719]
- Max = [0.945      0.98166667 0.90666667 0.205      0.04666667]
- 75% = [0.94166667 0.96416667 0.90416667 0.10666667 0.03708333]
- Median = [0.94       0.9525     0.9        0.08333333 0.03083333]
- 25% = [0.93166667 0.94791667 0.89458333 0.05291667 0.02916667]
- Min = [0.92       0.905      0.88166667 0.00833333 0.00333333]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 79.625 | 0.375 |
| Actual Positive | 1.5 | 18.5 |

### robot-3
#### accuracy
- Mean = 0.915
- Standard deviation = 0.019364916731037084
- Max = 0.94
- 75% = 0.93
- Median = 0.92
- 25% = 0.905
- Min = 0.88

#### f1
- Mean = 0.7251353291847632
- Standard deviation = 0.0818267954203809
- Max = 0.8235294117647058
- 75% = 0.787878787878788
- Median = 0.7499999999999999
- 25% = 0.6874304783092325
- Min = 0.5714285714285715

#### precision
- Mean = 1.0
- Standard deviation = 0.0
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 1.0
- Min = 1.0

#### recall
- Mean = 0.575
- Standard deviation = 0.09682458365518541
- Max = 0.7
- 75% = 0.65
- Median = 0.6
- 25% = 0.525
- Min = 0.4

#### facing_probas
- Mean = [0.36666667 0.9075     0.93229167 0.72270833 0.23208333]
- Standard deviation = [0.03316625 0.05357368 0.02266816 0.10593151 0.0477097 ]
- Max = [0.415      0.985      0.97333333 0.83666667 0.30166667]
- 75% = [0.39625    0.94333333 0.94875    0.78       0.26791667]
- Median = [0.36       0.90583333 0.93       0.76       0.23333333]
- 25% = [0.34291667 0.88       0.91541667 0.7125     0.18416667]
- Min = [0.315      0.82666667 0.89833333 0.48166667 0.17333333]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 80.0 | 0.0 |
| Actual Positive | 8.5 | 11.5 |

### robot-4
#### accuracy
- Mean = 0.95875
- Standard deviation = 0.02027159342528356
- Max = 0.99
- 75% = 0.965
- Median = 0.96
- 25% = 0.955
- Min = 0.92

#### f1
- Mean = 0.8862126564525945
- Standard deviation = 0.05853277979511257
- Max = 0.9743589743589743
- 75% = 0.9118421052631579
- Median = 0.888888888888889
- 25% = 0.8725490196078431
- Min = 0.7777777777777777

#### precision
- Mean = 0.971875
- Standard deviation = 0.04911323014219284
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 0.975
- Min = 0.875

#### recall
- Mean = 0.8187500000000001
- Standard deviation = 0.08637671850678284
- Max = 0.95
- 75% = 0.9
- Median = 0.8
- 25% = 0.775
- Min = 0.7

#### facing_probas
- Mean = [0.009375   0.21208333 0.79541667 0.94979167 0.92354167]
- Standard deviation = [0.00749711 0.08784752 0.06182834 0.02258376 0.02197596]
- Max = [0.025      0.40333333 0.87166667 0.98       0.95      ]
- 75% = [0.01291667 0.2375     0.84333333 0.96625    0.9475    ]
- Median = [0.00583333 0.19333333 0.8075     0.955      0.92083333]
- 25% = [0.00333333 0.18041667 0.745      0.935      0.90708333]
- Min = [0.00333333 0.06833333 0.70333333 0.90666667 0.88833333]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 79.5 | 0.5 |
| Actual Positive | 3.625 | 16.375 |

### robot-5
#### accuracy
- Mean = 0.975
- Standard deviation = 0.011180339887498959
- Max = 0.99
- 75% = 0.98
- Median = 0.98
- 25% = 0.97
- Min = 0.95

#### f1
- Mean = 0.941184379932626
- Standard deviation = 0.023911664980517056
- Max = 0.975609756097561
- 75% = 0.9523809523809523
- Median = 0.949874686716792
- 25% = 0.9302325581395349
- Min = 0.888888888888889

#### precision
- Mean = 0.902348014304536
- Standard deviation = 0.05567780602730745
- Max = 1.0
- 75% = 0.9199134199134199
- Median = 0.9090909090909091
- 25% = 0.8695652173913043
- Min = 0.8

#### recall
- Mean = 0.9875
- Standard deviation = 0.03307189138830738
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 1.0
- Min = 0.9

#### facing_probas
- Mean = [0.01854167 0.01       0.099375   0.97583333 0.96395833]
- Standard deviation = [0.00906908 0.01142609 0.05583916 0.01017213 0.01617907]
- Max = [0.03       0.03333333 0.21666667 0.985      0.98833333]
- 75% = [0.02708333 0.01125    0.1275     0.9825     0.97291667]
- Median = [0.02       0.005      0.08       0.98083333 0.96916667]
- 25% = [0.00958333 0.00291667 0.07291667 0.97       0.95333333]
- Min = [0.005      0.         0.01666667 0.95333333 0.93666667]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 77.75 | 2.25 |
| Actual Positive | 0.25 | 19.75 |

### robot-6
#### accuracy
- Mean = 0.86
- Standard deviation = 0.016583123951777013
- Max = 0.89
- 75% = 0.8725
- Median = 0.85
- 25% = 0.85
- Min = 0.84

#### f1
- Mean = 0.9246461989904879
- Standard deviation = 0.00953216768421997
- Max = 0.9417989417989417
- 75% = 0.9319035157583342
- Median = 0.9189189189189189
- 25% = 0.9189189189189189
- Min = 0.9130434782608696

#### precision
- Mean = 1.0
- Standard deviation = 0.0
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 1.0
- Min = 1.0

#### recall
- Mean = 0.86
- Standard deviation = 0.016583123951777013
- Max = 0.89
- 75% = 0.8725
- Median = 0.85
- 25% = 0.85
- Min = 0.84

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
| Actual Positive | 14.0 | 86.0 |

