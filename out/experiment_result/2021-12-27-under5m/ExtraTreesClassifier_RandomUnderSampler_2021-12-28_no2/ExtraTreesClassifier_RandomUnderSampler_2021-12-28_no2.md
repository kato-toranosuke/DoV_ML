# ExtraTreesClassifier_RandomUnderSampler_2021-12-28_no2
## Constants
- CSV_PATH = ../out/csv/experiment
- OUTPUT_PATH = ../out/experiment_result
- FEATURE_ATTRBS = ['low_power', 'high_power', 'hlbr', 'coe1[0]', 'coe1[1]', 'coe3[0]', 'coe3[1]', 'coe3[2]', 'coe3[3]', 'ratio_max_to_10ms_ave_peaks', 'ratio_max_to_9th_ave_peaks', 'ac_std', 'ac_auc', 'diff_std', 'diff_auc', 'srmr', 'gp_max_val_std', 'gp_max_val_range', 'gp_max_val_min', 'gp_max_val_max', 'gp_max_val_mean', 'gp_max_ix_std', 'gp_max_ix_range', 'gp_max_ix_min', 'gp_max_ix_max', 'gp_max_ix_mean', 'gp_auc_std', 'gp_auc_range', 'gp_auc_min', 'gp_auc_max', 'gp_auc_mean', 'tdoa_std', 'tdoa_range', 'tdoa_min', 'tdoa_max', 'tdoa_mean']
- LABEL_ATTRB = ['facing']
- FACING_DOV_ANGLES = [1]
- NCV = 8
- SCORING = ['accuracy', 'balanced_accuracy', 'f1']
- REFIT_SCORING = balanced_accuracy
- PARAM_GRID = [{'est__n_estimators': [50, 100, 150, 200, 300], 'est__min_samples_split': [2, 5, 10], 'est__min_samples_leaf': [1, 5, 10], 'est__max_features': ['sqrt', 'log2', None], 'est__bootstrap': [False], 'est__n_jobs': [-1], 'est__random_state': [42], 'est__max_samples': [0.01, 0.5, 0.09]}, {'est__n_estimators': [50, 100, 150, 200, 300], 'est__min_samples_split': [2, 5, 10], 'est__min_samples_leaf': [1, 5, 10], 'est__max_features': ['sqrt', 'log2', None], 'est__bootstrap': [True], 'est__oob_score': [True, False], 'est__n_jobs': [-1], 'est__random_state': [42], 'est__max_samples': [0.01, 0.5, 0.09]}]
- TRAIN_SET_SESSION = ['trial1', 'trial2']
- TEST_SET_SESSION = ['trial3', 'trial4', 'trial5']

## Loaded CSV
- 2021-12-27_raspi_48000Hz_w1_N2^12_overlap80_withfacing.csv

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
	- sample_indices_ = [ 70 111   6  57  34 144  87  14 112  91  24 139  15 120  54  39 110   2
 121 135  80  50 119  67  56  16  19  88 133  30   0   1  10  11  20  21
  32  33  42  43  52  53  64  65  74  75  84  85  96  97 106 107 116 117
 128 129 136 137 146 147]

- best_estimator
	- base_estimator = ExtraTreeClassifier()
	- n_estimators = 50
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
	- max_features = sqrt
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
- gp_auc_min = 0.15458866316725514
- gp_auc_max = 0.12502556908013304
- gp_max_val_min = 0.0933057584034274
- gp_max_val_max = 0.08013699129201096
- hlbr = 0.07102290958704312
- high_power = 0.07095080506196225
- gp_max_val_mean = 0.06915578331166525
- gp_auc_mean = 0.05126666175145373
- diff_auc = 0.03789090199332153
- coe1[1] = 0.03717909557038185
- coe1[0] = 0.03651680593629576
- low_power = 0.02557004584562598
- srmr = 0.023939011794203036
- diff_std = 0.02320300266258397
- coe3[2] = 0.01932545232204414
- coe3[3] = 0.015378406465192973
- tdoa_min = 0.012332182248123292
- gp_max_val_std = 0.011375208398364289
- gp_max_ix_min = 0.008011884824429544
- gp_max_ix_max = 0.005123180953772537
- gp_auc_std = 0.0049741542602608916
- gp_max_ix_range = 0.004328632049772834
- tdoa_max = 0.0043023634761306375
- tdoa_range = 0.003529936812638742
- gp_max_val_range = 0.0031673245736311096
- tdoa_std = 0.002274831266863427
- gp_max_ix_std = 0.0021200972354831855
- gp_auc_range = 0.001710180666237873
- tdoa_mean = 0.0009720071471113775
- ac_auc = 0.0009659774732525901
- ratio_max_to_9th_ave_peaks = 0.0003527256069628976
- ratio_max_to_10ms_ave_peaks = 3.4487623645960784e-06
- coe3[0] = 0.0
- coe3[1] = 0.0
- ac_std = 0.0
- gp_max_ix_mean = 0.0

## Evaluation
cv = 8
### accuracy
- Scores = [ 0.5714285714285714, 0.7857142857142857, 0.6428571428571429, 0.6785714285714286, 0.7857142857142857, 0.5357142857142857, 0.6428571428571429, 0.8214285714285714 ]
- Mean = 0.6830357142857143
- Standard deviation = 0.09851819861925852

### balanced_accuracy
- Scores = [ 0.606060606060606, 0.8636363636363636, 0.5909090909090908, 0.7954545454545454, 0.8636363636363636, 0.717391304347826, 0.7043478260869566, 0.7347826086956522 ]
- Mean = 0.7345273386034255
- Standard deviation = 0.09707266574206871

### f1
- Scores = [ 0.4, 0.6666666666666666, 0.37499999999999994, 0.5714285714285715, 0.6666666666666666, 0.4347826086956522, 0.4444444444444444, 0.5454545454545454 ]
- Mean = 0.5130554379195684
- Standard deviation = 0.1085845777964225

### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 116 | 63 |
| Actual Positive | 8 | 37 |

      