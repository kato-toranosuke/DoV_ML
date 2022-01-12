# ExtraTreesClassifier_SMOTEENN_2022-01-10_no5
## Constants
- CSV_PATH = ../out/csv/experiment
- OUTPUT_PATH = ../out/experiment_result/data_of_2022-01-10/NoAGC-0angle-5m
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
- AGC_STATUS = ['NoAGC']

## Loaded CSV
- 2022-01-10_raspi_48000Hz_w1_N2^12_overlap80.csv

## Estimator
### Type
- resampler = SMOTEENN
- estimator = ExtraTreesClassifier

### Arguments for hyperparameter search
- resampler = SMOTEENN
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
	- smote = None
	- enn = None
	- n_jobs = -1
	- n_features_in_ = 36
	- sampling_strategy_ = auto
	- smote_ = SMOTE(n_jobs=-1, random_state=42)
	- enn_ = EditedNearestNeighbours(n_jobs=-1, sampling_strategy='all')

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
- gp_max_val_max = 0.14620851955720868
- gp_auc_max = 0.14545539959442338
- gp_auc_min = 0.13454590568747624
- gp_max_val_mean = 0.11867931478845418
- gp_max_val_min = 0.0894618926926046
- hlbr = 0.06951414114316637
- srmr = 0.04587721377746628
- gp_auc_std = 0.03913458693295866
- gp_auc_mean = 0.03650674872890137
- gp_max_val_range = 0.030877804969469857
- coe3[3] = 0.023667271798287128
- gp_max_ix_mean = 0.0212501245619804
- gp_max_ix_range = 0.020512146522330868
- gp_max_val_std = 0.016695062488133582
- diff_std = 0.008090008993684507
- ac_auc = 0.007641206589720912
- coe3[2] = 0.006824874166415873
- tdoa_range = 0.006085951581905644
- gp_max_ix_min = 0.005226362401247927
- gp_max_ix_max = 0.004365314841706731
- ac_std = 0.003969181091540963
- tdoa_std = 0.0037642669007901656
- coe1[1] = 0.003315088188721764
- tdoa_max = 0.0026583777153468074
- ratio_max_to_9th_ave_peaks = 0.002104565970776538
- high_power = 0.001994438109781619
- low_power = 0.00159965510092668
- gp_auc_range = 0.0015639589169000926
- tdoa_min = 0.0012102812154269674
- diff_auc = 0.0006376008818557011
- ratio_max_to_10ms_ave_peaks = 0.00034224562363238345
- coe1[0] = 0.0002204884667571242
- coe3[0] = 0.0
- coe3[1] = 0.0
- gp_max_ix_std = 0.0
- tdoa_mean = 0.0

## Evaluation
cv = 8
### accuracy
- Scores = [ 0.7, 0.8, 0.8, 0.7777777777777778, 0.6666666666666666, 0.7777777777777778, 0.6666666666666666, 1.0 ]
- Mean = 0.773611111111111
- Standard deviation = 0.10060580389708032

### balanced_accuracy
- Scores = [ 0.8125, 0.6875, 0.5, 0.5, 0.42857142857142855, 0.5, 0.7857142857142857, 1.0 ]
- Mean = 0.6517857142857143
- Standard deviation = 0.1888239819871125

### f1
- Scores = [ 0.5714285714285715, 0.5, 0.0, 0.0, 0.0, 0.0, 0.5714285714285715, 1.0 ]
- Mean = 0.3303571428571429
- Standard deviation = 0.35881305888232357

### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 54 | 6 |
| Actual Positive | 4 | 11 |

      