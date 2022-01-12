# ExtraTreesClassifier_NoResampler_2022-01-10_no0
## Constants
- CSV_PATH = ../out/csv/experiment
- OUTPUT_PATH = ../out/experiment_result/data_of_2022-01-10/NoAGC-45angle-under5m
- FEATURE_ATTRBS = ['low_power', 'high_power', 'hlbr', 'coe1[0]', 'coe1[1]', 'coe3[0]', 'coe3[1]', 'coe3[2]', 'coe3[3]', 'ratio_max_to_10ms_ave_peaks', 'ratio_max_to_9th_ave_peaks', 'ac_std', 'ac_auc', 'diff_std', 'diff_auc', 'srmr', 'gp_max_val_std', 'gp_max_val_range', 'gp_max_val_min', 'gp_max_val_max', 'gp_max_val_mean', 'gp_max_ix_std', 'gp_max_ix_range', 'gp_max_ix_min', 'gp_max_ix_max', 'gp_max_ix_mean', 'gp_auc_std', 'gp_auc_range', 'gp_auc_min', 'gp_auc_max', 'gp_auc_mean', 'tdoa_std', 'tdoa_range', 'tdoa_min', 'tdoa_max', 'tdoa_mean']
- LABEL_ATTRB = ['facing2']
- FACING_DOV_ANGLES = [1, 2]
- NCV = 8
- SCORING = ['accuracy', 'balanced_accuracy', 'f1']
- REFIT_SCORING = balanced_accuracy
- PARAM_GRID = [{'est__n_estimators': [50, 100, 150, 200, 300], 'est__min_samples_split': [2, 5, 10], 'est__min_samples_leaf': [1, 5, 10], 'est__max_features': ['sqrt', 'log2', None], 'est__bootstrap': [False], 'est__n_jobs': [-1], 'est__random_state': [42], 'est__max_samples': [0.01, 0.5, 0.09]}, {'est__n_estimators': [50, 100, 150, 200, 300], 'est__min_samples_split': [2, 5, 10], 'est__min_samples_leaf': [1, 5, 10], 'est__max_features': ['sqrt', 'log2', None], 'est__bootstrap': [True], 'est__oob_score': [True, False], 'est__n_jobs': [-1], 'est__random_state': [42], 'est__max_samples': [0.01, 0.5, 0.09]}]
- TRAIN_SET_SESSION = ['trial1', 'trial2']
- TEST_SET_SESSION = ['trial3', 'trial4', 'trial5']
- DISTANCE = [1, 3, 5]
- AGC_STATUS = ['NoAGC']

## Loaded CSV
- 2022-01-10_raspi_48000Hz_w1_N2^12_overlap80.csv

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
	- n_estimators = 200
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
	- min_samples_split = 10
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
- gp_max_val_mean = 0.12556187849107825
- gp_max_val_min = 0.1054305614062089
- gp_auc_min = 0.10455518952619189
- gp_max_val_max = 0.09836724956310507
- gp_auc_max = 0.07959148092647739
- gp_auc_mean = 0.0736824373929433
- gp_max_ix_mean = 0.04096475857305814
- tdoa_mean = 0.03463854179113548
- srmr = 0.028751196343214085
- tdoa_min = 0.026903314679093796
- hlbr = 0.025446762171403972
- tdoa_std = 0.023091117150978405
- gp_max_ix_range = 0.023062741400160437
- gp_max_ix_std = 0.022378684968524146
- gp_max_ix_min = 0.021021892298935748
- gp_auc_std = 0.019227200040005214
- gp_max_val_std = 0.018019724257640268
- tdoa_range = 0.017621004504789473
- ratio_max_to_10ms_ave_peaks = 0.01670929591676936
- high_power = 0.013808090015925433
- gp_auc_range = 0.0125027721145157
- gp_max_val_range = 0.011635377865574868
- diff_std = 0.008870731647548879
- diff_auc = 0.00875853739109776
- tdoa_max = 0.006730343124766184
- gp_max_ix_max = 0.005175682326155034
- coe3[3] = 0.004090019370650807
- ac_auc = 0.003985533238028944
- coe3[2] = 0.003623906703753234
- ac_std = 0.0036097447033631115
- low_power = 0.003449460902236128
- coe1[1] = 0.003226642057185411
- coe1[0] = 0.0028486328021217933
- ratio_max_to_9th_ave_peaks = 0.002659494335363442
- coe3[0] = 0.0
- coe3[1] = 0.0

## Evaluation
cv = 8
### accuracy
- Scores = [ 0.896551724137931, 0.9642857142857143, 0.8571428571428571, 0.8571428571428571, 0.8214285714285714, 0.9642857142857143, 0.8571428571428571, 0.7857142857142857 ]
- Mean = 0.8754618226600985
- Standard deviation = 0.059377097342681255

### balanced_accuracy
- Scores = [ 0.8928571428571428, 0.9666666666666667, 0.8666666666666667, 0.8512820512820514, 0.8179487179487179, 0.9642857142857143, 0.8571428571428571, 0.7857142857142858 ]
- Mean = 0.8753205128205128
- Standard deviation = 0.06007331242180332

### f1
- Scores = [ 0.9090909090909091, 0.9655172413793104, 0.846153846153846, 0.8749999999999999, 0.8387096774193549, 0.9655172413793104, 0.8571428571428571, 0.75 ]
- Mean = 0.8758914715706985
- Standard deviation = 0.06674160990317254

### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 96 | 12 |
| Actual Positive | 13 | 104 |

      