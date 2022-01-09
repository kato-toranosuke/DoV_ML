# ExtraTreesClassifier_ClusterCentroids_2022-01-09_no1
## Constants
- CSV_PATH = ../out/csv/experiment
- OUTPUT_PATH = ../out/experiment_result/data_of_2022-01-07_new2/AGC-45angle-under5m
- FEATURE_ATTRBS = ['low_power', 'high_power', 'hlbr', 'coe1[0]', 'coe1[1]', 'coe3[0]', 'coe3[1]', 'coe3[2]', 'coe3[3]', 'ratio_max_to_10ms_ave_peaks', 'ratio_max_to_9th_ave_peaks', 'ac_std', 'ac_auc', 'diff_std', 'diff_auc', 'srmr', 'gp_max_val_std', 'gp_max_val_range', 'gp_max_val_min', 'gp_max_val_max', 'gp_max_val_mean', 'gp_max_ix_std', 'gp_max_ix_range', 'gp_max_ix_min', 'gp_max_ix_max', 'gp_max_ix_mean', 'gp_auc_std', 'gp_auc_range', 'gp_auc_min', 'gp_auc_max', 'gp_auc_mean', 'tdoa_std', 'tdoa_range', 'tdoa_min', 'tdoa_max', 'tdoa_mean']
- LABEL_ATTRB = ['facing2']
- FACING_DOV_ANGLES = [1, 2]
- NCV = 8
- SCORING = ['accuracy', 'balanced_accuracy', 'f1']
- REFIT_SCORING = balanced_accuracy
- PARAM_GRID = [{'est__n_estimators': range(10, 1000, 25), 'est__min_samples_split': [2, 5, 10], 'est__min_samples_leaf': [1, 5, 10], 'est__max_features': ['sqrt', 'log2', None], 'est__bootstrap': [False], 'est__n_jobs': [-1], 'est__random_state': [42], 'est__max_samples': [0.01, 0.5, 0.09]}]
- TRAIN_SET_SESSION = ['trial1', 'trial2']
- TEST_SET_SESSION = ['trial3', 'trial4', 'trial5']
- DISTANCE = [1, 3, 5]
- AGC_STATUS = ['AGC']

## Loaded CSV
- 2021-12-27_raspi_48000Hz_w1_N2^12_overlap80_with2022-01-07.csv

## Estimator
### Type
- resampler = ClusterCentroids
- estimator = ExtraTreesClassifier

### Arguments for hyperparameter search
- resampler = ClusterCentroids
- estimator = ExtraTreesClassifier
- param_grid = 
	- {'est__n_estimators': range(10, 1000, 25), 'est__min_samples_split': [2, 5, 10], 'est__min_samples_leaf': [1, 5, 10], 'est__max_features': ['sqrt', 'log2', None], 'est__bootstrap': [False], 'est__n_jobs': [-1], 'est__random_state': [42], 'est__max_samples': [0.01, 0.5, 0.09]}

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
	- sampling_strategy_ = OrderedDict([(1, 72)])
	- estimator_ = KMeans(n_clusters=72, random_state=42)
	- voting_ = soft

- best_estimator
	- base_estimator = ExtraTreeClassifier()
	- n_estimators = 35
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
- gp_auc_max = 0.10153137679386515
- gp_auc_min = 0.09235449935479743
- gp_auc_mean = 0.08667134134252526
- gp_max_val_min = 0.08607886011212429
- high_power = 0.06771326634272945
- diff_auc = 0.06739956989001843
- gp_max_val_mean = 0.06046670737981835
- gp_max_val_max = 0.046976974816312383
- coe1[0] = 0.039885492614747664
- diff_std = 0.03569600946509647
- coe1[1] = 0.029761769322922127
- srmr = 0.022618909037330392
- coe3[3] = 0.02227120579794589
- hlbr = 0.021985421674635647
- gp_max_ix_mean = 0.01920197817570795
- ratio_max_to_10ms_ave_peaks = 0.017885644994356898
- tdoa_range = 0.015809878014426498
- low_power = 0.014871018404226425
- coe3[2] = 0.013503622441256859
- gp_max_val_std = 0.012862572037818721
- tdoa_mean = 0.01241129326981846
- gp_max_ix_min = 0.011351440494297637
- ac_auc = 0.011016949538972143
- tdoa_min = 0.010229962018477423
- gp_max_ix_std = 0.0101165514664499
- gp_auc_std = 0.009617924101648632
- gp_max_val_range = 0.009139106320145326
- ac_std = 0.008945089546383013
- gp_max_ix_range = 0.008912807112855168
- gp_auc_range = 0.008307215271500986
- tdoa_std = 0.006950879133280955
- ratio_max_to_9th_ave_peaks = 0.006600499174028585
- tdoa_max = 0.006011560944193442
- gp_max_ix_max = 0.0048426035952860175
- coe3[0] = 0.0
- coe3[1] = 0.0

## Evaluation
cv = 8
### accuracy
- Scores = [ 0.896551724137931, 0.9642857142857143, 0.8928571428571429, 1.0, 0.8571428571428571, 1.0, 1.0, 1.0 ]
- Mean = 0.9513546798029557
- Standard deviation = 0.05582771899824206

### balanced_accuracy
- Scores = [ 0.8928571428571428, 0.9666666666666667, 0.9, 1.0, 0.8615384615384616, 1.0, 1.0, 1.0 ]
- Mean = 0.9526327838827839
- Standard deviation = 0.054558541127193626

### f1
- Scores = [ 0.9090909090909091, 0.9655172413793104, 0.888888888888889, 1.0, 0.8571428571428571, 1.0, 1.0, 1.0 ]
- Mean = 0.9525799870627456
- Standard deviation = 0.05502056969205582

### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 103 | 5 |
| Actual Positive | 6 | 111 |

      