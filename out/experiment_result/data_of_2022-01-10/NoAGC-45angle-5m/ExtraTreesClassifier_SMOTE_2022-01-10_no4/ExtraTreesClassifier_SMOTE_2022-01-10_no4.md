# ExtraTreesClassifier_SMOTE_2022-01-10_no4
## Constants
- CSV_PATH = ../out/csv/experiment
- OUTPUT_PATH = ../out/experiment_result/data_of_2022-01-10/NoAGC-45angle-5m
- FEATURE_ATTRBS = ['low_power', 'high_power', 'hlbr', 'coe1[0]', 'coe1[1]', 'coe3[0]', 'coe3[1]', 'coe3[2]', 'coe3[3]', 'ratio_max_to_10ms_ave_peaks', 'ratio_max_to_9th_ave_peaks', 'ac_std', 'ac_auc', 'diff_std', 'diff_auc', 'srmr', 'gp_max_val_std', 'gp_max_val_range', 'gp_max_val_min', 'gp_max_val_max', 'gp_max_val_mean', 'gp_max_ix_std', 'gp_max_ix_range', 'gp_max_ix_min', 'gp_max_ix_max', 'gp_max_ix_mean', 'gp_auc_std', 'gp_auc_range', 'gp_auc_min', 'gp_auc_max', 'gp_auc_mean', 'tdoa_std', 'tdoa_range', 'tdoa_min', 'tdoa_max', 'tdoa_mean']
- LABEL_ATTRB = ['facing2']
- FACING_DOV_ANGLES = [1, 2]
- NCV = 8
- SCORING = ['accuracy', 'balanced_accuracy', 'f1']
- REFIT_SCORING = balanced_accuracy
- PARAM_GRID = [{'est__n_estimators': [50, 100, 150, 200, 300], 'est__min_samples_split': [2, 5, 10], 'est__min_samples_leaf': [1, 5, 10], 'est__max_features': ['sqrt', 'log2', None], 'est__bootstrap': [False], 'est__n_jobs': [-1], 'est__random_state': [42], 'est__max_samples': [0.01, 0.5, 0.09]}, {'est__n_estimators': [50, 100, 150, 200, 300], 'est__min_samples_split': [2, 5, 10], 'est__min_samples_leaf': [1, 5, 10], 'est__max_features': ['sqrt', 'log2', None], 'est__bootstrap': [True], 'est__oob_score': [True, False], 'est__n_jobs': [-1], 'est__random_state': [42], 'est__max_samples': [0.01, 0.5, 0.09]}]
- TRAIN_SET_SESSION = ['trial1', 'trial2']
- TEST_SET_SESSION = ['trial3', 'trial4', 'trial5']
- DISTANCE = [5]
- AGC_STATUS = ['NoAGC']

## Loaded CSV
- 2022-01-10_raspi_48000Hz_w1_N2^12_overlap80.csv

## Estimator
### Type
- resampler = SMOTE
- estimator = ExtraTreesClassifier

### Arguments for hyperparameter search
- resampler = SMOTE
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
	- k_neighbors = 5
	- n_jobs = -1
	- n_features_in_ = 36
	- sampling_strategy_ = OrderedDict([(0, 2)])
	- nn_k_ = NearestNeighbors(n_neighbors=6)

- best_estimator
	- base_estimator = ExtraTreeClassifier()
	- n_estimators = 50
	- estimator_params = ('criterion', 'max_depth', 'min_samples_split', 'min_samples_leaf', 'min_weight_fraction_leaf', 'max_features', 'max_leaf_nodes', 'min_impurity_decrease', 'random_state', 'ccp_alpha')
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
	- max_features = None
	- max_leaf_nodes = None
	- min_impurity_decrease = 0.0
	- ccp_alpha = 0.0
	- n_features_in_ = 36
	- n_outputs_ = 1
	- classes_ = [0 1]
	- n_classes_ = 2
	- base_estimator_ = ExtraTreeClassifier()
	- oob_decision_function_ = [[0.21875    0.78125   ]
 [0.         1.        ]
 [0.         1.        ]
 [0.         1.        ]
 [0.77419355 0.22580645]
 [0.84375    0.15625   ]
 [1.         0.        ]
 [1.         0.        ]
 [1.         0.        ]
 [1.         0.        ]
 [0.29032258 0.70967742]
 [0.45454545 0.54545455]
 [0.         1.        ]
 [0.04166667 0.95833333]
 [0.05555556 0.94444444]
 [0.         1.        ]
 [0.5        0.5       ]
 [0.71875    0.28125   ]
 [1.         0.        ]
 [1.         0.        ]
 [1.         0.        ]
 [0.94117647 0.05882353]
 [0.21212121 0.78787879]
 [0.13793103 0.86206897]
 [0.04166667 0.95833333]
 [0.         1.        ]
 [0.         1.        ]
 [0.         1.        ]
 [0.3030303  0.6969697 ]
 [0.96296296 0.03703704]
 [1.         0.        ]
 [1.         0.        ]
 [0.94117647 0.05882353]
 [0.92592593 0.07407407]
 [0.12903226 0.87096774]
 [0.27586207 0.72413793]
 [0.         1.        ]
 [0.09090909 0.90909091]
 [0.         1.        ]
 [0.03448276 0.96551724]
 [1.         0.        ]
 [1.         0.        ]
 [1.         0.        ]
 [1.         0.        ]
 [1.         0.        ]
 [1.         0.        ]
 [0.28125    0.71875   ]
 [0.26923077 0.73076923]
 [0.07142857 0.92857143]
 [0.16666667 0.83333333]
 [1.         0.        ]
 [0.78571429 0.21428571]]
	- oob_score_ = 0.9807692307692307

#### Importance of features
- srmr = 0.18049172598332267
- gp_auc_mean = 0.1401433533786475
- gp_max_val_mean = 0.11763582820688083
- gp_auc_min = 0.10995755414176468
- gp_max_val_max = 0.10052280912364946
- gp_auc_max = 0.09267042606516292
- gp_max_val_min = 0.07962481962481963
- hlbr = 0.03916579716579717
- gp_max_val_std = 0.023960039960039967
- tdoa_range = 0.02288888888888889
- gp_max_ix_min = 0.02032750582750583
- high_power = 0.01661111111111111
- gp_auc_std = 0.014288548752834467
- coe3[3] = 0.011455950585362347
- tdoa_min = 0.011179911358482786
- coe1[0] = 0.0044047619047619035
- ac_std = 0.002857142857142858
- gp_max_val_range = 0.002307692307692308
- tdoa_std = 0.0020634920634920633
- diff_std = 0.001954887218045113
- gp_max_ix_range = 0.0017593984962406006
- coe1[1] = 0.0016250000000000001
- ratio_max_to_9th_ave_peaks = 0.0013295454545454546
- gp_auc_range = 0.0007738095238095242
- low_power = 0.0
- coe3[0] = 0.0
- coe3[1] = 0.0
- coe3[2] = 0.0
- ratio_max_to_10ms_ave_peaks = 0.0
- ac_auc = 0.0
- diff_auc = 0.0
- gp_max_ix_std = 0.0
- gp_max_ix_max = 0.0
- gp_max_ix_mean = 0.0
- tdoa_max = 0.0
- tdoa_mean = 0.0

## Evaluation
cv = 8
### accuracy
- Scores = [ 0.9, 0.8, 0.8, 0.7777777777777778, 0.8888888888888888, 1.0, 0.8888888888888888, 1.0 ]
- Mean = 0.8819444444444444
- Standard deviation = 0.08106876748618047

### balanced_accuracy
- Scores = [ 0.9, 0.8, 0.8, 0.8, 0.875, 1.0, 0.9, 1.0 ]
- Mean = 0.884375
- Standard deviation = 0.07799989983967927

### f1
- Scores = [ 0.9090909090909091, 0.7499999999999999, 0.8333333333333333, 0.7499999999999999, 0.9090909090909091, 1.0, 0.888888888888889, 1.0 ]
- Mean = 0.880050505050505
- Standard deviation = 0.09120672377958691

### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 34 | 2 |
| Actual Positive | 3 | 36 |

      