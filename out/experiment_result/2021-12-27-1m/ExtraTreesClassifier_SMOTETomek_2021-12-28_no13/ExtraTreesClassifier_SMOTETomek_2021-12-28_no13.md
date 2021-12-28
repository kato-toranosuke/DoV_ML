# ExtraTreesClassifier_SMOTETomek_2021-12-28_no13
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
- resampler = SMOTETomek
- estimator = ExtraTreesClassifier

### Arguments for hyperparameter search
- resampler = SMOTETomek
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
	- tomek = None
	- n_jobs = -1
	- n_features_in_ = 36
	- sampling_strategy_ = auto
	- smote_ = SMOTE(n_jobs=-1, random_state=42)
	- tomek_ = TomekLinks(n_jobs=-1, sampling_strategy='all')

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
	- oob_decision_function_ = [[0.33333333 0.66666667]
 [0.34782609 0.65217391]
 [0.24444444 0.75555556]
 [0.24489796 0.75510204]
 [0.33333333 0.66666667]
 [0.3877551  0.6122449 ]
 [0.72340426 0.27659574]
 [0.71111111 0.28888889]
 [0.23255814 0.76744186]
 [0.3877551  0.6122449 ]
 [0.4        0.6       ]
 [0.55319149 0.44680851]
 [0.54761905 0.45238095]
 [0.7173913  0.2826087 ]
 [0.72340426 0.27659574]
 [0.6        0.4       ]
 [0.36170213 0.63829787]
 [0.40425532 0.59574468]
 [0.31111111 0.68888889]
 [0.31914894 0.68085106]
 [0.39130435 0.60869565]
 [0.65306122 0.34693878]
 [0.63829787 0.36170213]
 [0.77272727 0.22727273]
 [0.82926829 0.17073171]
 [0.30434783 0.69565217]
 [0.29787234 0.70212766]
 [0.23913043 0.76086957]
 [0.17021277 0.82978723]
 [0.34883721 0.65116279]
 [0.82608696 0.17391304]
 [0.75555556 0.24444444]
 [0.77777778 0.22222222]
 [0.64444444 0.35555556]
 [0.63043478 0.36956522]
 [0.42857143 0.57142857]
 [0.56521739 0.43478261]
 [0.29166667 0.70833333]
 [0.2826087  0.7173913 ]
 [0.34782609 0.65217391]
 [0.26190476 0.73809524]
 [0.28888889 0.71111111]
 [0.36170213 0.63829787]
 [0.30434783 0.69565217]
 [0.23404255 0.76595745]
 [0.17777778 0.82222222]
 [0.28888889 0.71111111]
 [0.29787234 0.70212766]
 [0.32608696 0.67391304]
 [0.34782609 0.65217391]
 [0.48888889 0.51111111]
 [0.27906977 0.72093023]
 [0.22222222 0.77777778]
 [0.20833333 0.79166667]
 [0.34782609 0.65217391]
 [0.42222222 0.57777778]
 [0.34883721 0.65116279]
 [0.25       0.75      ]]
	- oob_score_ = 0.7586206896551724

#### Importance of features
- gp_max_ix_std = 0.07407407407407408
- hlbr = 0.07320601851851853
- gp_auc_max = 0.06481481481481483
- gp_max_val_max = 0.06250000000000001
- gp_auc_mean = 0.05208333333333335
- tdoa_range = 0.04947916666666668
- gp_auc_min = 0.04803240740740742
- coe1[1] = 0.04398148148148149
- srmr = 0.04166666666666667
- tdoa_mean = 0.04166666666666667
- ratio_max_to_10ms_ave_peaks = 0.04021990740740741
- coe1[0] = 0.03385416666666667
- gp_max_val_mean = 0.03298611111111112
- low_power = 0.03298611111111111
- ratio_max_to_9th_ave_peaks = 0.03240740740740741
- tdoa_max = 0.030092592592592594
- gp_max_val_range = 0.02951388888888889
- gp_max_ix_range = 0.027777777777777783
- gp_auc_range = 0.026041666666666675
- gp_max_val_std = 0.024594907407407416
- gp_auc_std = 0.022280092592592594
- gp_max_val_min = 0.020833333333333336
- diff_auc = 0.019386574074074077
- gp_max_ix_mean = 0.01851851851851852
- coe3[2] = 0.00925925925925926
- ac_std = 0.00925925925925926
- gp_max_ix_min = 0.00925925925925926
- tdoa_std = 0.00925925925925926
- coe3[3] = 0.007812500000000002
- diff_std = 0.007812500000000002
- high_power = 0.004340277777777778
- coe3[0] = 0.0
- coe3[1] = 0.0
- ac_auc = 0.0
- gp_max_ix_max = 0.0
- tdoa_min = 0.0

## Evaluation
cv = 8
### accuracy
- Scores = [ 0.4, 0.6, 0.8, 0.7777777777777778, 0.8888888888888888, 0.8888888888888888, 1.0, 0.8888888888888888 ]
- Mean = 0.7805555555555556
- Standard deviation = 0.18068371519943793

### balanced_accuracy
- Scores = [ 0.625, 0.75, 0.875, 0.8571428571428572, 0.75, 0.9285714285714286, 1.0, 0.9375 ]
- Mean = 0.8404017857142858
- Standard deviation = 0.11559289232913635

### f1
- Scores = [ 0.4, 0.5, 0.6666666666666666, 0.6666666666666666, 0.6666666666666666, 0.8, 1.0, 0.6666666666666666 ]
- Mean = 0.6708333333333334
- Standard deviation = 0.1686856873333097

### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 44 | 16 |
| Actual Positive | 1 | 14 |

      