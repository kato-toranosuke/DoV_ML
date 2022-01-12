# ExtraTreesClassifier_ClusterCentroids_2022-01-10_no1
## Constants
- CSV_PATH = ../out/csv/experiment
- OUTPUT_PATH = ../out/experiment_result/data_of_2022-01-10/NoAGC-0angle-under3m
- FEATURE_ATTRBS = ['low_power', 'high_power', 'hlbr', 'coe1[0]', 'coe1[1]', 'coe3[0]', 'coe3[1]', 'coe3[2]', 'coe3[3]', 'ratio_max_to_10ms_ave_peaks', 'ratio_max_to_9th_ave_peaks', 'ac_std', 'ac_auc', 'diff_std', 'diff_auc', 'srmr', 'gp_max_val_std', 'gp_max_val_range', 'gp_max_val_min', 'gp_max_val_max', 'gp_max_val_mean', 'gp_max_ix_std', 'gp_max_ix_range', 'gp_max_ix_min', 'gp_max_ix_max', 'gp_max_ix_mean', 'gp_auc_std', 'gp_auc_range', 'gp_auc_min', 'gp_auc_max', 'gp_auc_mean', 'tdoa_std', 'tdoa_range', 'tdoa_min', 'tdoa_max', 'tdoa_mean']
- LABEL_ATTRB = ['facing']
- FACING_DOV_ANGLES = [1]
- NCV = 8
- SCORING = ['accuracy', 'balanced_accuracy', 'f1']
- REFIT_SCORING = balanced_accuracy
- PARAM_GRID = [{'est__n_estimators': [50, 100, 150, 200, 300], 'est__min_samples_split': [2, 5, 10], 'est__min_samples_leaf': [1, 5, 10], 'est__max_features': ['sqrt', 'log2', None], 'est__bootstrap': [False], 'est__n_jobs': [-1], 'est__random_state': [42], 'est__max_samples': [0.01, 0.5, 0.09]}, {'est__n_estimators': [50, 100, 150, 200, 300], 'est__min_samples_split': [2, 5, 10], 'est__min_samples_leaf': [1, 5, 10], 'est__max_features': ['sqrt', 'log2', None], 'est__bootstrap': [True], 'est__oob_score': [True, False], 'est__n_jobs': [-1], 'est__random_state': [42], 'est__max_samples': [0.01, 0.5, 0.09]}]
- TRAIN_SET_SESSION = ['trial1', 'trial2']
- TEST_SET_SESSION = ['trial3', 'trial4', 'trial5']
- DISTANCE = [1, 3]
- AGC_STATUS = ['NoAGC']

## Loaded CSV
- 2022-01-10_raspi_48000Hz_w1_N2^12_overlap80.csv

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
	- sampling_strategy_ = OrderedDict([(0, 20)])
	- estimator_ = KMeans(n_clusters=20, random_state=42)
	- voting_ = soft

- best_estimator
	- base_estimator = ExtraTreeClassifier()
	- n_estimators = 100
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
	- min_samples_leaf = 10
	- min_weight_fraction_leaf = 0.0
	- max_features = None
	- max_leaf_nodes = None
	- min_impurity_decrease = 0.0
	- ccp_alpha = 0.0
	- n_features_in_ = 36
	- n_outputs_ = 1
	- classes_ = [0 1]
	- n_classes_ = 2
	- base_estimator_ = ExtraTreeClassifier()

#### Importance of features
- gp_auc_min = 0.18662970675589632
- gp_max_val_min = 0.16808881875092596
- gp_auc_mean = 0.15150275896124632
- gp_max_val_mean = 0.13969692074384044
- gp_max_val_max = 0.10662927511661016
- gp_auc_max = 0.07903619630840199
- srmr = 0.031991182846721006
- gp_max_ix_max = 0.022116648920527063
- tdoa_max = 0.017231106596346114
- coe3[3] = 0.016027579377680685
- coe3[2] = 0.014490768948893822
- coe1[0] = 0.009131934479200765
- tdoa_range = 0.007933270141922195
- gp_max_ix_std = 0.007222131398868559
- gp_max_ix_min = 0.004785451024936856
- low_power = 0.004757404359007908
- diff_auc = 0.004416666666666665
- coe1[1] = 0.00429908598927495
- tdoa_mean = 0.0032725970310280446
- gp_max_ix_mean = 0.0031610942249240136
- tdoa_min = 0.0029965421732793362
- hlbr = 0.0028994082840236666
- diff_std = 0.002666666666666666
- ac_std = 0.0023922940495911837
- gp_auc_std = 0.0017602823443951367
- ac_auc = 0.0016049382716049382
- ratio_max_to_10ms_ave_peaks = 0.0010718478122337808
- high_power = 0.0007758620689655169
- gp_max_val_std = 0.0007057798431600347
- gp_auc_range = 0.0007057798431600347
- coe3[0] = 0.0
- coe3[1] = 0.0
- ratio_max_to_9th_ave_peaks = 0.0
- gp_max_val_range = 0.0
- gp_max_ix_range = 0.0
- tdoa_std = 0.0

## Evaluation
cv = 8
### accuracy
- Scores = [ 0.5789473684210527, 0.6842105263157895, 0.6842105263157895, 0.6842105263157895, 0.8947368421052632, 0.631578947368421, 0.6111111111111112, 0.8333333333333334 ]
- Mean = 0.7002923976608187
- Standard deviation = 0.1022765054525889

### balanced_accuracy
- Scores = [ 0.7333333333333334, 0.8, 0.8, 0.8, 0.8416666666666667, 0.7666666666666666, 0.7666666666666666, 0.9 ]
- Mean = 0.8010416666666667
- Standard deviation = 0.04795062202701627

### f1
- Scores = [ 0.5, 0.5714285714285715, 0.5714285714285715, 0.5714285714285715, 0.75, 0.5333333333333333, 0.4615384615384615, 0.6666666666666666 ]
- Mean = 0.578228021978022
- Standard deviation = 0.08603583112426601

### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 82 | 38 |
| Actual Positive | 0 | 30 |

      