# ExtraTreesClassifier_ClusterCentroids_2022-01-10_no1
## Constants
- CSV_PATH = ../out/csv/experiment
- OUTPUT_PATH = ../out/experiment_result/data_of_2022-01-10/NoAGC-45angle-3m
- FEATURE_ATTRBS = ['low_power', 'high_power', 'hlbr', 'coe1[0]', 'coe1[1]', 'coe3[0]', 'coe3[1]', 'coe3[2]', 'coe3[3]', 'ratio_max_to_10ms_ave_peaks', 'ratio_max_to_9th_ave_peaks', 'ac_std', 'ac_auc', 'diff_std', 'diff_auc', 'srmr', 'gp_max_val_std', 'gp_max_val_range', 'gp_max_val_min', 'gp_max_val_max', 'gp_max_val_mean', 'gp_max_ix_std', 'gp_max_ix_range', 'gp_max_ix_min', 'gp_max_ix_max', 'gp_max_ix_mean', 'gp_auc_std', 'gp_auc_range', 'gp_auc_min', 'gp_auc_max', 'gp_auc_mean', 'tdoa_std', 'tdoa_range', 'tdoa_min', 'tdoa_max', 'tdoa_mean']
- LABEL_ATTRB = ['facing2']
- FACING_DOV_ANGLES = [1, 2]
- NCV = 8
- SCORING = ['accuracy', 'balanced_accuracy', 'f1']
- REFIT_SCORING = balanced_accuracy
- PARAM_GRID = [{'est__n_estimators': [50, 100, 150, 200, 300], 'est__min_samples_split': [2, 5, 10], 'est__min_samples_leaf': [1, 5, 10], 'est__max_features': ['sqrt', 'log2', None], 'est__bootstrap': [False], 'est__n_jobs': [-1], 'est__random_state': [42], 'est__max_samples': [0.01, 0.5, 0.09]}, {'est__n_estimators': [50, 100, 150, 200, 300], 'est__min_samples_split': [2, 5, 10], 'est__min_samples_leaf': [1, 5, 10], 'est__max_features': ['sqrt', 'log2', None], 'est__bootstrap': [True], 'est__oob_score': [True, False], 'est__n_jobs': [-1], 'est__random_state': [42], 'est__max_samples': [0.01, 0.5, 0.09]}]
- TRAIN_SET_SESSION = ['trial1', 'trial2']
- TEST_SET_SESSION = ['trial3', 'trial4', 'trial5']
- DISTANCE = [3]
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
- gp_max_val_max = 0.1456570310792711
- gp_max_val_mean = 0.14561616475372882
- gp_max_val_min = 0.14541023097273098
- gp_auc_min = 0.12556114003505306
- gp_auc_max = 0.12509531719698555
- gp_auc_mean = 0.11463237458960973
- hlbr = 0.034608118489697436
- srmr = 0.03084953249181861
- gp_max_ix_max = 0.01776953308266091
- ac_std = 0.011077417843536622
- tdoa_max = 0.010356061092903195
- high_power = 0.010294079667177845
- gp_max_ix_mean = 0.010190379403794032
- diff_auc = 0.009425509854441723
- ratio_max_to_10ms_ave_peaks = 0.007958380378669224
- tdoa_range = 0.006819205569205569
- gp_max_ix_range = 0.0065681293864220695
- diff_std = 0.006050505050505051
- coe3[3] = 0.005666666666666666
- gp_auc_std = 0.00485164236634825
- low_power = 0.004218434016074671
- tdoa_std = 0.004000000000000001
- tdoa_min = 0.003704942400594572
- ac_auc = 0.003363155363155362
- gp_max_val_std = 0.0031767609784851165
- coe1[1] = 0.002066511048863991
- gp_max_val_range = 0.001428571428571429
- ratio_max_to_9th_ave_peaks = 0.0009920634920634922
- gp_auc_range = 0.0008333333333333333
- tdoa_mean = 0.0006593137254901938
- gp_max_ix_min = 0.0004861111111111122
- coe3[2] = 0.00039153439153439174
- gp_max_ix_std = 0.00019047619047619165
- coe1[0] = 3.137254901960706e-05
- coe3[0] = 0.0
- coe3[1] = 0.0

## Evaluation
cv = 8
### accuracy
- Scores = [ 1.0, 1.0, 1.0, 0.8888888888888888, 1.0, 1.0, 1.0, 1.0 ]
- Mean = 0.9861111111111112
- Standard deviation = 0.03674654598700822

### balanced_accuracy
- Scores = [ 1.0, 1.0, 1.0, 0.9, 1.0, 1.0, 1.0, 1.0 ]
- Mean = 0.9875
- Standard deviation = 0.03307189138830738

### f1
- Scores = [ 1.0, 1.0, 1.0, 0.888888888888889, 1.0, 1.0, 1.0, 1.0 ]
- Mean = 0.9861111111111112
- Standard deviation = 0.03674654598700818

### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 36 | 0 |
| Actual Positive | 0 | 39 |

      