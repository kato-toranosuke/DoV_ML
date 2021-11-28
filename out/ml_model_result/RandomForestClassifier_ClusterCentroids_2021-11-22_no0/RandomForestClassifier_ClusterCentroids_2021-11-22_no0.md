# RandomForestClassifier_ClusterCentroids_2021-11-22_no0
## Constants
- CSV_PATH = ../../out/csv/
- OUTPUT_PATH = ./result/
- FEATURE_ATTRBS = ['low_power', 'high_power', 'hlbr', 'coe1[0]', 'coe1[1]', 'coe3[0]', 'coe3[1]', 'coe3[2]', 'coe3[3]', 'ratio_max_to_10ms_ave_peaks', 'ratio_max_to_9th_ave_peaks', 'ac_std', 'ac_auc', 'diff_std', 'diff_auc', 'srmr', 'gp_max_val_std', 'gp_max_val_range', 'gp_max_val_mean', 'gp_max_ix_std', 'gp_max_ix_range', 'gp_max_ix_mean', 'gp_auc_std', 'gp_auc_range', 'gp_auc_mean', 'tdoa_std', 'tdoa_range', 'tdoa_mean']
- LABEL_ATTRB = ['dov_angle']
- FACING_DOV_ANGLES = [0, 45, 315]
- NCV = 10
- SCORING = ['accuracy', 'balanced_accuracy', 'f1']
- REFIT_SCORING = balanced_accuracy
- PARAM_GRID = [{'est__n_estimators': range(100, 1600, 100), 'est__min_samples_split': [2, 5, 10], 'est__min_samples_leaf': [1, 5, 10], 'est__max_features': ['sqrt', 'log2', None], 'est__bootstrap': [False], 'est__n_jobs': [-1], 'est__random_state': [42], 'est__max_samples': [0.01, 0.5, 0.09]}, {'est__n_estimators': range(100, 1600, 100), 'est__min_samples_split': [2, 5, 10], 'est__min_samples_leaf': [1, 5, 10], 'est__max_features': ['sqrt', 'log2', None], 'est__bootstrap': [True], 'est__oob_score': [True, False], 'est__n_jobs': [-1], 'est__random_state': [42], 'est__max_samples': [0.01, 0.5, 0.09]}]

## Loaded CSV
- features_mono_ch_matlab.csv

## Estimator
### Type
- resampler = ClusterCentroids
- estimator = RandomForestClassifier

### Arguments for hyperparameter search
- resampler = ClusterCentroids
- estimator = RandomForestClassifier
- param_grid = 
	- {'est__n_estimators': range(100, 1600, 100), 'est__min_samples_split': [2, 5, 10], 'est__min_samples_leaf': [1, 5, 10], 'est__max_features': ['sqrt', 'log2', None], 'est__bootstrap': [False], 'est__n_jobs': [-1], 'est__random_state': [42], 'est__max_samples': [0.01, 0.5, 0.09]}
	- {'est__n_estimators': range(100, 1600, 100), 'est__min_samples_split': [2, 5, 10], 'est__min_samples_leaf': [1, 5, 10], 'est__max_features': ['sqrt', 'log2', None], 'est__bootstrap': [True], 'est__oob_score': [True, False], 'est__n_jobs': [-1], 'est__random_state': [42], 'est__max_samples': [0.01, 0.5, 0.09]}

- scoring = ['accuracy', 'balanced_accuracy', 'f1']
- refit = balanced_accuracy
- cv = 10

### Parameters of the best estimator
#### The best hyper-parameters
- best_resampler
	- sampling_strategy = auto
	- random_state = 42
	- estimator = None
	- voting = auto
	- n_jobs = deprecated
	- n_features_in_ = 28
	- sampling_strategy_ = OrderedDict([(0, 2160)])
	- estimator_ = KMeans(n_clusters=2160, random_state=42)
	- voting_ = soft

- best_estimator
	- base_estimator = DecisionTreeClassifier()
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
	- max_features = None
	- max_leaf_nodes = None
	- min_impurity_decrease = 0.0
	- min_impurity_split = None
	- ccp_alpha = 0.0
	- n_features_in_ = 28
	- n_features_ = 28
	- n_outputs_ = 1
	- classes_ = [0 1]
	- n_classes_ = 2
	- base_estimator_ = DecisionTreeClassifier()
	- oob_decision_function_ = [[0.39393939 0.60606061]
 [0.68047337 0.31952663]
 [0.94117647 0.05882353]
 ...
 [0.38709677 0.61290323]
 [0.875      0.125     ]
 [0.78378378 0.21621622]]
	- oob_score_ = 0.8701388888888889

#### Importance of features
- gp_max_val_mean = 0.39471579598024026
- gp_max_val_range = 0.06988314365013357
- gp_auc_mean = 0.04739224409617526
- gp_max_val_std = 0.04104965724430618
- tdoa_range = 0.0324660191224477
- ratio_max_to_9th_ave_peaks = 0.029646756510156493
- srmr = 0.028995177143622475
- gp_max_ix_range = 0.027291278197926806
- ratio_max_to_10ms_ave_peaks = 0.026189389376250226
- tdoa_std = 0.02614816390078737
- gp_max_ix_std = 0.02513343381502053
- diff_auc = 0.02455257039553402
- high_power = 0.02414716095447199
- hlbr = 0.023027086577794263
- gp_auc_range = 0.023017710102148432
- gp_max_ix_mean = 0.02235334313532822
- ac_auc = 0.0218949157926069
- tdoa_mean = 0.02156697747435916
- diff_std = 0.020346660221485065
- ac_std = 0.015844287354197427
- low_power = 0.012517785455212902
- coe1[1] = 0.011893670950384063
- gp_auc_std = 0.010042043259917885
- coe3[3] = 0.009415731981682184
- coe3[2] = 0.008833759280533185
- coe1[0] = 0.0016352380272775834
- coe3[0] = 0.0
- coe3[1] = 0.0

## Evaluation
cv = 10
### accuracy
- Scores = [ 0.7447916666666666, 0.8940972222222222, 0.8645833333333334, 0.8715277777777778, 0.8489583333333334, 0.796875, 0.8402777777777778, 0.8211805555555556, 0.8645833333333334, 0.7465277777777778 ]
- Mean = 0.8293402777777779
- Standard deviation = 0.04908038617904884

### balanced_accuracy
- Scores = [ 0.7810185185185186, 0.8939814814814815, 0.8592592592592592, 0.837037037037037, 0.8263888888888888, 0.7439814814814816, 0.8518518518518519, 0.7810185185185186, 0.837962962962963, 0.6722222222222223 ]
- Mean = 0.8084722222222223
- Standard deviation = 0.06165236251073436

### f1
- Scores = [ 0.7312614259597807, 0.8635346756152125, 0.8227272727272726, 0.8031914893617021, 0.7851851851851852, 0.6628242074927955, 0.8083333333333332, 0.7223719676549865, 0.8020304568527918, 0.5259740259740259 ]
- Mean = 0.7527434040157086
- Standard deviation = 0.09337188671674569

### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 3211 | 389 |
| Actual Positive | 594 | 1566 |

      