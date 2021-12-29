# ExtraTreesClassifier_RandomOverSampler_2021-12-29_no3
## Constants
- CSV_PATH = ../out/csv/experiment
- OUTPUT_PATH = ../out/experiment_result/data_of_2021-12-27/NoAGC-0angle-3m
- FEATURE_ATTRBS = ['low_power', 'high_power', 'hlbr', 'coe1[0]', 'coe1[1]', 'coe3[0]', 'coe3[1]', 'coe3[2]', 'coe3[3]', 'ratio_max_to_10ms_ave_peaks', 'ratio_max_to_9th_ave_peaks', 'ac_std', 'ac_auc', 'diff_std', 'diff_auc', 'srmr', 'gp_max_val_std', 'gp_max_val_range', 'gp_max_val_min', 'gp_max_val_max', 'gp_max_val_mean', 'gp_max_ix_std', 'gp_max_ix_range', 'gp_max_ix_min', 'gp_max_ix_max', 'gp_max_ix_mean', 'gp_auc_std', 'gp_auc_range', 'gp_auc_min', 'gp_auc_max', 'gp_auc_mean', 'tdoa_std', 'tdoa_range', 'tdoa_min', 'tdoa_max', 'tdoa_mean']
- LABEL_ATTRB = ['facing']
- FACING_DOV_ANGLES = [1]
- NCV = 8
- SCORING = ['accuracy', 'balanced_accuracy', 'f1']
- REFIT_SCORING = balanced_accuracy
- PARAM_GRID = [{'est__n_estimators': [50, 100, 150, 200, 300], 'est__min_samples_split': [2, 5, 10], 'est__min_samples_leaf': [1, 5, 10], 'est__max_features': ['sqrt', 'log2', None], 'est__bootstrap': [False], 'est__n_jobs': [-1], 'est__random_state': [42], 'est__max_samples': [0.01, 0.5, 0.09]}, {'est__n_estimators': [50, 100, 150, 200, 300], 'est__min_samples_split': [2, 5, 10], 'est__min_samples_leaf': [1, 5, 10], 'est__max_features': ['sqrt', 'log2', None], 'est__bootstrap': [True], 'est__oob_score': [True, False], 'est__n_jobs': [-1], 'est__random_state': [42], 'est__max_samples': [0.01, 0.5, 0.09]}]
- TRAIN_SET_SESSION = ['trial1', 'trial2']
- TEST_SET_SESSION = ['trial3', 'trial4', 'trial5']
- DISTANCE = [3]
- AGC_STATUS = ['NoAGC']

## Loaded CSV
- 2021-12-27_raspi_48000Hz_w1_N2^12_overlap80_new.csv

## Estimator
### Type
- resampler = RandomOverSampler
- estimator = ExtraTreesClassifier

### Arguments for hyperparameter search
- resampler = RandomOverSampler
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
	- shrinkage = None
	- n_features_in_ = 36
	- sampling_strategy_ = OrderedDict([(1, 24)])
	- shrinkage_ = None
	- sample_indices_ = [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23
 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 36 13 24 36 12 37 24 24
 36  1 12 36 12 12 37 24 13 37 37 12 25 24  1 37]

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
	- min_samples_leaf = 10
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
	- oob_decision_function_ = [[0.42994989 0.57005011]
 [0.44719468 0.55280532]
 [0.54399032 0.45600968]
 [0.48828655 0.51171345]
 [0.54165501 0.45834499]
 [0.45916685 0.54083315]
 [0.57060678 0.42939322]
 [0.56321093 0.43678907]
 [0.56814057 0.43185943]
 [0.48357431 0.51642569]
 [0.47188863 0.52811137]
 [0.473087   0.526913  ]
 [0.46514063 0.53485937]
 [0.40675186 0.59324814]
 [0.51435831 0.48564169]
 [0.46532352 0.53467648]
 [0.56720919 0.43279081]
 [0.55566495 0.44433505]
 [0.51946491 0.48053509]
 [0.56446186 0.43553814]
 [0.52232604 0.47767396]
 [0.51569543 0.48430457]
 [0.56461238 0.43538762]
 [0.49785789 0.50214211]
 [0.47853027 0.52146973]
 [0.4631018  0.5368982 ]
 [0.47091208 0.52908792]
 [0.44458947 0.55541053]
 [0.56590186 0.43409814]
 [0.56975833 0.43024167]
 [0.54368391 0.45631609]
 [0.54856131 0.45143869]
 [0.56186215 0.43813785]
 [0.54719239 0.45280761]
 [0.52765055 0.47234945]
 [0.41180115 0.58819885]
 [0.44736734 0.55263266]
 [0.39502723 0.60497277]
 [0.48823501 0.51176499]
 [0.47109811 0.52890189]
 [0.43386396 0.56613604]
 [0.42708483 0.57291517]
 [0.52672664 0.47327336]
 [0.41757271 0.58242729]
 [0.46722982 0.53277018]
 [0.39004406 0.60995594]
 [0.52807014 0.47192986]
 [0.52461024 0.47538976]
 [0.41792272 0.58207728]
 [0.40874806 0.59125194]
 [0.47853744 0.52146256]
 [0.41534619 0.58465381]
 [0.46174477 0.53825523]
 [0.47289842 0.52710158]
 [0.41168808 0.58831192]
 [0.53435715 0.46564285]
 [0.39152416 0.60847584]
 [0.40162986 0.59837014]
 [0.3956644  0.6043356 ]
 [0.48760507 0.51239493]
 [0.45490524 0.54509476]
 [0.46303566 0.53696434]
 [0.43360549 0.56639451]
 [0.39081357 0.60918643]]
	- oob_score_ = 0.75

#### Importance of features
- ratio_max_to_10ms_ave_peaks = 0.11111111111111112
- low_power = 0.08888888888888889
- high_power = 0.06666666666666667
- coe3[2] = 0.06666666666666667
- srmr = 0.06666666666666667
- gp_max_val_std = 0.06666666666666667
- coe1[0] = 0.044444444444444446
- ac_std = 0.044444444444444446
- gp_max_val_range = 0.044444444444444446
- gp_max_ix_mean = 0.044444444444444446
- gp_auc_min = 0.044444444444444446
- hlbr = 0.022222222222222223
- coe3[3] = 0.022222222222222223
- ratio_max_to_9th_ave_peaks = 0.022222222222222223
- ac_auc = 0.022222222222222223
- diff_std = 0.022222222222222223
- diff_auc = 0.022222222222222223
- gp_max_val_max = 0.022222222222222223
- gp_max_val_mean = 0.022222222222222223
- gp_max_ix_std = 0.022222222222222223
- gp_auc_std = 0.022222222222222223
- gp_auc_range = 0.022222222222222223
- gp_auc_max = 0.022222222222222223
- tdoa_std = 0.022222222222222223
- tdoa_mean = 0.022222222222222223
- coe1[1] = 0.0
- coe3[0] = 0.0
- coe3[1] = 0.0
- gp_max_val_min = 0.0
- gp_max_ix_range = 0.0
- gp_max_ix_min = 0.0
- gp_max_ix_max = 0.0
- gp_auc_mean = 0.0
- tdoa_range = 0.0
- tdoa_min = 0.0
- tdoa_max = 0.0

## Evaluation
cv = 8
### accuracy
- Scores = [ 0.75, 1.0, 0.5, 0.875, 0.5714285714285714, 0.7142857142857143, 1.0, 0.14285714285714285 ]
- Mean = 0.6941964285714286
- Standard deviation = 0.2692578702685042

### balanced_accuracy
- Scores = [ 0.8333333333333333, 1.0, 0.6666666666666666, 0.75, 0.75, 0.8333333333333333, 1.0, 0.5 ]
- Mean = 0.7916666666666666
- Standard deviation = 0.15590239111558088

### f1
- Scores = [ 0.6666666666666666, 1.0, 0.5, 0.6666666666666666, 0.4, 0.5, 1.0, 0.25 ]
- Mean = 0.6229166666666666
- Standard deviation = 0.25179046348104606

### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 31 | 17 |
| Actual Positive | 1 | 11 |

      