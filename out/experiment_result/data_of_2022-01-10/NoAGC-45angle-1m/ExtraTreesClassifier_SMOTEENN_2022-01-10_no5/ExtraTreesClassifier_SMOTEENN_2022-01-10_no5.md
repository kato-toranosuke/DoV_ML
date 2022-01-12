# ExtraTreesClassifier_SMOTEENN_2022-01-10_no5
## Constants
- CSV_PATH = ../out/csv/experiment
- OUTPUT_PATH = ../out/experiment_result/data_of_2022-01-10/NoAGC-45angle-1m
- FEATURE_ATTRBS = ['low_power', 'high_power', 'hlbr', 'coe1[0]', 'coe1[1]', 'coe3[0]', 'coe3[1]', 'coe3[2]', 'coe3[3]', 'ratio_max_to_10ms_ave_peaks', 'ratio_max_to_9th_ave_peaks', 'ac_std', 'ac_auc', 'diff_std', 'diff_auc', 'srmr', 'gp_max_val_std', 'gp_max_val_range', 'gp_max_val_min', 'gp_max_val_max', 'gp_max_val_mean', 'gp_max_ix_std', 'gp_max_ix_range', 'gp_max_ix_min', 'gp_max_ix_max', 'gp_max_ix_mean', 'gp_auc_std', 'gp_auc_range', 'gp_auc_min', 'gp_auc_max', 'gp_auc_mean', 'tdoa_std', 'tdoa_range', 'tdoa_min', 'tdoa_max', 'tdoa_mean']
- LABEL_ATTRB = ['facing2']
- FACING_DOV_ANGLES = [1, 2]
- NCV = 8
- SCORING = ['accuracy', 'balanced_accuracy', 'f1']
- REFIT_SCORING = balanced_accuracy
- PARAM_GRID = [{'est__n_estimators': [50, 100, 150, 200, 300], 'est__min_samples_split': [2, 5, 10], 'est__min_samples_leaf': [1, 5, 10], 'est__max_features': ['sqrt', 'log2', None], 'est__bootstrap': [False], 'est__n_jobs': [-1], 'est__random_state': [42], 'est__max_samples': [0.01, 0.5, 0.09]}, {'est__n_estimators': [50, 100, 150, 200, 300], 'est__min_samples_split': [2, 5, 10], 'est__min_samples_leaf': [1, 5, 10], 'est__max_features': ['sqrt', 'log2', None], 'est__bootstrap': [True], 'est__oob_score': [True, False], 'est__n_jobs': [-1], 'est__random_state': [42], 'est__max_samples': [0.01, 0.5, 0.09]}]
- TRAIN_SET_SESSION = ['trial1', 'trial2']
- TEST_SET_SESSION = ['trial3', 'trial4', 'trial5']
- DISTANCE = [1]
- AGC_STATUS = ['NoAGC']

## Loaded CSV
- 2022-01-10_raspi_48000Hz_w1_N2^12_overlap80.csv

## Estimator
### Type
- resampler = SMOTEENN
- estimator = ExtraTreesClassifier

### Arguments for hyperparameter search
- resampler = SMOTEENN
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
	- enn = None
	- n_jobs = -1
	- n_features_in_ = 36
	- sampling_strategy_ = auto
	- smote_ = SMOTE(n_jobs=-1, random_state=42)
	- enn_ = EditedNearestNeighbours(n_jobs=-1, sampling_strategy='all')

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
- gp_max_ix_range = 0.10131922398589067
- gp_max_val_max = 0.0930989380989381
- gp_auc_max = 0.07920388176638175
- gp_max_val_std = 0.0751278659611993
- tdoa_range = 0.06647222222222222
- gp_max_ix_min = 0.05691091778591779
- tdoa_mean = 0.045581404320987666
- tdoa_min = 0.04556695156695158
- gp_auc_mean = 0.04534259259259259
- tdoa_std = 0.0420462962962963
- gp_auc_min = 0.04160580160580161
- gp_max_val_mean = 0.03863001813001813
- gp_auc_range = 0.03115520282186949
- srmr = 0.02802272727272727
- gp_max_ix_std = 0.024888888888888894
- hlbr = 0.02168426827801827
- gp_max_val_range = 0.019870129870129868
- ac_auc = 0.01942965367965368
- gp_max_ix_mean = 0.016371104204437537
- gp_max_ix_max = 0.014638888888888892
- ac_std = 0.01311904761904762
- ratio_max_to_10ms_ave_peaks = 0.01239583333333333
- diff_std = 0.010479700854700855
- coe3[2] = 0.010074074074074074
- gp_auc_std = 0.009129629629629628
- low_power = 0.00787037037037037
- ratio_max_to_9th_ave_peaks = 0.007664983164983164
- high_power = 0.007555555555555554
- coe1[1] = 0.005981481481481479
- coe3[3] = 0.005666666666666664
- gp_max_val_min = 0.001259259259259258
- coe1[0] = 0.0010493827160493827
- tdoa_max = 0.0007870370370370375
- coe3[0] = 0.0
- coe3[1] = 0.0
- diff_auc = 0.0

## Evaluation
cv = 8
### accuracy
- Scores = [ 0.8, 0.9, 1.0, 0.4444444444444444, 0.7777777777777778, 0.7777777777777778, 0.8888888888888888, 0.8888888888888888 ]
- Mean = 0.8097222222222222
- Standard deviation = 0.15510226614386705

### balanced_accuracy
- Scores = [ 0.8, 0.9, 1.0, 0.5, 0.8, 0.8, 0.9, 0.9 ]
- Mean = 0.8250000000000001
- Standard deviation = 0.13919410907075055

### f1
- Scores = [ 0.8333333333333333, 0.888888888888889, 1.0, 0.0, 0.7499999999999999, 0.7499999999999999, 0.888888888888889, 0.888888888888889 ]
- Mean = 0.75
- Standard deviation = 0.293644090442583

### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 32 | 4 |
| Actual Positive | 11 | 28 |

      