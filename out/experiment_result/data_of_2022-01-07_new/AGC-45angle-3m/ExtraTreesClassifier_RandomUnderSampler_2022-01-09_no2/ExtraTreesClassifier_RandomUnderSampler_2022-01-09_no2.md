# ExtraTreesClassifier_RandomUnderSampler_2022-01-09_no2
## Constants
- CSV_PATH = ../out/csv/experiment
- OUTPUT_PATH = ../out/experiment_result/data_of_2022-01-07_new/AGC-45angle-3m
- FEATURE_ATTRBS = ['low_power', 'high_power', 'hlbr', 'coe1[0]', 'coe1[1]', 'coe3[0]', 'coe3[1]', 'coe3[2]', 'coe3[3]', 'ratio_max_to_10ms_ave_peaks', 'ratio_max_to_9th_ave_peaks', 'ac_std', 'ac_auc', 'diff_std', 'diff_auc', 'srmr', 'gp_max_val_std', 'gp_max_val_range', 'gp_max_val_min', 'gp_max_val_max', 'gp_max_val_mean', 'gp_max_ix_std', 'gp_max_ix_range', 'gp_max_ix_min', 'gp_max_ix_max', 'gp_max_ix_mean', 'gp_auc_std', 'gp_auc_range', 'gp_auc_min', 'gp_auc_max', 'gp_auc_mean', 'tdoa_std', 'tdoa_range', 'tdoa_min', 'tdoa_max', 'tdoa_mean']
- LABEL_ATTRB = ['facing2']
- FACING_DOV_ANGLES = [1, 2]
- NCV = 8
- SCORING = ['accuracy', 'balanced_accuracy', 'f1']
- REFIT_SCORING = balanced_accuracy
- PARAM_GRID = [{'est__n_estimators': [50, 100, 150, 200, 300], 'est__min_samples_split': [2, 5, 10], 'est__min_samples_leaf': [1, 5, 10], 'est__max_features': ['sqrt', 'log2', None], 'est__bootstrap': [False], 'est__n_jobs': [-1], 'est__random_state': [42], 'est__max_samples': [0.01, 0.5, 0.09]}, {'est__n_estimators': [50, 100, 150, 200, 300], 'est__min_samples_split': [2, 5, 10], 'est__min_samples_leaf': [1, 5, 10], 'est__max_features': ['sqrt', 'log2', None], 'est__bootstrap': [True], 'est__oob_score': [True, False], 'est__n_jobs': [-1], 'est__random_state': [42], 'est__max_samples': [0.01, 0.5, 0.09]}]
- TRAIN_SET_SESSION = ['trial1', 'trial2']
- TEST_SET_SESSION = ['trial3', 'trial4', 'trial5']
- DISTANCE = [3]
- AGC_STATUS = ['AGC']

## Loaded CSV
- 2021-12-27_raspi_48000Hz_w1_N2^12_overlap80_with2022-01-07.csv

## Estimator
### Type
- resampler = RandomUnderSampler
- estimator = ExtraTreesClassifier

### Arguments for hyperparameter search
- resampler = RandomUnderSampler
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
	- replacement = False
	- n_features_in_ = 36
	- sampling_strategy_ = OrderedDict([(1, 24)])
	- sample_indices_ = [ 4  5  6  7  8  9 16 17 18 19 20 21 28 29 30 31 32 33 40 41 42 43 44 45
 14 34  0 48 23 15 25  1 47 11  2 24 27  3 10 39 35 46 36 49 38 13 22 26]

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
	- min_samples_split = 5
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
- gp_auc_max = 0.1649474198537225
- gp_max_val_max = 0.15271092472368453
- gp_auc_min = 0.10963046315510337
- gp_max_val_mean = 0.10235002104754302
- gp_auc_mean = 0.07497483590291039
- gp_max_val_min = 0.07278295676187212
- high_power = 0.053600697266454195
- diff_auc = 0.050525880941704106
- srmr = 0.03534875607261491
- diff_std = 0.02643315036767722
- low_power = 0.025898038023357727
- hlbr = 0.022432669652584187
- coe1[1] = 0.019719009277765504
- coe1[0] = 0.017349566022031818
- coe3[3] = 0.01507030081372667
- gp_max_ix_mean = 0.011923312236451626
- tdoa_mean = 0.01007189681759103
- gp_max_ix_std = 0.005143090569561161
- tdoa_std = 0.004715810505284191
- tdoa_min = 0.0031750161603102786
- gp_max_ix_max = 0.0031447813908171956
- gp_max_ix_min = 0.0030868347338935576
- gp_max_val_std = 0.00266918636918637
- tdoa_range = 0.002130641419719696
- tdoa_max = 0.0017964421114027415
- coe3[2] = 0.0016415427709545363
- ac_std = 0.001600840336134456
- ratio_max_to_9th_ave_peaks = 0.0015961940872426814
- ratio_max_to_10ms_ave_peaks = 0.0014629156010230178
- gp_auc_std = 0.0013762289997584136
- gp_max_ix_range = 0.00041521368907631125
- gp_auc_range = 0.0002753623188405811
- coe3[0] = 0.0
- coe3[1] = 0.0
- ac_auc = 0.0
- gp_max_val_range = 0.0

## Evaluation
cv = 8
### accuracy
- Scores = [ 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0 ]
- Mean = 1.0
- Standard deviation = 0.0

### balanced_accuracy
- Scores = [ 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0 ]
- Mean = 1.0
- Standard deviation = 0.0

### f1
- Scores = [ 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0 ]
- Mean = 1.0
- Standard deviation = 0.0

### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 36 | 0 |
| Actual Positive | 0 | 39 |

      