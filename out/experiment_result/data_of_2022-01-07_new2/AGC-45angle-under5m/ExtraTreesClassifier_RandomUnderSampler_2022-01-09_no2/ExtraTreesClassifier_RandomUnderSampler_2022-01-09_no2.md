# ExtraTreesClassifier_RandomUnderSampler_2022-01-09_no2
## Constants
- CSV_PATH = ../out/csv/experiment
- OUTPUT_PATH = ../out/experiment_result/data_of_2022-01-07_new2/AGC-45angle-under5m
- FEATURE_ATTRBS = ['low_power', 'high_power', 'hlbr', 'coe1[0]', 'coe1[1]', 'coe3[0]', 'coe3[1]', 'coe3[2]', 'coe3[3]', 'ratio_max_to_10ms_ave_peaks', 'ratio_max_to_9th_ave_peaks', 'ac_std', 'ac_auc', 'diff_std', 'diff_auc', 'srmr', 'gp_max_val_std', 'gp_max_val_range', 'gp_max_val_min', 'gp_max_val_max', 'gp_max_val_mean', 'gp_max_ix_std', 'gp_max_ix_range', 'gp_max_ix_min', 'gp_max_ix_max', 'gp_max_ix_mean', 'gp_auc_std', 'gp_auc_range', 'gp_auc_min', 'gp_auc_max', 'gp_auc_mean', 'tdoa_std', 'tdoa_range', 'tdoa_min', 'tdoa_max', 'tdoa_mean']
- LABEL_ATTRB = ['facing2']
- FACING_DOV_ANGLES = [1, 2]
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
	- n_estimators = 35
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
- gp_auc_min = 0.09957909326602045
- gp_max_val_min = 0.09095102868509924
- gp_auc_max = 0.08773016258741631
- diff_auc = 0.07671246936827779
- gp_auc_mean = 0.07583250802067303
- gp_max_val_mean = 0.06686397257664801
- gp_max_val_max = 0.06043149534242433
- high_power = 0.05881531831459257
- diff_std = 0.042472912718145815
- coe1[0] = 0.03952937018615695
- coe1[1] = 0.030061068384446787
- srmr = 0.025796723525467708
- low_power = 0.0222017993197575
- ratio_max_to_10ms_ave_peaks = 0.021173886160273176
- tdoa_min = 0.019083030222345743
- tdoa_mean = 0.018885309415337347
- hlbr = 0.017745681472856017
- gp_max_ix_range = 0.013196395974061984
- gp_max_ix_std = 0.01208836742931145
- coe3[3] = 0.011747543021630882
- ac_auc = 0.011492738420491831
- gp_auc_std = 0.011046994572824247
- gp_max_ix_mean = 0.009655397201079162
- gp_auc_range = 0.00901810361345076
- tdoa_range = 0.008581769106079568
- ac_std = 0.008177972989033545
- gp_max_val_range = 0.00798548118805095
- tdoa_max = 0.00766633737983421
- tdoa_std = 0.007642417239325325
- gp_max_ix_min = 0.007324954923510286
- coe3[2] = 0.007030304345085817
- gp_max_ix_max = 0.005127617013286475
- gp_max_val_std = 0.00463007861083302
- ratio_max_to_9th_ave_peaks = 0.003721697406171655
- coe3[0] = 0.0
- coe3[1] = 0.0

## Evaluation
cv = 8
### accuracy
- Scores = [ 0.896551724137931, 0.9642857142857143, 0.9285714285714286, 0.9642857142857143, 0.8571428571428571, 1.0, 1.0, 1.0 ]
- Mean = 0.9513546798029557
- Standard deviation = 0.04978934731954077

### balanced_accuracy
- Scores = [ 0.8928571428571428, 0.9666666666666667, 0.9333333333333333, 0.9666666666666667, 0.8615384615384616, 1.0, 1.0, 1.0 ]
- Mean = 0.9526327838827839
- Standard deviation = 0.04920445970003251

### f1
- Scores = [ 0.9090909090909091, 0.9655172413793104, 0.9285714285714286, 0.9655172413793104, 0.8571428571428571, 1.0, 1.0, 1.0 ]
- Mean = 0.953229959695477
- Standard deviation = 0.04828728457762175

### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 104 | 4 |
| Actual Positive | 7 | 110 |

      