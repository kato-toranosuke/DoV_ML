# ExtraTreesClassifier_RandomUnderSampler_2022-01-08_no2
## Constants
- CSV_PATH = ../out/csv/experiment
- OUTPUT_PATH = ../out/experiment_result/data_of_2022-01-07/AGC-0angle-3m
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
	- sampling_strategy_ = OrderedDict([(0, 10)])
	- sample_indices_ = [23 20 19 32  6 16 45 33 47  8  0  1 12 13 24 25 36 37 48 49]

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
- high_power = 0.1623843000137118
- gp_auc_max = 0.16047890671420084
- gp_max_val_max = 0.12049786096256683
- gp_max_val_mean = 0.10033804855275441
- gp_auc_min = 0.08235431235431236
- hlbr = 0.05115728715728716
- gp_max_val_min = 0.05071979458450047
- diff_auc = 0.04616666666666666
- gp_auc_mean = 0.04042441218911808
- srmr = 0.023030303030303026
- gp_max_val_range = 0.02206965811965812
- low_power = 0.019543026907732793
- diff_std = 0.017761904761904763
- gp_max_ix_range = 0.014453229123817362
- tdoa_min = 0.012312240047534168
- tdoa_range = 0.010715966386554627
- tdoa_std = 0.009944733044733044
- gp_auc_range = 0.00918850038850039
- gp_max_ix_mean = 0.008222222222222221
- coe1[0] = 0.006626262626262628
- gp_auc_std = 0.006196078431372551
- gp_max_ix_std = 0.005222222222222222
- gp_max_ix_min = 0.005192810457516338
- ac_auc = 0.0040888888888888884
- gp_max_val_std = 0.004029411764705884
- coe1[1] = 0.00342063492063492
- tdoa_max = 0.0025714285714285704
- ratio_max_to_9th_ave_peaks = 0.0008888888888888889
- coe3[0] = 0.0
- coe3[1] = 0.0
- coe3[2] = 0.0
- coe3[3] = 0.0
- ratio_max_to_10ms_ave_peaks = 0.0
- ac_std = 0.0
- gp_max_ix_max = 0.0
- tdoa_mean = 0.0

## Evaluation
cv = 8
### accuracy
- Scores = [ 0.9, 0.9, 0.8, 0.8888888888888888, 0.8888888888888888, 0.8888888888888888, 0.7777777777777778, 0.6666666666666666 ]
- Mean = 0.8388888888888889
- Standard deviation = 0.07895928001973276

### balanced_accuracy
- Scores = [ 0.9375, 0.9375, 0.875, 0.9285714285714286, 0.9285714285714286, 0.9285714285714286, 0.6785714285714286, 0.8125 ]
- Mean = 0.8783482142857143
- Standard deviation = 0.08574886532762103

### f1
- Scores = [ 0.8, 0.8, 0.6666666666666666, 0.8, 0.8, 0.8, 0.5, 0.4 ]
- Mean = 0.6958333333333333
- Standard deviation = 0.15040454706483372

### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 44 | 16 |
| Actual Positive | 0 | 15 |

      