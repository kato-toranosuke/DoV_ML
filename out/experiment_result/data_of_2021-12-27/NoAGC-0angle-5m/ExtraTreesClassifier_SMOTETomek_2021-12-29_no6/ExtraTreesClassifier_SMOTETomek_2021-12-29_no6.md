# ExtraTreesClassifier_SMOTETomek_2021-12-29_no6
## Constants
- CSV_PATH = ../out/csv/experiment
- OUTPUT_PATH = ../out/experiment_result/data_of_2021-12-27/NoAGC-0angle-5m
- FEATURE_ATTRBS = ['low_power', 'high_power', 'hlbr', 'coe1[0]', 'coe1[1]', 'coe3[0]', 'coe3[1]', 'coe3[2]', 'coe3[3]', 'ratio_max_to_10ms_ave_peaks', 'ratio_max_to_9th_ave_peaks', 'ac_std', 'ac_auc', 'diff_std', 'diff_auc', 'srmr', 'gp_max_val_std', 'gp_max_val_range', 'gp_max_val_min', 'gp_max_val_max', 'gp_max_val_mean', 'gp_max_ix_std', 'gp_max_ix_range', 'gp_max_ix_min', 'gp_max_ix_max', 'gp_max_ix_mean', 'gp_auc_std', 'gp_auc_range', 'gp_auc_min', 'gp_auc_max', 'gp_auc_mean', 'tdoa_std', 'tdoa_range', 'tdoa_min', 'tdoa_max', 'tdoa_mean']
- LABEL_ATTRB = ['facing']
- FACING_DOV_ANGLES = [1]
- NCV = 8
- SCORING = ['accuracy', 'balanced_accuracy', 'f1']
- REFIT_SCORING = balanced_accuracy
- PARAM_GRID = [{'est__n_estimators': [50, 100, 150, 200, 300], 'est__min_samples_split': [2, 5, 10], 'est__min_samples_leaf': [1, 5, 10], 'est__max_features': ['sqrt', 'log2', None], 'est__bootstrap': [False], 'est__n_jobs': [-1], 'est__random_state': [42], 'est__max_samples': [0.01, 0.5, 0.09]}, {'est__n_estimators': [50, 100, 150, 200, 300], 'est__min_samples_split': [2, 5, 10], 'est__min_samples_leaf': [1, 5, 10], 'est__max_features': ['sqrt', 'log2', None], 'est__bootstrap': [True], 'est__oob_score': [True, False], 'est__n_jobs': [-1], 'est__random_state': [42], 'est__max_samples': [0.01, 0.5, 0.09]}]
- TRAIN_SET_SESSION = ['trial1', 'trial2']
- TEST_SET_SESSION = ['trial3', 'trial4', 'trial5']
- DISTANCE = [5]
- AGC_STATUS = ['NoAGC']

## Loaded CSV
- 2021-12-27_raspi_48000Hz_w1_N2^12_overlap80_new.csv

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
	- oob_decision_function_ = [[0.27659574 0.72340426]
 [0.52173913 0.47826087]
 [0.37777778 0.62222222]
 [0.77083333 0.22916667]
 [0.78723404 0.21276596]
 [0.83333333 0.16666667]
 [0.86956522 0.13043478]
 [0.84090909 0.15909091]
 [0.81395349 0.18604651]
 [0.71428571 0.28571429]
 [0.6        0.4       ]
 [0.38297872 0.61702128]
 [0.23809524 0.76190476]
 [0.65217391 0.34782609]
 [0.32608696 0.67391304]
 [0.84444444 0.15555556]
 [0.85106383 0.14893617]
 [0.70212766 0.29787234]
 [0.53333333 0.46666667]
 [0.21276596 0.78723404]
 [0.2173913  0.7826087 ]
 [0.45833333 0.54166667]
 [0.42553191 0.57446809]
 [0.79069767 0.20930233]
 [0.7804878  0.2195122 ]
 [0.80434783 0.19565217]
 [0.77777778 0.22222222]
 [0.73913043 0.26086957]
 [0.70212766 0.29787234]
 [0.14285714 0.85714286]
 [0.13043478 0.86956522]
 [0.18181818 0.81818182]
 [0.22222222 0.77777778]
 [0.4        0.6       ]
 [0.17391304 0.82608696]
 [0.20408163 0.79591837]
 [0.30434783 0.69565217]
 [0.23404255 0.76595745]
 [0.15217391 0.84782609]
 [0.2173913  0.7826087 ]
 [0.19047619 0.80952381]
 [0.25       0.75      ]
 [0.19148936 0.80851064]
 [0.22222222 0.77777778]
 [0.2826087  0.7173913 ]
 [0.22727273 0.77272727]
 [0.18181818 0.81818182]
 [0.46808511 0.53191489]
 [0.22222222 0.77777778]
 [0.17777778 0.82222222]
 [0.48888889 0.51111111]
 [0.23255814 0.76744186]
 [0.13333333 0.86666667]
 [0.20833333 0.79166667]]
	- oob_score_ = 0.8703703703703703

#### Importance of features
- gp_max_val_max = 0.10869565217391304
- gp_auc_min = 0.10446859903381642
- srmr = 0.07276570048309179
- low_power = 0.06521739130434782
- tdoa_mean = 0.05193236714975846
- high_power = 0.049516908212560384
- gp_auc_max = 0.04770531400966183
- hlbr = 0.043478260869565216
- gp_max_ix_range = 0.043478260869565216
- gp_auc_std = 0.043478260869565216
- gp_max_val_min = 0.03985507246376812
- gp_auc_mean = 0.03366545893719807
- gp_max_val_std = 0.03140096618357488
- coe1[0] = 0.030797101449275364
- gp_max_val_mean = 0.03079710144927536
- gp_max_ix_min = 0.025362318840579712
- tdoa_min = 0.025362318840579712
- ratio_max_to_9th_ave_peaks = 0.021739130434782608
- gp_auc_range = 0.021739130434782608
- tdoa_max = 0.021739130434782608
- tdoa_std = 0.01811594202898551
- coe3[3] = 0.017210144927536232
- diff_std = 0.013586956521739134
- gp_max_ix_std = 0.012077294685990338
- tdoa_range = 0.00966183574879227
- gp_max_val_range = 0.008152173913043475
- coe3[2] = 0.006642512077294685
- ratio_max_to_10ms_ave_peaks = 0.0013586956521739085
- coe1[1] = 0.0
- coe3[0] = 0.0
- coe3[1] = 0.0
- ac_std = 0.0
- ac_auc = 0.0
- diff_auc = 0.0
- gp_max_ix_max = 0.0
- gp_max_ix_mean = 0.0

## Evaluation
cv = 8
### accuracy
- Scores = [ 0.625, 1.0, 0.625, 1.0, 0.8571428571428571, 0.8571428571428571, 1.0, 0.8571428571428571 ]
- Mean = 0.8526785714285714
- Standard deviation = 0.14527803656493732

### balanced_accuracy
- Scores = [ 0.75, 1.0, 0.75, 1.0, 0.9166666666666667, 0.9166666666666667, 1.0, 0.9166666666666667 ]
- Mean = 0.90625
- Standard deviation = 0.09716019846967516

### f1
- Scores = [ 0.5714285714285715, 1.0, 0.5714285714285715, 1.0, 0.6666666666666666, 0.6666666666666666, 1.0, 0.6666666666666666 ]
- Mean = 0.7678571428571429
- Standard deviation = 0.18356123744177708

### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 39 | 9 |
| Actual Positive | 0 | 12 |

      