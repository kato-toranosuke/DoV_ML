# ExtraTreesClassifier_ClusterCentroids_2021-12-29_no1
## Constants
- CSV_PATH = ../out/csv/experiment
- OUTPUT_PATH = ../out/experiment_result/data_of_2021-12-27/AGC-45angle-under3m
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
- AGC_STATUS = ['AGC']

## Loaded CSV
- 2021-12-27_raspi_48000Hz_w1_N2^12_overlap80_new.csv

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
	- sampling_strategy_ = OrderedDict([(1, 46)])
	- estimator_ = KMeans(n_clusters=46, random_state=42)
	- voting_ = soft

- best_estimator
	- base_estimator = ExtraTreeClassifier()
	- n_estimators = 50
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
- gp_auc_min = 0.13530613531626434
- gp_max_val_min = 0.12923263803028961
- gp_max_val_max = 0.08858941574353686
- gp_auc_mean = 0.08789072135677217
- gp_max_val_mean = 0.08492720153483725
- gp_auc_max = 0.07919755516264898
- diff_auc = 0.05859676453135041
- srmr = 0.04285692322264878
- coe1[0] = 0.04167008513763673
- diff_std = 0.03216162867703576
- ratio_max_to_10ms_ave_peaks = 0.026515009059954367
- low_power = 0.02137223637789664
- coe3[3] = 0.020047443682810355
- coe1[1] = 0.019006379096386028
- hlbr = 0.013783501738633507
- tdoa_mean = 0.011082273172153156
- high_power = 0.01023640803141808
- gp_max_ix_mean = 0.009221047611801921
- tdoa_std = 0.008696388064285342
- coe3[2] = 0.008383894818940427
- gp_max_val_std = 0.007896123955707664
- gp_auc_std = 0.007873764755168931
- gp_max_ix_std = 0.007006560879283182
- gp_max_val_range = 0.006561631605109863
- gp_max_ix_range = 0.006037597963681846
- gp_auc_range = 0.005829542563796238
- ac_auc = 0.005736522290769162
- ratio_max_to_9th_ave_peaks = 0.004498021855203175
- ac_std = 0.004400008077353617
- tdoa_range = 0.004300779900968136
- gp_max_ix_min = 0.003982257308332983
- tdoa_min = 0.0029786501586077404
- gp_max_ix_max = 0.002672049819508986
- tdoa_max = 0.0014528384992078982
- coe3[0] = 0.0
- coe3[1] = 0.0

## Evaluation
cv = 8
### accuracy
- Scores = [ 0.8421052631578947, 1.0, 0.9473684210526315, 0.9473684210526315, 1.0, 1.0, 0.9444444444444444, 0.9444444444444444 ]
- Mean = 0.9532163742690059
- Standard deviation = 0.0489056394259583

### balanced_accuracy
- Scores = [ 0.8333333333333333, 1.0, 0.95, 0.95, 1.0, 1.0, 0.9444444444444444, 0.9444444444444444 ]
- Mean = 0.9527777777777777
- Standard deviation = 0.05137011669140816

### f1
- Scores = [ 0.8695652173913044, 1.0, 0.9473684210526316, 0.9473684210526316, 1.0, 1.0, 0.9411764705882353, 0.9411764705882353 ]
- Mean = 0.9558318750841297
- Standard deviation = 0.041634162468167264

### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 68 | 3 |
| Actual Positive | 4 | 74 |

      