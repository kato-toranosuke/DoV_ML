# ExtraTreesClassifier_SMOTEENN_2022-01-09_no5
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
- resampler = SMOTEENN
- estimator = ExtraTreesClassifier

### Arguments for hyperparameter search
- resampler = SMOTEENN
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
	- smote = None
	- enn = None
	- n_jobs = -1
	- n_features_in_ = 36
	- sampling_strategy_ = auto
	- smote_ = SMOTE(n_jobs=-1, random_state=42)
	- enn_ = EditedNearestNeighbours(n_jobs=-1, sampling_strategy='all')

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
	- oob_decision_function_ = [[0.78125    0.21875   ]
 [0.8        0.2       ]
 [0.03333333 0.96666667]
 [0.8125     0.1875    ]
 [0.90322581 0.09677419]
 [0.90909091 0.09090909]
 [0.34375    0.65625   ]
 [0.25925926 0.74074074]
 [0.         1.        ]
 [0.11111111 0.88888889]
 [0.12903226 0.87096774]
 [0.1        0.9       ]
 [0.         1.        ]
 [0.04       0.96      ]
 [0.15151515 0.84848485]
 [0.         1.        ]]
	- oob_score_ = 0.9375

#### Importance of features
- coe3[3] = 0.125
- ac_std = 0.10416666666666667
- gp_max_val_min = 0.08657407407407407
- gp_auc_min = 0.08333333333333333
- coe1[1] = 0.07407407407407407
- low_power = 0.06342592592592593
- coe3[2] = 0.0625
- ac_auc = 0.0625
- diff_auc = 0.0625
- tdoa_std = 0.0425
- gp_auc_mean = 0.041666666666666664
- gp_max_val_mean = 0.03333333333333333
- high_power = 0.020833333333333332
- coe1[0] = 0.020833333333333332
- ratio_max_to_10ms_ave_peaks = 0.020833333333333332
- srmr = 0.020833333333333332
- gp_max_ix_std = 0.012500000000000002
- gp_auc_max = 0.011574074074074075
- tdoa_range = 0.009259259259259259
- tdoa_mean = 0.009259259259259259
- ratio_max_to_9th_ave_peaks = 0.008333333333333333
- gp_max_ix_mean = 0.008333333333333333
- gp_max_val_max = 0.008333333333333331
- gp_max_ix_range = 0.007500000000000001
- hlbr = 0.0
- coe3[0] = 0.0
- coe3[1] = 0.0
- diff_std = 0.0
- gp_max_val_std = 0.0
- gp_max_val_range = 0.0
- gp_max_ix_min = 0.0
- gp_max_ix_max = 0.0
- gp_auc_std = 0.0
- gp_auc_range = 0.0
- tdoa_min = 0.0
- tdoa_max = 0.0

## Evaluation
cv = 8
### accuracy
- Scores = [ 0.8421052631578947, 0.47368421052631576, 0.8421052631578947, 0.7894736842105263, 0.7894736842105263, 1.0, 0.8888888888888888, 1.0 ]
- Mean = 0.8282163742690059
- Standard deviation = 0.1548310497897695

### balanced_accuracy
- Scores = [ 0.8333333333333333, 0.48888888888888893, 0.8444444444444444, 0.788888888888889, 0.7777777777777778, 1.0, 0.8888888888888888, 1.0 ]
- Mean = 0.8277777777777777
- Standard deviation = 0.1509230856356236

### f1
- Scores = [ 0.8695652173913044, 0.28571428571428575, 0.8421052631578948, 0.8000000000000002, 0.8333333333333333, 1.0, 0.9, 1.0 ]
- Mean = 0.8163397624496023
- Standard deviation = 0.21215477162631116

### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 58 | 14 |
| Actual Positive | 13 | 65 |

      