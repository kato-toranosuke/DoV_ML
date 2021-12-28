# ExtraTreesClassifier_RandomOverSampler_2021-12-28_no10
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
	- sampling_strategy_ = OrderedDict([(1, 30)])
	- shrinkage_ = None
	- sample_indices_ = [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23
 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47
 48 49 36 13 37 24 36 49 12 36 37 24 13 37 37 12 25 24  1 37 25  1 24  0
 49 25 48  0 49 12 36 13]

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
	- max_samples = 0.09
	- criterion = gini
	- max_depth = None
	- min_samples_split = 2
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
	- oob_decision_function_ = [[0.30434783 0.69565217]
 [0.24489796 0.75510204]
 [0.36363636 0.63636364]
 [0.2173913  0.7826087 ]
 [0.30434783 0.69565217]
 [0.5106383  0.4893617 ]
 [0.7826087  0.2173913 ]
 [0.7826087  0.2173913 ]
 [0.7804878  0.2195122 ]
 [0.75       0.25      ]
 [0.28888889 0.71111111]
 [0.38297872 0.61702128]
 [0.21276596 0.78723404]
 [0.3255814  0.6744186 ]
 [0.30434783 0.69565217]
 [0.32608696 0.67391304]
 [0.80851064 0.19148936]
 [0.83673469 0.16326531]
 [0.9047619  0.0952381 ]
 [0.84090909 0.15909091]
 [0.76595745 0.23404255]
 [0.68085106 0.31914894]
 [0.38297872 0.61702128]
 [0.37777778 0.62222222]
 [0.4        0.6       ]
 [0.33333333 0.66666667]
 [0.45652174 0.54347826]
 [0.53191489 0.46808511]
 [0.8125     0.1875    ]
 [0.77777778 0.22222222]
 [0.8125     0.1875    ]
 [0.85416667 0.14583333]
 [0.69565217 0.30434783]
 [0.69565217 0.30434783]
 [0.32608696 0.67391304]
 [0.40425532 0.59574468]
 [0.13333333 0.86666667]
 [0.19148936 0.80851064]
 [0.57446809 0.42553191]
 [0.4893617  0.5106383 ]
 [0.86666667 0.13333333]
 [0.78571429 0.21428571]
 [0.85106383 0.14893617]
 [0.69047619 0.30952381]
 [0.60869565 0.39130435]
 [0.7173913  0.2826087 ]
 [0.46511628 0.53488372]
 [0.53191489 0.46808511]
 [0.61363636 0.38636364]
 [0.25       0.75      ]
 [0.13043478 0.86956522]
 [0.29166667 0.70833333]
 [0.19565217 0.80434783]
 [0.34042553 0.65957447]
 [0.13636364 0.86363636]
 [0.24444444 0.75555556]
 [0.23255814 0.76744186]
 [0.13333333 0.86666667]
 [0.18367347 0.81632653]
 [0.33333333 0.66666667]
 [0.34146341 0.65853659]
 [0.20454545 0.79545455]
 [0.19565217 0.80434783]
 [0.22222222 0.77777778]
 [0.3125     0.6875    ]
 [0.34042553 0.65957447]
 [0.26666667 0.73333333]
 [0.1875     0.8125    ]
 [0.30612245 0.69387755]
 [0.26666667 0.73333333]
 [0.34782609 0.65217391]
 [0.31818182 0.68181818]
 [0.23404255 0.76595745]
 [0.30612245 0.69387755]
 [0.58695652 0.41304348]
 [0.30434783 0.69565217]
 [0.25581395 0.74418605]
 [0.23255814 0.76744186]
 [0.12765957 0.87234043]
 [0.31111111 0.68888889]]
	- oob_score_ = 0.8

#### Importance of features
- gp_max_val_min = 0.09751157407407407
- ac_std = 0.08229166666666667
- ratio_max_to_10ms_ave_peaks = 0.06918402777777778
- gp_auc_min = 0.06649305555555556
- hlbr = 0.06510416666666667
- srmr = 0.06354166666666668
- gp_auc_mean = 0.057638888888888885
- gp_auc_max = 0.050173611111111106
- gp_max_val_mean = 0.04366319444444444
- gp_max_val_range = 0.04331597222222222
- gp_max_val_max = 0.041666666666666664
- gp_max_ix_range = 0.03194444444444445
- low_power = 0.029513888888888885
- gp_max_val_std = 0.029079861111111115
- ac_auc = 0.023871527777777776
- coe1[1] = 0.020833333333333332
- gp_auc_range = 0.020833333333333332
- tdoa_range = 0.020833333333333332
- tdoa_min = 0.020833333333333332
- gp_max_ix_min = 0.01944444444444444
- tdoa_mean = 0.018836805555555555
- tdoa_max = 0.011111111111111113
- gp_auc_std = 0.011111111111111112
- coe1[0] = 0.00972222222222222
- ratio_max_to_9th_ave_peaks = 0.00972222222222222
- diff_auc = 0.00972222222222222
- gp_max_ix_std = 0.00972222222222222
- tdoa_std = 0.00972222222222222
- coe3[2] = 0.006481481481481481
- coe3[3] = 0.006076388888888888
- high_power = 0.0
- coe3[0] = 0.0
- coe3[1] = 0.0
- diff_std = 0.0
- gp_max_ix_max = 0.0
- gp_max_ix_mean = 0.0

## Evaluation
cv = 8
### accuracy
- Scores = [ 0.4, 0.6, 0.8, 0.6666666666666666, 0.8888888888888888, 0.6666666666666666, 1.0, 1.0 ]
- Mean = 0.7527777777777778
- Standard deviation = 0.1954537298028031

### balanced_accuracy
- Scores = [ 0.625, 0.75, 0.875, 0.6071428571428572, 0.9285714285714286, 0.7857142857142857, 1.0, 1.0 ]
- Mean = 0.8214285714285714
- Standard deviation = 0.14534661246517594

### f1
- Scores = [ 0.4, 0.5, 0.6666666666666666, 0.4, 0.8, 0.5714285714285715, 1.0, 1.0 ]
- Mean = 0.6672619047619048
- Standard deviation = 0.22887427234113172

### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 42 | 18 |
| Actual Positive | 1 | 14 |

      