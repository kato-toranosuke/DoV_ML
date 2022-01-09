# ExtraTreesClassifier_NoResampler_2022-01-09_no0
## Constants
- CSV_PATH = ../out/csv/experiment
- OUTPUT_PATH = ../out/experiment_result/data_of_2022-01-07_new/AGC-45angle-5m
- FEATURE_ATTRBS = ['low_power', 'high_power', 'hlbr', 'coe1[0]', 'coe1[1]', 'coe3[0]', 'coe3[1]', 'coe3[2]', 'coe3[3]', 'ratio_max_to_10ms_ave_peaks', 'ratio_max_to_9th_ave_peaks', 'ac_std', 'ac_auc', 'diff_std', 'diff_auc', 'srmr', 'gp_max_val_std', 'gp_max_val_range', 'gp_max_val_min', 'gp_max_val_max', 'gp_max_val_mean', 'gp_max_ix_std', 'gp_max_ix_range', 'gp_max_ix_min', 'gp_max_ix_max', 'gp_max_ix_mean', 'gp_auc_std', 'gp_auc_range', 'gp_auc_min', 'gp_auc_max', 'gp_auc_mean', 'tdoa_std', 'tdoa_range', 'tdoa_min', 'tdoa_max', 'tdoa_mean']
- LABEL_ATTRB = ['facing2']
- FACING_DOV_ANGLES = [1, 2]
- NCV = 8
- SCORING = ['accuracy', 'balanced_accuracy', 'f1']
- REFIT_SCORING = balanced_accuracy
- PARAM_GRID = [{'est__n_estimators': [50, 100, 150, 200, 300], 'est__min_samples_split': [2, 5, 10], 'est__min_samples_leaf': [1, 5, 10], 'est__max_features': ['sqrt', 'log2', None], 'est__bootstrap': [False], 'est__n_jobs': [-1], 'est__random_state': [42], 'est__max_samples': [0.01, 0.5, 0.09]}, {'est__n_estimators': [50, 100, 150, 200, 300], 'est__min_samples_split': [2, 5, 10], 'est__min_samples_leaf': [1, 5, 10], 'est__max_features': ['sqrt', 'log2', None], 'est__bootstrap': [True], 'est__oob_score': [True, False], 'est__n_jobs': [-1], 'est__random_state': [42], 'est__max_samples': [0.01, 0.5, 0.09]}]
- TRAIN_SET_SESSION = ['trial1', 'trial2']
- TEST_SET_SESSION = ['trial3', 'trial4', 'trial5']
- DISTANCE = [5]
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
- high_power = 0.11511342950358715
- gp_max_val_max = 0.1030259061629254
- gp_auc_max = 0.09215614650343693
- gp_max_val_mean = 0.08785418021080474
- gp_auc_mean = 0.06886195899392675
- gp_auc_min = 0.059046217836834544
- gp_max_val_min = 0.056947758149127274
- hlbr = 0.054363845189649235
- diff_auc = 0.049691119746266804
- srmr = 0.045768242542816855
- coe1[0] = 0.03683093466170676
- coe3[3] = 0.03050638540512737
- low_power = 0.028414362136205806
- coe1[1] = 0.021628529816088326
- diff_std = 0.017062312687312686
- gp_max_val_std = 0.016890394930051553
- gp_auc_std = 0.015848135138354983
- gp_auc_range = 0.013010957943023158
- tdoa_max = 0.012800549266690157
- tdoa_min = 0.012282217034055265
- coe3[2] = 0.011966456675508401
- gp_max_ix_max = 0.008967127221437565
- gp_max_ix_range = 0.008898638478379857
- gp_max_ix_min = 0.008555909902063747
- ac_auc = 0.006682435211846975
- ac_std = 0.004513888888888889
- tdoa_range = 0.004103535353535355
- gp_max_val_range = 0.0038369856639087433
- ratio_max_to_9th_ave_peaks = 0.0025106837606837613
- tdoa_std = 0.0010683760683760683
- ratio_max_to_10ms_ave_peaks = 0.0007478632478632478
- gp_max_ix_mean = 4.451566951566973e-05
- coe3[0] = 0.0
- coe3[1] = 0.0
- gp_max_ix_std = 0.0
- tdoa_mean = 0.0

## Evaluation
cv = 8
### accuracy
- Scores = [ 0.9, 1.0, 0.9, 0.6666666666666666, 1.0, 1.0, 1.0, 1.0 ]
- Mean = 0.9333333333333333
- Standard deviation = 0.10929064207170001

### balanced_accuracy
- Scores = [ 0.9, 1.0, 0.9, 0.7, 1.0, 1.0, 1.0, 1.0 ]
- Mean = 0.9375
- Standard deviation = 0.09921567416492216

### f1
- Scores = [ 0.9090909090909091, 1.0, 0.9090909090909091, 0.5714285714285715, 1.0, 1.0, 1.0, 1.0 ]
- Mean = 0.9237012987012987
- Standard deviation = 0.13857780325896452

### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 34 | 2 |
| Actual Positive | 1 | 38 |

      