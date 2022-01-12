# ExtraTreesClassifier_SMOTE_2022-01-10_no4
## Constants
- CSV_PATH = ../out/csv/experiment
- OUTPUT_PATH = ../out/experiment_result/data_of_2022-01-10/NoAGC-45angle-under5m
- FEATURE_ATTRBS = ['low_power', 'high_power', 'hlbr', 'coe1[0]', 'coe1[1]', 'coe3[0]', 'coe3[1]', 'coe3[2]', 'coe3[3]', 'ratio_max_to_10ms_ave_peaks', 'ratio_max_to_9th_ave_peaks', 'ac_std', 'ac_auc', 'diff_std', 'diff_auc', 'srmr', 'gp_max_val_std', 'gp_max_val_range', 'gp_max_val_min', 'gp_max_val_max', 'gp_max_val_mean', 'gp_max_ix_std', 'gp_max_ix_range', 'gp_max_ix_min', 'gp_max_ix_max', 'gp_max_ix_mean', 'gp_auc_std', 'gp_auc_range', 'gp_auc_min', 'gp_auc_max', 'gp_auc_mean', 'tdoa_std', 'tdoa_range', 'tdoa_min', 'tdoa_max', 'tdoa_mean']
- LABEL_ATTRB = ['facing2']
- FACING_DOV_ANGLES = [1, 2]
- NCV = 8
- SCORING = ['accuracy', 'balanced_accuracy', 'f1']
- REFIT_SCORING = balanced_accuracy
- PARAM_GRID = [{'est__n_estimators': [50, 100, 150, 200, 300], 'est__min_samples_split': [2, 5, 10], 'est__min_samples_leaf': [1, 5, 10], 'est__max_features': ['sqrt', 'log2', None], 'est__bootstrap': [False], 'est__n_jobs': [-1], 'est__random_state': [42], 'est__max_samples': [0.01, 0.5, 0.09]}, {'est__n_estimators': [50, 100, 150, 200, 300], 'est__min_samples_split': [2, 5, 10], 'est__min_samples_leaf': [1, 5, 10], 'est__max_features': ['sqrt', 'log2', None], 'est__bootstrap': [True], 'est__oob_score': [True, False], 'est__n_jobs': [-1], 'est__random_state': [42], 'est__max_samples': [0.01, 0.5, 0.09]}]
- TRAIN_SET_SESSION = ['trial1', 'trial2']
- TEST_SET_SESSION = ['trial3', 'trial4', 'trial5']
- DISTANCE = [1, 3, 5]
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
	- sampling_strategy_ = OrderedDict([(0, 6)])
	- nn_k_ = NearestNeighbors(n_neighbors=6)

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
- gp_max_val_mean = 0.12140306855184646
- gp_auc_min = 0.1188411909377614
- gp_auc_max = 0.11052738033823667
- gp_max_val_min = 0.08016839489387306
- gp_max_val_max = 0.06761008490336443
- gp_auc_mean = 0.054105746723639256
- gp_max_ix_mean = 0.03638302788124113
- hlbr = 0.03621470313549274
- tdoa_min = 0.033878016107867726
- gp_max_ix_std = 0.03276905856138278
- tdoa_mean = 0.031759877376413226
- srmr = 0.028066257935880766
- gp_max_ix_min = 0.026944234880314197
- tdoa_range = 0.020506227735235125
- gp_max_ix_range = 0.01827328017134553
- gp_max_val_std = 0.017955558109354473
- high_power = 0.017790468794548236
- tdoa_std = 0.017225351602738356
- ratio_max_to_10ms_ave_peaks = 0.0156394945325808
- gp_max_val_range = 0.014507523955388306
- gp_auc_range = 0.012678978536500043
- gp_auc_std = 0.011758594325633523
- tdoa_max = 0.008889282806201503
- diff_std = 0.008700797153239839
- coe3[2] = 0.008134199078703306
- coe3[3] = 0.007688205674580231
- diff_auc = 0.00679731875410889
- gp_max_ix_max = 0.006529672985713584
- coe1[1] = 0.005746998513739138
- ac_auc = 0.005409125151244196
- low_power = 0.00471352544889444
- coe1[0] = 0.004490056927116608
- ratio_max_to_9th_ave_peaks = 0.0041439235260431065
- ac_std = 0.003750373989776946
- coe3[0] = 0.0
- coe3[1] = 0.0

## Evaluation
cv = 8
### accuracy
- Scores = [ 0.9310344827586207, 0.9642857142857143, 0.8571428571428571, 0.8928571428571429, 0.8214285714285714, 1.0, 0.9285714285714286, 0.7857142857142857 ]
- Mean = 0.8976293103448276
- Standard deviation = 0.0679977999055802

### balanced_accuracy
- Scores = [ 0.9285714285714286, 0.9666666666666667, 0.8666666666666667, 0.8897435897435897, 0.8179487179487179, 1.0, 0.9285714285714286, 0.7857142857142858 ]
- Mean = 0.8979853479853479
- Standard deviation = 0.06805748430762562

### f1
- Scores = [ 0.9375, 0.9655172413793104, 0.846153846153846, 0.9032258064516129, 0.8387096774193549, 1.0, 0.9333333333333333, 0.75 ]
- Mean = 0.8968049880921822
- Standard deviation = 0.07574176768275187

### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 97 | 11 |
| Actual Positive | 13 | 104 |

      