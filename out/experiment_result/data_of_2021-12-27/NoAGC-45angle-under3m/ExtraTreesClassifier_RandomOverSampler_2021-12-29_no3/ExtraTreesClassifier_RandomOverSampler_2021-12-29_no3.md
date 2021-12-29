# ExtraTreesClassifier_RandomOverSampler_2021-12-29_no3
## Constants
- CSV_PATH = ../out/csv/experiment
- OUTPUT_PATH = ../out/experiment_result/data_of_2021-12-27/NoAGC-45angle-under3m
- FEATURE_ATTRBS = ['low_power', 'high_power', 'hlbr', 'coe1[0]', 'coe1[1]', 'coe3[0]', 'coe3[1]', 'coe3[2]', 'coe3[3]', 'ratio_max_to_10ms_ave_peaks', 'ratio_max_to_9th_ave_peaks', 'ac_std', 'ac_auc', 'diff_std', 'diff_auc', 'srmr', 'gp_max_val_std', 'gp_max_val_range', 'gp_max_val_min', 'gp_max_val_max', 'gp_max_val_mean', 'gp_max_ix_std', 'gp_max_ix_range', 'gp_max_ix_min', 'gp_max_ix_max', 'gp_max_ix_mean', 'gp_auc_std', 'gp_auc_range', 'gp_auc_min', 'gp_auc_max', 'gp_auc_mean', 'tdoa_std', 'tdoa_range', 'tdoa_min', 'tdoa_max', 'tdoa_mean']
- LABEL_ATTRB = ['facing2']
- FACING_DOV_ANGLES = [1, 2]
- NCV = 8
- SCORING = ['accuracy', 'balanced_accuracy', 'f1']
- REFIT_SCORING = balanced_accuracy
- PARAM_GRID = [{'est__n_estimators': [50, 100, 150, 200, 300], 'est__min_samples_split': [2, 5, 10], 'est__min_samples_leaf': [1, 5, 10], 'est__max_features': ['sqrt', 'log2', None], 'est__bootstrap': [False], 'est__n_jobs': [-1], 'est__random_state': [42], 'est__max_samples': [0.01, 0.5, 0.09]}, {'est__n_estimators': [50, 100, 150, 200, 300], 'est__min_samples_split': [2, 5, 10], 'est__min_samples_leaf': [1, 5, 10], 'est__max_features': ['sqrt', 'log2', None], 'est__bootstrap': [True], 'est__oob_score': [True, False], 'est__n_jobs': [-1], 'est__random_state': [42], 'est__max_samples': [0.01, 0.5, 0.09]}]
- TRAIN_SET_SESSION = ['trial1', 'trial2']
- TEST_SET_SESSION = ['trial3', 'trial4', 'trial5']
- DISTANCE = [1, 3]
- AGC_STATUS = ['NoAGC']

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
	- sampling_strategy_ = OrderedDict([(0, 8)])
	- shrinkage_ = None
	- sample_indices_ = [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23
 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47
 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71
 72 73 74 75 76 77 78 79 60 28 15 40 38 48 18 18]

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
- gp_max_val_min = 0.12200318148947407
- gp_max_val_mean = 0.11496092255207031
- gp_auc_mean = 0.09151014683726952
- gp_auc_min = 0.08790614422921482
- gp_auc_max = 0.07541516622260047
- gp_max_val_max = 0.06500735777096653
- diff_auc = 0.053362654736806146
- srmr = 0.046057811907509745
- diff_std = 0.04190663107390801
- ratio_max_to_10ms_ave_peaks = 0.04188886680742217
- high_power = 0.027520339091579298
- hlbr = 0.025765156739723072
- coe1[1] = 0.019494505207381073
- gp_max_ix_mean = 0.017535835856736622
- gp_max_ix_std = 0.014491202544069473
- tdoa_std = 0.014227512746537817
- coe1[0] = 0.013837173066014324
- tdoa_mean = 0.013659677363756118
- gp_max_val_std = 0.01266931742836439
- coe3[3] = 0.011402176056162066
- gp_auc_range = 0.011208061854156959
- gp_auc_std = 0.01019255198402359
- gp_max_ix_min = 0.008946201893362489
- low_power = 0.008730272938449099
- tdoa_range = 0.008490634450227177
- gp_max_val_range = 0.007798293747881932
- gp_max_ix_range = 0.007473037874701382
- tdoa_min = 0.005933069696777348
- tdoa_max = 0.004554016216804386
- gp_max_ix_max = 0.004418473456995537
- ac_auc = 0.0035747196765081955
- ac_std = 0.003334377021635496
- coe3[2] = 0.003170967243743355
- ratio_max_to_9th_ave_peaks = 0.001553542217166956
- coe3[0] = 0.0
- coe3[1] = 0.0

## Evaluation
cv = 8
### accuracy
- Scores = [ 0.8666666666666667, 1.0, 0.8666666666666667, 0.9333333333333333, 1.0, 1.0, 1.0, 1.0 ]
- Mean = 0.9583333333333334
- Standard deviation = 0.05713045500334202

### balanced_accuracy
- Scores = [ 0.8333333333333333, 1.0, 0.875, 0.9285714285714286, 1.0, 1.0, 1.0, 1.0 ]
- Mean = 0.9546130952380952
- Standard deviation = 0.06327030267350416

### f1
- Scores = [ 0.9, 1.0, 0.8571428571428571, 0.9411764705882353, 1.0, 1.0, 1.0, 1.0 ]
- Mean = 0.9622899159663865
- Standard deviation = 0.05302354120480989

### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 51 | 3 |
| Actual Positive | 2 | 63 |

      