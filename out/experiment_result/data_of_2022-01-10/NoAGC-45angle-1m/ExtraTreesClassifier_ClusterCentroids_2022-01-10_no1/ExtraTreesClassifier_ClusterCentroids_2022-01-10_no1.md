# ExtraTreesClassifier_ClusterCentroids_2022-01-10_no1
## Constants
- CSV_PATH = ../out/csv/experiment
- OUTPUT_PATH = ../out/experiment_result/data_of_2022-01-10/NoAGC-45angle-1m
- FEATURE_ATTRBS = ['low_power', 'high_power', 'hlbr', 'coe1[0]', 'coe1[1]', 'coe3[0]', 'coe3[1]', 'coe3[2]', 'coe3[3]', 'ratio_max_to_10ms_ave_peaks', 'ratio_max_to_9th_ave_peaks', 'ac_std', 'ac_auc', 'diff_std', 'diff_auc', 'srmr', 'gp_max_val_std', 'gp_max_val_range', 'gp_max_val_min', 'gp_max_val_max', 'gp_max_val_mean', 'gp_max_ix_std', 'gp_max_ix_range', 'gp_max_ix_min', 'gp_max_ix_max', 'gp_max_ix_mean', 'gp_auc_std', 'gp_auc_range', 'gp_auc_min', 'gp_auc_max', 'gp_auc_mean', 'tdoa_std', 'tdoa_range', 'tdoa_min', 'tdoa_max', 'tdoa_mean']
- LABEL_ATTRB = ['facing2']
- FACING_DOV_ANGLES = [1, 2]
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
	- sampling_strategy_ = OrderedDict([(1, 24)])
	- estimator_ = KMeans(n_clusters=24, random_state=42)
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
	- min_samples_split = 5
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
- gp_auc_max = 0.11186257574664947
- gp_max_val_mean = 0.1101088267940934
- gp_auc_mean = 0.08292259025107018
- tdoa_range = 0.07882248920783912
- gp_max_val_max = 0.07877476846614176
- gp_max_ix_range = 0.06622401002725856
- tdoa_min = 0.05204911023288203
- gp_auc_min = 0.04904514672248601
- gp_max_val_min = 0.04664887271659566
- gp_max_ix_min = 0.039519598712169035
- gp_max_ix_std = 0.03102195720585086
- ratio_max_to_10ms_ave_peaks = 0.03068634362579098
- hlbr = 0.02907145297728546
- tdoa_mean = 0.026655504300225917
- tdoa_std = 0.02627852637453186
- srmr = 0.02544196776110595
- gp_max_ix_mean = 0.01851550023262159
- gp_max_val_range = 0.015303992084987133
- gp_max_val_std = 0.014623737084861534
- gp_auc_range = 0.014456024596196977
- gp_auc_std = 0.008465270569719949
- diff_auc = 0.006813260565404683
- diff_std = 0.00629364479806525
- coe1[1] = 0.004689793750574313
- high_power = 0.00422054148800889
- tdoa_max = 0.004190502867644812
- coe3[3] = 0.003935532640932478
- low_power = 0.002869187227226025
- ac_std = 0.0025949745031524077
- ac_auc = 0.0020305988041647524
- coe1[0] = 0.0018577762595553113
- ratio_max_to_9th_ave_peaks = 0.001577600156194125
- coe3[2] = 0.0013962613893696819
- gp_max_ix_max = 0.00103205985934386
- coe3[0] = 0.0
- coe3[1] = 0.0

## Evaluation
cv = 8
### accuracy
- Scores = [ 0.8, 1.0, 1.0, 1.0, 0.8888888888888888, 1.0, 1.0, 0.7777777777777778 ]
- Mean = 0.9333333333333333
- Standard deviation = 0.0909483641319161

### balanced_accuracy
- Scores = [ 0.8, 1.0, 1.0, 1.0, 0.9, 1.0, 1.0, 0.8 ]
- Mean = 0.9375
- Standard deviation = 0.08569568250501304

### f1
- Scores = [ 0.8333333333333333, 1.0, 1.0, 1.0, 0.888888888888889, 1.0, 1.0, 0.8 ]
- Mean = 0.9402777777777778
- Standard deviation = 0.08030372514152091

### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 32 | 4 |
| Actual Positive | 1 | 38 |

      