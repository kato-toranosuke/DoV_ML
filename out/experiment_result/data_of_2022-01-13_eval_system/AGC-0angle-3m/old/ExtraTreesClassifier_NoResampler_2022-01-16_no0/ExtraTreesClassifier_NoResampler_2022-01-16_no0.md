# ExtraTreesClassifier_NoResampler_2022-01-16_no0
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
- resampler = NoResampler
- estimator = ExtraTreesClassifier

### Arguments for hyperparameter search
- resampler = NoResampler
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

- best_estimator
	- base_estimator = ExtraTreeClassifier()
	- n_estimators = 250
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
	- min_samples_split = 5
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
- gp_auc_max = 0.10537383857495972
- hlbr = 0.10161041013177513
- gp_max_val_max = 0.09192931460521465
- high_power = 0.0851314422540686
- gp_auc_min = 0.08248738153281461
- gp_auc_mean = 0.07813292749964816
- gp_max_val_mean = 0.07244235477689988
- gp_max_val_min = 0.06836888488026795
- diff_auc = 0.04324274749829762
- diff_std = 0.03753164129387923
- srmr = 0.020312094193230296
- tdoa_mean = 0.019417206441910445
- gp_max_ix_mean = 0.01491908647082167
- coe1[1] = 0.014318322089404171
- gp_max_val_range = 0.012431486534410865
- gp_max_ix_std = 0.012288109842320894
- low_power = 0.011383574445885595
- ratio_max_to_10ms_ave_peaks = 0.011152875966525078
- tdoa_std = 0.010957993675878774
- coe1[0] = 0.01066459468262765
- ac_auc = 0.01035981620972128
- gp_max_ix_range = 0.00900758346464618
- gp_auc_range = 0.008672401269763522
- coe3[3] = 0.008608233427802535
- gp_max_val_std = 0.007818634729850258
- tdoa_range = 0.007269019686846558
- ac_std = 0.006976409735373398
- gp_auc_std = 0.00665338247342633
- ratio_max_to_9th_ave_peaks = 0.006368152665683485
- coe3[2] = 0.0053879225172985545
- tdoa_max = 0.0053456886638540155
- gp_max_ix_max = 0.0051953347415481885
- gp_max_ix_min = 0.004844462201153665
- tdoa_min = 0.003396670822191113
- coe3[0] = 0.0
- coe3[1] = 0.0

## Evaluation
cv = 8
### robot-1
#### accuracy
- Mean = 0.7075
- Standard deviation = 0.17288604146469816

#### f1
- Mean = 0.7075
- Standard deviation = 0.1728860414646982

#### precision
- Mean = 0.7075
- Standard deviation = 0.17288604146469816

#### recall
- Mean = 0.7075
- Standard deviation = 0.17288604146469816

#### facing_probas
- Mean = -100.0
- Standard deviation = 0.0

#### Confusion Matrix|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 0 | 0 |
| Actual Positive | 10 | 23 |

### robot-2
#### accuracy
- Mean = 0.7075
- Standard deviation = 0.17288604146469816

#### f1
- Mean = 0.7075
- Standard deviation = 0.1728860414646982

#### precision
- Mean = 0.7075
- Standard deviation = 0.17288604146469816

#### recall
- Mean = 0.7075
- Standard deviation = 0.17288604146469816

#### facing_probas
- Mean = -100.0
- Standard deviation = 0.0

#### Confusion Matrix|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 0 | 0 |
| Actual Positive | 10 | 23 |

### robot-3
#### accuracy
- Mean = 0.7075
- Standard deviation = 0.17288604146469816

#### f1
- Mean = 0.7075
- Standard deviation = 0.1728860414646982

#### precision
- Mean = 0.7075
- Standard deviation = 0.17288604146469816

#### recall
- Mean = 0.7075
- Standard deviation = 0.17288604146469816

#### facing_probas
- Mean = -100.0
- Standard deviation = 0.0

#### Confusion Matrix|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 0 | 0 |
| Actual Positive | 10 | 23 |

### robot-4
#### accuracy
- Mean = 0.7075
- Standard deviation = 0.17288604146469816

#### f1
- Mean = 0.7075
- Standard deviation = 0.1728860414646982

#### precision
- Mean = 0.7075
- Standard deviation = 0.17288604146469816

#### recall
- Mean = 0.7075
- Standard deviation = 0.17288604146469816

#### facing_probas
- Mean = -100.0
- Standard deviation = 0.0

#### Confusion Matrix|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 0 | 0 |
| Actual Positive | 10 | 23 |

### robot-5
#### accuracy
- Mean = 0.7075
- Standard deviation = 0.17288604146469816

#### f1
- Mean = 0.7075
- Standard deviation = 0.1728860414646982

#### precision
- Mean = 0.7075
- Standard deviation = 0.17288604146469816

#### recall
- Mean = 0.7075
- Standard deviation = 0.17288604146469816

#### facing_probas
- Mean = -100.0
- Standard deviation = 0.0

#### Confusion Matrix|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 0 | 0 |
| Actual Positive | 10 | 23 |

