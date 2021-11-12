# RandomForestClassifier_RandomOverSampler_2021-11-12_no1
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
- resampler = RandomOverSampler
- estimator = RandomForestClassifier

### Arguments for hyperparameter search
- resampler = RandomOverSampler
- estimator = RandomForestClassifier
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
	- shrinkage = None
	- n_features_in_ = 36
	- sampling_strategy_ = OrderedDict([(1, 1440)])
	- shrinkage_ = None
	- sample_indices_ = [   0    1    2 ... 1375 3697 2545]

- best_estimator
	- base_estimator = DecisionTreeClassifier()
	- n_estimators = 1000
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
	- base_estimator_ = DecisionTreeClassifier()

#### Importance of features
- gp_max_val_mean = 0.1515999830611088
- gp_max_val_max = 0.12388359441306543
- gp_auc_max = 0.0707569126825647
- gp_max_val_min = 0.05478463654242173
- high_power = 0.052268357548177054
- gp_max_val_range = 0.04722087268335439
- gp_max_val_std = 0.03706625268223896
- hlbr = 0.03142999001282597
- tdoa_mean = 0.031268330134641406
- gp_max_ix_mean = 0.031028429680910907
- gp_max_ix_std = 0.029450557917669297
- diff_std = 0.02932002665507664
- gp_auc_mean = 0.022472239052365894
- ac_auc = 0.0212598880185318
- srmr = 0.021159441392305023
- diff_auc = 0.021113853901515826
- tdoa_std = 0.020479493194947927
- coe1[1] = 0.01764763429040001
- ratio_max_to_10ms_ave_peaks = 0.016411552938140537
- ac_std = 0.016303153509296998
- gp_max_ix_min = 0.015919598026206107
- tdoa_min = 0.015548687118848888
- low_power = 0.01493310678699776
- ratio_max_to_9th_ave_peaks = 0.014106488141450334
- gp_auc_min = 0.013424448069759556
- tdoa_max = 0.013235949568924406
- gp_max_ix_max = 0.013221204740784635
- coe3[3] = 0.01311517132464327
- tdoa_range = 0.0116977992920121
- gp_max_ix_range = 0.011522793618510854
- coe3[2] = 0.008594708682623454
- gp_auc_range = 0.005638271822434837
- gp_auc_std = 0.0016424543331264455
- coe1[0] = 0.00047411816211794666
- coe3[0] = 0.0
- coe3[1] = 0.0

## Evaluation
cv = 10
### accuracy
- Scores = [ 0.7690972222222222, 0.8802083333333334, 0.8871527777777778, 0.8472222222222222, 0.8663194444444444, 0.8072916666666666, 0.84375, 0.8194444444444444, 0.8836805555555556, 0.7690972222222222 ]
- Mean = 0.8373263888888888
- Standard deviation = 0.04240555785278101

### balanced_accuracy
- Scores = [ 0.8069444444444445, 0.8745370370370371, 0.8763888888888889, 0.8157407407407407, 0.8458333333333333, 0.7625, 0.8555555555555556, 0.7907407407407407, 0.8671296296296296, 0.6986111111111111 ]
- Mean = 0.8193981481481482
- Standard deviation = 0.054211935025204154

### f1
- Scores = [ 0.7568555758683729, 0.8421052631578948, 0.8470588235294118, 0.7720207253886009, 0.8108108108108107, 0.6942148760330579, 0.8125, 0.7373737373737375, 0.8377723970944311, 0.5750798722044728 ]
- Mean = 0.7685792081460792
- Standard deviation = 0.0801002423936165

### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 3208 | 392 |
| Actual Positive | 545 | 1615 |

      