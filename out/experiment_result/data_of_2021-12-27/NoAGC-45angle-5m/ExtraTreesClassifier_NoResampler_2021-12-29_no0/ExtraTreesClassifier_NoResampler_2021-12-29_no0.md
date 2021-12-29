# ExtraTreesClassifier_NoResampler_2021-12-29_no0
## Constants
- CSV_PATH = ../out/csv/experiment
- OUTPUT_PATH = ../out/experiment_result/data_of_2021-12-27/NoAGC-45angle-5m
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
- 2021-12-27_raspi_48000Hz_w1_N2^12_overlap80_new.csv

## Estimator
### Type
- resampler = NoResampler
- estimator = ExtraTreesClassifier

### Arguments for hyperparameter search
- resampler = NoResampler
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
- gp_auc_mean = 0.13207585718765427
- gp_auc_max = 0.12116716238697992
- gp_max_val_min = 0.1172917624439161
- gp_max_val_mean = 0.10915798788595746
- gp_max_val_max = 0.10434138661286478
- gp_auc_min = 0.10384509722995199
- high_power = 0.03190750641969383
- gp_max_val_std = 0.030741507297386464
- srmr = 0.02771117453297309
- diff_auc = 0.025122462155954983
- hlbr = 0.024616645480051064
- gp_auc_std = 0.02196409182185645
- diff_std = 0.016716540439346506
- gp_auc_range = 0.014789563125554624
- gp_max_ix_max = 0.014745775647736435
- tdoa_max = 0.011337574086805536
- tdoa_range = 0.009514877939120365
- gp_max_ix_range = 0.009356552538370722
- gp_max_val_range = 0.009162052712182497
- coe1[0] = 0.008760428252939576
- coe3[3] = 0.00845276289212814
- gp_max_ix_min = 0.008197005015186835
- tdoa_min = 0.007835313494850038
- low_power = 0.006365350601187229
- ac_std = 0.00621449523363399
- coe1[1] = 0.005182505485535791
- coe3[2] = 0.0026861581819051265
- ac_auc = 0.0021668968891191114
- ratio_max_to_10ms_ave_peaks = 0.0019809857183594563
- gp_max_ix_std = 0.00160333493666827
- gp_max_ix_mean = 0.0014610623382553215
- tdoa_mean = 0.0014395289210104038
- tdoa_std = 0.0011047294746354304
- ratio_max_to_9th_ave_peaks = 0.0009838646202282569
- coe3[0] = 0.0
- coe3[1] = 0.0

## Evaluation
cv = 8
### accuracy
- Scores = [ 1.0, 1.0, 1.0, 1.0, 1.0, 0.8571428571428571, 1.0, 1.0 ]
- Mean = 0.9821428571428572
- Standard deviation = 0.047245559126153414

### balanced_accuracy
- Scores = [ 1.0, 1.0, 1.0, 1.0, 1.0, 0.875, 1.0, 1.0 ]
- Mean = 0.984375
- Standard deviation = 0.04133986423538423

### f1
- Scores = [ 1.0, 1.0, 1.0, 1.0, 1.0, 0.8571428571428571, 1.0, 1.0 ]
- Mean = 0.9821428571428572
- Standard deviation = 0.047245559126153414

### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 27 | 0 |
| Actual Positive | 1 | 32 |

      