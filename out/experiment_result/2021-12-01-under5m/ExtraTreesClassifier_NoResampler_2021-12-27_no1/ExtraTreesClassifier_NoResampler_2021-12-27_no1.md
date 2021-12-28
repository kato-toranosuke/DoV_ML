# ExtraTreesClassifier_NoResampler_2021-12-27_no1
## Constants
- CSV_PATH = ../out/csv/experiment
- OUTPUT_PATH = ../out/experiment_result
- FEATURE_ATTRBS = ['low_power', 'high_power', 'hlbr', 'coe1[0]', 'coe1[1]', 'coe3[0]', 'coe3[1]', 'coe3[2]', 'coe3[3]', 'ratio_max_to_10ms_ave_peaks', 'ratio_max_to_9th_ave_peaks', 'ac_std', 'ac_auc', 'diff_std', 'diff_auc', 'srmr', 'gp_max_val_std', 'gp_max_val_range', 'gp_max_val_min', 'gp_max_val_max', 'gp_max_val_mean', 'gp_max_ix_std', 'gp_max_ix_range', 'gp_max_ix_min', 'gp_max_ix_max', 'gp_max_ix_mean', 'gp_auc_std', 'gp_auc_range', 'gp_auc_min', 'gp_auc_max', 'gp_auc_mean', 'tdoa_std', 'tdoa_range', 'tdoa_min', 'tdoa_max', 'tdoa_mean']
- LABEL_ATTRB = ['dov_angle']
- FACING_DOV_ANGLES = [0]
- NCV = 8
- SCORING = ['accuracy', 'balanced_accuracy', 'f1']
- REFIT_SCORING = balanced_accuracy
- PARAM_GRID = [{'est__n_estimators': [50, 100, 150, 200, 300], 'est__min_samples_split': [2, 5, 10], 'est__min_samples_leaf': [1, 5, 10], 'est__max_features': ['sqrt', 'log2', None], 'est__bootstrap': [False], 'est__n_jobs': [-1], 'est__random_state': [42], 'est__max_samples': [0.01, 0.5, 0.09]}, {'est__n_estimators': [50, 100, 150, 200, 300], 'est__min_samples_split': [2, 5, 10], 'est__min_samples_leaf': [1, 5, 10], 'est__max_features': ['sqrt', 'log2', None], 'est__bootstrap': [True], 'est__oob_score': [True, False], 'est__n_jobs': [-1], 'est__random_state': [42], 'est__max_samples': [0.01, 0.5, 0.09]}]
- TRAIN_SET_SESSION = ['trial1']
- TEST_SET_SESSION = ['trial2', 'trial3']

## Loaded CSV
- 2021-12-01_mac_48000Hz_w1_N2^12_overlap80.csv

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
- coe1[0] = 0.05932332621342176
- coe3[3] = 0.04606146497777098
- gp_max_val_max = 0.04433063650216616
- low_power = 0.04340895436544278
- gp_auc_range = 0.04317615062687349
- gp_auc_max = 0.041968426054308595
- gp_max_val_mean = 0.04185023972058084
- gp_auc_std = 0.04133130936551305
- coe1[1] = 0.03971726187783371
- srmr = 0.038880109758566046
- ratio_max_to_9th_ave_peaks = 0.03803636417622471
- gp_max_val_range = 0.03675035276424829
- gp_auc_mean = 0.03476287642033844
- diff_auc = 0.03078581698743483
- gp_max_ix_max = 0.028410125620044337
- diff_std = 0.0271033562958837
- coe3[2] = 0.026676632756812153
- gp_max_val_std = 0.025614738550222182
- gp_auc_min = 0.02390517338027117
- gp_max_val_min = 0.023710139397583072
- gp_max_ix_mean = 0.02254365453741233
- gp_max_ix_std = 0.022384813042416966
- ac_std = 0.021372095301115883
- tdoa_mean = 0.02136022505489457
- ratio_max_to_10ms_ave_peaks = 0.021092428890748218
- high_power = 0.019354803567429576
- tdoa_min = 0.019187095474549155
- ac_auc = 0.019048611816202436
- tdoa_range = 0.01847125112671331
- gp_max_ix_min = 0.017374297326311013
- tdoa_max = 0.017351339901966658
- tdoa_std = 0.01709145669145669
- gp_max_ix_range = 0.015349422593266215
- hlbr = 0.012215048863976691
- coe3[0] = 0.0
- coe3[1] = 0.0

## Evaluation
cv = 8
### accuracy
- Scores = [ 0.9444444444444444, 0.7777777777777778, 0.7777777777777778, 0.8888888888888888, 0.8888888888888888, 0.8888888888888888, 0.9444444444444444, 0.8888888888888888 ]
- Mean = 0.875
- Standard deviation = 0.06054026310473156

### balanced_accuracy
- Scores = [ 0.8333333333333333, 0.4666666666666667, 0.4375, 0.5, 0.71875, 0.5, 0.75, 0.5 ]
- Mean = 0.58828125
- Standard deviation = 0.14323555856949516

### f1
- Scores = [ 0.8, 0.0, 0.0, 0.0, 0.5, 0.0, 0.6666666666666666, 0.0 ]
- Mean = 0.24583333333333332
- Standard deviation = 0.3261464820870797

### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 122 | 4 |
| Actual Positive | 14 | 4 |

      