# ExtraTreesClassifier_RandomOverSampler_2022-01-08_no3
## Constants
- CSV_PATH = ../out/csv/experiment
- OUTPUT_PATH = ../out/experiment_result/data_of_2022-01-07/AGC-0angle-1m
- FEATURE_ATTRBS = ['low_power', 'high_power', 'hlbr', 'coe1[0]', 'coe1[1]', 'coe3[0]', 'coe3[1]', 'coe3[2]', 'coe3[3]', 'ratio_max_to_10ms_ave_peaks', 'ratio_max_to_9th_ave_peaks', 'ac_std', 'ac_auc', 'diff_std', 'diff_auc', 'srmr', 'gp_max_val_std', 'gp_max_val_range', 'gp_max_val_min', 'gp_max_val_max', 'gp_max_val_mean', 'gp_max_ix_std', 'gp_max_ix_range', 'gp_max_ix_min', 'gp_max_ix_max', 'gp_max_ix_mean', 'gp_auc_std', 'gp_auc_range', 'gp_auc_min', 'gp_auc_max', 'gp_auc_mean', 'tdoa_std', 'tdoa_range', 'tdoa_min', 'tdoa_max', 'tdoa_mean']
- LABEL_ATTRB = ['facing']
- FACING_DOV_ANGLES = [1]
- NCV = 8
- SCORING = ['accuracy', 'balanced_accuracy', 'f1']
- REFIT_SCORING = balanced_accuracy
- PARAM_GRID = [{'est__n_estimators': [50, 100, 150, 200, 300], 'est__min_samples_split': [2, 5, 10], 'est__min_samples_leaf': [1, 5, 10], 'est__max_features': ['sqrt', 'log2', None], 'est__bootstrap': [False], 'est__n_jobs': [-1], 'est__random_state': [42], 'est__max_samples': [0.01, 0.5, 0.09]}, {'est__n_estimators': [50, 100, 150, 200, 300], 'est__min_samples_split': [2, 5, 10], 'est__min_samples_leaf': [1, 5, 10], 'est__max_features': ['sqrt', 'log2', None], 'est__bootstrap': [True], 'est__oob_score': [True, False], 'est__n_jobs': [-1], 'est__random_state': [42], 'est__max_samples': [0.01, 0.5, 0.09]}]
- TRAIN_SET_SESSION = ['trial1', 'trial2']
- TEST_SET_SESSION = ['trial3', 'trial4', 'trial5']
- DISTANCE = [1]
- AGC_STATUS = ['AGC']

## Loaded CSV
- 2021-12-27_raspi_48000Hz_w1_N2^12_overlap80_with2022-01-07.csv

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
	- oob_decision_function_ = [[0.2826087  0.7173913 ]
 [0.24489796 0.75510204]
 [0.34090909 0.65909091]
 [0.32608696 0.67391304]
 [0.23913043 0.76086957]
 [0.4893617  0.5106383 ]
 [0.7826087  0.2173913 ]
 [0.80434783 0.19565217]
 [0.75609756 0.24390244]
 [0.75       0.25      ]
 [0.24444444 0.75555556]
 [0.27659574 0.72340426]
 [0.23404255 0.76595745]
 [0.23255814 0.76744186]
 [0.32608696 0.67391304]
 [0.2826087  0.7173913 ]
 [0.63829787 0.36170213]
 [0.71428571 0.28571429]
 [0.83333333 0.16666667]
 [0.81818182 0.18181818]
 [0.72340426 0.27659574]
 [0.55319149 0.44680851]
 [0.42553191 0.57446809]
 [0.44444444 0.55555556]
 [0.4        0.6       ]
 [0.31111111 0.68888889]
 [0.45652174 0.54347826]
 [0.44680851 0.55319149]
 [0.70833333 0.29166667]
 [0.6        0.4       ]
 [0.79166667 0.20833333]
 [0.85416667 0.14583333]
 [0.56521739 0.43478261]
 [0.60869565 0.39130435]
 [0.32608696 0.67391304]
 [0.36170213 0.63829787]
 [0.22222222 0.77777778]
 [0.21276596 0.78723404]
 [0.46808511 0.53191489]
 [0.38297872 0.61702128]
 [0.84444444 0.15555556]
 [0.76190476 0.23809524]
 [0.80851064 0.19148936]
 [0.57142857 0.42857143]
 [0.65217391 0.34782609]
 [0.58695652 0.41304348]
 [0.34883721 0.65116279]
 [0.46808511 0.53191489]
 [0.5        0.5       ]
 [0.25       0.75      ]
 [0.2173913  0.7826087 ]
 [0.20833333 0.79166667]
 [0.2173913  0.7826087 ]
 [0.34042553 0.65957447]
 [0.22727273 0.77272727]
 [0.24444444 0.75555556]
 [0.25581395 0.74418605]
 [0.22222222 0.77777778]
 [0.20408163 0.79591837]
 [0.33333333 0.66666667]
 [0.24390244 0.75609756]
 [0.22727273 0.77272727]
 [0.2173913  0.7826087 ]
 [0.24444444 0.75555556]
 [0.29166667 0.70833333]
 [0.34042553 0.65957447]
 [0.26666667 0.73333333]
 [0.20833333 0.79166667]
 [0.28571429 0.71428571]
 [0.26666667 0.73333333]
 [0.34782609 0.65217391]
 [0.29545455 0.70454545]
 [0.23404255 0.76595745]
 [0.28571429 0.71428571]
 [0.47826087 0.52173913]
 [0.2826087  0.7173913 ]
 [0.25581395 0.74418605]
 [0.25581395 0.74418605]
 [0.21276596 0.78723404]
 [0.22222222 0.77777778]]
	- oob_score_ = 0.7625

#### Importance of features
- gp_auc_min = 0.07593171296296297
- gp_max_val_std = 0.059895833333333336
- gp_auc_max = 0.05773148148148149
- ac_std = 0.05355902777777779
- gp_max_ix_std = 0.050144675925925926
- gp_max_val_mean = 0.04956597222222222
- gp_auc_range = 0.04369212962962963
- ratio_max_to_10ms_ave_peaks = 0.04305555555555556
- gp_max_val_max = 0.04210069444444444
- gp_max_ix_mean = 0.040763888888888884
- srmr = 0.040451388888888884
- tdoa_mean = 0.03741319444444444
- tdoa_min = 0.03518518518518519
- gp_max_ix_range = 0.03194444444444445
- ac_auc = 0.03177083333333334
- ratio_max_to_9th_ave_peaks = 0.029745370370370366
- hlbr = 0.02751736111111111
- tdoa_std = 0.025318287037037035
- gp_auc_std = 0.024913194444444443
- tdoa_range = 0.02326388888888889
- gp_max_ix_min = 0.022685185185185187
- low_power = 0.019386574074074073
- gp_max_val_min = 0.018836805555555555
- gp_auc_mean = 0.017621527777777774
- diff_auc = 0.017361111111111112
- coe1[1] = 0.01666087962962963
- high_power = 0.01597222222222222
- coe3[2] = 0.011140046296296295
- tdoa_max = 0.011111111111111113
- diff_std = 0.00972222222222222
- coe1[0] = 0.006736111111111109
- coe3[3] = 0.005468750000000001
- gp_max_val_range = 0.003333333333333334
- coe3[0] = 0.0
- coe3[1] = 0.0
- gp_max_ix_max = 0.0

## Evaluation
cv = 8
### accuracy
- Scores = [ 0.4, 0.6, 0.8, 0.5555555555555556, 1.0, 0.7777777777777778, 1.0, 1.0 ]
- Mean = 0.7666666666666666
- Standard deviation = 0.2154524381073924

### balanced_accuracy
- Scores = [ 0.625, 0.75, 0.875, 0.5357142857142857, 1.0, 0.8571428571428572, 1.0, 1.0 ]
- Mean = 0.8303571428571428
- Standard deviation = 0.1675148485651225

### f1
- Scores = [ 0.4, 0.5, 0.6666666666666666, 0.3333333333333333, 1.0, 0.6666666666666666, 1.0, 1.0 ]
- Mean = 0.6958333333333333
- Standard deviation = 0.25897098722100553

### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 41 | 19 |
| Actual Positive | 2 | 13 |

      