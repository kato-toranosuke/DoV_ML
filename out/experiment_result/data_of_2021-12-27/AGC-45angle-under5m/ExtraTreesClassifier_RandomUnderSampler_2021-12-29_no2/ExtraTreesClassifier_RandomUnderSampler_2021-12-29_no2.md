# ExtraTreesClassifier_RandomUnderSampler_2021-12-29_no2
## Constants
- CSV_PATH = ../out/csv/experiment
- OUTPUT_PATH = ../out/experiment_result/data_of_2021-12-27/AGC-45angle-under5m
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
- AGC_STATUS = ['AGC']

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
	- sampling_strategy_ = OrderedDict([(1, 70)])
	- sample_indices_ = [  4   5   6   7   8   9  14  15  16  17  18  19  24  25  26  27  28  29
  36  37  38  39  46  47  48  49  56  57  58  59  60  61  68  69  70  71
  78  79  80  81  88  89  90  91  92  93 100 101 102 103 110 111 112 113
 120 121 122 123 124 125 130 131 132 133 138 139 140 141 142 143  65   0
  66  30  22 147  62  10  95 126 115  44 136 104  40  84  63 108  21  11
  67  75 127  99  76  34  82  87  96  13  54 144  85 129  41 119  51 105
  31 106   3  35  74  20 116  12  72 145 118  86 146  33  53  77  52  94
  50  83 134 107  23  64 137 109 117 128  73  55   1  98]

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
- gp_auc_min = 0.10454561176379823
- diff_auc = 0.0830639246781067
- gp_max_val_min = 0.06969425925858624
- gp_auc_max = 0.06715553372609202
- gp_auc_mean = 0.05951417747631502
- diff_std = 0.05765859184017774
- gp_max_val_mean = 0.05502962054864633
- gp_max_val_max = 0.05402010491122141
- high_power = 0.04848023013246314
- coe1[1] = 0.04460593912089753
- srmr = 0.043383389660285286
- coe1[0] = 0.0417199227058709
- low_power = 0.028632758441653486
- hlbr = 0.022228784502115073
- ac_auc = 0.02075401964628194
- ac_std = 0.017280210390092168
- ratio_max_to_10ms_ave_peaks = 0.01664374390323214
- gp_max_ix_mean = 0.014372761192911102
- gp_max_val_std = 0.01417963365942616
- tdoa_min = 0.013207021440663238
- gp_max_val_range = 0.011445589505234667
- tdoa_std = 0.011220198633957875
- gp_max_ix_std = 0.010352594091063143
- gp_auc_range = 0.010315283843692626
- tdoa_mean = 0.010292561440354276
- coe3[2] = 0.010194564922304037
- tdoa_range = 0.008600321836516307
- ratio_max_to_9th_ave_peaks = 0.00857392837517782
- gp_max_ix_max = 0.008429105816335767
- coe3[3] = 0.008114877364997603
- gp_max_ix_min = 0.007258921369705321
- gp_auc_std = 0.007224113899636488
- gp_max_ix_range = 0.006674148437118843
- tdoa_max = 0.005133551465069313
- coe3[0] = 0.0
- coe3[1] = 0.0

## Evaluation
cv = 8
### accuracy
- Scores = [ 0.8928571428571429, 0.9642857142857143, 0.8214285714285714, 0.9642857142857143, 0.8928571428571429, 0.9642857142857143, 1.0, 0.9642857142857143 ]
- Mean = 0.9330357142857143
- Standard deviation = 0.05485806128323441

### balanced_accuracy
- Scores = [ 0.8846153846153846, 0.9666666666666667, 0.8282051282051281, 0.9666666666666667, 0.9, 0.9642857142857143, 1.0, 0.9642857142857143 ]
- Mean = 0.9343406593406594
- Standard deviation = 0.0537484161932968

### f1
- Scores = [ 0.9090909090909091, 0.9655172413793104, 0.8148148148148148, 0.9655172413793104, 0.888888888888889, 0.962962962962963, 1.0, 0.962962962962963 ]
- Mean = 0.9337193776848949
- Standard deviation = 0.055767747161402294

### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 103 | 4 |
| Actual Positive | 11 | 106 |

      