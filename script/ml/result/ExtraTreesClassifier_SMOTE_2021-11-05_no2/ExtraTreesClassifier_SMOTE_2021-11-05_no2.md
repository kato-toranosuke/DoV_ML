# ExtraTreesClassifier_SMOTE_2021-11-05_no2
## Constants
- CSV_PATH = ../../out/csv/
- OUTPUT_PATH = ./result/
- FEATURE_ATTRBS = ['low_power', 'high_power', 'hlbr', 'coe1[0]', 'coe1[1]', 'coe3[0]', 'coe3[1]', 'coe3[2]', 'coe3[3]', 'ratio_max_to_10ms_ave_peaks', 'ratio_max_to_9th_ave_peaks', 'ac_std', 'ac_auc', 'diff_std', 'diff_auc', 'srmr', 'gp_max_val_std', 'gp_max_val_range', 'gp_max_val_min', 'gp_max_val_max', 'gp_max_val_mean', 'gp_max_ix_std', 'gp_max_ix_range', 'gp_max_ix_min', 'gp_max_ix_max', 'gp_max_ix_mean', 'gp_auc_std', 'gp_auc_range', 'gp_auc_min', 'gp_auc_max', 'gp_auc_mean', 'tdoa_std', 'tdoa_range', 'tdoa_min', 'tdoa_max', 'tdoa_mean']
- LABEL_ATTRB = ['dov_angle']
- FACING_DOV_ANGLES = [0, 45, 315]
- NCV = 10
- SCORING = ['accuracy', 'balanced_accuracy', 'f1']
- REFIT_SCORING = balanced_accuracy
- PARAM_GRID = [{'est__n_estimators': [10, 100, 1000], 'est__min_samples_split': [2, 5, 10], 'est__min_samples_leaf': [1, 5, 10], 'est__max_features': ['sqrt', 'log2', None], 'est__bootstrap': [False], 'est__n_jobs': [-1], 'est__random_state': [42], 'est__max_samples': [0.01, 0.5, 0.09]}, {'est__n_estimators': [10, 100, 1000], 'est__min_samples_split': [2, 5, 10], 'est__min_samples_leaf': [1, 5, 10], 'est__max_features': ['sqrt', 'log2', None], 'est__bootstrap': [True], 'est__oob_score': [True, False], 'est__n_jobs': [-1], 'est__random_state': [42], 'est__max_samples': [0.01, 0.5, 0.09]}]

## Loaded CSV
- features_mono_ch_matlab.csv

## Estimator
### Type
- resampler = SMOTE
- estimator = ExtraTreesClassifier

### Arguments for hyperparameter search
- resampler = SMOTE
- estimator = ExtraTreesClassifier
- param_grid = 
	- {'est__n_estimators': [10, 100, 1000], 'est__min_samples_split': [2, 5, 10], 'est__min_samples_leaf': [1, 5, 10], 'est__max_features': ['sqrt', 'log2', None], 'est__bootstrap': [False], 'est__n_jobs': [-1], 'est__random_state': [42], 'est__max_samples': [0.01, 0.5, 0.09]}
	- {'est__n_estimators': [10, 100, 1000], 'est__min_samples_split': [2, 5, 10], 'est__min_samples_leaf': [1, 5, 10], 'est__max_features': ['sqrt', 'log2', None], 'est__bootstrap': [True], 'est__oob_score': [True, False], 'est__n_jobs': [-1], 'est__random_state': [42], 'est__max_samples': [0.01, 0.5, 0.09]}

- scoring = ['accuracy', 'balanced_accuracy', 'f1']
- refit = balanced_accuracy
- cv = 10

### Parameters of the best estimator
#### The best hyper-parameters
- best_resampler
	- sampling_strategy = auto
	- random_state = 42
	- k_neighbors = 5
	- n_jobs = -1
	- n_features_in_ = 36
	- sampling_strategy_ = OrderedDict([(1, 1440)])
	- nn_k_ = NearestNeighbors(n_neighbors=6)

- best_estimator
	- base_estimator = ExtraTreeClassifier()
	- n_estimators = 100
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
	- min_samples_split = 5
	- min_samples_leaf = 1
	- min_weight_fraction_leaf = 0.0
	- max_features = None
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
- gp_max_val_mean = 0.19642306887853647
- gp_max_val_max = 0.1692773953224482
- gp_max_val_min = 0.0827138266320743
- gp_max_val_range = 0.0452263071525685
- gp_auc_min = 0.0380043968206369
- gp_max_val_std = 0.037065383632596545
- gp_auc_mean = 0.02831922396406728
- high_power = 0.022471139702931017
- diff_std = 0.021766530353827997
- gp_auc_max = 0.021126738879571658
- diff_auc = 0.01959512837809957
- gp_auc_std = 0.019534693590457244
- gp_max_ix_mean = 0.01928590050896711
- tdoa_mean = 0.01885256624169645
- tdoa_min = 0.018376977718417592
- ac_auc = 0.018343444474628927
- ratio_max_to_9th_ave_peaks = 0.01679282183970437
- gp_max_ix_min = 0.01660538416917148
- ratio_max_to_10ms_ave_peaks = 0.016275320865895747
- gp_auc_range = 0.016137653460460415
- srmr = 0.01554209008011942
- tdoa_std = 0.013939345534847434
- gp_max_ix_std = 0.013751154064872352
- gp_max_ix_max = 0.013379710004281483
- hlbr = 0.013057045229441231
- tdoa_max = 0.013036450089146088
- ac_std = 0.01126831081499987
- gp_max_ix_range = 0.009588791216200923
- tdoa_range = 0.00950045775277371
- coe1[1] = 0.00926054763789588
- coe1[0] = 0.00914802241468673
- coe3[2] = 0.009067281973513877
- coe3[3] = 0.008814014786349685
- low_power = 0.008452875814113536
- coe3[0] = 0.0
- coe3[1] = 0.0

## Evaluation
cv = 10
### accuracy
- Scores = [ 0.7899305555555556, 0.90625, 0.8888888888888888, 0.8871527777777778, 0.8559027777777778, 0.8263888888888888, 0.8541666666666666, 0.8333333333333334, 0.890625, 0.7638888888888888 ]
- Mean = 0.8496527777777778
- Standard deviation = 0.04429091320219026

### balanced_accuracy
- Scores = [ 0.8226851851851852, 0.9046296296296297, 0.8888888888888888, 0.8597222222222223, 0.8402777777777778, 0.7796296296296297, 0.8657407407407407, 0.7944444444444444, 0.8754629629629629, 0.6953703703703704 ]
- Mean = 0.8326851851851853
- Standard deviation = 0.05939589282979092

### f1
- Scores = [ 0.772983114446529, 0.8778280542986425, 0.8571428571428572, 0.832904884318766, 0.801909307875895, 0.7191011235955056, 0.8242677824267782, 0.7419354838709676, 0.8481927710843373, 0.5723270440251572 ]
- Mean = 0.7848592423085436
- Standard deviation = 0.08573735199146575

### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 3242 | 358 |
| Actual Positive | 508 | 1652 |

      