# ExtraTreesClassifier_RandomOverSampler_2022-01-10_no3
## Constants
- CSV_PATH = ../out/csv/experiment
- OUTPUT_PATH = ../out/experiment_result/data_of_2022-01-10/NoAGC-0angle-under5m
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
- AGC_STATUS = ['NoAGC']

## Loaded CSV
- 2022-01-10_raspi_48000Hz_w1_N2^12_overlap80.csv

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
	- n_estimators = 300
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
	- min_samples_leaf = 10
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
- gp_auc_min = 0.13090082871236858
- gp_max_val_max = 0.12041443751276389
- gp_auc_max = 0.11835084061997372
- gp_auc_mean = 0.11811731071354387
- gp_max_val_mean = 0.1125873484446657
- gp_max_val_min = 0.10559159329523067
- hlbr = 0.08247636800561271
- gp_auc_std = 0.027524159601022852
- gp_max_val_std = 0.025718839722020062
- tdoa_mean = 0.01666222415074222
- gp_max_ix_mean = 0.015225077158211723
- gp_max_ix_std = 0.013617890565126155
- tdoa_std = 0.013261474904810281
- gp_auc_range = 0.010709714506581581
- gp_max_val_range = 0.009462804428391463
- srmr = 0.008309036052461418
- high_power = 0.007938971912821039
- ratio_max_to_10ms_ave_peaks = 0.007620520271310833
- tdoa_max = 0.007499641410672476
- gp_max_ix_max = 0.007153068450256108
- coe3[3] = 0.005757640235278762
- diff_std = 0.005509022490907372
- coe1[1] = 0.0045798195101701255
- coe1[0] = 0.0037506354539038143
- tdoa_range = 0.0030629933406726368
- gp_max_ix_range = 0.0030501465934390723
- low_power = 0.0029388163218668027
- coe3[2] = 0.0026353817246735746
- diff_auc = 0.0023254847767057384
- ratio_max_to_9th_ave_peaks = 0.0015493211490652488
- ac_auc = 0.0015184328397009042
- ac_std = 0.0015023040063825803
- tdoa_min = 0.0014518929232559953
- gp_max_ix_min = 0.001225958195390105
- coe3[0] = 0.0
- coe3[1] = 0.0

## Evaluation
cv = 8
### accuracy
- Scores = [ 0.7931034482758621, 0.7857142857142857, 0.8214285714285714, 0.8214285714285714, 0.8571428571428571, 0.6071428571428571, 0.8571428571428571, 0.8214285714285714 ]
- Mean = 0.795566502463054
- Standard deviation = 0.0751635198013159

### balanced_accuracy
- Scores = [ 0.8695652173913043, 0.803030303030303, 0.7651515151515151, 0.8257575757575758, 0.8484848484848485, 0.6043478260869566, 0.8347826086956522, 0.5 ]
- Mean = 0.7563899868247694
- Standard deviation = 0.12417331102954468

### f1
- Scores = [ 0.6666666666666666, 0.625, 0.6153846153846153, 0.6666666666666667, 0.7142857142857143, 0.35294117647058826, 0.6666666666666666, 0.0 ]
- Mean = 0.5384514382676147
- Standard deviation = 0.22857944540323308

### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 153 | 27 |
| Actual Positive | 12 | 33 |

      