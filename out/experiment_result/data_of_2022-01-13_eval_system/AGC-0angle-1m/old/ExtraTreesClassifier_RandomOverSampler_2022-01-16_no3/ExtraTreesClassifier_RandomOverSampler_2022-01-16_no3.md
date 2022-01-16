# ExtraTreesClassifier_RandomOverSampler_2022-01-16_no3
## Constants
- CSV_PATH = ../out/csv/experiment
- OUTPUT_PATH = ../out/experiment_result/data_of_2022-01-13_eval_system/AGC-0angle-1m
- FEATURE_ATTRBS = ['low_power', 'high_power', 'hlbr', 'coe1[0]', 'coe1[1]', 'coe3[0]', 'coe3[1]', 'coe3[2]', 'coe3[3]', 'ratio_max_to_10ms_ave_peaks', 'ratio_max_to_9th_ave_peaks', 'ac_std', 'ac_auc', 'diff_std', 'diff_auc', 'srmr', 'gp_max_val_std', 'gp_max_val_range', 'gp_max_val_min', 'gp_max_val_max', 'gp_max_val_mean', 'gp_max_ix_std', 'gp_max_ix_range', 'gp_max_ix_min', 'gp_max_ix_max', 'gp_max_ix_mean', 'gp_auc_std', 'gp_auc_range', 'gp_auc_min', 'gp_auc_max', 'gp_auc_mean', 'tdoa_std', 'tdoa_range', 'tdoa_min', 'tdoa_max', 'tdoa_mean']
- LABEL_ATTRB = ['facing']
- FACING_DOV_ANGLES = [1]
- NCV = 8
- SCORING = ['accuracy', 'balanced_accuracy', 'f1']
- REFIT_SCORING = balanced_accuracy
- PARAM_GRID = [{'est__n_estimators': range(50, 1001, 50), 'est__min_samples_split': [2, 5, 10], 'est__min_samples_leaf': [1, 5, 10], 'est__max_features': ['sqrt', 'log2', None], 'est__bootstrap': [False], 'est__n_jobs': [-1], 'est__random_state': [42], 'est__max_samples': [0.01, 0.5, 0.09]}, {'est__n_estimators': range(50, 1001, 50), 'est__min_samples_split': [2, 5, 10], 'est__min_samples_leaf': [1, 5, 10], 'est__max_features': ['sqrt', 'log2', None], 'est__bootstrap': [True], 'est__oob_score': [True, False], 'est__n_jobs': [-1], 'est__random_state': [42], 'est__max_samples': [0.01, 0.5, 0.09]}]
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
	- {'est__n_estimators': range(50, 1001, 50), 'est__min_samples_split': [2, 5, 10], 'est__min_samples_leaf': [1, 5, 10], 'est__max_features': ['sqrt', 'log2', None], 'est__bootstrap': [False], 'est__n_jobs': [-1], 'est__random_state': [42], 'est__max_samples': [0.01, 0.5, 0.09]}
	- {'est__n_estimators': range(50, 1001, 50), 'est__min_samples_split': [2, 5, 10], 'est__min_samples_leaf': [1, 5, 10], 'est__max_features': ['sqrt', 'log2', None], 'est__bootstrap': [True], 'est__oob_score': [True, False], 'est__n_jobs': [-1], 'est__random_state': [42], 'est__max_samples': [0.01, 0.5, 0.09]}

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
	- sampling_strategy_ = OrderedDict([(1, 45)])
	- shrinkage_ = None
	- sample_indices_ = [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23
 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47
 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71
 72 73 74 36 18 72 74 55 37 72 19 36 54  2 36 55 55 37 19 18 37 37  2 20
 19  1 37 56 73 20  1 56 19  0 56 54 20 72 56 38  0 55 55 74 54 56 56 74]

- best_estimator
	- base_estimator = ExtraTreeClassifier()
	- n_estimators = 50
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
	- min_samples_leaf = 5
	- min_weight_fraction_leaf = 0.0
	- max_features = None
	- max_leaf_nodes = None
	- min_impurity_decrease = 0.0
	- ccp_alpha = 0.0
	- n_features_in_ = 36
	- n_outputs_ = 1
	- classes_ = [0 1]
	- n_classes_ = 2
	- base_estimator_ = ExtraTreeClassifier()

#### Importance of features
- gp_max_val_min = 0.1867083181719326
- gp_max_val_mean = 0.18669736347244942
- gp_auc_min = 0.15681004452848002
- gp_auc_mean = 0.11875979949794661
- gp_max_val_max = 0.08015936223889655
- gp_auc_range = 0.04538815387606117
- gp_auc_max = 0.04406765768671158
- gp_auc_std = 0.02823507913367597
- gp_max_ix_range = 0.018678915832670263
- tdoa_max = 0.018317742331405075
- gp_max_val_range = 0.015248702570631427
- gp_max_ix_max = 0.014916606119958778
- gp_max_ix_std = 0.013067780296686744
- gp_max_val_std = 0.012647625214334317
- tdoa_mean = 0.01152677371888951
- tdoa_min = 0.011331369182228079
- gp_max_ix_min = 0.007657247037374658
- tdoa_range = 0.0071764978957335
- tdoa_std = 0.00481055841191996
- diff_auc = 0.0031811869939225635
- ratio_max_to_9th_ave_peaks = 0.0026450439388517625
- coe1[1] = 0.002251373944819604
- ac_std = 0.0020088238621452066
- high_power = 0.0015731207251814638
- srmr = 0.0014911592721131679
- ac_auc = 0.0011048733466890973
- low_power = 0.0009202309414398494
- coe3[2] = 0.0008708613507305385
- hlbr = 0.0007137758743754462
- diff_std = 0.0005467130018476231
- gp_max_ix_mean = 0.0002913968547641074
- ratio_max_to_10ms_ave_peaks = 0.0001334120425029517
- coe3[3] = 6.243063263041069e-05
- coe1[0] = 0.0
- coe3[0] = 0.0
- coe3[1] = 0.0

## Evaluation
cv = 8
### robot-1
#### accuracy
- Mean = 0.750929691653376
- Standard deviation = 0.1424372684219532

#### f1
- Mean = 0.750929691653376
- Standard deviation = 0.14243726842195323

#### precision
- Mean = 0.750929691653376
- Standard deviation = 0.1424372684219532

#### recall
- Mean = 0.750929691653376
- Standard deviation = 0.1424372684219532

#### facing_probas
- Mean = -100.0
- Standard deviation = 0.0

#### Confusion Matrix|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 0 | 0 |
| Actual Positive | 9 | 24 |

### robot-2
#### accuracy
- Mean = 0.750929691653376
- Standard deviation = 0.1424372684219532

#### f1
- Mean = 0.750929691653376
- Standard deviation = 0.14243726842195323

#### precision
- Mean = 0.750929691653376
- Standard deviation = 0.1424372684219532

#### recall
- Mean = 0.750929691653376
- Standard deviation = 0.1424372684219532

#### facing_probas
- Mean = -100.0
- Standard deviation = 0.0

#### Confusion Matrix|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 0 | 0 |
| Actual Positive | 9 | 24 |

### robot-3
#### accuracy
- Mean = 0.750929691653376
- Standard deviation = 0.1424372684219532

#### f1
- Mean = 0.750929691653376
- Standard deviation = 0.14243726842195323

#### precision
- Mean = 0.750929691653376
- Standard deviation = 0.1424372684219532

#### recall
- Mean = 0.750929691653376
- Standard deviation = 0.1424372684219532

#### facing_probas
- Mean = -100.0
- Standard deviation = 0.0

#### Confusion Matrix|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 0 | 0 |
| Actual Positive | 9 | 24 |

### robot-4
#### accuracy
- Mean = 0.750929691653376
- Standard deviation = 0.1424372684219532

#### f1
- Mean = 0.750929691653376
- Standard deviation = 0.14243726842195323

#### precision
- Mean = 0.750929691653376
- Standard deviation = 0.1424372684219532

#### recall
- Mean = 0.750929691653376
- Standard deviation = 0.1424372684219532

#### facing_probas
- Mean = -100.0
- Standard deviation = 0.0

#### Confusion Matrix|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 0 | 0 |
| Actual Positive | 9 | 24 |

### robot-5
#### accuracy
- Mean = 0.750929691653376
- Standard deviation = 0.1424372684219532

#### f1
- Mean = 0.750929691653376
- Standard deviation = 0.14243726842195323

#### precision
- Mean = 0.750929691653376
- Standard deviation = 0.1424372684219532

#### recall
- Mean = 0.750929691653376
- Standard deviation = 0.1424372684219532

#### facing_probas
- Mean = -100.0
- Standard deviation = 0.0

#### Confusion Matrix|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 0 | 0 |
| Actual Positive | 9 | 24 |

