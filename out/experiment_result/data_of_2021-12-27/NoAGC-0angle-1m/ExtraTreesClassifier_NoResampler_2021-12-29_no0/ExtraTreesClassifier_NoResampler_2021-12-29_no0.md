# ExtraTreesClassifier_NoResampler_2021-12-29_no0
## Constants
- CSV_PATH = ../out/csv/experiment
- OUTPUT_PATH = ../out/experiment_result/data_of_2021-12-27/NoAGC-0angle-1m
- FEATURE_ATTRBS = ['low_power', 'high_power', 'hlbr', 'coe1[0]', 'coe1[1]', 'coe3[0]', 'coe3[1]', 'coe3[2]', 'coe3[3]', 'ratio_max_to_10ms_ave_peaks', 'ratio_max_to_9th_ave_peaks', 'ac_std', 'ac_auc', 'diff_std', 'diff_auc', 'srmr', 'gp_max_val_std', 'gp_max_val_range', 'gp_max_val_min', 'gp_max_val_max', 'gp_max_val_mean', 'gp_max_ix_std', 'gp_max_ix_range', 'gp_max_ix_min', 'gp_max_ix_max', 'gp_max_ix_mean', 'gp_auc_std', 'gp_auc_range', 'gp_auc_min', 'gp_auc_max', 'gp_auc_mean', 'tdoa_std', 'tdoa_range', 'tdoa_min', 'tdoa_max', 'tdoa_mean']
- LABEL_ATTRB = ['facing']
- FACING_DOV_ANGLES = [1]
- NCV = 8
- SCORING = ['accuracy', 'balanced_accuracy', 'f1']
- REFIT_SCORING = balanced_accuracy
- PARAM_GRID = [{'est__n_estimators': [50, 100, 150, 200, 300], 'est__min_samples_split': [2, 5, 10], 'est__min_samples_leaf': [1, 5, 10], 'est__max_features': ['sqrt', 'log2', None], 'est__bootstrap': [False], 'est__n_jobs': [-1], 'est__random_state': [42], 'est__max_samples': [0.01, 0.5, 0.09]}, {'est__n_estimators': [50, 100, 150, 200, 300], 'est__min_samples_split': [2, 5, 10], 'est__min_samples_leaf': [1, 5, 10], 'est__max_features': ['sqrt', 'log2', None], 'est__bootstrap': [True], 'est__oob_score': [True, False], 'est__n_jobs': [-1], 'est__random_state': [42], 'est__max_samples': [0.01, 0.5, 0.09]}]
- TRAIN_SET_SESSION = ['trial1', 'trial2']
- TEST_SET_SESSION = ['trial3', 'trial4', 'trial5']
- DISTANCE = [1]
- AGC_STATUS = ['NoAGC']

## Loaded CSV
- 2021-12-27_raspi_48000Hz_w1_N2^12_overlap80_new.csv

## Estimator
### Type
- resampler = NoResampler
- estimator = ExtraTreesClassifier

### Arguments for hyperparameter search
- resampler = NoResampler
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

#### Importance of features
- gp_auc_max = 0.06714811177137339
- gp_max_val_min = 0.06552783255393829
- gp_max_val_max = 0.06388091673902227
- low_power = 0.06268266332710186
- hlbr = 0.06038898043867471
- diff_auc = 0.059909359836861534
- gp_auc_min = 0.059450076485384064
- high_power = 0.0548279431375555
- srmr = 0.051282002106384755
- coe1[1] = 0.05046734644114952
- gp_max_val_mean = 0.039855603844411454
- gp_auc_mean = 0.036347513804040214
- coe1[0] = 0.03548282768335107
- diff_std = 0.029260972687324784
- gp_auc_std = 0.022198599061647995
- tdoa_mean = 0.021206511173697654
- coe3[2] = 0.020115764366865796
- ac_std = 0.019792742556038804
- ac_auc = 0.018950798366925637
- ratio_max_to_9th_ave_peaks = 0.017721100258237022
- gp_max_val_std = 0.016673327015996595
- gp_max_ix_mean = 0.016520589370752403
- gp_max_ix_range = 0.014260612517289484
- tdoa_range = 0.013560364453303102
- gp_auc_range = 0.012760833914204612
- coe3[3] = 0.012362837468063626
- gp_max_ix_std = 0.010459759554617434
- tdoa_std = 0.010101349086070749
- ratio_max_to_10ms_ave_peaks = 0.00970442708684684
- gp_max_ix_max = 0.008910547952075278
- gp_max_val_range = 0.0069454634197685505
- tdoa_max = 0.005341128780024087
- gp_max_ix_min = 0.0032196535378225936
- tdoa_min = 0.0026814392031783312
- coe3[0] = 0.0
- coe3[1] = 0.0

## Evaluation
cv = 8
### accuracy
- Scores = [ 0.75, 0.875, 0.875, 0.7142857142857143, 0.8571428571428571, 0.7142857142857143, 0.8571428571428571, 0.7142857142857143 ]
- Mean = 0.7946428571428572
- Standard deviation = 0.07253605718424963

### balanced_accuracy
- Scores = [ 0.5, 0.75, 0.9166666666666667, 0.5, 0.5, 0.4166666666666667, 0.5, 0.8333333333333333 ]
- Mean = 0.6145833333333334
- Standard deviation = 0.17646952443851474

### f1
- Scores = [ 0.0, 0.6666666666666666, 0.8, 0.0, 0.0, 0.0, 0.0, 0.5 ]
- Mean = 0.24583333333333335
- Standard deviation = 0.3261464820870797

### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 43 | 4 |
| Actual Positive | 8 | 4 |

      