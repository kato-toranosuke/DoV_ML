# ExtraTreesClassifier_SMOTETomek_2021-12-29_no6
## Constants
- CSV_PATH = ../out/csv/experiment
- OUTPUT_PATH = ../out/experiment_result/data_of_2021-12-27/AGC-45angle-5m
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
- 2021-12-27_raspi_48000Hz_w1_N2^12_overlap80_new.csv

## Estimator
### Type
- resampler = SMOTETomek
- estimator = ExtraTreesClassifier

### Arguments for hyperparameter search
- resampler = SMOTETomek
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
	- smote = None
	- tomek = None
	- n_jobs = -1
	- n_features_in_ = 36
	- sampling_strategy_ = auto
	- smote_ = SMOTE(n_jobs=-1, random_state=42)
	- tomek_ = TomekLinks(n_jobs=-1, sampling_strategy='all')

- best_estimator
	- base_estimator = ExtraTreeClassifier()
	- n_estimators = 100
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
	- min_samples_split = 2
	- min_samples_leaf = 5
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
	- oob_decision_function_ = [[0.18858471 0.81141529]
 [0.10784748 0.89215252]
 [0.27873233 0.72126767]
 [0.65875055 0.34124945]
 [0.46352918 0.53647082]
 [0.8667181  0.1332819 ]
 [0.8207839  0.1792161 ]
 [0.86864541 0.13135459]
 [0.8846855  0.1153145 ]
 [0.19398599 0.80601401]
 [0.20372511 0.79627489]
 [0.31175083 0.68824917]
 [0.18208626 0.81791374]
 [0.75965063 0.24034937]
 [0.66969697 0.33030303]
 [0.29067784 0.70932216]
 [0.13018599 0.86981401]
 [0.17986026 0.82013974]
 [0.13870187 0.86129813]
 [0.71937841 0.28062159]
 [0.85081333 0.14918667]
 [0.8318401  0.1681599 ]
 [0.70683514 0.29316486]
 [0.29757907 0.70242093]
 [0.29751843 0.70248157]
 [0.1042194  0.8957806 ]
 [0.07724766 0.92275234]
 [0.36924787 0.63075213]
 [0.84434377 0.15565623]
 [0.86490792 0.13509208]
 [0.87823574 0.12176426]
 [0.70530989 0.29469011]
 [0.75165051 0.24834949]
 [0.12427738 0.87572262]
 [0.14054415 0.85945585]
 [0.12382088 0.87617912]
 [0.84795992 0.15204008]
 [0.88488878 0.11511122]]
	- oob_score_ = 0.9736842105263158

#### Importance of features
- gp_auc_max = 0.10536454458497184
- gp_auc_mean = 0.08849669935934062
- gp_max_val_max = 0.07973508676679818
- gp_max_val_mean = 0.07829016502898976
- gp_max_val_min = 0.06989318737379105
- high_power = 0.05941484407617946
- coe3[2] = 0.05170897167344368
- gp_auc_min = 0.047345521572325695
- srmr = 0.041237113402061855
- gp_auc_range = 0.041237113402061855
- diff_auc = 0.040388245412203594
- coe1[0] = 0.03268513016971297
- tdoa_max = 0.02169360978172036
- diff_std = 0.021467424690889192
- hlbr = 0.020968961510798
- coe3[3] = 0.020618556701030927
- tdoa_min = 0.020618556701030927
- ac_auc = 0.02036067932269379
- gp_auc_std = 0.01451014853076709
- low_power = 0.01294701777184808
- gp_max_ix_max = 0.012750104377428783
- ratio_max_to_9th_ave_peaks = 0.01258103943033266
- gp_max_val_std = 0.010623182659265134
- coe1[1] = 0.010309278350515464
- ac_std = 0.010309278350515464
- gp_max_val_range = 0.010309278350515464
- gp_max_ix_mean = 0.010309278350515464
- tdoa_range = 0.010309278350515464
- tdoa_mean = 0.008830269092112113
- tdoa_std = 0.008238078923599212
- ratio_max_to_10ms_ave_peaks = 0.004060620704467355
- gp_max_ix_range = 0.0023887352275584603
- coe3[0] = 0.0
- coe3[1] = 0.0
- gp_max_ix_std = 0.0
- gp_max_ix_min = 0.0

## Evaluation
cv = 8
### accuracy
- Scores = [ 1.0, 1.0, 0.9, 0.6666666666666666, 1.0, 1.0, 1.0, 1.0 ]
- Mean = 0.9458333333333333
- Standard deviation = 0.11047561319635711

### balanced_accuracy
- Scores = [ 1.0, 1.0, 0.9, 0.7, 1.0, 1.0, 1.0, 1.0 ]
- Mean = 0.95
- Standard deviation = 0.1

### f1
- Scores = [ 1.0, 1.0, 0.9090909090909091, 0.5714285714285715, 1.0, 1.0, 1.0, 1.0 ]
- Mean = 0.935064935064935
- Standard deviation = 0.1406260248552449

### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 35 | 1 |
| Actual Positive | 3 | 36 |

      