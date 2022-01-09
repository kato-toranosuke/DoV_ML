# ExtraTreesClassifier_SMOTETomek_2022-01-08_no6
## Constants
- CSV_PATH = ../out/csv/experiment
- OUTPUT_PATH = ../out/experiment_result/data_of_2022-01-07/AGC-0angle-3m
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
- AGC_STATUS = ['AGC']

## Loaded CSV
- 2021-12-27_raspi_48000Hz_w1_N2^12_overlap80_with2022-01-07.csv

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
	- n_estimators = 100
	- estimator_params = ('criterion', 'max_depth', 'min_samples_split', 'min_samples_leaf', 'min_weight_fraction_leaf', 'max_features', 'max_leaf_nodes', 'min_impurity_decrease', 'min_impurity_split', 'random_state', 'ccp_alpha')
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
	- max_features = sqrt
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
	- oob_decision_function_ = [[0.05084746 0.94915254]
 [0.33783784 0.66216216]
 [0.67857143 0.32142857]
 [1.         0.        ]
 [0.98275862 0.01724138]
 [1.         0.        ]
 [0.96551724 0.03448276]
 [0.57692308 0.42307692]
 [0.85245902 0.14754098]
 [0.14285714 0.85714286]
 [0.05       0.95      ]
 [0.63492063 0.36507937]
 [0.37704918 0.62295082]
 [1.         0.        ]
 [0.98591549 0.01408451]
 [1.         0.        ]
 [0.87096774 0.12903226]
 [0.71666667 0.28333333]
 [0.05084746 0.94915254]
 [0.25806452 0.74193548]
 [0.95588235 0.04411765]
 [0.95714286 0.04285714]
 [0.91525424 0.08474576]
 [0.92982456 0.07017544]
 [1.         0.        ]
 [0.98333333 0.01666667]
 [0.51724138 0.48275862]
 [0.58       0.42      ]
 [0.203125   0.796875  ]
 [0.57894737 0.42105263]
 [0.96774194 0.03225806]
 [0.98305085 0.01694915]
 [0.95081967 0.04918033]
 [0.96721311 0.03278689]
 [1.         0.        ]
 [0.95081967 0.04918033]
 [0.96078431 0.03921569]
 [0.07272727 0.92727273]
 [0.14545455 0.85454545]
 [0.1509434  0.8490566 ]
 [0.05660377 0.94339623]
 [0.05660377 0.94339623]
 [0.12280702 0.87719298]
 [0.03333333 0.96666667]
 [0.14754098 0.85245902]
 [0.15625    0.84375   ]
 [0.24590164 0.75409836]
 [0.09615385 0.90384615]
 [0.171875   0.828125  ]
 [0.05769231 0.94230769]
 [0.10714286 0.89285714]
 [0.03508772 0.96491228]
 [0.03508772 0.96491228]
 [0.         1.        ]
 [0.03225806 0.96774194]
 [0.09090909 0.90909091]
 [0.03773585 0.96226415]
 [0.140625   0.859375  ]
 [0.03278689 0.96721311]
 [0.01694915 0.98305085]]
	- oob_score_ = 0.9833333333333333

#### Importance of features
- high_power = 0.12336506326382016
- gp_auc_max = 0.11569569897277662
- gp_max_val_max = 0.08514569987106198
- gp_max_val_mean = 0.07049067613507774
- hlbr = 0.06206289890956579
- gp_auc_mean = 0.051577257107535
- diff_auc = 0.04399780131112722
- gp_auc_min = 0.04231157451286466
- gp_max_val_min = 0.03709765511996032
- gp_max_ix_mean = 0.03406649364453596
- diff_std = 0.028029510944096343
- gp_auc_range = 0.02635369861572725
- srmr = 0.026065150743586108
- coe3[2] = 0.020768280539120318
- gp_max_val_range = 0.01863645173970558
- low_power = 0.01820257036842318
- gp_max_ix_std = 0.01803639591600486
- tdoa_mean = 0.016857992474998706
- tdoa_std = 0.016857626215569004
- ratio_max_to_9th_ave_peaks = 0.015868999004487756
- tdoa_range = 0.01250856708057364
- coe1[0] = 0.011870819535334679
- gp_max_ix_range = 0.011468555670335855
- tdoa_max = 0.011029814585937428
- coe1[1] = 0.010956873114754772
- coe3[3] = 0.0108353346812727
- tdoa_min = 0.009907025589275892
- ac_auc = 0.009372828945021143
- gp_max_ix_min = 0.009244008065840642
- gp_auc_std = 0.007487054288652031
- ratio_max_to_10ms_ave_peaks = 0.006640365233574576
- ac_std = 0.006543907289636499
- gp_max_ix_max = 0.0064948691014867456
- gp_max_val_std = 0.004152481408258718
- coe3[0] = 0.0
- coe3[1] = 0.0

## Evaluation
cv = 8
### accuracy
- Scores = [ 0.9, 1.0, 0.9, 0.8888888888888888, 1.0, 0.8888888888888888, 0.6666666666666666, 0.6666666666666666 ]
- Mean = 0.8638888888888889
- Standard deviation = 0.1218111774960039

### balanced_accuracy
- Scores = [ 0.9375, 1.0, 0.9375, 0.75, 1.0, 0.9285714285714286, 0.42857142857142855, 0.8125 ]
- Mean = 0.8493303571428572
- Standard deviation = 0.1787073980112577

### f1
- Scores = [ 0.8, 1.0, 0.8, 0.6666666666666666, 1.0, 0.8, 0.0, 0.4 ]
- Mean = 0.6833333333333333
- Standard deviation = 0.3140240613569462

### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 55 | 5 |
| Actual Positive | 2 | 13 |

      