# ExtraTreesClassifier_NoResampler_2022-01-20-05-31_no0
## Constants
- CSV_PATH = ../out/csv/experiment
- OUTPUT_PATH = ../out/experiment_result/data_of_2022-01-13_eval_system/NoAGC-45angle-3m
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
- DISTANCE = [3]
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
- gp_auc_mean = 0.14294327428970469
- gp_max_val_mean = 0.14181453118168072
- gp_max_val_min = 0.1390451591307897
- gp_auc_max = 0.12850242719064417
- gp_auc_min = 0.10289792305883443
- gp_max_val_max = 0.08806318047091324
- srmr = 0.05828563682690081
- diff_auc = 0.016255547342647187
- hlbr = 0.01625307456645688
- high_power = 0.014476627633557632
- gp_max_ix_mean = 0.010392535335641474
- coe1[1] = 0.009923867943169736
- coe1[0] = 0.009034655575021706
- low_power = 0.008863769443227951
- tdoa_mean = 0.008812565462475818
- tdoa_std = 0.00876624293130305
- gp_max_ix_max = 0.008012812911204058
- ratio_max_to_10ms_ave_peaks = 0.007950030405271662
- coe3[3] = 0.007910160448152513
- ac_std = 0.007766555317429895
- coe3[2] = 0.006629203295288357
- ac_auc = 0.006462387522736543
- gp_max_val_std = 0.006178721456327099
- diff_std = 0.00575904165340264
- gp_max_ix_std = 0.005646309938474363
- tdoa_max = 0.005528836063867882
- gp_auc_range = 0.004509849757983769
- gp_max_ix_range = 0.004469598459114385
- gp_max_ix_min = 0.004215326366408247
- gp_auc_std = 0.0034741457032809488
- gp_max_val_range = 0.0033143233787286683
- ratio_max_to_9th_ave_peaks = 0.0032840244493630324
- tdoa_range = 0.0028562401573156053
- tdoa_min = 0.00170141433268127
- coe3[0] = 0.0
- coe3[1] = 0.0

## Evaluation
cv = 8
### robot-1
#### accuracy
- Mean = 0.985
- Standard deviation = 0.013228756555322964
- Max = 1.0
- 75% = 1.0
- Median = 0.98
- 25% = 0.98
- Min = 0.96

#### f1
- Mean = 0.9648268398268398
- Standard deviation = 0.0304908757293957
- Max = 1.0
- 75% = 1.0
- Median = 0.9523809523809523
- 25% = 0.9523809523809523
- Min = 0.9090909090909091

#### precision
- Mean = 0.9337121212121212
- Standard deviation = 0.056660133718377234
- Max = 1.0
- 75% = 1.0
- Median = 0.9090909090909091
- 25% = 0.9090909090909091
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
- Mean = [9.68083333e-01 7.62500000e-01 5.48333333e-02 7.91666667e-04
 1.41666667e-03]
- Standard deviation = [0.01376666 0.07356535 0.02685558 0.00101294 0.00102402]
- Max = [0.993      0.89333333 0.11133333 0.00333333 0.004     ]
- 75% = [9.75916667e-01 8.07333333e-01 7.23333333e-02 7.50000000e-04
 1.41666667e-03]
- Median = [9.63833333e-01 7.52000000e-01 4.28333333e-02 5.00000000e-04
 1.00000000e-03]
- 25% = [9.56833333e-01 7.05166667e-01 3.65833333e-02 2.50000000e-04
 9.16666667e-04]
- Min = [9.52333333e-01 6.63333333e-01 2.66666667e-02 0.00000000e+00
 6.66666667e-04]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 78.5 | 1.5 |
| Actual Positive | 0.0 | 20.0 |

### robot-2
#### accuracy
- Mean = 0.98375
- Standard deviation = 0.012183492931011215
- Max = 1.0
- 75% = 0.9924999999999999
- Median = 0.98
- 25% = 0.98
- Min = 0.96

#### f1
- Mean = 0.9565901934322987
- Standard deviation = 0.033556264631734105
- Max = 1.0
- 75% = 0.9807692307692307
- Median = 0.9473684210526316
- 25% = 0.9473684210526316
- Min = 0.888888888888889

#### precision
- Mean = 1.0
- Standard deviation = 0.0
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 1.0
- Min = 1.0

#### recall
- Mean = 0.91875
- Standard deviation = 0.06091746465505601
- Max = 1.0
- 75% = 0.9624999999999999
- Median = 0.9
- 25% = 0.9
- Min = 0.8

#### facing_probas
- Mean = [0.96416667 0.95445833 0.84195833 0.09508333 0.001125  ]
- Standard deviation = [0.01834848 0.02078323 0.06997905 0.07471664 0.00125762]
- Max = [0.99166667 0.99366667 0.955      0.231      0.00433333]
- 75% = [0.98091667 0.96358333 0.8925     0.15108333 0.00108333]
- Median = [9.56333333e-01 9.45333333e-01 8.33833333e-01 4.90000000e-02
 6.66666667e-04]
- 25% = [9.52333333e-01 9.41083333e-01 7.97583333e-01 4.28333333e-02
 3.33333333e-04]
- Min = [9.40000000e-01 9.30666667e-01 7.46666667e-01 2.66666667e-02
 3.33333333e-04]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 80.0 | 0.0 |
| Actual Positive | 1.625 | 18.375 |

### robot-3
#### accuracy
- Mean = 0.9874999999999999
- Standard deviation = 0.016393596310755015
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 0.97
- Min = 0.96

#### f1
- Mean = 0.9658408408408408
- Standard deviation = 0.04494326589603446
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 0.9189189189189189
- Min = 0.888888888888889

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
- Standard deviation = 0.08196798155377501
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 0.85
- Min = 0.8

#### facing_probas
- Mean = [0.18616667 0.90191667 0.95416667 0.87758333 0.09379167]
- Standard deviation = [0.09082064 0.03646374 0.02289408 0.0637366  0.05979199]
- Max = [0.34566667 0.97233333 0.994      0.968      0.212     ]
- 75% = [0.22583333 0.91708333 0.97175    0.94916667 0.12041667]
- Median = [0.14133333 0.89383333 0.9455     0.83833333 0.08966667]
- 25% = [0.12208333 0.87975    0.93825    0.83241667 0.04641667]
- Min = [0.10466667 0.84733333 0.92233333 0.81233333 0.01633333]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 80.0 | 0.0 |
| Actual Positive | 1.25 | 18.75 |

### robot-4
#### accuracy
- Mean = 0.9524999999999999
- Standard deviation = 0.02727178028658927
- Max = 0.99
- 75% = 0.97
- Median = 0.96
- 25% = 0.9425
- Min = 0.9

#### f1
- Mean = 0.8633806671490495
- Standard deviation = 0.08693348270183185
- Max = 0.9743589743589743
- 75% = 0.9189189189189189
- Median = 0.888888888888889
- 25% = 0.839825119236884
- Min = 0.6874999999999999

#### precision
- Mean = 0.9733018207282913
- Standard deviation = 0.035007768176922825
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 0.9380252100840336
- Min = 0.9166666666666666

#### recall
- Mean = 0.78125
- Standard deviation = 0.11709371246996995
- Max = 0.95
- 75% = 0.85
- Median = 0.8
- 25% = 0.7625000000000001
- Min = 0.55

#### facing_probas
- Mean = [0.004375   0.23795833 0.91895833 0.96575    0.798375  ]
- Standard deviation = [0.00198912 0.10635873 0.03716945 0.02515714 0.05578118]
- Max = [0.00833333 0.43333333 0.98133333 0.99866667 0.894     ]
- 75% = [0.00508333 0.31883333 0.94525    0.99683333 0.82258333]
- Median = [0.004      0.21283333 0.904      0.95333333 0.79066667]
- 25% = [0.00325    0.17091667 0.89366667 0.9425     0.746     ]
- Min = [0.002      0.08966667 0.872      0.942      0.738     ]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 79.625 | 0.375 |
| Actual Positive | 4.375 | 15.625 |

### robot-5
#### accuracy
- Mean = 0.99625
- Standard deviation = 0.0048412291827592754
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 0.99
- Min = 0.99

#### f1
- Mean = 0.9903846153846154
- Standard deviation = 0.012413408160921218
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 0.9743589743589743
- Min = 0.9743589743589743

#### precision
- Mean = 1.0
- Standard deviation = 0.0
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 1.0
- Min = 1.0

#### recall
- Mean = 0.98125
- Standard deviation = 0.024206145913796377
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 0.95
- Min = 0.95

#### facing_probas
- Mean = [0.00345833 0.00516667 0.12670833 0.92783333 0.93816667]
- Standard deviation = [0.0020065  0.0029392  0.04402475 0.03042523 0.01856969]
- Max = [0.00666667 0.01033333 0.18066667 0.97833333 0.97033333]
- 75% = [0.00466667 0.007      0.15691667 0.94841667 0.94766667]
- Median = [0.0025     0.00433333 0.144      0.9155     0.93966667]
- 25% = [0.00225    0.00266667 0.08083333 0.90725    0.928     ]
- Min = [0.001      0.00166667 0.058      0.89333333 0.90833333]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 80.0 | 0.0 |
| Actual Positive | 0.375 | 19.625 |

### robot-6
#### accuracy
- Mean = 0.9237500000000001
- Standard deviation = 0.024968730444297704
- Max = 0.95
- 75% = 0.94
- Median = 0.935
- 25% = 0.915
- Min = 0.87

#### f1
- Mean = 0.9601861346201184
- Standard deviation = 0.013694989281795343
- Max = 0.9743589743589743
- 75% = 0.9690721649484536
- Median = 0.9664013674483201
- 25% = 0.955592105263158
- Min = 0.9304812834224598

#### precision
- Mean = 1.0
- Standard deviation = 0.0
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 1.0
- Min = 1.0

#### recall
- Mean = 0.9237500000000001
- Standard deviation = 0.024968730444297704
- Max = 0.95
- 75% = 0.94
- Median = 0.935
- 25% = 0.915
- Min = 0.87

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
| Actual Positive | 7.625 | 92.375 |

