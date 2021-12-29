# ExtraTreesClassifier_RandomOverSampler_2021-12-29_no3
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
- resampler = RandomOverSampler
- estimator = ExtraTreesClassifier

### Arguments for hyperparameter search
- resampler = RandomOverSampler
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
	- shrinkage = None
	- n_features_in_ = 36
	- sampling_strategy_ = OrderedDict([(0, 8)])
	- shrinkage_ = None
	- sample_indices_ = [  0   1   2   3   4   5   6   7   8   9  10  11  12  13  14  15  16  17
  18  19  20  21  22  23  24  25  26  27  28  29  30  31  32  33  34  35
  36  37  38  39  40  41  42  43  44  45  46  47  48  49  50  51  52  53
  54  55  56  57  58  59  60  61  62  63  64  65  66  67  68  69  70  71
  72  73  74  75  76  77  78  79  80  81  82  83  84  85  86  87  88  89
  90  91  92  93  94  95  96  97  98  99 100 101 102 103 104 105 106 107
 108 109 110 111 112 113 114 115 116 117 118 119 120 121 122 123 124 125
 126 127 128 129 130 131 132 133 134 135 136 137 138 139 140 141 142 143
 144 145 146 147 111  26 130  38  47   6  39 112]

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
- gp_auc_min = 0.09831332102572904
- gp_max_val_min = 0.08071457894870643
- diff_auc = 0.07872622454293726
- gp_auc_max = 0.0694008312764117
- gp_auc_mean = 0.06688060901745115
- gp_max_val_mean = 0.06363859652678834
- diff_std = 0.05827320113718889
- gp_max_val_max = 0.05229479065834924
- high_power = 0.04662738474448945
- coe1[0] = 0.0377237146532078
- srmr = 0.03595511641516026
- coe1[1] = 0.032654323785795136
- low_power = 0.030204472107413807
- ac_std = 0.02434973659669425
- ac_auc = 0.022650978340734738
- ratio_max_to_10ms_ave_peaks = 0.02211431947745888
- hlbr = 0.021063413779469752
- gp_max_ix_mean = 0.012880208536887969
- gp_auc_range = 0.01255072603280587
- gp_max_val_range = 0.011955943368642717
- tdoa_std = 0.011914784075911454
- gp_max_ix_std = 0.01142364597701671
- coe3[3] = 0.010178972777154809
- coe3[2] = 0.010109997349106005
- gp_max_ix_min = 0.009303013305537722
- gp_auc_std = 0.009288496737619306
- gp_max_ix_range = 0.008826951900956101
- tdoa_mean = 0.008695161148790174
- gp_max_val_std = 0.008432369262746651
- gp_max_ix_max = 0.0073192986739876965
- ratio_max_to_9th_ave_peaks = 0.0067453332093008215
- tdoa_min = 0.00636057145491829
- tdoa_max = 0.006291526425159435
- tdoa_range = 0.0061373867294721276
- coe3[0] = 0.0
- coe3[1] = 0.0

## Evaluation
cv = 8
### accuracy
- Scores = [ 0.8928571428571429, 0.9285714285714286, 0.8928571428571429, 0.9642857142857143, 0.8928571428571429, 0.9642857142857143, 1.0, 0.9642857142857143 ]
- Mean = 0.9375
- Standard deviation = 0.03891874056732743

### balanced_accuracy
- Scores = [ 0.8846153846153846, 0.9282051282051282, 0.8948717948717949, 0.9666666666666667, 0.9, 0.9642857142857143, 1.0, 0.9642857142857143 ]
- Mean = 0.9378663003663004
- Standard deviation = 0.039206841040314

### f1
- Scores = [ 0.9090909090909091, 0.9333333333333333, 0.896551724137931, 0.9655172413793104, 0.888888888888889, 0.962962962962963, 1.0, 0.962962962962963 ]
- Mean = 0.9399135028445373
- Standard deviation = 0.03675183633047004

### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 102 | 5 |
| Actual Positive | 9 | 108 |

      