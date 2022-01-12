# ExtraTreesClassifier_ClusterCentroids_2022-01-11_no1
## Constants
- CSV_PATH = ../out/csv/experiment
- OUTPUT_PATH = ../out/experiment_result/data_of_2022-01-10/NoAGC-45angle-under3m
- FEATURE_ATTRBS = ['low_power', 'high_power', 'hlbr', 'coe1[0]', 'coe1[1]', 'coe3[0]', 'coe3[1]', 'coe3[2]', 'coe3[3]', 'ratio_max_to_10ms_ave_peaks', 'ratio_max_to_9th_ave_peaks', 'ac_std', 'ac_auc', 'diff_std', 'diff_auc', 'srmr', 'gp_max_val_std', 'gp_max_val_range', 'gp_max_val_min', 'gp_max_val_max', 'gp_max_val_mean', 'gp_max_ix_std', 'gp_max_ix_range', 'gp_max_ix_min', 'gp_max_ix_max', 'gp_max_ix_mean', 'gp_auc_std', 'gp_auc_range', 'gp_auc_min', 'gp_auc_max', 'gp_auc_mean', 'tdoa_std', 'tdoa_range', 'tdoa_min', 'tdoa_max', 'tdoa_mean']
- LABEL_ATTRB = ['facing2']
- FACING_DOV_ANGLES = [1, 2]
- NCV = 8
- SCORING = ['accuracy', 'balanced_accuracy', 'f1']
- REFIT_SCORING = balanced_accuracy
- PARAM_GRID = [{'est__n_estimators': [50, 100, 150, 200, 300], 'est__min_samples_split': [2, 5, 10], 'est__min_samples_leaf': [1, 5, 10], 'est__max_features': ['sqrt', 'log2', None], 'est__bootstrap': [False], 'est__n_jobs': [-1], 'est__random_state': [42], 'est__max_samples': [0.01, 0.5, 0.09]}, {'est__n_estimators': [50, 100, 150, 200, 300], 'est__min_samples_split': [2, 5, 10], 'est__min_samples_leaf': [1, 5, 10], 'est__max_features': ['sqrt', 'log2', None], 'est__bootstrap': [True], 'est__oob_score': [True, False], 'est__n_jobs': [-1], 'est__random_state': [42], 'est__max_samples': [0.01, 0.5, 0.09]}]
- TRAIN_SET_SESSION = ['trial1', 'trial2']
- TEST_SET_SESSION = ['trial3', 'trial4', 'trial5']
- DISTANCE = [1, 3]
- AGC_STATUS = ['NoAGC']

## Loaded CSV
- 2022-01-10_raspi_48000Hz_w1_N2^12_overlap80.csv

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
	- sampling_strategy_ = OrderedDict([(1, 48)])
	- estimator_ = KMeans(n_clusters=48, random_state=42)
	- voting_ = soft

- best_estimator
	- base_estimator = ExtraTreeClassifier()
	- n_estimators = 100
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
	- min_samples_split = 5
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
- gp_max_val_mean = 0.12550227749676035
- gp_max_val_min = 0.12166106041421519
- gp_auc_mean = 0.11771370454589146
- gp_auc_min = 0.11351680084547709
- gp_auc_max = 0.1039854065307019
- gp_max_val_max = 0.07786050437623286
- srmr = 0.04120753970520833
- gp_max_ix_mean = 0.024975599090245333
- tdoa_mean = 0.02426414388005435
- ratio_max_to_10ms_ave_peaks = 0.02088726735283142
- tdoa_std = 0.020849427595594036
- hlbr = 0.01991705048316319
- gp_max_ix_range = 0.017883244104456786
- gp_max_ix_min = 0.01770154415954162
- gp_max_ix_std = 0.01489386223239527
- tdoa_range = 0.014406449284589389
- tdoa_min = 0.014383203730022802
- diff_std = 0.014374553986367878
- high_power = 0.010038615023825869
- tdoa_max = 0.009630003023373317
- gp_max_val_range = 0.009574459633312875
- diff_auc = 0.00843478937916588
- gp_auc_range = 0.007958248972351695
- gp_max_val_std = 0.007329567491630515
- gp_max_ix_max = 0.007252202475205744
- gp_auc_std = 0.006771832355025894
- low_power = 0.004436769723667182
- coe1[0] = 0.004379624524456182
- coe1[1] = 0.0041779023336075945
- coe3[2] = 0.003552322191084661
- ac_auc = 0.00287110851371149
- ratio_max_to_9th_ave_peaks = 0.0025759947105828103
- coe3[3] = 0.002572462132807106
- ac_std = 0.0024604577024418942
- coe3[0] = 0.0
- coe3[1] = 0.0

## Evaluation
cv = 8
### accuracy
- Scores = [ 0.8947368421052632, 1.0, 1.0, 0.9473684210526315, 1.0, 1.0, 0.8888888888888888, 1.0 ]
- Mean = 0.9663742690058479
- Standard deviation = 0.0463014257956524

### balanced_accuracy
- Scores = [ 0.8888888888888888, 1.0, 1.0, 0.95, 1.0, 1.0, 0.8888888888888888, 1.0 ]
- Mean = 0.9659722222222222
- Standard deviation = 0.04733951935320631

### f1
- Scores = [ 0.9090909090909091, 1.0, 1.0, 0.9473684210526316, 1.0, 1.0, 0.9, 1.0 ]
- Mean = 0.9695574162679426
- Standard deviation = 0.04126217801774376

### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 69 | 3 |
| Actual Positive | 1 | 77 |

      