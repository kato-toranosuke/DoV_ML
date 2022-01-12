# ExtraTreesClassifier_SMOTETomek_2022-01-11_no6
## Constants
- CSV_PATH = ../out/csv/experiment
- OUTPUT_PATH = ../out/experiment_result/data_of_2022-01-10/NoAGC-45angle-under3m
- FEATURE_ATTRBS = ['low_power', 'high_power', 'hlbr', 'coe1[0]', 'coe1[1]', 'coe3[0]', 'coe3[1]', 'coe3[2]', 'coe3[3]', 'ratio_max_to_10ms_ave_peaks', 'ratio_max_to_9th_ave_peaks', 'ac_std', 'ac_auc', 'diff_std', 'diff_auc', 'srmr', 'gp_max_val_std', 'gp_max_val_range', 'gp_max_val_min', 'gp_max_val_max', 'gp_max_val_mean', 'gp_max_ix_std', 'gp_max_ix_range', 'gp_max_ix_min', 'gp_max_ix_max', 'gp_max_ix_mean', 'gp_auc_std', 'gp_auc_range', 'gp_auc_min', 'gp_auc_max', 'gp_auc_mean', 'tdoa_std', 'tdoa_range', 'tdoa_min', 'tdoa_max', 'tdoa_mean']
- LABEL_ATTRB = ['facing2']
- FACING_DOV_ANGLES = [1, 2]
- NCV = 8
- SCORING = ['accuracy', 'balanced_accuracy', 'f1']
- REFIT_SCORING = balanced_accuracy
- PARAM_GRID = [{'est__n_estimators': [50, 100, 150, 200, 300], 'est__min_samples_split': [2, 5, 10], 'est__min_samples_leaf': [1, 5, 10], 'est__max_features': ['sqrt', 'log2', None], 'est__bootstrap': [False], 'est__n_jobs': [-1], 'est__random_state': [42], 'est__max_samples': [0.01, 0.5, 0.09]}, {'est__n_estimators': [50, 100, 150, 200, 300], 'est__min_samples_split': [2, 5, 10], 'est__min_samples_leaf': [1, 5, 10], 'est__max_features': ['sqrt', 'log2', None], 'est__bootstrap': [True], 'est__oob_score': [True, False], 'est__n_jobs': [-1], 'est__random_state': [42], 'est__max_samples': [0.01, 0.5, 0.09]}]
- TRAIN_SET_SESSION = ['trial1', 'trial2']
- TEST_SET_SESSION = ['trial3', 'trial4', 'trial5']
- DISTANCE = [1, 3]
- AGC_STATUS = ['NoAGC']

## Loaded CSV
- 2022-01-10_raspi_48000Hz_w1_N2^12_overlap80.csv

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
	- max_features = None
	- max_leaf_nodes = None
	- min_impurity_decrease = 0.0
	- ccp_alpha = 0.0
	- n_features_in_ = 36
	- n_outputs_ = 1
	- classes_ = [0 1]
	- n_classes_ = 2
	- base_estimator_ = ExtraTreeClassifier()

#### Importance of features
- gp_max_val_min = 0.24203413808330496
- gp_auc_mean = 0.18880661582828273
- gp_auc_min = 0.14893554938612513
- gp_max_val_mean = 0.08867591548748968
- srmr = 0.08260933335538936
- ratio_max_to_10ms_ave_peaks = 0.05781435983971739
- gp_auc_max = 0.04969786738472413
- gp_max_val_max = 0.030319512810421893
- gp_auc_range = 0.012032807910149027
- gp_max_ix_std = 0.011465113318054495
- gp_max_ix_mean = 0.011120281501030166
- tdoa_std = 0.010067705060186262
- gp_max_val_range = 0.0076836875687731005
- gp_max_val_std = 0.006598825601597221
- tdoa_mean = 0.00645215104864902
- hlbr = 0.006116521689692424
- gp_max_ix_min = 0.005304301758847215
- gp_max_ix_range = 0.004825510746563381
- gp_auc_std = 0.0046473526473526485
- diff_auc = 0.0043434343434343445
- tdoa_min = 0.004215007215007216
- tdoa_range = 0.0029908765070055386
- ratio_max_to_9th_ave_peaks = 0.0020202020202020206
- tdoa_max = 0.0019671717171717167
- high_power = 0.001943722943722944
- diff_std = 0.0018181818181818182
- coe3[3] = 0.0013311688311688312
- coe1[1] = 0.0013169286853497385
- ac_std = 0.0009927849927849923
- gp_max_ix_max = 0.0007177603098655721
- ac_auc = 0.0007052341597796145
- low_power = 0.0004299754299754309
- coe1[0] = 0.0
- coe3[0] = 0.0
- coe3[1] = 0.0
- coe3[2] = 0.0

## Evaluation
cv = 8
### accuracy
- Scores = [ 0.9473684210526315, 1.0, 1.0, 0.8947368421052632, 1.0, 0.8947368421052632, 0.8888888888888888, 1.0 ]
- Mean = 0.9532163742690059
- Standard deviation = 0.04970760233918129

### balanced_accuracy
- Scores = [ 0.9444444444444444, 1.0, 1.0, 0.9, 1.0, 0.8888888888888888, 0.8888888888888888, 1.0 ]
- Mean = 0.9527777777777777
- Standard deviation = 0.04992277987669842

### f1
- Scores = [ 0.9523809523809523, 1.0, 1.0, 0.888888888888889, 1.0, 0.9090909090909091, 0.9, 1.0 ]
- Mean = 0.9562950937950938
- Standard deviation = 0.046899846624710514

### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 69 | 3 |
| Actual Positive | 2 | 76 |

      