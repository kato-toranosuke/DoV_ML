# ExtraTreesClassifier_ClusterCentroids_2021-12-29_no1
## Constants
- CSV_PATH = ../out/csv/experiment
- OUTPUT_PATH = ../out/experiment_result/data_of_2021-12-27/NoAGC-45angle-under5m
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
- AGC_STATUS = ['NoAGC']

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
	- sampling_strategy_ = OrderedDict([(1, 54)])
	- estimator_ = KMeans(n_clusters=54, random_state=42)
	- voting_ = soft

- best_estimator
	- base_estimator = ExtraTreeClassifier()
	- n_estimators = 100
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
- gp_auc_min = 0.08696085980539058
- gp_max_val_mean = 0.08560253163844087
- gp_max_val_min = 0.07593231809070378
- gp_auc_mean = 0.0688329775111253
- gp_auc_max = 0.06406800955904329
- gp_max_val_max = 0.05047256776572713
- srmr = 0.04635202735740156
- diff_auc = 0.04259507291420024
- hlbr = 0.04184748067574642
- diff_std = 0.04106688801743723
- high_power = 0.04017748661165333
- ratio_max_to_10ms_ave_peaks = 0.030545398504114904
- tdoa_max = 0.02653115119293424
- gp_max_ix_max = 0.024364277373717592
- tdoa_range = 0.02319735386599924
- gp_max_ix_mean = 0.021149585010819795
- gp_max_ix_std = 0.01994684178599605
- tdoa_std = 0.019695461073003215
- low_power = 0.01661056958342158
- coe1[1] = 0.01649537954246327
- gp_max_ix_min = 0.01606160005398909
- tdoa_mean = 0.01582965993040285
- gp_max_val_range = 0.015469897296053076
- tdoa_min = 0.0145577804714267
- gp_max_ix_range = 0.014102430759749872
- coe3[3] = 0.01306852890673842
- coe1[0] = 0.011605256632345405
- gp_auc_std = 0.011465632048188424
- gp_max_val_std = 0.009349258420357665
- coe3[2] = 0.008474771117498192
- gp_auc_range = 0.007964128629044375
- ac_auc = 0.00768544142942721
- ratio_max_to_9th_ave_peaks = 0.007152458797397737
- ac_std = 0.004768917628041427
- coe3[0] = 0.0
- coe3[1] = 0.0

## Evaluation
cv = 8
### accuracy
- Scores = [ 0.9130434782608695, 1.0, 0.9130434782608695, 0.9545454545454546, 0.8636363636363636, 0.9090909090909091, 1.0, 0.9545454545454546 ]
- Mean = 0.9384881422924902
- Standard deviation = 0.044504128704669466

### balanced_accuracy
- Scores = [ 0.9, 1.0, 0.9166666666666667, 0.95, 0.85, 0.9083333333333333, 1.0, 0.9583333333333333 ]
- Mean = 0.9354166666666667
- Standard deviation = 0.04836744485934958

### f1
- Scores = [ 0.9285714285714286, 1.0, 0.9090909090909091, 0.9600000000000001, 0.888888888888889, 0.9166666666666666, 1.0, 0.9565217391304348 ]
- Mean = 0.9449674540435411
- Standard deviation = 0.03859782593566281

### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 74 | 7 |
| Actual Positive | 4 | 94 |

      