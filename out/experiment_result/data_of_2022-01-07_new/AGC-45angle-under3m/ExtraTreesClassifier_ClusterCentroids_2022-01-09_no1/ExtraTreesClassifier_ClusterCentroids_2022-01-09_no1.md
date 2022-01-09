# ExtraTreesClassifier_ClusterCentroids_2022-01-09_no1
## Constants
- CSV_PATH = ../out/csv/experiment
- OUTPUT_PATH = ../out/experiment_result/data_of_2022-01-07_new/AGC-45angle-under3m
- FEATURE_ATTRBS = ['low_power', 'high_power', 'hlbr', 'coe1[0]', 'coe1[1]', 'coe3[0]', 'coe3[1]', 'coe3[2]', 'coe3[3]', 'ratio_max_to_10ms_ave_peaks', 'ratio_max_to_9th_ave_peaks', 'ac_std', 'ac_auc', 'diff_std', 'diff_auc', 'srmr', 'gp_max_val_std', 'gp_max_val_range', 'gp_max_val_min', 'gp_max_val_max', 'gp_max_val_mean', 'gp_max_ix_std', 'gp_max_ix_range', 'gp_max_ix_min', 'gp_max_ix_max', 'gp_max_ix_mean', 'gp_auc_std', 'gp_auc_range', 'gp_auc_min', 'gp_auc_max', 'gp_auc_mean', 'tdoa_std', 'tdoa_range', 'tdoa_min', 'tdoa_max', 'tdoa_mean']
- LABEL_ATTRB = ['facing2']
- FACING_DOV_ANGLES = [1, 2]
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
	- sampling_strategy_ = OrderedDict([(1, 48)])
	- estimator_ = KMeans(n_clusters=48, random_state=42)
	- voting_ = soft

- best_estimator
	- base_estimator = ExtraTreeClassifier()
	- n_estimators = 300
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
- gp_max_val_min = 0.13089847540143779
- gp_auc_min = 0.12987786212931618
- gp_max_val_mean = 0.11435615121285035
- gp_auc_mean = 0.10636170806704658
- gp_auc_max = 0.07450699303759774
- gp_max_val_max = 0.07288876645790278
- diff_std = 0.0488342736465625
- srmr = 0.048502103565152395
- diff_auc = 0.0384631293368759
- hlbr = 0.027039281587114754
- ratio_max_to_10ms_ave_peaks = 0.02118709680371609
- high_power = 0.019923827530073778
- coe1[1] = 0.018275490944733446
- coe1[0] = 0.012762389479059144
- low_power = 0.012144145417470028
- gp_max_ix_std = 0.010172269018623583
- coe3[3] = 0.009348175983557758
- tdoa_std = 0.00901071236147928
- gp_max_ix_mean = 0.008982515810339754
- coe3[2] = 0.00890175508622163
- tdoa_mean = 0.007963471080747781
- gp_max_ix_range = 0.007487299053634984
- gp_max_val_range = 0.006919720129307813
- ratio_max_to_9th_ave_peaks = 0.006889874353956236
- gp_auc_std = 0.006609445407374653
- ac_std = 0.006411557161257929
- tdoa_range = 0.0060879456576807345
- gp_auc_range = 0.006073535316982252
- ac_auc = 0.005810225551164993
- gp_max_val_std = 0.00544437933751431
- tdoa_min = 0.005067044474354237
- gp_max_ix_min = 0.0036559790567884847
- gp_max_ix_max = 0.0016582313162684184
- tdoa_max = 0.001484169225835893
- coe3[0] = 0.0
- coe3[1] = 0.0

## Evaluation
cv = 8
### accuracy
- Scores = [ 0.8421052631578947, 1.0, 1.0, 0.9473684210526315, 1.0, 1.0, 1.0, 1.0 ]
- Mean = 0.9736842105263157
- Standard deviation = 0.05263157894736844

### balanced_accuracy
- Scores = [ 0.8333333333333333, 1.0, 1.0, 0.95, 1.0, 1.0, 1.0, 1.0 ]
- Mean = 0.9729166666666667
- Standard deviation = 0.055237806598178577

### f1
- Scores = [ 0.8695652173913044, 1.0, 1.0, 0.9473684210526316, 1.0, 1.0, 1.0, 1.0 ]
- Mean = 0.9771167048054921
- Standard deviation = 0.044150529477287696

### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 69 | 3 |
| Actual Positive | 1 | 77 |

      