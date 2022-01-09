# ExtraTreesClassifier_SMOTE_2022-01-09_no4
## Constants
- CSV_PATH = ../out/csv/experiment
- OUTPUT_PATH = ../out/experiment_result/data_of_2022-01-07_new/AGC-45angle-under3m
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
	- sampling_strategy_ = OrderedDict([(0, 4)])
	- nn_k_ = NearestNeighbors(n_neighbors=6)

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
	- min_samples_leaf = 10
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
- gp_max_val_min = 0.2713978137890724
- gp_auc_min = 0.17680792237980983
- gp_max_val_mean = 0.1604627954089407
- gp_auc_mean = 0.12414261444850283
- srmr = 0.0713748923743882
- gp_max_val_max = 0.0669437267415617
- gp_auc_max = 0.044415451364068013
- diff_std = 0.018137898789061795
- diff_auc = 0.016406156679971362
- coe1[1] = 0.013719850194861933
- hlbr = 0.008941881093058856
- coe1[0] = 0.005660166912376724
- high_power = 0.00291526190988832
- coe3[3] = 0.0025645002762578768
- ac_std = 0.002273637189711677
- gp_auc_std = 0.0022301429354555195
- gp_max_ix_mean = 0.001873796637017832
- gp_max_val_range = 0.0016539381150517689
- coe3[2] = 0.0014631800443328936
- gp_max_val_std = 0.0011137946743528758
- ratio_max_to_10ms_ave_peaks = 0.0009278499460249966
- gp_auc_range = 0.0008160700084296294
- ac_auc = 0.000677520045390871
- tdoa_mean = 0.0006718802257164289
- tdoa_max = 0.0005578295414356598
- ratio_max_to_9th_ave_peaks = 0.00045756423917460225
- low_power = 0.0004490240200829485
- tdoa_min = 0.00032524526155526166
- gp_max_ix_min = 0.00028169761484493475
- gp_max_ix_max = 0.0002775243771412353
- tdoa_std = 3.4084074049322515e-05
- gp_max_ix_std = 2.428868841082594e-05
- coe3[0] = 0.0
- coe3[1] = 0.0
- gp_max_ix_range = 0.0
- tdoa_range = 0.0

## Evaluation
cv = 8
### accuracy
- Scores = [ 0.8421052631578947, 1.0, 1.0, 0.8947368421052632, 1.0, 1.0, 1.0, 1.0 ]
- Mean = 0.9671052631578947
- Standard deviation = 0.0584749632718131

### balanced_accuracy
- Scores = [ 0.8333333333333333, 1.0, 1.0, 0.8888888888888888, 1.0, 1.0, 1.0, 1.0 ]
- Mean = 0.9652777777777778
- Standard deviation = 0.0617235723424694

### f1
- Scores = [ 0.8695652173913044, 1.0, 1.0, 0.9090909090909091, 1.0, 1.0, 1.0, 1.0 ]
- Mean = 0.9723320158102767
- Standard deviation = 0.04893050752229226

### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 69 | 3 |
| Actual Positive | 1 | 77 |

      