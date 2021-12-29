# ExtraTreesClassifier_ClusterCentroids_2021-12-29_no1
## Constants
- CSV_PATH = ../out/csv/experiment
- OUTPUT_PATH = ../out/experiment_result/data_of_2021-12-27/AGC-45angle-under5m
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
- 2021-12-27_raspi_48000Hz_w1_N2^12_overlap80_new.csv

## Estimator
### Type
- resampler = ClusterCentroids
- estimator = ExtraTreesClassifier

### Arguments for hyperparameter search
- resampler = ClusterCentroids
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
	- estimator = None
	- voting = auto
	- n_jobs = deprecated
	- n_features_in_ = 36
	- sampling_strategy_ = OrderedDict([(1, 70)])
	- estimator_ = KMeans(n_clusters=70, random_state=42)
	- voting_ = soft

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
- diff_auc = 0.14526618599548236
- gp_auc_min = 0.12160777394199351
- diff_std = 0.1121240286264384
- gp_max_val_min = 0.09853054723188656
- gp_max_val_mean = 0.06110350398314184
- gp_auc_max = 0.05131435883731809
- gp_auc_mean = 0.04817891191166368
- coe1[1] = 0.04809342758782181
- high_power = 0.041797816467085934
- coe1[0] = 0.03900845748319274
- srmr = 0.03461866406196028
- hlbr = 0.03287723968905433
- gp_max_val_max = 0.027053817416229156
- low_power = 0.021880161117511954
- ratio_max_to_10ms_ave_peaks = 0.013432175830113349
- coe3[3] = 0.008920957270023953
- ratio_max_to_9th_ave_peaks = 0.008761026916229504
- coe3[2] = 0.008554294790376664
- ac_std = 0.008136558648858861
- gp_max_val_range = 0.0074093248460314854
- ac_auc = 0.007353100135533337
- gp_auc_range = 0.005859712608371034
- gp_max_val_std = 0.005611672493719844
- tdoa_range = 0.005097103353666501
- gp_max_ix_min = 0.0046453923075534115
- gp_max_ix_range = 0.004451994733945579
- gp_max_ix_max = 0.004325688243644901
- gp_auc_std = 0.003906005874269487
- gp_max_ix_std = 0.003892020466306182
- tdoa_max = 0.0036435710259239674
- gp_max_ix_mean = 0.0036134299152160653
- tdoa_min = 0.0033441722176476042
- tdoa_mean = 0.00333029479762399
- tdoa_std = 0.0022566091741636537
- coe3[0] = 0.0
- coe3[1] = 0.0

## Evaluation
cv = 8
### accuracy
- Scores = [ 0.8928571428571429, 0.9285714285714286, 0.8214285714285714, 0.9285714285714286, 0.8928571428571429, 0.9642857142857143, 1.0, 0.9642857142857143 ]
- Mean = 0.9241071428571429
- Standard deviation = 0.05187031267242077

### balanced_accuracy
- Scores = [ 0.8846153846153846, 0.9333333333333333, 0.8179487179487179, 0.9282051282051282, 0.9, 0.9642857142857143, 1.0, 0.9642857142857143 ]
- Mean = 0.9240842490842491
- Standard deviation = 0.05303375969111819

### f1
- Scores = [ 0.9090909090909091, 0.9285714285714286, 0.8387096774193549, 0.9333333333333333, 0.888888888888889, 0.962962962962963, 1.0, 0.962962962962963 ]
- Mean = 0.9280650204037301
- Standard deviation = 0.04679416249656859

### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 100 | 7 |
| Actual Positive | 10 | 107 |

      