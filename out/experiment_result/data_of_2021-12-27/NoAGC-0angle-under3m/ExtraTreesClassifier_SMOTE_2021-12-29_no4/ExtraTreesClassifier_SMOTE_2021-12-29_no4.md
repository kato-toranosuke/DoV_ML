# ExtraTreesClassifier_SMOTE_2021-12-29_no4
## Constants
- CSV_PATH = ../out/csv/experiment
- OUTPUT_PATH = ../out/experiment_result/data_of_2021-12-27/NoAGC-0angle-under3m
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
	- sampling_strategy_ = OrderedDict([(1, 48)])
	- nn_k_ = NearestNeighbors(n_neighbors=6)

- best_estimator
	- base_estimator = ExtraTreeClassifier()
	- n_estimators = 50
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
	- min_samples_leaf = 10
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
- gp_auc_min = 0.2079348403774443
- diff_std = 0.13591852260814866
- diff_auc = 0.12148354968374564
- gp_max_val_min = 0.0741193825749907
- gp_auc_mean = 0.051697140889128995
- gp_max_val_max = 0.050468437270275966
- coe1[1] = 0.04828613218328643
- gp_auc_max = 0.04457929787881679
- high_power = 0.04315894581142671
- gp_max_val_mean = 0.04266311182956981
- coe1[0] = 0.03261049328468295
- srmr = 0.028875617164737837
- gp_max_ix_std = 0.010750352495130108
- gp_max_val_range = 0.010735500009842289
- tdoa_min = 0.009796214833363528
- tdoa_mean = 0.009673324755884751
- hlbr = 0.007992565999340742
- ac_std = 0.00787746093234435
- low_power = 0.0075575717490775915
- gp_max_ix_range = 0.007016044126839498
- tdoa_std = 0.006421379409765658
- gp_max_ix_max = 0.005823424360536734
- gp_max_ix_mean = 0.005452425770437654
- coe3[2] = 0.004922977380961819
- tdoa_range = 0.004838923131677925
- ratio_max_to_10ms_ave_peaks = 0.004552877567062876
- gp_max_ix_min = 0.0033668915563314626
- ac_auc = 0.0029771760023231397
- gp_max_val_std = 0.002836042665861359
- coe3[3] = 0.002259987463166408
- ratio_max_to_9th_ave_peaks = 0.0018366569778381163
- gp_auc_std = 0.0007536189624415321
- gp_auc_range = 0.0007071119977701832
- tdoa_max = 5.6000295747482486e-05
- coe3[0] = 0.0
- coe3[1] = 0.0

## Evaluation
cv = 8
### accuracy
- Scores = [ 0.7333333333333333, 0.9333333333333333, 0.6666666666666666, 1.0, 0.7333333333333333, 0.9333333333333333, 0.8, 0.8571428571428571 ]
- Mean = 0.8321428571428571
- Standard deviation = 0.11023963796102462

### balanced_accuracy
- Scores = [ 0.5833333333333334, 0.8333333333333333, 0.4166666666666667, 1.0, 0.7083333333333333, 0.8333333333333333, 0.75, 0.9090909090909092 ]
- Mean = 0.7542613636363635
- Standard deviation = 0.1739894150817551

### f1
- Scores = [ 0.3333333333333333, 0.8, 0.0, 1.0, 0.5, 0.8, 0.5714285714285715, 0.7499999999999999 ]
- Mean = 0.5943452380952381
- Standard deviation = 0.29668409693311143

### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 84 | 11 |
| Actual Positive | 9 | 15 |

      