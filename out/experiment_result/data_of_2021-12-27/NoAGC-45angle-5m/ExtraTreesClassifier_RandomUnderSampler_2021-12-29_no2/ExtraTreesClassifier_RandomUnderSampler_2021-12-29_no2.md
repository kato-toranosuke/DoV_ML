# ExtraTreesClassifier_RandomUnderSampler_2021-12-29_no2
## Constants
- CSV_PATH = ../out/csv/experiment
- OUTPUT_PATH = ../out/experiment_result/data_of_2021-12-27/NoAGC-45angle-5m
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
- 2021-12-27_raspi_48000Hz_w1_N2^12_overlap80_new.csv

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
	- sampling_strategy_ = OrderedDict([(1, 18)])
	- sample_indices_ = [ 4  5  6  7  8  9 16 17 18 19 20 21 28 29 30 31 32 33  0 25 14  1 27 11
 38 23  3 10 35 24 36 34  2 15 39 13]

- best_estimator
	- base_estimator = ExtraTreeClassifier()
	- n_estimators = 100
	- estimator_params = ('criterion', 'max_depth', 'min_samples_split', 'min_samples_leaf', 'min_weight_fraction_leaf', 'max_features', 'max_leaf_nodes', 'min_impurity_decrease', 'min_impurity_split', 'random_state', 'ccp_alpha')
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

#### Importance of features
- gp_auc_max = 0.1320209487201601
- gp_auc_mean = 0.1269808397815355
- gp_auc_min = 0.11159277381159197
- gp_max_val_min = 0.10311741314968781
- gp_max_val_mean = 0.09805930997937548
- gp_max_val_max = 0.09142700955286767
- gp_max_val_std = 0.0439320813221069
- hlbr = 0.03241360071471099
- srmr = 0.029006910133137335
- high_power = 0.028458687727626785
- gp_auc_range = 0.028379559816899973
- gp_auc_std = 0.02225826935300952
- gp_max_val_range = 0.014202821869488538
- gp_max_ix_max = 0.013877618840854134
- coe1[0] = 0.01309636891793755
- tdoa_max = 0.012245845772161564
- diff_auc = 0.011349879716012439
- diff_std = 0.009541151280281716
- ac_std = 0.008917553911516763
- coe1[1] = 0.008666127181573407
- gp_max_ix_min = 0.008618042233728512
- tdoa_range = 0.00797850218992589
- low_power = 0.007235212855642965
- coe3[3] = 0.006939465441753774
- tdoa_min = 0.006216931216931217
- gp_max_ix_range = 0.00488888888888889
- ac_auc = 0.004104938271604938
- ratio_max_to_9th_ave_peaks = 0.0037073347857661584
- coe3[2] = 0.003480308205153408
- gp_max_ix_std = 0.002492877492877493
- tdoa_mean = 0.0022120914512218873
- gp_max_ix_mean = 0.0012177328843995517
- ratio_max_to_10ms_ave_peaks = 0.0009083570750237417
- tdoa_std = 0.00045454545454545465
- coe3[0] = 0.0
- coe3[1] = 0.0

## Evaluation
cv = 8
### accuracy
- Scores = [ 1.0, 1.0, 1.0, 1.0, 1.0, 0.8571428571428571, 1.0, 1.0 ]
- Mean = 0.9821428571428572
- Standard deviation = 0.047245559126153414

### balanced_accuracy
- Scores = [ 1.0, 1.0, 1.0, 1.0, 1.0, 0.875, 1.0, 1.0 ]
- Mean = 0.984375
- Standard deviation = 0.04133986423538423

### f1
- Scores = [ 1.0, 1.0, 1.0, 1.0, 1.0, 0.8571428571428571, 1.0, 1.0 ]
- Mean = 0.9821428571428572
- Standard deviation = 0.047245559126153414

### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 27 | 0 |
| Actual Positive | 1 | 32 |

      