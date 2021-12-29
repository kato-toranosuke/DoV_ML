# ExtraTreesClassifier_NoResampler_2021-12-29_no0
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
	- n_estimators = 100
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

#### Importance of features
- gp_max_val_min = 0.10981845177147045
- gp_max_val_mean = 0.10613232301014563
- gp_auc_min = 0.09176794358118462
- gp_auc_max = 0.08305266213864097
- gp_max_val_max = 0.07916633651036695
- gp_auc_mean = 0.07840781800215156
- diff_auc = 0.056259984756178674
- diff_std = 0.045527727625840994
- ratio_max_to_10ms_ave_peaks = 0.04267147868364307
- srmr = 0.03400389625710375
- high_power = 0.029547677720996375
- hlbr = 0.0277749493948122
- gp_max_ix_mean = 0.020723919945244928
- tdoa_std = 0.017192768765164384
- coe1[1] = 0.016458581453433218
- gp_auc_std = 0.01641475170780427
- tdoa_mean = 0.01571789767797639
- coe1[0] = 0.014959083764116251
- coe3[3] = 0.013277379304981159
- gp_max_ix_std = 0.013260333025281056
- gp_max_val_std = 0.011410372610552626
- tdoa_range = 0.009944084744643334
- gp_auc_range = 0.009287273449732887
- gp_max_val_range = 0.007304156258808728
- gp_max_ix_min = 0.0072422268547999505
- low_power = 0.007217697094761078
- gp_max_ix_range = 0.006928873521053054
- tdoa_min = 0.0058663927102039545
- tdoa_max = 0.00578009267480724
- gp_max_ix_max = 0.004831676594499317
- ac_auc = 0.004054143589716712
- ac_std = 0.00287825801594655
- ratio_max_to_9th_ave_peaks = 0.002717919182535137
- coe3[2] = 0.0024008676014023603
- coe3[0] = 0.0
- coe3[1] = 0.0

## Evaluation
cv = 8
### accuracy
- Scores = [ 0.8666666666666667, 1.0, 0.8666666666666667, 0.9333333333333333, 1.0, 1.0, 1.0, 1.0 ]
- Mean = 0.9583333333333334
- Standard deviation = 0.05713045500334202

### balanced_accuracy
- Scores = [ 0.8333333333333333, 1.0, 0.875, 0.9285714285714286, 1.0, 1.0, 1.0, 1.0 ]
- Mean = 0.9546130952380952
- Standard deviation = 0.06327030267350416

### f1
- Scores = [ 0.9, 1.0, 0.8571428571428571, 0.9411764705882353, 1.0, 1.0, 1.0, 1.0 ]
- Mean = 0.9622899159663865
- Standard deviation = 0.05302354120480989

### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 51 | 3 |
| Actual Positive | 2 | 63 |

      