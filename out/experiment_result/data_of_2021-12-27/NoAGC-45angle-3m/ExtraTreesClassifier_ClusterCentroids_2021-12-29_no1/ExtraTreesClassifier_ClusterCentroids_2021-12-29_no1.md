# ExtraTreesClassifier_ClusterCentroids_2021-12-29_no1
## Constants
- CSV_PATH = ../out/csv/experiment
- OUTPUT_PATH = ../out/experiment_result/data_of_2021-12-27/NoAGC-45angle-3m
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
	- sampling_strategy_ = OrderedDict([(1, 18)])
	- estimator_ = KMeans(n_clusters=18, random_state=42)
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
	- min_samples_leaf = 5
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
- gp_auc_max = 0.1429619584303909
- gp_max_val_max = 0.1411823108157319
- gp_auc_min = 0.1252398331679644
- gp_max_val_mean = 0.10083209089855662
- gp_max_val_min = 0.09616905934947317
- high_power = 0.07556948053498984
- srmr = 0.05331424051150657
- diff_auc = 0.04133468992420199
- gp_auc_mean = 0.037150965826450943
- diff_std = 0.029141285450116766
- low_power = 0.027312122053430768
- hlbr = 0.02589051297423981
- ratio_max_to_10ms_ave_peaks = 0.01920761427483396
- gp_max_val_std = 0.011914832220867
- coe1[1] = 0.01180936450512831
- coe3[3] = 0.011787720930953618
- tdoa_max = 0.008785390310730713
- tdoa_mean = 0.008590959283953063
- gp_max_ix_mean = 0.008214170604360138
- gp_max_ix_max = 0.006304054388448006
- gp_max_ix_range = 0.005720945890333574
- tdoa_range = 0.0029549266006570333
- tdoa_std = 0.0023996129656506993
- ac_std = 0.0022172949002217304
- ac_auc = 0.0020354928090777144
- coe1[0] = 0.000849303135888504
- coe3[2] = 0.0008139321497103711
- gp_max_val_range = 0.00012183235867446461
- gp_auc_range = 0.00011185343308116517
- gp_auc_std = 6.21493003764495e-05
- coe3[0] = 0.0
- coe3[1] = 0.0
- ratio_max_to_9th_ave_peaks = 0.0
- gp_max_ix_std = 0.0
- gp_max_ix_min = 0.0
- tdoa_min = 0.0

## Evaluation
cv = 8
### accuracy
- Scores = [ 1.0, 0.875, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0 ]
- Mean = 0.984375
- Standard deviation = 0.04133986423538423

### balanced_accuracy
- Scores = [ 1.0, 0.875, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0 ]
- Mean = 0.984375
- Standard deviation = 0.04133986423538423

### f1
- Scores = [ 1.0, 0.8571428571428571, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0 ]
- Mean = 0.9821428571428572
- Standard deviation = 0.047245559126153414

### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 27 | 0 |
| Actual Positive | 1 | 32 |

      