# ExtraTreesClassifier_NoResampler_2021-12-29_no0
## Constants
- CSV_PATH = ../out/csv/experiment
- OUTPUT_PATH = ../out/experiment_result/data_of_2021-12-27/NoAGC-0angle-under5m
- FEATURE_ATTRBS = ['low_power', 'high_power', 'hlbr', 'coe1[0]', 'coe1[1]', 'coe3[0]', 'coe3[1]', 'coe3[2]', 'coe3[3]', 'ratio_max_to_10ms_ave_peaks', 'ratio_max_to_9th_ave_peaks', 'ac_std', 'ac_auc', 'diff_std', 'diff_auc', 'srmr', 'gp_max_val_std', 'gp_max_val_range', 'gp_max_val_min', 'gp_max_val_max', 'gp_max_val_mean', 'gp_max_ix_std', 'gp_max_ix_range', 'gp_max_ix_min', 'gp_max_ix_max', 'gp_max_ix_mean', 'gp_auc_std', 'gp_auc_range', 'gp_auc_min', 'gp_auc_max', 'gp_auc_mean', 'tdoa_std', 'tdoa_range', 'tdoa_min', 'tdoa_max', 'tdoa_mean']
- LABEL_ATTRB = ['facing']
- FACING_DOV_ANGLES = [1]
- NCV = 8
- SCORING = ['accuracy', 'balanced_accuracy', 'f1']
- REFIT_SCORING = balanced_accuracy
- PARAM_GRID = [{'est__n_estimators': [50, 100, 150, 200, 300], 'est__min_samples_split': [2, 5, 10], 'est__min_samples_leaf': [1, 5, 10], 'est__max_features': ['sqrt', 'log2', None], 'est__bootstrap': [False], 'est__n_jobs': [-1], 'est__random_state': [42], 'est__max_samples': [0.01, 0.5, 0.09]}, {'est__n_estimators': [50, 100, 150, 200, 300], 'est__min_samples_split': [2, 5, 10], 'est__min_samples_leaf': [1, 5, 10], 'est__max_features': ['sqrt', 'log2', None], 'est__bootstrap': [True], 'est__oob_score': [True, False], 'est__n_jobs': [-1], 'est__random_state': [42], 'est__max_samples': [0.01, 0.5, 0.09]}]
- TRAIN_SET_SESSION = ['trial1', 'trial2']
- TEST_SET_SESSION = ['trial3', 'trial4', 'trial5']
- DISTANCE = [1, 3, 5]
- AGC_STATUS = ['NoAGC']

## Loaded CSV
- 2021-12-27_raspi_48000Hz_w1_N2^12_overlap80_new.csv

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
	- n_estimators = 100
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
	- min_samples_leaf = 5
	- min_weight_fraction_leaf = 0.0
	- max_features = None
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
- gp_auc_min = 0.11437503293029117
- gp_max_val_min = 0.08022784723441939
- gp_max_val_max = 0.06365016865702632
- gp_auc_max = 0.05497186306422165
- coe1[1] = 0.05475658935941006
- hlbr = 0.04531370443256123
- srmr = 0.041045510340469764
- diff_auc = 0.04016007516927946
- gp_auc_mean = 0.03595860018552616
- diff_std = 0.035637460763432945
- coe1[0] = 0.03533557890987662
- high_power = 0.03479510064553996
- low_power = 0.03078479692646669
- gp_max_val_mean = 0.028834489835627995
- gp_max_ix_min = 0.028817681971581747
- ratio_max_to_9th_ave_peaks = 0.025562530500063227
- tdoa_range = 0.023506815567146896
- gp_auc_range = 0.02130268718431005
- gp_max_ix_mean = 0.019853433515153833
- gp_max_val_range = 0.017476722419671985
- gp_auc_std = 0.016362830193533198
- tdoa_min = 0.016169690867845234
- gp_max_ix_range = 0.015437676260448691
- gp_max_val_std = 0.014531178211480495
- coe3[3] = 0.013830849965374599
- ac_auc = 0.013127611371493186
- gp_max_ix_std = 0.01282446603192047
- tdoa_max = 0.012622410747169754
- ac_std = 0.011405259378676676
- tdoa_std = 0.010180365016203669
- coe3[2] = 0.009645986991800568
- ratio_max_to_10ms_ave_peaks = 0.007424480850074511
- gp_max_ix_max = 0.007389876772735286
- tdoa_mean = 0.006680627729166508
- coe3[0] = 0.0
- coe3[1] = 0.0

## Evaluation
cv = 8
### accuracy
- Scores = [ 0.8260869565217391, 0.782608695652174, 0.9130434782608695, 0.7727272727272727, 0.7272727272727273, 0.8636363636363636, 0.8181818181818182, 0.8181818181818182 ]
- Mean = 0.8152173913043479
- Standard deviation = 0.05321309097958994

### balanced_accuracy
- Scores = [ 0.6, 0.5722222222222222, 0.9444444444444444, 0.5, 0.6388888888888888, 0.625, 0.6944444444444444, 0.7916666666666667 ]
- Mean = 0.6708333333333333
- Standard deviation = 0.13089494892592682

### f1
- Scores = [ 0.33333333333333337, 0.28571428571428575, 0.8333333333333333, 0.0, 0.4, 0.4, 0.5, 0.6 ]
- Mean = 0.41904761904761906
- Standard deviation = 0.2270410074141212

### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 131 | 12 |
| Actual Positive | 21 | 15 |

      