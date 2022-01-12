# ExtraTreesClassifier_RandomOverSampler_2022-01-10_no3
## Constants
- CSV_PATH = ../out/csv/experiment
- OUTPUT_PATH = ../out/experiment_result/data_of_2022-01-10/NoAGC-0angle-under3m
- FEATURE_ATTRBS = ['low_power', 'high_power', 'hlbr', 'coe1[0]', 'coe1[1]', 'coe3[0]', 'coe3[1]', 'coe3[2]', 'coe3[3]', 'ratio_max_to_10ms_ave_peaks', 'ratio_max_to_9th_ave_peaks', 'ac_std', 'ac_auc', 'diff_std', 'diff_auc', 'srmr', 'gp_max_val_std', 'gp_max_val_range', 'gp_max_val_min', 'gp_max_val_max', 'gp_max_val_mean', 'gp_max_ix_std', 'gp_max_ix_range', 'gp_max_ix_min', 'gp_max_ix_max', 'gp_max_ix_mean', 'gp_auc_std', 'gp_auc_range', 'gp_auc_min', 'gp_auc_max', 'gp_auc_mean', 'tdoa_std', 'tdoa_range', 'tdoa_min', 'tdoa_max', 'tdoa_mean']
- LABEL_ATTRB = ['facing']
- FACING_DOV_ANGLES = [1]
- NCV = 8
- SCORING = ['accuracy', 'balanced_accuracy', 'f1']
- REFIT_SCORING = balanced_accuracy
- PARAM_GRID = [{'est__n_estimators': [50, 100, 150, 200, 300], 'est__min_samples_split': [2, 5, 10], 'est__min_samples_leaf': [1, 5, 10], 'est__max_features': ['sqrt', 'log2', None], 'est__bootstrap': [False], 'est__n_jobs': [-1], 'est__random_state': [42], 'est__max_samples': [0.01, 0.5, 0.09]}, {'est__n_estimators': [50, 100, 150, 200, 300], 'est__min_samples_split': [2, 5, 10], 'est__min_samples_leaf': [1, 5, 10], 'est__max_features': ['sqrt', 'log2', None], 'est__bootstrap': [True], 'est__oob_score': [True, False], 'est__n_jobs': [-1], 'est__random_state': [42], 'est__max_samples': [0.01, 0.5, 0.09]}]
- TRAIN_SET_SESSION = ['trial1', 'trial2']
- TEST_SET_SESSION = ['trial3', 'trial4', 'trial5']
- DISTANCE = [1, 3]
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
	- sampling_strategy_ = OrderedDict([(1, 60)])
	- shrinkage_ = None
	- sample_indices_ = [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23
 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47
 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71
 72 73 74 75 76 77 78 79 80 81 82 83 84 85 86 87 88 89 90 91 92 93 94 95
 96 97 98 99 32 99 76 54 33 32 98 54 54 11 33 10  1 55 23  1  0 55 55 88
 45 77 76 76 98 55 99 10 22 98 32 44 32 89 11 67 89 44  1 99 76 32 55 33
 76 10 67 88 11 89 33 11  1 23 45 11 89 55  1 45]

- best_estimator
	- base_estimator = ExtraTreeClassifier()
	- n_estimators = 200
	- estimator_params = ('criterion', 'max_depth', 'min_samples_split', 'min_samples_leaf', 'min_weight_fraction_leaf', 'max_features', 'max_leaf_nodes', 'min_impurity_decrease', 'random_state', 'ccp_alpha')
	- bootstrap = False
	- oob_score = False
	- n_jobs = -1
	- random_state = 42
	- verbose = 0
	- warm_start = False
	- class_weight = None
	- max_samples = 0.01
	- criterion = gini
	- max_depth = None
	- min_samples_split = 2
	- min_samples_leaf = 10
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

#### Importance of features
- gp_max_val_min = 0.23343070468290358
- gp_auc_min = 0.19534947033967198
- gp_auc_mean = 0.1628240287392673
- gp_max_val_mean = 0.13391647805787818
- gp_auc_max = 0.0650013294863849
- gp_max_val_max = 0.06288734690192425
- gp_max_val_std = 0.017863060043597917
- gp_max_ix_max = 0.016720340039327666
- srmr = 0.015925274928943578
- tdoa_max = 0.01165078750885867
- hlbr = 0.011508241114604844
- gp_auc_std = 0.010296807199275964
- gp_max_ix_mean = 0.009997897848829951
- gp_max_val_range = 0.005988968769429592
- tdoa_mean = 0.005548275493387776
- tdoa_range = 0.0053078961765621845
- gp_auc_range = 0.005280155745811281
- tdoa_std = 0.003912824690742096
- gp_max_ix_range = 0.003683139737017784
- gp_max_ix_std = 0.003510075509990411
- tdoa_min = 0.0028181658920195755
- coe1[0] = 0.0027688944869986537
- ratio_max_to_9th_ave_peaks = 0.0027292309500410615
- gp_max_ix_min = 0.002233755280939007
- coe3[2] = 0.002069895442567885
- coe1[1] = 0.0015548500686354946
- diff_auc = 0.001290521990878439
- ac_std = 0.0012844648213063028
- high_power = 0.0008639642073744468
- ac_auc = 0.0005447512381328833
- coe3[3] = 0.0005086633004281598
- low_power = 0.0003299199030868469
- diff_std = 0.000285306919201266
- ratio_max_to_10ms_ave_peaks = 0.00011451248398025129
- coe3[0] = 0.0
- coe3[1] = 0.0

## Evaluation
cv = 8
### accuracy
- Scores = [ 0.7894736842105263, 0.7368421052631579, 0.8947368421052632, 0.6842105263157895, 0.8947368421052632, 0.7894736842105263, 0.6666666666666666, 0.6666666666666666 ]
- Mean = 0.7653508771929824
- Standard deviation = 0.08769188168040443

### balanced_accuracy
- Scores = [ 0.8666666666666667, 0.8333333333333333, 0.9333333333333333, 0.525, 0.75, 0.8666666666666667, 0.5333333333333333, 0.4 ]
- Mean = 0.7135416666666666
- Standard deviation = 0.1861496513784899

### f1
- Scores = [ 0.6666666666666666, 0.6153846153846153, 0.8, 0.25, 0.6666666666666666, 0.6666666666666666, 0.25, 0.0 ]
- Mean = 0.48942307692307685
- Standard deviation = 0.2647527082927075

### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 93 | 27 |
| Actual Positive | 5 | 25 |

      