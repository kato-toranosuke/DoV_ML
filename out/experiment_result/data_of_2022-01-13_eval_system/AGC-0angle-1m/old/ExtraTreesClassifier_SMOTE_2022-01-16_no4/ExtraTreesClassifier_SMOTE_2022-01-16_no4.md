# ExtraTreesClassifier_SMOTE_2022-01-16_no4
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
- resampler = SMOTE
- estimator = ExtraTreesClassifier

### Arguments for hyperparameter search
- resampler = SMOTE
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
	- k_neighbors = 5
	- n_jobs = -1
	- n_features_in_ = 36
	- sampling_strategy_ = OrderedDict([(1, 45)])
	- nn_k_ = NearestNeighbors(n_neighbors=6)

- best_estimator
	- base_estimator = ExtraTreeClassifier()
	- n_estimators = 200
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
- gp_max_val_min = 0.20891661257496819
- gp_auc_min = 0.1677378697488061
- gp_auc_mean = 0.12473729316139956
- gp_max_val_mean = 0.11694380625141114
- gp_max_val_max = 0.07380544270287841
- gp_auc_max = 0.05781248301603838
- gp_max_val_range = 0.044039002694533425
- gp_auc_range = 0.02675038122104264
- tdoa_mean = 0.02133847907668563
- hlbr = 0.016681590616166486
- gp_max_ix_range = 0.014276385908495748
- gp_max_ix_mean = 0.013246290782636954
- gp_max_ix_max = 0.011682294225136445
- srmr = 0.010870324544630827
- tdoa_range = 0.010301441731031155
- gp_auc_std = 0.010292013747347253
- diff_std = 0.008967355082912045
- coe3[2] = 0.007827674312442013
- tdoa_min = 0.006306616972550336
- gp_max_ix_min = 0.006136308995867128
- diff_auc = 0.0051340070008580665
- ratio_max_to_10ms_ave_peaks = 0.004738943235476415
- ac_auc = 0.004496266136650173
- gp_max_val_std = 0.0041456746346383595
- gp_max_ix_std = 0.004125868036871463
- ac_std = 0.003885021388150874
- tdoa_max = 0.003631000059918876
- high_power = 0.0030045878151326076
- coe1[1] = 0.0018496153466231178
- coe1[0] = 0.0017609273074159584
- low_power = 0.001469304829316919
- tdoa_std = 0.0014379655428148422
- coe3[3] = 0.0008876430249109912
- ratio_max_to_9th_ave_peaks = 0.0007635082742412578
- coe3[0] = 0.0
- coe3[1] = 0.0

## Evaluation
cv = 8
### robot-1
#### accuracy
- Mean = 0.7853330453659403
- Standard deviation = 0.13532211463618407

#### f1
- Mean = 0.7853330453659403
- Standard deviation = 0.13532211463618407

#### precision
- Mean = 0.7853330453659403
- Standard deviation = 0.13532211463618407

#### recall
- Mean = 0.7853330453659403
- Standard deviation = 0.13532211463618407

#### facing_probas
- Mean = -100.0
- Standard deviation = 0.0

#### Confusion Matrix|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 1 | 1 |
| Actual Positive | 8 | 25 |

### robot-2
#### accuracy
- Mean = 0.7853330453659403
- Standard deviation = 0.13532211463618407

#### f1
- Mean = 0.7853330453659403
- Standard deviation = 0.13532211463618407

#### precision
- Mean = 0.7853330453659403
- Standard deviation = 0.13532211463618407

#### recall
- Mean = 0.7853330453659403
- Standard deviation = 0.13532211463618407

#### facing_probas
- Mean = -100.0
- Standard deviation = 0.0

#### Confusion Matrix|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 1 | 1 |
| Actual Positive | 8 | 25 |

### robot-3
#### accuracy
- Mean = 0.7853330453659403
- Standard deviation = 0.13532211463618407

#### f1
- Mean = 0.7853330453659403
- Standard deviation = 0.13532211463618407

#### precision
- Mean = 0.7853330453659403
- Standard deviation = 0.13532211463618407

#### recall
- Mean = 0.7853330453659403
- Standard deviation = 0.13532211463618407

#### facing_probas
- Mean = -100.0
- Standard deviation = 0.0

#### Confusion Matrix|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 1 | 1 |
| Actual Positive | 8 | 25 |

### robot-4
#### accuracy
- Mean = 0.7853330453659403
- Standard deviation = 0.13532211463618407

#### f1
- Mean = 0.7853330453659403
- Standard deviation = 0.13532211463618407

#### precision
- Mean = 0.7853330453659403
- Standard deviation = 0.13532211463618407

#### recall
- Mean = 0.7853330453659403
- Standard deviation = 0.13532211463618407

#### facing_probas
- Mean = -100.0
- Standard deviation = 0.0

#### Confusion Matrix|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 1 | 1 |
| Actual Positive | 8 | 25 |

### robot-5
#### accuracy
- Mean = 0.7853330453659403
- Standard deviation = 0.13532211463618407

#### f1
- Mean = 0.7853330453659403
- Standard deviation = 0.13532211463618407

#### precision
- Mean = 0.7853330453659403
- Standard deviation = 0.13532211463618407

#### recall
- Mean = 0.7853330453659403
- Standard deviation = 0.13532211463618407

#### facing_probas
- Mean = -100.0
- Standard deviation = 0.0

#### Confusion Matrix|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 1 | 1 |
| Actual Positive | 8 | 25 |

