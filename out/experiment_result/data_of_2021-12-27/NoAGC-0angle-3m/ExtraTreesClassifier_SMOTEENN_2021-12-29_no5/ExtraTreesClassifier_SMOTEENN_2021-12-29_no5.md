# ExtraTreesClassifier_SMOTEENN_2021-12-29_no5
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
	- n_estimators = 300
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
	- min_samples_split = 5
	- min_samples_leaf = 1
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
- low_power = 0.08980857939144093
- high_power = 0.08927804383337566
- coe3[3] = 0.08818113051185578
- diff_std = 0.07290287239669371
- coe1[0] = 0.06664385593656387
- coe1[1] = 0.06303008853417313
- diff_auc = 0.06221744085632434
- ac_std = 0.06043072556434552
- coe3[2] = 0.05843160362662442
- ac_auc = 0.05553499278902208
- gp_auc_max = 0.028628663246795548
- gp_max_val_max = 0.028177583555886235
- gp_max_val_min = 0.027165122072314023
- ratio_max_to_10ms_ave_peaks = 0.022415011187555248
- gp_max_val_mean = 0.02079149021696107
- srmr = 0.019990498528525212
- gp_auc_min = 0.018707346959455185
- gp_max_ix_std = 0.017565257817492606
- gp_max_val_range = 0.015929414631308533
- tdoa_std = 0.013038497516462062
- gp_auc_range = 0.01256442829062462
- gp_auc_std = 0.012458639628684287
- gp_max_val_std = 0.012130637080261599
- gp_auc_mean = 0.011151641306769157
- gp_max_ix_mean = 0.006848974582125436
- tdoa_mean = 0.006717875548309012
- hlbr = 0.005936782311896049
- gp_max_ix_max = 0.004754778268621748
- ratio_max_to_9th_ave_peaks = 0.004461743498691646
- tdoa_max = 0.0022526062550120283
- tdoa_range = 0.0018536740558292278
- coe3[0] = 0.0
- coe3[1] = 0.0
- gp_max_ix_range = 0.0
- gp_max_ix_min = 0.0
- tdoa_min = 0.0

## Evaluation
cv = 8
### accuracy
- Scores = [ 0.875, 0.875, 0.875, 0.875, 0.5714285714285714, 1.0, 1.0, 0.42857142857142855 ]
- Mean = 0.8125
- Standard deviation = 0.19087105648599956

### balanced_accuracy
- Scores = [ 0.75, 0.75, 0.9166666666666667, 0.75, 0.75, 1.0, 1.0, 0.6666666666666666 ]
- Mean = 0.8229166666666667
- Standard deviation = 0.1210307295689818

### f1
- Scores = [ 0.6666666666666666, 0.6666666666666666, 0.8, 0.6666666666666666, 0.4, 1.0, 1.0, 0.33333333333333337 ]
- Mean = 0.6916666666666667
- Standard deviation = 0.22836982676741202

### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 40 | 8 |
| Actual Positive | 3 | 9 |

      