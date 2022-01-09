# ExtraTreesClassifier_SMOTEENN_2022-01-09_no5
## Constants
- CSV_PATH = ../out/csv/experiment
- OUTPUT_PATH = ../out/experiment_result/data_of_2022-01-07_new/AGC-0angle-1m
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
- AGC_STATUS = ['AGC']

## Loaded CSV
- 2021-12-27_raspi_48000Hz_w1_N2^12_overlap80_with2022-01-07.csv

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
	- estimator_params = ('criterion', 'max_depth', 'min_samples_split', 'min_samples_leaf', 'min_weight_fraction_leaf', 'max_features', 'max_leaf_nodes', 'min_impurity_decrease', 'random_state', 'ccp_alpha')
	- bootstrap = True
	- oob_score = True
	- n_jobs = -1
	- random_state = 42
	- verbose = 0
	- warm_start = False
	- class_weight = None
	- max_samples = 0.5
	- criterion = gini
	- max_depth = None
	- min_samples_split = 5
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
	- oob_decision_function_ = [[0.2859003  0.7140997 ]
 [0.4912178  0.5087822 ]
 [0.46352986 0.53647014]
 [0.43644689 0.56355311]
 [0.75241815 0.24758185]
 [0.83314732 0.16685268]
 [0.90577078 0.09422922]
 [0.95493197 0.04506803]
 [0.85835763 0.14164237]
 [0.85087719 0.14912281]
 [0.42415515 0.57584485]
 [0.30870279 0.69129721]
 [0.30849754 0.69150246]
 [0.45326279 0.54673721]]
	- oob_score_ = 0.7142857142857143

#### Importance of features
- ac_auc = 0.09638554216867472
- srmr = 0.08433734939759037
- hlbr = 0.07228915662650603
- low_power = 0.04819277108433736
- high_power = 0.04819277108433736
- gp_max_val_max = 0.04819277108433736
- gp_auc_min = 0.04819277108433736
- ratio_max_to_9th_ave_peaks = 0.045489650911337665
- coe3[3] = 0.03614457831325302
- diff_auc = 0.03614457831325302
- gp_max_val_std = 0.03614457831325302
- gp_max_val_mean = 0.03614457831325302
- gp_max_ix_max = 0.03614457831325302
- ratio_max_to_10ms_ave_peaks = 0.03181958603645351
- gp_max_val_min = 0.031124497991967877
- coe1[0] = 0.02409638554216868
- coe1[1] = 0.02409638554216868
- ac_std = 0.02409638554216868
- gp_max_val_range = 0.02409638554216868
- gp_auc_max = 0.02409638554216868
- gp_auc_mean = 0.02409638554216868
- tdoa_std = 0.02409638554216868
- tdoa_min = 0.02409638554216868
- tdoa_max = 0.02409638554216868
- diff_std = 0.01204819277108434
- gp_max_ix_std = 0.01204819277108434
- gp_max_ix_range = 0.01204819277108434
- gp_auc_range = 0.01204819277108434
- coe3[0] = 0.0
- coe3[1] = 0.0
- coe3[2] = 0.0
- gp_max_ix_min = 0.0
- gp_max_ix_mean = 0.0
- gp_auc_std = 0.0
- tdoa_range = 0.0
- tdoa_mean = 0.0

## Evaluation
cv = 8
### accuracy
- Scores = [ 0.1, 0.8, 0.8, 0.6666666666666666, 0.8888888888888888, 0.8888888888888888, 0.7777777777777778, 0.8888888888888888 ]
- Mean = 0.7263888888888889
- Standard deviation = 0.2471402798032619

### balanced_accuracy
- Scores = [ 0.0625, 0.6875, 0.875, 0.42857142857142855, 0.75, 0.9285714285714286, 0.8571428571428572, 0.5 ]
- Mean = 0.6361607142857143
- Standard deviation = 0.27333498442704823

### f1
- Scores = [ 0.0, 0.5, 0.6666666666666666, 0.0, 0.6666666666666666, 0.8, 0.6666666666666666, 0.0 ]
- Mean = 0.4125
- Standard deviation = 0.32826881768859295

### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 46 | 14 |
| Actual Positive | 13 | 2 |

      