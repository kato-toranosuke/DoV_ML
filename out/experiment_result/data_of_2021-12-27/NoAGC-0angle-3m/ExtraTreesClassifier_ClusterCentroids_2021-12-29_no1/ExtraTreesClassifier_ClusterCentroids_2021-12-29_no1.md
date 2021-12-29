# ExtraTreesClassifier_ClusterCentroids_2021-12-29_no1
## Constants
- CSV_PATH = ../out/csv/experiment
- OUTPUT_PATH = ../out/experiment_result/data_of_2021-12-27/NoAGC-0angle-3m
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
	- sampling_strategy_ = OrderedDict([(0, 8)])
	- estimator_ = KMeans(random_state=42)
	- voting_ = soft

- best_estimator
	- base_estimator = ExtraTreeClassifier()
	- n_estimators = 50
	- estimator_params = ('criterion', 'max_depth', 'min_samples_split', 'min_samples_leaf', 'min_weight_fraction_leaf', 'max_features', 'max_leaf_nodes', 'min_impurity_decrease', 'min_impurity_split', 'random_state', 'ccp_alpha')
	- bootstrap = True
	- oob_score = True
	- n_jobs = -1
	- random_state = 42
	- verbose = 0
	- warm_start = False
	- class_weight = None
	- max_samples = 0.5
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
	- oob_decision_function_ = [[0.90625    0.09375   ]
 [0.9        0.1       ]
 [0.9        0.1       ]
 [0.78125    0.21875   ]
 [0.90322581 0.09677419]
 [0.75757576 0.24242424]
 [0.75       0.25      ]
 [0.62962963 0.37037037]
 [0.04545455 0.95454545]
 [0.11111111 0.88888889]
 [0.61290323 0.38709677]
 [0.2        0.8       ]
 [0.17857143 0.82142857]
 [0.16       0.84      ]
 [0.06060606 0.93939394]
 [0.1        0.9       ]]
	- oob_score_ = 0.9375

#### Importance of features
- high_power = 0.13422857142857142
- gp_auc_max = 0.1291984126984127
- gp_auc_min = 0.10800000000000001
- gp_auc_mean = 0.08730158730158731
- gp_max_val_min = 0.08520634920634923
- diff_auc = 0.0660952380952381
- gp_max_val_mean = 0.05683333333333333
- ac_std = 0.052000000000000005
- gp_max_val_max = 0.04333333333333333
- diff_std = 0.04
- ratio_max_to_10ms_ave_peaks = 0.03333333333333334
- coe3[3] = 0.027200000000000002
- tdoa_max = 0.023111111111111114
- gp_auc_range = 0.02177777777777778
- coe3[2] = 0.019111111111111106
- tdoa_min = 0.014920634920634916
- srmr = 0.012000000000000002
- gp_max_ix_std = 0.012000000000000002
- hlbr = 0.008888888888888889
- ac_auc = 0.008571428571428568
- ratio_max_to_9th_ave_peaks = 0.007999999999999998
- tdoa_range = 0.006666666666666667
- gp_max_val_range = 0.001333333333333332
- coe1[1] = 0.0008888888888888894
- low_power = 0.0
- coe1[0] = 0.0
- coe3[0] = 0.0
- coe3[1] = 0.0
- gp_max_val_std = 0.0
- gp_max_ix_range = 0.0
- gp_max_ix_min = 0.0
- gp_max_ix_max = 0.0
- gp_max_ix_mean = 0.0
- gp_auc_std = 0.0
- tdoa_std = 0.0
- tdoa_mean = 0.0

## Evaluation
cv = 8
### accuracy
- Scores = [ 0.75, 1.0, 0.625, 1.0, 0.7142857142857143, 0.5714285714285714, 1.0, 0.14285714285714285 ]
- Mean = 0.7254464285714286
- Standard deviation = 0.2738812907370935

### balanced_accuracy
- Scores = [ 0.8333333333333333, 1.0, 0.75, 1.0, 0.8333333333333333, 0.75, 1.0, 0.5 ]
- Mean = 0.8333333333333333
- Standard deviation = 0.1613743060919757

### f1
- Scores = [ 0.6666666666666666, 1.0, 0.5714285714285715, 1.0, 0.5, 0.4, 1.0, 0.25 ]
- Mean = 0.6735119047619047
- Standard deviation = 0.27715716882332075

### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 32 | 16 |
| Actual Positive | 0 | 12 |

      