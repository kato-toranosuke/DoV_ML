# ExtraTreesClassifier_RandomUnderSampler_2022-01-10_no2
## Constants
- CSV_PATH = ../out/csv/experiment
- OUTPUT_PATH = ../out/experiment_result/data_of_2022-01-10/NoAGC-45angle-5m
- FEATURE_ATTRBS = ['low_power', 'high_power', 'hlbr', 'coe1[0]', 'coe1[1]', 'coe3[0]', 'coe3[1]', 'coe3[2]', 'coe3[3]', 'ratio_max_to_10ms_ave_peaks', 'ratio_max_to_9th_ave_peaks', 'ac_std', 'ac_auc', 'diff_std', 'diff_auc', 'srmr', 'gp_max_val_std', 'gp_max_val_range', 'gp_max_val_min', 'gp_max_val_max', 'gp_max_val_mean', 'gp_max_ix_std', 'gp_max_ix_range', 'gp_max_ix_min', 'gp_max_ix_max', 'gp_max_ix_mean', 'gp_auc_std', 'gp_auc_range', 'gp_auc_min', 'gp_auc_max', 'gp_auc_mean', 'tdoa_std', 'tdoa_range', 'tdoa_min', 'tdoa_max', 'tdoa_mean']
- LABEL_ATTRB = ['facing2']
- FACING_DOV_ANGLES = [1, 2]
- NCV = 8
- SCORING = ['accuracy', 'balanced_accuracy', 'f1']
- REFIT_SCORING = balanced_accuracy
- PARAM_GRID = [{'est__n_estimators': [50, 100, 150, 200, 300], 'est__min_samples_split': [2, 5, 10], 'est__min_samples_leaf': [1, 5, 10], 'est__max_features': ['sqrt', 'log2', None], 'est__bootstrap': [False], 'est__n_jobs': [-1], 'est__random_state': [42], 'est__max_samples': [0.01, 0.5, 0.09]}, {'est__n_estimators': [50, 100, 150, 200, 300], 'est__min_samples_split': [2, 5, 10], 'est__min_samples_leaf': [1, 5, 10], 'est__max_features': ['sqrt', 'log2', None], 'est__bootstrap': [True], 'est__oob_score': [True, False], 'est__n_jobs': [-1], 'est__random_state': [42], 'est__max_samples': [0.01, 0.5, 0.09]}]
- TRAIN_SET_SESSION = ['trial1', 'trial2']
- TEST_SET_SESSION = ['trial3', 'trial4', 'trial5']
- DISTANCE = [5]
- AGC_STATUS = ['NoAGC']

## Loaded CSV
- 2022-01-10_raspi_48000Hz_w1_N2^12_overlap80.csv

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
	- sampling_strategy_ = OrderedDict([(1, 24)])
	- sample_indices_ = [ 4  5  6  7  8  9 16 17 18 19 20 21 28 29 30 31 32 33 40 41 42 43 44 45
 14 34  0 48 23 15 25  1 47 11  2 24 27  3 10 39 35 46 36 49 38 13 22 26]

- best_estimator
	- base_estimator = ExtraTreeClassifier()
	- n_estimators = 100
	- estimator_params = ('criterion', 'max_depth', 'min_samples_split', 'min_samples_leaf', 'min_weight_fraction_leaf', 'max_features', 'max_leaf_nodes', 'min_impurity_decrease', 'random_state', 'ccp_alpha')
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
	- ccp_alpha = 0.0
	- n_features_in_ = 36
	- n_outputs_ = 1
	- classes_ = [0 1]
	- n_classes_ = 2
	- base_estimator_ = ExtraTreeClassifier()

#### Importance of features
- gp_auc_mean = 0.15140558653144234
- gp_max_val_max = 0.14668374111151275
- srmr = 0.1416260757042524
- gp_max_val_mean = 0.13576313085988317
- gp_max_val_min = 0.11909014267402222
- gp_auc_max = 0.11448088056738115
- gp_auc_min = 0.10490680585335518
- hlbr = 0.0258658160123953
- diff_std = 0.005355185185185184
- gp_max_val_range = 0.0048789196310935435
- coe3[3] = 0.004368627450980391
- coe1[1] = 0.003928104575163398
- coe3[2] = 0.003787314135140222
- diff_auc = 0.0035624999999999997
- low_power = 0.0030065181869849394
- high_power = 0.00285575396825397
- coe1[0] = 0.002799999999999999
- gp_max_ix_min = 0.0027327852099591236
- ac_auc = 0.0025393518518518534
- tdoa_range = 0.002485623374210332
- tdoa_min = 0.0023944682164950717
- gp_auc_std = 0.0023836755233494367
- gp_max_val_std = 0.0023787394645706683
- gp_auc_range = 0.002129110105580694
- ratio_max_to_9th_ave_peaks = 0.002114808894572322
- gp_max_ix_range = 0.0019533896658896653
- tdoa_std = 0.0011238095238095235
- tdoa_max = 0.001040723981900452
- gp_max_ix_max = 0.0007352941176470588
- ratio_max_to_10ms_ave_peaks = 0.0007142857142857144
- ac_std = 0.0006666666666666665
- tdoa_mean = 0.00024216524216524166
- coe3[0] = 0.0
- coe3[1] = 0.0
- gp_max_ix_std = 0.0
- gp_max_ix_mean = 0.0

## Evaluation
cv = 8
### accuracy
- Scores = [ 0.9, 0.8, 0.8, 0.7777777777777778, 0.8888888888888888, 1.0, 0.8888888888888888, 1.0 ]
- Mean = 0.8819444444444444
- Standard deviation = 0.08106876748618047

### balanced_accuracy
- Scores = [ 0.9, 0.8, 0.8, 0.8, 0.875, 1.0, 0.9, 1.0 ]
- Mean = 0.884375
- Standard deviation = 0.07799989983967927

### f1
- Scores = [ 0.9090909090909091, 0.7499999999999999, 0.8333333333333333, 0.7499999999999999, 0.9090909090909091, 1.0, 0.888888888888889, 1.0 ]
- Mean = 0.880050505050505
- Standard deviation = 0.09120672377958691

### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 34 | 2 |
| Actual Positive | 4 | 35 |

      