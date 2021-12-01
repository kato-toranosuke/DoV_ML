# ExtraTreesClassifier_NoResampler_2021-11-29_no2
## Constants
- CSV_PATH = ../out/csv/experiment
- OUTPUT_PATH = ../out/ml_model_result
- FEATURE_ATTRBS = ['low_power', 'high_power', 'hlbr', 'coe1[0]', 'coe1[1]', 'coe3[0]', 'coe3[1]', 'coe3[2]', 'coe3[3]', 'ratio_max_to_10ms_ave_peaks', 'ratio_max_to_9th_ave_peaks', 'ac_std', 'ac_auc', 'diff_std', 'diff_auc', 'srmr', 'gp_max_val_std', 'gp_max_val_range', 'gp_max_val_min', 'gp_max_val_max', 'gp_max_val_mean', 'gp_max_ix_std', 'gp_max_ix_range', 'gp_max_ix_min', 'gp_max_ix_max', 'gp_max_ix_mean', 'gp_auc_std', 'gp_auc_range', 'gp_auc_min', 'gp_auc_max', 'gp_auc_mean', 'tdoa_std', 'tdoa_range', 'tdoa_min', 'tdoa_max', 'tdoa_mean']
- LABEL_ATTRB = ['dov_angle']
- FACING_DOV_ANGLES = [0, 45, 315]
- NCV = 8
- SCORING = ['accuracy', 'balanced_accuracy', 'f1']
- REFIT_SCORING = balanced_accuracy
- PARAM_GRID = [{'est__n_estimators': [300, 400, 500, 600, 700, 800], 'est__min_samples_split': [2, 5, 10], 'est__min_samples_leaf': [1, 5, 10], 'est__max_features': ['sqrt', 'log2', None], 'est__bootstrap': [False], 'est__n_jobs': [-1], 'est__random_state': [42], 'est__max_samples': [0.01, 0.5, 0.09]}, {'est__n_estimators': [300, 400, 500, 600, 700, 800], 'est__min_samples_split': [2, 5, 10], 'est__min_samples_leaf': [1, 5, 10], 'est__max_features': ['sqrt', 'log2', None], 'est__bootstrap': [True], 'est__oob_score': [True, False], 'est__n_jobs': [-1], 'est__random_state': [42], 'est__max_samples': [0.01, 0.5, 0.09]}]

## Loaded CSV
- 2021-11-26_raspi_16000Hz_w1_N2^12_overlap80.csv

## Estimator
### Type
- resampler = NoResampler
- estimator = ExtraTreesClassifier

### Arguments for hyperparameter search
- resampler = NoResampler
- estimator = ExtraTreesClassifier
- param_grid = 
	- {'est__n_estimators': [300, 400, 500, 600, 700, 800], 'est__min_samples_split': [2, 5, 10], 'est__min_samples_leaf': [1, 5, 10], 'est__max_features': ['sqrt', 'log2', None], 'est__bootstrap': [False], 'est__n_jobs': [-1], 'est__random_state': [42], 'est__max_samples': [0.01, 0.5, 0.09]}
	- {'est__n_estimators': [300, 400, 500, 600, 700, 800], 'est__min_samples_split': [2, 5, 10], 'est__min_samples_leaf': [1, 5, 10], 'est__max_features': ['sqrt', 'log2', None], 'est__bootstrap': [True], 'est__oob_score': [True, False], 'est__n_jobs': [-1], 'est__random_state': [42], 'est__max_samples': [0.01, 0.5, 0.09]}

- scoring = ['accuracy', 'balanced_accuracy', 'f1']
- refit = balanced_accuracy
- cv = 8

### Parameters of the best estimator
#### The best hyper-parameters
- best_resampler

- best_estimator
	- base_estimator = ExtraTreeClassifier()
	- n_estimators = 300
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
- gp_auc_min = 0.1405747948958343
- gp_max_val_mean = 0.12630310990850743
- gp_max_val_min = 0.1256790148607653
- gp_auc_mean = 0.11970455481068243
- gp_max_val_max = 0.09293035331904771
- gp_auc_max = 0.08416085878725822
- high_power = 0.06214824697691206
- hlbr = 0.0531235445559711
- diff_std = 0.047378357946382295
- diff_auc = 0.02453466911687733
- srmr = 0.009859320616440272
- gp_auc_std = 0.00921323755168254
- gp_max_val_range = 0.008901337868824239
- gp_max_ix_max = 0.007374996564048652
- ratio_max_to_9th_ave_peaks = 0.006877546342494215
- ratio_max_to_10ms_ave_peaks = 0.0067486424801304346
- tdoa_max = 0.006710923967545915
- low_power = 0.006204067284436229
- gp_max_val_std = 0.005897282137264905
- gp_max_ix_std = 0.0047692779217301745
- gp_auc_range = 0.004725748388956044
- gp_max_ix_range = 0.004534116879000955
- coe3[3] = 0.0044347483433315954
- tdoa_range = 0.004300132832296577
- coe3[2] = 0.004027436162134019
- gp_max_ix_min = 0.00400011676517168
- gp_max_ix_mean = 0.003957668149481016
- tdoa_min = 0.003615954799401147
- tdoa_std = 0.0032307034529256754
- coe1[0] = 0.0031660786413381364
- ac_auc = 0.003127009963165184
- tdoa_mean = 0.002838825934732368
- coe1[1] = 0.002530220938521259
- ac_std = 0.0024171008367086795
- coe3[0] = 0.0
- coe3[1] = 0.0

## Evaluation
cv = 8
### accuracy
- Scores = [ 0.6666666666666666, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0 ]
- Mean = 0.9583333333333333
- Standard deviation = 0.11023963796102462

### balanced_accuracy
- Scores = [ 0.5, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0 ]
- Mean = 0.9375
- Standard deviation = 0.16535945694153692

### f1
- Scores = [ 0.8, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0 ]
- Mean = 0.975
- Standard deviation = 0.06614378277661474

### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 14 | 1 |
| Actual Positive | 0 | 9 |

      