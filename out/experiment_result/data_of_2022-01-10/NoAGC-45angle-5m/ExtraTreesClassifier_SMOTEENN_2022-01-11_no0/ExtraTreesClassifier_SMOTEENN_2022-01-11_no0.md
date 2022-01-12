# ExtraTreesClassifier_SMOTEENN_2022-01-11_no0
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
	- max_features = log2
	- max_leaf_nodes = None
	- min_impurity_decrease = 0.0
	- ccp_alpha = 0.0
	- n_features_in_ = 36
	- n_outputs_ = 1
	- classes_ = [0 1]
	- n_classes_ = 2
	- base_estimator_ = ExtraTreeClassifier()
	- oob_decision_function_ = [[0.96875    0.03125   ]
 [0.93333333 0.06666667]
 [1.         0.        ]
 [1.         0.        ]
 [0.93548387 0.06451613]
 [1.         0.        ]
 [0.90625    0.09375   ]
 [1.         0.        ]
 [0.54545455 0.45454545]
 [0.18518519 0.81481481]
 [0.09677419 0.90322581]
 [0.06666667 0.93333333]
 [0.10714286 0.89285714]
 [0.08       0.92      ]
 [0.03030303 0.96969697]
 [0.03333333 0.96666667]]
	- oob_score_ = 1.0

#### Importance of features
- tdoa_range = 0.11370262390670555
- gp_max_ix_min = 0.11020408163265308
- gp_auc_max = 0.09446064139941691
- srmr = 0.08979591836734696
- gp_max_ix_range = 0.0816326530612245
- tdoa_min = 0.0816326530612245
- gp_max_val_min = 0.048526077097505685
- gp_auc_min = 0.04625850340136055
- gp_max_val_max = 0.0435374149659864
- coe3[2] = 0.04081632653061225
- tdoa_std = 0.03764172335600908
- gp_max_val_mean = 0.03206997084548106
- ac_auc = 0.03174603174603175
- low_power = 0.020408163265306124
- hlbr = 0.020408163265306124
- ac_std = 0.020408163265306124
- gp_auc_std = 0.020408163265306124
- gp_max_ix_mean = 0.018594104308390022
- ratio_max_to_10ms_ave_peaks = 0.012244897959183675
- gp_max_ix_std = 0.008746355685131194
- ratio_max_to_9th_ave_peaks = 0.008707482993197279
- coe1[1] = 0.00816326530612245
- gp_max_val_std = 0.0054421768707483
- diff_auc = 0.004444444444444449
- high_power = 0.0
- coe1[0] = 0.0
- coe3[0] = 0.0
- coe3[1] = 0.0
- coe3[3] = 0.0
- diff_std = 0.0
- gp_max_val_range = 0.0
- gp_max_ix_max = 0.0
- gp_auc_range = 0.0
- gp_auc_mean = 0.0
- tdoa_max = 0.0
- tdoa_mean = 0.0

## Evaluation
cv = 8
### accuracy
- Scores = [ 0.7, 0.8, 0.8, 1.0, 0.7777777777777778, 0.5555555555555556, 1.0, 0.7777777777777778 ]
- Mean = 0.8013888888888889
- Standard deviation = 0.13726129673089538

### balanced_accuracy
- Scores = [ 0.7, 0.8, 0.8, 1.0, 0.75, 0.5, 1.0, 0.8 ]
- Mean = 0.79375
- Standard deviation = 0.15090870584562044

### f1
- Scores = [ 0.7692307692307693, 0.7499999999999999, 0.8333333333333333, 1.0, 0.8333333333333333, 0.7142857142857143, 1.0, 0.8 ]
- Mean = 0.8375228937728937
- Standard deviation = 0.10108917233260424

### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 18 | 18 |
| Actual Positive | 0 | 39 |

      