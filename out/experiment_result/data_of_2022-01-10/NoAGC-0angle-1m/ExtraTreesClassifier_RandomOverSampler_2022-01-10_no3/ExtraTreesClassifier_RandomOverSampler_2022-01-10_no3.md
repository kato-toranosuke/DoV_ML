# ExtraTreesClassifier_RandomOverSampler_2022-01-10_no3
## Constants
- CSV_PATH = ../out/csv/experiment
- OUTPUT_PATH = ../out/experiment_result/data_of_2022-01-10/NoAGC-0angle-1m
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
	- sampling_strategy_ = OrderedDict([(1, 30)])
	- shrinkage_ = None
	- sample_indices_ = [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23
 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47
 48 49 36 13 37 24 36 49 12 36 37 24 13 37 37 12 25 24  1 37 25  1 24  0
 49 25 48  0 49 12 36 13]

- best_estimator
	- base_estimator = ExtraTreeClassifier()
	- n_estimators = 100
	- estimator_params = ('criterion', 'max_depth', 'min_samples_split', 'min_samples_leaf', 'min_weight_fraction_leaf', 'max_features', 'max_leaf_nodes', 'min_impurity_decrease', 'random_state', 'ccp_alpha')
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
	- ccp_alpha = 0.0
	- n_features_in_ = 36
	- n_outputs_ = 1
	- classes_ = [0 1]
	- n_classes_ = 2
	- base_estimator_ = ExtraTreeClassifier()
	- oob_decision_function_ = [[0.27777778 0.72222222]
 [0.2688172  0.7311828 ]
 [0.34090909 0.65909091]
 [0.29032258 0.70967742]
 [0.56179775 0.43820225]
 [0.58947368 0.41052632]
 [0.82954545 0.17045455]
 [0.84444444 0.15555556]
 [0.87058824 0.12941176]
 [0.88297872 0.11702128]
 [0.37894737 0.62105263]
 [0.23404255 0.76595745]
 [0.31521739 0.68478261]
 [0.35632184 0.64367816]
 [0.34736842 0.65263158]
 [0.42857143 0.57142857]
 [0.61290323 0.38709677]
 [0.63829787 0.36170213]
 [0.8372093  0.1627907 ]
 [0.7752809  0.2247191 ]
 [0.79381443 0.20618557]
 [0.67741935 0.32258065]
 [0.34831461 0.65168539]
 [0.34065934 0.65934066]
 [0.35714286 0.64285714]
 [0.44565217 0.55434783]
 [0.49462366 0.50537634]
 [0.57608696 0.42391304]
 [0.69473684 0.30526316]
 [0.76344086 0.23655914]
 [0.79787234 0.20212766]
 [0.79787234 0.20212766]
 [0.76842105 0.23157895]
 [0.55434783 0.44565217]
 [0.40659341 0.59340659]
 [0.42553191 0.57446809]
 [0.42045455 0.57954545]
 [0.40425532 0.59574468]
 [0.36666667 0.63333333]
 [0.34065934 0.65934066]
 [0.85714286 0.14285714]
 [0.86363636 0.13636364]
 [0.81521739 0.18478261]
 [0.88636364 0.11363636]
 [0.69148936 0.30851064]
 [0.65217391 0.34782609]
 [0.45555556 0.54444444]
 [0.47368421 0.52631579]
 [0.29545455 0.70454545]
 [0.21348315 0.78651685]
 [0.41111111 0.58888889]
 [0.32291667 0.67708333]
 [0.40860215 0.59139785]
 [0.32967033 0.67032967]
 [0.39784946 0.60215054]
 [0.20212766 0.79787234]
 [0.3258427  0.6741573 ]
 [0.40659341 0.59340659]
 [0.42696629 0.57303371]
 [0.31914894 0.68085106]
 [0.36046512 0.63953488]
 [0.42696629 0.57303371]
 [0.41304348 0.58695652]
 [0.31868132 0.68131868]
 [0.42708333 0.57291667]
 [0.31914894 0.68085106]
 [0.27777778 0.72222222]
 [0.4        0.6       ]
 [0.43157895 0.56842105]
 [0.28089888 0.71910112]
 [0.34090909 0.65909091]
 [0.28089888 0.71910112]
 [0.20652174 0.79347826]
 [0.42268041 0.57731959]
 [0.27956989 0.72043011]
 [0.2688172  0.7311828 ]
 [0.21590909 0.78409091]
 [0.31868132 0.68131868]
 [0.39784946 0.60215054]
 [0.33333333 0.66666667]]
	- oob_score_ = 0.8125

#### Importance of features
- ratio_max_to_10ms_ave_peaks = 0.07148437500000002
- hlbr = 0.06866319444444446
- tdoa_mean = 0.05632233796296298
- ratio_max_to_9th_ave_peaks = 0.053819444444444454
- gp_max_val_mean = 0.05290798611111113
- gp_auc_mean = 0.0490451388888889
- diff_auc = 0.048567708333333355
- gp_auc_min = 0.04822048611111112
- gp_max_val_min = 0.042664930555555564
- gp_auc_max = 0.04114583333333334
- gp_max_ix_std = 0.03611111111111112
- gp_max_ix_max = 0.03224826388888889
- gp_max_val_max = 0.03155381944444445
- diff_std = 0.03125000000000001
- gp_max_val_range = 0.030251736111111118
- gp_auc_range = 0.028385416666666673
- low_power = 0.02721354166666667
- gp_max_val_std = 0.02660590277777778
- gp_max_ix_mean = 0.025390625000000007
- gp_auc_std = 0.021831597222222224
- coe1[1] = 0.020543981481481483
- high_power = 0.02005208333333334
- tdoa_max = 0.016970486111111117
- coe3[2] = 0.014973958333333337
- ac_auc = 0.01427951388888889
- coe3[3] = 0.013845486111111114
- srmr = 0.012152777777777781
- gp_max_ix_range = 0.011414930555555558
- ac_std = 0.010416666666666668
- tdoa_std = 0.010416666666666668
- tdoa_range = 0.010416666666666668
- tdoa_min = 0.010416666666666668
- coe1[0] = 0.005555555555555557
- gp_max_ix_min = 0.004861111111111111
- coe3[0] = 0.0
- coe3[1] = 0.0

## Evaluation
cv = 8
### accuracy
- Scores = [ 0.6, 0.6, 0.8, 0.5555555555555556, 1.0, 0.7777777777777778, 0.6666666666666666, 0.6666666666666666 ]
- Mean = 0.7083333333333333
- Standard deviation = 0.1362810730226231

### balanced_accuracy
- Scores = [ 0.75, 0.75, 0.875, 0.7142857142857143, 1.0, 0.6785714285714286, 0.7857142857142857, 0.8125 ]
- Mean = 0.7957589285714286
- Standard deviation = 0.09548119898208296

### f1
- Scores = [ 0.5, 0.5, 0.6666666666666666, 0.5, 1.0, 0.5, 0.5714285714285715, 0.4 ]
- Mean = 0.5797619047619047
- Standard deviation = 0.17391956725169216

### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 41 | 19 |
| Actual Positive | 1 | 14 |

      