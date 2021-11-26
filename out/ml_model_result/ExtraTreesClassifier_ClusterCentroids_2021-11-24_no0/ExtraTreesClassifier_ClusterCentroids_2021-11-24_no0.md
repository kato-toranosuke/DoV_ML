# ExtraTreesClassifier_ClusterCentroids_2021-11-24_no0
## Constants
- DATASET_PATH = None
- CSV_PATH = ../out/csv
- OUTPUT_PATH = ../out/ml_model_result
- FEATURE_ATTRBS = ['low_power', 'high_power', 'hlbr', 'coe1[0]', 'coe1[1]', 'coe3[0]', 'coe3[1]', 'coe3[2]', 'coe3[3]', 'ratio_max_to_10ms_ave_peaks', 'ratio_max_to_9th_ave_peaks', 'ac_std', 'ac_auc', 'diff_std', 'diff_auc', 'srmr', 'gp_max_val_std', 'gp_max_val_range', 'gp_max_val_min', 'gp_max_val_max', 'gp_max_val_mean', 'gp_max_ix_std', 'gp_max_ix_range', 'gp_max_ix_min', 'gp_max_ix_max', 'gp_max_ix_mean', 'gp_auc_std', 'gp_auc_range', 'gp_auc_min', 'gp_auc_max', 'gp_auc_mean', 'tdoa_std', 'tdoa_range', 'tdoa_min', 'tdoa_max', 'tdoa_mean']
- LABEL_ATTRB = ['dov_angle']
- FACING_DOV_ANGLES = [0]
- NCV = 10
- SCORING = ['accuracy', 'balanced_accuracy', 'f1']
- REFIT_SCORING = balanced_accuracy
- PARAM_GRID = [{'est__n_estimators': range(100, 1600, 100), 'est__min_samples_split': [2, 5, 10], 'est__min_samples_leaf': [1, 5, 10], 'est__max_features': ['sqrt', 'log2', None], 'est__bootstrap': [False], 'est__n_jobs': [-1], 'est__random_state': [42], 'est__max_samples': [0.01, 0.5, 0.09]}, {'est__n_estimators': range(100, 1600, 100), 'est__min_samples_split': [2, 5, 10], 'est__min_samples_leaf': [1, 5, 10], 'est__max_features': ['sqrt', 'log2', None], 'est__bootstrap': [True], 'est__oob_score': [True, False], 'est__n_jobs': [-1], 'est__random_state': [42], 'est__max_samples': [0.01, 0.5, 0.09]}]

## Loaded CSV
- features_matlab.csv

## Estimator
### Type
- resampler = ClusterCentroids
- estimator = ExtraTreesClassifier

### Arguments for hyperparameter search
- resampler = ClusterCentroids
- estimator = ExtraTreesClassifier
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
	- n_features_in_ = 36
	- sampling_strategy_ = OrderedDict([(0, 720)])
	- estimator_ = KMeans(n_clusters=720, random_state=42)
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
	- max_samples = 0.01
	- criterion = gini
	- max_depth = None
	- min_samples_split = 10
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
	- oob_decision_function_ = [[0.79150579 0.20849421]
 [0.61980798 0.38019202]
 [0.75602828 0.24397172]
 ...
 [0.6293491  0.3706509 ]
 [0.56661491 0.43338509]
 [0.53407275 0.46592725]]
	- oob_score_ = 0.8527777777777777

#### Importance of features
- gp_max_ix_range = 0.0769086516912606
- gp_max_val_max = 0.07517398954379856
- gp_max_val_range = 0.06456583463506167
- tdoa_range = 0.059349964163092295
- gp_max_val_mean = 0.0573702485494514
- gp_max_ix_mean = 0.05188250709806182
- gp_auc_range = 0.0464022252968089
- gp_max_val_std = 0.04169014602148325
- gp_max_val_min = 0.03896376860486533
- tdoa_std = 0.036233115977351946
- gp_max_ix_std = 0.036191932295489594
- gp_auc_std = 0.0344819168155939
- gp_max_ix_min = 0.03424813365201318
- ratio_max_to_9th_ave_peaks = 0.034124891444674864
- tdoa_min = 0.03311934521915068
- srmr = 0.030720709238724504
- ac_auc = 0.028344683178391415
- diff_std = 0.026760387539653076
- tdoa_mean = 0.025092929292929285
- gp_max_ix_max = 0.024826983402796904
- gp_auc_max = 0.023390222046924973
- gp_auc_min = 0.021741410159115456
- tdoa_max = 0.01181906016688625
- diff_auc = 0.011397047397047395
- low_power = 0.0094756481747018
- coe1[1] = 0.009162210338680926
- ratio_max_to_10ms_ave_peaks = 0.009140759709773792
- hlbr = 0.00911418346631852
- coe3[2] = 0.009009368409368407
- ac_std = 0.007524630924630922
- high_power = 0.006807864285930088
- gp_auc_mean = 0.006606060606060605
- coe3[3] = 0.005025837320574161
- coe1[0] = 0.0033333333333333327
- coe3[0] = 0.0
- coe3[1] = 0.0

## Evaluation
cv = 10
### accuracy
- Scores = [ 0.8628472222222222, 0.8836805555555556, 0.890625, 0.8836805555555556, 0.8871527777777778, 0.8819444444444444, 0.8784722222222222, 0.875, 0.8784722222222222, 0.875 ]
- Mean = 0.8796875
- Standard deviation = 0.0073677413798343624

### balanced_accuracy
- Scores = [ 0.6240079365079365, 0.5823412698412698, 0.5625, 0.5347222222222222, 0.560515873015873, 0.5277777777777778, 0.5615079365079365, 0.5, 0.5198412698412699, 0.5 ]
- Mean = 0.5473214285714285
- Standard deviation = 0.03672524717301947

### f1
- Scores = [ 0.3577235772357724, 0.27956989247311825, 0.2222222222222222, 0.12987012987012989, 0.21686746987951808, 0.10526315789473684, 0.22222222222222227, 0.0, 0.07894736842105264, 0.0 ]
- Mean = 0.16126860402187726
- Standard deviation = 0.11226132801188186

### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 4992 | 48 |
| Actual Positive | 645 | 75 |

      