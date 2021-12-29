# ExtraTreesClassifier_RandomUnderSampler_2021-12-29_no2
## Constants
- CSV_PATH = ../out/csv/experiment
- OUTPUT_PATH = ../out/experiment_result/data_of_2021-12-27/AGC-45angle-5m
- FEATURE_ATTRBS = ['low_power', 'high_power', 'hlbr', 'coe1[0]', 'coe1[1]', 'coe3[0]', 'coe3[1]', 'coe3[2]', 'coe3[3]', 'ratio_max_to_10ms_ave_peaks', 'ratio_max_to_9th_ave_peaks', 'ac_std', 'ac_auc', 'diff_std', 'diff_auc', 'srmr', 'gp_max_val_std', 'gp_max_val_range', 'gp_max_val_min', 'gp_max_val_max', 'gp_max_val_mean', 'gp_max_ix_std', 'gp_max_ix_range', 'gp_max_ix_min', 'gp_max_ix_max', 'gp_max_ix_mean', 'gp_auc_std', 'gp_auc_range', 'gp_auc_min', 'gp_auc_max', 'gp_auc_mean', 'tdoa_std', 'tdoa_range', 'tdoa_min', 'tdoa_max', 'tdoa_mean']
- LABEL_ATTRB = ['facing2']
- FACING_DOV_ANGLES = [1, 2]
- NCV = 8
- SCORING = ['accuracy', 'balanced_accuracy', 'f1']
- REFIT_SCORING = balanced_accuracy
- PARAM_GRID = [{'est__n_estimators': [50, 100, 150, 200, 300], 'est__min_samples_split': [2, 5, 10], 'est__min_samples_leaf': [1, 5, 10], 'est__max_features': ['sqrt', 'log2', None], 'est__bootstrap': [False], 'est__n_jobs': [-1], 'est__random_state': [42], 'est__max_samples': [0.01, 0.5, 0.09]}, {'est__n_estimators': [50, 100, 150, 200, 300], 'est__min_samples_split': [2, 5, 10], 'est__min_samples_leaf': [1, 5, 10], 'est__max_features': ['sqrt', 'log2', None], 'est__bootstrap': [True], 'est__oob_score': [True, False], 'est__n_jobs': [-1], 'est__random_state': [42], 'est__max_samples': [0.01, 0.5, 0.09]}]
- TRAIN_SET_SESSION = ['trial1', 'trial2']
- TEST_SET_SESSION = ['trial3', 'trial4', 'trial5']
- DISTANCE = [5]
- AGC_STATUS = ['AGC']

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
	- sampling_strategy_ = OrderedDict([(1, 24)])
	- sample_indices_ = [ 4  5  6  7  8  9 16 17 18 19 20 21 28 29 30 31 32 33 40 41 42 43 44 45
 14 34  0 48 23 15 25  1 47 11  2 24 27  3 10 39 35 46 36 49 38 13 22 26]

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
- high_power = 0.1085034210427466
- gp_max_val_max = 0.09802489269989272
- gp_max_val_mean = 0.08104694932404467
- gp_auc_max = 0.0760972199097199
- diff_auc = 0.06801741314241314
- gp_auc_mean = 0.06749854234827288
- gp_auc_min = 0.061558698424022375
- hlbr = 0.05870660497249041
- gp_max_val_min = 0.05375458291353432
- srmr = 0.04049496947683154
- coe1[0] = 0.04003449748945342
- diff_std = 0.036684381572582685
- coe3[3] = 0.036388963140321834
- coe3[2] = 0.02127490560275418
- gp_max_val_std = 0.01980024869766249
- coe1[1] = 0.018951849294496347
- gp_auc_range = 0.01775899052638183
- gp_auc_std = 0.01406946399011616
- low_power = 0.013181339006765953
- gp_max_ix_min = 0.013043920598204483
- tdoa_min = 0.011264421251214556
- gp_max_ix_range = 0.009435536685536688
- tdoa_max = 0.008800925925925927
- gp_max_ix_max = 0.00561904761904762
- ac_std = 0.0035833333333333333
- ac_auc = 0.002957516339869281
- tdoa_range = 0.002777777777777778
- ratio_max_to_10ms_ave_peaks = 0.0027777777777777775
- ratio_max_to_9th_ave_peaks = 0.002611111111111112
- gp_max_val_range = 0.0024010683760683727
- gp_max_ix_std = 0.0011111111111111111
- tdoa_mean = 0.0008888888888888888
- tdoa_std = 0.0008333333333333333
- gp_max_ix_mean = 4.6296296296296504e-05
- coe3[0] = 0.0
- coe3[1] = 0.0

## Evaluation
cv = 8
### accuracy
- Scores = [ 1.0, 1.0, 0.9, 0.6666666666666666, 1.0, 1.0, 1.0, 1.0 ]
- Mean = 0.9458333333333333
- Standard deviation = 0.11047561319635711

### balanced_accuracy
- Scores = [ 1.0, 1.0, 0.9, 0.7, 1.0, 1.0, 1.0, 1.0 ]
- Mean = 0.95
- Standard deviation = 0.1

### f1
- Scores = [ 1.0, 1.0, 0.9090909090909091, 0.5714285714285715, 1.0, 1.0, 1.0, 1.0 ]
- Mean = 0.935064935064935
- Standard deviation = 0.1406260248552449

### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 35 | 1 |
| Actual Positive | 3 | 36 |

      