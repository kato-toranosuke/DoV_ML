# ExtraTreesClassifier_SMOTEENN_2021-12-28_no5
## Constants
- CSV_PATH = ../out/csv/experiment
- OUTPUT_PATH = ../out/experiment_result/data_of_2021-12-27/AGC-0angle-3m
- FEATURE_ATTRBS = ['low_power', 'high_power', 'hlbr', 'coe1[0]', 'coe1[1]', 'coe3[0]', 'coe3[1]', 'coe3[2]', 'coe3[3]', 'ratio_max_to_10ms_ave_peaks', 'ratio_max_to_9th_ave_peaks', 'ac_std', 'ac_auc', 'diff_std', 'diff_auc', 'srmr', 'gp_max_val_std', 'gp_max_val_range', 'gp_max_val_min', 'gp_max_val_max', 'gp_max_val_mean', 'gp_max_ix_std', 'gp_max_ix_range', 'gp_max_ix_min', 'gp_max_ix_max', 'gp_max_ix_mean', 'gp_auc_std', 'gp_auc_range', 'gp_auc_min', 'gp_auc_max', 'gp_auc_mean', 'tdoa_std', 'tdoa_range', 'tdoa_min', 'tdoa_max', 'tdoa_mean']
- LABEL_ATTRB = ['facing']
- FACING_DOV_ANGLES = [1]
- NCV = 8
- SCORING = ['accuracy', 'balanced_accuracy', 'f1']
- REFIT_SCORING = balanced_accuracy
- PARAM_GRID = [{'est__n_estimators': [50, 100, 150, 200, 300], 'est__min_samples_split': [2, 5, 10], 'est__min_samples_leaf': [1, 5, 10], 'est__max_features': ['sqrt', 'log2', None], 'est__bootstrap': [False], 'est__n_jobs': [-1], 'est__random_state': [42], 'est__max_samples': [0.01, 0.5, 0.09]}, {'est__n_estimators': [50, 100, 150, 200, 300], 'est__min_samples_split': [2, 5, 10], 'est__min_samples_leaf': [1, 5, 10], 'est__max_features': ['sqrt', 'log2', None], 'est__bootstrap': [True], 'est__oob_score': [True, False], 'est__n_jobs': [-1], 'est__random_state': [42], 'est__max_samples': [0.01, 0.5, 0.09]}]
- TRAIN_SET_SESSION = ['trial1', 'trial2']
- TEST_SET_SESSION = ['trial3', 'trial4', 'trial5']
- DISTANCE = [3]
- AGC_STATUS = ['AGC']

## Loaded CSV
- 2021-12-27_raspi_48000Hz_w1_N2^12_overlap80_new.csv

## Estimator
### Type
- resampler = SMOTEENN
- estimator = ExtraTreesClassifier

### Arguments for hyperparameter search
- resampler = SMOTEENN
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
	- smote = None
	- enn = None
	- n_jobs = -1
	- n_features_in_ = 36
	- sampling_strategy_ = auto
	- smote_ = SMOTE(n_jobs=-1, random_state=42)
	- enn_ = EditedNearestNeighbours(n_jobs=-1, sampling_strategy='all')

- best_estimator
	- base_estimator = ExtraTreeClassifier()
	- n_estimators = 100
	- estimator_params = ('criterion', 'max_depth', 'min_samples_split', 'min_samples_leaf', 'min_weight_fraction_leaf', 'max_features', 'max_leaf_nodes', 'min_impurity_decrease', 'min_impurity_split', 'random_state', 'ccp_alpha')
	- bootstrap = True
	- oob_score = True
	- n_jobs = -1
	- random_state = 42
	- verbose = 0
	- warm_start = False
	- class_weight = None
	- max_samples = 0.09
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
	- oob_decision_function_ = [[0.7173913  0.2826087 ]
 [0.8        0.2       ]
 [0.72340426 0.27659574]
 [0.73195876 0.26804124]
 [0.66315789 0.33684211]
 [0.62105263 0.37894737]
 [0.3258427  0.6741573 ]
 [0.7173913  0.2826087 ]
 [0.8        0.2       ]
 [0.83505155 0.16494845]
 [0.78125    0.21875   ]
 [0.79569892 0.20430108]
 [0.61176471 0.38823529]
 [0.73913043 0.26086957]
 [0.64516129 0.35483871]
 [0.82608696 0.17391304]
 [0.78494624 0.21505376]
 [0.77419355 0.22580645]
 [0.73033708 0.26966292]
 [0.86956522 0.13043478]
 [0.84210526 0.15789474]
 [0.34408602 0.65591398]
 [0.34782609 0.65217391]
 [0.10227273 0.89772727]
 [0.08139535 0.91860465]
 [0.11956522 0.88043478]
 [0.14893617 0.85106383]
 [0.26666667 0.73333333]
 [0.14285714 0.85714286]
 [0.15730337 0.84269663]
 [0.24175824 0.75824176]
 [0.07954545 0.92045455]
 [0.06521739 0.93478261]
 [0.12087912 0.87912088]
 [0.04301075 0.95698925]
 [0.06315789 0.93684211]
 [0.13483146 0.86516854]
 [0.07368421 0.92631579]
 [0.08791209 0.91208791]
 [0.13186813 0.86813187]
 [0.08045977 0.91954023]
 [0.20454545 0.79545455]
 [0.05494505 0.94505495]
 [0.07608696 0.92391304]
 [0.12087912 0.87912088]
 [0.08791209 0.91208791]]
	- oob_score_ = 0.9347826086956522

#### Importance of features
- high_power = 0.13120567375886527
- ratio_max_to_10ms_ave_peaks = 0.07092198581560286
- gp_max_val_min = 0.06264775413711586
- diff_auc = 0.060283687943262415
- gp_max_val_mean = 0.060283687943262415
- low_power = 0.053191489361702135
- coe1[0] = 0.053191489361702135
- coe3[2] = 0.053191489361702135
- gp_auc_mean = 0.053191489361702135
- coe3[3] = 0.04964539007092199
- gp_auc_max = 0.03900709219858157
- gp_auc_min = 0.03191489361702128
- ratio_max_to_9th_ave_peaks = 0.024822695035460998
- gp_max_ix_std = 0.024822695035460998
- ac_std = 0.024822695035460994
- ac_auc = 0.021276595744680854
- diff_std = 0.021276595744680854
- srmr = 0.021276595744680854
- gp_max_val_std = 0.021276595744680854
- tdoa_std = 0.021276595744680854
- hlbr = 0.01773049645390071
- coe1[1] = 0.01773049645390071
- gp_max_val_max = 0.01773049645390071
- gp_auc_range = 0.015366430260047284
- gp_max_val_range = 0.010638297872340427
- tdoa_max = 0.010638297872340427
- tdoa_mean = 0.010638297872340427
- coe3[0] = 0.0
- coe3[1] = 0.0
- gp_max_ix_range = 0.0
- gp_max_ix_min = 0.0
- gp_max_ix_max = 0.0
- gp_max_ix_mean = 0.0
- gp_auc_std = 0.0
- tdoa_range = 0.0
- tdoa_min = 0.0

## Evaluation
cv = 8
### accuracy
- Scores = [ 0.8, 0.7, 0.6666666666666666, 0.4444444444444444, 0.6666666666666666, 0.8888888888888888, 0.7777777777777778, 0.3333333333333333 ]
- Mean = 0.6597222222222222
- Standard deviation = 0.17346660652773177

### balanced_accuracy
- Scores = [ 0.875, 0.8125, 0.7857142857142857, 0.6428571428571428, 0.7857142857142857, 0.75, 0.6785714285714286, 0.625 ]
- Mean = 0.7444196428571428
- Standard deviation = 0.08218863970653867

### f1
- Scores = [ 0.6666666666666666, 0.5714285714285715, 0.5714285714285715, 0.4444444444444445, 0.5714285714285715, 0.6666666666666666, 0.5, 0.25 ]
- Mean = 0.5302579365079365
- Standard deviation = 0.12704514747909254

### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 36 | 23 |
| Actual Positive | 2 | 13 |

      