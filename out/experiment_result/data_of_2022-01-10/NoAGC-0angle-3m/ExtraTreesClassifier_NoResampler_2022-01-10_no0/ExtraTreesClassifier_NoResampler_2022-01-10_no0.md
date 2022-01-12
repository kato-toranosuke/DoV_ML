# ExtraTreesClassifier_NoResampler_2022-01-10_no0
## Constants
- CSV_PATH = ../out/csv/experiment
- OUTPUT_PATH = ../out/experiment_result/data_of_2022-01-10/NoAGC-0angle-3m
- FEATURE_ATTRBS = ['low_power', 'high_power', 'hlbr', 'coe1[0]', 'coe1[1]', 'coe3[0]', 'coe3[1]', 'coe3[2]', 'coe3[3]', 'ratio_max_to_10ms_ave_peaks', 'ratio_max_to_9th_ave_peaks', 'ac_std', 'ac_auc', 'diff_std', 'diff_auc', 'srmr', 'gp_max_val_std', 'gp_max_val_range', 'gp_max_val_min', 'gp_max_val_max', 'gp_max_val_mean', 'gp_max_ix_std', 'gp_max_ix_range', 'gp_max_ix_min', 'gp_max_ix_max', 'gp_max_ix_mean', 'gp_auc_std', 'gp_auc_range', 'gp_auc_min', 'gp_auc_max', 'gp_auc_mean', 'tdoa_std', 'tdoa_range', 'tdoa_min', 'tdoa_max', 'tdoa_mean']
- LABEL_ATTRB = ['facing']
- FACING_DOV_ANGLES = [1]
- NCV = 8
- SCORING = ['accuracy', 'balanced_accuracy', 'f1']
- REFIT_SCORING = balanced_accuracy
- PARAM_GRID = [{'est__n_estimators': [50, 100, 150, 200, 300], 'est__min_samples_split': [2, 5, 10], 'est__min_samples_leaf': [1, 5, 10], 'est__max_features': ['sqrt', 'log2', None], 'est__bootstrap': [False], 'est__n_jobs': [-1], 'est__random_state': [42], 'est__max_samples': [0.01, 0.5, 0.09]}, {'est__n_estimators': [50, 100, 150, 200, 300], 'est__min_samples_split': [2, 5, 10], 'est__min_samples_leaf': [1, 5, 10], 'est__max_features': ['sqrt', 'log2', None], 'est__bootstrap': [True], 'est__oob_score': [True, False], 'est__n_jobs': [-1], 'est__random_state': [42], 'est__max_samples': [0.01, 0.5, 0.09]}]
- TRAIN_SET_SESSION = ['trial1', 'trial2']
- TEST_SET_SESSION = ['trial3', 'trial4', 'trial5']
- DISTANCE = [3]
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
	- n_estimators = 100
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
	- min_samples_split = 10
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
	- oob_decision_function_ = [[0.38463564 0.61536436]
 [0.43598635 0.56401365]
 [0.3796891  0.6203109 ]
 [0.70368279 0.29631721]
 [0.98677249 0.01322751]
 [0.99230769 0.00769231]
 [0.98781676 0.01218324]
 [0.99278846 0.00721154]
 [0.99364407 0.00635593]
 [1.         0.        ]
 [0.91855159 0.08144841]
 [0.91677827 0.08322173]
 [0.31361921 0.68638079]
 [0.40446708 0.59553292]
 [0.42746805 0.57253195]
 [0.30131249 0.69868751]
 [0.94350282 0.05649718]
 [0.96174863 0.03825137]
 [0.98541667 0.01458333]
 [0.98914931 0.01085069]
 [0.98611111 0.01388889]
 [0.984375   0.015625  ]
 [0.76832861 0.23167139]
 [0.98830409 0.01169591]
 [0.3707324  0.6292676 ]
 [0.32818829 0.67181171]
 [0.93991101 0.06008899]
 [0.92494658 0.07505342]
 [0.99305556 0.00694444]
 [1.         0.        ]
 [1.         0.        ]
 [1.         0.        ]
 [0.98425926 0.01574074]
 [1.         0.        ]
 [0.89072528 0.10927472]
 [0.78718577 0.21281423]
 [0.46098554 0.53901446]
 [0.67530698 0.32469302]
 [0.53906058 0.46093942]
 [0.71866215 0.28133785]
 [0.92857143 0.07142857]
 [0.99764151 0.00235849]
 [0.99764151 0.00235849]
 [0.99791667 0.00208333]
 [0.9897541  0.0102459 ]
 [0.96031746 0.03968254]
 [0.96920375 0.03079625]
 [0.97362278 0.02637722]
 [0.2990959  0.7009041 ]
 [0.38381746 0.61618254]]
	- oob_score_ = 0.92

#### Importance of features
- gp_max_val_max = 0.17570561449916017
- gp_auc_max = 0.16902840735679875
- gp_auc_mean = 0.10200331884373683
- gp_auc_min = 0.09831662503485246
- gp_max_val_mean = 0.09435657105243564
- hlbr = 0.07962055806020606
- gp_max_val_min = 0.0652765756754686
- high_power = 0.05808675434004025
- srmr = 0.057139633512677646
- diff_std = 0.025464113181504485
- gp_auc_range = 0.021533125177589936
- ratio_max_to_9th_ave_peaks = 0.010173753712011123
- gp_max_ix_range = 0.01
- ac_std = 0.008600223964165734
- coe1[1] = 0.00794185747363005
- diff_auc = 0.005513280689160087
- gp_max_val_range = 0.0040878378378378395
- gp_max_val_std = 0.002380952380952382
- tdoa_std = 0.001945222533457829
- gp_max_ix_std = 0.0018140589569160994
- low_power = 0.0010115157173980701
- coe1[0] = 0.0
- coe3[0] = 0.0
- coe3[1] = 0.0
- coe3[2] = 0.0
- coe3[3] = 0.0
- ratio_max_to_10ms_ave_peaks = 0.0
- ac_auc = 0.0
- gp_max_ix_min = 0.0
- gp_max_ix_max = 0.0
- gp_max_ix_mean = 0.0
- gp_auc_std = 0.0
- tdoa_range = 0.0
- tdoa_min = 0.0
- tdoa_max = 0.0
- tdoa_mean = 0.0

## Evaluation
cv = 8
### accuracy
- Scores = [ 0.8, 0.8, 1.0, 0.8888888888888888, 0.8888888888888888, 0.8888888888888888, 1.0, 0.8888888888888888 ]
- Mean = 0.8944444444444444
- Standard deviation = 0.0709285851933539

### balanced_accuracy
- Scores = [ 0.875, 0.6875, 1.0, 0.75, 0.75, 0.9285714285714286, 1.0, 0.5 ]
- Mean = 0.8113839285714286
- Standard deviation = 0.16154531547182932

### f1
- Scores = [ 0.6666666666666666, 0.5, 1.0, 0.6666666666666666, 0.6666666666666666, 0.8, 1.0, 0.0 ]
- Mean = 0.6625
- Standard deviation = 0.29834613566571744

### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 55 | 5 |
| Actual Positive | 6 | 9 |

      