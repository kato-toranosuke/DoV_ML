# ExtraTreesClassifier_RandomUnderSampler_2021-12-29_no2
## Constants
- CSV_PATH = ../out/csv/experiment
- OUTPUT_PATH = ../out/experiment_result/data_of_2021-12-27/NoAGC-45angle-under5m
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
- 2021-12-27_raspi_48000Hz_w1_N2^12_overlap80_new.csv

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
	- sampling_strategy_ = OrderedDict([(1, 54)])
	- sample_indices_ = [  4   5   6   7   8   9  14  15  16  17  18  19  24  25  26  27  28  29
  36  37  38  39  46  47  48  49  56  57  58  59  60  61  68  69  70  71
  78  79  80  81  88  89  90  91  92  93 100 101 102 103 110 111 112 113
 104 116   0  85  11 117  34  30 119  62  65  21  77  31  66  51   3  35
  76  20  12  54  10  94  72  41 106 109 108  96  63  84 118  33  53  52
  50  87  23  64 115  86  73  55  83  95   1  43   2  99  75  67  98  45]

- best_estimator
	- base_estimator = ExtraTreeClassifier()
	- n_estimators = 200
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
	- min_samples_leaf = 1
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
- gp_max_val_mean = 0.08320596604293104
- gp_max_val_min = 0.08210170227443818
- gp_auc_min = 0.07501019409039301
- gp_auc_mean = 0.06119819230558544
- srmr = 0.061107070701929694
- gp_auc_max = 0.05818046374615756
- gp_max_val_max = 0.05524015573302474
- diff_std = 0.04190282443288769
- hlbr = 0.04159640113339165
- diff_auc = 0.04088665572027894
- high_power = 0.03679309269093398
- gp_max_ix_max = 0.028863420976376494
- coe1[1] = 0.024441344661092677
- tdoa_mean = 0.023110039085988916
- tdoa_max = 0.022550302061997173
- gp_max_ix_mean = 0.020088784169969075
- gp_max_ix_std = 0.020031366995903993
- tdoa_std = 0.019379465728619462
- tdoa_range = 0.019028498216468678
- gp_max_ix_range = 0.01829135327126178
- coe1[0] = 0.01788411950981828
- ratio_max_to_10ms_ave_peaks = 0.01694269836725133
- gp_max_val_std = 0.014636057927378836
- tdoa_min = 0.014506601551756064
- gp_max_val_range = 0.014303859251355697
- gp_auc_std = 0.0130817360489957
- gp_max_ix_min = 0.012650452842850646
- low_power = 0.012596824114541829
- coe3[3] = 0.011116741810346309
- gp_auc_range = 0.010767750999094647
- coe3[2] = 0.01069077558906628
- ac_auc = 0.006920134996879435
- ac_std = 0.006140557415597273
- ratio_max_to_9th_ave_peaks = 0.004754395535437552
- coe3[0] = 0.0
- coe3[1] = 0.0

## Evaluation
cv = 8
### accuracy
- Scores = [ 0.9130434782608695, 1.0, 0.9565217391304348, 0.9090909090909091, 1.0, 0.9090909090909091, 1.0, 0.9545454545454546 ]
- Mean = 0.9552865612648221
- Standard deviation = 0.038814469491621054

### balanced_accuracy
- Scores = [ 0.9, 1.0, 0.9583333333333333, 0.9083333333333333, 1.0, 0.9083333333333333, 1.0, 0.9583333333333333 ]
- Mean = 0.9541666666666666
- Standard deviation = 0.04103690750748377

### f1
- Scores = [ 0.9285714285714286, 1.0, 0.9565217391304348, 0.9166666666666666, 1.0, 0.9166666666666666, 1.0, 0.9565217391304348 ]
- Mean = 0.959368530020704
- Standard deviation = 0.0345765766456713

### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 77 | 4 |
| Actual Positive | 4 | 94 |

      