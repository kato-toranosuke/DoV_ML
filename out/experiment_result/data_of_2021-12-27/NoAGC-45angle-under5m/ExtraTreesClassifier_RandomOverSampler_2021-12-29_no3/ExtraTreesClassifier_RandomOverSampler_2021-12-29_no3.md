# ExtraTreesClassifier_RandomOverSampler_2021-12-29_no3
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
	- sampling_strategy_ = OrderedDict([(0, 12)])
	- shrinkage_ = None
	- sample_indices_ = [  0   1   2   3   4   5   6   7   8   9  10  11  12  13  14  15  16  17
  18  19  20  21  22  23  24  25  26  27  28  29  30  31  32  33  34  35
  36  37  38  39  40  41  42  43  44  45  46  47  48  49  50  51  52  53
  54  55  56  57  58  59  60  61  62  63  64  65  66  67  68  69  70  71
  72  73  74  75  76  77  78  79  80  81  82  83  84  85  86  87  88  89
  90  91  92  93  94  95  96  97  98  99 100 101 102 103 104 105 106 107
 108 109 110 111 112 113 114 115 116 117 118 119  80 111  58  26  90  15
  38  80  36  46  18  18]

- best_estimator
	- base_estimator = ExtraTreeClassifier()
	- n_estimators = 100
	- estimator_params = ('criterion', 'max_depth', 'min_samples_split', 'min_samples_leaf', 'min_weight_fraction_leaf', 'max_features', 'max_leaf_nodes', 'min_impurity_decrease', 'min_impurity_split', 'random_state', 'ccp_alpha')
	- bootstrap = True
	- oob_score = True
	- n_jobs = -1
	- random_state = 42
	- verbose = 0
	- warm_start = False
	- class_weight = None
	- max_samples = 0.5
	- criterion = gini
	- max_depth = None
	- min_samples_split = 5
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
	- oob_decision_function_ = [[0.02777778 0.97222222]
 [0.00564972 0.99435028]
 [0.01912568 0.98087432]
 [0.01092896 0.98907104]
 [0.45694444 0.54305556]
 [0.47705314 0.52294686]
 [0.955      0.045     ]
 [0.8637931  0.1362069 ]
 [0.89062736 0.10937264]
 [0.95833333 0.04166667]
 [0.0825     0.9175    ]
 [0.05318627 0.94681373]
 [0.19517544 0.80482456]
 [0.04454545 0.95545455]
 [0.79708995 0.20291005]
 [0.60730994 0.39269006]
 [0.99       0.01      ]
 [0.9978022  0.0021978 ]
 [1.         0.        ]
 [0.95238095 0.04761905]
 [0.28040293 0.71959707]
 [0.12711864 0.87288136]
 [0.12193878 0.87806122]
 [0.25145089 0.74854911]
 [0.84348958 0.15651042]
 [0.86129944 0.13870056]
 [1.         0.        ]
 [1.         0.        ]
 [1.         0.        ]
 [0.98591549 0.01408451]
 [0.04666667 0.95333333]
 [0.03393939 0.96606061]
 [0.01612903 0.98387097]
 [0.02298851 0.97701149]
 [0.20502646 0.79497354]
 [0.16909091 0.83090909]
 [0.80132275 0.19867725]
 [0.66783626 0.33216374]
 [0.98275862 0.01724138]
 [0.68390805 0.31609195]
 [0.20785256 0.79214744]
 [0.10357143 0.89642857]
 [0.11333333 0.88666667]
 [0.04651741 0.95348259]
 [0.28585859 0.71414141]
 [0.15992063 0.84007937]
 [0.75248756 0.24751244]
 [0.48258706 0.51741294]
 [0.99166667 0.00833333]
 [0.98181818 0.01818182]
 [0.5531746  0.4468254 ]
 [0.31958333 0.68041667]
 [0.23335351 0.76664649]
 [0.11032338 0.88967662]
 [0.46065934 0.53934066]
 [0.17586266 0.82413734]
 [0.92234127 0.07765873]
 [0.9454023  0.0545977 ]
 [0.98958333 0.01041667]
 [0.9875     0.0125    ]
 [0.6341954  0.3658046 ]
 [0.67083333 0.32916667]
 [0.12053571 0.87946429]
 [0.04296875 0.95703125]
 [0.0579096  0.9420904 ]
 [0.05944444 0.94055556]
 [0.19791667 0.80208333]
 [0.13737374 0.86262626]
 [0.63852459 0.36147541]
 [0.59016393 0.40983607]
 [0.36421131 0.63578869]
 [0.27963435 0.72036565]
 [0.37012472 0.62987528]
 [0.09751984 0.90248016]
 [0.17651515 0.82348485]
 [0.07604167 0.92395833]
 [0.05134409 0.94865591]
 [0.02674731 0.97325269]
 [0.52055556 0.47944444]
 [0.62894737 0.37105263]
 [0.92089947 0.07910053]
 [0.86293103 0.13706897]
 [0.26119792 0.73880208]
 [0.15146199 0.84853801]
 [0.10865079 0.89134921]
 [0.09352679 0.90647321]
 [0.18599206 0.81400794]
 [0.38111111 0.61888889]
 [0.91181818 0.08818182]
 [0.95185185 0.04814815]
 [0.92528736 0.07471264]
 [0.88472222 0.11527778]
 [0.69270833 0.30729167]
 [0.63111111 0.36888889]
 [0.09649123 0.90350877]
 [0.12727273 0.87272727]
 [0.06944444 0.93055556]
 [0.03191489 0.96808511]
 [0.16029412 0.83970588]
 [0.23022599 0.76977401]
 [0.98113208 0.01886792]
 [1.         0.        ]
 [0.87193878 0.12806122]
 [0.69770531 0.30229469]
 [0.04199134 0.95800866]
 [0.09150327 0.90849673]
 [0.09313725 0.90686275]
 [0.06215847 0.93784153]
 [0.08154762 0.91845238]
 [0.08928571 0.91071429]
 [0.98976608 0.01023392]
 [0.94093567 0.05906433]
 [0.87377112 0.12622888]
 [0.79290123 0.20709877]
 [0.42183288 0.57816712]
 [0.06721311 0.93278689]
 [0.05900298 0.94099702]
 [0.0319209  0.9680791 ]
 [0.04974937 0.95025063]
 [0.14021739 0.85978261]
 [0.93358209 0.06641791]
 [0.9479313  0.0520687 ]
 [1.         0.        ]
 [1.         0.        ]
 [0.93852459 0.06147541]
 [0.65273224 0.34726776]
 [0.97761194 0.02238806]
 [0.92724868 0.07275132]
 [0.81010101 0.18989899]
 [0.68926554 0.31073446]
 [1.         0.        ]
 [1.         0.        ]]
	- oob_score_ = 0.9545454545454546

#### Importance of features
- gp_max_val_mean = 0.10779128076734108
- gp_max_val_min = 0.08053731853170412
- gp_auc_min = 0.07829700437010569
- gp_auc_max = 0.06641298723622174
- gp_max_val_max = 0.06234715227977103
- gp_auc_mean = 0.04979368856164241
- srmr = 0.04688416283621019
- diff_auc = 0.04683702616398932
- high_power = 0.04481444555554548
- diff_std = 0.04249537672800147
- hlbr = 0.039228702710896284
- ratio_max_to_10ms_ave_peaks = 0.03252372417456553
- gp_max_ix_max = 0.028017469584903996
- gp_max_val_std = 0.022675889487710776
- tdoa_max = 0.022241736977592765
- tdoa_range = 0.01903200955711118
- tdoa_mean = 0.01892707401598129
- tdoa_std = 0.017132458046541576
- coe1[1] = 0.01692085504646318
- coe1[0] = 0.015081335063562995
- low_power = 0.014540433430663831
- gp_max_ix_mean = 0.014240699091860556
- gp_auc_std = 0.01368231807132575
- gp_max_ix_std = 0.012543366786261032
- gp_max_val_range = 0.011601310500579286
- gp_max_ix_range = 0.011481058285930358
- tdoa_min = 0.01128284624300391
- coe3[2] = 0.01015537455079824
- ac_std = 0.00885170190643751
- gp_max_ix_min = 0.008548381577061268
- coe3[3] = 0.008393270401637122
- gp_auc_range = 0.007711753366176279
- ac_auc = 0.005338868590407248
- ratio_max_to_9th_ave_peaks = 0.0036369195019955005
- coe3[0] = 0.0
- coe3[1] = 0.0

## Evaluation
cv = 8
### accuracy
- Scores = [ 0.9130434782608695, 1.0, 1.0, 0.9545454545454546, 0.9545454545454546, 0.8636363636363636, 1.0, 0.9545454545454546 ]
- Mean = 0.9550395256916997
- Standard deviation = 0.044976759418755945

### balanced_accuracy
- Scores = [ 0.9, 1.0, 1.0, 0.95, 0.95, 0.8583333333333334, 1.0, 0.9583333333333333 ]
- Mean = 0.9520833333333333
- Standard deviation = 0.04800716092417878

### f1
- Scores = [ 0.9285714285714286, 1.0, 1.0, 0.9600000000000001, 0.9600000000000001, 0.8799999999999999, 1.0, 0.9565217391304348 ]
- Mean = 0.9606366459627329
- Standard deviation = 0.0390458238100803

### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 75 | 6 |
| Actual Positive | 2 | 96 |

      