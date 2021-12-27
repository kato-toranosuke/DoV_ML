# ExtraTreesClassifier_ClusterCentroids_2021-12-27_no2
## Constants
- CSV_PATH = ../out/csv/experiment
- OUTPUT_PATH = ../out/experiment_result
- FEATURE_ATTRBS = ['low_power', 'high_power', 'hlbr', 'coe1[0]', 'coe1[1]', 'coe3[0]', 'coe3[1]', 'coe3[2]', 'coe3[3]', 'ratio_max_to_10ms_ave_peaks', 'ratio_max_to_9th_ave_peaks', 'ac_std', 'ac_auc', 'diff_std', 'diff_auc', 'srmr', 'gp_max_val_std', 'gp_max_val_range', 'gp_max_val_min', 'gp_max_val_max', 'gp_max_val_mean', 'gp_max_ix_std', 'gp_max_ix_range', 'gp_max_ix_min', 'gp_max_ix_max', 'gp_max_ix_mean', 'gp_auc_std', 'gp_auc_range', 'gp_auc_min', 'gp_auc_max', 'gp_auc_mean', 'tdoa_std', 'tdoa_range', 'tdoa_min', 'tdoa_max', 'tdoa_mean']
- LABEL_ATTRB = ['dov_angle']
- FACING_DOV_ANGLES = [0]
- NCV = 8
- SCORING = ['accuracy', 'balanced_accuracy', 'f1']
- REFIT_SCORING = balanced_accuracy
- PARAM_GRID = [{'est__n_estimators': [50, 100, 150, 200, 300], 'est__min_samples_split': [2, 5, 10], 'est__min_samples_leaf': [1, 5, 10], 'est__max_features': ['sqrt', 'log2', None], 'est__bootstrap': [False], 'est__n_jobs': [-1], 'est__random_state': [42], 'est__max_samples': [0.01, 0.5, 0.09]}, {'est__n_estimators': [50, 100, 150, 200, 300], 'est__min_samples_split': [2, 5, 10], 'est__min_samples_leaf': [1, 5, 10], 'est__max_features': ['sqrt', 'log2', None], 'est__bootstrap': [True], 'est__oob_score': [True, False], 'est__n_jobs': [-1], 'est__random_state': [42], 'est__max_samples': [0.01, 0.5, 0.09]}]
- TRAIN_SET_SESSION = ['trial1']
- TEST_SET_SESSION = ['trial2', 'trial3']

## Loaded CSV
- 2021-12-01_mac_48000Hz_w1_N2^12_overlap80.csv

## Estimator
### Type
- resampler = ClusterCentroids
- estimator = ExtraTreesClassifier

### Arguments for hyperparameter search
- resampler = ClusterCentroids
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
	- estimator = None
	- voting = auto
	- n_jobs = deprecated
	- n_features_in_ = 36
	- sampling_strategy_ = OrderedDict([(0, 9)])
	- estimator_ = KMeans(n_clusters=9, random_state=42)
	- voting_ = soft

- best_estimator
	- base_estimator = ExtraTreeClassifier()
	- n_estimators = 300
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
	- oob_decision_function_ = [[0.83516484 0.16483516]
 [0.84916201 0.15083799]
 [0.80701754 0.19298246]
 [0.82702703 0.17297297]
 [0.69189189 0.30810811]
 [0.90862944 0.09137056]
 [0.62275449 0.37724551]
 [0.2754491  0.7245509 ]
 [0.89534884 0.10465116]
 [0.33510638 0.66489362]
 [0.21857923 0.78142077]
 [0.35294118 0.64705882]
 [0.35       0.65      ]
 [0.38596491 0.61403509]
 [0.22093023 0.77906977]
 [0.31284916 0.68715084]
 [0.48369565 0.51630435]
 [0.81666667 0.18333333]]
	- oob_score_ = 0.8888888888888888

#### Importance of features
- tdoa_std = 0.06101488095238097
- gp_max_val_mean = 0.05461130952380953
- gp_max_ix_std = 0.05323809523809524
- tdoa_min = 0.05107380952380953
- gp_max_ix_min = 0.04542797619047619
- gp_max_val_max = 0.042632936507936516
- gp_max_val_min = 0.040066666666666674
- gp_auc_mean = 0.03791986961451248
- gp_auc_min = 0.03734126984126984
- tdoa_mean = 0.036239682539682544
- gp_auc_max = 0.03621468253968254
- gp_auc_std = 0.035996995464852605
- gp_max_ix_max = 0.03471785714285715
- gp_max_ix_range = 0.031212500000000004
- ratio_max_to_9th_ave_peaks = 0.028930555555555557
- gp_auc_range = 0.028291269841269843
- high_power = 0.026067658730158733
- coe3[3] = 0.02482698412698413
- gp_max_ix_mean = 0.02431666666666667
- tdoa_range = 0.02264384920634921
- gp_max_val_std = 0.02185912698412698
- coe1[1] = 0.02120595238095238
- diff_std = 0.020714880952380953
- gp_max_val_range = 0.02070357142857143
- coe1[0] = 0.02060059523809524
- srmr = 0.019867857142857145
- ratio_max_to_10ms_ave_peaks = 0.018571031746031745
- tdoa_max = 0.018058730158730163
- diff_auc = 0.017079166666666666
- coe3[2] = 0.016002380952380955
- hlbr = 0.014588293650793652
- low_power = 0.014235714285714286
- ac_auc = 0.013087301587301588
- ac_std = 0.010639880952380953
- coe3[0] = 0.0
- coe3[1] = 0.0

## Evaluation
cv = 8
### accuracy
- Scores = [ 0.8888888888888888, 0.7777777777777778, 0.8333333333333334, 0.8888888888888888, 0.8888888888888888, 0.8888888888888888, 0.8888888888888888, 0.8888888888888888 ]
- Mean = 0.8680555555555556
- Standard deviation = 0.03866503029743067

### balanced_accuracy
- Scores = [ 0.6666666666666666, 0.4666666666666667, 0.46875, 0.5, 0.5, 0.5, 0.5, 0.5 ]
- Mean = 0.5127604166666666
- Standard deviation = 0.059752432503657665

### f1
- Scores = [ 0.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0 ]
- Mean = 0.0625
- Standard deviation = 0.16535945694153692

### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 124 | 2 |
| Actual Positive | 17 | 1 |

      