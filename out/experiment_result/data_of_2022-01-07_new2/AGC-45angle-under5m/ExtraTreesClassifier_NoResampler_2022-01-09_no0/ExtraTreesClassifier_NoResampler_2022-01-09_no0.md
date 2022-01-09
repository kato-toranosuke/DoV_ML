# ExtraTreesClassifier_NoResampler_2022-01-09_no0
## Constants
- CSV_PATH = ../out/csv/experiment
- OUTPUT_PATH = ../out/experiment_result/data_of_2022-01-07_new2/AGC-45angle-under5m
- FEATURE_ATTRBS = ['low_power', 'high_power', 'hlbr', 'coe1[0]', 'coe1[1]', 'coe3[0]', 'coe3[1]', 'coe3[2]', 'coe3[3]', 'ratio_max_to_10ms_ave_peaks', 'ratio_max_to_9th_ave_peaks', 'ac_std', 'ac_auc', 'diff_std', 'diff_auc', 'srmr', 'gp_max_val_std', 'gp_max_val_range', 'gp_max_val_min', 'gp_max_val_max', 'gp_max_val_mean', 'gp_max_ix_std', 'gp_max_ix_range', 'gp_max_ix_min', 'gp_max_ix_max', 'gp_max_ix_mean', 'gp_auc_std', 'gp_auc_range', 'gp_auc_min', 'gp_auc_max', 'gp_auc_mean', 'tdoa_std', 'tdoa_range', 'tdoa_min', 'tdoa_max', 'tdoa_mean']
- LABEL_ATTRB = ['facing2']
- FACING_DOV_ANGLES = [1, 2]
- NCV = 8
- SCORING = ['accuracy', 'balanced_accuracy', 'f1']
- REFIT_SCORING = balanced_accuracy
- PARAM_GRID = [{'est__n_estimators': range(10, 1000, 25), 'est__min_samples_split': [2, 5, 10], 'est__min_samples_leaf': [1, 5, 10], 'est__max_features': ['sqrt', 'log2', None], 'est__bootstrap': [False], 'est__n_jobs': [-1], 'est__random_state': [42], 'est__max_samples': [0.01, 0.5, 0.09]}]
- TRAIN_SET_SESSION = ['trial1', 'trial2']
- TEST_SET_SESSION = ['trial3', 'trial4', 'trial5']
- DISTANCE = [1, 3, 5]
- AGC_STATUS = ['AGC']

## Loaded CSV
- 2021-12-27_raspi_48000Hz_w1_N2^12_overlap80_with2022-01-07.csv

## Estimator
### Type
- resampler = NoResampler
- estimator = ExtraTreesClassifier

### Arguments for hyperparameter search
- resampler = NoResampler
- estimator = ExtraTreesClassifier
- param_grid = 
	- {'est__n_estimators': range(10, 1000, 25), 'est__min_samples_split': [2, 5, 10], 'est__min_samples_leaf': [1, 5, 10], 'est__max_features': ['sqrt', 'log2', None], 'est__bootstrap': [False], 'est__n_jobs': [-1], 'est__random_state': [42], 'est__max_samples': [0.01, 0.5, 0.09]}

- scoring = ['accuracy', 'balanced_accuracy', 'f1']
- refit = balanced_accuracy
- cv = 8

### Parameters of the best estimator
#### The best hyper-parameters
- best_resampler

- best_estimator
	- base_estimator = ExtraTreeClassifier()
	- n_estimators = 210
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
	- min_samples_leaf = 1
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
- gp_max_val_min = 0.09063787065748348
- gp_auc_min = 0.08696939754529276
- gp_max_val_mean = 0.08379135506430631
- gp_auc_mean = 0.07143458719855107
- gp_auc_max = 0.06897642403483796
- diff_auc = 0.061889765214746165
- diff_std = 0.05773223045543634
- gp_max_val_max = 0.055186142375838396
- high_power = 0.047282885861312296
- srmr = 0.03825172706352862
- hlbr = 0.031532434077723465
- low_power = 0.027226204960662345
- coe1[1] = 0.026450818575543697
- coe1[0] = 0.025269110018256814
- coe3[3] = 0.020630686503644476
- tdoa_mean = 0.01595033888760145
- ratio_max_to_10ms_ave_peaks = 0.0154159414925303
- coe3[2] = 0.013958463125752638
- tdoa_std = 0.01391791028378041
- tdoa_range = 0.013591670248727358
- gp_max_ix_std = 0.013383809285681064
- gp_max_ix_range = 0.012799066378146073
- ac_std = 0.011938143091732417
- gp_auc_std = 0.01155238588738252
- gp_max_ix_mean = 0.011365045553797153
- gp_max_ix_min = 0.010368902844529824
- tdoa_min = 0.010254293748022147
- gp_auc_range = 0.009868733974296367
- gp_max_val_std = 0.009744281747073048
- ac_auc = 0.008969653377826826
- gp_max_val_range = 0.008491421219309951
- ratio_max_to_9th_ave_peaks = 0.00541079376692284
- gp_max_ix_max = 0.004991203573031912
- tdoa_max = 0.004766301906691432
- coe3[0] = 0.0
- coe3[1] = 0.0

## Evaluation
cv = 8
### accuracy
- Scores = [ 0.896551724137931, 0.9642857142857143, 0.9285714285714286, 0.9642857142857143, 0.8928571428571429, 1.0, 1.0, 1.0 ]
- Mean = 0.9558189655172413
- Standard deviation = 0.04215816702657617

### balanced_accuracy
- Scores = [ 0.8928571428571428, 0.9666666666666667, 0.9333333333333333, 0.9666666666666667, 0.9, 1.0, 1.0, 1.0 ]
- Mean = 0.9574404761904762
- Standard deviation = 0.0413154843373734

### f1
- Scores = [ 0.9090909090909091, 0.9655172413793104, 0.9285714285714286, 0.9655172413793104, 0.888888888888889, 1.0, 1.0, 1.0 ]
- Mean = 0.9571982136637309
- Standard deviation = 0.040979202978721416

### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 105 | 3 |
| Actual Positive | 7 | 110 |

      