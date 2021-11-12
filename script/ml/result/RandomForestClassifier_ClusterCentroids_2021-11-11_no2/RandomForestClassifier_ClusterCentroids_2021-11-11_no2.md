# RandomForestClassifier_ClusterCentroids_2021-11-11_no2
## Constants
- CSV_PATH = ../../out/csv/
- OUTPUT_PATH = ./result/
- FEATURE_ATTRBS = ['low_power', 'high_power', 'hlbr', 'coe1[0]', 'coe1[1]', 'coe3[0]', 'coe3[1]', 'coe3[2]', 'coe3[3]', 'ratio_max_to_10ms_ave_peaks', 'ratio_max_to_9th_ave_peaks', 'ac_std', 'ac_auc', 'diff_std', 'diff_auc', 'srmr', 'gp_max_val_std', 'gp_max_val_range', 'gp_max_val_min', 'gp_max_val_max', 'gp_max_val_mean', 'gp_max_ix_std', 'gp_max_ix_range', 'gp_max_ix_min', 'gp_max_ix_max', 'gp_max_ix_mean', 'gp_auc_std', 'gp_auc_range', 'gp_auc_min', 'gp_auc_max', 'gp_auc_mean', 'tdoa_std', 'tdoa_range', 'tdoa_min', 'tdoa_max', 'tdoa_mean']
- LABEL_ATTRB = ['dov_angle']
- FACING_DOV_ANGLES = [0, 45, 315]
- NCV = 10
- SCORING = ['accuracy', 'balanced_accuracy', 'f1']
- REFIT_SCORING = balanced_accuracy
- PARAM_GRID = [{'est__n_estimators': [10, 100, 500, 800, 1000], 'est__min_samples_split': [2, 5, 10], 'est__min_samples_leaf': [1, 5, 10], 'est__max_features': ['sqrt', 'log2', None], 'est__bootstrap': [False], 'est__n_jobs': [-1], 'est__random_state': [42], 'est__max_samples': [0.01, 0.5, 0.09]}, {'est__n_estimators': [10, 100, 500, 800, 1000], 'est__min_samples_split': [2, 5, 10], 'est__min_samples_leaf': [1, 5, 10], 'est__max_features': ['sqrt', 'log2', None], 'est__bootstrap': [True], 'est__oob_score': [True, False], 'est__n_jobs': [-1], 'est__random_state': [42], 'est__max_samples': [0.01, 0.5, 0.09]}]

## Loaded CSV
- features_mono_ch_python.csv

## Estimator
### Type
- resampler = ClusterCentroids
- estimator = RandomForestClassifier

### Arguments for hyperparameter search
- resampler = ClusterCentroids
- estimator = RandomForestClassifier
- param_grid = 
	- {'est__n_estimators': [10, 100, 500, 800, 1000], 'est__min_samples_split': [2, 5, 10], 'est__min_samples_leaf': [1, 5, 10], 'est__max_features': ['sqrt', 'log2', None], 'est__bootstrap': [False], 'est__n_jobs': [-1], 'est__random_state': [42], 'est__max_samples': [0.01, 0.5, 0.09]}
	- {'est__n_estimators': [10, 100, 500, 800, 1000], 'est__min_samples_split': [2, 5, 10], 'est__min_samples_leaf': [1, 5, 10], 'est__max_features': ['sqrt', 'log2', None], 'est__bootstrap': [True], 'est__oob_score': [True, False], 'est__n_jobs': [-1], 'est__random_state': [42], 'est__max_samples': [0.01, 0.5, 0.09]}

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
	- n_features_in_ = 36
	- sampling_strategy_ = OrderedDict([(0, 2160)])
	- estimator_ = KMeans(n_clusters=2160, random_state=42)
	- voting_ = soft

- best_estimator
	- base_estimator = DecisionTreeClassifier()
	- n_estimators = 1000
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
	- base_estimator_ = DecisionTreeClassifier()

#### Importance of features
- gp_max_val_max = 0.11686452818930489
- gp_max_val_mean = 0.10602226806841729
- gp_auc_max = 0.05734200836096587
- gp_max_val_range = 0.05556665157836469
- gp_max_val_min = 0.051594576133518734
- gp_max_ix_std = 0.03964633097688454
- gp_max_val_std = 0.03925698898327443
- gp_max_ix_mean = 0.036076147991996696
- high_power = 0.03601714894909675
- tdoa_mean = 0.03341406860450049
- tdoa_std = 0.030647768847514315
- hlbr = 0.02823453431540968
- gp_max_ix_range = 0.026744893216144785
- tdoa_range = 0.026554491315389332
- diff_std = 0.024740936300645736
- gp_auc_mean = 0.024611579999163663
- tdoa_max = 0.021490090588267074
- tdoa_min = 0.02102335178697979
- gp_max_ix_min = 0.020928720656421238
- gp_max_ix_max = 0.020745589646892056
- srmr = 0.01995237545988388
- ratio_max_to_10ms_ave_peaks = 0.01704815198488745
- diff_auc = 0.016158194356339674
- ratio_max_to_9th_ave_peaks = 0.01607594071522433
- ac_auc = 0.016003845617468284
- gp_auc_min = 0.015317363532476765
- coe1[1] = 0.014510892625561794
- ac_std = 0.014467360730471742
- low_power = 0.013823407132701021
- coe3[3] = 0.013205572797261892
- coe3[2] = 0.010601120215826945
- gp_auc_range = 0.008639350066806061
- gp_auc_std = 0.0042259823321414165
- coe1[0] = 0.0024477679237967483
- coe3[0] = 0.0
- coe3[1] = 0.0

## Evaluation
cv = 10
### accuracy
- Scores = [ 0.7621527777777778, 0.8784722222222222, 0.8854166666666666, 0.8524305555555556, 0.8663194444444444, 0.8055555555555556, 0.8524305555555556, 0.8177083333333334, 0.8784722222222222, 0.7638888888888888 ]
- Mean = 0.8362847222222222
- Standard deviation = 0.04407158320702192

### balanced_accuracy
- Scores = [ 0.7986111111111112, 0.8722222222222222, 0.8768518518518518, 0.8217592592592593, 0.8458333333333333, 0.7620370370370371, 0.8662037037037037, 0.7865740740740741, 0.8657407407407407, 0.6925925925925925 ]
- Mean = 0.8188425925925926
- Standard deviation = 0.05657780569010978

### f1
- Scores = [ 0.7486238532110092, 0.8394495412844037, 0.8465116279069766, 0.7803617571059431, 0.8108108108108107, 0.6939890710382514, 0.824016563146998, 0.7314578005115089, 0.8341232227488151, 0.5641025641025641 ]
- Mean = 0.767344681186728
- Standard deviation = 0.08338050258458303

### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 3199 | 401 |
| Actual Positive | 542 | 1618 |

      