# ExtraTreesClassifier_RandomOverSampler_2021-12-29_no3
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
	- n_estimators = 150
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

#### Importance of features
- gp_auc_max = 0.1276720752517294
- high_power = 0.10044548143782166
- gp_auc_mean = 0.08602917128248008
- gp_auc_min = 0.08295587219260121
- gp_max_val_mean = 0.07680616486346413
- gp_max_val_min = 0.07268189099119249
- gp_max_val_max = 0.07142627966672901
- srmr = 0.06106887452385789
- hlbr = 0.05079491782522
- diff_auc = 0.04830971140200742
- diff_std = 0.03723133824551026
- coe1[0] = 0.028367810082648895
- gp_auc_std = 0.0243494002171907
- coe1[1] = 0.019543242922609515
- gp_max_val_std = 0.014630096099575081
- gp_auc_range = 0.013569219997618868
- gp_max_ix_max = 0.01140654322156943
- gp_max_val_range = 0.011259693015602867
- ac_auc = 0.011113115782730013
- ac_std = 0.011079643513562012
- tdoa_max = 0.009586372476853353
- coe3[2] = 0.008614790654819923
- low_power = 0.0057723687183126515
- ratio_max_to_9th_ave_peaks = 0.003704732370530256
- tdoa_mean = 0.0031172605739599652
- gp_max_ix_mean = 0.0027691235173505574
- gp_max_ix_std = 0.0023809181332644118
- coe3[3] = 0.0017717021098127973
- ratio_max_to_10ms_ave_peaks = 0.001219533296405038
- tdoa_std = 0.00032265561297004883
- coe3[0] = 0.0
- coe3[1] = 0.0
- gp_max_ix_range = 0.0
- gp_max_ix_min = 0.0
- tdoa_range = 0.0
- tdoa_min = 0.0

## Evaluation
cv = 8
### accuracy
- Scores = [ 0.75, 1.0, 0.625, 1.0, 1.0, 0.7142857142857143, 1.0, 0.8571428571428571 ]
- Mean = 0.8683035714285714
- Standard deviation = 0.14422821409955452

### balanced_accuracy
- Scores = [ 0.8333333333333333, 1.0, 0.75, 1.0, 1.0, 0.8333333333333333, 1.0, 0.9166666666666667 ]
- Mean = 0.9166666666666666
- Standard deviation = 0.09316949906249125

### f1
- Scores = [ 0.6666666666666666, 1.0, 0.5714285714285715, 1.0, 1.0, 0.5, 1.0, 0.6666666666666666 ]
- Mean = 0.8005952380952381
- Standard deviation = 0.20548650170011745

### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 40 | 8 |
| Actual Positive | 0 | 12 |

      