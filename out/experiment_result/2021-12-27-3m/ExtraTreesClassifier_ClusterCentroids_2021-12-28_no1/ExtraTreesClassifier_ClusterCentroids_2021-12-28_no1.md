# ExtraTreesClassifier_ClusterCentroids_2021-12-28_no1
## Constants
- CSV_PATH = ../out/csv/experiment
- OUTPUT_PATH = ../out/experiment_result/2021-12-27-3m
- FEATURE_ATTRBS = ['low_power', 'high_power', 'hlbr', 'coe1[0]', 'coe1[1]', 'coe3[0]', 'coe3[1]', 'coe3[2]', 'coe3[3]', 'ratio_max_to_10ms_ave_peaks', 'ratio_max_to_9th_ave_peaks', 'ac_std', 'ac_auc', 'diff_std', 'diff_auc', 'srmr', 'gp_max_val_std', 'gp_max_val_range', 'gp_max_val_min', 'gp_max_val_max', 'gp_max_val_mean', 'gp_max_ix_std', 'gp_max_ix_range', 'gp_max_ix_min', 'gp_max_ix_max', 'gp_max_ix_mean', 'gp_auc_std', 'gp_auc_range', 'gp_auc_min', 'gp_auc_max', 'gp_auc_mean', 'tdoa_std', 'tdoa_range', 'tdoa_min', 'tdoa_max', 'tdoa_mean']
- LABEL_ATTRB = ['facing']
- FACING_DOV_ANGLES = [1]
- NCV = 8
- SCORING = ['accuracy', 'balanced_accuracy', 'f1']
- REFIT_SCORING = balanced_accuracy
- PARAM_GRID = [{'est__n_estimators': [50, 100, 150, 200, 300], 'est__min_samples_split': [2, 5, 10], 'est__min_samples_leaf': [1, 5, 10], 'est__max_features': ['sqrt', 'log2', None], 'est__bootstrap': [False], 'est__n_jobs': [-1], 'est__random_state': [42], 'est__max_samples': [0.01, 0.5, 0.09]}, {'est__n_estimators': [50, 100, 150, 200, 300], 'est__min_samples_split': [2, 5, 10], 'est__min_samples_leaf': [1, 5, 10], 'est__max_features': ['sqrt', 'log2', None], 'est__bootstrap': [True], 'est__oob_score': [True, False], 'est__n_jobs': [-1], 'est__random_state': [42], 'est__max_samples': [0.01, 0.5, 0.09]}]
- TRAIN_SET_SESSION = ['trial1', 'trial2']
- TEST_SET_SESSION = ['trial3', 'trial4', 'trial5']

## Loaded CSV
- 2021-12-27_raspi_48000Hz_w1_N2^12_overlap80_withfacing.csv

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
- gp_auc_min = 0.11480533267901691
- gp_max_val_max = 0.11113545343545342
- gp_max_val_mean = 0.10120637467108055
- gp_max_val_min = 0.05938141074611662
- high_power = 0.05424563214563214
- gp_auc_mean = 0.050650183150183145
- diff_auc = 0.04742840166369578
- coe3[2] = 0.03270620490620491
- hlbr = 0.026571279597595386
- coe3[3] = 0.025416941881647764
- coe1[0] = 0.02173838383838384
- diff_std = 0.02140392156862745
- srmr = 0.019639682539682544
- gp_max_val_std = 0.016923351158645277
- gp_max_val_range = 0.015061327561327562
- ac_auc = 0.01373001443001443
- coe1[1] = 0.013129403929403928
- gp_auc_range = 0.012977777777777779
- ac_std = 0.012914141414141413
- low_power = 0.012305772005772007
- ratio_max_to_10ms_ave_peaks = 0.011466666666666667
- gp_max_ix_mean = 0.010606334841628961
- gp_auc_std = 0.009947712418300659
- gp_max_ix_std = 0.00936767676767677
- tdoa_max = 0.008833333333333334
- tdoa_range = 0.008750971250971254
- tdoa_mean = 0.00824051504051504
- tdoa_std = 0.007062271062271061
- ratio_max_to_9th_ave_peaks = 0.006800000000000001
- gp_max_ix_max = 0.003703496503496505
- gp_max_ix_range = 0.0029333333333333355
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

      