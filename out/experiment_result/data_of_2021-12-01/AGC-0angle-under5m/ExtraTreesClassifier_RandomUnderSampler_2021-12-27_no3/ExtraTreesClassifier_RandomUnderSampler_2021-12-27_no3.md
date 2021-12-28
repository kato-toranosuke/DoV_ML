# ExtraTreesClassifier_RandomUnderSampler_2021-12-27_no3
## Constants
- CSV_PATH = ../out/csv/experiment
- OUTPUT_PATH = ../out/experiment_result
- FEATURE_ATTRBS = ['low_power', 'high_power', 'hlbr', 'coe1[0]', 'coe1[1]', 'coe3[0]', 'coe3[1]', 'coe3[2]', 'coe3[3]', 'ratio_max_to_10ms_ave_peaks', 'ratio_max_to_9th_ave_peaks', 'ac_std', 'ac_auc', 'diff_std', 'diff_auc', 'srmr', 'gp_max_val_std', 'gp_max_val_range', 'gp_max_val_min', 'gp_max_val_max', 'gp_max_val_mean', 'gp_max_ix_std', 'gp_max_ix_range', 'gp_max_ix_min', 'gp_max_ix_max', 'gp_max_ix_mean', 'gp_auc_std', 'gp_auc_range', 'gp_auc_min', 'gp_auc_max', 'gp_auc_mean', 'tdoa_std', 'tdoa_range', 'tdoa_min', 'tdoa_max', 'tdoa_mean']
- LABEL_ATTRB = ['dov_angle']
- FACING_DOV_ANGLES = [0]
- NCV = 8
- SCORING = ['accuracy', 'balanced_accuracy', 'f1']
- REFIT_SCORING = balanced_accuracy
- PARAM_GRID = [{'est__n_estimators': [50, 100, 150, 200, 300], 'est__min_samples_split': [2, 5, 10], 'est__min_samples_leaf': [1, 5, 10], 'est__max_features': ['sqrt', 'log2', None], 'est__bootstrap': [False], 'est__n_jobs': [-1], 'est__random_state': [42], 'est__max_samples': [0.01, 0.5, 0.09]}, {'est__n_estimators': [50, 100, 150, 200, 300], 'est__min_samples_split': [2, 5, 10], 'est__min_samples_leaf': [1, 5, 10], 'est__max_features': ['sqrt', 'log2', None], 'est__bootstrap': [True], 'est__oob_score': [True, False], 'est__n_jobs': [-1], 'est__random_state': [42], 'est__max_samples': [0.01, 0.5, 0.09]}]
- TRAIN_SET_SESSION = ['trial1']
- TEST_SET_SESSION = ['trial2', 'trial3']

## Loaded CSV
- 2021-12-01_mac_48000Hz_w1_N2^12_overlap80.csv

## Estimator
### Type
- resampler = RandomUnderSampler
- estimator = ExtraTreesClassifier

### Arguments for hyperparameter search
- resampler = RandomUnderSampler
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
	- replacement = False
	- n_features_in_ = 36
	- sampling_strategy_ = OrderedDict([(0, 9)])
	- sample_indices_ = [70 66  1 50  6 42 19 14 29  0  8 16 24 32 40 48 56 64]

- best_estimator
	- base_estimator = ExtraTreeClassifier()
	- n_estimators = 150
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
	- min_samples_split = 5
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
	- oob_decision_function_ = [[0.77516291 0.22483709]
 [0.78588611 0.21411389]
 [0.41221289 0.58778711]
 [0.77633775 0.22366225]
 [0.53092732 0.46907268]
 [0.63784978 0.36215022]
 [0.74620927 0.25379073]
 [0.46233505 0.53766495]
 [0.82868901 0.17131099]
 [0.27714286 0.72285714]
 [0.25481151 0.74518849]
 [0.44488636 0.55511364]
 [0.396567   0.603433  ]
 [0.55617386 0.44382614]
 [0.16532567 0.83467433]
 [0.26388889 0.73611111]
 [0.50102757 0.49897243]
 [0.42673993 0.57326007]]
	- oob_score_ = 0.7777777777777778

#### Importance of features
- gp_auc_std = 0.09270260859402353
- gp_max_val_std = 0.08796799553662
- gp_auc_range = 0.05915670995670996
- gp_auc_min = 0.055828665365410465
- gp_max_val_range = 0.0547550539083558
- gp_max_val_mean = 0.05283904838232629
- gp_max_val_min = 0.05120250162413557
- gp_auc_max = 0.05015696702702182
- gp_max_ix_std = 0.041888436529110805
- gp_max_val_max = 0.03936842105263159
- gp_auc_mean = 0.03086663859893191
- ac_std = 0.030006070016939584
- diff_auc = 0.029842168313866428
- coe3[3] = 0.029531944444444447
- coe1[0] = 0.027695581148411343
- ratio_max_to_9th_ave_peaks = 0.02375136054421769
- low_power = 0.023620071684587816
- tdoa_std = 0.02217560410460113
- ratio_max_to_10ms_ave_peaks = 0.019483333333333335
- coe3[2] = 0.019163998010271306
- gp_max_ix_range = 0.018742857142857144
- tdoa_max = 0.017500000000000005
- high_power = 0.016690476190476193
- coe1[1] = 0.01661117078410312
- gp_max_ix_max = 0.014235488045147935
- diff_std = 0.012825396825396828
- tdoa_mean = 0.011289115646258504
- gp_max_ix_min = 0.010833333333333335
- hlbr = 0.01004761904761905
- srmr = 0.00804761904761905
- tdoa_range = 0.007861751152073737
- tdoa_min = 0.005714285714285714
- ac_auc = 0.005297619047619049
- gp_max_ix_mean = 0.00230008984725966
- coe3[0] = 0.0
- coe3[1] = 0.0

## Evaluation
cv = 8
### accuracy
- Scores = [ 0.8888888888888888, 0.8333333333333334, 0.8888888888888888, 0.8888888888888888, 0.8888888888888888, 0.8888888888888888, 0.8888888888888888, 0.8888888888888888 ]
- Mean = 0.8819444444444444
- Standard deviation = 0.018373272993504074

### balanced_accuracy
- Scores = [ 0.6666666666666666, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5 ]
- Mean = 0.5208333333333333
- Standard deviation = 0.05511981898051229

### f1
- Scores = [ 0.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0 ]
- Mean = 0.0625
- Standard deviation = 0.16535945694153692

### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 126 | 0 |
| Actual Positive | 17 | 1 |

      