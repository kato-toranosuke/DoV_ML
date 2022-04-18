# ExtraTreesClassifier_ClusterCentroids_2022-04-14-21-03_no1
## Constants
- CSV_PATH = ../out/csv/experiment
- OUTPUT_PATH = ../out/experiment_result/data_of_2022-03-23_eval_system/AGC-15deg-0angle-3m
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
- DISTANCE = [3]
- AGC_STATUS = ['AGC-15deg']
- ANGLES = [60, 75, 90, 105, 120]

## Loaded CSV
- 2022-03-23_raspi_48000Hz_w1_N2^12_overlap80_all.csv

## Estimator
### Type
- resampler = ClusterCentroids
- estimator = ExtraTreesClassifier

### Arguments for hyperparameter search
- resampler = ClusterCentroids
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
	- estimator = None
	- voting = auto
	- n_jobs = deprecated
	- n_features_in_ = 36
	- sampling_strategy_ = OrderedDict([(0, 15)])
	- estimator_ = KMeans(n_clusters=15, random_state=42)
	- voting_ = soft

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
	- oob_decision_function_ = [[0.55319149 0.44680851]
 [0.54545455 0.45454545]
 [0.29166667 0.70833333]
 [0.51020408 0.48979592]
 [0.51111111 0.48888889]
 [0.47916667 0.52083333]
 [0.36956522 0.63043478]
 [0.46808511 0.53191489]
 [0.37209302 0.62790698]
 [0.48888889 0.51111111]
 [0.38       0.62      ]
 [0.38636364 0.61363636]
 [0.19047619 0.80952381]
 [0.36363636 0.63636364]
 [0.33333333 0.66666667]
 [0.25       0.75      ]
 [0.44444444 0.55555556]
 [0.27659574 0.72340426]
 [0.37777778 0.62222222]
 [0.3255814  0.6744186 ]
 [0.27906977 0.72093023]
 [0.40425532 0.59574468]
 [0.36170213 0.63829787]
 [0.27906977 0.72093023]
 [0.55       0.45      ]
 [0.46511628 0.53488372]
 [0.5        0.5       ]
 [0.30434783 0.69565217]
 [0.42222222 0.57777778]
 [0.46666667 0.53333333]]
	- oob_score_ = 0.5666666666666667

#### Importance of features
- gp_auc_max = 0.1
- gp_max_val_max = 0.09375
- tdoa_max = 0.075
- gp_auc_min = 0.05625
- coe1[1] = 0.05
- ratio_max_to_9th_ave_peaks = 0.05
- gp_max_ix_std = 0.05
- tdoa_range = 0.05
- ratio_max_to_10ms_ave_peaks = 0.04375
- gp_max_ix_mean = 0.04375
- coe3[2] = 0.03125
- gp_max_val_std = 0.03125
- gp_max_ix_max = 0.03125
- ac_std = 0.025
- ac_auc = 0.025
- diff_std = 0.025
- diff_auc = 0.025
- srmr = 0.025
- gp_max_val_mean = 0.025
- gp_max_ix_range = 0.025
- gp_auc_std = 0.025
- gp_auc_mean = 0.025
- tdoa_std = 0.025
- high_power = 0.01875
- gp_max_val_min = 0.01875
- coe3[3] = 0.0062499999999999995
- low_power = 0.0
- hlbr = 0.0
- coe1[0] = 0.0
- coe3[0] = 0.0
- coe3[1] = 0.0
- gp_max_val_range = 0.0
- gp_max_ix_min = 0.0
- gp_auc_range = 0.0
- tdoa_min = 0.0
- tdoa_mean = 0.0

## Evaluation
cv = 8
### robot-1
#### accuracy
- Mean = 0.84125
- Standard deviation = 0.060917464655056035
- Max = 0.91
- 75% = 0.88
- Median = 0.855
- 25% = 0.8175
- Min = 0.74

#### f1
- Mean = 0.6558779683208935
- Standard deviation = 0.12411973729179233
- Max = 0.8085106382978724
- 75% = 0.7232558139534884
- Median = 0.6747967479674797
- 25% = 0.6224489795918366
- Min = 0.4347826086956522

#### precision
- Mean = 0.5854762392918316
- Standard deviation = 0.1190218975318938
- Max = 0.72
- 75% = 0.6759259259259259
- Median = 0.6118012422360248
- 25% = 0.5320197044334976
- Min = 0.38461538461538464

#### recall
- Mean = 0.75
- Standard deviation = 0.13919410907075055
- Max = 0.95
- 75% = 0.8250000000000001
- Median = 0.775
- 25% = 0.6749999999999999
- Min = 0.5

#### facing_probas
- Mean = [0.624625 0.46025  0.539875 0.45     0.502125]
- Standard deviation = [0.03689152 0.03888043 0.02919519 0.05244283 0.0474722 ]
- Max = [0.661 0.545 0.573 0.543 0.596]
- 75% = [0.6565  0.471   0.5595  0.48525 0.53575]
- Median = [0.6385 0.4595 0.5485 0.4315 0.4805]
- 25% = [0.59575 0.4395  0.531   0.4155  0.471  ]
- Min = [0.556 0.404 0.479 0.377 0.445]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 69.125 | 10.875 |
| Actual Positive | 5.0 | 15.0 |

### robot-2
#### accuracy
- Mean = 0.6575
- Standard deviation = 0.044370598373247125
- Max = 0.73
- 75% = 0.675
- Median = 0.665
- 25% = 0.6425000000000001
- Min = 0.59

#### f1
- Mean = 0.39722998800934745
- Standard deviation = 0.07884960565842053
- Max = 0.5263157894736842
- 75% = 0.43121349772874756
- Median = 0.38510781671159033
- 25% = 0.3555102040816327
- Min = 0.2807017543859649

#### precision
- Mean = 0.3068294234792768
- Standard deviation = 0.05364967544937784
- Max = 0.40540540540540543
- 75% = 0.3231841526045488
- Median = 0.3042929292929293
- 25% = 0.28095238095238095
- Min = 0.21621621621621623

#### recall
- Mean = 0.575
- Standard deviation = 0.1600781059358212
- Max = 0.85
- 75% = 0.7124999999999999
- Median = 0.525
- 25% = 0.4375
- Min = 0.4

#### facing_probas
- Mean = [0.589375 0.656625 0.60575  0.509625 0.551625]
- Standard deviation = [0.0398307  0.03726908 0.04193671 0.03234168 0.02323218]
- Max = [0.644 0.702 0.664 0.56  0.581]
- 75% = [0.62775 0.67875 0.64375 0.5305  0.568  ]
- Median = [0.5865 0.6655 0.6035 0.5145 0.5555]
- 25% = [0.56025 0.64275 0.5695  0.48175 0.5355 ]
- Min = [0.524 0.586 0.548 0.457 0.515]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 54.25 | 25.75 |
| Actual Positive | 8.5 | 11.5 |

### robot-3
#### accuracy
- Mean = 0.7024999999999999
- Standard deviation = 0.06832825184358225
- Max = 0.78
- 75% = 0.7575000000000001
- Median = 0.72
- 25% = 0.6475
- Min = 0.58

#### f1
- Mean = 0.13610613210674571
- Standard deviation = 0.06918825375871161
- Max = 0.2173913043478261
- 75% = 0.19873271889400917
- Median = 0.13782051282051283
- 25% = 0.06919642857142858
- Min = 0.05405405405405405

#### precision
- Mean = 0.18918022847250787
- Standard deviation = 0.09913239733280008
- Max = 0.375
- 75% = 0.2556818181818182
- Median = 0.17427884615384615
- 25% = 0.11458333333333333
- Min = 0.058823529411764705

#### recall
- Mean = 0.125
- Standard deviation = 0.08291561975888499
- Max = 0.25
- 75% = 0.175
- Median = 0.1
- 25% = 0.05
- Min = 0.05

#### facing_probas
- Mean = [0.58925  0.67075  0.64275  0.55575  0.620375]
- Standard deviation = [0.0381764  0.04351652 0.05280092 0.03701267 0.03489963]
- Max = [0.637 0.721 0.712 0.631 0.678]
- 75% = [0.6195 0.7045 0.69   0.567  0.6385]
- Median = [0.5995 0.687  0.65   0.5485 0.625 ]
- 25% = [0.5575  0.6325  0.5945  0.53    0.59575]
- Min = [0.528 0.597 0.556 0.512 0.57 ]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 67.75 | 12.25 |
| Actual Positive | 17.5 | 2.5 |

### robot-4
#### accuracy
- Mean = 0.7875
- Standard deviation = 0.008291561975888507
- Max = 0.8
- 75% = 0.79
- Median = 0.79
- 25% = 0.7875000000000001
- Min = 0.77

#### f1
- Mean = 0.010000000000000002
- Standard deviation = 0.02645751311064591
- Max = 0.08000000000000002
- 75% = 0.0
- Median = 0.0
- 25% = 0.0
- Min = 0.0

#### precision
- Mean = 0.025
- Standard deviation = 0.06614378277661477
- Max = 0.2
- 75% = 0.0
- Median = 0.0
- 25% = 0.0
- Min = 0.0

#### recall
- Mean = 0.00625
- Standard deviation = 0.016535945694153693
- Max = 0.05
- 75% = 0.0
- Median = 0.0
- 25% = 0.0
- Min = 0.0

#### facing_probas
- Mean = [0.593875 0.642625 0.6175   0.523875 0.60175 ]
- Standard deviation = [0.02321873 0.03340635 0.04889018 0.03561403 0.0213234 ]
- Max = [0.626 0.685 0.671 0.576 0.637]
- 75% = [0.615   0.6745  0.65175 0.5505  0.6135 ]
- Median = [0.592  0.639  0.6385 0.528  0.6055]
- 25% = [0.57775 0.622   0.5805  0.49475 0.58475]
- Min = [0.558 0.584 0.535 0.464 0.567]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 78.625 | 1.375 |
| Actual Positive | 19.875 | 0.125 |

### robot-5
#### accuracy
- Mean = 0.8
- Standard deviation = 0.07778174593052023
- Max = 0.89
- 75% = 0.8525
- Median = 0.825
- 25% = 0.775
- Min = 0.65

#### f1
- Mean = 0.46841134811381047
- Standard deviation = 0.19394554079363904
- Max = 0.7441860465116279
- 75% = 0.5952380952380953
- Median = 0.4768270944741533
- 25% = 0.3887362637362638
- Min = 0.10256410256410256

#### precision
- Mean = 0.5161267895195956
- Standard deviation = 0.18864341220828748
- Max = 0.6956521739130435
- 75% = 0.6488095238095238
- Median = 0.5874125874125874
- 25% = 0.4609375
- Min = 0.10526315789473684

#### recall
- Mean = 0.45625
- Standard deviation = 0.2214123697989794
- Max = 0.8
- 75% = 0.5875
- Median = 0.475
- 25% = 0.3125
- Min = 0.1

#### facing_probas
- Mean = [0.54325  0.57725  0.56325  0.499125 0.59875 ]
- Standard deviation = [0.03869028 0.02155661 0.04293818 0.0303539  0.02608999]
- Max = [0.595 0.604 0.619 0.551 0.65 ]
- 75% = [0.5745  0.5955  0.59975 0.519   0.61225]
- Median = [0.5445 0.581  0.562  0.497  0.596 ]
- 25% = [0.51875 0.562   0.5425  0.4755  0.58425]
- Min = [0.481 0.54  0.478 0.456 0.556]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 70.875 | 9.125 |
| Actual Positive | 10.875 | 9.125 |

### robot-6
#### accuracy
- Mean = 0.3825
- Standard deviation = 0.07693341276714558
- Max = 0.49
- 75% = 0.4275
- Median = 0.405
- 25% = 0.33
- Min = 0.23

#### f1
- Mean = 0.5486763587142328
- Standard deviation = 0.0840607321691389
- Max = 0.6577181208053691
- 75% = 0.5988343856240894
- Median = 0.5764944275582573
- 25% = 0.49624060150375937
- Min = 0.3739837398373984

#### precision
- Mean = 1.0
- Standard deviation = 0.0
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 1.0
- Min = 1.0

#### recall
- Mean = 0.3825
- Standard deviation = 0.07693341276714558
- Max = 0.49
- 75% = 0.4275
- Median = 0.405
- 25% = 0.33
- Min = 0.23

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
| Actual Positive | 61.75 | 38.25 |

