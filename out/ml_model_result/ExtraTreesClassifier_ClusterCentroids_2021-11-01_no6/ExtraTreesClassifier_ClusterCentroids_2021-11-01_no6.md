# ExtraTreesClassifier_ClusterCentroids_2021-11-01_no6
## Constants
- CSV_PATH = ../../out/csv/
- OUTPUT_PATH = ./result/
- FEATURE_ATTRBS = ['low_power', 'high_power', 'hlbr', 'coe1[0]', 'coe1[1]', 'coe3[0]', 'coe3[1]', 'coe3[2]', 'coe3[3]', 'ratio_max_to_10ms_ave_peaks', 'ratio_max_to_9th_ave_peaks', 'ac_std', 'ac_auc', 'diff_std', 'diff_auc', 'srmr', 'gp_max_val_std', 'gp_max_val_range', 'gp_max_val_min', 'gp_max_val_max', 'gp_max_val_mean', 'gp_max_ix_std', 'gp_max_ix_range', 'gp_max_ix_min', 'gp_max_ix_max', 'gp_max_ix_mean', 'gp_auc_std', 'gp_auc_range', 'gp_auc_min', 'gp_auc_max', 'gp_auc_mean', 'tdoa_std', 'tdoa_range', 'tdoa_min', 'tdoa_max', 'tdoa_mean']
- LABEL_ATTRB = ['dov_angle']
- FACING_DOV_ANGLES = [0, 45, 315]
- NCV = 10
- SCORING = ['accuracy', 'balanced_accuracy', 'f1']
- REFIT_SCORING = balanced_accuracy
- PARAM_GRID = [{'est__n_estimators': [10], 'est__min_samples_split': [2], 'est__min_samples_leaf': [5], 'est__max_features': [None], 'est__bootstrap': [False], 'est__n_jobs': [-1], 'est__random_state': [42], 'est__max_samples': [0.5]}]

## Loaded CSV
- features_mono_ch_python.csv

## Estimator
### Type
- resampler = ClusterCentroids
- estimator = ExtraTreesClassifier

### Arguments for hyperparameter search
- resampler = ClusterCentroids
- estimator = ExtraTreesClassifier
- param_grid = 
	- {'est__n_estimators': [10], 'est__min_samples_split': [2], 'est__min_samples_leaf': [5], 'est__max_features': [None], 'est__bootstrap': [False], 'est__n_jobs': [-1], 'est__random_state': [42], 'est__max_samples': [0.5]}

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
	- n_estimators = 10
	- estimator_params = ('criterion', 'max_depth', 'min_samples_split', 'min_samples_leaf', 'min_weight_fraction_leaf', 'max_features', 'max_leaf_nodes', 'min_impurity_decrease', 'min_impurity_split', 'random_state', 'ccp_alpha')
	- bootstrap = False
	- oob_score = False
	- n_jobs = -1
	- random_state = 42
	- verbose = 0
	- warm_start = False
	- class_weight = None
	- max_samples = 0.5
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
- gp_auc_max = 0.1621204276415504
- gp_max_val_max = 0.1473209374999338
- gp_auc_mean = 0.08126042349833236
- gp_max_val_mean = 0.07995540045824187
- gp_max_val_min = 0.039688693528530584
- gp_auc_min = 0.03906948245115219
- gp_max_val_range = 0.03826961743275078
- tdoa_range = 0.03298179255045051
- gp_max_val_std = 0.03155774412116707
- tdoa_std = 0.03078971712873731
- gp_max_ix_range = 0.03047790713597696
- gp_max_ix_std = 0.0302489617478997
- tdoa_mean = 0.028717777648641717
- gp_max_ix_mean = 0.02740441736633137
- tdoa_max = 0.027301673988067134
- gp_max_ix_min = 0.02317118039392752
- tdoa_min = 0.022921334359482008
- gp_max_ix_max = 0.020525958554932715
- gp_auc_std = 0.01071883936815996
- srmr = 0.009291784903054085
- ratio_max_to_10ms_ave_peaks = 0.008518223100223512
- gp_auc_range = 0.00851812489941366
- diff_std = 0.007088737914724594
- coe3[3] = 0.0069899388055296675
- ac_auc = 0.006539758641728262
- high_power = 0.006092929688061502
- low_power = 0.006021463899125813
- ratio_max_to_9th_ave_peaks = 0.005944732010394957
- hlbr = 0.005877557970967256
- diff_auc = 0.005525366313714887
- coe3[2] = 0.005403852300448402
- coe1[0] = 0.004710438216007827
- ac_std = 0.00460834496348855
- coe1[1] = 0.004366459498851075
- coe3[0] = 0.0
- coe3[1] = 0.0

## Evaluation
cv = 10
### accuracy
- Scores = [ 0.7881944444444444, 0.8767361111111112, 0.8524305555555556, 0.8506944444444444, 0.8506944444444444, 0.8003472222222222, 0.8298611111111112, 0.8142361111111112, 0.8871527777777778, 0.7777777777777778 ]
- Mean = 0.8328125
- Standard deviation = 0.035119686919681106

### balanced_accuracy
- Scores = [ 0.8166666666666667, 0.8662037037037037, 0.8449074074074074, 0.8194444444444444, 0.8305555555555555, 0.7560185185185185, 0.8398148148148148, 0.7847222222222222, 0.8745370370370371, 0.7138888888888889 ]
- Mean = 0.8146759259259259
- Standard deviation = 0.04749650283133626

### f1
- Scores = [ 0.7671755725190841, 0.8337236533957846, 0.8054919908466818, 0.7772020725388601, 0.7902439024390243, 0.684931506849315, 0.7949790794979079, 0.7291139240506329, 0.8456057007125891, 0.607361963190184 ]
- Mean = 0.7635829366040063
- Standard deviation = 0.06861332841301078

### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 3194 | 406 |
| Actual Positive | 557 | 1603 |

      