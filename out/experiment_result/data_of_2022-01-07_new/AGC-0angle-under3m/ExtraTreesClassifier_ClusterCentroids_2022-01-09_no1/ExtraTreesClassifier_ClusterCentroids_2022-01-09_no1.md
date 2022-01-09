# ExtraTreesClassifier_ClusterCentroids_2022-01-09_no1
## Constants
- CSV_PATH = ../out/csv/experiment
- OUTPUT_PATH = ../out/experiment_result/data_of_2022-01-07_new/AGC-0angle-under3m
- FEATURE_ATTRBS = ['low_power', 'high_power', 'hlbr', 'coe1[0]', 'coe1[1]', 'coe3[0]', 'coe3[1]', 'coe3[2]', 'coe3[3]', 'ratio_max_to_10ms_ave_peaks', 'ratio_max_to_9th_ave_peaks', 'ac_std', 'ac_auc', 'diff_std', 'diff_auc', 'srmr', 'gp_max_val_std', 'gp_max_val_range', 'gp_max_val_min', 'gp_max_val_max', 'gp_max_val_mean', 'gp_max_ix_std', 'gp_max_ix_range', 'gp_max_ix_min', 'gp_max_ix_max', 'gp_max_ix_mean', 'gp_auc_std', 'gp_auc_range', 'gp_auc_min', 'gp_auc_max', 'gp_auc_mean', 'tdoa_std', 'tdoa_range', 'tdoa_min', 'tdoa_max', 'tdoa_mean']
- LABEL_ATTRB = ['facing']
- FACING_DOV_ANGLES = [1]
- NCV = 8
- SCORING = ['accuracy', 'balanced_accuracy', 'f1']
- REFIT_SCORING = balanced_accuracy
- PARAM_GRID = [{'est__n_estimators': [50, 100, 150, 200, 300], 'est__min_samples_split': [2, 5, 10], 'est__min_samples_leaf': [1, 5, 10], 'est__max_features': ['sqrt', 'log2', None], 'est__bootstrap': [False], 'est__n_jobs': [-1], 'est__random_state': [42], 'est__max_samples': [0.01, 0.5, 0.09]}, {'est__n_estimators': [50, 100, 150, 200, 300], 'est__min_samples_split': [2, 5, 10], 'est__min_samples_leaf': [1, 5, 10], 'est__max_features': ['sqrt', 'log2', None], 'est__bootstrap': [True], 'est__oob_score': [True, False], 'est__n_jobs': [-1], 'est__random_state': [42], 'est__max_samples': [0.01, 0.5, 0.09]}]
- TRAIN_SET_SESSION = ['trial1', 'trial2']
- TEST_SET_SESSION = ['trial3', 'trial4', 'trial5']
- DISTANCE = [1, 3]
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
	- sampling_strategy_ = OrderedDict([(0, 20)])
	- estimator_ = KMeans(n_clusters=20, random_state=42)
	- voting_ = soft

- best_estimator
	- base_estimator = ExtraTreeClassifier()
	- n_estimators = 150
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
	- max_features = None
	- max_leaf_nodes = None
	- min_impurity_decrease = 0.0
	- ccp_alpha = 0.0
	- n_features_in_ = 36
	- n_outputs_ = 1
	- classes_ = [0 1]
	- n_classes_ = 2
	- base_estimator_ = ExtraTreeClassifier()

#### Importance of features
- gp_max_val_min = 0.18722586751592826
- gp_max_val_mean = 0.1751236199817614
- gp_auc_min = 0.16249301470299846
- gp_auc_mean = 0.14733344135749687
- gp_max_val_max = 0.1227343328299188
- gp_auc_max = 0.10895051126243761
- srmr = 0.02375634366349628
- diff_auc = 0.020754957953974678
- diff_std = 0.013979205998396867
- high_power = 0.0054718594211800725
- gp_max_val_std = 0.0047104816101013035
- gp_max_val_range = 0.003977335322450333
- hlbr = 0.003495717290188445
- coe3[3] = 0.002488688669019431
- gp_auc_std = 0.002439923826861276
- ac_auc = 0.0024292595826209277
- gp_auc_range = 0.0018768791036401576
- gp_max_ix_mean = 0.0016507580011229654
- gp_max_ix_range = 0.0014081057831057836
- tdoa_range = 0.0011713795966275889
- gp_max_ix_max = 0.0011658876174560563
- coe1[0] = 0.0009019986203579913
- ratio_max_to_10ms_ave_peaks = 0.0008819163292847501
- coe1[1] = 0.0008740207151329797
- low_power = 0.0008727431750901729
- ratio_max_to_9th_ave_peaks = 0.0008651527894589287
- tdoa_max = 0.000293594935818949
- ac_std = 0.00018270507712738745
- tdoa_mean = 0.0001666666666666669
- gp_max_ix_std = 0.00011986301369863008
- tdoa_std = 0.00011718749999999994
- coe3[2] = 8.658008658008677e-05
- coe3[0] = 0.0
- coe3[1] = 0.0
- gp_max_ix_min = 0.0
- tdoa_min = 0.0

## Evaluation
cv = 8
### accuracy
- Scores = [ 0.5789473684210527, 0.6842105263157895, 0.7368421052631579, 0.6842105263157895, 0.9473684210526315, 0.6842105263157895, 0.5555555555555556, 0.8333333333333334 ]
- Mean = 0.7130847953216374
- Standard deviation = 0.12001167592359706

### balanced_accuracy
- Scores = [ 0.7333333333333334, 0.8, 0.8333333333333333, 0.8, 0.9666666666666667, 0.8, 0.4666666666666667, 0.9 ]
- Mean = 0.7875000000000001
- Standard deviation = 0.13838101587846344

### f1
- Scores = [ 0.5, 0.5714285714285715, 0.6153846153846153, 0.5714285714285715, 0.888888888888889, 0.5714285714285715, 0.2, 0.6666666666666666 ]
- Mean = 0.5731532356532356
- Standard deviation = 0.1784730058381186

### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 83 | 37 |
| Actual Positive | 2 | 28 |

      