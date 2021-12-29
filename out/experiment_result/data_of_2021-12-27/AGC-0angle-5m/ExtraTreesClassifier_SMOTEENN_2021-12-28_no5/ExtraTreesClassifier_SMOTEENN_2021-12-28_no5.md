# ExtraTreesClassifier_SMOTEENN_2021-12-28_no5
## Constants
- CSV_PATH = ../out/csv/experiment
- OUTPUT_PATH = ../out/experiment_result/data_of_2021-12-27/AGC-0angle-5m
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
- AGC_STATUS = ['AGC']

## Loaded CSV
- 2021-12-27_raspi_48000Hz_w1_N2^12_overlap80_new.csv

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
	- min_samples_split = 10
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
	- oob_decision_function_ = [[0.60942074 0.39057926]
 [0.88952069 0.11047931]
 [0.89680936 0.10319064]
 [0.97001528 0.02998472]
 [0.92809524 0.07190476]
 [0.95811315 0.04188685]
 [0.84388121 0.15611879]
 [0.77739298 0.22260702]
 [0.6751665  0.3248335 ]
 [0.94826093 0.05173907]
 [0.91289683 0.08710317]
 [0.89040885 0.10959115]
 [0.82179705 0.17820295]
 [0.97428571 0.02571429]
 [0.9752381  0.0247619 ]
 [0.95221088 0.04778912]
 [0.95385878 0.04614122]
 [0.83442652 0.16557348]
 [0.18206937 0.81793063]
 [0.19473016 0.80526984]
 [0.35757808 0.64242192]
 [0.16825397 0.83174603]
 [0.1329932  0.8670068 ]
 [0.15086368 0.84913632]
 [0.14765684 0.85234316]
 [0.13224206 0.86775794]
 [0.16294643 0.83705357]
 [0.17481767 0.82518233]]
	- oob_score_ = 1.0

#### Importance of features
- gp_max_val_max = 0.1276595744680851
- high_power = 0.10638297872340426
- gp_auc_max = 0.10638297872340426
- hlbr = 0.0768321513002364
- diff_auc = 0.06382978723404255
- gp_max_val_min = 0.06382978723404255
- gp_auc_min = 0.06382978723404255
- coe3[2] = 0.0425531914893617
- coe3[3] = 0.0425531914893617
- ac_auc = 0.0425531914893617
- gp_max_val_std = 0.0425531914893617
- gp_auc_mean = 0.029550827423167846
- ratio_max_to_9th_ave_peaks = 0.02127659574468085
- srmr = 0.02127659574468085
- gp_max_val_mean = 0.02127659574468085
- gp_max_ix_range = 0.02127659574468085
- gp_auc_std = 0.02127659574468085
- gp_auc_range = 0.02127659574468085
- tdoa_min = 0.02127659574468085
- tdoa_max = 0.02127659574468085
- ac_std = 0.019094380796508457
- tdoa_range = 0.0021822149481723957
- low_power = 0.0
- coe1[0] = 0.0
- coe1[1] = 0.0
- coe3[0] = 0.0
- coe3[1] = 0.0
- ratio_max_to_10ms_ave_peaks = 0.0
- diff_std = 0.0
- gp_max_val_range = 0.0
- gp_max_ix_std = 0.0
- gp_max_ix_min = 0.0
- gp_max_ix_max = 0.0
- gp_max_ix_mean = 0.0
- tdoa_std = 0.0
- tdoa_mean = 0.0

## Evaluation
cv = 8
### accuracy
- Scores = [ 0.8, 0.7, 0.7, 0.8888888888888888, 0.7777777777777778, 0.7777777777777778, 0.6666666666666666, 0.6666666666666666 ]
- Mean = 0.7472222222222222
- Standard deviation = 0.07259519080762213

### balanced_accuracy
- Scores = [ 0.875, 0.8125, 0.625, 0.9285714285714286, 0.8571428571428572, 0.8571428571428572, 0.7857142857142857, 0.8125 ]
- Mean = 0.8191964285714286
- Standard deviation = 0.08432065521216119

### f1
- Scores = [ 0.6666666666666666, 0.5714285714285715, 0.4, 0.8, 0.6666666666666666, 0.6666666666666666, 0.5714285714285715, 0.4 ]
- Mean = 0.5928571428571429
- Standard deviation = 0.1296908936323459

### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 42 | 18 |
| Actual Positive | 1 | 14 |

      