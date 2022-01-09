# ExtraTreesClassifier_SMOTETomek_2022-01-09_no6
## Constants
- CSV_PATH = ../out/csv/experiment
- OUTPUT_PATH = ../out/experiment_result/data_of_2022-01-07_new/AGC-45angle-3m
- FEATURE_ATTRBS = ['low_power', 'high_power', 'hlbr', 'coe1[0]', 'coe1[1]', 'coe3[0]', 'coe3[1]', 'coe3[2]', 'coe3[3]', 'ratio_max_to_10ms_ave_peaks', 'ratio_max_to_9th_ave_peaks', 'ac_std', 'ac_auc', 'diff_std', 'diff_auc', 'srmr', 'gp_max_val_std', 'gp_max_val_range', 'gp_max_val_min', 'gp_max_val_max', 'gp_max_val_mean', 'gp_max_ix_std', 'gp_max_ix_range', 'gp_max_ix_min', 'gp_max_ix_max', 'gp_max_ix_mean', 'gp_auc_std', 'gp_auc_range', 'gp_auc_min', 'gp_auc_max', 'gp_auc_mean', 'tdoa_std', 'tdoa_range', 'tdoa_min', 'tdoa_max', 'tdoa_mean']
- LABEL_ATTRB = ['facing2']
- FACING_DOV_ANGLES = [1, 2]
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
- gp_auc_max = 0.1666503238655909
- gp_max_val_max = 0.12448180605514196
- high_power = 0.11559570583283818
- gp_auc_min = 0.09682283198827317
- gp_max_val_mean = 0.08452844622697565
- gp_max_val_min = 0.05503054204137796
- gp_auc_mean = 0.0507128129980129
- diff_auc = 0.04862121212121212
- hlbr = 0.0452787013356067
- low_power = 0.04150621205419967
- srmr = 0.03837346662886776
- diff_std = 0.03560897435897436
- coe3[3] = 0.02242467499820441
- gp_max_ix_mean = 0.013292290813188647
- gp_max_val_range = 0.011233529187493381
- tdoa_std = 0.010185185185185186
- gp_auc_range = 0.009526995063759768
- coe1[1] = 0.0048517156862745115
- gp_max_val_std = 0.004728609625668449
- gp_auc_std = 0.003968253968253969
- ac_std = 0.0037839176074470206
- tdoa_range = 0.0034905445431761208
- coe3[2] = 0.0021428571428571434
- gp_max_ix_min = 0.001875
- ratio_max_to_10ms_ave_peaks = 0.0016666666666666666
- gp_max_ix_std = 0.0016666666666666666
- coe1[0] = 0.0007715017825311951
- gp_max_ix_max = 0.000625
- gp_max_ix_range = 0.0005555555555555556
- coe3[0] = 0.0
- coe3[1] = 0.0
- ratio_max_to_9th_ave_peaks = 0.0
- ac_auc = 0.0
- tdoa_min = 0.0
- tdoa_max = 0.0
- tdoa_mean = 0.0

## Evaluation
cv = 8
### accuracy
- Scores = [ 1.0, 0.9, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0 ]
- Mean = 0.9875
- Standard deviation = 0.03307189138830738

### balanced_accuracy
- Scores = [ 1.0, 0.9, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0 ]
- Mean = 0.9875
- Standard deviation = 0.03307189138830738

### f1
- Scores = [ 1.0, 0.888888888888889, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0 ]
- Mean = 0.9861111111111112
- Standard deviation = 0.03674654598700818

### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 36 | 0 |
| Actual Positive | 1 | 38 |

      