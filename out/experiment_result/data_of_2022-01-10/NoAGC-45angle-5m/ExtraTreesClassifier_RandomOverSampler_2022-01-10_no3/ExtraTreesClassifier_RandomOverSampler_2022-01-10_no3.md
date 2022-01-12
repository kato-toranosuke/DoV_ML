# ExtraTreesClassifier_RandomOverSampler_2022-01-10_no3
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
- resampler = RandomOverSampler
- estimator = ExtraTreesClassifier

### Arguments for hyperparameter search
- resampler = RandomOverSampler
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
	- shrinkage = None
	- n_features_in_ = 36
	- sampling_strategy_ = OrderedDict([(0, 2)])
	- shrinkage_ = None
	- sample_indices_ = [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23
 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47
 48 49 16 41]

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
	- oob_decision_function_ = [[0.1875     0.8125    ]
 [0.         1.        ]
 [0.         1.        ]
 [0.         1.        ]
 [0.77419355 0.22580645]
 [0.875      0.125     ]
 [1.         0.        ]
 [1.         0.        ]
 [1.         0.        ]
 [1.         0.        ]
 [0.38709677 0.61290323]
 [0.48484848 0.51515152]
 [0.         1.        ]
 [0.08333333 0.91666667]
 [0.08333333 0.91666667]
 [0.         1.        ]
 [0.70833333 0.29166667]
 [0.78125    0.21875   ]
 [1.         0.        ]
 [1.         0.        ]
 [1.         0.        ]
 [0.94117647 0.05882353]
 [0.24242424 0.75757576]
 [0.13793103 0.86206897]
 [0.04166667 0.95833333]
 [0.         1.        ]
 [0.         1.        ]
 [0.         1.        ]
 [0.27272727 0.72727273]
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
 [0.25       0.75      ]
 [0.26923077 0.73076923]
 [0.03571429 0.96428571]
 [0.16666667 0.83333333]
 [0.77419355 0.22580645]
 [1.         0.        ]]
	- oob_score_ = 0.9807692307692307

#### Importance of features
- srmr = 0.1571569840057235
- gp_auc_mean = 0.14860367083896495
- gp_max_val_min = 0.11994069264069265
- gp_max_val_max = 0.10665702947845805
- gp_max_val_mean = 0.10649490549010673
- gp_auc_min = 0.09046310969732023
- gp_auc_max = 0.06826643990929705
- hlbr = 0.04337876012876013
- tdoa_range = 0.02288888888888889
- gp_max_val_std = 0.02238428238428239
- gp_auc_std = 0.019705215419501133
- gp_max_ix_min = 0.018364135864135864
- high_power = 0.01661111111111111
- tdoa_min = 0.013099103277674704
- gp_max_val_range = 0.01302197802197802
- coe3[3] = 0.010943130072541836
- gp_max_ix_range = 0.004648287385129489
- coe1[0] = 0.0044047619047619035
- ac_std = 0.002857142857142858
- diff_auc = 0.0023636363636363638
- tdoa_std = 0.0020634920634920633
- diff_std = 0.001954887218045113
- coe1[1] = 0.0016250000000000001
- ratio_max_to_9th_ave_peaks = 0.0013295454545454546
- gp_auc_range = 0.0007738095238095242
- low_power = 0.0
- coe3[0] = 0.0
- coe3[1] = 0.0
- coe3[2] = 0.0
- ratio_max_to_10ms_ave_peaks = 0.0
- ac_auc = 0.0
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

      