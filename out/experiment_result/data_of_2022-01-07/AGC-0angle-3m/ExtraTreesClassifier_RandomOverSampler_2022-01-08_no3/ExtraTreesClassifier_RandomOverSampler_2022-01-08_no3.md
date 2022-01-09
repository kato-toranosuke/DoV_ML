# ExtraTreesClassifier_RandomOverSampler_2022-01-08_no3
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
- resampler = RandomOverSampler
- estimator = ExtraTreesClassifier

### Arguments for hyperparameter search
- resampler = RandomOverSampler
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
	- shrinkage = None
	- n_features_in_ = 36
	- sampling_strategy_ = OrderedDict([(1, 30)])
	- shrinkage_ = None
	- sample_indices_ = [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23
 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47
 48 49 36 13 37 24 36 49 12 36 37 24 13 37 37 12 25 24  1 37 25  1 24  0
 49 25 48  0 49 12 36 13]

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
- high_power = 0.14385666834062344
- gp_auc_max = 0.12760182704078266
- gp_max_val_max = 0.09220969254315113
- gp_max_val_mean = 0.0761864890178055
- gp_auc_mean = 0.06765085692731293
- gp_auc_min = 0.05851845250883314
- diff_auc = 0.05520780603841389
- gp_max_ix_mean = 0.0331470967531208
- gp_max_val_min = 0.03160362115859139
- hlbr = 0.03129573861424804
- tdoa_mean = 0.02558980537791912
- low_power = 0.023808435096529454
- coe1[1] = 0.02268777782583569
- coe3[3] = 0.021533974003153263
- diff_std = 0.021086773942846405
- coe1[0] = 0.014948983145555199
- srmr = 0.014711552913637651
- tdoa_max = 0.013734630295351031
- gp_max_ix_range = 0.013723181647739398
- tdoa_range = 0.013028857064444715
- gp_max_ix_std = 0.01020457056554979
- gp_max_val_std = 0.010069195226403444
- coe3[2] = 0.009975063144541975
- tdoa_min = 0.009346325676499637
- gp_max_val_range = 0.007923614000930496
- gp_max_ix_min = 0.007188631008931106
- gp_auc_range = 0.006829888797042703
- ratio_max_to_9th_ave_peaks = 0.006317915388846089
- ratio_max_to_10ms_ave_peaks = 0.006063354335679319
- tdoa_std = 0.005645901727358634
- gp_auc_std = 0.005273957937847882
- ac_std = 0.0046198012510890105
- gp_max_ix_max = 0.0045394021485853555
- ac_auc = 0.0038701585347997005
- coe3[0] = 0.0
- coe3[1] = 0.0

## Evaluation
cv = 8
### accuracy
- Scores = [ 0.9, 1.0, 0.9, 0.8888888888888888, 1.0, 0.8888888888888888, 0.8888888888888888, 1.0 ]
- Mean = 0.9333333333333333
- Standard deviation = 0.05181877251716009

### balanced_accuracy
- Scores = [ 0.9375, 1.0, 0.9375, 0.75, 1.0, 0.9285714285714286, 0.75, 1.0 ]
- Mean = 0.9129464285714286
- Standard deviation = 0.09829035203707141

### f1
- Scores = [ 0.8, 1.0, 0.8, 0.6666666666666666, 1.0, 0.8, 0.6666666666666666, 1.0 ]
- Mean = 0.8416666666666667
- Standard deviation = 0.13307266185559427

### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 56 | 4 |
| Actual Positive | 3 | 12 |

      