# ExtraTreesClassifier_RandomOverSampler_2022-01-10_no3
## Constants
- CSV_PATH = ../out/csv/experiment
- OUTPUT_PATH = ../out/experiment_result/data_of_2022-01-10/NoAGC-0angle-5m
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
	- n_estimators = 50
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
	- min_samples_leaf = 5
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

#### Importance of features
- gp_max_val_max = 0.16146695715207582
- gp_auc_max = 0.1215651727340712
- gp_auc_min = 0.10480086455475769
- gp_max_val_std = 0.07401838679460954
- gp_max_val_min = 0.0724130024363422
- gp_max_val_mean = 0.06845816253492117
- gp_auc_mean = 0.06787363502454301
- hlbr = 0.04565346558954461
- srmr = 0.04512977350115313
- gp_auc_std = 0.04057119713409013
- gp_auc_range = 0.021961246726488186
- diff_std = 0.01663339848148769
- diff_auc = 0.01506511318985987
- gp_max_ix_range = 0.01493194802502604
- gp_max_ix_max = 0.012401740354200988
- gp_max_ix_mean = 0.010910302609294965
- ac_std = 0.010094480920828435
- gp_max_ix_min = 0.009880596370712433
- coe3[2] = 0.009387299158491062
- tdoa_max = 0.008772727685451332
- high_power = 0.008691820597779797
- ratio_max_to_10ms_ave_peaks = 0.008422436166208509
- gp_max_val_range = 0.0074891403892094486
- ratio_max_to_9th_ave_peaks = 0.0073626256776119945
- low_power = 0.0059831575011576885
- tdoa_min = 0.005803088111240917
- tdoa_mean = 0.005660619040466366
- coe3[3] = 0.005356441704107864
- tdoa_std = 0.00462620672853346
- coe1[1] = 0.004154010177007059
- coe1[0] = 0.001681961697559491
- tdoa_range = 0.0015956019219692979
- gp_max_ix_std = 0.0011834193091985797
- coe3[0] = 0.0
- coe3[1] = 0.0
- ac_auc = 0.0

## Evaluation
cv = 8
### accuracy
- Scores = [ 0.8, 0.8, 0.8, 1.0, 0.7777777777777778, 1.0, 0.8888888888888888, 1.0 ]
- Mean = 0.8833333333333333
- Standard deviation = 0.09541980020732035

### balanced_accuracy
- Scores = [ 0.875, 0.6875, 0.875, 1.0, 0.8571428571428572, 1.0, 0.9285714285714286, 1.0 ]
- Mean = 0.9029017857142857
- Standard deviation = 0.09936797040661338

### f1
- Scores = [ 0.6666666666666666, 0.5, 0.6666666666666666, 1.0, 0.6666666666666666, 1.0, 0.8, 1.0 ]
- Mean = 0.7875
- Standard deviation = 0.18099838857477893

### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 52 | 8 |
| Actual Positive | 2 | 13 |

      