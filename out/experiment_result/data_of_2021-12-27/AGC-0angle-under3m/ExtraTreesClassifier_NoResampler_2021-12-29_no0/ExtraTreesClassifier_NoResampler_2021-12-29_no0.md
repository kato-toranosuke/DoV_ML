# ExtraTreesClassifier_NoResampler_2021-12-29_no0
## Constants
- CSV_PATH = ../out/csv/experiment
- OUTPUT_PATH = ../out/experiment_result/data_of_2021-12-27/AGC-0angle-under3m
- FEATURE_ATTRBS = ['low_power', 'high_power', 'hlbr', 'coe1[0]', 'coe1[1]', 'coe3[0]', 'coe3[1]', 'coe3[2]', 'coe3[3]', 'ratio_max_to_10ms_ave_peaks', 'ratio_max_to_9th_ave_peaks', 'ac_std', 'ac_auc', 'diff_std', 'diff_auc', 'srmr', 'gp_max_val_std', 'gp_max_val_range', 'gp_max_val_min', 'gp_max_val_max', 'gp_max_val_mean', 'gp_max_ix_std', 'gp_max_ix_range', 'gp_max_ix_min', 'gp_max_ix_max', 'gp_max_ix_mean', 'gp_auc_std', 'gp_auc_range', 'gp_auc_min', 'gp_auc_max', 'gp_auc_mean', 'tdoa_std', 'tdoa_range', 'tdoa_min', 'tdoa_max', 'tdoa_mean']
- LABEL_ATTRB = ['facing']
- FACING_DOV_ANGLES = [1]
- NCV = 8
- SCORING = ['accuracy', 'balanced_accuracy', 'f1']
- REFIT_SCORING = balanced_accuracy
- PARAM_GRID = [{'est__n_estimators': [50, 100, 150, 200, 300], 'est__min_samples_split': [2, 5, 10], 'est__min_samples_leaf': [1, 5, 10], 'est__max_features': ['sqrt', 'log2', None], 'est__bootstrap': [False], 'est__n_jobs': [-1], 'est__random_state': [42], 'est__max_samples': [0.01, 0.5, 0.09]}, {'est__n_estimators': [50, 100, 150, 200, 300], 'est__min_samples_split': [2, 5, 10], 'est__min_samples_leaf': [1, 5, 10], 'est__max_features': ['sqrt', 'log2', None], 'est__bootstrap': [True], 'est__oob_score': [True, False], 'est__n_jobs': [-1], 'est__random_state': [42], 'est__max_samples': [0.01, 0.5, 0.09]}]
- TRAIN_SET_SESSION = ['trial1', 'trial2']
- TEST_SET_SESSION = ['trial3', 'trial4', 'trial5']
- DISTANCE = [1, 3]
- AGC_STATUS = ['AGC']

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
	- min_samples_split = 10
	- min_samples_leaf = 1
	- min_weight_fraction_leaf = 0.0
	- max_features = None
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
- gp_max_val_min = 0.15499814462636838
- gp_auc_min = 0.14879581836727387
- gp_max_val_mean = 0.07114017564791493
- gp_auc_mean = 0.05656076414524596
- coe1[0] = 0.05511959127384978
- coe1[1] = 0.054828030671927715
- gp_auc_max = 0.04836221301002268
- gp_max_val_max = 0.039005076966471326
- low_power = 0.036608297452751244
- diff_auc = 0.03255539150889012
- high_power = 0.029946850668703454
- ratio_max_to_9th_ave_peaks = 0.02767669154661992
- srmr = 0.026187955914074638
- gp_max_ix_max = 0.02509218811381763
- diff_std = 0.02313167694365842
- gp_max_val_range = 0.02276974439208856
- ratio_max_to_10ms_ave_peaks = 0.022186951306459472
- tdoa_max = 0.021220341034395573
- ac_std = 0.01786070780415254
- gp_auc_range = 0.014291735500029564
- coe3[3] = 0.012446146065249828
- gp_auc_std = 0.008385230985614242
- hlbr = 0.008360595485731656
- ac_auc = 0.006626159546214639
- coe3[2] = 0.00644707613300768
- gp_max_val_std = 0.005917338261227461
- tdoa_mean = 0.0048622227521624645
- tdoa_range = 0.004367848852622627
- tdoa_std = 0.004106481908960647
- gp_max_ix_mean = 0.0025689972277430522
- gp_max_ix_std = 0.002409257582800963
- gp_max_ix_range = 0.002096050006470394
- gp_max_ix_min = 0.0020263648329162023
- tdoa_min = 0.0010418834645620802
- coe3[0] = 0.0
- coe3[1] = 0.0

## Evaluation
cv = 8
### accuracy
- Scores = [ 0.631578947368421, 0.5789473684210527, 0.8947368421052632, 0.7368421052631579, 0.8947368421052632, 0.8333333333333334, 0.7777777777777778, 0.7222222222222222 ]
- Mean = 0.7587719298245614
- Standard deviation = 0.10794979498230839

### balanced_accuracy
- Scores = [ 0.49166666666666664, 0.36666666666666664, 0.8416666666666667, 0.4666666666666667, 0.75, 0.8035714285714286, 0.4666666666666667, 0.43333333333333335 ]
- Mean = 0.5775297619047619
- Standard deviation = 0.17600379981580846

### f1
- Scores = [ 0.22222222222222224, 0.0, 0.75, 0.0, 0.6666666666666666, 0.6666666666666665, 0.0, 0.0 ]
- Mean = 0.2881944444444444
- Standard deviation = 0.32332709878487137

### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 104 | 15 |
| Actual Positive | 21 | 9 |

      