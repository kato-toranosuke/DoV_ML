# ExtraTreesClassifier_SMOTE_2022-01-09_no4
## Constants
- CSV_PATH = ../out/csv/experiment
- OUTPUT_PATH = ../out/experiment_result/data_of_2022-01-07_new/AGC-0angle-1m
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
	- sampling_strategy_ = OrderedDict([(1, 30)])
	- nn_k_ = NearestNeighbors(n_neighbors=6)

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
	- max_features = log2
	- max_leaf_nodes = None
	- min_impurity_decrease = 0.0
	- ccp_alpha = 0.0
	- n_features_in_ = 36
	- n_outputs_ = 1
	- classes_ = [0 1]
	- n_classes_ = 2
	- base_estimator_ = ExtraTreeClassifier()
	- oob_decision_function_ = [[0.3        0.7       ]
 [0.19354839 0.80645161]
 [0.26136364 0.73863636]
 [0.33333333 0.66666667]
 [0.30337079 0.69662921]
 [0.48421053 0.51578947]
 [0.76136364 0.23863636]
 [0.76666667 0.23333333]
 [0.76470588 0.23529412]
 [0.76595745 0.23404255]
 [0.24210526 0.75789474]
 [0.26595745 0.73404255]
 [0.19565217 0.80434783]
 [0.33333333 0.66666667]
 [0.35789474 0.64210526]
 [0.36263736 0.63736264]
 [0.69892473 0.30107527]
 [0.71276596 0.28723404]
 [0.81395349 0.18604651]
 [0.79775281 0.20224719]
 [0.71134021 0.28865979]
 [0.60215054 0.39784946]
 [0.38202247 0.61797753]
 [0.35164835 0.64835165]
 [0.42857143 0.57142857]
 [0.44565217 0.55434783]
 [0.4516129  0.5483871 ]
 [0.47826087 0.52173913]
 [0.71578947 0.28421053]
 [0.70967742 0.29032258]
 [0.79787234 0.20212766]
 [0.81914894 0.18085106]
 [0.55789474 0.44210526]
 [0.63043478 0.36956522]
 [0.36263736 0.63736264]
 [0.38297872 0.61702128]
 [0.27272727 0.72727273]
 [0.32978723 0.67021277]
 [0.48888889 0.51111111]
 [0.3956044  0.6043956 ]
 [0.8021978  0.1978022 ]
 [0.78409091 0.21590909]
 [0.79347826 0.20652174]
 [0.59090909 0.40909091]
 [0.62765957 0.37234043]
 [0.60869565 0.39130435]
 [0.42222222 0.57777778]
 [0.48421053 0.51578947]
 [0.52272727 0.47727273]
 [0.33707865 0.66292135]
 [0.32222222 0.67777778]
 [0.26041667 0.73958333]
 [0.20430108 0.79569892]
 [0.36263736 0.63736264]
 [0.23655914 0.76344086]
 [0.38297872 0.61702128]
 [0.34831461 0.65168539]
 [0.28571429 0.71428571]
 [0.21348315 0.78651685]
 [0.19148936 0.80851064]
 [0.18604651 0.81395349]
 [0.24719101 0.75280899]
 [0.22826087 0.77173913]
 [0.35164835 0.64835165]
 [0.21875    0.78125   ]
 [0.23404255 0.76595745]
 [0.34444444 0.65555556]
 [0.27368421 0.72631579]
 [0.35789474 0.64210526]
 [0.41573034 0.58426966]
 [0.29545455 0.70454545]
 [0.43820225 0.56179775]
 [0.20652174 0.79347826]
 [0.40206186 0.59793814]
 [0.3655914  0.6344086 ]
 [0.20430108 0.79569892]
 [0.32954545 0.67045455]
 [0.42857143 0.57142857]
 [0.3655914  0.6344086 ]
 [0.29032258 0.70967742]]
	- oob_score_ = 0.7625

#### Importance of features
- gp_max_ix_std = 0.061953125000000005
- gp_auc_min = 0.058489583333333345
- gp_auc_max = 0.056093750000000005
- gp_auc_mean = 0.05058159722222223
- gp_max_val_min = 0.049895833333333334
- gp_max_val_mean = 0.04768807870370371
- ratio_max_to_10ms_ave_peaks = 0.046701388888888896
- ratio_max_to_9th_ave_peaks = 0.046440972222222224
- gp_max_val_max = 0.04608217592592593
- high_power = 0.03629918981481482
- srmr = 0.035879629629629636
- gp_max_val_std = 0.035214120370370375
- tdoa_range = 0.03266782407407408
- tdoa_min = 0.03155381944444445
- gp_max_ix_range = 0.02971643518518519
- gp_auc_range = 0.029325810185185187
- coe1[1] = 0.028773148148148152
- hlbr = 0.026403356481481486
- gp_max_ix_max = 0.025694444444444443
- tdoa_mean = 0.024247685185185185
- tdoa_max = 0.02391203703703704
- gp_max_ix_mean = 0.019748263888888888
- ac_auc = 0.019531250000000003
- diff_auc = 0.017141203703703707
- gp_max_ix_min = 0.01697048611111112
- gp_max_val_range = 0.016221064814814817
- coe3[3] = 0.01517650462962963
- low_power = 0.01423611111111111
- coe3[2] = 0.014149305555555556
- tdoa_std = 0.012847222222222225
- gp_auc_std = 0.01144386574074074
- diff_std = 0.008188657407407408
- coe1[0] = 0.0060879629629629626
- ac_std = 0.004644097222222224
- coe3[0] = 0.0
- coe3[1] = 0.0

## Evaluation
cv = 8
### accuracy
- Scores = [ 0.3, 0.7, 0.8, 0.5555555555555556, 0.8888888888888888, 0.7777777777777778, 1.0, 1.0 ]
- Mean = 0.7527777777777778
- Standard deviation = 0.2208813714347898

### balanced_accuracy
- Scores = [ 0.375, 0.8125, 0.875, 0.5357142857142857, 0.9285714285714286, 0.8571428571428572, 1.0, 1.0 ]
- Mean = 0.7979910714285714
- Standard deviation = 0.21095521467565584

### f1
- Scores = [ 0.22222222222222224, 0.5714285714285715, 0.6666666666666666, 0.3333333333333333, 0.8, 0.6666666666666666, 1.0, 1.0 ]
- Mean = 0.6575396825396825
- Standard deviation = 0.26387635726301545

### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 43 | 17 |
| Actual Positive | 6 | 9 |

      