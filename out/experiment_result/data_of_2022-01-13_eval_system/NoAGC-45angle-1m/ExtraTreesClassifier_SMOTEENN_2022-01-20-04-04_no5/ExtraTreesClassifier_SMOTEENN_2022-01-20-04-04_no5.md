# ExtraTreesClassifier_SMOTEENN_2022-01-20-04-04_no5
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
- gp_max_ix_range = 0.09168075665495687
- gp_auc_max = 0.09077470355731228
- gp_auc_mean = 0.08665630665630666
- tdoa_min = 0.07842510068000264
- tdoa_mean = 0.07450980392156864
- gp_max_ix_std = 0.07194361919852117
- gp_max_val_mean = 0.06330610452349583
- gp_max_ix_min = 0.05994535192540009
- gp_max_val_max = 0.04454149336502279
- gp_auc_min = 0.041790123456790125
- tdoa_range = 0.03851851851851852
- hlbr = 0.03319404874960431
- tdoa_std = 0.025984787677254144
- srmr = 0.022049146435111352
- gp_max_val_min = 0.021367521367521368
- coe1[1] = 0.02121212121212122
- diff_std = 0.020607787274453948
- diff_auc = 0.019719416386083058
- gp_auc_std = 0.01849382716049383
- gp_max_val_range = 0.017598204264870933
- gp_auc_range = 0.01394500561167228
- ac_std = 0.0104320987654321
- gp_max_val_std = 0.00942760942760943
- low_power = 0.008641975308641978
- ratio_max_to_10ms_ave_peaks = 0.008592592592592596
- gp_max_ix_mean = 0.002592592592592593
- high_power = 0.002074074074074076
- tdoa_max = 0.0019753086419753096
- coe1[0] = 0.0
- coe3[0] = 0.0
- coe3[1] = 0.0
- coe3[2] = 0.0
- coe3[3] = 0.0
- ratio_max_to_9th_ave_peaks = 0.0
- ac_auc = 0.0
- gp_max_ix_max = 0.0

## Evaluation
cv = 8
### robot-1
#### accuracy
- Mean = 0.96375
- Standard deviation = 0.06122448448129227
- Max = 1.0
- 75% = 1.0
- Median = 0.99
- 25% = 0.97
- Min = 0.81

#### f1
- Mean = 0.851688043638508
- Standard deviation = 0.29139849172295446
- Max = 1.0
- 75% = 1.0
- Median = 0.9736842105263158
- 25% = 0.9164086687306502
- Min = 0.09523809523809523

#### precision
- Mean = 1.0
- Standard deviation = 0.0
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 1.0
- Min = 1.0

#### recall
- Mean = 0.81875
- Standard deviation = 0.3061224224064614
- Max = 1.0
- 75% = 1.0
- Median = 0.95
- 25% = 0.85
- Min = 0.05

#### facing_probas
- Mean = [0.95083333 0.75979167 0.25625    0.05708333 0.03645833]
- Standard deviation = [0.03497023 0.08734286 0.17399862 0.09813805 0.02629213]
- Max = [0.99166667 0.88333333 0.53166667 0.31166667 0.09      ]
- 75% = [0.9825     0.84666667 0.41666667 0.04125    0.04458333]
- Median = [0.9575     0.73416667 0.1525     0.015      0.03833333]
- 25% = [0.92041667 0.68208333 0.11375    0.00916667 0.01833333]
- Min = [0.895      0.665      0.09833333 0.         0.        ]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 80.0 | 0.0 |
| Actual Positive | 3.625 | 16.375 |

### robot-2
#### accuracy
- Mean = 0.94875
- Standard deviation = 0.06372548548265441
- Max = 1.0
- 75% = 0.99
- Median = 0.97
- 25% = 0.94
- Min = 0.79

#### f1
- Mean = 0.8930728262965105
- Standard deviation = 0.11118563257841066
- Max = 1.0
- 75% = 0.9743589743589743
- Median = 0.925
- 25% = 0.8571428571428572
- Min = 0.631578947368421

#### precision
- Mean = 0.8716062653562653
- Standard deviation = 0.16218516511776218
- Max = 1.0
- 75% = 1.0
- Median = 0.925
- 25% = 0.8181818181818182
- Min = 0.4864864864864865

#### recall
- Mean = 0.93125
- Standard deviation = 0.03479852726768762
- Max = 1.0
- 75% = 0.95
- Median = 0.925
- 25% = 0.9
- Min = 0.9

#### facing_probas
- Mean = [0.94416667 0.94708333 0.89208333 0.16708333 0.05708333]
- Standard deviation = [0.02824742 0.02834252 0.06774006 0.12382714 0.02999711]
- Max = [0.98       0.99666667 0.96166667 0.44833333 0.10333333]
- 75% = [0.95875    0.95791667 0.945      0.17916667 0.07958333]
- Median = [0.95333333 0.94833333 0.92416667 0.11666667 0.06      ]
- 25% = [0.94041667 0.93666667 0.84583333 0.07916667 0.03041667]
- Min = [0.88333333 0.89833333 0.77333333 0.07166667 0.01666667]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 76.25 | 3.75 |
| Actual Positive | 1.375 | 18.625 |

### robot-3
#### accuracy
- Mean = 0.83375
- Standard deviation = 0.03533323506275641
- Max = 0.88
- 75% = 0.8574999999999999
- Median = 0.84
- 25% = 0.8
- Min = 0.78

#### f1
- Mean = 0.29826803631151455
- Standard deviation = 0.21981287765786364
- Max = 0.6
- 75% = 0.4428571428571429
- Median = 0.33043478260869563
- 25% = 0.11538461538461536
- Min = 0.0

#### precision
- Mean = 0.6541666666666667
- Standard deviation = 0.43267177064272533
- Max = 1.0
- 75% = 1.0
- Median = 0.95
- 25% = 0.25
- Min = 0.0

#### recall
- Mean = 0.2
- Standard deviation = 0.15811388300841897
- Max = 0.45
- 75% = 0.2875
- Median = 0.2
- 25% = 0.07500000000000001
- Min = 0.0

#### facing_probas
- Mean = [0.61604167 0.92895833 0.90145833 0.69416667 0.388125  ]
- Standard deviation = [0.17057692 0.04268699 0.07001209 0.11688967 0.21716199]
- Max = [0.91833333 0.99       0.99166667 0.82666667 0.79      ]
- 75% = [0.72208333 0.96708333 0.94041667 0.80041667 0.45833333]
- Median = [0.61       0.9275     0.9125     0.72166667 0.27416667]
- 25% = [0.44541667 0.8975     0.86583333 0.59916667 0.23875   ]
- Min = [0.41666667 0.85833333 0.78333333 0.48833333 0.205     ]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 79.375 | 0.625 |
| Actual Positive | 16.0 | 4.0 |

### robot-4
#### accuracy
- Mean = 0.8925000000000001
- Standard deviation = 0.053326822519253844
- Max = 0.96
- 75% = 0.9225
- Median = 0.895
- 25% = 0.8775
- Min = 0.79

#### f1
- Mean = 0.5911043134346805
- Standard deviation = 0.2772005884430456
- Max = 0.888888888888889
- 75% = 0.7544802867383513
- Median = 0.6436781609195402
- 25% = 0.5488505747126438
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
- Mean = 0.46875
- Standard deviation = 0.25487435630129607
- Max = 0.8
- 75% = 0.6125
- Median = 0.475
- 25% = 0.3875
- Min = 0.0

#### facing_probas
- Mean = [0.08520833 0.455      0.81729167 0.95270833 0.85375   ]
- Standard deviation = [0.09621459 0.11039387 0.07952523 0.03167694 0.12221267]
- Max = [0.33166667 0.60166667 0.92833333 0.99166667 0.98833333]
- 75% = [0.07833333 0.54208333 0.88791667 0.97333333 0.94583333]
- Median = [0.06166667 0.455      0.80333333 0.96083333 0.8825    ]
- 25% = [0.02833333 0.34291667 0.76083333 0.94166667 0.80875   ]
- Min = [0.01       0.32833333 0.69833333 0.88833333 0.63166667]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 79.875 | 0.125 |
| Actual Positive | 10.625 | 9.375 |

### robot-5
#### accuracy
- Mean = 0.97
- Standard deviation = 0.03968626966596886
- Max = 1.0
- 75% = 0.9924999999999999
- Median = 0.98
- 25% = 0.97
- Min = 0.87

#### f1
- Mean = 0.9066600087587041
- Standard deviation = 0.14956917502290623
- Max = 1.0
- 75% = 0.9817073170731707
- Median = 0.9529211571185479
- 25% = 0.9284436493738819
- Min = 0.5185185185185185

#### precision
- Mean = 0.9489075950746431
- Standard deviation = 0.05055717653642961
- Max = 1.0
- 75% = 1.0
- Median = 0.9523809523809523
- 25% = 0.9279176201372997
- Min = 0.8695652173913043

#### recall
- Mean = 0.90625
- Standard deviation = 0.21277555663186504
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 0.975
- Min = 0.35

#### facing_probas
- Mean = [0.10854167 0.21229167 0.11291667 0.975      0.91604167]
- Standard deviation = [0.10810051 0.16389135 0.05991748 0.01840894 0.09878054]
- Max = [0.38166667 0.525      0.20166667 0.99833333 0.99666667]
- 75% = [0.10416667 0.28041667 0.15208333 0.98708333 0.98125   ]
- Median = [0.07916667 0.24916667 0.1075     0.97833333 0.9525    ]
- 25% = [0.06416667 0.035      0.08458333 0.96208333 0.91208333]
- Min = [0.01166667 0.02       0.02       0.94166667 0.70333333]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 78.875 | 1.125 |
| Actual Positive | 1.875 | 18.125 |

### robot-6
#### accuracy
- Mean = 0.665
- Standard deviation = 0.13152946437965904
- Max = 0.8
- 75% = 0.78
- Median = 0.71
- 25% = 0.5875
- Min = 0.45

#### f1
- Mean = 0.7907836710232914
- Standard deviation = 0.10159323283615132
- Max = 0.888888888888889
- 75% = 0.8764044943820225
- Median = 0.8303693570451436
- 25% = 0.7372888478023364
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
- Mean = 0.665
- Standard deviation = 0.13152946437965904
- Max = 0.8
- 75% = 0.78
- Median = 0.71
- 25% = 0.5875
- Min = 0.45

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
| Actual Positive | 33.5 | 66.5 |

