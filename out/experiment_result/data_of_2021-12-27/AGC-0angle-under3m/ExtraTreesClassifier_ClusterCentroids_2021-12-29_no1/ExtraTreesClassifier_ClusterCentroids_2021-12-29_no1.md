# ExtraTreesClassifier_ClusterCentroids_2021-12-29_no1
## Constants
- CSV_PATH = ../out/csv/experiment
- OUTPUT_PATH = ../out/experiment_result/data_of_2021-12-27/AGC-0angle-under3m
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
	- sampling_strategy_ = OrderedDict([(0, 20)])
	- estimator_ = KMeans(n_clusters=20, random_state=42)
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
	- min_samples_split = 5
	- min_samples_leaf = 1
	- min_weight_fraction_leaf = 0.0
	- max_features = log2
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
	- oob_decision_function_ = [[0.91935484 0.08064516]
 [0.89166667 0.10833333]
 [0.91066667 0.08933333]
 [0.64040404 0.35959596]
 [0.90104167 0.09895833]
 [0.31021505 0.68978495]
 [0.8734375  0.1265625 ]
 [0.85064103 0.14935897]
 [0.76785714 0.23214286]
 [0.8462963  0.1537037 ]
 [0.90645161 0.09354839]
 [0.13641457 0.86358543]
 [0.34358974 0.65641026]
 [0.86376812 0.13623188]
 [0.66527778 0.33472222]
 [0.70931373 0.29068627]
 [0.22179487 0.77820513]
 [0.75625    0.24375   ]
 [0.9202381  0.0797619 ]
 [0.86290323 0.13709677]
 [0.2045977  0.7954023 ]
 [0.13039216 0.86960784]
 [0.38277778 0.61722222]
 [0.47722222 0.52277778]
 [0.13478261 0.86521739]
 [0.27150538 0.72849462]
 [0.20820106 0.79179894]
 [0.21862245 0.78137755]
 [0.18080808 0.81919192]
 [0.1525641  0.8474359 ]
 [0.17277778 0.82722222]
 [0.41794872 0.58205128]
 [0.07714286 0.92285714]
 [0.14827586 0.85172414]
 [0.31034483 0.68965517]
 [0.33351648 0.66648352]
 [0.5057971  0.4942029 ]
 [0.15909091 0.84090909]
 [0.52258065 0.47741935]
 [0.23988095 0.76011905]]
	- oob_score_ = 0.85

#### Importance of features
- gp_auc_min = 0.13540564181689527
- gp_max_val_min = 0.10174653608325938
- gp_max_val_max = 0.099766417113918
- gp_auc_max = 0.08954196695638736
- gp_max_val_mean = 0.06521723571110954
- gp_auc_mean = 0.056939608569613734
- gp_max_ix_std = 0.04168704884741035
- gp_max_val_std = 0.03605101863016144
- tdoa_mean = 0.030802535589682246
- diff_auc = 0.03019271221439523
- diff_std = 0.028105417959241045
- coe1[1] = 0.025968696213425124
- tdoa_std = 0.023999009102574468
- srmr = 0.022779744455351053
- hlbr = 0.02225181095254534
- ratio_max_to_9th_ave_peaks = 0.020822348430843594
- low_power = 0.020344226730076458
- gp_max_ix_range = 0.019370435765784608
- coe1[0] = 0.013786946736684172
- ac_std = 0.01363315277034442
- gp_max_val_range = 0.013259923113574174
- high_power = 0.012815474283936836
- ratio_max_to_10ms_ave_peaks = 0.011048137421352243
- tdoa_max = 0.009306847302116372
- gp_auc_range = 0.00910200246412871
- gp_max_ix_min = 0.008574650076545476
- coe3[2] = 0.008108495855505646
- ac_auc = 0.007627526901085044
- tdoa_range = 0.007453749315818283
- tdoa_min = 0.006410256410256411
- gp_auc_std = 0.0028571428571428576
- gp_max_ix_max = 0.002502784739626846
- gp_max_ix_mean = 0.002160138248847926
- coe3[3] = 0.0003603603603603598
- coe3[0] = 0.0
- coe3[1] = 0.0

## Evaluation
cv = 8
### accuracy
- Scores = [ 0.5263157894736842, 0.6842105263157895, 0.7894736842105263, 0.6842105263157895, 0.8947368421052632, 0.5, 0.8333333333333334, 0.7222222222222222 ]
- Mean = 0.7043128654970761
- Standard deviation = 0.1297669046077611

### balanced_accuracy
- Scores = [ 0.7, 0.8, 0.8666666666666667, 0.8, 0.9333333333333333, 0.5892857142857143, 0.9, 0.7 ]
- Mean = 0.7861607142857143
- Standard deviation = 0.1090243813291612

### f1
- Scores = [ 0.47058823529411764, 0.5714285714285715, 0.6666666666666666, 0.5714285714285715, 0.8, 0.39999999999999997, 0.6666666666666666, 0.4444444444444444 ]
- Mean = 0.5739028944911297
- Standard deviation = 0.12550797102727815

### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 77 | 42 |
| Actual Positive | 2 | 28 |

      