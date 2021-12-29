# ExtraTreesClassifier_SMOTE_2021-12-29_no4
## Constants
- CSV_PATH = ../out/csv/experiment
- OUTPUT_PATH = ../out/experiment_result/data_of_2021-12-27/NoAGC-0angle-1m
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
- AGC_STATUS = ['NoAGC']

## Loaded CSV
- 2021-12-27_raspi_48000Hz_w1_N2^12_overlap80_new.csv

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
	- sampling_strategy_ = OrderedDict([(1, 24)])
	- nn_k_ = NearestNeighbors(n_neighbors=6)

- best_estimator
	- base_estimator = ExtraTreeClassifier()
	- n_estimators = 300
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
	- min_samples_leaf = 5
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
- diff_auc = 0.15894133766250965
- coe1[1] = 0.10042098318162
- srmr = 0.08584375375503749
- gp_max_val_min = 0.07744973210366433
- gp_auc_min = 0.07540558890385536
- high_power = 0.07536408709451264
- diff_std = 0.07113022716899939
- hlbr = 0.05369223181909497
- coe1[0] = 0.04595352311823188
- gp_max_val_mean = 0.03260657046435213
- gp_auc_mean = 0.03187237542968616
- gp_max_val_max = 0.027942492310459352
- gp_auc_max = 0.02480050511804942
- coe3[2] = 0.01841375281857018
- low_power = 0.01841156877679916
- ratio_max_to_9th_ave_peaks = 0.01735159411628462
- coe3[3] = 0.01671424074447666
- ac_auc = 0.013059162433101113
- ac_std = 0.011730897948034032
- tdoa_std = 0.006702539899199639
- gp_max_ix_std = 0.006479372118314364
- gp_max_ix_mean = 0.004545851589687205
- tdoa_range = 0.0038862479644027944
- tdoa_mean = 0.0037416121496005534
- gp_max_val_range = 0.0030227397580491902
- ratio_max_to_10ms_ave_peaks = 0.0026513287610444845
- tdoa_max = 0.002408910849122858
- gp_max_ix_range = 0.0021227897618617065
- gp_auc_range = 0.0020825977331922693
- gp_auc_std = 0.0019533136185288635
- gp_max_val_std = 0.0016579658087553626
- gp_max_ix_max = 0.0016401050209021786
- coe3[0] = 0.0
- coe3[1] = 0.0
- gp_max_ix_min = 0.0
- tdoa_min = 0.0

## Evaluation
cv = 8
### accuracy
- Scores = [ 0.75, 1.0, 0.875, 1.0, 0.8571428571428571, 0.8571428571428571, 1.0, 0.7142857142857143 ]
- Mean = 0.8816964285714286
- Standard deviation = 0.10524263601898468

### balanced_accuracy
- Scores = [ 0.5, 1.0, 0.9166666666666667, 1.0, 0.5, 0.9166666666666667, 1.0, 0.8333333333333333 ]
- Mean = 0.8333333333333334
- Standard deviation = 0.19982631347136331

### f1
- Scores = [ 0.0, 1.0, 0.8, 1.0, 0.0, 0.6666666666666666, 1.0, 0.5 ]
- Mean = 0.6208333333333333
- Standard deviation = 0.39543839947301246

### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 43 | 4 |
| Actual Positive | 3 | 9 |

      