# ExtraTreesClassifier_NoResampler_2021-12-29_no0
## Constants
- CSV_PATH = ../out/csv/experiment
- OUTPUT_PATH = ../out/experiment_result/data_of_2021-12-27/NoAGC-0angle-5m
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
	- min_samples_split = 10
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
- gp_max_val_max = 0.12978509046701805
- gp_auc_max = 0.12747379491900512
- high_power = 0.09874407124347061
- hlbr = 0.09509608602511238
- gp_max_val_min = 0.08199530855451456
- gp_auc_min = 0.07574623884202529
- gp_auc_mean = 0.06464256305500057
- gp_max_val_mean = 0.05317454699613209
- diff_std = 0.033302112609275104
- gp_max_val_std = 0.029892215189511573
- srmr = 0.028945218513217963
- gp_auc_range = 0.025224440476857533
- gp_auc_std = 0.023205830986609416
- diff_auc = 0.01733211241741881
- coe3[2] = 0.016498928547603788
- coe1[1] = 0.013903294324002809
- gp_max_val_range = 0.010617970089761427
- ac_std = 0.00987657633508195
- ratio_max_to_9th_ave_peaks = 0.00958703229140138
- coe3[3] = 0.00926878677817608
- tdoa_mean = 0.007239014736254601
- coe1[0] = 0.006010476750679455
- gp_max_ix_mean = 0.005343249017122702
- low_power = 0.0052830547272675835
- gp_max_ix_std = 0.0033650588802774835
- gp_max_ix_max = 0.003121191320817999
- ratio_max_to_10ms_ave_peaks = 0.0029377171719506046
- tdoa_std = 0.0026158467070310975
- ac_auc = 0.00253801201927209
- tdoa_range = 0.0025277453271028046
- gp_max_ix_range = 0.0019158184112418742
- tdoa_min = 0.0014335175162160996
- tdoa_max = 0.0012856820556663793
- gp_max_ix_min = 7.13966979027222e-05
- coe3[0] = 0.0
- coe3[1] = 0.0

## Evaluation
cv = 8
### accuracy
- Scores = [ 0.75, 1.0, 1.0, 0.875, 1.0, 1.0, 1.0, 1.0 ]
- Mean = 0.953125
- Standard deviation = 0.08699631816921909

### balanced_accuracy
- Scores = [ 0.6666666666666667, 1.0, 1.0, 0.75, 1.0, 1.0, 1.0, 1.0 ]
- Mean = 0.9270833333333334
- Standard deviation = 0.12800214299421359

### f1
- Scores = [ 0.5, 1.0, 1.0, 0.6666666666666666, 1.0, 1.0, 1.0, 1.0 ]
- Mean = 0.8958333333333333
- Standard deviation = 0.1851707170274081

### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 47 | 1 |
| Actual Positive | 2 | 10 |

      