# ExtraTreesClassifier_RandomUnderSampler_2022-01-11_no2
## Constants
- CSV_PATH = ../out/csv/experiment
- OUTPUT_PATH = ../out/experiment_result/data_of_2022-01-10/NoAGC-45angle-under3m
- FEATURE_ATTRBS = ['low_power', 'high_power', 'hlbr', 'coe1[0]', 'coe1[1]', 'coe3[0]', 'coe3[1]', 'coe3[2]', 'coe3[3]', 'ratio_max_to_10ms_ave_peaks', 'ratio_max_to_9th_ave_peaks', 'ac_std', 'ac_auc', 'diff_std', 'diff_auc', 'srmr', 'gp_max_val_std', 'gp_max_val_range', 'gp_max_val_min', 'gp_max_val_max', 'gp_max_val_mean', 'gp_max_ix_std', 'gp_max_ix_range', 'gp_max_ix_min', 'gp_max_ix_max', 'gp_max_ix_mean', 'gp_auc_std', 'gp_auc_range', 'gp_auc_min', 'gp_auc_max', 'gp_auc_mean', 'tdoa_std', 'tdoa_range', 'tdoa_min', 'tdoa_max', 'tdoa_mean']
- LABEL_ATTRB = ['facing2']
- FACING_DOV_ANGLES = [1, 2]
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
- resampler = RandomUnderSampler
- estimator = ExtraTreesClassifier

### Arguments for hyperparameter search
- resampler = RandomUnderSampler
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
	- replacement = False
	- n_features_in_ = 36
	- sampling_strategy_ = OrderedDict([(1, 48)])
	- sample_indices_ = [ 4  5  6  7  8  9 14 15 16 17 18 19 26 27 28 29 36 37 38 39 40 41 48 49
 50 51 58 59 60 61 62 63 70 71 72 73 80 81 82 83 84 85 90 91 92 93 94 95
 35 77 89 24 79 11 33 98  3 64 25 20 52 12 66 10 69 46 86 65 97 31 21 32
 56 68 47 23  0 88 53 57 75 55 87  1 43  2 76 67 45 96 22 44 34 99 42 13]

- best_estimator
	- base_estimator = ExtraTreeClassifier()
	- n_estimators = 150
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
	- min_samples_split = 5
	- min_samples_leaf = 1
	- min_weight_fraction_leaf = 0.0
	- max_features = sqrt
	- max_leaf_nodes = None
	- min_impurity_decrease = 0.0
	- ccp_alpha = 0.0
	- n_features_in_ = 36
	- n_outputs_ = 1
	- classes_ = [0 1]
	- n_classes_ = 2
	- base_estimator_ = ExtraTreeClassifier()

#### Importance of features
- gp_max_val_mean = 0.12955604899453707
- gp_max_val_min = 0.12874229917613197
- gp_auc_mean = 0.11754573231085798
- gp_auc_min = 0.10998196067707314
- gp_auc_max = 0.0973278440589401
- gp_max_val_max = 0.07811691720902034
- srmr = 0.03780162582180161
- ratio_max_to_10ms_ave_peaks = 0.0280696575646508
- tdoa_std = 0.022733663542627812
- tdoa_mean = 0.022180846941890715
- gp_max_ix_mean = 0.021052826898597287
- gp_max_ix_range = 0.01955643791691824
- hlbr = 0.018386673971770313
- tdoa_min = 0.016144197748548784
- tdoa_range = 0.015413626016288103
- gp_max_ix_std = 0.015181885186098277
- gp_auc_range = 0.014810200519478237
- gp_max_ix_min = 0.012321090677731631
- gp_max_val_range = 0.011416130388245274
- diff_auc = 0.010753037282217643
- diff_std = 0.009491193444274975
- gp_auc_std = 0.008668996690364384
- gp_max_val_std = 0.008637114677247655
- high_power = 0.007794287257110894
- tdoa_max = 0.007758473578559378
- low_power = 0.005877304933449549
- gp_max_ix_max = 0.004688509430987199
- coe1[1] = 0.004320226812049083
- coe1[0] = 0.003352318711067487
- coe3[3] = 0.003329984362923967
- coe3[2] = 0.0031332579077927203
- ac_auc = 0.0029131351935109454
- ac_std = 0.001830556901080828
- ratio_max_to_9th_ave_peaks = 0.0011119371961554683
- coe3[0] = 0.0
- coe3[1] = 0.0

## Evaluation
cv = 8
### accuracy
- Scores = [ 0.9473684210526315, 1.0, 1.0, 0.9473684210526315, 0.9473684210526315, 1.0, 0.9444444444444444, 1.0 ]
- Mean = 0.9733187134502923
- Standard deviation = 0.02669630275193737

### balanced_accuracy
- Scores = [ 0.9444444444444444, 1.0, 1.0, 0.95, 0.95, 1.0, 0.9444444444444444, 1.0 ]
- Mean = 0.9736111111111111
- Standard deviation = 0.026461887337857863

### f1
- Scores = [ 0.9523809523809523, 1.0, 1.0, 0.9473684210526316, 0.9473684210526316, 1.0, 0.9473684210526316, 1.0 ]
- Mean = 0.9743107769423559
- Standard deviation = 0.02573502854375042

### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 70 | 2 |
| Actual Positive | 1 | 77 |

      