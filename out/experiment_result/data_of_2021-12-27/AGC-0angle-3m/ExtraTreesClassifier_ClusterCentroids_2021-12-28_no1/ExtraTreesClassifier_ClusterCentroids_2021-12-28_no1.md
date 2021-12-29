# ExtraTreesClassifier_ClusterCentroids_2021-12-28_no1
## Constants
- CSV_PATH = ../out/csv/experiment
- OUTPUT_PATH = ../out/experiment_result/data_of_2021-12-27/AGC-0angle-3m
- FEATURE_ATTRBS = ['low_power', 'high_power', 'hlbr', 'coe1[0]', 'coe1[1]', 'coe3[0]', 'coe3[1]', 'coe3[2]', 'coe3[3]', 'ratio_max_to_10ms_ave_peaks', 'ratio_max_to_9th_ave_peaks', 'ac_std', 'ac_auc', 'diff_std', 'diff_auc', 'srmr', 'gp_max_val_std', 'gp_max_val_range', 'gp_max_val_min', 'gp_max_val_max', 'gp_max_val_mean', 'gp_max_ix_std', 'gp_max_ix_range', 'gp_max_ix_min', 'gp_max_ix_max', 'gp_max_ix_mean', 'gp_auc_std', 'gp_auc_range', 'gp_auc_min', 'gp_auc_max', 'gp_auc_mean', 'tdoa_std', 'tdoa_range', 'tdoa_min', 'tdoa_max', 'tdoa_mean']
- LABEL_ATTRB = ['facing']
- FACING_DOV_ANGLES = [1]
- NCV = 8
- SCORING = ['accuracy', 'balanced_accuracy', 'f1']
- REFIT_SCORING = balanced_accuracy
- PARAM_GRID = [{'est__n_estimators': [50, 100, 150, 200, 300], 'est__min_samples_split': [2, 5, 10], 'est__min_samples_leaf': [1, 5, 10], 'est__max_features': ['sqrt', 'log2', None], 'est__bootstrap': [False], 'est__n_jobs': [-1], 'est__random_state': [42], 'est__max_samples': [0.01, 0.5, 0.09]}, {'est__n_estimators': [50, 100, 150, 200, 300], 'est__min_samples_split': [2, 5, 10], 'est__min_samples_leaf': [1, 5, 10], 'est__max_features': ['sqrt', 'log2', None], 'est__bootstrap': [True], 'est__oob_score': [True, False], 'est__n_jobs': [-1], 'est__random_state': [42], 'est__max_samples': [0.01, 0.5, 0.09]}]
- TRAIN_SET_SESSION = ['trial1', 'trial2']
- TEST_SET_SESSION = ['trial3', 'trial4', 'trial5']
- DISTANCE = [3]
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
	- sampling_strategy_ = OrderedDict([(0, 10)])
	- estimator_ = KMeans(n_clusters=10, random_state=42)
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
- gp_auc_max = 0.12725003101473692
- gp_max_val_max = 0.11113545343545342
- gp_auc_min = 0.1108053326790169
- gp_max_val_mean = 0.10108415244885834
- gp_max_val_min = 0.06038141074611663
- high_power = 0.05624563214563214
- gp_auc_mean = 0.050316849816849814
- diff_auc = 0.04742840166369578
- coe3[2] = 0.03203953823953824
- hlbr = 0.028571279597595388
- coe3[3] = 0.025416941881647764
- coe1[0] = 0.02173838383838384
- srmr = 0.02063968253968254
- diff_std = 0.019537254901960784
- gp_max_val_std = 0.016923351158645277
- coe1[1] = 0.016329403929403928
- gp_max_val_range = 0.015061327561327562
- ac_auc = 0.01373001443001443
- gp_auc_range = 0.012977777777777779
- ac_std = 0.01185858585858586
- tdoa_max = 0.0115
- low_power = 0.011472438672438672
- tdoa_std = 0.011373382173382171
- ratio_max_to_10ms_ave_peaks = 0.0108
- gp_max_ix_mean = 0.010606334841628961
- gp_max_ix_std = 0.00936767676767677
- tdoa_mean = 0.00824051504051504
- gp_auc_std = 0.007947712418300657
- tdoa_range = 0.006750971250971254
- ratio_max_to_9th_ave_peaks = 0.004433333333333334
- gp_max_ix_max = 0.003703496503496505
- gp_max_ix_range = 0.002666666666666667
- gp_max_ix_min = 0.0016666666666666679
- coe3[0] = 0.0
- coe3[1] = 0.0
- tdoa_min = 0.0

## Evaluation
cv = 8
### accuracy
- Scores = [ 0.7, 0.7, 0.7777777777777778, 1.0, 0.7777777777777778, 0.6666666666666666, 0.5555555555555556, 0.7777777777777778 ]
- Mean = 0.7444444444444445
- Standard deviation = 0.11954130439638896

### balanced_accuracy
- Scores = [ 0.8125, 0.8125, 0.8571428571428572, 1.0, 0.8571428571428572, 0.6071428571428572, 0.5357142857142857, 0.875 ]
- Mean = 0.7946428571428572
- Standard deviation = 0.14110250561856347

### f1
- Scores = [ 0.5714285714285715, 0.5714285714285715, 0.6666666666666666, 1.0, 0.6666666666666666, 0.4, 0.3333333333333333, 0.5 ]
- Mean = 0.5886904761904761
- Standard deviation = 0.19059427143504307

### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 42 | 17 |
| Actual Positive | 2 | 13 |

      