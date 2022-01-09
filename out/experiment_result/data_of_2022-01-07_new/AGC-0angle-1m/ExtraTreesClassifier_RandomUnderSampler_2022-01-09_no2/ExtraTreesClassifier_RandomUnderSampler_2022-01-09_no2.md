# ExtraTreesClassifier_RandomUnderSampler_2022-01-09_no2
## Constants
- CSV_PATH = ../out/csv/experiment
- OUTPUT_PATH = ../out/experiment_result/data_of_2022-01-07_new/AGC-0angle-1m
- FEATURE_ATTRBS = ['low_power', 'high_power', 'hlbr', 'coe1[0]', 'coe1[1]', 'coe3[0]', 'coe3[1]', 'coe3[2]', 'coe3[3]', 'ratio_max_to_10ms_ave_peaks', 'ratio_max_to_9th_ave_peaks', 'ac_std', 'ac_auc', 'diff_std', 'diff_auc', 'srmr', 'gp_max_val_std', 'gp_max_val_range', 'gp_max_val_min', 'gp_max_val_max', 'gp_max_val_mean', 'gp_max_ix_std', 'gp_max_ix_range', 'gp_max_ix_min', 'gp_max_ix_max', 'gp_max_ix_mean', 'gp_auc_std', 'gp_auc_range', 'gp_auc_min', 'gp_auc_max', 'gp_auc_mean', 'tdoa_std', 'tdoa_range', 'tdoa_min', 'tdoa_max', 'tdoa_mean']
- LABEL_ATTRB = ['facing']
- FACING_DOV_ANGLES = [1]
- NCV = 8
- SCORING = ['accuracy', 'balanced_accuracy', 'f1']
- REFIT_SCORING = balanced_accuracy
- PARAM_GRID = [{'est__n_estimators': [50, 100, 150, 200, 300], 'est__min_samples_split': [2, 5, 10], 'est__min_samples_leaf': [1, 5, 10], 'est__max_features': ['sqrt', 'log2', None], 'est__bootstrap': [False], 'est__n_jobs': [-1], 'est__random_state': [42], 'est__max_samples': [0.01, 0.5, 0.09]}, {'est__n_estimators': [50, 100, 150, 200, 300], 'est__min_samples_split': [2, 5, 10], 'est__min_samples_leaf': [1, 5, 10], 'est__max_features': ['sqrt', 'log2', None], 'est__bootstrap': [True], 'est__oob_score': [True, False], 'est__n_jobs': [-1], 'est__random_state': [42], 'est__max_samples': [0.01, 0.5, 0.09]}]
- TRAIN_SET_SESSION = ['trial1', 'trial2']
- TEST_SET_SESSION = ['trial3', 'trial4', 'trial5']
- DISTANCE = [1]
- AGC_STATUS = ['AGC']

## Loaded CSV
- 2021-12-27_raspi_48000Hz_w1_N2^12_overlap80_with2022-01-07.csv

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
	- sampling_strategy_ = OrderedDict([(0, 10)])
	- sample_indices_ = [23 20 19 32  6 16 45 33 47  8  0  1 12 13 24 25 36 37 48 49]

- best_estimator
	- base_estimator = ExtraTreeClassifier()
	- n_estimators = 100
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

#### Importance of features
- gp_max_val_min = 0.16972990342990346
- gp_auc_min = 0.1573974358974359
- ratio_max_to_10ms_ave_peaks = 0.10255540015540017
- gp_max_val_mean = 0.10114819624819628
- gp_auc_mean = 0.0803763014763015
- gp_max_val_max = 0.07112556332556334
- srmr = 0.044365034965034966
- hlbr = 0.043819735819735826
- gp_auc_max = 0.04139347319347321
- gp_auc_range = 0.029294871794871797
- gp_max_val_range = 0.02782927072927073
- tdoa_max = 0.01940303030303031
- gp_auc_std = 0.01571662781662782
- gp_max_ix_max = 0.015521212121212125
- diff_std = 0.010935131535131537
- ratio_max_to_9th_ave_peaks = 0.009106060606060609
- gp_max_val_std = 0.00794871794871795
- tdoa_std = 0.007500000000000001
- high_power = 0.005115384615384617
- tdoa_range = 0.005000000000000001
- coe1[0] = 0.004995959595959597
- tdoa_mean = 0.0036820512820512834
- gp_max_ix_std = 0.0036666666666666675
- coe1[1] = 0.003633333333333334
- diff_auc = 0.003595959595959597
- coe3[2] = 0.0034959595959595966
- tdoa_min = 0.002482051282051283
- ac_auc = 0.002333333333333334
- coe3[3] = 0.0020000000000000005
- ac_std = 0.0020000000000000005
- gp_max_ix_mean = 0.0015000000000000002
- gp_max_ix_range = 0.0013333333333333335
- low_power = 0.0
- coe3[0] = 0.0
- coe3[1] = 0.0
- gp_max_ix_min = 0.0

## Evaluation
cv = 8
### accuracy
- Scores = [ 0.4, 0.6, 0.8, 0.6666666666666666, 1.0, 0.6666666666666666, 0.8888888888888888, 1.0 ]
- Mean = 0.7527777777777778
- Standard deviation = 0.1954537298028031

### balanced_accuracy
- Scores = [ 0.625, 0.75, 0.875, 0.42857142857142855, 1.0, 0.7857142857142857, 0.75, 1.0 ]
- Mean = 0.7767857142857143
- Standard deviation = 0.1785714285714286

### f1
- Scores = [ 0.4, 0.5, 0.6666666666666666, 0.0, 1.0, 0.5714285714285715, 0.6666666666666666, 1.0 ]
- Mean = 0.6005952380952381
- Standard deviation = 0.30407696002664786

### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 43 | 17 |
| Actual Positive | 1 | 14 |

      