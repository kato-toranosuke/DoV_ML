# ExtraTreesClassifier_SMOTE_2022-01-11_no4
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
- resampler = SMOTE
- estimator = ExtraTreesClassifier

### Arguments for hyperparameter search
- resampler = SMOTE
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
	- k_neighbors = 5
	- n_jobs = -1
	- n_features_in_ = 36
	- sampling_strategy_ = OrderedDict([(0, 4)])
	- nn_k_ = NearestNeighbors(n_neighbors=6)

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
- gp_max_val_mean = 0.12065635296956419
- gp_max_val_min = 0.12047134110646493
- gp_auc_min = 0.11565685854174097
- gp_auc_mean = 0.10346740130603495
- gp_auc_max = 0.0984137161194006
- gp_max_val_max = 0.07622647475132824
- srmr = 0.04806143751005092
- tdoa_mean = 0.024895230271280232
- tdoa_std = 0.024523799692631344
- hlbr = 0.023992248141936595
- ratio_max_to_10ms_ave_peaks = 0.020549196886921216
- gp_max_ix_mean = 0.019109438902077974
- tdoa_min = 0.018204003291615933
- gp_max_ix_std = 0.017652747518923418
- gp_max_ix_min = 0.01603071827835075
- tdoa_range = 0.015104743287666776
- gp_max_ix_range = 0.01474331300956498
- gp_max_val_range = 0.013405231485957474
- gp_auc_range = 0.013015910791738274
- diff_std = 0.011911068121745295
- gp_auc_std = 0.00955848100961262
- tdoa_max = 0.009488947817702197
- diff_auc = 0.00945544958095098
- gp_max_val_std = 0.008054945854035251
- gp_max_ix_max = 0.0065910942126047815
- low_power = 0.005935196317330312
- high_power = 0.005822883128069611
- coe3[2] = 0.005129688153726615
- coe3[3] = 0.004865321315136865
- ratio_max_to_9th_ave_peaks = 0.004432480980557904
- ac_std = 0.004226107428094867
- ac_auc = 0.0039119142918485035
- coe1[0] = 0.0039036942687080724
- coe1[1] = 0.0025325636566263577
- coe3[0] = 0.0
- coe3[1] = 0.0

## Evaluation
cv = 8
### accuracy
- Scores = [ 1.0, 1.0, 1.0, 0.9473684210526315, 1.0, 1.0, 0.9444444444444444, 1.0 ]
- Mean = 0.9864766081871346
- Standard deviation = 0.023434605412149787

### balanced_accuracy
- Scores = [ 1.0, 1.0, 1.0, 0.95, 1.0, 1.0, 0.9444444444444444, 1.0 ]
- Mean = 0.9868055555555556
- Standard deviation = 0.022895613224770205

### f1
- Scores = [ 1.0, 1.0, 1.0, 0.9473684210526316, 1.0, 1.0, 0.9473684210526316, 1.0 ]
- Mean = 0.986842105263158
- Standard deviation = 0.022790142204853623

### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 70 | 2 |
| Actual Positive | 1 | 77 |

      