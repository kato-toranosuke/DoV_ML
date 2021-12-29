# ExtraTreesClassifier_SMOTETomek_2021-12-29_no6
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
- resampler = SMOTETomek
- estimator = ExtraTreesClassifier

### Arguments for hyperparameter search
- resampler = SMOTETomek
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
	- tomek = None
	- n_jobs = -1
	- n_features_in_ = 36
	- sampling_strategy_ = auto
	- smote_ = SMOTE(n_jobs=-1, random_state=42)
	- tomek_ = TomekLinks(n_jobs=-1, sampling_strategy='all')

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
- gp_auc_max = 0.13333351431326934
- gp_auc_mean = 0.11324283585202283
- gp_max_val_mean = 0.10663273580863433
- gp_auc_min = 0.10271491267353335
- gp_max_val_min = 0.09814458695759005
- gp_max_val_max = 0.0908749767188386
- high_power = 0.04979717514877698
- tdoa_max = 0.02650618436144752
- tdoa_range = 0.02629144996879551
- gp_max_ix_max = 0.025206241627085624
- gp_max_ix_range = 0.025066867927394248
- diff_auc = 0.022383333333333335
- srmr = 0.021322817945728167
- gp_max_val_std = 0.018258263305322132
- ac_std = 0.017764783140910487
- coe1[0] = 0.013568614718614721
- diff_std = 0.012462835639306228
- gp_auc_std = 0.011776470588235296
- gp_max_ix_min = 0.010935064935064936
- hlbr = 0.010817258663901133
- coe1[1] = 0.008889294848374136
- coe3[3] = 0.00803813474107592
- tdoa_min = 0.007429192546583852
- ac_auc = 0.006247138047138047
- gp_auc_range = 0.005868641659562375
- coe3[2] = 0.004352029583763332
- gp_max_val_range = 0.0039240740740740755
- gp_max_ix_mean = 0.0039047619047619057
- tdoa_mean = 0.0034637983848510184
- gp_max_ix_std = 0.0029629629629629637
- low_power = 0.002866666666666667
- tdoa_std = 0.002507936507936509
- ratio_max_to_9th_ave_peaks = 0.001777777777777778
- ratio_max_to_10ms_ave_peaks = 0.0006666666666666668
- coe3[0] = 0.0
- coe3[1] = 0.0

## Evaluation
cv = 8
### accuracy
- Scores = [ 1.0, 1.0, 0.875, 1.0, 1.0, 0.8571428571428571, 1.0, 1.0 ]
- Mean = 0.9665178571428572
- Standard deviation = 0.0581643491999794

### balanced_accuracy
- Scores = [ 1.0, 1.0, 0.875, 1.0, 1.0, 0.875, 1.0, 1.0 ]
- Mean = 0.96875
- Standard deviation = 0.05412658773652741

### f1
- Scores = [ 1.0, 1.0, 0.888888888888889, 1.0, 1.0, 0.8571428571428571, 1.0, 1.0 ]
- Mean = 0.9682539682539683
- Standard deviation = 0.05555555555555556

### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 26 | 1 |
| Actual Positive | 1 | 32 |

      