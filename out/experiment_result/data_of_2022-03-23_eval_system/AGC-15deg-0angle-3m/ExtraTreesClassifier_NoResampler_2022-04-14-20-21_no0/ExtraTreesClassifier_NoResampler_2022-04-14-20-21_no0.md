# ExtraTreesClassifier_NoResampler_2022-04-14-20-21_no0
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
	- n_estimators = 10
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
	- min_samples_split = 10
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
- gp_max_val_mean = 0.12730475400539484
- gp_auc_mean = 0.0912710660059176
- ac_std = 0.07224999700917309
- gp_max_val_max = 0.059759407096885174
- gp_auc_min = 0.046533389261381716
- ratio_max_to_10ms_ave_peaks = 0.04555652110027403
- gp_auc_max = 0.04480945516997224
- ratio_max_to_9th_ave_peaks = 0.04305548117271359
- tdoa_max = 0.03797212123171125
- srmr = 0.03699591907118945
- high_power = 0.0353558710868713
- gp_max_val_std = 0.0353057775834334
- coe3[2] = 0.03415914295011823
- coe3[3] = 0.03278589451736603
- coe1[0] = 0.031599107769845244
- gp_max_ix_mean = 0.030676193985083543
- tdoa_std = 0.02839506640721475
- gp_max_ix_max = 0.024064331333970367
- gp_max_ix_std = 0.020132011283021306
- gp_auc_std = 0.013939223144988048
- tdoa_mean = 0.013610474631751239
- coe1[1] = 0.012974531201581176
- tdoa_range = 0.012951270164250827
- gp_max_val_range = 0.011785787863350152
- ac_auc = 0.010479165963321393
- diff_std = 0.010191095275058291
- hlbr = 0.010191082802547767
- gp_max_val_min = 0.009994939097652712
- diff_auc = 0.004702388970409806
- low_power = 0.004021543985637357
- tdoa_min = 0.00398564790306457
- gp_max_ix_range = 0.003191340954849672
- coe3[0] = 0.0
- coe3[1] = 0.0
- gp_max_ix_min = 0.0
- gp_auc_range = 0.0

## Evaluation
cv = 8
### robot-1
#### accuracy
- Mean = 0.81625
- Standard deviation = 0.02117634293262174
- Max = 0.85
- 75% = 0.8325
- Median = 0.815
- 25% = 0.7975000000000001
- Min = 0.79

#### f1
- Mean = 0.2951522521683812
- Standard deviation = 0.14536068695801507
- Max = 0.5161290322580645
- 75% = 0.39444444444444443
- Median = 0.2985714285714286
- 25% = 0.16000000000000003
- Min = 0.09090909090909091

#### precision
- Mean = 0.5833198051948052
- Standard deviation = 0.12632237549585185
- Max = 0.7272727272727273
- 75% = 0.7035714285714285
- Median = 0.6125
- 25% = 0.475
- Min = 0.4

#### recall
- Mean = 0.20625
- Standard deviation = 0.1184205957593526
- Max = 0.4
- 75% = 0.275
- Median = 0.2
- 25% = 0.1
- Min = 0.05

#### facing_probas
- Mean = [0.3501059  0.14215625 0.11741865 0.13713839 0.08385938]
- Standard deviation = [0.03617594 0.07882447 0.02363997 0.04894495 0.03618966]
- Max = [0.42798214 0.3235     0.15623413 0.23572421 0.15372619]
- 75% = [0.36307391 0.17516567 0.14162054 0.16378869 0.10092262]
- Median = [0.33471528 0.11126786 0.10782937 0.12602877 0.0818125 ]
- 25% = [0.32344246 0.09490675 0.09568056 0.09950893 0.05725099]
- Min = [0.31851984 0.06663889 0.09293452 0.08269048 0.03236905]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 77.5 | 2.5 |
| Actual Positive | 15.875 | 4.125 |

### robot-2
#### accuracy
- Mean = 0.7475
- Standard deviation = 0.03561951712193755
- Max = 0.8
- 75% = 0.7775000000000001
- Median = 0.735
- 25% = 0.72
- Min = 0.7

#### f1
- Mean = 0.1941016482817295
- Standard deviation = 0.14316915480517423
- Max = 0.425531914893617
- 75% = 0.2892857142857143
- Median = 0.22532894736842102
- 25% = 0.06818181818181818
- Min = 0.0

#### precision
- Mean = 0.2747685185185185
- Standard deviation = 0.1812638942690167
- Max = 0.5
- 75% = 0.4027777777777778
- Median = 0.28888888888888886
- 25% = 0.1875
- Min = 0.0

#### recall
- Mean = 0.18125
- Standard deviation = 0.15995604865087157
- Max = 0.5
- 75% = 0.2625
- Median = 0.175
- 25% = 0.037500000000000006
- Min = 0.0

#### facing_probas
- Mean = [0.25824479 0.3684561  0.25269816 0.19035466 0.10344444]
- Standard deviation = [0.03169965 0.06806509 0.02987037 0.0314384  0.03002635]
- Max = [0.32208333 0.47795635 0.29972421 0.2618869  0.16696627]
- 75% = [0.26923264 0.41625446 0.26755357 0.19372569 0.11387946]
- Median = [0.261375   0.35371131 0.26262202 0.18248413 0.09326488]
- 25% = [0.23446329 0.31731796 0.23390774 0.17092361 0.08831746]
- Min = [0.21293254 0.27576984 0.1964623  0.15872222 0.06140278]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 71.125 | 8.875 |
| Actual Positive | 16.375 | 3.625 |

### robot-3
#### accuracy
- Mean = 0.8049999999999999
- Standard deviation = 0.01870828693386969
- Max = 0.82
- 75% = 0.82
- Median = 0.81
- 25% = 0.8
- Min = 0.76

#### f1
- Mean = 0.16356435231435232
- Standard deviation = 0.09457070736252227
- Max = 0.30769230769230765
- 75% = 0.2425
- Median = 0.16233766233766234
- 25% = 0.09415584415584416
- Min = 0.0

#### precision
- Mean = 0.5958333333333333
- Standard deviation = 0.3239030633452614
- Max = 1.0
- 75% = 0.8125
- Median = 0.6333333333333333
- 25% = 0.4375
- Min = 0.0

#### recall
- Mean = 0.1
- Standard deviation = 0.06123724356957946
- Max = 0.2
- 75% = 0.15
- Median = 0.1
- 25% = 0.05
- Min = 0.0

#### facing_probas
- Mean = [0.25789707 0.42300868 0.35759077 0.25346701 0.25594692]
- Standard deviation = [0.02125648 0.09342828 0.04485874 0.0466478  0.03896593]
- Max = [0.28759325 0.5381131  0.43868254 0.3363373  0.33168452]
- 75% = [0.27204514 0.50797321 0.38428621 0.2864251  0.26968502]
- Median = [0.26135417 0.43664087 0.35563393 0.24915972 0.25922817]
- 25% = [0.24440179 0.34174802 0.32300546 0.21978869 0.22444742]
- Min = [0.21772619 0.29372222 0.29576786 0.18858929 0.19806349]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 78.5 | 1.5 |
| Actual Positive | 18.0 | 2.0 |

### robot-4
#### accuracy
- Mean = 0.79125
- Standard deviation = 0.013635890143294655
- Max = 0.81
- 75% = 0.8
- Median = 0.795
- 25% = 0.785
- Min = 0.77

#### f1
- Mean = 0.02173913043478261
- Standard deviation = 0.05751633284923023
- Max = 0.1739130434782609
- 75% = 0.0
- Median = 0.0
- 25% = 0.0
- Min = 0.0

#### precision
- Mean = 0.08333333333333333
- Standard deviation = 0.2204792759220492
- Max = 0.6666666666666666
- 75% = 0.0
- Median = 0.0
- 25% = 0.0
- Min = 0.0

#### recall
- Mean = 0.0125
- Standard deviation = 0.033071891388307385
- Max = 0.1
- 75% = 0.0
- Median = 0.0
- 25% = 0.0
- Min = 0.0

#### facing_probas
- Mean = [0.22199231 0.3337557  0.27839335 0.21482763 0.23269643]
- Standard deviation = [0.02269639 0.05020201 0.03030344 0.04769749 0.03148687]
- Max = [0.24822222 0.41561508 0.31914286 0.29958135 0.26497421]
- 75% = [0.24740427 0.36215923 0.31372569 0.24707688 0.25792808]
- Median = [0.21986607 0.3315     0.26518254 0.203625   0.24116865]
- 25% = [0.20690724 0.28935863 0.25138046 0.18600992 0.22114236]
- Min = [0.18462302 0.27442262 0.24634524 0.14076389 0.16468849]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 78.875 | 1.125 |
| Actual Positive | 19.75 | 0.25 |

### robot-5
#### accuracy
- Mean = 0.77875
- Standard deviation = 0.016153559979150123
- Max = 0.79
- 75% = 0.79
- Median = 0.785
- 25% = 0.7775000000000001
- Min = 0.74

#### f1
- Mean = 0.010416666666666668
- Standard deviation = 0.027559909490256156
- Max = 0.08333333333333334
- 75% = 0.0
- Median = 0.0
- 25% = 0.0
- Min = 0.0

#### precision
- Mean = 0.03125
- Standard deviation = 0.08267972847076846
- Max = 0.25
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
- Mean = [0.0882815  0.1346756  0.14297718 0.15271999 0.19027207]
- Standard deviation = [0.0438479  0.02683046 0.03348921 0.02262884 0.03932964]
- Max = [0.18764286 0.178375   0.20007937 0.18103968 0.2414127 ]
- 75% = [0.0958621  0.14588145 0.16956845 0.16516518 0.22381101]
- Median = [0.07746528 0.12534425 0.12344246 0.15991865 0.19072718]
- 25% = [0.07004762 0.12123363 0.11761954 0.14515476 0.15260417]
- Min = [0.03148413 0.09928968 0.11126389 0.10495635 0.13885913]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 77.75 | 2.25 |
| Actual Positive | 19.875 | 0.125 |

### robot-6
#### accuracy
- Mean = 0.10125
- Standard deviation = 0.060298735475961686
- Max = 0.22
- 75% = 0.1275
- Median = 0.095
- 25% = 0.06
- Min = 0.01

#### f1
- Mean = 0.17854680476150153
- Standard deviation = 0.09763873596049429
- Max = 0.36065573770491804
- 75% = 0.2259316770186335
- Median = 0.17317317317317316
- 25% = 0.11320754716981131
- Min = 0.019801980198019802

#### precision
- Mean = 1.0
- Standard deviation = 0.0
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 1.0
- Min = 1.0

#### recall
- Mean = 0.10125
- Standard deviation = 0.060298735475961686
- Max = 0.22
- 75% = 0.1275
- Median = 0.095
- 25% = 0.06
- Min = 0.01

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
| Actual Positive | 89.875 | 10.125 |

