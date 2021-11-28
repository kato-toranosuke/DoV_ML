# RandomForestClassifier_SMOTE_2021-11-26_no0
## Constants
- CSV_PATH = ../../out/csv/
- OUTPUT_PATH = ./result/
- FEATURE_ATTRBS = ['low_power', 'high_power', 'hlbr', 'coe1[0]', 'coe1[1]', 'coe3[0]', 'coe3[1]', 'coe3[2]', 'coe3[3]', 'ratio_max_to_10ms_ave_peaks', 'ratio_max_to_9th_ave_peaks', 'ac_std', 'ac_auc', 'diff_std', 'diff_auc', 'srmr', 'gp_max_val_std', 'gp_max_val_range', 'gp_max_val_mean', 'gp_max_ix_std', 'gp_max_ix_range', 'gp_max_ix_mean', 'gp_auc_std', 'gp_auc_range', 'gp_auc_mean', 'tdoa_std', 'tdoa_range', 'tdoa_mean']
- LABEL_ATTRB = ['dov_angle']
- FACING_DOV_ANGLES = [0, 45, 315]
- NCV = 10
- SCORING = ['accuracy', 'balanced_accuracy', 'f1']
- REFIT_SCORING = balanced_accuracy
- PARAM_GRID = [{'est__n_estimators': range(100, 1600, 100), 'est__min_samples_split': [2, 5, 10], 'est__min_samples_leaf': [1, 5, 10], 'est__max_features': ['sqrt', 'log2', None], 'est__bootstrap': [False], 'est__n_jobs': [-1], 'est__random_state': [42], 'est__max_samples': [0.01, 0.5, 0.09]}, {'est__n_estimators': range(100, 1600, 100), 'est__min_samples_split': [2, 5, 10], 'est__min_samples_leaf': [1, 5, 10], 'est__max_features': ['sqrt', 'log2', None], 'est__bootstrap': [True], 'est__oob_score': [True, False], 'est__n_jobs': [-1], 'est__random_state': [42], 'est__max_samples': [0.01, 0.5, 0.09]}]

## Loaded CSV
- features_mono_ch_matlab.csv

## Estimator
### Type
- resampler = SMOTE
- estimator = RandomForestClassifier

### Arguments for hyperparameter search
- resampler = SMOTE
- estimator = RandomForestClassifier
- param_grid = 
	- {'est__n_estimators': range(100, 1600, 100), 'est__min_samples_split': [2, 5, 10], 'est__min_samples_leaf': [1, 5, 10], 'est__max_features': ['sqrt', 'log2', None], 'est__bootstrap': [False], 'est__n_jobs': [-1], 'est__random_state': [42], 'est__max_samples': [0.01, 0.5, 0.09]}
	- {'est__n_estimators': range(100, 1600, 100), 'est__min_samples_split': [2, 5, 10], 'est__min_samples_leaf': [1, 5, 10], 'est__max_features': ['sqrt', 'log2', None], 'est__bootstrap': [True], 'est__oob_score': [True, False], 'est__n_jobs': [-1], 'est__random_state': [42], 'est__max_samples': [0.01, 0.5, 0.09]}

- scoring = ['accuracy', 'balanced_accuracy', 'f1']
- refit = balanced_accuracy
- cv = 10

### Parameters of the best estimator
#### The best hyper-parameters
- best_resampler
	- sampling_strategy = auto
	- random_state = 42
	- k_neighbors = 5
	- n_jobs = -1
	- n_features_in_ = 28
	- sampling_strategy_ = OrderedDict([(1, 1440)])
	- nn_k_ = NearestNeighbors(n_neighbors=6)

- best_estimator
	- base_estimator = DecisionTreeClassifier()
	- n_estimators = 700
	- estimator_params = ('criterion', 'max_depth', 'min_samples_split', 'min_samples_leaf', 'min_weight_fraction_leaf', 'max_features', 'max_leaf_nodes', 'min_impurity_decrease', 'min_impurity_split', 'random_state', 'ccp_alpha')
	- bootstrap = True
	- oob_score = True
	- n_jobs = -1
	- random_state = 42
	- verbose = 0
	- warm_start = False
	- class_weight = None
	- max_samples = 0.5
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
	- n_features_in_ = 28
	- n_features_ = 28
	- n_outputs_ = 1
	- classes_ = [0 1]
	- n_classes_ = 2
	- base_estimator_ = DecisionTreeClassifier()
	- oob_decision_function_ = [[0.00423735 0.99576265]
 [0.         1.        ]
 [0.25041403 0.74958597]
 ...
 [0.02997215 0.97002785]
 [0.06443028 0.93556972]
 [0.08072925 0.91927075]]
	- oob_score_ = 0.8579166666666667

#### Importance of features
- gp_max_val_mean = 0.5273219055434352
- high_power = 0.039068513190784505
- gp_max_val_range = 0.03826390841245342
- gp_auc_mean = 0.03636138252738288
- ac_auc = 0.029137493726054575
- gp_max_val_std = 0.028943989490262275
- diff_auc = 0.02665001075415544
- srmr = 0.024685421202861157
- ratio_max_to_10ms_ave_peaks = 0.02325817556786855
- gp_auc_range = 0.021921973930367343
- ratio_max_to_9th_ave_peaks = 0.021305665421277088
- hlbr = 0.02016208137955669
- tdoa_mean = 0.01900277816875796
- gp_max_ix_mean = 0.01784277828739094
- ac_std = 0.01718884042744024
- diff_std = 0.01711480406133415
- coe1[1] = 0.014310416181680479
- tdoa_std = 0.013627871239890496
- gp_max_ix_std = 0.012781789322894683
- tdoa_range = 0.01129061973899681
- gp_max_ix_range = 0.01027356649036916
- coe3[3] = 0.009434021733384533
- low_power = 0.008365952007654913
- coe3[2] = 0.005799226900983441
- gp_auc_std = 0.005768001668695153
- coe1[0] = 0.0001188126240679372
- coe3[0] = 0.0
- coe3[1] = 0.0

## Evaluation
cv = 10
### accuracy
- Scores = [ 0.7465277777777778, 0.8940972222222222, 0.8541666666666666, 0.8559027777777778, 0.8524305555555556, 0.8020833333333334, 0.8559027777777778, 0.8072916666666666, 0.8663194444444444, 0.7447916666666666 ]
- Mean = 0.827951388888889
- Standard deviation = 0.048309143950961204

### balanced_accuracy
- Scores = [ 0.7777777777777778, 0.8967592592592593, 0.8490740740740741, 0.8180555555555555, 0.8310185185185185, 0.7472222222222222, 0.8652777777777778, 0.7643518518518518, 0.8402777777777778, 0.6699074074074074 ]
- Mean = 0.8059722222222222
- Standard deviation = 0.06329279417852048

### f1
- Scores = [ 0.7276119402985075, 0.8653421633554084, 0.8099547511312217, 0.7762803234501348, 0.791154791154791, 0.6666666666666666, 0.824524312896406, 0.6975476839237057, 0.8050632911392406, 0.5211726384364821 ]
- Mean = 0.7485318562452565
- Standard deviation = 0.09508202794051111

### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 3218 | 382 |
| Actual Positive | 609 | 1551 |

      