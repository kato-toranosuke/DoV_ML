# ExtraTreesClassifier_SMOTE_2021-12-28_no4
## Constants
- CSV_PATH = ../out/csv/experiment
- OUTPUT_PATH = ../out/experiment_result/2021-12-27-5m
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
- resampler = SMOTE
- estimator = ExtraTreesClassifier

### Arguments for hyperparameter search
- resampler = SMOTE
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
	- k_neighbors = 5
	- n_jobs = -1
	- n_features_in_ = 36
	- sampling_strategy_ = OrderedDict([(1, 30)])
	- nn_k_ = NearestNeighbors(n_neighbors=6)

- best_estimator
	- base_estimator = ExtraTreeClassifier()
	- n_estimators = 200
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
	- min_samples_leaf = 10
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
- high_power = 0.15705100352067336
- gp_auc_mean = 0.152366303488993
- gp_max_val_min = 0.13562978235852985
- gp_max_val_max = 0.12257559988835222
- hlbr = 0.0994701360671135
- gp_max_val_mean = 0.09382797172729986
- gp_auc_max = 0.08779185826116204
- gp_auc_min = 0.07435050144510995
- diff_std = 0.017890046211371247
- diff_auc = 0.017770963672889176
- tdoa_mean = 0.007924987433452975
- gp_max_ix_max = 0.007167313299290768
- gp_max_ix_mean = 0.0044910485387727635
- tdoa_max = 0.004257000727062148
- srmr = 0.0041069287175597565
- gp_max_ix_range = 0.0028701346416005235
- tdoa_range = 0.0022476897558896193
- ac_std = 0.001324971150383451
- gp_max_val_std = 0.0009399696737391745
- low_power = 0.0007778445295808337
- coe1[0] = 0.0007355834585168947
- coe1[1] = 0.0007260307996903661
- ac_auc = 0.000634715025906736
- ratio_max_to_10ms_ave_peaks = 0.0005448447257939932
- ratio_max_to_9th_ave_peaks = 0.0004981252569046121
- coe3[2] = 0.00041333053746237463
- tdoa_min = 0.00036901084019436
- gp_max_ix_min = 0.00034828633551034044
- tdoa_std = 0.00027751497950173463
- gp_auc_range = 0.00026333088738331173
- gp_max_val_range = 0.0002581592759674731
- gp_auc_std = 5.4330850629998415e-05
- coe3[3] = 3.330394546588071e-05
- gp_max_ix_std = 1.1377972245732375e-05
- coe3[0] = 0.0
- coe3[1] = 0.0

## Evaluation
cv = 8
### accuracy
- Scores = [ 0.9, 0.8, 0.8, 1.0, 0.7777777777777778, 1.0, 0.8888888888888888, 0.8888888888888888 ]
- Mean = 0.8819444444444444
- Standard deviation = 0.08106876748618047

### balanced_accuracy
- Scores = [ 0.9375, 0.875, 0.6875, 1.0, 0.8571428571428572, 1.0, 0.75, 0.9375 ]
- Mean = 0.8805803571428572
- Standard deviation = 0.10601503694304744

### f1
- Scores = [ 0.8, 0.6666666666666666, 0.5, 1.0, 0.6666666666666666, 1.0, 0.6666666666666666, 0.6666666666666666 ]
- Mean = 0.7458333333333333
- Standard deviation = 0.16493896177407907

### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 53 | 7 |
| Actual Positive | 2 | 13 |

      