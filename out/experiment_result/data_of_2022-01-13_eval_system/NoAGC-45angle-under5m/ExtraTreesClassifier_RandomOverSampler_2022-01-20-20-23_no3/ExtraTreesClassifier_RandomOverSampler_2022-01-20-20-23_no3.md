# ExtraTreesClassifier_RandomOverSampler_2022-01-20-20-23_no3
## Constants
- CSV_PATH = ../out/csv/experiment
- OUTPUT_PATH = ../out/experiment_result/data_of_2022-01-13_eval_system/NoAGC-45angle-under5m
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
- AGC_STATUS = ['NoAGC']

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
	- sampling_strategy_ = OrderedDict([(0, 9)])
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
 216 217 218 219 220 221 222 223 224 215 102 197  29 219 146 123  44 215]

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
	- min_samples_split = 5
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
- gp_auc_min = 0.10605596168662247
- gp_auc_max = 0.077332635109062
- gp_max_val_mean = 0.07167670195484745
- gp_auc_mean = 0.0714676605156475
- gp_max_val_min = 0.07108546314816305
- srmr = 0.07061600779205363
- gp_max_val_max = 0.06562634096404904
- diff_std = 0.03419780556676874
- ratio_max_to_10ms_ave_peaks = 0.03297111875034804
- gp_max_ix_std = 0.0326566425375475
- hlbr = 0.026957983831397275
- tdoa_std = 0.025895091424798625
- gp_max_ix_min = 0.025037942523386977
- tdoa_mean = 0.022846601918103494
- gp_max_ix_mean = 0.022614767619089607
- tdoa_min = 0.022563422411589137
- gp_max_ix_range = 0.022101094595645035
- tdoa_range = 0.021257333470782215
- high_power = 0.017390704265321653
- tdoa_max = 0.01500172734291735
- diff_auc = 0.01322769291421511
- low_power = 0.013197695508091491
- gp_max_val_std = 0.013188361983626662
- coe1[0] = 0.012894079873788468
- gp_auc_std = 0.012658648242804757
- ac_auc = 0.010537771281059632
- gp_auc_range = 0.010434356571146951
- ac_std = 0.010381333042452912
- gp_max_ix_max = 0.010362474217751034
- gp_max_val_range = 0.009800632328671085
- coe1[1] = 0.008829468199344263
- coe3[3] = 0.007486380658037723
- coe3[2] = 0.007388171510469599
- ratio_max_to_9th_ave_peaks = 0.004259926240399519
- coe3[0] = 0.0
- coe3[1] = 0.0

## Evaluation
cv = 8
### robot-1
#### accuracy
- Mean = 0.9745833333333334
- Standard deviation = 0.0064415103473917995
- Max = 0.9866666666666667
- 75% = 0.9775
- Median = 0.9750000000000001
- 25% = 0.9691666666666666
- Min = 0.9666666666666667

#### f1
- Mean = 0.9357540731841743
- Standard deviation = 0.015995225902076724
- Max = 0.9666666666666667
- 75% = 0.9431704885343968
- Median = 0.9356669123065586
- 25% = 0.9224439775910364
- Min = 0.9166666666666666

#### precision
- Mean = 0.947120902183731
- Standard deviation = 0.02238101318616224
- Max = 0.9818181818181818
- 75% = 0.9658045977011495
- Median = 0.9487142022209234
- 25% = 0.928319209039548
- Min = 0.9166666666666666

#### recall
- Mean = 0.925
- Standard deviation = 0.018633899812498255
- Max = 0.9666666666666667
- 75% = 0.9333333333333333
- Median = 0.9166666666666666
- 25% = 0.9166666666666666
- Min = 0.9

#### facing_probas
- Mean = [0.93116667 0.77617014 0.112      0.00808333 0.00385069]
- Standard deviation = [0.02198887 0.01888573 0.04017917 0.00592847 0.00241363]
- Max = [0.96922222 0.80041667 0.18691667 0.02175    0.00694444]
- 75% = [0.9443125  0.78580556 0.13049306 0.01006944 0.00611111]
- Median = [0.93175    0.77941667 0.10005556 0.00623611 0.00395833]
- 25% = [0.9164375  0.76536806 0.07746528 0.00399306 0.00175   ]
- Min = [8.96944444e-01 7.38750000e-01 7.28611111e-02 2.25000000e-03
 3.33333333e-04]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 236.875 | 3.125 |
| Actual Positive | 4.5 | 55.5 |

### robot-2
#### accuracy
- Mean = 0.9366666666666666
- Standard deviation = 0.01972026594366539
- Max = 0.9666666666666667
- 75% = 0.9541666666666667
- Median = 0.9333333333333333
- 25% = 0.925
- Min = 0.9033333333333333

#### f1
- Mean = 0.822815047431023
- Standard deviation = 0.05732085752437883
- Max = 0.912280701754386
- 75% = 0.8752661752661753
- Median = 0.8113929684023142
- 25% = 0.7816315205327414
- Min = 0.7339449541284403

#### precision
- Mean = 0.9267760350105712
- Standard deviation = 0.04828597971016966
- Max = 0.9629629629629629
- 75% = 0.9601960784313726
- Median = 0.9539682539682539
- 25% = 0.9089962997224792
- Min = 0.8163265306122449

#### recall
- Mean = 0.7416666666666667
- Standard deviation = 0.07120003121097944
- Max = 0.8666666666666667
- 75% = 0.8041666666666667
- Median = 0.7166666666666667
- 25% = 0.6791666666666667
- Min = 0.6666666666666666

#### facing_probas
- Mean = [0.91665972 0.93187153 0.83532292 0.22956597 0.02168056]
- Standard deviation = [0.02556132 0.0260844  0.04415002 0.09590466 0.0125119 ]
- Max = [0.94533333 0.96858333 0.89827778 0.38094444 0.04630556]
- 75% = [0.94251389 0.95796528 0.87053472 0.29024306 0.02756944]
- Median = [0.92059722 0.92454167 0.831375   0.26186111 0.02165278]
- 25% = [0.88882639 0.91177778 0.79954167 0.1345625  0.01190278]
- Min = [0.88322222 0.8975     0.78097222 0.08591667 0.00555556]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 236.5 | 3.5 |
| Actual Positive | 15.5 | 44.5 |

### robot-3
#### accuracy
- Mean = 0.9241666666666666
- Standard deviation = 0.01630865482565077
- Max = 0.9433333333333334
- 75% = 0.935
- Median = 0.9283333333333333
- 25% = 0.9158333333333333
- Min = 0.89

#### f1
- Mean = 0.7659694609917291
- Standard deviation = 0.06486550254607505
- Max = 0.8440366972477065
- 75% = 0.8088235294117647
- Median = 0.7834040832827978
- 25% = 0.7334826427771556
- Min = 0.6292134831460675

#### precision
- Mean = 0.982084212995543
- Standard deviation = 0.02092690328567293
- Max = 1.0
- 75% = 1.0
- Median = 0.9880952380952381
- 25% = 0.9735221674876847
- Min = 0.9387755102040817

#### recall
- Mean = 0.6333333333333333
- Standard deviation = 0.08819171036881969
- Max = 0.7666666666666667
- 75% = 0.6875
- Median = 0.65
- 25% = 0.5791666666666667
- Min = 0.4666666666666667

#### facing_probas
- Mean = [0.32244444 0.87381597 0.91074653 0.78820486 0.21767014]
- Standard deviation = [0.06884503 0.03945897 0.03110429 0.05053076 0.05870613]
- Max = [0.43911111 0.91988889 0.95736111 0.84341667 0.31172222]
- 75% = [0.34761111 0.90139583 0.93582639 0.82822917 0.257625  ]
- Median = [0.31620833 0.88180556 0.91205556 0.80184722 0.21843056]
- 25% = [0.28695833 0.85847917 0.87951389 0.75646528 0.17275   ]
- Min = [0.22852778 0.79225    0.87419444 0.68391667 0.13755556]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 239.25 | 0.75 |
| Actual Positive | 22.0 | 38.0 |

### robot-4
#### accuracy
- Mean = 0.9004166666666666
- Standard deviation = 0.03634088224331135
- Max = 0.9433333333333334
- 75% = 0.9258333333333333
- Median = 0.9166666666666667
- 25% = 0.8691666666666666
- Min = 0.8333333333333334

#### f1
- Mean = 0.6914781166457433
- Standard deviation = 0.11919919917598097
- Max = 0.8349514563106796
- 75% = 0.7825242718446602
- Median = 0.7473469387755102
- 25% = 0.5501567398119123
- Min = 0.5283018867924527

#### precision
- Mean = 0.8977910471747281
- Standard deviation = 0.11855228469455384
- Max = 1.0
- 75% = 0.9624999999999999
- Median = 0.9388004895960832
- 25% = 0.8809523809523809
- Min = 0.6086956521739131

#### recall
- Mean = 0.56875
- Standard deviation = 0.11915136848190669
- Max = 0.7166666666666667
- 75% = 0.6666666666666666
- Median = 0.6166666666666667
- 25% = 0.45
- Min = 0.4

#### facing_probas
- Mean = [0.01165972 0.37332639 0.85919097 0.93586458 0.79189236]
- Standard deviation = [0.00584733 0.07054294 0.03566345 0.03874889 0.06133849]
- Max = [0.02161111 0.49694444 0.90377778 0.98647222 0.86825   ]
- 75% = [0.01577778 0.40970833 0.89102083 0.9725625  0.8421875 ]
- Median = [0.01143056 0.376875   0.85827778 0.93731944 0.80244444]
- 25% = [0.00652778 0.30623611 0.82604167 0.89952778 0.75172222]
- Min = [0.00375    0.27825    0.81833333 0.88622222 0.69263889]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 236.0 | 4.0 |
| Actual Positive | 25.875 | 34.125 |

### robot-5
#### accuracy
- Mean = 0.9770833333333333
- Standard deviation = 0.01611051244098434
- Max = 0.99
- 75% = 0.9866666666666667
- Median = 0.9833333333333333
- 25% = 0.9758333333333333
- Min = 0.9366666666666666

#### f1
- Mean = 0.9378871591612439
- Standard deviation = 0.04838569485127609
- Max = 0.9747899159663865
- 75% = 0.9656633547632963
- Median = 0.9572649572649572
- 25% = 0.9356826801517067
- Min = 0.8155339805825242

#### precision
- Mean = 0.9884332418619435
- Standard deviation = 0.0091557815562692
- Max = 1.0
- 75% = 1.0
- Median = 0.9829047340736412
- 25% = 0.9824561403508771
- Min = 0.9767441860465116

#### recall
- Mean = 0.8958333333333334
- Standard deviation = 0.08025566785107595
- Max = 0.9666666666666667
- 75% = 0.9375
- Median = 0.9333333333333333
- 25% = 0.8791666666666667
- Min = 0.7

#### facing_probas
- Mean = [0.00970833 0.01297569 0.19801389 0.92048611 0.89508333]
- Standard deviation = [0.00511848 0.00826282 0.06004533 0.04117999 0.03144197]
- Max = [0.01672222 0.03152778 0.33538889 0.96711111 0.94297222]
- 75% = [0.014      0.01660417 0.20932639 0.96004861 0.92313194]
- Median = [0.01036111 0.00940278 0.17176389 0.92722222 0.88841667]
- 25% = [0.00473611 0.00741667 0.16061111 0.87955556 0.86827778]
- Min = [0.00316667 0.00427778 0.14511111 0.85930556 0.8575    ]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 239.375 | 0.625 |
| Actual Positive | 6.25 | 53.75 |

### robot-6
#### accuracy
- Mean = 0.7529166666666667
- Standard deviation = 0.03584060003837981
- Max = 0.8
- 75% = 0.7775
- Median = 0.7633333333333333
- 25% = 0.7325
- Min = 0.6833333333333333

#### f1
- Mean = 0.8585610154343986
- Standard deviation = 0.023648933773315808
- Max = 0.888888888888889
- 75% = 0.8748234500495394
- Median = 0.865719646207451
- 25% = 0.8455787171360978
- Min = 0.8118811881188119

#### precision
- Mean = 1.0
- Standard deviation = 0.0
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 1.0
- Min = 1.0

#### recall
- Mean = 0.7529166666666667
- Standard deviation = 0.03584060003837981
- Max = 0.8
- 75% = 0.7775
- Median = 0.7633333333333333
- 25% = 0.7325
- Min = 0.6833333333333333

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
| Actual Positive | 74.125 | 225.875 |

