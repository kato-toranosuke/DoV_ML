# ExtraTreesClassifier_NoResampler_2021-12-28_no0
## Constants
- CSV_PATH = ../out/csv/experiment
- OUTPUT_PATH = ../out/experiment_result/2021-12-27-under3m
- FEATURE_ATTRBS = ['low_power', 'high_power', 'hlbr', 'coe1[0]', 'coe1[1]', 'coe3[0]', 'coe3[1]', 'coe3[2]', 'coe3[3]', 'ratio_max_to_10ms_ave_peaks', 'ratio_max_to_9th_ave_peaks', 'ac_std', 'ac_auc', 'diff_std', 'diff_auc', 'srmr', 'gp_max_val_std', 'gp_max_val_range', 'gp_max_val_min', 'gp_max_val_max', 'gp_max_val_mean', 'gp_max_ix_std', 'gp_max_ix_range', 'gp_max_ix_min', 'gp_max_ix_max', 'gp_max_ix_mean', 'gp_auc_std', 'gp_auc_range', 'gp_auc_min', 'gp_auc_max', 'gp_auc_mean', 'tdoa_std', 'tdoa_range', 'tdoa_min', 'tdoa_max', 'tdoa_mean']
- LABEL_ATTRB = ['facing']
- FACING_DOV_ANGLES = [1]
- NCV = 8
- SCORING = ['accuracy', 'balanced_accuracy', 'f1']
- REFIT_SCORING = balanced_accuracy
- PARAM_GRID = [{'est__n_estimators': [50, 100, 150, 200, 300], 'est__min_samples_split': [2, 5, 10], 'est__min_samples_leaf': [1, 5, 10], 'est__max_features': ['sqrt', 'log2', None], 'est__bootstrap': [False], 'est__n_jobs': [-1], 'est__random_state': [42], 'est__max_samples': [0.01, 0.5, 0.09]}, {'est__n_estimators': [50, 100, 150, 200, 300], 'est__min_samples_split': [2, 5, 10], 'est__min_samples_leaf': [1, 5, 10], 'est__max_features': ['sqrt', 'log2', None], 'est__bootstrap': [True], 'est__oob_score': [True, False], 'est__n_jobs': [-1], 'est__random_state': [42], 'est__max_samples': [0.01, 0.5, 0.09]}]
- TRAIN_SET_SESSION = ['trial1', 'trial2']
- TEST_SET_SESSION = ['trial3', 'trial4', 'trial5']

## Loaded CSV
- 2021-12-27_raspi_48000Hz_w1_N2^12_overlap80_withfacing.csv

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
	- min_samples_split = 5
	- min_samples_leaf = 1
	- min_weight_fraction_leaf = 0.0
	- max_features = log2
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
- gp_auc_min = 0.0855843847674985
- gp_max_val_min = 0.06569474277828237
- gp_max_val_max = 0.058236242817395915
- gp_max_val_mean = 0.0579586533384632
- gp_auc_max = 0.057127713088728396
- gp_auc_mean = 0.04457703866748534
- high_power = 0.04436524489464786
- diff_auc = 0.037268142632999345
- coe1[0] = 0.036856679780542925
- low_power = 0.03660827958828652
- coe1[1] = 0.028953872333130296
- diff_std = 0.028946293288756503
- gp_max_ix_mean = 0.02702606927491259
- coe3[3] = 0.02507326137771937
- ac_std = 0.024845816362093286
- gp_max_val_range = 0.02292276607098955
- tdoa_mean = 0.02205816709235665
- ac_auc = 0.021897783017142753
- srmr = 0.021569005209291007
- coe3[2] = 0.02090190657781459
- gp_auc_range = 0.020858480543324367
- ratio_max_to_9th_ave_peaks = 0.020287937322765875
- gp_auc_std = 0.020141840610973686
- hlbr = 0.019651852748107067
- tdoa_std = 0.019105198346497265
- gp_max_ix_std = 0.018291337257268864
- tdoa_max = 0.018236130656908628
- ratio_max_to_10ms_ave_peaks = 0.018064063786315986
- gp_max_val_std = 0.016901476771003274
- gp_max_ix_max = 0.016165921066593758
- tdoa_range = 0.014636390630539424
- tdoa_min = 0.010096057657858393
- gp_max_ix_range = 0.009930114749789295
- gp_max_ix_min = 0.009161134893517144
- coe3[0] = 0.0
- coe3[1] = 0.0

## Evaluation
cv = 8
### accuracy
- Scores = [ 0.5789473684210527, 0.6842105263157895, 0.9473684210526315, 0.7368421052631579, 0.8947368421052632, 0.7777777777777778, 0.7777777777777778, 0.7777777777777778 ]
- Mean = 0.7719298245614035
- Standard deviation = 0.1073143234122957

### balanced_accuracy
- Scores = [ 0.4583333333333333, 0.525, 0.875, 0.4666666666666667, 0.75, 0.7678571428571428, 0.4666666666666667, 0.4666666666666667 ]
- Mean = 0.5970238095238095
- Standard deviation = 0.1601787815645133

### f1
- Scores = [ 0.2, 0.25, 0.8571428571428571, 0.0, 0.6666666666666666, 0.6, 0.0, 0.0 ]
- Mean = 0.32172619047619044
- Standard deviation = 0.31889974695993584

### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 105 | 14 |
| Actual Positive | 20 | 10 |

      