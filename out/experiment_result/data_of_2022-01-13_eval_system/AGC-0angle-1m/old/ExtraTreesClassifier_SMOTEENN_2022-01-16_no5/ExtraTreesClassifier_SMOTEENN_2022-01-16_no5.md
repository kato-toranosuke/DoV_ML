# ExtraTreesClassifier_SMOTEENN_2022-01-16_no5
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
- resampler = SMOTEENN
- estimator = ExtraTreesClassifier

### Arguments for hyperparameter search
- resampler = SMOTEENN
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
	- smote = None
	- enn = None
	- n_jobs = -1
	- n_features_in_ = 36
	- sampling_strategy_ = auto
	- smote_ = SMOTE(n_jobs=-1, random_state=42)
	- enn_ = EditedNearestNeighbours(n_jobs=-1, sampling_strategy='all')

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
	- max_samples = 0.5
	- criterion = gini
	- max_depth = None
	- min_samples_split = 10
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
	- oob_decision_function_ = [[0.40856009 0.59143991]
 [0.39817285 0.60182715]
 [0.70241035 0.29758965]
 [0.93211421 0.06788579]
 [0.96877706 0.03122294]
 [0.90809574 0.09190426]
 [0.91709724 0.08290276]
 [0.94607985 0.05392015]
 [0.32538156 0.67461844]
 [0.73418918 0.26581082]
 [0.94554361 0.05445639]
 [0.83298461 0.16701539]
 [0.96358998 0.03641002]
 [0.53297835 0.46702165]
 [0.28907407 0.71092593]
 [0.94103664 0.05896336]
 [0.67219485 0.32780515]
 [0.31890332 0.68109668]
 [0.32619048 0.67380952]
 [0.36667532 0.63332468]
 [0.31795489 0.68204511]
 [0.38295745 0.61704255]
 [0.3387549  0.6612451 ]
 [0.38416943 0.61583057]
 [0.42452072 0.57547928]
 [0.30708085 0.69291915]
 [0.33728468 0.66271532]
 [0.31063921 0.68936079]]
	- oob_score_ = 0.8571428571428571

#### Importance of features
- high_power = 0.1400709219858156
- gp_auc_max = 0.10638297872340427
- srmr = 0.08510638297872342
- tdoa_mean = 0.08510638297872342
- hlbr = 0.0776462528070643
- gp_max_val_max = 0.05141843971631206
- diff_auc = 0.04255319148936171
- gp_max_ix_std = 0.04255319148936171
- gp_max_ix_range = 0.04255319148936171
- tdoa_max = 0.04255319148936171
- ratio_max_to_10ms_ave_peaks = 0.02911534154535275
- gp_auc_mean = 0.02873672591633997
- gp_auc_std = 0.02281145506229493
- coe1[0] = 0.021276595744680854
- ratio_max_to_9th_ave_peaks = 0.021276595744680854
- gp_max_val_std = 0.021276595744680854
- gp_max_val_min = 0.021276595744680854
- gp_max_ix_min = 0.021276595744680854
- gp_max_ix_mean = 0.021276595744680854
- gp_auc_range = 0.021276595744680854
- gp_auc_min = 0.021276595744680854
- tdoa_std = 0.021276595744680854
- tdoa_min = 0.011902990626394883
- low_power = 0.0
- coe1[1] = 0.0
- coe3[0] = 0.0
- coe3[1] = 0.0
- coe3[2] = 0.0
- coe3[3] = 0.0
- ac_std = 0.0
- ac_auc = 0.0
- diff_std = 0.0
- gp_max_val_range = 0.0
- gp_max_val_mean = 0.0
- gp_max_ix_max = 0.0
- tdoa_range = 0.0

## Evaluation
cv = 8
### robot-1
#### accuracy
- Mean = 0.748866405280879
- Standard deviation = 0.20338748777407706

#### f1
- Mean = 0.748866405280879
- Standard deviation = 0.20338748777407706

#### precision
- Mean = 0.748866405280879
- Standard deviation = 0.20338748777407706

#### recall
- Mean = 0.748866405280879
- Standard deviation = 0.20338748777407706

#### facing_probas
- Mean = -100.0
- Standard deviation = 0.0

#### Confusion Matrix|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 3 | 3 |
| Actual Positive | 11 | 24 |

### robot-2
#### accuracy
- Mean = 0.748866405280879
- Standard deviation = 0.20338748777407706

#### f1
- Mean = 0.748866405280879
- Standard deviation = 0.20338748777407706

#### precision
- Mean = 0.748866405280879
- Standard deviation = 0.20338748777407706

#### recall
- Mean = 0.748866405280879
- Standard deviation = 0.20338748777407706

#### facing_probas
- Mean = -100.0
- Standard deviation = 0.0

#### Confusion Matrix|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 3 | 3 |
| Actual Positive | 11 | 24 |

### robot-3
#### accuracy
- Mean = 0.748866405280879
- Standard deviation = 0.20338748777407706

#### f1
- Mean = 0.748866405280879
- Standard deviation = 0.20338748777407706

#### precision
- Mean = 0.748866405280879
- Standard deviation = 0.20338748777407706

#### recall
- Mean = 0.748866405280879
- Standard deviation = 0.20338748777407706

#### facing_probas
- Mean = -100.0
- Standard deviation = 0.0

#### Confusion Matrix|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 3 | 3 |
| Actual Positive | 11 | 24 |

### robot-4
#### accuracy
- Mean = 0.748866405280879
- Standard deviation = 0.20338748777407706

#### f1
- Mean = 0.748866405280879
- Standard deviation = 0.20338748777407706

#### precision
- Mean = 0.748866405280879
- Standard deviation = 0.20338748777407706

#### recall
- Mean = 0.748866405280879
- Standard deviation = 0.20338748777407706

#### facing_probas
- Mean = -100.0
- Standard deviation = 0.0

#### Confusion Matrix|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 3 | 3 |
| Actual Positive | 11 | 24 |

### robot-5
#### accuracy
- Mean = 0.748866405280879
- Standard deviation = 0.20338748777407706

#### f1
- Mean = 0.748866405280879
- Standard deviation = 0.20338748777407706

#### precision
- Mean = 0.748866405280879
- Standard deviation = 0.20338748777407706

#### recall
- Mean = 0.748866405280879
- Standard deviation = 0.20338748777407706

#### facing_probas
- Mean = -100.0
- Standard deviation = 0.0

#### Confusion Matrix|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 3 | 3 |
| Actual Positive | 11 | 24 |

