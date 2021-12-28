# ExtraTreesClassifier_ClusterCentroids_2021-12-28_no1
## Constants
- CSV_PATH = ../out/csv/experiment
- OUTPUT_PATH = ../out/experiment_result
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
	- sampling_strategy_ = OrderedDict([(0, 30)])
	- estimator_ = KMeans(n_clusters=30, random_state=42)
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
	- min_samples_split = 10
	- min_samples_leaf = 1
	- min_weight_fraction_leaf = 0.0
	- max_features = None
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
- gp_max_val_min = 0.1949152426441282
- gp_auc_min = 0.14630294587060277
- gp_auc_mean = 0.11338275793431353
- gp_max_val_mean = 0.1048032767812857
- diff_std = 0.07744185769186847
- high_power = 0.068235584885579
- diff_auc = 0.0564649534936379
- gp_max_val_max = 0.05016561429177563
- gp_auc_max = 0.03932359719843915
- coe1[1] = 0.013702849953174211
- gp_max_ix_mean = 0.01256446808658883
- gp_max_ix_range = 0.012344419249295436
- ratio_max_to_9th_ave_peaks = 0.010177229657267419
- hlbr = 0.009076996871896252
- tdoa_min = 0.008973784077211722
- low_power = 0.008778704363839143
- gp_max_ix_max = 0.008734566672427122
- tdoa_range = 0.007974803488195677
- coe1[0] = 0.007182810602444381
- gp_max_ix_min = 0.0064111644325206335
- srmr = 0.006280391756557192
- ratio_max_to_10ms_ave_peaks = 0.006013087929026358
- coe3[3] = 0.005599809738504076
- tdoa_mean = 0.005253135923830913
- tdoa_max = 0.003775615985740369
- ac_auc = 0.0036199226670032563
- coe3[2] = 0.00302965613006181
- gp_auc_std = 0.0022634880363416104
- gp_max_val_range = 0.002064168810911676
- ac_std = 0.0020330242051173485
- gp_max_ix_std = 0.0018900364239937302
- tdoa_std = 0.000542418849055005
- gp_auc_range = 0.0005031966927143555
- gp_max_val_std = 0.00017441860465116288
- coe3[0] = 0.0
- coe3[1] = 0.0

## Evaluation
cv = 8
### accuracy
- Scores = [ 0.6428571428571429, 0.7857142857142857, 0.6785714285714286, 0.7142857142857143, 0.75, 0.5714285714285714, 0.9642857142857143, 0.8928571428571429 ]
- Mean = 0.75
- Standard deviation = 0.12111303541295122

### balanced_accuracy
- Scores = [ 0.7727272727272727, 0.8636363636363636, 0.6742424242424242, 0.8181818181818181, 0.8409090909090908, 0.7391304347826086, 0.9, 0.9347826086956521 ]
- Mean = 0.8179512516469039
- Standard deviation = 0.08054964665705806

### f1
- Scores = [ 0.5454545454545454, 0.6666666666666666, 0.4705882352941177, 0.6, 0.631578947368421, 0.45454545454545453, 0.888888888888889, 0.7692307692307693 ]
- Mean = 0.6283691884311079
- Standard deviation = 0.13783081439330264

### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 126 | 53 |
| Actual Positive | 3 | 42 |

      