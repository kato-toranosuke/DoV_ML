# ExtraTreesClassifier_RandomOverSampler_2022-01-09_no3
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
- resampler = RandomOverSampler
- estimator = ExtraTreesClassifier

### Arguments for hyperparameter search
- resampler = RandomOverSampler
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
	- shrinkage = None
	- n_features_in_ = 36
	- sampling_strategy_ = OrderedDict([(1, 90)])
	- shrinkage_ = None
	- sample_indices_ = [  0   1   2   3   4   5   6   7   8   9  10  11  12  13  14  15  16  17
  18  19  20  21  22  23  24  25  26  27  28  29  30  31  32  33  34  35
  36  37  38  39  40  41  42  43  44  45  46  47  48  49  50  51  52  53
  54  55  56  57  58  59  60  61  62  63  64  65  66  67  68  69  70  71
  72  73  74  75  76  77  78  79  80  81  82  83  84  85  86  87  88  89
  90  91  92  93  94  95  96  97  98  99 100 101 102 103 104 105 106 107
 108 109 110 111 112 113 114 115 116 117 118 119 120 121 122 123 124 125
 126 127 128 129 130 131 132 133 134 135 136 137 138 139 140 141 142 143
 144 145 146 147 148 149  32  97 148  74  52  33 148 106  32 129  96 116
  52  52 117 106  11  33 117  10 107 106   1 117  53 149  21   1 139 106
   0  53 129 107 148  53 128  84 138 138  43 139 139  75  74 149 149  74
 149  96  53 116  97 128  10  20  96  32 106  42  32  85  11 128 139  65
  85 129  42 129 106   1  97 139  74 139  32  53 148  33  74  10  65  84
  11  85  33  11   1 149]

- best_estimator
	- base_estimator = ExtraTreeClassifier()
	- n_estimators = 310
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
	- min_samples_leaf = 5
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
- gp_auc_min = 0.09196031143947053
- gp_max_val_min = 0.08432009994997156
- gp_max_val_mean = 0.0682637784627049
- diff_auc = 0.06188644363768911
- high_power = 0.058940295947598885
- gp_auc_mean = 0.05740669902268575
- diff_std = 0.05725753466203682
- gp_auc_max = 0.05612952564497268
- gp_max_val_max = 0.053942166843564676
- hlbr = 0.03416718977460398
- coe1[1] = 0.03190324915989874
- srmr = 0.03174738249624247
- low_power = 0.02693094098721519
- coe1[0] = 0.022325390283507607
- coe3[3] = 0.017896924009896467
- gp_max_val_range = 0.01769341294901849
- ac_auc = 0.017150520553364135
- gp_auc_std = 0.01681955939466888
- ratio_max_to_10ms_ave_peaks = 0.016773812078772873
- gp_max_val_std = 0.016376078813392737
- ac_std = 0.015588987878765245
- tdoa_mean = 0.014704468929538115
- gp_max_ix_range = 0.014115740050936028
- ratio_max_to_9th_ave_peaks = 0.013596787976378094
- gp_max_ix_mean = 0.013442992127086387
- coe3[2] = 0.01330109443606023
- gp_auc_range = 0.01310259744641363
- tdoa_std = 0.011174662909562452
- gp_max_ix_min = 0.010341440737738962
- gp_max_ix_std = 0.009527473444801406
- tdoa_range = 0.009048107082504763
- tdoa_min = 0.008729820131279598
- tdoa_max = 0.00714927825093936
- gp_max_ix_max = 0.006285232486719111
- coe3[0] = 0.0
- coe3[1] = 0.0

## Evaluation
cv = 8
### accuracy
- Scores = [ 0.7241379310344828, 0.8214285714285714, 0.8571428571428571, 0.7857142857142857, 0.8571428571428571, 0.8214285714285714, 0.8214285714285714, 0.8214285714285714 ]
- Mean = 0.8137315270935961
- Standard deviation = 0.04002818286623213

### balanced_accuracy
- Scores = [ 0.7028985507246377, 0.8257575757575758, 0.7272727272727273, 0.6212121212121212, 0.8484848484848485, 0.8913043478260869, 0.6565217391304348, 0.7347826086956522 ]
- Mean = 0.7510293148880105
- Standard deviation = 0.08922448227129394

### f1
- Scores = [ 0.5, 0.6666666666666667, 0.6, 0.4, 0.7142857142857143, 0.6666666666666666, 0.4444444444444445, 0.5454545454545454 ]
- Mean = 0.5671897546897547
- Standard deviation = 0.10636655564362371

### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 152 | 28 |
| Actual Positive | 14 | 31 |

      