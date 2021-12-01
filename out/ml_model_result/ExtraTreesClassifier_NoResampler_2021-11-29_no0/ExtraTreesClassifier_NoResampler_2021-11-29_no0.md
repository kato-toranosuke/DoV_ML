# ExtraTreesClassifier_NoResampler_2021-11-29_no0
## Constants
- CSV_PATH = ../out/csv/experiment
- OUTPUT_PATH = ../out/ml_model_result
- FEATURE_ATTRBS = ['low_power', 'high_power', 'hlbr', 'coe1[0]', 'coe1[1]', 'coe3[0]', 'coe3[1]', 'coe3[2]', 'coe3[3]', 'ratio_max_to_10ms_ave_peaks', 'ratio_max_to_9th_ave_peaks', 'ac_std', 'ac_auc', 'diff_std', 'diff_auc', 'srmr', 'gp_max_val_std', 'gp_max_val_range', 'gp_max_val_min', 'gp_max_val_max', 'gp_max_val_mean', 'gp_max_ix_std', 'gp_max_ix_range', 'gp_max_ix_min', 'gp_max_ix_max', 'gp_max_ix_mean', 'gp_auc_std', 'gp_auc_range', 'gp_auc_min', 'gp_auc_max', 'gp_auc_mean', 'tdoa_std', 'tdoa_range', 'tdoa_min', 'tdoa_max', 'tdoa_mean']
- LABEL_ATTRB = ['dov_angle']
- FACING_DOV_ANGLES = [0, 45, 315]
- NCV = 10
- SCORING = ['accuracy', 'balanced_accuracy', 'f1']
- REFIT_SCORING = balanced_accuracy
- PARAM_GRID = [{'est__n_estimators': [100, 500, 1000], 'est__min_samples_split': [2, 5, 10], 'est__min_samples_leaf': [1, 5, 10], 'est__max_features': ['sqrt', 'log2', None], 'est__bootstrap': [False], 'est__n_jobs': [-1], 'est__random_state': [42], 'est__max_samples': [0.01, 0.5, 0.09]}, {'est__n_estimators': [100, 500, 1000], 'est__min_samples_split': [2, 5, 10], 'est__min_samples_leaf': [1, 5, 10], 'est__max_features': ['sqrt', 'log2', None], 'est__bootstrap': [True], 'est__oob_score': [True, False], 'est__n_jobs': [-1], 'est__random_state': [42], 'est__max_samples': [0.01, 0.5, 0.09]}]

## Loaded CSV
- 2021-11-26_raspi_16000Hz_w1_N2^12_overlap80.csv

## Estimator
### Type
- resampler = NoResampler
- estimator = ExtraTreesClassifier

### Arguments for hyperparameter search
- resampler = NoResampler
- estimator = ExtraTreesClassifier
- param_grid = 
	- {'est__n_estimators': [100, 500, 1000], 'est__min_samples_split': [2, 5, 10], 'est__min_samples_leaf': [1, 5, 10], 'est__max_features': ['sqrt', 'log2', None], 'est__bootstrap': [False], 'est__n_jobs': [-1], 'est__random_state': [42], 'est__max_samples': [0.01, 0.5, 0.09]}
	- {'est__n_estimators': [100, 500, 1000], 'est__min_samples_split': [2, 5, 10], 'est__min_samples_leaf': [1, 5, 10], 'est__max_features': ['sqrt', 'log2', None], 'est__bootstrap': [True], 'est__oob_score': [True, False], 'est__n_jobs': [-1], 'est__random_state': [42], 'est__max_samples': [0.01, 0.5, 0.09]}

- scoring = ['accuracy', 'balanced_accuracy', 'f1']
- refit = balanced_accuracy
- cv = 10

### Parameters of the best estimator
#### The best hyper-parameters
- best_resampler

- best_estimator
	- base_estimator = ExtraTreeClassifier()
	- n_estimators = 500
	- estimator_params = ('criterion', 'max_depth', 'min_samples_split', 'min_samples_leaf', 'min_weight_fraction_leaf', 'max_features', 'max_leaf_nodes', 'min_impurity_decrease', 'min_impurity_split', 'random_state', 'ccp_alpha')
	- bootstrap = True
	- oob_score = True
	- n_jobs = -1
	- random_state = 42
	- verbose = 0
	- warm_start = False
	- class_weight = None
	- max_samples = 0.09
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
	- oob_decision_function_ = [[0.36043956 0.63956044]
 [0.41684665 0.58315335]
 [0.56531049 0.43468951]
 [0.87012987 0.12987013]
 [0.79609544 0.20390456]
 [0.8245614  0.1754386 ]
 [0.73144105 0.26855895]
 [0.48701299 0.51298701]
 [0.41986456 0.58013544]
 [0.47008547 0.52991453]
 [0.87201735 0.12798265]
 [0.87633262 0.12366738]
 [0.87527352 0.12472648]
 [0.88552916 0.11447084]
 [0.79333333 0.20666667]
 [0.53617021 0.46382979]
 [0.32112069 0.67887931]
 [0.35064935 0.64935065]
 [0.82429501 0.17570499]
 [0.72688172 0.27311828]
 [0.86609071 0.13390929]
 [0.87284483 0.12715517]
 [0.72747253 0.27252747]
 [0.37796976 0.62203024]
 [0.34151786 0.65848214]
 [0.34140969 0.65859031]
 [0.62114537 0.37885463]
 [0.80477223 0.19522777]
 [0.86830357 0.13169643]
 [0.86784141 0.13215859]
 [0.73752711 0.26247289]
 [0.51082251 0.48917749]
 [0.45633188 0.54366812]
 [0.44662309 0.55337691]
 [0.79784946 0.20215054]
 [0.81637168 0.18362832]
 [0.85560345 0.14439655]
 [0.85200846 0.14799154]
 [0.85217391 0.14782609]
 [0.48464912 0.51535088]
 [0.31485588 0.68514412]
 [0.35869565 0.64130435]
 [0.7012987  0.2987013 ]
 [0.87311828 0.12688172]
 [0.85307018 0.14692982]
 [0.77483444 0.22516556]
 [0.76821192 0.23178808]
 [0.48712446 0.51287554]]
	- oob_score_ = 0.9583333333333334

#### Importance of features
- gp_auc_min = 0.07565011820330969
- gp_max_val_mean = 0.06776989755713161
- gp_max_val_max = 0.066193853427896
- high_power = 0.06619385342789598
- gp_auc_max = 0.05673758865248227
- gp_max_val_min = 0.056474914630943
- gp_auc_mean = 0.055686892566325204
- diff_std = 0.05358550039401103
- hlbr = 0.04412923561859732
- diff_auc = 0.03940110323089046
- low_power = 0.030995534541633837
- tdoa_min = 0.027580772261623327
- gp_max_val_range = 0.027318098240084052
- coe3[3] = 0.026004728132387706
- ac_auc = 0.023903335960073546
- gp_auc_std = 0.02364066193853428
- ac_std = 0.0225899658523772
- gp_auc_range = 0.02127659574468085
- coe1[1] = 0.01970055161544523
- ratio_max_to_9th_ave_peaks = 0.01970055161544523
- srmr = 0.018124507486209616
- gp_max_ix_range = 0.016548463356973995
- gp_max_val_std = 0.015760441292356184
- ratio_max_to_10ms_ave_peaks = 0.014972419227738376
- tdoa_range = 0.014184397163120569
- coe3[2] = 0.014184397163120567
- gp_max_ix_std = 0.013396375098502757
- coe1[0] = 0.01260835303388495
- tdoa_max = 0.012083004990806409
- tdoa_mean = 0.011032308904649329
- gp_max_ix_mean = 0.01024428684003152
- tdoa_std = 0.009456264775413711
- gp_max_ix_min = 0.008930916732335172
- gp_max_ix_max = 0.003940110323089047
- coe3[0] = 0.0
- coe3[1] = 0.0

## Evaluation
cv = 10
### accuracy
- Scores = [ 0.6666666666666666, 0.6666666666666666, 0.6666666666666666, 0.6666666666666666, 0.5, 0.5, 0.5, 0.5, 0.5, 1.0 ]
- Mean = 0.6166666666666666
- Standard deviation = 0.15

### balanced_accuracy
- Scores = [ 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 1.0 ]
- Mean = 0.55
- Standard deviation = 0.15

### f1
- Scores = [ 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0 ]
- Mean = 0.0
- Standard deviation = 0.0

### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 15 | 0 |
| Actual Positive | 9 | 0 |

      