# ExtraTreesClassifier_RandomUnderSampler_2021-12-28_no2
## Constants
- CSV_PATH = ../out/csv/experiment
- OUTPUT_PATH = ../out/experiment_result/2021-12-27-3m
- FEATURE_ATTRBS = ['low_power', 'high_power', 'hlbr', 'coe1[0]', 'coe1[1]', 'coe3[0]', 'coe3[1]', 'coe3[2]', 'coe3[3]', 'ratio_max_to_10ms_ave_peaks', 'ratio_max_to_9th_ave_peaks', 'ac_std', 'ac_auc', 'diff_std', 'diff_auc', 'srmr', 'gp_max_val_std', 'gp_max_val_range', 'gp_max_val_min', 'gp_max_val_max', 'gp_max_val_mean', 'gp_max_ix_std', 'gp_max_ix_range', 'gp_max_ix_min', 'gp_max_ix_max', 'gp_max_ix_mean', 'gp_auc_std', 'gp_auc_range', 'gp_auc_min', 'gp_auc_max', 'gp_auc_mean', 'tdoa_std', 'tdoa_range', 'tdoa_min', 'tdoa_max', 'tdoa_mean']
- LABEL_ATTRB = ['facing']
- FACING_DOV_ANGLES = [1]
- NCV = 8
- SCORING = ['accuracy', 'balanced_accuracy', 'f1']
- REFIT_SCORING = balanced_accuracy
- PARAM_GRID = [{'est__n_estimators': [50, 100, 150, 200, 300], 'est__min_samples_split': [2, 5, 10], 'est__min_samples_leaf': [1, 5, 10], 'est__max_features': ['sqrt', 'log2', None], 'est__bootstrap': [False], 'est__n_jobs': [-1], 'est__random_state': [42], 'est__max_samples': [0.01, 0.5, 0.09]}, {'est__n_estimators': [50, 100, 150, 200, 300], 'est__min_samples_split': [2, 5, 10], 'est__min_samples_leaf': [1, 5, 10], 'est__max_features': ['sqrt', 'log2', None], 'est__bootstrap': [True], 'est__oob_score': [True, False], 'est__n_jobs': [-1], 'est__random_state': [42], 'est__max_samples': [0.01, 0.5, 0.09]}]
- TRAIN_SET_SESSION = ['trial1', 'trial2']
- TEST_SET_SESSION = ['trial3', 'trial4', 'trial5']

## Loaded CSV
- 2021-12-27_raspi_48000Hz_w1_N2^12_overlap80_withfacing.csv

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
	- sampling_strategy_ = OrderedDict([(0, 10)])
	- sample_indices_ = [41 44  6 17 38 32  8 33 30 19  0  1 12 13 24 25 36 37 46 47]

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
	- min_samples_split = 5
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
	- oob_decision_function_ = [[0.92353741 0.07646259]
 [0.19782313 0.80217687]
 [0.84367816 0.15632184]
 [0.74709821 0.25290179]
 [0.20208333 0.79791667]
 [0.79727891 0.20272109]
 [0.70246032 0.29753968]
 [0.71666667 0.28333333]
 [0.97095238 0.02904762]
 [0.83222222 0.16777778]
 [0.2459596  0.7540404 ]
 [0.21301587 0.78698413]
 [0.21333333 0.78666667]
 [0.02222222 0.97777778]
 [0.08277778 0.91722222]
 [0.15883257 0.84116743]
 [0.1652381  0.8347619 ]
 [0.07313988 0.92686012]
 [0.296      0.704     ]
 [0.1125     0.8875    ]]
	- oob_score_ = 0.9

#### Importance of features
- gp_max_val_max = 0.15666666666666668
- gp_auc_max = 0.11009157509157509
- coe1[0] = 0.08
- gp_max_val_mean = 0.06813624971519709
- coe3[2] = 0.06375939849624061
- gp_auc_mean = 0.06236430236430237
- gp_auc_min = 0.056240601503759396
- low_power = 0.045396825396825394
- gp_max_val_min = 0.03904761904761905
- diff_auc = 0.0387012987012987
- hlbr = 0.0368421052631579
- high_power = 0.031005291005291005
- ratio_max_to_10ms_ave_peaks = 0.030384615384615385
- tdoa_max = 0.022051282051282053
- srmr = 0.02
- tdoa_std = 0.02
- tdoa_mean = 0.02
- ratio_max_to_9th_ave_peaks = 0.014285714285714285
- gp_max_val_std = 0.013073593073593076
- coe3[3] = 0.011688311688311687
- tdoa_min = 0.010384615384615383
- ac_std = 0.009615384615384616
- gp_max_ix_mean = 0.00857142857142857
- coe1[1] = 0.008518518518518519
- ac_auc = 0.007499999999999999
- gp_auc_range = 0.006666666666666665
- gp_max_ix_std = 0.003333333333333333
- tdoa_range = 0.003333333333333333
- gp_auc_std = 0.002341269841269842
- coe3[0] = 0.0
- coe3[1] = 0.0
- diff_std = 0.0
- gp_max_val_range = 0.0
- gp_max_ix_range = 0.0
- gp_max_ix_min = 0.0
- gp_max_ix_max = 0.0

## Evaluation
cv = 8
### accuracy
- Scores = [ 0.7, 0.7, 0.7777777777777778, 1.0, 0.7777777777777778, 0.6666666666666666, 0.7777777777777778, 0.7777777777777778 ]
- Mean = 0.7722222222222221
- Standard deviation = 0.09590375834240039

### balanced_accuracy
- Scores = [ 0.8125, 0.8125, 0.8571428571428572, 1.0, 0.8571428571428572, 0.6071428571428572, 0.6785714285714286, 0.875 ]
- Mean = 0.8125
- Standard deviation = 0.11355444055336521

### f1
- Scores = [ 0.5714285714285715, 0.5714285714285715, 0.6666666666666666, 1.0, 0.6666666666666666, 0.4, 0.5, 0.5 ]
- Mean = 0.6095238095238095
- Standard deviation = 0.169483007395781

### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 44 | 15 |
| Actual Positive | 2 | 13 |

      