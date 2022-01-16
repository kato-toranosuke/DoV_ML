# ExtraTreesClassifier_SMOTETomek_2022-01-16_no6
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
- resampler = SMOTETomek
- estimator = ExtraTreesClassifier

### Arguments for hyperparameter search
- resampler = SMOTETomek
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
	- tomek = None
	- n_jobs = -1
	- n_features_in_ = 36
	- sampling_strategy_ = auto
	- smote_ = SMOTE(n_jobs=-1, random_state=42)
	- tomek_ = TomekLinks(n_jobs=-1, sampling_strategy='all')

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
	- min_samples_leaf = 10
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
- gp_max_val_min = 0.17373093222446112
- gp_max_val_mean = 0.15940195531112814
- gp_auc_min = 0.15722383704653456
- gp_auc_mean = 0.11468535658110574
- gp_max_val_max = 0.11354887430640483
- gp_auc_max = 0.09403928377274912
- srmr = 0.055612945457845585
- hlbr = 0.03430172011899815
- gp_max_ix_range = 0.009207317745401006
- tdoa_range = 0.00804342612169419
- tdoa_mean = 0.007745525080501955
- tdoa_min = 0.006329691261317332
- gp_max_ix_max = 0.006202861425332004
- ratio_max_to_9th_ave_peaks = 0.006071820936579123
- tdoa_max = 0.005935656630041019
- diff_std = 0.005666153119623266
- high_power = 0.0047866309834740444
- gp_auc_range = 0.004640641510185479
- gp_max_ix_min = 0.0038631175433449625
- gp_max_ix_mean = 0.0035678498833066957
- gp_max_val_range = 0.0030851932087775816
- gp_max_val_std = 0.0029160073374361562
- gp_max_ix_std = 0.002829569726858102
- tdoa_std = 0.0024995089417061992
- gp_auc_std = 0.0021087729393905593
- coe1[0] = 0.0019919809591936333
- coe1[1] = 0.0019567457033859716
- diff_auc = 0.0019237567811335283
- ratio_max_to_10ms_ave_peaks = 0.0017806218164876928
- low_power = 0.0012115996767495117
- ac_auc = 0.0010790846655837675
- coe3[2] = 0.0009440133948341333
- coe3[3] = 0.0007653595155792377
- ac_std = 0.0003021882728557492
- coe3[0] = 0.0
- coe3[1] = 0.0

## Evaluation
cv = 8
### robot-1
#### accuracy
- Mean = 0.7717243709020024
- Standard deviation = 0.1572859469374131

#### f1
- Mean = 0.7717243709020026
- Standard deviation = 0.1572859469374131

#### precision
- Mean = 0.7717243709020024
- Standard deviation = 0.1572859469374131

#### recall
- Mean = 0.7717243709020024
- Standard deviation = 0.1572859469374131

#### facing_probas
- Mean = -100.0
- Standard deviation = 0.0

#### Confusion Matrix|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 2 | 2 |
| Actual Positive | 9 | 25 |

### robot-2
#### accuracy
- Mean = 0.7717243709020024
- Standard deviation = 0.1572859469374131

#### f1
- Mean = 0.7717243709020026
- Standard deviation = 0.1572859469374131

#### precision
- Mean = 0.7717243709020024
- Standard deviation = 0.1572859469374131

#### recall
- Mean = 0.7717243709020024
- Standard deviation = 0.1572859469374131

#### facing_probas
- Mean = -100.0
- Standard deviation = 0.0

#### Confusion Matrix|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 2 | 2 |
| Actual Positive | 9 | 25 |

### robot-3
#### accuracy
- Mean = 0.7717243709020024
- Standard deviation = 0.1572859469374131

#### f1
- Mean = 0.7717243709020026
- Standard deviation = 0.1572859469374131

#### precision
- Mean = 0.7717243709020024
- Standard deviation = 0.1572859469374131

#### recall
- Mean = 0.7717243709020024
- Standard deviation = 0.1572859469374131

#### facing_probas
- Mean = -100.0
- Standard deviation = 0.0

#### Confusion Matrix|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 2 | 2 |
| Actual Positive | 9 | 25 |

### robot-4
#### accuracy
- Mean = 0.7717243709020024
- Standard deviation = 0.1572859469374131

#### f1
- Mean = 0.7717243709020026
- Standard deviation = 0.1572859469374131

#### precision
- Mean = 0.7717243709020024
- Standard deviation = 0.1572859469374131

#### recall
- Mean = 0.7717243709020024
- Standard deviation = 0.1572859469374131

#### facing_probas
- Mean = -100.0
- Standard deviation = 0.0

#### Confusion Matrix|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 2 | 2 |
| Actual Positive | 9 | 25 |

### robot-5
#### accuracy
- Mean = 0.7717243709020024
- Standard deviation = 0.1572859469374131

#### f1
- Mean = 0.7717243709020026
- Standard deviation = 0.1572859469374131

#### precision
- Mean = 0.7717243709020024
- Standard deviation = 0.1572859469374131

#### recall
- Mean = 0.7717243709020024
- Standard deviation = 0.1572859469374131

#### facing_probas
- Mean = -100.0
- Standard deviation = 0.0

#### Confusion Matrix|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 2 | 2 |
| Actual Positive | 9 | 25 |

