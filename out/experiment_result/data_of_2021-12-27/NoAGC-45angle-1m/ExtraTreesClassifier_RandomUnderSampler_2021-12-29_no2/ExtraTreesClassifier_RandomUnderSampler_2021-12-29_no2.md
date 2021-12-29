# ExtraTreesClassifier_RandomUnderSampler_2021-12-29_no2
## Constants
- CSV_PATH = ../out/csv/experiment
- OUTPUT_PATH = ../out/experiment_result/data_of_2021-12-27/NoAGC-45angle-1m
- FEATURE_ATTRBS = ['low_power', 'high_power', 'hlbr', 'coe1[0]', 'coe1[1]', 'coe3[0]', 'coe3[1]', 'coe3[2]', 'coe3[3]', 'ratio_max_to_10ms_ave_peaks', 'ratio_max_to_9th_ave_peaks', 'ac_std', 'ac_auc', 'diff_std', 'diff_auc', 'srmr', 'gp_max_val_std', 'gp_max_val_range', 'gp_max_val_min', 'gp_max_val_max', 'gp_max_val_mean', 'gp_max_ix_std', 'gp_max_ix_range', 'gp_max_ix_min', 'gp_max_ix_max', 'gp_max_ix_mean', 'gp_auc_std', 'gp_auc_range', 'gp_auc_min', 'gp_auc_max', 'gp_auc_mean', 'tdoa_std', 'tdoa_range', 'tdoa_min', 'tdoa_max', 'tdoa_mean']
- LABEL_ATTRB = ['facing2']
- FACING_DOV_ANGLES = [1, 2]
- NCV = 8
- SCORING = ['accuracy', 'balanced_accuracy', 'f1']
- REFIT_SCORING = balanced_accuracy
- PARAM_GRID = [{'est__n_estimators': [50, 100, 150, 200, 300], 'est__min_samples_split': [2, 5, 10], 'est__min_samples_leaf': [1, 5, 10], 'est__max_features': ['sqrt', 'log2', None], 'est__bootstrap': [False], 'est__n_jobs': [-1], 'est__random_state': [42], 'est__max_samples': [0.01, 0.5, 0.09]}, {'est__n_estimators': [50, 100, 150, 200, 300], 'est__min_samples_split': [2, 5, 10], 'est__min_samples_leaf': [1, 5, 10], 'est__max_features': ['sqrt', 'log2', None], 'est__bootstrap': [True], 'est__oob_score': [True, False], 'est__n_jobs': [-1], 'est__random_state': [42], 'est__max_samples': [0.01, 0.5, 0.09]}]
- TRAIN_SET_SESSION = ['trial1', 'trial2']
- TEST_SET_SESSION = ['trial3', 'trial4', 'trial5']
- DISTANCE = [1]
- AGC_STATUS = ['NoAGC']

## Loaded CSV
- 2021-12-27_raspi_48000Hz_w1_N2^12_overlap80_new.csv

## Estimator
### Type
- resampler = RandomUnderSampler
- estimator = ExtraTreesClassifier

### Arguments for hyperparameter search
- resampler = RandomUnderSampler
- estimator = ExtraTreesClassifier
- param_grid = 
	- {'est__n_estimators': [50, 100, 150, 200, 300], 'est__min_samples_split': [2, 5, 10], 'est__min_samples_leaf': [1, 5, 10], 'est__max_features': ['sqrt', 'log2', None], 'est__bootstrap': [False], 'est__n_jobs': [-1], 'est__random_state': [42], 'est__max_samples': [0.01, 0.5, 0.09]}
	- {'est__n_estimators': [50, 100, 150, 200, 300], 'est__min_samples_split': [2, 5, 10], 'est__min_samples_leaf': [1, 5, 10], 'est__max_features': ['sqrt', 'log2', None], 'est__bootstrap': [True], 'est__oob_score': [True, False], 'est__n_jobs': [-1], 'est__random_state': [42], 'est__max_samples': [0.01, 0.5, 0.09]}

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
	- sampling_strategy_ = OrderedDict([(1, 18)])
	- sample_indices_ = [ 4  5  6  7  8  9 16 17 18 19 20 21 28 29 30 31 32 33  0 25 14  1 27 11
 38 23  3 10 35 24 36 34  2 15 39 13]

- best_estimator
	- base_estimator = ExtraTreeClassifier()
	- n_estimators = 50
	- estimator_params = ('criterion', 'max_depth', 'min_samples_split', 'min_samples_leaf', 'min_weight_fraction_leaf', 'max_features', 'max_leaf_nodes', 'min_impurity_decrease', 'min_impurity_split', 'random_state', 'ccp_alpha')
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
	- max_features = sqrt
	- max_leaf_nodes = None
	- min_impurity_decrease = 0.0
	- min_impurity_split = None
	- ccp_alpha = 0.0
	- n_features_in_ = 36
	- n_features_ = 36
	- n_outputs_ = 1
	- classes_ = [0 1]
	- n_classes_ = 2
	- base_estimator_ = ExtraTreeClassifier()

#### Importance of features
- gp_auc_max = 0.11480811327933818
- high_power = 0.11320408400954456
- diff_auc = 0.09364188332784824
- hlbr = 0.0857167275897253
- diff_std = 0.07616341683008349
- srmr = 0.07227284148981776
- gp_auc_mean = 0.05651169273745485
- gp_max_val_mean = 0.05210159673927789
- gp_max_val_max = 0.04528063890132856
- gp_auc_min = 0.04101598321163538
- ratio_max_to_10ms_ave_peaks = 0.04069353650782959
- gp_max_val_min = 0.03420461945461946
- coe1[0] = 0.025088687274961784
- tdoa_range = 0.019902458652458658
- gp_max_ix_std = 0.01963492063492064
- low_power = 0.011825320877952456
- gp_max_val_std = 0.01168888888888889
- gp_auc_std = 0.011500000000000002
- tdoa_std = 0.007417989417989419
- coe3[2] = 0.007090050835148876
- gp_max_ix_range = 0.006933621933621936
- coe1[1] = 0.0067816739351778295
- tdoa_max = 0.006172494172494176
- tdoa_min = 0.005853174603174605
- gp_max_ix_mean = 0.004920854973486553
- gp_max_ix_max = 0.004894059644059644
- tdoa_mean = 0.004860263193596525
- gp_max_ix_min = 0.004842287342287343
- gp_auc_range = 0.004274587985114301
- gp_max_val_range = 0.0039947089947089945
- coe3[3] = 0.002934892787524369
- ratio_max_to_9th_ave_peaks = 0.001851851851851852
- ac_std = 0.0015584415584415578
- ac_auc = 0.0003636363636363646
- coe3[0] = 0.0
- coe3[1] = 0.0

## Evaluation
cv = 8
### accuracy
- Scores = [ 0.75, 1.0, 1.0, 0.8571428571428571, 1.0, 1.0, 1.0, 1.0 ]
- Mean = 0.9508928571428572
- Standard deviation = 0.08917403730106331

### balanced_accuracy
- Scores = [ 0.75, 1.0, 1.0, 0.875, 1.0, 1.0, 1.0, 1.0 ]
- Mean = 0.953125
- Standard deviation = 0.08699631816921909

### f1
- Scores = [ 0.8, 1.0, 1.0, 0.8571428571428571, 1.0, 1.0, 1.0, 1.0 ]
- Mean = 0.9571428571428572
- Standard deviation = 0.07559289460184544

### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 25 | 2 |
| Actual Positive | 1 | 31 |

      