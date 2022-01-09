# ExtraTreesClassifier_SMOTE_2022-01-09_no4
## Constants
- CSV_PATH = ../out/csv/experiment
- OUTPUT_PATH = ../out/experiment_result/data_of_2022-01-07_new/AGC-0angle-5m
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
- AGC_STATUS = ['AGC']

## Loaded CSV
- 2021-12-27_raspi_48000Hz_w1_N2^12_overlap80_with2022-01-07.csv

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
	- sampling_strategy_ = OrderedDict([(1, 30)])
	- nn_k_ = NearestNeighbors(n_neighbors=6)

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
	- min_samples_leaf = 5
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
- high_power = 0.1660989762165036
- gp_auc_max = 0.09472795832796672
- gp_max_val_mean = 0.08823283399884257
- gp_auc_mean = 0.07477711484173055
- gp_max_val_max = 0.07431216677904018
- gp_max_val_min = 0.07186855141667765
- hlbr = 0.07080367940081275
- gp_auc_min = 0.06971033097422359
- diff_std = 0.05673648497538877
- diff_auc = 0.04826671474147271
- srmr = 0.021382998282487988
- low_power = 0.01478145259596998
- coe3[3] = 0.013193892853568685
- coe1[0] = 0.012227342542492877
- tdoa_min = 0.011086144818933386
- ac_auc = 0.010856407199353168
- tdoa_max = 0.009868616786311572
- coe1[1] = 0.009455632252875679
- gp_max_ix_max = 0.00884738188954388
- tdoa_mean = 0.008753212913262816
- gp_max_ix_mean = 0.00755141651141823
- coe3[2] = 0.0064641833872065586
- tdoa_range = 0.005862789941234277
- gp_max_ix_range = 0.005317937973071651
- ratio_max_to_9th_ave_peaks = 0.00519166565857447
- ratio_max_to_10ms_ave_peaks = 0.005078698932432335
- gp_auc_std = 0.005070273608543067
- gp_max_val_std = 0.004382809307800014
- gp_max_ix_min = 0.003850581655717528
- ac_std = 0.003648097637757191
- gp_max_val_range = 0.003483901104027394
- gp_auc_range = 0.0034632406217621594
- tdoa_std = 0.002635065302348356
- gp_max_ix_std = 0.002011444550647748
- coe3[0] = 0.0
- coe3[1] = 0.0

## Evaluation
cv = 8
### accuracy
- Scores = [ 0.9, 0.9, 0.9, 0.8888888888888888, 0.7777777777777778, 1.0, 0.7777777777777778, 1.0 ]
- Mean = 0.8930555555555555
- Standard deviation = 0.07875134723519353

### balanced_accuracy
- Scores = [ 0.9375, 0.9375, 0.75, 0.9285714285714286, 0.8571428571428572, 1.0, 0.5, 1.0 ]
- Mean = 0.8638392857142858
- Standard deviation = 0.1571244662533756

### f1
- Scores = [ 0.8, 0.8, 0.6666666666666666, 0.8, 0.6666666666666666, 1.0, 0.0, 1.0 ]
- Mean = 0.7166666666666667
- Standard deviation = 0.2958039891549808

### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 53 | 7 |
| Actual Positive | 2 | 13 |

      