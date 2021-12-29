# ExtraTreesClassifier_RandomOverSampler_2021-12-28_no3
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
	- sampling_strategy_ = OrderedDict([(1, 28)])
	- shrinkage_ = None
	- sample_indices_ = [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23
 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47
 36 13 37 24 36 47 12 36 37 24 13 37 37 12 25 24  1 37 25  1 24  0 47 25
 46  0 47 12]

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
	- min_samples_leaf = 5
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
- gp_max_val_max = 0.08868379480485458
- gp_auc_max = 0.07635471913995175
- diff_auc = 0.06622707585906787
- diff_std = 0.060476440331505184
- gp_max_val_min = 0.06047624071016058
- gp_max_val_mean = 0.06009557343340283
- coe1[0] = 0.05227966306550134
- gp_auc_mean = 0.04815000061397452
- gp_auc_min = 0.04585168500579296
- coe3[3] = 0.04494319865505193
- high_power = 0.04329237644840792
- coe3[2] = 0.04209845148049413
- coe1[1] = 0.03863291193801933
- ac_std = 0.035410747130256395
- hlbr = 0.03266540306015693
- low_power = 0.029748964221129274
- tdoa_mean = 0.021285049437066633
- srmr = 0.02044212541511817
- gp_max_ix_mean = 0.01883551929452686
- ac_auc = 0.01731422617792001
- tdoa_std = 0.013169590284184967
- gp_max_ix_max = 0.01106573945296844
- gp_auc_range = 0.009868300901204705
- ratio_max_to_9th_ave_peaks = 0.009733573087039782
- gp_max_val_range = 0.009301726502058152
- gp_max_ix_std = 0.008424905861573479
- tdoa_max = 0.008022964215084761
- gp_max_val_std = 0.006921449158495001
- gp_max_ix_range = 0.005189296617760541
- gp_auc_std = 0.00509215850638349
- ratio_max_to_10ms_ave_peaks = 0.005076054879008039
- tdoa_range = 0.00487007431187959
- coe3[0] = 0.0
- coe3[1] = 0.0
- gp_max_ix_min = 0.0
- tdoa_min = 0.0

## Evaluation
cv = 8
### accuracy
- Scores = [ 0.8, 0.9, 0.8888888888888888, 1.0, 0.8888888888888888, 0.8888888888888888, 0.6666666666666666, 0.7777777777777778 ]
- Mean = 0.851388888888889
- Standard deviation = 0.09410683120269403

### balanced_accuracy
- Scores = [ 0.875, 0.75, 0.9285714285714286, 1.0, 0.9285714285714286, 0.75, 0.42857142857142855, 0.875 ]
- Mean = 0.8169642857142858
- Standard deviation = 0.16769321402672277

### f1
- Scores = [ 0.6666666666666666, 0.6666666666666666, 0.8, 1.0, 0.8, 0.6666666666666666, 0.0, 0.5 ]
- Mean = 0.6375
- Standard deviation = 0.2766051638467125

### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 52 | 7 |
| Actual Positive | 4 | 11 |

      