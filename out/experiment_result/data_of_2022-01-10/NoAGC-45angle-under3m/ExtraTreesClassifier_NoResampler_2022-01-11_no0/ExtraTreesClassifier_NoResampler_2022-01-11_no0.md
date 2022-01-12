# ExtraTreesClassifier_NoResampler_2022-01-11_no0
## Constants
- CSV_PATH = ../out/csv/experiment
- OUTPUT_PATH = ../out/experiment_result/data_of_2022-01-10/NoAGC-45angle-under3m
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
- 2022-01-10_raspi_48000Hz_w1_N2^12_overlap80.csv

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
	- min_samples_split = 2
	- min_samples_leaf = 1
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
- gp_max_val_mean = 0.13165508673887535
- gp_max_val_min = 0.12014430905356126
- gp_auc_min = 0.11416960304997764
- gp_auc_mean = 0.10512161860588354
- gp_auc_max = 0.10179704168880481
- gp_max_val_max = 0.06671643112902777
- srmr = 0.04603771896158069
- tdoa_mean = 0.026851626043321346
- hlbr = 0.023208138716950613
- tdoa_std = 0.02238517042953802
- ratio_max_to_10ms_ave_peaks = 0.02144312190424024
- gp_max_ix_mean = 0.019838960396759205
- gp_max_ix_std = 0.019672931517068958
- gp_max_ix_min = 0.016268565147210222
- tdoa_min = 0.01556871880036433
- gp_auc_range = 0.015469798984652193
- tdoa_range = 0.01448092779422513
- gp_max_ix_range = 0.013481389018519167
- diff_std = 0.012207354166174456
- gp_max_val_range = 0.011441090384340416
- diff_auc = 0.009942947370117142
- tdoa_max = 0.009734310027531294
- gp_max_val_std = 0.008554105573553395
- gp_auc_std = 0.008421830758617124
- high_power = 0.007790259902371637
- low_power = 0.005975988409728994
- gp_max_ix_max = 0.0055169250856970525
- ratio_max_to_9th_ave_peaks = 0.004983619235803535
- ac_auc = 0.00449995337167241
- coe3[2] = 0.004088210689773188
- coe3[3] = 0.003738943792195638
- coe1[0] = 0.0037105664109473844
- ac_std = 0.002927837010116327
- coe1[1] = 0.002154899830799344
- coe3[0] = 0.0
- coe3[1] = 0.0

## Evaluation
cv = 8
### accuracy
- Scores = [ 1.0, 1.0, 1.0, 0.9473684210526315, 1.0, 1.0, 0.8888888888888888, 1.0 ]
- Mean = 0.97953216374269
- Standard deviation = 0.038347593709368445

### balanced_accuracy
- Scores = [ 1.0, 1.0, 1.0, 0.95, 1.0, 1.0, 0.8888888888888888, 1.0 ]
- Mean = 0.9798611111111111
- Standard deviation = 0.03808063853015334

### f1
- Scores = [ 1.0, 1.0, 1.0, 0.9473684210526316, 1.0, 1.0, 0.9, 1.0 ]
- Mean = 0.980921052631579
- Standard deviation = 0.03510347782093183

### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 69 | 3 |
| Actual Positive | 1 | 77 |

      