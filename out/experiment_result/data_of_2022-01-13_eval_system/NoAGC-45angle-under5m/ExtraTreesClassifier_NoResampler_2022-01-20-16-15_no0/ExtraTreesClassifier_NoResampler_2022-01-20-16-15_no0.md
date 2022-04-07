# ExtraTreesClassifier_NoResampler_2022-01-20-16-15_no0
## Constants
- CSV_PATH = ../out/csv/experiment
- OUTPUT_PATH = ../out/experiment_result/data_of_2022-01-13_eval_system/NoAGC-45angle-under5m
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
- DISTANCE = [1, 3, 5]
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
- gp_auc_min = 0.09350626797254079
- gp_max_val_mean = 0.08795005513022207
- gp_max_val_min = 0.08116268056668957
- gp_max_val_max = 0.07770174477303683
- gp_auc_max = 0.07120316024889452
- gp_auc_mean = 0.06669616871291884
- diff_std = 0.05157514955141624
- diff_auc = 0.0472081902469192
- hlbr = 0.0340919743935075
- srmr = 0.031336798135092235
- high_power = 0.03069772379660282
- gp_max_ix_range = 0.02235827843818607
- gp_max_ix_min = 0.019414318583283977
- tdoa_range = 0.018985743175100652
- coe1[1] = 0.01885199542172009
- gp_max_val_std = 0.01818546962425849
- tdoa_std = 0.0173309756876403
- gp_max_ix_mean = 0.016876514280562013
- gp_auc_std = 0.015012060193334578
- tdoa_max = 0.01482101786309893
- gp_max_ix_std = 0.014642341407761246
- gp_max_ix_max = 0.01427350785649051
- coe3[3] = 0.013682143804027946
- tdoa_min = 0.01361637930611854
- gp_max_val_range = 0.013481457816474444
- gp_auc_range = 0.013339890695996717
- low_power = 0.013167067344636971
- coe1[0] = 0.01203922317903944
- ratio_max_to_10ms_ave_peaks = 0.011718335497983224
- tdoa_mean = 0.011668304979226857
- coe3[2] = 0.010632934152541892
- ac_std = 0.009246766261303501
- ac_auc = 0.008844679561094866
- ratio_max_to_9th_ave_peaks = 0.004680681342278153
- coe3[0] = 0.0
- coe3[1] = 0.0

## Evaluation
cv = 8
### robot-1
#### accuracy
- Mean = 0.9729166666666667
- Standard deviation = 0.00888780375320896
- Max = 0.9933333333333333
- 75% = 0.9750000000000001
- Median = 0.9683333333333333
- 25% = 0.9666666666666667
- Min = 0.9666666666666667

#### f1
- Mean = 0.9323448662599243
- Standard deviation = 0.02221209748765567
- Max = 0.9833333333333333
- 75% = 0.9368574604056682
- Median = 0.9212012673922028
- 25% = 0.9166666666666666
- Min = 0.9166666666666666

#### precision
- Mean = 0.9315652828315202
- Standard deviation = 0.023568965922116037
- Max = 0.9833333333333333
- 75% = 0.9386818687430478
- Median = 0.9244350282485876
- 25% = 0.9166666666666666
- Min = 0.9032258064516129

#### recall
- Mean = 0.9333333333333333
- Standard deviation = 0.025000000000000005
- Max = 0.9833333333333333
- 75% = 0.9416666666666667
- Median = 0.9166666666666666
- 25% = 0.9166666666666666
- Min = 0.9166666666666666

#### facing_probas
- Mean = [0.92121667 0.76816667 0.06604167 0.00428333 0.00208333]
- Standard deviation = [0.02794906 0.0329106  0.01807865 0.00556794 0.00230814]
- Max = [0.97046667 0.84126667 0.09346667 0.01673333 0.00746667]
- 75% = [0.92565    0.76946667 0.08065    0.00508333 0.00225   ]
- Median = [0.91106667 0.76386667 0.0612     0.00116667 0.00093333]
- 25% = [9.08600000e-01 7.60083333e-01 4.89333333e-02 8.83333333e-04
 7.50000000e-04]
- Min = [8.83333333e-01 7.12666667e-01 4.76000000e-02 2.66666667e-04
 4.00000000e-04]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 235.875 | 4.125 |
| Actual Positive | 4.0 | 56.0 |

### robot-2
#### accuracy
- Mean = 0.9591666666666667
- Standard deviation = 0.011395661942647796
- Max = 0.9766666666666667
- 75% = 0.9641666666666666
- Median = 0.9583333333333333
- 25% = 0.95
- Min = 0.9433333333333334

#### f1
- Mean = 0.8891968216808663
- Standard deviation = 0.03351418122956316
- Max = 0.9401709401709402
- 75% = 0.9044254658385094
- Median = 0.8867955439056356
- 25% = 0.8648648648648648
- Min = 0.838095238095238

#### precision
- Mean = 0.9636912426607251
- Standard deviation = 0.015018468117196362
- Max = 0.9818181818181818
- 75% = 0.9782312925170068
- Median = 0.963225371120108
- 25% = 0.956447963800905
- Min = 0.9411764705882353

#### recall
- Mean = 0.8270833333333334
- Standard deviation = 0.05523780659817855
- Max = 0.9166666666666666
- 75% = 0.8500000000000001
- Median = 0.8166666666666667
- 25% = 0.8
- Min = 0.7333333333333333

#### facing_probas
- Mean = [0.89795833 0.92605833 0.81113333 0.148275   0.020425  ]
- Standard deviation = [0.02500471 0.0152359  0.0315214  0.04019037 0.00647954]
- Max = [0.94026667 0.95633333 0.86793333 0.22926667 0.03333333]
- 75% = [0.90925    0.93305    0.82528333 0.17578333 0.02215   ]
- Median = [0.89553333 0.92386667 0.797      0.13226667 0.01733333]
- 25% = [0.8868     0.9134     0.78851667 0.11626667 0.01646667]
- Min = [0.8552     0.90873333 0.779      0.10553333 0.01413333]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 238.125 | 1.875 |
| Actual Positive | 10.375 | 49.625 |

### robot-3
#### accuracy
- Mean = 0.94375
- Standard deviation = 0.006548430685625712
- Max = 0.9533333333333334
- 75% = 0.95
- Median = 0.9433333333333334
- 25% = 0.9391666666666666
- Min = 0.9333333333333333

#### f1
- Mean = 0.8366984559025177
- Standard deviation = 0.02233736407919698
- Max = 0.8679245283018869
- 75% = 0.8578104138851802
- Median = 0.8349514563106796
- 25% = 0.8231626047220107
- Min = 0.8

#### precision
- Mean = 0.9944995164410058
- Standard deviation = 0.00953401736572969
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 0.9946808510638298
- Min = 0.9772727272727273

#### recall
- Mean = 0.7229166666666667
- Standard deviation = 0.034295995069071536
- Max = 0.7666666666666667
- 75% = 0.7541666666666667
- Median = 0.7166666666666667
- 25% = 0.7083333333333334
- Min = 0.6666666666666666

#### facing_probas
- Mean = [0.22298333 0.86645833 0.89215833 0.75305833 0.14846667]
- Standard deviation = [0.03692438 0.02254485 0.03130997 0.03991326 0.03256421]
- Max = [0.25906667 0.8934     0.9462     0.8248     0.21573333]
- 75% = [0.25163333 0.8815     0.89943333 0.77581667 0.1648    ]
- Median = [0.24376667 0.87073333 0.88316667 0.73176667 0.1433    ]
- 25% = [0.18528333 0.85695    0.87596667 0.72233333 0.1264    ]
- Min = [0.15986667 0.82593333 0.84766667 0.71726667 0.10193333]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 239.75 | 0.25 |
| Actual Positive | 16.625 | 43.375 |

### robot-4
#### accuracy
- Mean = 0.93375
- Standard deviation = 0.017355554666382094
- Max = 0.96
- 75% = 0.9425
- Median = 0.9316666666666666
- 25% = 0.9216666666666666
- Min = 0.91

#### f1
- Mean = 0.803570465968079
- Standard deviation = 0.05898347994484587
- Max = 0.8928571428571429
- 75% = 0.8338727076591155
- Median = 0.8001713632901752
- 25% = 0.7626262626262625
- Min = 0.7157894736842105

#### precision
- Mean = 0.9705757904885812
- Standard deviation = 0.021926718351426146
- Max = 1.0
- 75% = 0.9825581395348837
- Median = 0.9728937728937729
- 25% = 0.9583333333333334
- Min = 0.9318181818181818

#### recall
- Mean = 0.6895833333333333
- Standard deviation = 0.08413675210961948
- Max = 0.8333333333333334
- 75% = 0.725
- Median = 0.6833333333333333
- 25% = 0.6291666666666667
- Min = 0.5666666666666667

#### facing_probas
- Mean = [0.00721667 0.26315833 0.82415833 0.91124167 0.74265   ]
- Standard deviation = [0.00536126 0.03745003 0.04592491 0.03393895 0.04539431]
- Max = [0.01793333 0.31793333 0.901      0.9734     0.82093333]
- 75% = [0.00908333 0.29126667 0.83541667 0.9249     0.75525   ]
- Median = [0.00483333 0.26606667 0.81183333 0.89223333 0.74513333]
- 25% = [0.0037     0.24075    0.79755    0.88715    0.73536667]
- Min = [0.00153333 0.18913333 0.76673333 0.8832     0.647     ]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 238.75 | 1.25 |
| Actual Positive | 18.625 | 41.375 |

### robot-5
#### accuracy
- Mean = 0.9829166666666667
- Standard deviation = 0.009195031871130795
- Max = 1.0
- 75% = 0.9883333333333333
- Median = 0.98
- 25% = 0.9766666666666667
- Min = 0.97

#### f1
- Mean = 0.9556399766218585
- Standard deviation = 0.02403015177634436
- Max = 1.0
- 75% = 0.9699006428988896
- Median = 0.9482758620689654
- 25% = 0.9391304347826087
- Min = 0.9217391304347826

#### precision
- Mean = 0.9864448051948052
- Standard deviation = 0.011996247990344424
- Max = 1.0
- 75% = 1.0
- Median = 0.9821428571428571
- 25% = 0.9818181818181818
- Min = 0.9636363636363636

#### recall
- Mean = 0.9270833333333333
- Standard deviation = 0.036264364969852525
- Max = 1.0
- 75% = 0.9416666666666667
- Median = 0.9166666666666666
- 25% = 0.9
- Min = 0.8833333333333333

#### facing_probas
- Mean = [0.00655833 0.00749167 0.14024167 0.89179167 0.87695   ]
- Standard deviation = [0.00193073 0.00432216 0.04195791 0.03563407 0.03474582]
- Max = [0.0094     0.01506667 0.22473333 0.95753333 0.93206667]
- 75% = [0.00786667 0.00898333 0.15923333 0.90928333 0.88991667]
- Median = [0.00646667 0.0059     0.13156667 0.87696667 0.8754    ]
- 25% = [0.00508333 0.00448333 0.1106     0.869      0.84738333]
- Min = [0.00366667 0.00293333 0.09033333 0.84693333 0.8374    ]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 239.25 | 0.75 |
| Actual Positive | 4.375 | 55.625 |

### robot-6
#### accuracy
- Mean = 0.8200000000000001
- Standard deviation = 0.03872983346207418
- Max = 0.89
- 75% = 0.8300000000000001
- Median = 0.8049999999999999
- 25% = 0.7941666666666667
- Min = 0.7833333333333333

#### f1
- Mean = 0.9006110940960386
- Standard deviation = 0.022924684954237644
- Max = 0.9417989417989417
- 75% = 0.9068366708385481
- Median = 0.8919658142976994
- 25% = 0.8852698474233656
- Min = 0.8785046728971964

#### precision
- Mean = 1.0
- Standard deviation = 0.0
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 1.0
- Min = 1.0

#### recall
- Mean = 0.8200000000000001
- Standard deviation = 0.03872983346207418
- Max = 0.89
- 75% = 0.8300000000000001
- Median = 0.8049999999999999
- 25% = 0.7941666666666667
- Min = 0.7833333333333333

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
| Actual Positive | 54.0 | 246.0 |

