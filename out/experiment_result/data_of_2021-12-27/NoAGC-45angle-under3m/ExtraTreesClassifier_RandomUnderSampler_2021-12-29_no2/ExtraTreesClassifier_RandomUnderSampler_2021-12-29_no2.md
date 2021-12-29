# ExtraTreesClassifier_RandomUnderSampler_2021-12-29_no2
## Constants
- CSV_PATH = ../out/csv/experiment
- OUTPUT_PATH = ../out/experiment_result/data_of_2021-12-27/NoAGC-45angle-under3m
- FEATURE_ATTRBS = ['low_power', 'high_power', 'hlbr', 'coe1[0]', 'coe1[1]', 'coe3[0]', 'coe3[1]', 'coe3[2]', 'coe3[3]', 'ratio_max_to_10ms_ave_peaks', 'ratio_max_to_9th_ave_peaks', 'ac_std', 'ac_auc', 'diff_std', 'diff_auc', 'srmr', 'gp_max_val_std', 'gp_max_val_range', 'gp_max_val_min', 'gp_max_val_max', 'gp_max_val_mean', 'gp_max_ix_std', 'gp_max_ix_range', 'gp_max_ix_min', 'gp_max_ix_max', 'gp_max_ix_mean', 'gp_auc_std', 'gp_auc_range', 'gp_auc_min', 'gp_auc_max', 'gp_auc_mean', 'tdoa_std', 'tdoa_range', 'tdoa_min', 'tdoa_max', 'tdoa_mean']
- LABEL_ATTRB = ['facing2']
- FACING_DOV_ANGLES = [1, 2]
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
	- sampling_strategy_ = OrderedDict([(1, 36)])
	- sample_indices_ = [ 4  5  6  7  8  9 14 15 16 17 18 19 26 27 28 29 36 37 38 39 40 41 48 49
 50 51 58 59 60 61 62 63 70 71 72 73 69 46 47 68 66 76 10 24 20  3 12 53
 57 35 33 25 77 31 21 32 56 52  0 55 78 11 23 64  1 75 43  2 65 45 67 22]

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
	- min_samples_leaf = 1
	- min_weight_fraction_leaf = 0.0
	- max_features = log2
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
- gp_auc_min = 0.10388543610550086
- diff_auc = 0.07978260223635225
- srmr = 0.07574195658874652
- gp_auc_mean = 0.07300895933108714
- gp_max_val_mean = 0.07277219033741864
- gp_auc_max = 0.07189359386653207
- gp_max_val_max = 0.0693770479933392
- gp_max_val_min = 0.06763508842007067
- diff_std = 0.04004432481116197
- ratio_max_to_10ms_ave_peaks = 0.03874474529194719
- hlbr = 0.031070364562420853
- high_power = 0.030929851052613203
- tdoa_mean = 0.026332178162527694
- coe1[1] = 0.023917729400346772
- tdoa_std = 0.019987564771464503
- gp_max_ix_std = 0.015859167261128047
- coe3[3] = 0.015642997370574774
- coe1[0] = 0.014943003865259994
- low_power = 0.014900493095310106
- tdoa_range = 0.012141975308641974
- gp_max_ix_mean = 0.012079043074550138
- gp_max_ix_range = 0.010737576524496036
- coe3[2] = 0.010099128635722838
- gp_max_val_std = 0.00865294772514353
- gp_auc_range = 0.008026487696410331
- tdoa_min = 0.0076476127817123995
- gp_max_ix_max = 0.006216817004778289
- gp_max_ix_min = 0.005970438693971665
- tdoa_max = 0.0059395150608918725
- gp_auc_std = 0.005628526721147982
- gp_max_val_range = 0.005584599496364201
- ratio_max_to_9th_ave_peaks = 0.005490283862832881
- ac_auc = 0.004919147951261784
- ac_std = 0.004396604938271602
- coe3[0] = 0.0
- coe3[1] = 0.0

## Evaluation
cv = 8
### accuracy
- Scores = [ 0.8666666666666667, 1.0, 0.8666666666666667, 1.0, 1.0, 1.0, 1.0, 1.0 ]
- Mean = 0.9666666666666667
- Standard deviation = 0.05773502691896256

### balanced_accuracy
- Scores = [ 0.8333333333333333, 1.0, 0.875, 1.0, 1.0, 1.0, 1.0, 1.0 ]
- Mean = 0.9635416666666666
- Standard deviation = 0.06400107149710683

### f1
- Scores = [ 0.9, 1.0, 0.8571428571428571, 1.0, 1.0, 1.0, 1.0, 1.0 ]
- Mean = 0.9696428571428571
- Standard deviation = 0.053660640004702574

### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 52 | 2 |
| Actual Positive | 2 | 63 |

      