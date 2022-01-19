# ExtraTreesClassifier_RandomOverSampler_2022-01-18-16-32_no3
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
	- sampling_strategy_ = OrderedDict([(0, 2)])
	- shrinkage_ = None
	- sample_indices_ = [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23
 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47
 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 59 29]

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
- gp_auc_max = 0.12513395658518475
- high_power = 0.12015336934487321
- tdoa_mean = 0.078962922124513
- gp_max_val_mean = 0.06916279560811002
- gp_max_ix_std = 0.06503772954127564
- gp_max_ix_range = 0.06275237171357732
- gp_auc_mean = 0.058715816524538146
- gp_max_val_max = 0.05343533167744436
- diff_auc = 0.050263670284820705
- gp_auc_min = 0.041934911099772786
- tdoa_min = 0.03948841592468803
- gp_max_ix_mean = 0.035591313187363485
- diff_std = 0.0302221819195293
- srmr = 0.027677939775349707
- gp_max_ix_min = 0.024227473871089797
- coe1[1] = 0.01570487731725224
- hlbr = 0.012118907732942828
- gp_max_val_std = 0.011235302763080542
- coe3[2] = 0.009182066885503387
- tdoa_range = 0.008192641363373067
- ac_auc = 0.008041422374755709
- gp_max_val_range = 0.007100342996503956
- ac_std = 0.006803124782619076
- ratio_max_to_10ms_ave_peaks = 0.0067506434022601945
- gp_max_val_min = 0.0065424066107819395
- tdoa_std = 0.006277702651942001
- gp_auc_range = 0.004475308641975308
- ratio_max_to_9th_ave_peaks = 0.004295473045473046
- gp_max_ix_max = 0.003376925714888678
- coe3[3] = 0.0030519244734931016
- gp_auc_std = 0.0028021498141111378
- tdoa_max = 0.0010416666666666667
- low_power = 0.00024691358024691434
- coe1[0] = 0.0
- coe3[0] = 0.0
- coe3[1] = 0.0

## Evaluation
cv = 8
### robot-1
#### accuracy
- Mean = 1.0
- Standard deviation = 0.0
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 1.0
- Min = 1.0

#### f1
- Mean = 1.0
- Standard deviation = 0.0
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 1.0
- Min = 1.0

#### precision
- Mean = 1.0
- Standard deviation = 0.0
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 1.0
- Min = 1.0

#### recall
- Mean = 1.0
- Standard deviation = 0.0
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 1.0
- Min = 1.0

#### facing_probas
- Mean = [0.95604167 0.75729167 0.05145833 0.         0.001875  ]
- Standard deviation = [0.01554424 0.06342065 0.02468464 0.         0.00347985]
- Max = [0.97333333 0.865      0.09166667 0.         0.01      ]
- 75% = [0.96416667 0.785      0.06791667 0.         0.00125   ]
- Median = [0.95833333 0.75166667 0.0525     0.         0.        ]
- 25% = [0.95291667 0.72       0.03291667 0.         0.        ]
- Min = [0.92       0.65666667 0.015      0.         0.        ]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 79.125 | 0.0 |
| Actual Positive | 0.0 | 20.0 |

### robot-2
#### accuracy
- Mean = 0.9987373737373737
- Standard deviation = 0.0033405950897280033
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 1.0
- Min = 0.98989898989899

#### f1
- Mean = 0.9969512195121951
- Standard deviation = 0.008066314972757905
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 1.0
- Min = 0.975609756097561

#### precision
- Mean = 0.9940476190476191
- Standard deviation = 0.01574851970871782
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 1.0
- Min = 0.9523809523809523

#### recall
- Mean = 1.0
- Standard deviation = 0.0
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 1.0
- Min = 1.0

#### facing_probas
- Mean = [0.97166667 0.97333333 0.956875   0.03208333 0.00666667]
- Standard deviation = [0.01263813 0.01452966 0.02031757 0.01433115 0.00634648]
- Max = [0.99       0.99666667 0.98166667 0.05666667 0.02166667]
- 75% = [0.98125    0.98708333 0.975      0.04125    0.0075    ]
- Median = [0.97333333 0.96916667 0.95833333 0.02916667 0.005     ]
- 25% = [0.96125    0.96166667 0.94416667 0.02083333 0.00291667]
- Min = [0.95333333 0.95333333 0.92       0.01333333 0.        ]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 79.0 | 0.125 |
| Actual Positive | 0.0 | 20.0 |

### robot-3
#### accuracy
- Mean = 0.9028787878787878
- Standard deviation = 0.023183028510909857
- Max = 0.9292929292929293
- 75% = 0.9193939393939394
- Median = 0.904040404040404
- 25% = 0.898989898989899
- Min = 0.8484848484848485

#### f1
- Mean = 0.6746945259042033
- Standard deviation = 0.11237589320225859
- Max = 0.787878787878788
- 75% = 0.7499999999999999
- Median = 0.6881720430107527
- 25% = 0.6666666666666666
- Min = 0.4

#### precision
- Mean = 1.0
- Standard deviation = 0.0
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 1.0
- Min = 1.0

#### recall
- Mean = 0.51875
- Standard deviation = 0.11439378261076953
- Max = 0.65
- 75% = 0.6
- Median = 0.525
- 25% = 0.5
- Min = 0.25

#### facing_probas
- Mean = [0.45645833 0.935625   0.96354167 0.885625   0.13625   ]
- Standard deviation = [0.07197336 0.01794934 0.01836054 0.01916553 0.06018923]
- Max = [0.57833333 0.97166667 0.98666667 0.93       0.25333333]
- 75% = [0.49583333 0.94166667 0.97583333 0.88875    0.16166667]
- Median = [0.44       0.92916667 0.96416667 0.88333333 0.135     ]
- 25% = [0.3925     0.92375    0.95625    0.87125    0.07833333]
- Min = [0.38       0.91666667 0.925      0.865      0.07      ]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 79.125 | 0.0 |
| Actual Positive | 9.625 | 10.375 |

### robot-4
#### accuracy
- Mean = 0.9697474747474748
- Standard deviation = 0.016720680763271146
- Max = 1.0
- 75% = 0.9797979797979798
- Median = 0.9698989898989898
- 25% = 0.9570707070707071
- Min = 0.9494949494949495

#### f1
- Mean = 0.9126931075460487
- Standard deviation = 0.050472149794495665
- Max = 1.0
- 75% = 0.9444444444444444
- Median = 0.9166666666666667
- 25% = 0.873885918003565
- Min = 0.8484848484848484

#### precision
- Mean = 1.0
- Standard deviation = 0.0
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 1.0
- Min = 1.0

#### recall
- Mean = 0.843421052631579
- Standard deviation = 0.08655254756680886
- Max = 1.0
- 75% = 0.8947368421052632
- Median = 0.8473684210526315
- 25% = 0.7763157894736842
- Min = 0.7368421052631579

#### facing_probas
- Mean = [0.         0.016875   0.93657895 0.98077851 0.77778509]
- Standard deviation = [0.         0.01836604 0.03376031 0.00776965 0.06931706]
- Max = [0.         0.05087719 0.97333333 0.98947368 0.8877193 ]
- 75% = [0.         0.02412281 0.96929825 0.98655702 0.81710526]
- Median = [0.         0.00789474 0.94561404 0.98421053 0.80149123]
- 25% = [0.         0.00436404 0.9004386  0.97412281 0.72675439]
- Min = [0.         0.         0.88947368 0.96842105 0.66491228]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 80.0 | 0.0 |
| Actual Positive | 3.0 | 16.125 |

### robot-5
#### accuracy
- Mean = 1.0
- Standard deviation = 0.0
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 1.0
- Min = 1.0

#### f1
- Mean = 1.0
- Standard deviation = 0.0
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 1.0
- Min = 1.0

#### precision
- Mean = 1.0
- Standard deviation = 0.0
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 1.0
- Min = 1.0

#### recall
- Mean = 1.0
- Standard deviation = 0.0
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 1.0
- Min = 1.0

#### facing_probas
- Mean = [0.0125     0.         0.03083333 0.9725     0.98125   ]
- Standard deviation = [0.01130388 0.         0.02129489 0.01346291 0.00780625]
- Max = [0.03333333 0.         0.06333333 0.98666667 0.99333333]
- 75% = [0.02125    0.         0.04875    0.98291667 0.98458333]
- Median = [0.0075     0.         0.02416667 0.97166667 0.98166667]
- 25% = [0.00333333 0.         0.01541667 0.97       0.97916667]
- Min = [0.         0.         0.00166667 0.94166667 0.965     ]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 79.125 | 0.0 |
| Actual Positive | 0.0 | 20.0 |

### robot-6
#### accuracy
- Mean = 0.8726262626262626
- Standard deviation = 0.010124719648686237
- Max = 0.88
- 75% = 0.8787878787878788
- Median = 0.8787878787878788
- 25% = 0.8686868686868687
- Min = 0.8484848484848485

#### f1
- Mean = 0.9319497428727037
- Standard deviation = 0.0058235641186820475
- Max = 0.9361702127659575
- 75% = 0.9354838709677419
- Median = 0.9354838709677419
- 25% = 0.9297297297297298
- Min = 0.9180327868852458

#### precision
- Mean = 1.0
- Standard deviation = 0.0
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 1.0
- Min = 1.0

#### recall
- Mean = 0.8726262626262626
- Standard deviation = 0.010124719648686237
- Max = 0.88
- 75% = 0.8787878787878788
- Median = 0.8787878787878788
- 25% = 0.8686868686868687
- Min = 0.8484848484848485

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
| Actual Positive | 12.625 | 86.5 |

