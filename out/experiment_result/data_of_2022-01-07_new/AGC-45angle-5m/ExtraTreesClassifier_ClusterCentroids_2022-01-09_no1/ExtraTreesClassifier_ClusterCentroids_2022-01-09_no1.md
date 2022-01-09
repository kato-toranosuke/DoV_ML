# ExtraTreesClassifier_ClusterCentroids_2022-01-09_no1
## Constants
- CSV_PATH = ../out/csv/experiment
- OUTPUT_PATH = ../out/experiment_result/data_of_2022-01-07_new/AGC-45angle-5m
- FEATURE_ATTRBS = ['low_power', 'high_power', 'hlbr', 'coe1[0]', 'coe1[1]', 'coe3[0]', 'coe3[1]', 'coe3[2]', 'coe3[3]', 'ratio_max_to_10ms_ave_peaks', 'ratio_max_to_9th_ave_peaks', 'ac_std', 'ac_auc', 'diff_std', 'diff_auc', 'srmr', 'gp_max_val_std', 'gp_max_val_range', 'gp_max_val_min', 'gp_max_val_max', 'gp_max_val_mean', 'gp_max_ix_std', 'gp_max_ix_range', 'gp_max_ix_min', 'gp_max_ix_max', 'gp_max_ix_mean', 'gp_auc_std', 'gp_auc_range', 'gp_auc_min', 'gp_auc_max', 'gp_auc_mean', 'tdoa_std', 'tdoa_range', 'tdoa_min', 'tdoa_max', 'tdoa_mean']
- LABEL_ATTRB = ['facing2']
- FACING_DOV_ANGLES = [1, 2]
- NCV = 8
- SCORING = ['accuracy', 'balanced_accuracy', 'f1']
- REFIT_SCORING = balanced_accuracy
- PARAM_GRID = [{'est__n_estimators': [50, 100, 150, 200, 300], 'est__min_samples_split': [2, 5, 10], 'est__min_samples_leaf': [1, 5, 10], 'est__max_features': ['sqrt', 'log2', None], 'est__bootstrap': [False], 'est__n_jobs': [-1], 'est__random_state': [42], 'est__max_samples': [0.01, 0.5, 0.09]}, {'est__n_estimators': [50, 100, 150, 200, 300], 'est__min_samples_split': [2, 5, 10], 'est__min_samples_leaf': [1, 5, 10], 'est__max_features': ['sqrt', 'log2', None], 'est__bootstrap': [True], 'est__oob_score': [True, False], 'est__n_jobs': [-1], 'est__random_state': [42], 'est__max_samples': [0.01, 0.5, 0.09]}]
- TRAIN_SET_SESSION = ['trial1', 'trial2']
- TEST_SET_SESSION = ['trial3', 'trial4', 'trial5']
- DISTANCE = [5]
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
	- sampling_strategy_ = OrderedDict([(1, 24)])
	- estimator_ = KMeans(n_clusters=24, random_state=42)
	- voting_ = soft

- best_estimator
	- base_estimator = ExtraTreeClassifier()
	- n_estimators = 50
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
- high_power = 0.11641091384822035
- gp_max_val_max = 0.09880382022398151
- gp_auc_max = 0.09455111873435511
- gp_max_val_mean = 0.08987177013317987
- gp_auc_min = 0.0663345279131702
- gp_auc_mean = 0.06075236072994694
- diff_auc = 0.05930240592740592
- gp_max_val_min = 0.05848085965611541
- hlbr = 0.05186345598845599
- srmr = 0.042097999727715746
- coe1[0] = 0.03739093597093381
- coe3[3] = 0.03618491801828507
- diff_std = 0.028511507011507006
- coe3[2] = 0.017514877031181382
- gp_max_val_std = 0.01743896021137401
- coe1[1] = 0.01575767852273937
- low_power = 0.01499738510785619
- gp_auc_std = 0.014973504394156565
- tdoa_min = 0.011633790283790286
- gp_max_ix_min = 0.011483038700430007
- gp_auc_range = 0.010218518518518517
- gp_max_ix_range = 0.007469974469974471
- tdoa_max = 0.0072238667073941006
- gp_max_ix_max = 0.006674603174603175
- tdoa_range = 0.004007936507936508
- gp_max_val_range = 0.0039057971014492742
- ac_std = 0.0035833333333333333
- ratio_max_to_9th_ave_peaks = 0.003478835978835978
- ac_auc = 0.003194444444444444
- tdoa_std = 0.0022222222222222222
- ratio_max_to_10ms_ave_peaks = 0.001611111111111111
- gp_max_ix_mean = 0.001497972739820566
- tdoa_mean = 0.0005555555555555556
- coe3[0] = 0.0
- coe3[1] = 0.0
- gp_max_ix_std = 0.0

## Evaluation
cv = 8
### accuracy
- Scores = [ 1.0, 1.0, 0.9, 0.6666666666666666, 1.0, 1.0, 1.0, 1.0 ]
- Mean = 0.9458333333333333
- Standard deviation = 0.11047561319635711

### balanced_accuracy
- Scores = [ 1.0, 1.0, 0.9, 0.7, 1.0, 1.0, 1.0, 1.0 ]
- Mean = 0.95
- Standard deviation = 0.1

### f1
- Scores = [ 1.0, 1.0, 0.9090909090909091, 0.5714285714285715, 1.0, 1.0, 1.0, 1.0 ]
- Mean = 0.935064935064935
- Standard deviation = 0.1406260248552449

### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 35 | 1 |
| Actual Positive | 1 | 38 |

      