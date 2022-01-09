# ExtraTreesClassifier_RandomUnderSampler_2022-01-09_no2
## Constants
- CSV_PATH = ../out/csv/experiment
- OUTPUT_PATH = ../out/experiment_result/data_of_2022-01-07_new/AGC-0angle-under5m
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
	- sampling_strategy_ = OrderedDict([(0, 30)])
	- sample_indices_ = [ 56  59   6  69  34  80  91  14  50 133  24  78  15  46 111 113 135   2
 110 130  81  57  39  88  54  16  19 142  94 121   0   1  10  11  20  21
  32  33  42  43  52  53  64  65  74  75  84  85  96  97 106 107 116 117
 128 129 138 139 148 149]

- best_estimator
	- base_estimator = ExtraTreeClassifier()
	- n_estimators = 150
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
- diff_auc = 0.12868285421151604
- diff_std = 0.10083480878803758
- gp_max_val_min = 0.08895853238810938
- gp_auc_mean = 0.08114392401058565
- gp_auc_max = 0.06823234987561445
- gp_max_val_mean = 0.06698591797927317
- gp_max_val_max = 0.06474370374757608
- gp_auc_min = 0.06314508627223454
- hlbr = 0.054893076143917315
- coe1[1] = 0.04892793396270001
- high_power = 0.04300201791845712
- srmr = 0.03379202256431306
- coe1[0] = 0.02040883262408399
- ratio_max_to_10ms_ave_peaks = 0.020158356730917062
- ratio_max_to_9th_ave_peaks = 0.01703409271357985
- coe3[3] = 0.012477260499912048
- low_power = 0.011570496812235003
- ac_std = 0.009360128626749668
- gp_auc_std = 0.00794194981075168
- tdoa_range = 0.007496319579953061
- coe3[2] = 0.006863192452153313
- gp_max_val_std = 0.006202458778827378
- gp_auc_range = 0.006197419096270406
- tdoa_min = 0.0058070597831671854
- gp_max_ix_range = 0.0052969999102787544
- gp_max_val_range = 0.0043860325713373964
- ac_auc = 0.004169408687910959
- gp_max_ix_min = 0.003332475165381845
- tdoa_std = 0.0024448391171491314
- gp_max_ix_mean = 0.0016821593757895385
- tdoa_max = 0.0014997513515007108
- tdoa_mean = 0.0008361551836870963
- gp_max_ix_max = 0.0007534274427361834
- gp_max_ix_std = 0.0007389558232931725
- coe3[0] = 0.0
- coe3[1] = 0.0

## Evaluation
cv = 8
### accuracy
- Scores = [ 0.7241379310344828, 0.75, 0.7857142857142857, 0.7857142857142857, 0.8928571428571429, 0.6071428571428571, 0.9642857142857143, 0.8571428571428571 ]
- Mean = 0.7958743842364532
- Standard deviation = 0.10283389500855021

### balanced_accuracy
- Scores = [ 0.7644927536231885, 0.8409090909090908, 0.6818181818181819, 0.803030303030303, 0.9318181818181819, 0.7608695652173914, 0.9, 0.9130434782608696 ]
- Mean = 0.8244976943346509
- Standard deviation = 0.0820025905758613

### f1
- Scores = [ 0.5555555555555556, 0.631578947368421, 0.5, 0.625, 0.8, 0.47619047619047616, 0.888888888888889, 0.7142857142857143 ]
- Mean = 0.648937447786132
- Standard deviation = 0.1352245174660939

### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 133 | 47 |
| Actual Positive | 4 | 41 |

      