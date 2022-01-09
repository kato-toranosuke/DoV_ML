# ExtraTreesClassifier_SMOTE_2022-01-09_no4
## Constants
- CSV_PATH = ../out/csv/experiment
- OUTPUT_PATH = ../out/experiment_result/data_of_2022-01-07_new/AGC-45angle-1m
- FEATURE_ATTRBS = ['low_power', 'high_power', 'hlbr', 'coe1[0]', 'coe1[1]', 'coe3[0]', 'coe3[1]', 'coe3[2]', 'coe3[3]', 'ratio_max_to_10ms_ave_peaks', 'ratio_max_to_9th_ave_peaks', 'ac_std', 'ac_auc', 'diff_std', 'diff_auc', 'srmr', 'gp_max_val_std', 'gp_max_val_range', 'gp_max_val_min', 'gp_max_val_max', 'gp_max_val_mean', 'gp_max_ix_std', 'gp_max_ix_range', 'gp_max_ix_min', 'gp_max_ix_max', 'gp_max_ix_mean', 'gp_auc_std', 'gp_auc_range', 'gp_auc_min', 'gp_auc_max', 'gp_auc_mean', 'tdoa_std', 'tdoa_range', 'tdoa_min', 'tdoa_max', 'tdoa_mean']
- LABEL_ATTRB = ['facing2']
- FACING_DOV_ANGLES = [1, 2]
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
	- sampling_strategy_ = OrderedDict([(0, 2)])
	- nn_k_ = NearestNeighbors(n_neighbors=6)

- best_estimator
	- base_estimator = ExtraTreeClassifier()
	- n_estimators = 150
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
	- min_samples_split = 2
	- min_samples_leaf = 5
	- min_weight_fraction_leaf = 0.0
	- max_features = sqrt
	- max_leaf_nodes = None
	- min_impurity_decrease = 0.0
	- ccp_alpha = 0.0
	- n_features_in_ = 36
	- n_outputs_ = 1
	- classes_ = [0 1]
	- n_classes_ = 2
	- base_estimator_ = ExtraTreeClassifier()

#### Importance of features
- gp_auc_max = 0.11991557673561519
- srmr = 0.10334756200484353
- gp_max_val_mean = 0.10056874112271931
- gp_max_val_min = 0.0933194068356926
- gp_max_val_max = 0.08771974271969671
- gp_auc_mean = 0.08023563211070074
- gp_auc_min = 0.06290941478421405
- hlbr = 0.05653836864615807
- ratio_max_to_10ms_ave_peaks = 0.039740858341496314
- tdoa_range = 0.0362437635429625
- gp_max_ix_range = 0.029291322946366265
- tdoa_min = 0.027221652120251606
- gp_max_ix_std = 0.024508931751818355
- gp_max_ix_min = 0.024469640231326396
- high_power = 0.0138463978831094
- tdoa_std = 0.013450157971842165
- diff_std = 0.012359778260092496
- diff_auc = 0.010740267803662808
- coe1[1] = 0.008527307455395655
- gp_max_ix_mean = 0.006731295931645313
- gp_auc_std = 0.005455625536912983
- gp_max_val_std = 0.004557788688068293
- low_power = 0.004477275018827216
- ac_auc = 0.004339970081593034
- coe1[0] = 0.004206632018006913
- coe3[3] = 0.003862862984357026
- gp_max_val_range = 0.003391583167447057
- coe3[2] = 0.003151099606921153
- gp_auc_range = 0.0031337033836167216
- tdoa_mean = 0.0031092237237868308
- gp_max_ix_max = 0.0029957259782401563
- tdoa_max = 0.0027252506813824472
- ac_std = 0.002039287288655444
- ratio_max_to_9th_ave_peaks = 0.0008681526425751477
- coe3[0] = 0.0
- coe3[1] = 0.0

## Evaluation
cv = 8
### accuracy
- Scores = [ 0.7, 1.0, 1.0, 1.0, 1.0, 1.0, 0.8888888888888888, 1.0 ]
- Mean = 0.9486111111111111
- Standard deviation = 0.10075907887286706

### balanced_accuracy
- Scores = [ 0.7, 1.0, 1.0, 1.0, 1.0, 1.0, 0.9, 1.0 ]
- Mean = 0.95
- Standard deviation = 0.1

### f1
- Scores = [ 0.7692307692307693, 1.0, 1.0, 1.0, 1.0, 1.0, 0.888888888888889, 1.0 ]
- Mean = 0.9572649572649572
- Standard deviation = 0.07983564825756154

### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 33 | 3 |
| Actual Positive | 1 | 38 |

      