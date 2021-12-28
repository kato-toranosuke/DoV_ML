# ExtraTreesClassifier_RandomUnderSampler_2021-12-28_no9
## Constants
- CSV_PATH = ../out/csv/experiment
- OUTPUT_PATH = ../out/experiment_result
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
- resampler = RandomUnderSampler
- estimator = ExtraTreesClassifier

### Arguments for hyperparameter search
- resampler = RandomUnderSampler
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
	- replacement = False
	- n_features_in_ = 36
	- sampling_strategy_ = OrderedDict([(0, 10)])
	- sample_indices_ = [23 20 19 32  6 16 45 33 47  8  0  1 12 13 24 25 36 37 48 49]

- best_estimator
	- base_estimator = ExtraTreeClassifier()
	- n_estimators = 50
	- estimator_params = ('criterion', 'max_depth', 'min_samples_split', 'min_samples_leaf', 'min_weight_fraction_leaf', 'max_features', 'max_leaf_nodes', 'min_impurity_decrease', 'min_impurity_split', 'random_state', 'ccp_alpha')
	- bootstrap = True
	- oob_score = True
	- n_jobs = -1
	- random_state = 42
	- verbose = 0
	- warm_start = False
	- class_weight = None
	- max_samples = 0.5
	- criterion = gini
	- max_depth = None
	- min_samples_split = 5
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
	- oob_decision_function_ = [[0.17142857 0.82857143]
 [0.90380952 0.09619048]
 [0.89482759 0.10517241]
 [0.73958333 0.26041667]
 [0.79947917 0.20052083]
 [0.7422619  0.2577381 ]
 [0.79055556 0.20944444]
 [0.89408602 0.10591398]
 [0.15333333 0.84666667]
 [0.88611111 0.11388889]
 [0.19191919 0.80808081]
 [0.16666667 0.83333333]
 [0.10666667 0.89333333]
 [0.30740741 0.69259259]
 [0.28611111 0.71388889]
 [0.16075269 0.83924731]
 [0.18555556 0.81444444]
 [0.17916667 0.82083333]
 [0.54133333 0.45866667]
 [0.22222222 0.77777778]]
	- oob_score_ = 0.85

#### Importance of features
- gp_auc_min = 0.17684210526315788
- ratio_max_to_10ms_ave_peaks = 0.11549783549783549
- gp_auc_max = 0.11341991341991342
- gp_max_val_max = 0.08476190476190476
- gp_max_val_mean = 0.08
- srmr = 0.07999999999999999
- gp_max_val_min = 0.07649122807017544
- gp_auc_mean = 0.06457393483709273
- gp_max_val_std = 0.05399749373433584
- gp_auc_range = 0.039523809523809524
- hlbr = 0.02
- coe3[3] = 0.02
- diff_std = 0.02
- gp_max_ix_mean = 0.015151515151515154
- ac_std = 0.011428571428571429
- gp_max_ix_min = 0.008311688311688312
- ratio_max_to_9th_ave_peaks = 0.006666666666666667
- gp_max_val_range = 0.006666666666666667
- coe1[0] = 0.006666666666666666
- low_power = 0.0
- high_power = 0.0
- coe1[1] = 0.0
- coe3[0] = 0.0
- coe3[1] = 0.0
- coe3[2] = 0.0
- ac_auc = 0.0
- diff_auc = 0.0
- gp_max_ix_std = 0.0
- gp_max_ix_range = 0.0
- gp_max_ix_max = 0.0
- gp_auc_std = 0.0
- tdoa_std = 0.0
- tdoa_range = 0.0
- tdoa_min = 0.0
- tdoa_max = 0.0
- tdoa_mean = 0.0

## Evaluation
cv = 8
### accuracy
- Scores = [ 0.4, 0.6, 0.8, 0.7777777777777778, 1.0, 0.6666666666666666, 0.8888888888888888, 1.0 ]
- Mean = 0.7666666666666666
- Standard deviation = 0.19277057303219414

### balanced_accuracy
- Scores = [ 0.625, 0.75, 0.875, 0.6785714285714286, 1.0, 0.7857142857142857, 0.75, 1.0 ]
- Mean = 0.8080357142857143
- Standard deviation = 0.13023171558763233

### f1
- Scores = [ 0.4, 0.5, 0.6666666666666666, 0.5, 1.0, 0.5714285714285715, 0.6666666666666666, 1.0 ]
- Mean = 0.6630952380952381
- Standard deviation = 0.21149974670704183

### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 44 | 16 |
| Actual Positive | 2 | 13 |

      