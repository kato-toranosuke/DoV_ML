# ExtraTreesClassifier_RandomUnderSampler_2022-01-10_no2
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
	- sampling_strategy_ = OrderedDict([(1, 72)])
	- sample_indices_ = [  4   5   6   7   8   9  14  15  16  17  18  19  24  25  26  27  28  29
  36  37  38  39  46  47  48  49  56  57  58  59  60  61  68  69  70  71
  78  79  80  81  88  89  90  91  92  93 100 101 102 103 110 111 112 113
 120 121 122 123 124 125 130 131 132 133 134 135 140 141 142 143 144 145
  65   0  66  30  22 149  62  10  95 126 115  44 138 104  40  84  63 108
  21  11  67  75 127  99  76  34  82  87  96  13  54 146  85 129  41 119
  51 105  31 106   3  35  74  20 116  12  72 147 118  86 148  33  53  77
  52  94  50  83 136 107  23  64 139 109 117 128  73  55   1  98  43   2]

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
	- min_samples_split = 2
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
- gp_max_val_mean = 0.1029358515031981
- gp_max_val_min = 0.09177482205667202
- gp_auc_min = 0.08003965119540205
- gp_max_val_max = 0.07746679317238495
- gp_auc_max = 0.07736207951584625
- gp_auc_mean = 0.0666652778569607
- srmr = 0.04116668283619403
- tdoa_mean = 0.0399512781669743
- gp_max_ix_mean = 0.031499720068411625
- gp_max_ix_std = 0.03126773893640173
- hlbr = 0.02963089937766238
- gp_max_ix_min = 0.02859121499998634
- gp_auc_std = 0.025057617754132788
- gp_max_ix_range = 0.022544833019653206
- tdoa_std = 0.02181007870232325
- gp_max_val_std = 0.021283896911493492
- tdoa_min = 0.021264420601049695
- tdoa_range = 0.021059953751947486
- ratio_max_to_10ms_ave_peaks = 0.01777116555302482
- gp_auc_range = 0.01616873157102433
- gp_max_val_range = 0.015626491981042896
- high_power = 0.013656637949090701
- diff_auc = 0.013114416290441794
- diff_std = 0.011936548285211509
- coe3[3] = 0.009982730596819858
- coe1[1] = 0.009405666515512815
- ac_std = 0.00871853021013227
- low_power = 0.008608201131851057
- tdoa_max = 0.007993713951775349
- coe3[2] = 0.007709114331627427
- ac_auc = 0.0072168142958583615
- gp_max_ix_max = 0.00713409172411058
- coe1[0] = 0.006891719658219268
- ratio_max_to_9th_ave_peaks = 0.006692615527562517
- coe3[0] = 0.0
- coe3[1] = 0.0

## Evaluation
cv = 8
### accuracy
- Scores = [ 0.896551724137931, 0.9285714285714286, 0.8214285714285714, 0.8928571428571429, 0.8214285714285714, 0.9642857142857143, 0.9285714285714286, 0.75 ]
- Mean = 0.8754618226600985
- Standard deviation = 0.06694977477111831

### balanced_accuracy
- Scores = [ 0.8928571428571428, 0.9333333333333333, 0.8282051282051281, 0.8897435897435897, 0.8179487179487179, 0.9642857142857143, 0.9285714285714286, 0.75 ]
- Mean = 0.8756181318681319
- Standard deviation = 0.0669397281290804

### f1
- Scores = [ 0.9090909090909091, 0.9285714285714286, 0.8148148148148148, 0.9032258064516129, 0.8387096774193549, 0.9655172413793104, 0.9285714285714286, 0.6956521739130435 ]
- Mean = 0.8730191850264878
- Standard deviation = 0.08136764626142987

### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 99 | 9 |
| Actual Positive | 15 | 102 |

      