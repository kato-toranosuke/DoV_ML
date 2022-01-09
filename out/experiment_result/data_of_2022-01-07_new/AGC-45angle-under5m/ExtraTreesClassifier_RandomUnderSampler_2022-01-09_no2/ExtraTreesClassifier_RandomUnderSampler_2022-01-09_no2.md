# ExtraTreesClassifier_RandomUnderSampler_2022-01-09_no2
## Constants
- CSV_PATH = ../out/csv/experiment
- OUTPUT_PATH = ../out/experiment_result/data_of_2022-01-07_new/AGC-45angle-under5m
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
	- n_estimators = 50
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
- gp_auc_min = 0.10381555193524879
- gp_auc_max = 0.08019975034974998
- gp_max_val_min = 0.0793512805082418
- diff_auc = 0.0698170618342746
- gp_auc_mean = 0.06685990070220178
- high_power = 0.06579938252285615
- gp_max_val_max = 0.05761419060539792
- gp_max_val_mean = 0.04919938114934835
- diff_std = 0.044061772355267606
- srmr = 0.03453724052844186
- coe1[0] = 0.032944044244039974
- coe1[1] = 0.03086199956217182
- low_power = 0.028403422238562508
- hlbr = 0.02797060976645813
- coe3[3] = 0.018024758911519324
- ratio_max_to_10ms_ave_peaks = 0.01711090369817298
- tdoa_min = 0.016182406583826383
- gp_max_ix_range = 0.015153076741621587
- gp_max_ix_std = 0.0147943882521671
- ac_std = 0.014248985077281059
- tdoa_std = 0.013809256990682157
- ac_auc = 0.013592443846860657
- tdoa_mean = 0.012007662333099155
- gp_auc_std = 0.01190912853755273
- gp_auc_range = 0.010293306322611493
- gp_max_val_range = 0.010100396260876608
- gp_max_ix_mean = 0.0096814344406076
- coe3[2] = 0.009544868908502285
- gp_max_val_std = 0.00934820404491568
- gp_max_ix_min = 0.008313257701097037
- tdoa_range = 0.008050753372773124
- gp_max_ix_max = 0.006339723662253527
- tdoa_max = 0.006067390285506226
- ratio_max_to_9th_ave_peaks = 0.003992065725811854
- coe3[0] = 0.0
- coe3[1] = 0.0

## Evaluation
cv = 8
### accuracy
- Scores = [ 0.896551724137931, 0.9285714285714286, 0.8928571428571429, 0.9642857142857143, 0.8571428571428571, 1.0, 1.0, 1.0 ]
- Mean = 0.9424261083743843
- Standard deviation = 0.05297266739312184

### balanced_accuracy
- Scores = [ 0.8928571428571428, 0.9282051282051282, 0.9, 0.9666666666666667, 0.8615384615384616, 1.0, 1.0, 1.0 ]
- Mean = 0.943658424908425
- Standard deviation = 0.0518674024877707

### f1
- Scores = [ 0.9090909090909091, 0.9333333333333333, 0.888888888888889, 0.9655172413793104, 0.8571428571428571, 1.0, 1.0, 1.0 ]
- Mean = 0.9442466537294123
- Standard deviation = 0.052182762013860906

### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 105 | 3 |
| Actual Positive | 7 | 110 |

      