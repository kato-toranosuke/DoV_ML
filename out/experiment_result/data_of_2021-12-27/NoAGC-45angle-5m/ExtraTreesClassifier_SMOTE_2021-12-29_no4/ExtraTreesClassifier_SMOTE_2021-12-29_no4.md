# ExtraTreesClassifier_SMOTE_2021-12-29_no4
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
- gp_max_val_min = 0.12282126583197484
- gp_auc_mean = 0.12128314671645835
- gp_auc_max = 0.11943217760007414
- gp_max_val_mean = 0.10704468171855884
- gp_auc_min = 0.10206249410906751
- gp_max_val_max = 0.10158888683705757
- high_power = 0.03171400253209333
- gp_max_val_std = 0.030329311144668678
- srmr = 0.0277281788235675
- diff_auc = 0.026791542310476396
- hlbr = 0.026694687293588114
- gp_auc_std = 0.023228192702524256
- diff_std = 0.01743100162451988
- gp_max_ix_max = 0.016081212687095045
- gp_auc_range = 0.014406854998584536
- gp_max_ix_range = 0.013905745769382137
- tdoa_max = 0.013466931319538744
- tdoa_range = 0.010386050056103536
- gp_max_ix_min = 0.009711991711991715
- coe1[0] = 0.009100961571976068
- ac_std = 0.008655493166836814
- coe3[3] = 0.008625991750892938
- gp_max_val_range = 0.0073785318229861495
- tdoa_min = 0.0070537768826538895
- low_power = 0.004810330555428594
- coe1[1] = 0.004801665301665304
- coe3[2] = 0.0030116319268493185
- ratio_max_to_9th_ave_peaks = 0.002165103415103416
- gp_max_ix_std = 0.0017460317460317462
- ac_auc = 0.0016517402185851386
- ratio_max_to_10ms_ave_peaks = 0.0014288276587741838
- gp_max_ix_mean = 0.001405520405520406
- tdoa_std = 0.001103896103896104
- tdoa_mean = 0.0009521416854750204
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

      