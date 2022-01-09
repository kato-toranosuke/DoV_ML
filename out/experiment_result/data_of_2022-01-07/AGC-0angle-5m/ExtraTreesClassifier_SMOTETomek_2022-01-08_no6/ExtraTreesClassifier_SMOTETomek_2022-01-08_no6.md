# ExtraTreesClassifier_SMOTETomek_2022-01-08_no6
## Constants
- CSV_PATH = ../out/csv/experiment
- OUTPUT_PATH = ../out/experiment_result/data_of_2022-01-07/AGC-0angle-5m
- FEATURE_ATTRBS = ['low_power', 'high_power', 'hlbr', 'coe1[0]', 'coe1[1]', 'coe3[0]', 'coe3[1]', 'coe3[2]', 'coe3[3]', 'ratio_max_to_10ms_ave_peaks', 'ratio_max_to_9th_ave_peaks', 'ac_std', 'ac_auc', 'diff_std', 'diff_auc', 'srmr', 'gp_max_val_std', 'gp_max_val_range', 'gp_max_val_min', 'gp_max_val_max', 'gp_max_val_mean', 'gp_max_ix_std', 'gp_max_ix_range', 'gp_max_ix_min', 'gp_max_ix_max', 'gp_max_ix_mean', 'gp_auc_std', 'gp_auc_range', 'gp_auc_min', 'gp_auc_max', 'gp_auc_mean', 'tdoa_std', 'tdoa_range', 'tdoa_min', 'tdoa_max', 'tdoa_mean']
- LABEL_ATTRB = ['facing']
- FACING_DOV_ANGLES = [1]
- NCV = 8
- SCORING = ['accuracy', 'balanced_accuracy', 'f1']
- REFIT_SCORING = balanced_accuracy
- PARAM_GRID = [{'est__n_estimators': [50, 100, 150, 200, 300], 'est__min_samples_split': [2, 5, 10], 'est__min_samples_leaf': [1, 5, 10], 'est__max_features': ['sqrt', 'log2', None], 'est__bootstrap': [False], 'est__n_jobs': [-1], 'est__random_state': [42], 'est__max_samples': [0.01, 0.5, 0.09]}, {'est__n_estimators': [50, 100, 150, 200, 300], 'est__min_samples_split': [2, 5, 10], 'est__min_samples_leaf': [1, 5, 10], 'est__max_features': ['sqrt', 'log2', None], 'est__bootstrap': [True], 'est__oob_score': [True, False], 'est__n_jobs': [-1], 'est__random_state': [42], 'est__max_samples': [0.01, 0.5, 0.09]}]
- TRAIN_SET_SESSION = ['trial1', 'trial2']
- TEST_SET_SESSION = ['trial3', 'trial4', 'trial5']
- DISTANCE = [5]
- AGC_STATUS = ['AGC']

## Loaded CSV
- 2021-12-27_raspi_48000Hz_w1_N2^12_overlap80_with2022-01-07.csv

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
- gp_max_val_max = 0.25240419483136173
- gp_max_val_mean = 0.17975590209983996
- gp_auc_max = 0.15085851086987837
- gp_auc_mean = 0.09825986474266936
- gp_auc_min = 0.08782753519373629
- gp_max_val_min = 0.0777160453395449
- hlbr = 0.06536930635441529
- high_power = 0.03871058099790216
- diff_auc = 0.02040740844103044
- gp_auc_range = 0.0038526041893467353
- gp_max_ix_max = 0.0032260237779177053
- tdoa_max = 0.0028742313074311588
- gp_auc_std = 0.0020161878204697377
- srmr = 0.0019791209538349334
- diff_std = 0.0018306552087407723
- gp_max_ix_range = 0.0017857573189571834
- coe1[1] = 0.001672248647608312
- tdoa_mean = 0.0015589761282360896
- ac_std = 0.0012408185115963379
- ratio_max_to_10ms_ave_peaks = 0.0009895473071137456
- ratio_max_to_9th_ave_peaks = 0.0009677419354838719
- gp_max_val_std = 0.0009447128287708001
- gp_max_val_range = 0.0008996197782099181
- coe1[0] = 0.0007971303308090866
- tdoa_range = 0.0007745425354972824
- low_power = 0.0007393162393162395
- tdoa_min = 0.0005414163102817552
- coe3[0] = 0.0
- coe3[1] = 0.0
- coe3[2] = 0.0
- coe3[3] = 0.0
- ac_auc = 0.0
- gp_max_ix_std = 0.0
- gp_max_ix_min = 0.0
- gp_max_ix_mean = 0.0
- tdoa_std = 0.0

## Evaluation
cv = 8
### accuracy
- Scores = [ 0.9, 0.8, 0.7, 1.0, 0.7777777777777778, 1.0, 1.0, 0.8888888888888888 ]
- Mean = 0.8833333333333333
- Standard deviation = 0.1077262190536962

### balanced_accuracy
- Scores = [ 0.9375, 0.875, 0.625, 1.0, 0.8571428571428572, 1.0, 1.0, 0.9375 ]
- Mean = 0.9040178571428572
- Standard deviation = 0.117670137081225

### f1
- Scores = [ 0.8, 0.6666666666666666, 0.4, 1.0, 0.6666666666666666, 1.0, 1.0, 0.6666666666666666 ]
- Mean = 0.7749999999999999
- Standard deviation = 0.2025874296857203

### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 54 | 6 |
| Actual Positive | 2 | 13 |

      