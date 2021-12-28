# ExtraTreesClassifier_SMOTETomek_2021-12-28_no6
## Constants
- CSV_PATH = ../out/csv/experiment
- OUTPUT_PATH = ../out/experiment_result/2021-12-27-3m
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
	- min_samples_leaf = 5
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
- gp_auc_max = 0.10671595001889828
- coe1[0] = 0.08881535754387
- diff_auc = 0.08515126911016967
- gp_max_val_max = 0.08419295853773785
- high_power = 0.07278329413549318
- coe3[2] = 0.07098037217091951
- ac_std = 0.05407467432230634
- gp_auc_mean = 0.052399612645996754
- gp_max_val_mean = 0.04598102337591607
- gp_auc_min = 0.0423556820665734
- gp_max_val_min = 0.03841983480386537
- hlbr = 0.037444216203960025
- low_power = 0.03624939701097736
- coe1[1] = 0.03571951004564266
- diff_std = 0.03212765900887637
- gp_max_ix_mean = 0.02643843122177216
- coe3[3] = 0.020756864006478064
- tdoa_mean = 0.015605713018648862
- srmr = 0.015008971632876232
- gp_max_val_std = 0.0078010462916665805
- gp_auc_range = 0.007145963820637262
- ac_auc = 0.00514270461084165
- tdoa_std = 0.004895316137284338
- gp_max_val_range = 0.003947915928132002
- gp_auc_std = 0.003105765636003828
- ratio_max_to_9th_ave_peaks = 0.0022101882305033574
- gp_max_ix_std = 0.0018479363993872506
- tdoa_max = 0.0015482439152080065
- ratio_max_to_10ms_ave_peaks = 0.0011341281493575334
- coe3[0] = 0.0
- coe3[1] = 0.0
- gp_max_ix_range = 0.0
- gp_max_ix_min = 0.0
- gp_max_ix_max = 0.0
- tdoa_range = 0.0
- tdoa_min = 0.0

## Evaluation
cv = 8
### accuracy
- Scores = [ 0.8, 1.0, 0.8888888888888888, 1.0, 0.7777777777777778, 1.0, 0.7777777777777778, 0.6666666666666666 ]
- Mean = 0.8638888888888889
- Standard deviation = 0.11937982748302388

### balanced_accuracy
- Scores = [ 0.875, 1.0, 0.9285714285714286, 1.0, 0.8571428571428572, 1.0, 0.6785714285714286, 0.8125 ]
- Mean = 0.8939732142857143
- Standard deviation = 0.1058739499953957

### f1
- Scores = [ 0.6666666666666666, 1.0, 0.8, 1.0, 0.6666666666666666, 1.0, 0.5, 0.4 ]
- Mean = 0.7541666666666667
- Standard deviation = 0.220439901106855

### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 50 | 9 |
| Actual Positive | 1 | 14 |

      