# ExtraTreesClassifier_RandomUnderSampler_2022-01-19-16-40_no2
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
- resampler = RandomUnderSampler
- estimator = ExtraTreesClassifier

### Arguments for hyperparameter search
- resampler = RandomUnderSampler
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
	- replacement = False
	- n_features_in_ = 36
	- sampling_strategy_ = OrderedDict([(1, 108)])
	- sample_indices_ = [  2   3   4   7   8   9  12  13  14  18  19  23  24  28  29  30  34  35
  39  40  44  45  46  50  51  55  56  60  61  62  65  66  67  70  71  72
  79  80  81  82  83  84  89  90  91  92  93  94  99 100 101 102 103 104
 111 112 113 114 121 122 123 124 131 132 133 134 135 136 143 144 145 146
 153 154 155 156 163 164 165 166 167 168 175 176 177 178 185 186 187 188
 195 196 197 198 199 200 205 206 207 208 209 210 215 216 217 218 219 220
  86  10 107  78  21 161 140 180  69  22  76  49 181 194  36   0 120 214
 148 191 130 171 223  25  31 137  58  47 110  42 213 127 152  57 141  95
  20  63 212 129  53  87 159  11 160 128  75  68  32 126  64 109  16  85
 138 149  52  37 179 184  48  17 182  97  26 203   6  33  74 172  15 170
 190 222 108  98 150  88 157 119 221 151 173  77 116  96 204 115 147  59
 211 117 125 183  73  54 193   1 106  41   5  43 189 169 201 142 162 158]

- best_estimator
	- base_estimator = ExtraTreeClassifier()
	- n_estimators = 90
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
- gp_max_val_mean = 0.0923760939424324
- gp_max_val_min = 0.07839467641038984
- gp_auc_min = 0.07745610459460613
- gp_auc_max = 0.07610828073889425
- gp_max_val_max = 0.07310378394132014
- gp_auc_mean = 0.060244689377252504
- diff_auc = 0.05628647232414064
- high_power = 0.051408976750363114
- srmr = 0.0425551662547603
- diff_std = 0.04222432535878746
- tdoa_mean = 0.03316426090317709
- gp_max_ix_mean = 0.030064588733779592
- hlbr = 0.027867972024284204
- gp_max_ix_min = 0.027448413743127315
- tdoa_min = 0.021294314715058698
- ratio_max_to_10ms_ave_peaks = 0.018985214597458593
- tdoa_std = 0.018036391459471775
- gp_max_val_std = 0.0176923646613236
- coe1[1] = 0.016212699120275197
- gp_max_ix_std = 0.015292931868377367
- gp_max_ix_range = 0.015127679273428117
- coe1[0] = 0.012259948952167078
- tdoa_range = 0.012216223544341407
- gp_auc_range = 0.012145579752900293
- gp_max_val_range = 0.011018536669056741
- gp_auc_std = 0.010940687697569163
- tdoa_max = 0.008446267341362898
- gp_max_ix_max = 0.007859070167559379
- low_power = 0.006874004799100925
- coe3[3] = 0.006569047784227547
- coe3[2] = 0.006127745851784761
- ac_std = 0.004837642913834188
- ratio_max_to_9th_ave_peaks = 0.0047034328426658716
- ac_auc = 0.004656410890721358
- coe3[0] = 0.0
- coe3[1] = 0.0

## Evaluation
cv = 8
### robot-1
#### accuracy
- Mean = 0.9674038461538462
- Standard deviation = 0.010412689628296938
- Max = 0.979933110367893
- 75% = 0.9749163879598662
- Median = 0.9682775919732441
- 25% = 0.9632107023411371
- Min = 0.9498327759197325

#### f1
- Mean = 0.9205599600536744
- Standard deviation = 0.025335586471002505
- Max = 0.9516129032258064
- 75% = 0.9385245901639345
- Median = 0.9231273776728324
- 25% = 0.9093579234972677
- Min = 0.8799999999999999

#### precision
- Mean = 0.9007809201611671
- Standard deviation = 0.027545596728831227
- Max = 0.9354838709677419
- 75% = 0.919984879032258
- Median = 0.9106292966684294
- 25% = 0.8821969696969697
- Min = 0.8461538461538461

#### recall
- Mean = 0.9416666666666667
- Standard deviation = 0.03004626062886658
- Max = 0.9833333333333333
- 75% = 0.9666666666666667
- Median = 0.9416666666666667
- 25% = 0.9291666666666667
- Min = 0.8833333333333333

#### facing_probas
- Mean = [0.97780093 0.78902778 0.13664352 0.00233796 0.00155093]
- Standard deviation = [0.00354817 0.02960267 0.02052789 0.00227548 0.00071084]
- Max = [0.98444444 0.83351852 0.16814815 0.00611111 0.00277778]
- 75% = [0.97925926 0.80231481 0.14884259 0.00393519 0.00208333]
- Median = [0.97842593 0.79277778 0.13462963 0.0012963  0.00148148]
- 25% = [9.76018519e-01 7.78750000e-01 1.26388889e-01 3.70370370e-04
 9.25925926e-04]
- Min = [9.72592593e-01 7.26666667e-01 9.96296296e-02 1.85185185e-04
 5.55555556e-04]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 232.875 | 6.25 |
| Actual Positive | 3.5 | 56.5 |

### robot-2
#### accuracy
- Mean = 0.960296822742475
- Standard deviation = 0.015464759961169517
- Max = 0.9732441471571907
- 75% = 0.9732441471571907
- Median = 0.9666053511705686
- 25% = 0.9540133779264215
- Min = 0.9331103678929766

#### f1
- Mean = 0.896586505165033
- Standard deviation = 0.04155033849861728
- Max = 0.9322033898305084
- 75% = 0.9301270417422868
- Median = 0.9151763269410328
- 25% = 0.8776074589127687
- Min = 0.8245614035087719

#### precision
- Mean = 0.9343465367261499
- Standard deviation = 0.03610897801402214
- Max = 0.9814814814814815
- 75% = 0.9622252747252747
- Median = 0.940239625949737
- 25% = 0.9190665342601787
- Min = 0.8703703703703703

#### recall
- Mean = 0.8625
- Standard deviation = 0.05187458165828638
- Max = 0.9166666666666666
- 75% = 0.9041666666666667
- Median = 0.8833333333333333
- 25% = 0.8208333333333333
- Min = 0.7833333333333333

#### facing_probas
- Mean = [0.91055556 0.93203704 0.81219907 0.10694444 0.005     ]
- Standard deviation = [0.03522585 0.02756664 0.03587619 0.02217491 0.00336278]
- Max = [0.94981481 0.96296296 0.86425926 0.15148148 0.01240741]
- 75% = [0.93509259 0.9575     0.83976852 0.11416667 0.00625   ]
- Median = [0.92537037 0.93935185 0.81935185 0.10537037 0.00453704]
- 25% = [0.88967593 0.91166667 0.77768519 0.09824074 0.00277778]
- Min = [0.83518519 0.88240741 0.75666667 0.07       0.00092593]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 235.5 | 3.625 |
| Actual Positive | 8.25 | 51.75 |

### robot-3
#### accuracy
- Mean = 0.9531967670011148
- Standard deviation = 0.015142872485512708
- Max = 0.9732441471571907
- 75% = 0.9607023411371238
- Median = 0.9549275362318841
- 25% = 0.9464882943143813
- Min = 0.9264214046822743

#### f1
- Mean = 0.8658263725728048
- Standard deviation = 0.04917095384619682
- Max = 0.9285714285714286
- 75% = 0.8910213618157544
- Median = 0.8732146005995416
- 25% = 0.8458274398868458
- Min = 0.7755102040816326

#### precision
- Mean = 1.0
- Standard deviation = 0.0
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 1.0
- Min = 1.0

#### recall
- Mean = 0.7666666666666666
- Standard deviation = 0.07546154281781182
- Max = 0.8666666666666667
- 75% = 0.8041666666666667
- Median = 0.775
- 25% = 0.7333333333333334
- Min = 0.6333333333333333

#### facing_probas
- Mean = [0.28407407 0.93986111 0.96659722 0.89108796 0.11835648]
- Standard deviation = [0.05248432 0.00974589 0.01451961 0.0148268  0.04393491]
- Max = [0.37388889 0.95888889 0.98796296 0.90925926 0.22037037]
- 75% = [0.30842593 0.94407407 0.97569444 0.90333333 0.12384259]
- Median = [0.2937963  0.93916667 0.97027778 0.89583333 0.10277778]
- 25% = [0.25296296 0.9325463  0.95523148 0.87689815 0.09282407]
- Min = [0.20407407 0.92555556 0.94462963 0.86833333 0.07722222]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 239.125 | 0.0 |
| Actual Positive | 14.0 | 46.0 |

### robot-4
#### accuracy
- Mean = 0.9356577480490524
- Standard deviation = 0.01846574467106871
- Max = 0.959866220735786
- 75% = 0.9473244147157192
- Median = 0.9414715719063546
- 25% = 0.9264994425863992
- Min = 0.9063545150501672

#### f1
- Mean = 0.8321819786330531
- Standard deviation = 0.047333320243130195
- Max = 0.8983050847457628
- 75% = 0.8628906857409423
- Median = 0.8499926286303996
- 25% = 0.8001572327044024
- Min = 0.7543859649122806

#### precision
- Mean = 0.8615303203278143
- Standard deviation = 0.058971471349397696
- Max = 0.94
- 75% = 0.9024522178146412
- Median = 0.877657935285054
- 25% = 0.8240740740740741
- Min = 0.7540983606557377

#### recall
- Mean = 0.8078036723163842
- Standard deviation = 0.06015091114871672
- Max = 0.8983050847457628
- 75% = 0.8516949152542372
- Median = 0.8135593220338984
- 25% = 0.7669491525423728
- Min = 0.7166666666666667

#### facing_probas
- Mean = [0.01384769 0.13732972 0.89441502 0.97619233 0.71834785]
- Standard deviation = [0.00904232 0.04533396 0.01821859 0.00719074 0.02138932]
- Max = [0.0354049  0.24237288 0.91388889 0.98436911 0.75762712]
- 75% = [0.01501883 0.15140144 0.9066855  0.98182439 0.73281544]
- Median = [0.01101695 0.1220339  0.90338983 0.97919021 0.71237445]
- 25% = [0.00843927 0.11384181 0.88352166 0.97099812 0.69868173]
- Min = [0.00433145 0.0905838  0.85951036 0.96346516 0.6960452 ]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 232.125 | 7.875 |
| Actual Positive | 11.375 | 47.75 |

### robot-5
#### accuracy
- Mean = 0.9732594760312152
- Standard deviation = 0.013261469301393474
- Max = 0.9899665551839465
- 75% = 0.9816053511705686
- Median = 0.9765886287625418
- 25% = 0.9657497212931996
- Min = 0.9464882943143813

#### f1
- Mean = 0.9275518210108512
- Standard deviation = 0.038294125432934444
- Max = 0.9743589743589743
- 75% = 0.9519056261343013
- Median = 0.9379699248120301
- 25% = 0.9065888240200166
- Min = 0.849056603773585

#### precision
- Mean = 0.9972826086956521
- Standard deviation = 0.007189541606153774
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 1.0
- Min = 0.9782608695652174

#### recall
- Mean = 0.86875
- Standard deviation = 0.062046969215980956
- Max = 0.95
- 75% = 0.9083333333333333
- Median = 0.8833333333333333
- 25% = 0.8291666666666667
- Min = 0.75

#### facing_probas
- Mean = [0.00402778 0.0037037  0.21453704 0.95597222 0.94263889]
- Standard deviation = [0.00103832 0.00194003 0.04331968 0.00822707 0.01757595]
- Max = [0.00574074 0.00666667 0.30148148 0.97166667 0.97462963]
- 75% = [0.00486111 0.00486111 0.22935185 0.96060185 0.95166667]
- Median = [0.00388889 0.00333333 0.20814815 0.95407407 0.94027778]
- 25% = [0.00310185 0.00203704 0.18532407 0.94962963 0.93361111]
- Min = [0.00277778 0.0012963  0.16203704 0.94555556 0.91185185]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 239.0 | 0.125 |
| Actual Positive | 7.875 | 52.125 |

### robot-6
#### accuracy
- Mean = 0.849569397993311
- Standard deviation = 0.0369785586225893
- Max = 0.8929765886287625
- 75% = 0.8745819397993311
- Median = 0.8561872909698997
- 25% = 0.8396070234113713
- Min = 0.7658862876254181

#### f1
- Mean = 0.9182243109647672
- Standard deviation = 0.022159246137373727
- Max = 0.9434628975265017
- 75% = 0.9330929079816979
- Median = 0.9225085302625471
- 25% = 0.9128013646326103
- Min = 0.8674242424242424

#### precision
- Mean = 1.0
- Standard deviation = 0.0
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 1.0
- Min = 1.0

#### recall
- Mean = 0.849569397993311
- Standard deviation = 0.0369785586225893
- Max = 0.8929765886287625
- 75% = 0.8745819397993311
- Median = 0.8561872909698997
- 25% = 0.8396070234113713
- Min = 0.7658862876254181

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
| Actual Positive | 45.0 | 254.125 |

