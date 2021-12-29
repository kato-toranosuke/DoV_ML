# ExtraTreesClassifier_RandomUnderSampler_2021-12-29_no2
## Constants
- CSV_PATH = ../out/csv/experiment
- OUTPUT_PATH = ../out/experiment_result/data_of_2021-12-27/AGC-0angle-under3m
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
- AGC_STATUS = ['AGC']

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
	- sampling_strategy_ = OrderedDict([(0, 20)])
	- sample_indices_ = [41  2 42 16 14 95 38  6 61 82 75 28 90 68 24 56 39 72 13  7  0  1 10 11
 22 23 32 33 44 45 54 55 66 67 76 77 88 89 96 97]

- best_estimator
	- base_estimator = ExtraTreeClassifier()
	- n_estimators = 50
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
	- min_samples_split = 10
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
	- oob_decision_function_ = [[0.87243053 0.12756947]
 [0.24227591 0.75772409]
 [0.16653391 0.83346609]
 [0.94130592 0.05869408]
 [0.86971726 0.13028274]
 [0.69109063 0.30890937]
 [0.9796503  0.0203497 ]
 [0.89739011 0.10260989]
 [0.95565476 0.04434524]
 [0.96626984 0.03373016]
 [0.23897071 0.76102929]
 [0.98077731 0.01922269]
 [0.96561355 0.03438645]
 [0.36212797 0.63787203]
 [0.15054544 0.84945456]
 [0.4287012  0.5712988 ]
 [0.9742674  0.0257326 ]
 [0.91837798 0.08162202]
 [0.21175055 0.78824945]
 [0.94619816 0.05380184]
 [0.26505487 0.73494513]
 [0.20670498 0.79329502]
 [0.42205665 0.57794335]
 [0.56451419 0.43548581]
 [0.31695104 0.68304896]
 [0.26514838 0.73485162]
 [0.26084831 0.73915169]
 [0.11536579 0.88463421]
 [0.33908894 0.66091106]
 [0.26007326 0.73992674]
 [0.19348244 0.80651756]
 [0.31641275 0.68358725]
 [0.11358515 0.88641485]
 [0.19424206 0.80575794]
 [0.2902228  0.7097772 ]
 [0.18680625 0.81319375]
 [0.611201   0.388799  ]
 [0.113679   0.886321  ]
 [0.42541464 0.57458536]
 [0.26811393 0.73188607]]
	- oob_score_ = 0.775

#### Importance of features
- gp_max_val_max = 0.18058333401954768
- gp_auc_min = 0.14218361841256788
- gp_auc_max = 0.11067830046590167
- gp_auc_mean = 0.10357822537493283
- gp_max_val_min = 0.09599462547164901
- gp_max_val_mean = 0.08449254647223818
- hlbr = 0.050980008691873094
- coe3[3] = 0.03848068470969235
- coe1[1] = 0.0362406015037594
- srmr = 0.025039134890116395
- diff_std = 0.019075934110084368
- ratio_max_to_9th_ave_peaks = 0.017351398601398605
- ac_std = 0.015862394661074645
- gp_max_val_range = 0.013563565703643525
- gp_max_val_std = 0.012307059668426735
- low_power = 0.009024525170569791
- diff_auc = 0.007396375554270294
- gp_auc_std = 0.007142857142857142
- ratio_max_to_10ms_ave_peaks = 0.006666666666666665
- coe1[0] = 0.006640419947506563
- high_power = 0.00632768361581921
- coe3[2] = 0.0038461538461538446
- ac_auc = 0.0038461538461538446
- gp_auc_range = 0.0013488657265481316
- tdoa_max = 0.0013488657265481316
- coe3[0] = 0.0
- coe3[1] = 0.0
- gp_max_ix_std = 0.0
- gp_max_ix_range = 0.0
- gp_max_ix_min = 0.0
- gp_max_ix_max = 0.0
- gp_max_ix_mean = 0.0
- tdoa_std = 0.0
- tdoa_range = 0.0
- tdoa_min = 0.0
- tdoa_mean = 0.0

## Evaluation
cv = 8
### accuracy
- Scores = [ 0.5789473684210527, 0.631578947368421, 0.9473684210526315, 0.6842105263157895, 0.8947368421052632, 0.6666666666666666, 0.7222222222222222, 0.6666666666666666 ]
- Mean = 0.7240497076023391
- Standard deviation = 0.12082373671928055

### balanced_accuracy
- Scores = [ 0.7333333333333334, 0.675, 0.9666666666666667, 0.8, 0.9333333333333333, 0.7857142857142857, 0.8333333333333333, 0.4 ]
- Mean = 0.765922619047619
- Standard deviation = 0.16494319082762046

### f1
- Scores = [ 0.5, 0.46153846153846156, 0.888888888888889, 0.5714285714285715, 0.8, 0.5714285714285715, 0.5454545454545454, 0.0 ]
- Mean = 0.5423423798423799
- Standard deviation = 0.2476492070781432

### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 82 | 37 |
| Actual Positive | 4 | 26 |

      