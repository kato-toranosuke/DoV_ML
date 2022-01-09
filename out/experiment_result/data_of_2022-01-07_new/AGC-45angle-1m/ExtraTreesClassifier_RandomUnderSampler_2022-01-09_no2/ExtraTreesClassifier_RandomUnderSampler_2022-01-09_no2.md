# ExtraTreesClassifier_RandomUnderSampler_2022-01-09_no2
## Constants
- CSV_PATH = ../out/csv/experiment
- OUTPUT_PATH = ../out/experiment_result/data_of_2022-01-07_new/AGC-45angle-1m
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
- AGC_STATUS = ['AGC']

## Loaded CSV
- 2021-12-27_raspi_48000Hz_w1_N2^12_overlap80_with2022-01-07.csv

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
- gp_max_val_mean = 0.18481734587251836
- gp_auc_max = 0.17789880526769583
- gp_max_val_max = 0.1556673219963075
- srmr = 0.08896385305515742
- gp_auc_min = 0.06948331532239578
- gp_max_val_min = 0.06904963104528322
- gp_auc_mean = 0.06816469383384675
- hlbr = 0.05259790486597083
- ratio_max_to_9th_ave_peaks = 0.011533251691947338
- high_power = 0.01152930402930403
- diff_auc = 0.010932336182336178
- ratio_max_to_10ms_ave_peaks = 0.010848931623931626
- coe1[1] = 0.008911782661782662
- ac_std = 0.008123931623931623
- ac_auc = 0.0076492118992119
- diff_std = 0.0070744921744921715
- tdoa_std = 0.006904761904761903
- gp_max_ix_std = 0.0067120721870721845
- gp_max_ix_mean = 0.006666666666666667
- coe1[0] = 0.006111111111111114
- gp_max_val_range = 0.006022533022533023
- low_power = 0.004899013024013023
- gp_auc_range = 0.004524216524216524
- gp_max_val_std = 0.004222222222222221
- coe3[3] = 0.0034814814814814756
- gp_auc_std = 0.0034038461538461536
- coe3[2] = 0.0016300366300366267
- gp_max_ix_range = 0.0011111111111111111
- tdoa_mean = 0.0008333333333333332
- gp_max_ix_max = 0.0002314814814814814
- coe3[0] = 0.0
- coe3[1] = 0.0
- gp_max_ix_min = 0.0
- tdoa_range = 0.0
- tdoa_min = 0.0
- tdoa_max = 0.0

## Evaluation
cv = 8
### accuracy
- Scores = [ 0.7, 1.0, 1.0, 0.7777777777777778, 1.0, 1.0, 1.0, 1.0 ]
- Mean = 0.9347222222222222
- Standard deviation = 0.11472423996073325

### balanced_accuracy
- Scores = [ 0.7, 1.0, 1.0, 0.8, 1.0, 1.0, 1.0, 1.0 ]
- Mean = 0.9375
- Standard deviation = 0.11110243021644486

### f1
- Scores = [ 0.7692307692307693, 1.0, 1.0, 0.7499999999999999, 1.0, 1.0, 1.0, 1.0 ]
- Mean = 0.9399038461538461
- Standard deviation = 0.10420056154660215

### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 33 | 3 |
| Actual Positive | 2 | 37 |

      