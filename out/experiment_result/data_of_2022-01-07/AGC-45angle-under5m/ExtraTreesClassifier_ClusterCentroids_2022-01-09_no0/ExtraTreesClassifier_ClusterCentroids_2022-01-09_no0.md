# ExtraTreesClassifier_ClusterCentroids_2022-01-09_no0
## Constants
- CSV_PATH = ../out/csv/experiment
- OUTPUT_PATH = ../out/experiment_result/data_of_2022-01-07/AGC-45angle-under5m
- FEATURE_ATTRBS = ['low_power', 'high_power', 'hlbr', 'coe1[0]', 'coe1[1]', 'coe3[0]', 'coe3[1]', 'coe3[2]', 'coe3[3]', 'ratio_max_to_10ms_ave_peaks', 'ratio_max_to_9th_ave_peaks', 'ac_std', 'ac_auc', 'diff_std', 'diff_auc', 'srmr', 'gp_max_val_std', 'gp_max_val_range', 'gp_max_val_min', 'gp_max_val_max', 'gp_max_val_mean', 'gp_max_ix_std', 'gp_max_ix_range', 'gp_max_ix_min', 'gp_max_ix_max', 'gp_max_ix_mean', 'gp_auc_std', 'gp_auc_range', 'gp_auc_min', 'gp_auc_max', 'gp_auc_mean', 'tdoa_std', 'tdoa_range', 'tdoa_min', 'tdoa_max', 'tdoa_mean']
- LABEL_ATTRB = ['facing2']
- FACING_DOV_ANGLES = [1, 2]
- NCV = 8
- SCORING = ['accuracy', 'balanced_accuracy', 'f1']
- REFIT_SCORING = balanced_accuracy
- PARAM_GRID = [{'est__n_estimators': [50, 100, 150, 200, 300], 'est__min_samples_split': [2, 5, 10], 'est__min_samples_leaf': [1, 5, 10], 'est__max_features': ['sqrt', 'log2', None], 'est__bootstrap': [False], 'est__n_jobs': [-1], 'est__random_state': [42], 'est__max_samples': [0.01, 0.5, 0.09]}, {'est__n_estimators': [50, 100, 150, 200, 300], 'est__min_samples_split': [2, 5, 10], 'est__min_samples_leaf': [1, 5, 10], 'est__max_features': ['sqrt', 'log2', None], 'est__bootstrap': [True], 'est__oob_score': [True, False], 'est__n_jobs': [-1], 'est__random_state': [42], 'est__max_samples': [0.01, 0.5, 0.09]}]
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
	- sampling_strategy_ = OrderedDict([(1, 72)])
	- estimator_ = KMeans(n_clusters=72, random_state=42)
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
- gp_auc_min = 0.10542175483343037
- gp_auc_max = 0.09253547647028379
- gp_max_val_min = 0.08976005731307515
- high_power = 0.07572394289929406
- diff_auc = 0.0696642569847004
- gp_auc_mean = 0.06730026219494861
- gp_max_val_max = 0.055315858313097654
- gp_max_val_mean = 0.05075494708168936
- diff_std = 0.041925213111215234
- coe1[1] = 0.03116124269500678
- coe1[0] = 0.03032351260094601
- srmr = 0.024881780779776944
- hlbr = 0.02434215114972814
- low_power = 0.022279133416937283
- coe3[3] = 0.02042675423075746
- ratio_max_to_10ms_ave_peaks = 0.01778878767402805
- gp_max_ix_mean = 0.01735685258140112
- coe3[2] = 0.013354408313951259
- gp_max_ix_min = 0.012900935574379734
- gp_max_ix_range = 0.012409782220036447
- tdoa_range = 0.012341220165654105
- gp_max_val_std = 0.010450802498475178
- tdoa_mean = 0.010239096634905003
- gp_max_val_range = 0.010200966467115855
- tdoa_std = 0.00979522819845772
- gp_auc_range = 0.009551857093523759
- gp_max_ix_std = 0.009463936361651642
- ac_auc = 0.009450472980868284
- gp_auc_std = 0.009403345243897495
- ac_std = 0.008652758550648674
- tdoa_min = 0.00823663078025823
- ratio_max_to_9th_ave_peaks = 0.006908454834925424
- tdoa_max = 0.004896363649206397
- gp_max_ix_max = 0.004781756101728427
- coe3[0] = 0.0
- coe3[1] = 0.0

## Evaluation
cv = 8
### accuracy
- Scores = [ 0.896551724137931, 0.9642857142857143, 0.9285714285714286, 0.9642857142857143, 0.8928571428571429, 1.0, 1.0, 1.0 ]
- Mean = 0.9558189655172413
- Standard deviation = 0.04215816702657617

### balanced_accuracy
- Scores = [ 0.8928571428571428, 0.9666666666666667, 0.9333333333333333, 0.9666666666666667, 0.9, 1.0, 1.0, 1.0 ]
- Mean = 0.9574404761904762
- Standard deviation = 0.0413154843373734

### f1
- Scores = [ 0.9090909090909091, 0.9655172413793104, 0.9285714285714286, 0.9655172413793104, 0.888888888888889, 1.0, 1.0, 1.0 ]
- Mean = 0.9571982136637309
- Standard deviation = 0.040979202978721416

### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 104 | 4 |
| Actual Positive | 7 | 110 |

      