# ExtraTreesClassifier_ClusterCentroids_2022-01-16_no1
## Constants
- CSV_PATH = ../out/csv/experiment
- OUTPUT_PATH = ../out/experiment_result/data_of_2022-01-13_eval_system/AGC-0angle-3m
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
- DISTANCE = [3]
- AGC_STATUS = ['AGC']

## Loaded CSV
- 2021-12-27_AGC.csv
- 2022-01-10_NoAGC.csv
- 2022-01-13_raspi_48000Hz_w1_N2^12_overlap80.csv

## Estimator
### Type
- resampler = ClusterCentroids
- estimator = ExtraTreesClassifier

### Arguments for hyperparameter search
- resampler = ClusterCentroids
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
- gp_max_val_max = 0.25741297852474326
- gp_max_val_mean = 0.21815555555555557
- gp_auc_max = 0.15220410830999068
- gp_auc_min = 0.0936953363801661
- gp_auc_mean = 0.06069411764705883
- gp_max_val_min = 0.04237072583419334
- coe3[2] = 0.029648739495798323
- ac_std = 0.02332287581699347
- diff_auc = 0.018872549019607845
- coe1[1] = 0.016006535947712418
- coe3[3] = 0.01595396825396826
- coe1[0] = 0.010522875816993463
- ac_auc = 0.01051699346405229
- diff_std = 0.008253968253968253
- tdoa_std = 0.006666666666666667
- srmr = 0.006426281389748886
- tdoa_mean = 0.005333333333333333
- low_power = 0.004144444444444447
- gp_max_ix_mean = 0.0035555555555555557
- gp_max_ix_std = 0.003333333333333334
- high_power = 0.003111111111111112
- tdoa_min = 0.0022058823529411764
- ratio_max_to_9th_ave_peaks = 0.0017777777777777779
- gp_max_val_range = 0.0017777777777777779
- tdoa_range = 0.0017777777777777779
- gp_auc_range = 0.0013333333333333335
- hlbr = 0.0007222222222222224
- gp_max_val_std = 0.00020317460317460337
- coe3[0] = 0.0
- coe3[1] = 0.0
- ratio_max_to_10ms_ave_peaks = 0.0
- gp_max_ix_range = 0.0
- gp_max_ix_min = 0.0
- gp_max_ix_max = 0.0
- gp_auc_std = 0.0
- tdoa_max = 0.0

## Evaluation
cv = 8
### robot-1
#### accuracy
- Mean = 0.735
- Standard deviation = 0.20956303745333207

#### f1
- Mean = 0.735
- Standard deviation = 0.20956303745333207

#### precision
- Mean = 0.735
- Standard deviation = 0.20956303745333207

#### recall
- Mean = 0.735
- Standard deviation = 0.20956303745333207

#### facing_probas
- Mean = -100.0
- Standard deviation = 0.0

#### Confusion Matrix|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 2 | 2 |
| Actual Positive | 11 | 24 |

### robot-2
#### accuracy
- Mean = 0.735
- Standard deviation = 0.20956303745333207

#### f1
- Mean = 0.735
- Standard deviation = 0.20956303745333207

#### precision
- Mean = 0.735
- Standard deviation = 0.20956303745333207

#### recall
- Mean = 0.735
- Standard deviation = 0.20956303745333207

#### facing_probas
- Mean = -100.0
- Standard deviation = 0.0

#### Confusion Matrix|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 2 | 2 |
| Actual Positive | 11 | 24 |

### robot-3
#### accuracy
- Mean = 0.735
- Standard deviation = 0.20956303745333207

#### f1
- Mean = 0.735
- Standard deviation = 0.20956303745333207

#### precision
- Mean = 0.735
- Standard deviation = 0.20956303745333207

#### recall
- Mean = 0.735
- Standard deviation = 0.20956303745333207

#### facing_probas
- Mean = -100.0
- Standard deviation = 0.0

#### Confusion Matrix|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 2 | 2 |
| Actual Positive | 11 | 24 |

### robot-4
#### accuracy
- Mean = 0.735
- Standard deviation = 0.20956303745333207

#### f1
- Mean = 0.735
- Standard deviation = 0.20956303745333207

#### precision
- Mean = 0.735
- Standard deviation = 0.20956303745333207

#### recall
- Mean = 0.735
- Standard deviation = 0.20956303745333207

#### facing_probas
- Mean = -100.0
- Standard deviation = 0.0

#### Confusion Matrix|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 2 | 2 |
| Actual Positive | 11 | 24 |

### robot-5
#### accuracy
- Mean = 0.735
- Standard deviation = 0.20956303745333207

#### f1
- Mean = 0.735
- Standard deviation = 0.20956303745333207

#### precision
- Mean = 0.735
- Standard deviation = 0.20956303745333207

#### recall
- Mean = 0.735
- Standard deviation = 0.20956303745333207

#### facing_probas
- Mean = -100.0
- Standard deviation = 0.0

#### Confusion Matrix|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 2 | 2 |
| Actual Positive | 11 | 24 |

