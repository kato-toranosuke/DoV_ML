# ExtraTreesClassifier_SMOTE_2022-01-09_no4
## Constants
- CSV_PATH = ../out/csv/experiment
- OUTPUT_PATH = ../out/experiment_result/data_of_2022-01-07_new/AGC-45angle-under5m
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
	- sampling_strategy_ = OrderedDict([(0, 6)])
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
	- min_samples_split = 5
	- min_samples_leaf = 1
	- min_weight_fraction_leaf = 0.0
	- max_features = log2
	- max_leaf_nodes = None
	- min_impurity_decrease = 0.0
	- ccp_alpha = 0.0
	- n_features_in_ = 36
	- n_outputs_ = 1
	- classes_ = [0 1]
	- n_classes_ = 2
	- base_estimator_ = ExtraTreeClassifier()

#### Importance of features
- gp_max_val_min = 0.09632872930213567
- gp_max_val_mean = 0.08849540617014691
- gp_auc_min = 0.08454974694499365
- diff_auc = 0.07192802914435846
- gp_auc_mean = 0.07116770459613228
- gp_auc_max = 0.06587685225262022
- gp_max_val_max = 0.05906181768105112
- diff_std = 0.05663295155896906
- high_power = 0.041991549476878554
- srmr = 0.0414165839202811
- coe1[1] = 0.029833791521041368
- hlbr = 0.028665721455642095
- low_power = 0.02565041495235621
- coe1[0] = 0.02080518761071512
- coe3[3] = 0.017963443212804926
- gp_max_ix_range = 0.015905466037139385
- tdoa_min = 0.01558307582752695
- tdoa_std = 0.014340960676073124
- gp_max_ix_min = 0.013193932568665629
- ratio_max_to_10ms_ave_peaks = 0.01289683172937051
- gp_max_ix_mean = 0.012715663342900871
- tdoa_range = 0.012368050756495667
- ac_std = 0.012165363084223712
- tdoa_mean = 0.01108359702566073
- ac_auc = 0.010399290655131625
- gp_auc_range = 0.010234427122236319
- gp_auc_std = 0.010232376379089199
- coe3[2] = 0.009525011731711676
- gp_max_ix_std = 0.009209707627261489
- gp_max_val_std = 0.007329346468104582
- gp_max_val_range = 0.006142537149977136
- ratio_max_to_9th_ave_peaks = 0.005789720798125012
- gp_max_ix_max = 0.0054790739536755215
- tdoa_max = 0.005037637266504159
- coe3[0] = 0.0
- coe3[1] = 0.0

## Evaluation
cv = 8
### accuracy
- Scores = [ 0.896551724137931, 0.9642857142857143, 0.9285714285714286, 0.9642857142857143, 0.8571428571428571, 1.0, 1.0, 1.0 ]
- Mean = 0.9513546798029557
- Standard deviation = 0.04978934731954077

### balanced_accuracy
- Scores = [ 0.8928571428571428, 0.9666666666666667, 0.9333333333333333, 0.9666666666666667, 0.8615384615384616, 1.0, 1.0, 1.0 ]
- Mean = 0.9526327838827839
- Standard deviation = 0.04920445970003251

### f1
- Scores = [ 0.9090909090909091, 0.9655172413793104, 0.9285714285714286, 0.9655172413793104, 0.8571428571428571, 1.0, 1.0, 1.0 ]
- Mean = 0.953229959695477
- Standard deviation = 0.04828728457762175

### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 104 | 4 |
| Actual Positive | 7 | 110 |

      