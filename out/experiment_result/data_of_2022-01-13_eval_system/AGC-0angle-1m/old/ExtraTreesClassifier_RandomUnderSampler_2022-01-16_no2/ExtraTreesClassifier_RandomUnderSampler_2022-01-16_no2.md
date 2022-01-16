# ExtraTreesClassifier_RandomUnderSampler_2022-01-16_no2
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
- resampler = RandomUnderSampler
- estimator = ExtraTreesClassifier

### Arguments for hyperparameter search
- resampler = RandomUnderSampler
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
	- replacement = False
	- n_features_in_ = 36
	- sampling_strategy_ = OrderedDict([(0, 15)])
	- sample_indices_ = [ 3  8 45 57 16 66 42 60 15 69 58 62 40  6 64  0  1  2 18 19 20 36 37 38
 54 55 56 72 73 74]

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
- gp_max_ix_range = 0.10581648757851521
- gp_auc_min = 0.08679965875060754
- gp_auc_max = 0.06359070516951414
- tdoa_min = 0.06346760313955506
- gp_max_ix_min = 0.05334779847244991
- gp_max_val_mean = 0.0507849549572954
- gp_auc_mean = 0.049267176503317876
- gp_max_val_min = 0.04855344576267482
- tdoa_range = 0.04701012704495775
- hlbr = 0.043019271527437675
- gp_auc_std = 0.040810607461107005
- gp_max_val_max = 0.036681154920926794
- tdoa_std = 0.03285308330780937
- high_power = 0.0308133489183387
- gp_max_val_std = 0.029422704032298946
- gp_max_ix_mean = 0.02636524018988437
- gp_max_val_range = 0.02409887722285493
- tdoa_max = 0.023549754266808942
- tdoa_mean = 0.022511960486755297
- gp_auc_range = 0.020698035440551422
- gp_max_ix_std = 0.018786340603690034
- diff_auc = 0.01769470710981651
- coe3[2] = 0.01667390182098184
- gp_max_ix_max = 0.0151053137033373
- srmr = 0.010438114533950077
- coe1[0] = 0.009033797108022894
- coe3[3] = 0.0031552185654333503
- ratio_max_to_9th_ave_peaks = 0.002893542290470659
- low_power = 0.0021106933658729243
- ac_std = 0.0017241379310344843
- ratio_max_to_10ms_ave_peaks = 0.0013690700109805169
- ac_auc = 0.0011503957078218888
- coe1[1] = 0.0004027720949263511
- coe3[0] = 0.0
- coe3[1] = 0.0
- diff_std = 0.0

## Evaluation
cv = 8
### robot-1
#### accuracy
- Mean = 0.7477175261385788
- Standard deviation = 0.2124884934447419

#### f1
- Mean = 0.7477175261385788
- Standard deviation = 0.21248849344474194

#### precision
- Mean = 0.7477175261385788
- Standard deviation = 0.2124884934447419

#### recall
- Mean = 0.7477175261385788
- Standard deviation = 0.2124884934447419

#### facing_probas
- Mean = -100.0
- Standard deviation = 0.0

#### Confusion Matrix|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 2 | 2 |
| Actual Positive | 10 | 24 |

### robot-2
#### accuracy
- Mean = 0.7477175261385788
- Standard deviation = 0.2124884934447419

#### f1
- Mean = 0.7477175261385788
- Standard deviation = 0.21248849344474194

#### precision
- Mean = 0.7477175261385788
- Standard deviation = 0.2124884934447419

#### recall
- Mean = 0.7477175261385788
- Standard deviation = 0.2124884934447419

#### facing_probas
- Mean = -100.0
- Standard deviation = 0.0

#### Confusion Matrix|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 2 | 2 |
| Actual Positive | 10 | 24 |

### robot-3
#### accuracy
- Mean = 0.7477175261385788
- Standard deviation = 0.2124884934447419

#### f1
- Mean = 0.7477175261385788
- Standard deviation = 0.21248849344474194

#### precision
- Mean = 0.7477175261385788
- Standard deviation = 0.2124884934447419

#### recall
- Mean = 0.7477175261385788
- Standard deviation = 0.2124884934447419

#### facing_probas
- Mean = -100.0
- Standard deviation = 0.0

#### Confusion Matrix|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 2 | 2 |
| Actual Positive | 10 | 24 |

### robot-4
#### accuracy
- Mean = 0.7477175261385788
- Standard deviation = 0.2124884934447419

#### f1
- Mean = 0.7477175261385788
- Standard deviation = 0.21248849344474194

#### precision
- Mean = 0.7477175261385788
- Standard deviation = 0.2124884934447419

#### recall
- Mean = 0.7477175261385788
- Standard deviation = 0.2124884934447419

#### facing_probas
- Mean = -100.0
- Standard deviation = 0.0

#### Confusion Matrix|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 2 | 2 |
| Actual Positive | 10 | 24 |

### robot-5
#### accuracy
- Mean = 0.7477175261385788
- Standard deviation = 0.2124884934447419

#### f1
- Mean = 0.7477175261385788
- Standard deviation = 0.21248849344474194

#### precision
- Mean = 0.7477175261385788
- Standard deviation = 0.2124884934447419

#### recall
- Mean = 0.7477175261385788
- Standard deviation = 0.2124884934447419

#### facing_probas
- Mean = -100.0
- Standard deviation = 0.0

#### Confusion Matrix|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 2 | 2 |
| Actual Positive | 10 | 24 |

