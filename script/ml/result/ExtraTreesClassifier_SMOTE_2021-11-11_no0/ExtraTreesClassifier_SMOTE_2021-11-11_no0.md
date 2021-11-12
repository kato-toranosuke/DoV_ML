# ExtraTreesClassifier_SMOTE_2021-11-11_no0
## Constants
- CSV_PATH = ../../out/csv/
- OUTPUT_PATH = ./result/
- FEATURE_ATTRBS = ['low_power', 'high_power', 'hlbr', 'coe1[0]', 'coe1[1]', 'coe3[0]', 'coe3[1]', 'coe3[2]', 'coe3[3]', 'ratio_max_to_10ms_ave_peaks', 'ratio_max_to_9th_ave_peaks', 'ac_std', 'ac_auc', 'diff_std', 'diff_auc', 'srmr', 'gp_max_val_std', 'gp_max_val_range', 'gp_max_val_min', 'gp_max_val_max', 'gp_max_val_mean', 'gp_max_ix_std', 'gp_max_ix_range', 'gp_max_ix_min', 'gp_max_ix_max', 'gp_max_ix_mean', 'gp_auc_std', 'gp_auc_range', 'gp_auc_min', 'gp_auc_max', 'gp_auc_mean', 'tdoa_std', 'tdoa_range', 'tdoa_min', 'tdoa_max', 'tdoa_mean']
- LABEL_ATTRB = ['dov_angle']
- FACING_DOV_ANGLES = [0, 45, 315]
- NCV = 10
- SCORING = ['accuracy', 'balanced_accuracy', 'f1']
- REFIT_SCORING = balanced_accuracy
- PARAM_GRID = [{'est__n_estimators': [10, 100, 500, 800, 1000], 'est__min_samples_split': [2, 5, 10], 'est__min_samples_leaf': [1, 5, 10], 'est__max_features': ['sqrt', 'log2', None], 'est__bootstrap': [False], 'est__n_jobs': [-1], 'est__random_state': [42], 'est__max_samples': [0.01, 0.5, 0.09]}, {'est__n_estimators': [10, 100, 500, 800, 1000], 'est__min_samples_split': [2, 5, 10], 'est__min_samples_leaf': [1, 5, 10], 'est__max_features': ['sqrt', 'log2', None], 'est__bootstrap': [True], 'est__oob_score': [True, False], 'est__n_jobs': [-1], 'est__random_state': [42], 'est__max_samples': [0.01, 0.5, 0.09]}]

## Loaded CSV
- features_mono_ch_python.csv

## Estimator
### Type
- resampler = SMOTE
- estimator = ExtraTreesClassifier

### Arguments for hyperparameter search
- resampler = SMOTE
- estimator = ExtraTreesClassifier
- param_grid = 
	- {'est__n_estimators': [10, 100, 500, 800, 1000], 'est__min_samples_split': [2, 5, 10], 'est__min_samples_leaf': [1, 5, 10], 'est__max_features': ['sqrt', 'log2', None], 'est__bootstrap': [False], 'est__n_jobs': [-1], 'est__random_state': [42], 'est__max_samples': [0.01, 0.5, 0.09]}
	- {'est__n_estimators': [10, 100, 500, 800, 1000], 'est__min_samples_split': [2, 5, 10], 'est__min_samples_leaf': [1, 5, 10], 'est__max_features': ['sqrt', 'log2', None], 'est__bootstrap': [True], 'est__oob_score': [True, False], 'est__n_jobs': [-1], 'est__random_state': [42], 'est__max_samples': [0.01, 0.5, 0.09]}

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
	- n_features_in_ = 36
	- sampling_strategy_ = OrderedDict([(1, 1440)])
	- nn_k_ = NearestNeighbors(n_neighbors=6)

- best_estimator
	- base_estimator = ExtraTreeClassifier()
	- n_estimators = 500
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
- gp_max_val_max = 0.11653752684150026
- gp_auc_max = 0.11249210639260208
- gp_auc_mean = 0.1122951414497822
- gp_max_val_mean = 0.1102519860359914
- gp_max_val_min = 0.036497275321561
- gp_auc_min = 0.032442133946893284
- gp_max_ix_min = 0.023366816538911993
- tdoa_min = 0.023211711714478136
- gp_max_ix_mean = 0.022658435151089704
- gp_auc_range = 0.02224370453361306
- tdoa_mean = 0.022198300069656975
- gp_max_val_range = 0.020964773023223165
- gp_max_ix_std = 0.020244695365705487
- gp_max_val_std = 0.019890688332523266
- tdoa_std = 0.019485919205673802
- diff_auc = 0.018500313597159913
- ac_auc = 0.01822931810128553
- ratio_max_to_10ms_ave_peaks = 0.017990098633430287
- gp_max_ix_max = 0.017982462995015085
- srmr = 0.01796821821236611
- tdoa_max = 0.01796164675400042
- high_power = 0.017844361989110137
- gp_auc_std = 0.017412419028383225
- gp_max_ix_range = 0.016840316059652312
- ratio_max_to_9th_ave_peaks = 0.01648135102697544
- tdoa_range = 0.016408043960180637
- diff_std = 0.01578161293037033
- hlbr = 0.015523174518438964
- ac_std = 0.011666256104580055
- coe3[2] = 0.010437973809843364
- coe1[0] = 0.009970667824781837
- coe1[1] = 0.009945909501426068
- coe3[3] = 0.009353660893013677
- low_power = 0.008920980136780709
- coe3[0] = 0.0
- coe3[1] = 0.0

## Evaluation
cv = 10
### accuracy
- Scores = [ 0.7829861111111112, 0.8819444444444444, 0.8802083333333334, 0.8697916666666666, 0.8645833333333334, 0.8055555555555556, 0.8454861111111112, 0.8246527777777778, 0.8871527777777778, 0.7708333333333334 ]
- Mean = 0.8413194444444445
- Standard deviation = 0.04069468145551002

### balanced_accuracy
- Scores = [ 0.813425925925926, 0.874074074074074, 0.8745370370370371, 0.8412037037037037, 0.8444444444444444, 0.7675925925925926, 0.8578703703703704, 0.7921296296296296, 0.8745370370370371, 0.7037037037037037 ]
- Mean = 0.8243518518518519
- Standard deviation = 0.05315621309308824

### f1
- Scores = [ 0.7637051039697542, 0.8425925925925926, 0.8421052631578948, 0.8071979434447302, 0.8088235294117647, 0.7037037037037038, 0.814968814968815, 0.7390180878552973, 0.8456057007125891, 0.5875 ]
- Mean = 0.7755220739817142
- Standard deviation = 0.07713251175413176

### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 3212 | 388 |
| Actual Positive | 526 | 1634 |

      