# ExtraTreesClassifier_NoResampler_2022-01-10_no0
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
- resampler = NoResampler
- estimator = ExtraTreesClassifier

### Arguments for hyperparameter search
- resampler = NoResampler
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
	- oob_decision_function_ = [[0.19354839 0.80645161]
 [0.         1.        ]
 [0.         1.        ]
 [0.         1.        ]
 [0.6875     0.3125    ]
 [0.71875    0.28125   ]
 [1.         0.        ]
 [1.         0.        ]
 [1.         0.        ]
 [1.         0.        ]
 [0.22580645 0.77419355]
 [0.36363636 0.63636364]
 [0.         1.        ]
 [0.04166667 0.95833333]
 [0.05555556 0.94444444]
 [0.         1.        ]
 [0.44       0.56      ]
 [0.59375    0.40625   ]
 [1.         0.        ]
 [1.         0.        ]
 [1.         0.        ]
 [0.94117647 0.05882353]
 [0.21875    0.78125   ]
 [0.13333333 0.86666667]
 [0.04166667 0.95833333]
 [0.         1.        ]
 [0.         1.        ]
 [0.         1.        ]
 [0.24242424 0.75757576]
 [0.92592593 0.07407407]
 [1.         0.        ]
 [1.         0.        ]
 [0.94117647 0.05882353]
 [0.92592593 0.07407407]
 [0.12903226 0.87096774]
 [0.25       0.75      ]
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
 [0.25925926 0.74074074]
 [0.06896552 0.93103448]
 [0.16       0.84      ]]
	- oob_score_ = 0.96

#### Importance of features
- srmr = 0.14963996115667974
- gp_auc_mean = 0.1417586834214508
- gp_auc_min = 0.12444658477221501
- gp_max_val_mean = 0.11353479749838293
- gp_max_val_max = 0.11070439364557012
- gp_auc_max = 0.09805122792248414
- gp_max_val_min = 0.07532788639931497
- hlbr = 0.045261086316281125
- gp_auc_std = 0.023375512739531073
- tdoa_range = 0.023030303030303033
- gp_max_ix_min = 0.018343323343323344
- high_power = 0.017320261437908498
- gp_max_val_std = 0.012144973082473082
- tdoa_min = 0.010884115884115884
- coe3[3] = 0.010837773337773336
- coe1[0] = 0.004578754578754579
- gp_max_ix_range = 0.004195906432748536
- gp_max_ix_std = 0.0030303030303030307
- ac_std = 0.002958579881656804
- gp_max_val_range = 0.002403846153846154
- diff_std = 0.0021929824561403508
- tdoa_std = 0.0021367521367521365
- coe1[1] = 0.0016666666666666668
- ratio_max_to_9th_ave_peaks = 0.0013636363636363642
- gp_auc_range = 0.000811688311688312
- low_power = 0.0
- coe3[0] = 0.0
- coe3[1] = 0.0
- coe3[2] = 0.0
- ratio_max_to_10ms_ave_peaks = 0.0
- ac_auc = 0.0
- diff_auc = 0.0
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

      