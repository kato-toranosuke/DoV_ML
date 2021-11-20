# ExtraTreesClassifier_ClusterCentroids_2021-11-04_no0
## Constants
- CSV_PATH = ../../out/csv/
- OUTPUT_PATH = ./result/
- FEATURE_ATTRBS = ['low_power', 'high_power', 'hlbr', 'coe1[0]', 'coe1[1]', 'coe3[0]', 'coe3[1]', 'coe3[2]', 'coe3[3]', 'ratio_max_to_10ms_ave_peaks', 'ratio_max_to_9th_ave_peaks', 'ac_std', 'ac_auc', 'diff_std', 'diff_auc', 'srmr', 'gp_max_val_std', 'gp_max_val_range', 'gp_max_val_min', 'gp_max_val_max', 'gp_max_val_mean', 'gp_max_ix_std', 'gp_max_ix_range', 'gp_max_ix_min', 'gp_max_ix_max', 'gp_max_ix_mean', 'gp_auc_std', 'gp_auc_range', 'gp_auc_min', 'gp_auc_max', 'gp_auc_mean', 'tdoa_std', 'tdoa_range', 'tdoa_min', 'tdoa_max', 'tdoa_mean']
- LABEL_ATTRB = ['dov_angle']
- FACING_DOV_ANGLES = [0, 45, 315]
- NCV = 10
- SCORING = ['accuracy', 'balanced_accuracy', 'f1']
- REFIT_SCORING = balanced_accuracy
- PARAM_GRID = [{'est__n_estimators': [2, 10, 100, 1000], 'est__min_samples_split': [2, 5, 10], 'est__min_samples_leaf': [1, 5, 10], 'est__max_features': ['sqrt', 'log2', None], 'est__bootstrap': [False], 'est__n_jobs': [-1], 'est__random_state': [42], 'est__max_samples': [0.01, 0.5, 0.09]}, {'est__n_estimators': [2, 10, 100, 1000], 'est__min_samples_split': [2, 5, 10], 'est__min_samples_leaf': [1, 5, 10], 'est__max_features': ['sqrt', 'log2', None], 'est__bootstrap': [True], 'est__oob_score': [True, False], 'est__n_jobs': [-1], 'est__random_state': [42], 'est__max_samples': [0.01, 0.5, 0.09]}]

## Loaded CSV
- features_mono_ch_matlab.csv

## Estimator
### Type
- resampler = ClusterCentroids
- estimator = ExtraTreesClassifier

### Arguments for hyperparameter search
- resampler = ClusterCentroids
- estimator = ExtraTreesClassifier
- param_grid = 
	- {'est__n_estimators': [2, 10, 100, 1000], 'est__min_samples_split': [2, 5, 10], 'est__min_samples_leaf': [1, 5, 10], 'est__max_features': ['sqrt', 'log2', None], 'est__bootstrap': [False], 'est__n_jobs': [-1], 'est__random_state': [42], 'est__max_samples': [0.01, 0.5, 0.09]}
	- {'est__n_estimators': [2, 10, 100, 1000], 'est__min_samples_split': [2, 5, 10], 'est__min_samples_leaf': [1, 5, 10], 'est__max_features': ['sqrt', 'log2', None], 'est__bootstrap': [True], 'est__oob_score': [True, False], 'est__n_jobs': [-1], 'est__random_state': [42], 'est__max_samples': [0.01, 0.5, 0.09]}

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
	- base_estimator = ExtraTreeClassifier()
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

#### Importance of features
- gp_max_val_max = 0.18813039491268305
- gp_max_val_mean = 0.16039869378648017
- gp_max_val_range = 0.059106931001991596
- gp_max_val_min = 0.0578550862912246
- gp_max_val_std = 0.037956279213826556
- gp_auc_mean = 0.03733117640781887
- gp_auc_min = 0.031089763899980777
- gp_auc_max = 0.030462815793909713
- tdoa_std = 0.024558373085464005
- gp_max_ix_std = 0.02405147274482527
- tdoa_mean = 0.023114859628460136
- gp_max_ix_min = 0.02303494215544054
- tdoa_min = 0.022824049604033694
- gp_max_ix_mean = 0.022384590877838593
- tdoa_range = 0.02175396766010774
- gp_max_ix_range = 0.021460664224467983
- diff_std = 0.01601387041135091
- high_power = 0.015575848021908078
- ratio_max_to_9th_ave_peaks = 0.015151988341564225
- srmr = 0.0142339559989493
- gp_auc_range = 0.014092562151883802
- ratio_max_to_10ms_ave_peaks = 0.013968000721808404
- gp_max_ix_max = 0.01384905326703681
- tdoa_max = 0.01351254198624274
- gp_auc_std = 0.013446973753939138
- ac_auc = 0.012018252307913268
- diff_auc = 0.011950759878447762
- hlbr = 0.011703938241746164
- ac_std = 0.009338676226406337
- coe3[2] = 0.008564389624026962
- coe1[1] = 0.007939264597606906
- coe1[0] = 0.007921993660827464
- low_power = 0.007764994485851059
- coe3[3] = 0.007438875033937292
- coe3[0] = 0.0
- coe3[1] = 0.0

## Evaluation
cv = 10
### accuracy
- Scores = [ 0.7986111111111112, 0.90625, 0.8975694444444444, 0.8871527777777778, 0.8680555555555556, 0.8298611111111112, 0.8576388888888888, 0.8350694444444444, 0.8940972222222222, 0.765625 ]
- Mean = 0.8539930555555557
- Standard deviation = 0.04400587925875836

### balanced_accuracy
- Scores = [ 0.8305555555555555, 0.9055555555555556, 0.8949074074074075, 0.8597222222222223, 0.8527777777777777, 0.7833333333333333, 0.8703703703703703, 0.7986111111111112, 0.8791666666666667, 0.6986111111111111 ]
- Mean = 0.837361111111111
- Standard deviation = 0.0593763491652362

### f1
- Scores = [ 0.7811320754716982, 0.8783783783783783, 0.8662131519274376, 0.832904884318766, 0.8181818181818182, 0.7247191011235955, 0.8291666666666665, 0.7480106100795756, 0.8530120481927711, 0.5794392523364487 ]
- Mean = 0.7911157986677156
- Standard deviation = 0.08496204762161605

### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 3254 | 346 |
| Actual Positive | 495 | 1665 |

      