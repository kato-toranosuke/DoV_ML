# ExtraTreesClassifier_ClusterCentroids_2021-12-28_no8
## Constants
- CSV_PATH = ../out/csv/experiment
- OUTPUT_PATH = ../out/experiment_result
- FEATURE_ATTRBS = ['low_power', 'high_power', 'hlbr', 'coe1[0]', 'coe1[1]', 'coe3[0]', 'coe3[1]', 'coe3[2]', 'coe3[3]', 'ratio_max_to_10ms_ave_peaks', 'ratio_max_to_9th_ave_peaks', 'ac_std', 'ac_auc', 'diff_std', 'diff_auc', 'srmr', 'gp_max_val_std', 'gp_max_val_range', 'gp_max_val_min', 'gp_max_val_max', 'gp_max_val_mean', 'gp_max_ix_std', 'gp_max_ix_range', 'gp_max_ix_min', 'gp_max_ix_max', 'gp_max_ix_mean', 'gp_auc_std', 'gp_auc_range', 'gp_auc_min', 'gp_auc_max', 'gp_auc_mean', 'tdoa_std', 'tdoa_range', 'tdoa_min', 'tdoa_max', 'tdoa_mean']
- LABEL_ATTRB = ['facing']
- FACING_DOV_ANGLES = [1]
- NCV = 8
- SCORING = ['accuracy', 'balanced_accuracy', 'f1']
- REFIT_SCORING = balanced_accuracy
- PARAM_GRID = [{'est__n_estimators': [50, 100, 150, 200, 300], 'est__min_samples_split': [2, 5, 10], 'est__min_samples_leaf': [1, 5, 10], 'est__max_features': ['sqrt', 'log2', None], 'est__bootstrap': [False], 'est__n_jobs': [-1], 'est__random_state': [42], 'est__max_samples': [0.01, 0.5, 0.09]}, {'est__n_estimators': [50, 100, 150, 200, 300], 'est__min_samples_split': [2, 5, 10], 'est__min_samples_leaf': [1, 5, 10], 'est__max_features': ['sqrt', 'log2', None], 'est__bootstrap': [True], 'est__oob_score': [True, False], 'est__n_jobs': [-1], 'est__random_state': [42], 'est__max_samples': [0.01, 0.5, 0.09]}]
- TRAIN_SET_SESSION = ['trial1', 'trial2']
- TEST_SET_SESSION = ['trial3', 'trial4', 'trial5']

## Loaded CSV
- 2021-12-27_raspi_48000Hz_w1_N2^12_overlap80_withfacing.csv

## Estimator
### Type
- resampler = ClusterCentroids
- estimator = ExtraTreesClassifier

### Arguments for hyperparameter search
- resampler = ClusterCentroids
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
	- estimator = None
	- voting = auto
	- n_jobs = deprecated
	- n_features_in_ = 36
	- sampling_strategy_ = OrderedDict([(0, 10)])
	- estimator_ = KMeans(n_clusters=10, random_state=42)
	- voting_ = soft

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
	- min_samples_split = 10
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
- gp_max_val_mean = 0.2213444862081748
- gp_auc_max = 0.14615885692989763
- gp_auc_min = 0.1370385982856571
- gp_max_val_max = 0.10869405399259445
- gp_max_val_min = 0.07578510900863843
- gp_auc_mean = 0.0712684648012691
- srmr = 0.0709111022803223
- hlbr = 0.047510732122496825
- ratio_max_to_10ms_ave_peaks = 0.021796664873587952
- tdoa_min = 0.016926203208556152
- tdoa_max = 0.014436363636363641
- gp_max_ix_max = 0.014332867132867135
- gp_max_ix_range = 0.012511027434104358
- coe1[0] = 0.011428571428571429
- tdoa_range = 0.00969030969030969
- gp_max_ix_min = 0.00831888111888112
- gp_max_ix_std = 0.004615384615384617
- diff_auc = 0.0036363636363636364
- low_power = 0.0018181818181818188
- coe3[3] = 0.0017777777777777787
- high_power = 0.0
- coe1[1] = 0.0
- coe3[0] = 0.0
- coe3[1] = 0.0
- coe3[2] = 0.0
- ratio_max_to_9th_ave_peaks = 0.0
- ac_std = 0.0
- ac_auc = 0.0
- diff_std = 0.0
- gp_max_val_std = 0.0
- gp_max_val_range = 0.0
- gp_max_ix_mean = 0.0
- gp_auc_std = 0.0
- gp_auc_range = 0.0
- tdoa_std = 0.0
- tdoa_mean = 0.0

## Evaluation
cv = 8
### accuracy
- Scores = [ 0.4, 0.6, 0.8, 0.7777777777777778, 0.8888888888888888, 0.6666666666666666, 1.0, 0.8888888888888888 ]
- Mean = 0.7527777777777778
- Standard deviation = 0.17896737408716237

### balanced_accuracy
- Scores = [ 0.625, 0.75, 0.875, 0.6785714285714286, 0.9285714285714286, 0.7857142857142857, 1.0, 0.9375 ]
- Mean = 0.8225446428571429
- Standard deviation = 0.12503487236781471

### f1
- Scores = [ 0.4, 0.5, 0.6666666666666666, 0.5, 0.8, 0.5714285714285715, 1.0, 0.6666666666666666 ]
- Mean = 0.638095238095238
- Standard deviation = 0.17961599250040283

### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 42 | 18 |
| Actual Positive | 1 | 14 |

      