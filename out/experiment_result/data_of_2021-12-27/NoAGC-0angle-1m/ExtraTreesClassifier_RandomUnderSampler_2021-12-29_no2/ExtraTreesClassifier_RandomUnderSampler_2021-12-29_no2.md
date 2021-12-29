# ExtraTreesClassifier_RandomUnderSampler_2021-12-29_no2
## Constants
- CSV_PATH = ../out/csv/experiment
- OUTPUT_PATH = ../out/experiment_result/data_of_2021-12-27/NoAGC-0angle-1m
- FEATURE_ATTRBS = ['low_power', 'high_power', 'hlbr', 'coe1[0]', 'coe1[1]', 'coe3[0]', 'coe3[1]', 'coe3[2]', 'coe3[3]', 'ratio_max_to_10ms_ave_peaks', 'ratio_max_to_9th_ave_peaks', 'ac_std', 'ac_auc', 'diff_std', 'diff_auc', 'srmr', 'gp_max_val_std', 'gp_max_val_range', 'gp_max_val_min', 'gp_max_val_max', 'gp_max_val_mean', 'gp_max_ix_std', 'gp_max_ix_range', 'gp_max_ix_min', 'gp_max_ix_max', 'gp_max_ix_mean', 'gp_auc_std', 'gp_auc_range', 'gp_auc_min', 'gp_auc_max', 'gp_auc_mean', 'tdoa_std', 'tdoa_range', 'tdoa_min', 'tdoa_max', 'tdoa_mean']
- LABEL_ATTRB = ['facing']
- FACING_DOV_ANGLES = [1]
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
	- sampling_strategy_ = OrderedDict([(0, 8)])
	- sample_indices_ = [35 19 30 21 10 11 38 31  0  1 12 13 24 25 36 37]

- best_estimator
	- base_estimator = ExtraTreeClassifier()
	- n_estimators = 150
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
	- max_features = log2
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
- gp_auc_min = 0.07280288692788693
- gp_max_val_min = 0.06825835738335741
- gp_auc_max = 0.06324879287379288
- coe3[2] = 0.05633204295704295
- gp_max_val_mean = 0.051982905982905975
- gp_max_val_max = 0.0512998066748067
- gp_auc_mean = 0.045259583009583014
- srmr = 0.04124444999445
- gp_max_val_range = 0.039876341251341256
- diff_auc = 0.03581351056351058
- ac_std = 0.03296893384393385
- gp_max_ix_max = 0.03179707792207793
- tdoa_max = 0.028788378288378297
- high_power = 0.02762389462389463
- gp_auc_range = 0.025721782846782847
- hlbr = 0.025006632256632258
- diff_std = 0.024898587523587524
- tdoa_range = 0.02475614200614201
- coe1[1] = 0.02457874070374071
- low_power = 0.023449568949568952
- ac_auc = 0.02234010434010434
- gp_max_val_std = 0.021882936507936514
- gp_max_ix_range = 0.02120290820290821
- gp_auc_std = 0.019677567802567807
- ratio_max_to_9th_ave_peaks = 0.018228294853294857
- coe3[3] = 0.01783719983719984
- gp_max_ix_std = 0.016878713878713883
- coe1[0] = 0.013846741221741224
- ratio_max_to_10ms_ave_peaks = 0.013465728715728716
- gp_max_ix_mean = 0.011632395382395383
- tdoa_mean = 0.009208333333333336
- tdoa_std = 0.00835989010989011
- tdoa_min = 0.008192307692307697
- gp_max_ix_min = 0.0015384615384615391
- coe3[0] = 0.0
- coe3[1] = 0.0

## Evaluation
cv = 8
### accuracy
- Scores = [ 0.875, 1.0, 0.625, 1.0, 0.7142857142857143, 0.7142857142857143, 1.0, 0.2857142857142857 ]
- Mean = 0.7767857142857143
- Standard deviation = 0.23214285714285715

### balanced_accuracy
- Scores = [ 0.75, 1.0, 0.75, 1.0, 0.4166666666666667, 0.8333333333333333, 1.0, 0.5833333333333334 ]
- Mean = 0.7916666666666667
- Standard deviation = 0.19982631347136331

### f1
- Scores = [ 0.6666666666666666, 1.0, 0.5714285714285715, 1.0, 0.0, 0.5, 1.0, 0.2857142857142857 ]
- Mean = 0.6279761904761905
- Standard deviation = 0.3441974257803684

### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 36 | 11 |
| Actual Positive | 2 | 10 |

      