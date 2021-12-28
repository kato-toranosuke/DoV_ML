# ExtraTreesClassifier_SMOTE_2021-12-28_no4
## Constants
- CSV_PATH = ../out/csv/experiment
- OUTPUT_PATH = ../out/experiment_result/2021-12-27-3m
- FEATURE_ATTRBS = ['low_power', 'high_power', 'hlbr', 'coe1[0]', 'coe1[1]', 'coe3[0]', 'coe3[1]', 'coe3[2]', 'coe3[3]', 'ratio_max_to_10ms_ave_peaks', 'ratio_max_to_9th_ave_peaks', 'ac_std', 'ac_auc', 'diff_std', 'diff_auc', 'srmr', 'gp_max_val_std', 'gp_max_val_range', 'gp_max_val_min', 'gp_max_val_max', 'gp_max_val_mean', 'gp_max_ix_std', 'gp_max_ix_range', 'gp_max_ix_min', 'gp_max_ix_max', 'gp_max_ix_mean', 'gp_auc_std', 'gp_auc_range', 'gp_auc_min', 'gp_auc_max', 'gp_auc_mean', 'tdoa_std', 'tdoa_range', 'tdoa_min', 'tdoa_max', 'tdoa_mean']
- LABEL_ATTRB = ['facing']
- FACING_DOV_ANGLES = [1]
- NCV = 8
- SCORING = ['accuracy', 'balanced_accuracy', 'f1']
- REFIT_SCORING = balanced_accuracy
- PARAM_GRID = [{'est__n_estimators': [50, 100, 150, 200, 300], 'est__min_samples_split': [2, 5, 10], 'est__min_samples_leaf': [1, 5, 10], 'est__max_features': ['sqrt', 'log2', None], 'est__bootstrap': [False], 'est__n_jobs': [-1], 'est__random_state': [42], 'est__max_samples': [0.01, 0.5, 0.09]}, {'est__n_estimators': [50, 100, 150, 200, 300], 'est__min_samples_split': [2, 5, 10], 'est__min_samples_leaf': [1, 5, 10], 'est__max_features': ['sqrt', 'log2', None], 'est__bootstrap': [True], 'est__oob_score': [True, False], 'est__n_jobs': [-1], 'est__random_state': [42], 'est__max_samples': [0.01, 0.5, 0.09]}]
- TRAIN_SET_SESSION = ['trial1', 'trial2']
- TEST_SET_SESSION = ['trial3', 'trial4', 'trial5']

## Loaded CSV
- 2021-12-27_raspi_48000Hz_w1_N2^12_overlap80_withfacing.csv

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
	- sampling_strategy_ = OrderedDict([(1, 28)])
	- nn_k_ = NearestNeighbors(n_neighbors=6)

- best_estimator
	- base_estimator = ExtraTreeClassifier()
	- n_estimators = 150
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
	- max_features = log2
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
- diff_auc = 0.08627865023973703
- gp_auc_max = 0.06677803802417187
- gp_auc_min = 0.062592362115889
- coe1[0] = 0.060452796119229824
- gp_max_val_max = 0.055887071884611284
- low_power = 0.0525671652986135
- gp_max_val_mean = 0.051842407487622894
- gp_auc_mean = 0.05098353447451839
- coe1[1] = 0.04987933052451335
- coe3[2] = 0.049065528634516166
- high_power = 0.04729185663902598
- gp_max_ix_mean = 0.04498010684915177
- gp_max_val_min = 0.04286488679021573
- coe3[3] = 0.04205234454060621
- diff_std = 0.04092338151641534
- ac_std = 0.03560806053598066
- hlbr = 0.03369194365282209
- tdoa_mean = 0.0241781835782674
- ac_auc = 0.021968899552050777
- srmr = 0.019764197430769098
- gp_max_ix_std = 0.008905714362151158
- gp_max_val_std = 0.008591725490343888
- tdoa_std = 0.008274439945746281
- gp_auc_std = 0.007061647430738895
- ratio_max_to_9th_ave_peaks = 0.004785292997453354
- gp_max_ix_max = 0.004693191026846281
- ratio_max_to_10ms_ave_peaks = 0.004084706263754047
- tdoa_max = 0.00402304269241845
- gp_max_val_range = 0.00372843923171857
- tdoa_range = 0.002309403016912478
- gp_auc_range = 0.002159606621808189
- gp_max_ix_range = 0.0017320450313800559
- coe3[0] = 0.0
- coe3[1] = 0.0
- gp_max_ix_min = 0.0
- tdoa_min = 0.0

## Evaluation
cv = 8
### accuracy
- Scores = [ 0.8, 1.0, 0.8888888888888888, 1.0, 0.7777777777777778, 1.0, 0.6666666666666666, 0.6666666666666666 ]
- Mean = 0.85
- Standard deviation = 0.13414107186277374

### balanced_accuracy
- Scores = [ 0.875, 1.0, 0.9285714285714286, 1.0, 0.8571428571428572, 1.0, 0.42857142857142855, 0.8125 ]
- Mean = 0.8627232142857143
- Standard deviation = 0.17750448556239476

### f1
- Scores = [ 0.6666666666666666, 1.0, 0.8, 1.0, 0.6666666666666666, 1.0, 0.0, 0.4 ]
- Mean = 0.6916666666666667
- Standard deviation = 0.32818947779192026

### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 50 | 9 |
| Actual Positive | 2 | 13 |

      