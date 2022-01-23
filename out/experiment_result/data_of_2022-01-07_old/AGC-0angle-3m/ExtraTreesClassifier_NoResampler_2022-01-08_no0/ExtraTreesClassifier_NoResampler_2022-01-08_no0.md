# ExtraTreesClassifier_NoResampler_2022-01-08_no0
## Constants
- CSV_PATH = ../out/csv/experiment
- OUTPUT_PATH = ../out/experiment_result/data_of_2022-01-07/AGC-0angle-3m
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
- 2021-12-27_raspi_48000Hz_w1_N2^12_overlap80_with2022-01-07.csv

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
- high_power = 0.1448623438486701
- gp_max_val_max = 0.11196924085367056
- gp_max_val_mean = 0.10505170924355835
- gp_auc_max = 0.09996653144359191
- diff_auc = 0.08932256118686308
- gp_auc_mean = 0.08155449597673954
- gp_max_ix_mean = 0.0601661942936998
- tdoa_mean = 0.05993379697097485
- hlbr = 0.050128199569647335
- gp_auc_min = 0.04875988342505995
- gp_max_val_min = 0.04082310502404647
- diff_std = 0.024021179918629544
- coe1[1] = 0.015659606353999364
- gp_max_ix_std = 0.011061038184505068
- tdoa_std = 0.009530092847607464
- coe1[0] = 0.00580409451550606
- srmr = 0.00501735110787928
- gp_auc_std = 0.004966411292839935
- ratio_max_to_9th_ave_peaks = 0.004701272417022948
- gp_max_val_std = 0.002941835470173491
- coe3[3] = 0.0029196671981930457
- tdoa_range = 0.002742253573113622
- low_power = 0.0024705190240736754
- ac_std = 0.002340543894201857
- gp_max_val_range = 0.002285615712560684
- ac_auc = 0.0021421432335451147
- gp_max_ix_range = 0.0020307582660238806
- gp_auc_range = 0.001967914438502674
- ratio_max_to_10ms_ave_peaks = 0.0018062045451407455
- tdoa_max = 0.0011636008918617608
- coe3[2] = 0.000949803756658257
- gp_max_ix_min = 0.0006473485946102584
- tdoa_min = 0.0002926829268292685
- coe3[0] = 0.0
- coe3[1] = 0.0
- gp_max_ix_max = 0.0

## Evaluation
cv = 8
### accuracy
- Scores = [ 0.9, 1.0, 0.9, 0.8888888888888888, 0.7777777777777778, 0.8888888888888888, 0.7777777777777778, 0.8888888888888888 ]
- Mean = 0.8777777777777778
- Standard deviation = 0.06735753140545633

### balanced_accuracy
- Scores = [ 0.9375, 1.0, 0.9375, 0.75, 0.5, 0.9285714285714286, 0.5, 0.9375 ]
- Mean = 0.8113839285714286
- Standard deviation = 0.1919350839499982

### f1
- Scores = [ 0.8, 1.0, 0.8, 0.6666666666666666, 0.0, 0.8, 0.0, 0.6666666666666666 ]
- Mean = 0.5916666666666667
- Standard deviation = 0.3550234734023465

### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 56 | 4 |
| Actual Positive | 5 | 10 |

      