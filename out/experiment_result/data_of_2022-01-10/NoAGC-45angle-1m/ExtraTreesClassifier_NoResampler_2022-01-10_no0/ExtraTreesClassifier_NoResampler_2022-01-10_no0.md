# ExtraTreesClassifier_NoResampler_2022-01-10_no0
## Constants
- CSV_PATH = ../out/csv/experiment
- OUTPUT_PATH = ../out/experiment_result/data_of_2022-01-10/NoAGC-45angle-1m
- FEATURE_ATTRBS = ['low_power', 'high_power', 'hlbr', 'coe1[0]', 'coe1[1]', 'coe3[0]', 'coe3[1]', 'coe3[2]', 'coe3[3]', 'ratio_max_to_10ms_ave_peaks', 'ratio_max_to_9th_ave_peaks', 'ac_std', 'ac_auc', 'diff_std', 'diff_auc', 'srmr', 'gp_max_val_std', 'gp_max_val_range', 'gp_max_val_min', 'gp_max_val_max', 'gp_max_val_mean', 'gp_max_ix_std', 'gp_max_ix_range', 'gp_max_ix_min', 'gp_max_ix_max', 'gp_max_ix_mean', 'gp_auc_std', 'gp_auc_range', 'gp_auc_min', 'gp_auc_max', 'gp_auc_mean', 'tdoa_std', 'tdoa_range', 'tdoa_min', 'tdoa_max', 'tdoa_mean']
- LABEL_ATTRB = ['facing2']
- FACING_DOV_ANGLES = [1, 2]
- NCV = 8
- SCORING = ['accuracy', 'balanced_accuracy', 'f1']
- REFIT_SCORING = balanced_accuracy
- PARAM_GRID = [{'est__n_estimators': [50, 100, 150, 200, 300], 'est__min_samples_split': [2, 5, 10], 'est__min_samples_leaf': [1, 5, 10], 'est__max_features': ['sqrt', 'log2', None], 'est__bootstrap': [False], 'est__n_jobs': [-1], 'est__random_state': [42], 'est__max_samples': [0.01, 0.5, 0.09]}, {'est__n_estimators': [50, 100, 150, 200, 300], 'est__min_samples_split': [2, 5, 10], 'est__min_samples_leaf': [1, 5, 10], 'est__max_features': ['sqrt', 'log2', None], 'est__bootstrap': [True], 'est__oob_score': [True, False], 'est__n_jobs': [-1], 'est__random_state': [42], 'est__max_samples': [0.01, 0.5, 0.09]}]
- TRAIN_SET_SESSION = ['trial1', 'trial2']
- TEST_SET_SESSION = ['trial3', 'trial4', 'trial5']
- DISTANCE = [1]
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
	- ccp_alpha = 0.0
	- n_features_in_ = 36
	- n_outputs_ = 1
	- classes_ = [0 1]
	- n_classes_ = 2
	- base_estimator_ = ExtraTreeClassifier()

#### Importance of features
- gp_auc_max = 0.14129787840695793
- gp_max_val_mean = 0.11145607035847659
- gp_max_val_max = 0.088634655884025
- tdoa_range = 0.08577750786644062
- gp_auc_mean = 0.06486535647099932
- tdoa_min = 0.05299530974707412
- gp_max_ix_range = 0.05137122602888519
- gp_max_ix_min = 0.046941903029150134
- gp_auc_min = 0.03701539388096511
- gp_max_val_min = 0.03483949748806558
- gp_max_ix_std = 0.03461672062349268
- hlbr = 0.030181234366545413
- tdoa_mean = 0.02742824497143749
- ratio_max_to_10ms_ave_peaks = 0.026370728835178135
- tdoa_std = 0.026122447471116972
- srmr = 0.02085501676626505
- gp_auc_range = 0.017317276347834136
- gp_max_ix_mean = 0.013804726747847912
- gp_max_val_range = 0.012559968629476108
- gp_max_val_std = 0.012428015485108147
- gp_auc_std = 0.009150337615411149
- ac_std = 0.008055626783500809
- diff_std = 0.007153325787663648
- diff_auc = 0.007097352600895109
- coe1[1] = 0.004469099276791586
- coe3[3] = 0.004049553092861097
- high_power = 0.003871237008779762
- coe1[0] = 0.003765743931588231
- ac_auc = 0.0031054464810011937
- low_power = 0.0028667079448329463
- ratio_max_to_9th_ave_peaks = 0.0028317102235371474
- tdoa_max = 0.002653133903133904
- gp_max_ix_max = 0.00220127912043673
- coe3[2] = 0.0018502668242251577
- coe3[0] = 0.0
- coe3[1] = 0.0

## Evaluation
cv = 8
### accuracy
- Scores = [ 0.8, 1.0, 1.0, 1.0, 0.8888888888888888, 1.0, 1.0, 0.7777777777777778 ]
- Mean = 0.9333333333333333
- Standard deviation = 0.0909483641319161

### balanced_accuracy
- Scores = [ 0.8, 1.0, 1.0, 1.0, 0.9, 1.0, 1.0, 0.8 ]
- Mean = 0.9375
- Standard deviation = 0.08569568250501304

### f1
- Scores = [ 0.8333333333333333, 1.0, 1.0, 1.0, 0.888888888888889, 1.0, 1.0, 0.8 ]
- Mean = 0.9402777777777778
- Standard deviation = 0.08030372514152091

### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 32 | 4 |
| Actual Positive | 1 | 38 |

      