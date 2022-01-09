# ExtraTreesClassifier_RandomUnderSampler_2022-01-09_no2
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
- resampler = RandomUnderSampler
- estimator = ExtraTreesClassifier

### Arguments for hyperparameter search
- resampler = RandomUnderSampler
- estimator = ExtraTreesClassifier
- param_grid = 
	- {'est__n_estimators': range(10, 1000, 25), 'est__min_samples_split': [2, 5, 10], 'est__min_samples_leaf': [1, 5, 10], 'est__max_features': ['sqrt', 'log2', None], 'est__bootstrap': [False], 'est__n_jobs': [-1], 'est__random_state': [42], 'est__max_samples': [0.01, 0.5, 0.09]}

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
	- n_estimators = 10
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
	- max_features = log2
	- max_leaf_nodes = None
	- min_impurity_decrease = 0.0
	- ccp_alpha = 0.0
	- n_features_in_ = 36
	- n_outputs_ = 1
	- classes_ = [0 1]
	- n_classes_ = 2
	- base_estimator_ = ExtraTreeClassifier()

#### Importance of features
- gp_max_val_mean = 0.13159750108404558
- hlbr = 0.10835473432272547
- gp_max_val_max = 0.09769243399328296
- diff_auc = 0.09477429887509506
- gp_auc_min = 0.09026343118897653
- high_power = 0.07842766933832704
- gp_auc_mean = 0.05975341730034476
- gp_auc_max = 0.057473070401639716
- diff_std = 0.03854605982505468
- srmr = 0.030544790231393986
- coe3[3] = 0.028175146350812558
- gp_max_val_std = 0.026582686970420533
- gp_max_val_min = 0.022591502220509457
- low_power = 0.01664182767377034
- tdoa_min = 0.0163731417810492
- tdoa_range = 0.015083550355869344
- gp_max_ix_std = 0.013328135377862487
- gp_max_ix_range = 0.012929124298072543
- gp_max_val_range = 0.0120806724599952
- coe1[1] = 0.0118234978852229
- gp_auc_std = 0.010358697914675436
- tdoa_max = 0.004221955550200514
- ratio_max_to_10ms_ave_peaks = 0.0038549144854268568
- coe3[2] = 0.003478260869565218
- tdoa_std = 0.003417809811671695
- ac_std = 0.003244465794003442
- coe1[0] = 0.0032225579053373615
- ac_auc = 0.0023372287145242065
- gp_max_ix_max = 0.0022973067571902214
- ratio_max_to_9th_ave_peaks = 0.0005301102629346897
- coe3[0] = 0.0
- coe3[1] = 0.0
- gp_max_ix_min = 0.0
- gp_max_ix_mean = 0.0
- gp_auc_range = 0.0
- tdoa_mean = 0.0

## Evaluation
cv = 8
### accuracy
- Scores = [ 0.6896551724137931, 0.6428571428571429, 0.6785714285714286, 0.8214285714285714, 0.8214285714285714, 0.6785714285714286, 0.9285714285714286, 0.7142857142857143 ]
- Mean = 0.7469211822660098
- Standard deviation = 0.09261255697491784

### balanced_accuracy
- Scores = [ 0.7427536231884058, 0.7727272727272727, 0.6136363636363636, 0.8257575757575758, 0.8863636363636364, 0.8043478260869565, 0.9565217391304348, 0.6695652173913043 ]
- Mean = 0.7839591567852437
- Standard deviation = 0.10389129317611018

### f1
- Scores = [ 0.5263157894736842, 0.5454545454545454, 0.4, 0.6666666666666667, 0.7058823529411764, 0.5263157894736842, 0.8333333333333333, 0.42857142857142855 ]
- Mean = 0.5790674882393149
- Standard deviation = 0.1368467613060969

### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 134 | 46 |
| Actual Positive | 7 | 38 |

      