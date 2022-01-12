# ExtraTreesClassifier_ClusterCentroids_2022-01-10_no1
## Constants
- CSV_PATH = ../out/csv/experiment
- OUTPUT_PATH = ../out/experiment_result/data_of_2022-01-10/NoAGC-0angle-1m
- FEATURE_ATTRBS = ['low_power', 'high_power', 'hlbr', 'coe1[0]', 'coe1[1]', 'coe3[0]', 'coe3[1]', 'coe3[2]', 'coe3[3]', 'ratio_max_to_10ms_ave_peaks', 'ratio_max_to_9th_ave_peaks', 'ac_std', 'ac_auc', 'diff_std', 'diff_auc', 'srmr', 'gp_max_val_std', 'gp_max_val_range', 'gp_max_val_min', 'gp_max_val_max', 'gp_max_val_mean', 'gp_max_ix_std', 'gp_max_ix_range', 'gp_max_ix_min', 'gp_max_ix_max', 'gp_max_ix_mean', 'gp_auc_std', 'gp_auc_range', 'gp_auc_min', 'gp_auc_max', 'gp_auc_mean', 'tdoa_std', 'tdoa_range', 'tdoa_min', 'tdoa_max', 'tdoa_mean']
- LABEL_ATTRB = ['facing']
- FACING_DOV_ANGLES = [1]
- NCV = 8
- SCORING = ['accuracy', 'balanced_accuracy', 'f1']
- REFIT_SCORING = balanced_accuracy
- PARAM_GRID = [{'est__n_estimators': [50, 100, 150, 200, 300], 'est__min_samples_split': [2, 5, 10], 'est__min_samples_leaf': [1, 5, 10], 'est__max_features': ['sqrt', 'log2', None], 'est__bootstrap': [False], 'est__n_jobs': [-1], 'est__random_state': [42], 'est__max_samples': [0.01, 0.5, 0.09]}, {'est__n_estimators': [50, 100, 150, 200, 300], 'est__min_samples_split': [2, 5, 10], 'est__min_samples_leaf': [1, 5, 10], 'est__max_features': ['sqrt', 'log2', None], 'est__bootstrap': [True], 'est__oob_score': [True, False], 'est__n_jobs': [-1], 'est__random_state': [42], 'est__max_samples': [0.01, 0.5, 0.09]}]
- TRAIN_SET_SESSION = ['trial1', 'trial2']
- TEST_SET_SESSION = ['trial3', 'trial4', 'trial5']
- DISTANCE = [1]
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
	- sampling_strategy_ = OrderedDict([(0, 10)])
	- estimator_ = KMeans(n_clusters=10, random_state=42)
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
	- min_samples_split = 10
	- min_samples_leaf = 1
	- min_weight_fraction_leaf = 0.0
	- max_features = log2
	- max_leaf_nodes = None
	- min_impurity_decrease = 0.0
	- ccp_alpha = 0.0
	- n_features_in_ = 36
	- n_outputs_ = 1
	- classes_ = [0 1]
	- n_classes_ = 2
	- base_estimator_ = ExtraTreeClassifier()

#### Importance of features
- gp_auc_max = 0.09806070533844051
- tdoa_min = 0.09137165939155484
- gp_auc_mean = 0.07547451035476917
- tdoa_range = 0.0671913333902818
- gp_max_ix_range = 0.06673067780522482
- gp_max_val_mean = 0.06468114835663873
- gp_max_val_max = 0.05742751097300621
- gp_max_val_min = 0.05364991963793748
- tdoa_mean = 0.049110200636727705
- gp_auc_min = 0.0475531978047972
- srmr = 0.035122118881441115
- tdoa_std = 0.032599333431870464
- gp_max_ix_mean = 0.03221026546558584
- gp_max_ix_std = 0.028347574329085433
- gp_max_ix_min = 0.025802566869623764
- gp_max_ix_max = 0.024102080254042937
- hlbr = 0.018621955921806006
- gp_max_val_std = 0.017453277140510228
- gp_auc_range = 0.01640293645636539
- gp_auc_std = 0.015258603723764318
- ac_std = 0.01478626414553336
- tdoa_max = 0.012836149496436577
- coe1[1] = 0.009854087560037222
- low_power = 0.00966532523647291
- coe3[2] = 0.006799523088625558
- coe3[3] = 0.006232666558247958
- ratio_max_to_10ms_ave_peaks = 0.004909577032653958
- high_power = 0.004223606906243814
- diff_std = 0.003778340871364128
- ac_auc = 0.0035233996772458323
- coe1[0] = 0.002952363251366575
- diff_auc = 0.0013223140495867776
- gp_max_val_range = 0.0011121334805545343
- ratio_max_to_9th_ave_peaks = 0.0008326724821570188
- coe3[0] = 0.0
- coe3[1] = 0.0

## Evaluation
cv = 8
### accuracy
- Scores = [ 0.4, 0.6, 0.8, 0.5555555555555556, 1.0, 0.8888888888888888, 0.6666666666666666, 0.3333333333333333 ]
- Mean = 0.6555555555555556
- Standard deviation = 0.2168802366215904

### balanced_accuracy
- Scores = [ 0.625, 0.75, 0.6875, 0.7142857142857143, 1.0, 0.9285714285714286, 0.7857142857142857, 0.625 ]
- Mean = 0.7645089285714286
- Standard deviation = 0.12767681536005154

### f1
- Scores = [ 0.4, 0.5, 0.5, 0.5, 1.0, 0.8, 0.5714285714285715, 0.25 ]
- Mean = 0.5651785714285714
- Standard deviation = 0.21897947147751415

### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 33 | 27 |
| Actual Positive | 0 | 15 |

      