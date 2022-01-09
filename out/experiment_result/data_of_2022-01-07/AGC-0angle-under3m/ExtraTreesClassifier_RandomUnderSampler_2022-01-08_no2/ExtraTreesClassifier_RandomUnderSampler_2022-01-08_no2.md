# ExtraTreesClassifier_RandomUnderSampler_2022-01-08_no2
## Constants
- CSV_PATH = ../out/csv/experiment
- OUTPUT_PATH = ../out/experiment_result/data_of_2022-01-07/AGC-0angle-under3m
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
	- sampling_strategy_ = OrderedDict([(0, 20)])
	- sample_indices_ = [38  2 28 39 24 36 14 86  6 16 61 41 83 43 84 57 91 75 69 50  0  1 10 11
 22 23 32 33 44 45 54 55 66 67 76 77 88 89 98 99]

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
	- min_samples_split = 5
	- min_samples_leaf = 1
	- min_weight_fraction_leaf = 0.0
	- max_features = None
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
- gp_max_val_min = 0.19146096910857796
- gp_auc_min = 0.1846558771051263
- gp_max_val_mean = 0.1106144625437256
- gp_auc_mean = 0.07329383693878204
- gp_auc_max = 0.06831730026178688
- gp_max_val_max = 0.06558320090528798
- srmr = 0.03471451252724767
- ratio_max_to_9th_ave_peaks = 0.03470796415429785
- diff_auc = 0.028246200189040456
- diff_std = 0.022647209754830373
- high_power = 0.021168158921556535
- hlbr = 0.016845543077248986
- gp_auc_range = 0.016810103305343976
- gp_max_val_range = 0.014055187322448485
- coe1[1] = 0.01193863374789313
- gp_max_ix_max = 0.010383478764246164
- coe3[3] = 0.010049531938609333
- ratio_max_to_10ms_ave_peaks = 0.009510846881060287
- gp_max_val_std = 0.008868174459406826
- ac_auc = 0.00853086444008485
- coe3[2] = 0.007765469843389084
- tdoa_range = 0.007250025676474768
- tdoa_max = 0.006772933704857568
- ac_std = 0.005298340102647747
- coe1[0] = 0.0051704728989388545
- gp_auc_std = 0.0050918712738675775
- gp_max_ix_std = 0.004054558807131989
- low_power = 0.003789788844703146
- gp_max_ix_mean = 0.0036290726817042613
- gp_max_ix_range = 0.0027644878706199463
- tdoa_mean = 0.00243265306122449
- gp_max_ix_min = 0.0018991480087180504
- tdoa_std = 0.0008791208791208793
- tdoa_min = 0.0008000000000000001
- coe3[0] = 0.0
- coe3[1] = 0.0

## Evaluation
cv = 8
### accuracy
- Scores = [ 0.5263157894736842, 0.5789473684210527, 0.8947368421052632, 0.631578947368421, 0.9473684210526315, 0.8421052631578947, 0.5555555555555556, 0.7777777777777778 ]
- Mean = 0.7192982456140351
- Standard deviation = 0.15521882385949703

### balanced_accuracy
- Scores = [ 0.425, 0.55, 0.9333333333333333, 0.49166666666666664, 0.875, 0.9, 0.4666666666666667, 0.7333333333333334 ]
- Mean = 0.671875
- Standard deviation = 0.19869091976540404

### f1
- Scores = [ 0.18181818181818182, 0.3333333333333333, 0.8, 0.22222222222222224, 0.8571428571428571, 0.7272727272727273, 0.2, 0.5 ]
- Mean = 0.4777236652236653
- Standard deviation = 0.26490846845373633

### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 89 | 31 |
| Actual Positive | 3 | 27 |

      