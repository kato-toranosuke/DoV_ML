# ExtraTreesClassifier_RandomOverSampler_2022-01-19-17-52_no3
## Constants
- CSV_PATH = ../out/csv/experiment
- OUTPUT_PATH = ../out/experiment_result/data_of_2022-01-13_eval_system/AGC-45angle-under5m
- FEATURE_ATTRBS = ['low_power', 'high_power', 'hlbr', 'coe1[0]', 'coe1[1]', 'coe3[0]', 'coe3[1]', 'coe3[2]', 'coe3[3]', 'ratio_max_to_10ms_ave_peaks', 'ratio_max_to_9th_ave_peaks', 'ac_std', 'ac_auc', 'diff_std', 'diff_auc', 'srmr', 'gp_max_val_std', 'gp_max_val_range', 'gp_max_val_min', 'gp_max_val_max', 'gp_max_val_mean', 'gp_max_ix_std', 'gp_max_ix_range', 'gp_max_ix_min', 'gp_max_ix_max', 'gp_max_ix_mean', 'gp_auc_std', 'gp_auc_range', 'gp_auc_min', 'gp_auc_max', 'gp_auc_mean', 'tdoa_std', 'tdoa_range', 'tdoa_min', 'tdoa_max', 'tdoa_mean']
- LABEL_ATTRB = ['facing2']
- FACING_DOV_ANGLES = [1, 2]
- NCV = 8
- SCORING = ['accuracy', 'balanced_accuracy', 'f1']
- REFIT_SCORING = balanced_accuracy
- PARAM_GRID = [{'est__n_estimators': range(10, 400, 20), 'est__min_samples_split': [2, 5, 10], 'est__min_samples_leaf': [1, 5, 10], 'est__max_features': ['sqrt', 'log2', None], 'est__bootstrap': [False], 'est__n_jobs': [-1], 'est__random_state': [42], 'est__max_samples': [0.01, 0.5, 0.09]}, {'est__n_estimators': range(10, 400, 20), 'est__min_samples_split': [2, 5, 10], 'est__min_samples_leaf': [1, 5, 10], 'est__max_features': ['sqrt', 'log2', None], 'est__bootstrap': [True], 'est__oob_score': [True, False], 'est__n_jobs': [-1], 'est__random_state': [42], 'est__max_samples': [0.01, 0.5, 0.09]}]
- HP_SET_SESSION = ['trial1', 'trial21']
- TRAIN_SET_SESSION = None
- TEST_SET_SESSION = None
- DISTANCE = [1, 3, 5]
- AGC_STATUS = ['AGC']

## Loaded CSV
- 2021-12-27_AGC.csv
- 2022-01-10_NoAGC.csv
- 2022-01-13_raspi_48000Hz_w1_N2^12_overlap80.csv

## Estimator
### Type
- resampler = RandomOverSampler
- estimator = ExtraTreesClassifier

### Arguments for hyperparameter search
- resampler = RandomOverSampler
- estimator = ExtraTreesClassifier
- param_grid = 
	- {'est__n_estimators': range(10, 400, 20), 'est__min_samples_split': [2, 5, 10], 'est__min_samples_leaf': [1, 5, 10], 'est__max_features': ['sqrt', 'log2', None], 'est__bootstrap': [False], 'est__n_jobs': [-1], 'est__random_state': [42], 'est__max_samples': [0.01, 0.5, 0.09]}
	- {'est__n_estimators': range(10, 400, 20), 'est__min_samples_split': [2, 5, 10], 'est__min_samples_leaf': [1, 5, 10], 'est__max_features': ['sqrt', 'log2', None], 'est__bootstrap': [True], 'est__oob_score': [True, False], 'est__n_jobs': [-1], 'est__random_state': [42], 'est__max_samples': [0.01, 0.5, 0.09]}

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
 144 145 146 147 148 149 150 151 152 153 154 155 156 157 158 159 160 161
 162 163 164 165 166 167 168 169 170 171 172 173 174 175 176 177 178 179
 180 181 182 183 184 185 186 187 188 189 190 191 192 193 194 195 196 197
 198 199 200 201 202 203 204 205 206 207 208 209 210 211 212 213 214 215
 216 217 218 219 210 104 194  26 150 131  38 210]

- best_estimator
	- base_estimator = ExtraTreeClassifier()
	- n_estimators = 130
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
- gp_max_val_min = 0.08600796332434481
- gp_max_val_mean = 0.08305698167053903
- gp_auc_max = 0.07861300120030422
- gp_auc_min = 0.0767557288060228
- diff_auc = 0.07153319191602503
- gp_max_val_max = 0.06551760021289146
- diff_std = 0.06157928529522803
- high_power = 0.05459636523179142
- srmr = 0.047576633153683955
- gp_auc_mean = 0.047112516685450384
- hlbr = 0.04297418400488462
- tdoa_mean = 0.027703862715557817
- gp_max_ix_mean = 0.024747719729205947
- coe1[1] = 0.0218722540303385
- gp_max_ix_std = 0.019579340685438065
- gp_max_ix_min = 0.018143024993861997
- tdoa_min = 0.016449683821473077
- tdoa_std = 0.015543061743136459
- coe1[0] = 0.013766672922748007
- ratio_max_to_10ms_ave_peaks = 0.013666340439190882
- gp_auc_range = 0.011403662946676673
- gp_max_val_range = 0.010389865850665755
- gp_max_ix_range = 0.010109786188776003
- tdoa_range = 0.009591914616580152
- coe3[2] = 0.00942837517775911
- gp_max_val_std = 0.009287196699171888
- low_power = 0.00886189596537652
- ac_auc = 0.007818543876214362
- gp_auc_std = 0.007705535245172558
- ac_std = 0.007573100667489063
- coe3[3] = 0.006837218981082602
- gp_max_ix_max = 0.006178409783836733
- tdoa_max = 0.005263158575028389
- ratio_max_to_9th_ave_peaks = 0.002755922844053577
- coe3[0] = 0.0
- coe3[1] = 0.0

## Evaluation
cv = 8
### robot-1
#### accuracy
- Mean = 0.968683110367893
- Standard deviation = 0.009151929181979278
- Max = 0.9866220735785953
- 75% = 0.9740997770345596
- Median = 0.9666666666666667
- 25% = 0.9623745819397993
- Min = 0.9565217391304348

#### f1
- Mean = 0.9234436309232434
- Standard deviation = 0.021582878487135252
- Max = 0.9666666666666667
- 75% = 0.937150093308451
- Median = 0.9166435120866907
- 25% = 0.9068627450980391
- Min = 0.8976377952755905

#### precision
- Mean = 0.9089050068707891
- Standard deviation = 0.03533546350175229
- Max = 0.9666666666666667
- 75% = 0.9318824194460147
- Median = 0.9107521186440678
- 25% = 0.8933284457478006
- Min = 0.8507462686567164

#### recall
- Mean = 0.9395833333333333
- Standard deviation = 0.024913043214794567
- Max = 0.9666666666666667
- 75% = 0.9541666666666666
- Median = 0.95
- 25% = 0.925
- Min = 0.9

#### facing_probas
- Mean = [0.96463141 0.78230769 0.12769231 0.00216346 0.00198718]
- Standard deviation = [0.01265509 0.03851044 0.01910579 0.00148607 0.000991  ]
- Max = [0.97551282 0.83692308 0.15346154 0.00512821 0.00346154]
- 75% = [0.97320513 0.81275641 0.14570513 0.00320513 0.00288462]
- Median = [0.96814103 0.78455128 0.12570513 0.00173077 0.00173077]
- 25% = [9.63044872e-01 7.64358974e-01 1.11538462e-01 8.97435897e-04
 1.41025641e-03]
- Min = [9.33589744e-01 7.19615385e-01 9.97435897e-02 5.12820513e-04
 2.56410256e-04]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 233.625 | 5.75 |
| Actual Positive | 3.625 | 56.375 |

### robot-2
#### accuracy
- Mean = 0.9594941471571906
- Standard deviation = 0.007579244657688573
- Max = 0.9698996655518395
- 75% = 0.9666666666666667
- Median = 0.959938684503902
- 25% = 0.9523411371237458
- Min = 0.9498327759197325

#### f1
- Mean = 0.8946937920548619
- Standard deviation = 0.020705195666725712
- Max = 0.9217391304347826
- 75% = 0.9141583869082408
- Median = 0.8975520643039825
- 25% = 0.8741987179487178
- Min = 0.8648648648648648

#### precision
- Mean = 0.9328850066281318
- Standard deviation = 0.022635924666677177
- Max = 0.9636363636363636
- 75% = 0.9456980519480519
- Median = 0.9417420814479638
- 25% = 0.9228521332554062
- Min = 0.8947368421052632

#### recall
- Mean = 0.8604166666666666
- Standard deviation = 0.033268165463898554
- Max = 0.9
- 75% = 0.8833333333333333
- Median = 0.875
- 25% = 0.8416666666666667
- Min = 0.8

#### facing_probas
- Mean = [0.92637821 0.94346154 0.81967949 0.11177885 0.00586538]
- Standard deviation = [0.00808474 0.0105909  0.01944021 0.01825398 0.0025735 ]
- Max = [0.93794872 0.95782051 0.84115385 0.14025641 0.01076923]
- 75% = [0.93314103 0.95532051 0.8375     0.12291667 0.00663462]
- Median = [0.92551282 0.94038462 0.82442308 0.11224359 0.00532051]
- 25% = [0.9211859  0.935      0.80762821 0.1025641  0.00371795]
- Min = [0.91269231 0.92987179 0.78564103 0.07551282 0.00307692]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 235.625 | 3.75 |
| Actual Positive | 8.375 | 51.625 |

### robot-3
#### accuracy
- Mean = 0.9544941471571906
- Standard deviation = 0.008308698832869008
- Max = 0.9665551839464883
- 75% = 0.9607023411371238
- Median = 0.9550000000000001
- 25% = 0.9489966555183946
- Min = 0.94

#### f1
- Mean = 0.8712897103809537
- Standard deviation = 0.02666335517382865
- Max = 0.9090909090909091
- 75% = 0.8914373088685016
- Median = 0.8732146005995416
- 25% = 0.8543956043956044
- Min = 0.8235294117647058

#### precision
- Mean = 1.0
- Standard deviation = 0.0
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 1.0
- Min = 1.0

#### recall
- Mean = 0.7729166666666667
- Standard deviation = 0.04161455074049623
- Max = 0.8333333333333334
- 75% = 0.8041666666666667
- Median = 0.775
- 25% = 0.7458333333333333
- Min = 0.7

#### facing_probas
- Mean = [0.29655449 0.94046474 0.97008013 0.90107372 0.11900641]
- Standard deviation = [0.03134867 0.00780287 0.01334056 0.01273383 0.02172044]
- Max = [0.35397436 0.95602564 0.98525641 0.93       0.1675641 ]
- 75% = [0.31548077 0.94394231 0.97708333 0.90221154 0.12400641]
- Median = [0.29570513 0.93833333 0.97371795 0.89762821 0.11647436]
- 25% = [0.2775641  0.93583333 0.96762821 0.89407051 0.11028846]
- Min = [0.24641026 0.92935897 0.93782051 0.88538462 0.08974359]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 239.375 | 0.0 |
| Actual Positive | 13.625 | 46.375 |

### robot-4
#### accuracy
- Mean = 0.9323676142697882
- Standard deviation = 0.0103365359017942
- Max = 0.9498327759197325
- 75% = 0.9382859531772575
- Median = 0.9297658862876255
- 25% = 0.9289910813823857
- Min = 0.9133333333333333

#### f1
- Mean = 0.8271607340991856
- Standard deviation = 0.02730619230780994
- Max = 0.8717948717948718
- 75% = 0.8452748832195474
- Median = 0.8249878463782206
- 25% = 0.8132056759231004
- Min = 0.7758620689655172

#### precision
- Mean = 0.8385253991096207
- Standard deviation = 0.027171546404045933
- Max = 0.8793103448275862
- 75% = 0.8576388888888888
- Median = 0.837675644028103
- 25% = 0.8141129032258064
- Min = 0.8035714285714286

#### recall
- Mean = 0.8169844632768362
- Standard deviation = 0.038153751039183365
- Max = 0.864406779661017
- 75% = 0.848093220338983
- Median = 0.8305084745762712
- 25% = 0.7824152542372882
- Min = 0.75

#### facing_probas
- Mean = [0.01472132 0.15234979 0.91645046 0.97314591 0.73415852]
- Standard deviation = [0.01339423 0.01999238 0.01532491 0.00770129 0.02507275]
- Max = [0.04974359 0.17666232 0.94576923 0.98679487 0.76987179]
- 75% = [0.01170143 0.16863103 0.92868318 0.97721643 0.7577249 ]
- Median = [0.01082138 0.15544872 0.90986636 0.97356041 0.73559322]
- 25% = [0.00903846 0.14054759 0.9041395  0.97043677 0.70811875]
- Min = [0.00560626 0.11564537 0.9        0.96076923 0.70025641]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 230.625 | 9.375 |
| Actual Positive | 10.875 | 48.5 |

### robot-5
#### accuracy
- Mean = 0.9686872909698997
- Standard deviation = 0.005998984384554701
- Max = 0.9765886287625418
- 75% = 0.9740802675585285
- Median = 0.9683333333333333
- 25% = 0.9633026755852843
- Min = 0.959866220735786

#### f1
- Mean = 0.9149676847218862
- Standard deviation = 0.017627608138684202
- Max = 0.9380530973451328
- 75% = 0.9309418457648546
- Median = 0.914004914004914
- 25% = 0.8990825688073394
- Min = 0.888888888888889

#### precision
- Mean = 1.0
- Standard deviation = 0.0
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 1.0
- Min = 1.0

#### recall
- Mean = 0.84375
- Standard deviation = 0.029973947020704484
- Max = 0.8833333333333333
- 75% = 0.8708333333333333
- Median = 0.8416666666666667
- 25% = 0.8166666666666667
- Min = 0.8

#### facing_probas
- Mean = [0.004375   0.00330128 0.23950321 0.95634615 0.95948718]
- Standard deviation = [0.00144684 0.00165771 0.02491203 0.00734891 0.00787419]
- Max = [0.00653846 0.00589744 0.27102564 0.96602564 0.97012821]
- 75% = [0.00535256 0.00461538 0.25522436 0.96266026 0.96557692]
- Median = [0.00448718 0.00307692 0.24262821 0.95698718 0.96032051]
- 25% = [0.00371795 0.00192308 0.22352564 0.95230769 0.9550641 ]
- Min = [0.00166667 0.00128205 0.19192308 0.94294872 0.94564103]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 239.375 | 0.0 |
| Actual Positive | 9.375 | 50.625 |

### robot-6
#### accuracy
- Mean = 0.8467739687848383
- Standard deviation = 0.016962495143347897
- Max = 0.8662207357859532
- 75% = 0.8590551839464883
- Median = 0.8464046822742475
- 25% = 0.8419732441471572
- Min = 0.81

#### f1
- Mean = 0.9169383059238022
- Standard deviation = 0.010031162199940016
- Max = 0.9283154121863798
- 75% = 0.9241793916462359
- Median = 0.9168097316917643
- 25% = 0.9142072265302755
- Min = 0.8950276243093923

#### precision
- Mean = 1.0
- Standard deviation = 0.0
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 1.0
- Min = 1.0

#### recall
- Mean = 0.8467739687848383
- Standard deviation = 0.016962495143347897
- Max = 0.8662207357859532
- 75% = 0.8590551839464883
- Median = 0.8464046822742475
- 25% = 0.8419732441471572
- Min = 0.81

#### facing_probas
- Mean = -100.0
- Standard deviation = 0.0
- Max = -100
- 75% = -100.0
- Median = -100.0
- 25% = -100.0
- Min = -100

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 0.0 | 0.0 |
| Actual Positive | 45.875 | 253.5 |

