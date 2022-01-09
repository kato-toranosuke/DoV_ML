# ExtraTreesClassifier_NoResampler_2022-01-09_no0
## Constants
- CSV_PATH = ../out/csv/experiment
- OUTPUT_PATH = ../out/experiment_result/data_of_2022-01-07_new2/AGC-0angle-under5m
- FEATURE_ATTRBS = ['low_power', 'high_power', 'hlbr', 'coe1[0]', 'coe1[1]', 'coe3[0]', 'coe3[1]', 'coe3[2]', 'coe3[3]', 'ratio_max_to_10ms_ave_peaks', 'ratio_max_to_9th_ave_peaks', 'ac_std', 'ac_auc', 'diff_std', 'diff_auc', 'srmr', 'gp_max_val_std', 'gp_max_val_range', 'gp_max_val_min', 'gp_max_val_max', 'gp_max_val_mean', 'gp_max_ix_std', 'gp_max_ix_range', 'gp_max_ix_min', 'gp_max_ix_max', 'gp_max_ix_mean', 'gp_auc_std', 'gp_auc_range', 'gp_auc_min', 'gp_auc_max', 'gp_auc_mean', 'tdoa_std', 'tdoa_range', 'tdoa_min', 'tdoa_max', 'tdoa_mean']
- LABEL_ATTRB = ['facing']
- FACING_DOV_ANGLES = [1]
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
	- n_estimators = 85
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
- high_power = 0.08015074018468682
- gp_auc_min = 0.05886416105505457
- diff_auc = 0.055023514106442066
- gp_max_val_mean = 0.05426992223739076
- gp_max_val_min = 0.052407175588370096
- gp_auc_max = 0.05004742032559543
- gp_max_val_max = 0.05003651171701475
- hlbr = 0.04581464809508586
- gp_auc_mean = 0.045006573750460764
- diff_std = 0.03723741014345649
- coe1[0] = 0.030145804989615294
- gp_max_val_std = 0.02761650873674935
- low_power = 0.027368113677880463
- ac_std = 0.026526971641151104
- coe1[1] = 0.024657749889423083
- gp_auc_range = 0.024052840105841078
- gp_max_val_range = 0.0240346105879998
- coe3[3] = 0.023553783327969983
- ratio_max_to_9th_ave_peaks = 0.02344688769600993
- coe3[2] = 0.020372533722817866
- tdoa_mean = 0.02032602290033018
- ratio_max_to_10ms_ave_peaks = 0.02002237146847457
- srmr = 0.019860850090090948
- gp_auc_std = 0.01932138459698501
- ac_auc = 0.018345356300325646
- tdoa_std = 0.01748925666692308
- tdoa_max = 0.016344326844490692
- gp_max_ix_mean = 0.015084052269314814
- tdoa_range = 0.013659244178058784
- tdoa_min = 0.01348515855728955
- gp_max_ix_max = 0.013190510499774013
- gp_max_ix_std = 0.012592674432304241
- gp_max_ix_range = 0.01176353857039071
- gp_max_ix_min = 0.007881371046232117
- coe3[0] = 0.0
- coe3[1] = 0.0

## Evaluation
cv = 8
### accuracy
- Scores = [ 0.7241379310344828, 0.75, 0.8571428571428571, 0.7857142857142857, 0.8571428571428571, 0.8214285714285714, 0.8571428571428571, 0.7857142857142857 ]
- Mean = 0.8048029556650246
- Standard deviation = 0.048391336710316486

### balanced_accuracy
- Scores = [ 0.5797101449275363, 0.5984848484848485, 0.7272727272727273, 0.5606060606060607, 0.7272727272727273, 0.8913043478260869, 0.6, 0.5565217391304348 ]
- Mean = 0.6551465744400528
- Standard deviation = 0.10998975829007357

### f1
- Scores = [ 0.3333333333333333, 0.3636363636363636, 0.6, 0.25, 0.6, 0.6666666666666666, 0.33333333333333337, 0.25 ]
- Mean = 0.4246212121212121
- Standard deviation = 0.15869494374390325

### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 164 | 16 |
| Actual Positive | 23 | 22 |

      