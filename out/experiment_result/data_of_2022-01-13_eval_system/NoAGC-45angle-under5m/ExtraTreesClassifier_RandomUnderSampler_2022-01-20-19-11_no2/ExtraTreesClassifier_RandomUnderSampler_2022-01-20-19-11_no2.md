# ExtraTreesClassifier_RandomUnderSampler_2022-01-20-19-11_no2
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
	- n_estimators = 10
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
	- min_samples_split = 10
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
- gp_max_val_mean = 0.17604890362104506
- gp_max_val_max = 0.11183659445225358
- gp_auc_min = 0.09110673017159089
- gp_auc_mean = 0.07240698606915476
- gp_max_val_min = 0.06781471111591296
- hlbr = 0.050845854416741276
- gp_auc_max = 0.04045760093594921
- srmr = 0.035385809141210686
- gp_max_ix_mean = 0.0328398193354177
- tdoa_mean = 0.028737198332341347
- diff_auc = 0.026079327680857724
- ratio_max_to_10ms_ave_peaks = 0.023135122428453093
- gp_auc_std = 0.020207745483673593
- gp_max_ix_range = 0.019123607876103402
- tdoa_range = 0.01890137571883658
- tdoa_std = 0.018511132513140276
- coe1[1] = 0.0184267031946835
- tdoa_min = 0.016979083786636234
- gp_max_val_range = 0.016460468670944733
- gp_max_ix_min = 0.016393373517382667
- gp_max_val_std = 0.01566360234616409
- ac_std = 0.011949512174845701
- gp_max_ix_std = 0.011338149406105207
- diff_std = 0.010737703598835118
- coe1[0] = 0.009595683707225125
- low_power = 0.009020737437991613
- coe3[2] = 0.008392601917252935
- gp_auc_range = 0.0060906511509072414
- gp_max_ix_max = 0.003613373625334906
- tdoa_max = 0.003612706006740453
- high_power = 0.0034774063123488323
- coe3[3] = 0.002264254107300326
- ratio_max_to_9th_ave_peaks = 0.0016407265766970821
- ac_auc = 0.0009047431699220771
- coe3[0] = 0.0
- coe3[1] = 0.0

## Evaluation
cv = 8
### robot-1
#### accuracy
- Mean = 0.9733333333333333
- Standard deviation = 0.010000000000000004
- Max = 0.9833333333333333
- 75% = 0.98
- Median = 0.9766666666666667
- 25% = 0.97
- Min = 0.95

#### f1
- Mean = 0.9318388642683804
- Standard deviation = 0.028017674325156176
- Max = 0.9586776859504132
- 75% = 0.950204918032787
- Median = 0.9408045977011494
- 25% = 0.9243697478991596
- Min = 0.8648648648648648

#### precision
- Mean = 0.9446703729780415
- Standard deviation = 0.015836606534987613
- Max = 0.9821428571428571
- 75% = 0.9502049180327868
- Median = 0.9383301707779885
- 25% = 0.9330508474576271
- Min = 0.9322033898305084

#### recall
- Mean = 0.9208333333333334
- Standard deviation = 0.04982608642958915
- Max = 0.9666666666666667
- 75% = 0.9541666666666666
- Median = 0.925
- 25% = 0.9166666666666666
- Min = 0.8

#### facing_probas
- Mean = [0.89509871 0.72439344 0.1228645  0.00658292 0.00392675]
- Standard deviation = [0.01944835 0.03139487 0.03481571 0.00492062 0.00255735]
- Max = [0.92418717 0.76239153 0.19623016 0.01444444 0.00731481]
- 75% = [0.90760103 0.75268849 0.13535929 0.01054911 0.00657325]
- Median = [0.89471726 0.72811078 0.12265245 0.0058631  0.00366898]
- 25% = [0.88339649 0.70209044 0.09766104 0.00244048 0.00154167]
- Min = [8.59467593e-01 6.65603836e-01 7.92996032e-02 3.33333333e-04
 3.33333333e-04]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 236.75 | 3.25 |
| Actual Positive | 4.75 | 55.25 |

### robot-2
#### accuracy
- Mean = 0.94125
- Standard deviation = 0.014427741410983996
- Max = 0.9666666666666667
- 75% = 0.9516666666666667
- Median = 0.9383333333333334
- 25% = 0.9266666666666666
- Min = 0.9266666666666666

#### f1
- Mean = 0.8369253557791458
- Standard deviation = 0.04201605210288804
- Max = 0.9107142857142857
- 75% = 0.8645962732919255
- Median = 0.8244069015097053
- 25% = 0.8043372319688109
- Min = 0.7884615384615384

#### precision
- Mean = 0.9374421985126773
- Standard deviation = 0.04426549001662325
- Max = 1.0
- 75% = 0.9632774140752864
- Median = 0.9431818181818181
- 25% = 0.9194128787878788
- Min = 0.8518518518518519

#### recall
- Mean = 0.7583333333333333
- Standard deviation = 0.05892556509887896
- Max = 0.85
- 75% = 0.7875000000000001
- Median = 0.75
- 25% = 0.7125
- Min = 0.6833333333333333

#### facing_probas
- Mean = [0.87854258 0.90176992 0.79303861 0.23458226 0.02411334]
- Standard deviation = [0.02884347 0.01418751 0.04195014 0.06133038 0.01090697]
- Max = [0.92768849 0.93312765 0.87181349 0.32947288 0.04800992]
- 75% = [0.90290675 0.90360268 0.82028191 0.28549487 0.02820767]
- Median = [0.87093254 0.89822917 0.7810582  0.20917163 0.01912136]
- 25% = [0.85469312 0.89534177 0.76679712 0.19630489 0.01599091]
- Min = [0.84389021 0.8835205  0.73559325 0.15361905 0.01462963]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 236.875 | 3.125 |
| Actual Positive | 14.5 | 45.5 |

### robot-3
#### accuracy
- Mean = 0.9133333333333333
- Standard deviation = 0.014337208778404371
- Max = 0.9366666666666666
- 75% = 0.9208333333333334
- Median = 0.9166666666666667
- 25% = 0.9033333333333333
- Min = 0.8866666666666667

#### f1
- Mean = 0.7245016280408587
- Standard deviation = 0.062489284605563564
- Max = 0.8256880733944955
- 75% = 0.7582457225314367
- Median = 0.7367021276595744
- 25% = 0.6864587025877349
- Min = 0.6046511627906976

#### precision
- Mean = 0.9795134376901294
- Standard deviation = 0.026397331258808006
- Max = 1.0
- 75% = 1.0
- Median = 0.9871794871794872
- 25% = 0.9726874003189793
- Min = 0.9183673469387755

#### recall
- Mean = 0.58125
- Standard deviation = 0.08757437315409874
- Max = 0.75
- 75% = 0.6208333333333333
- Median = 0.5833333333333333
- 25% = 0.5291666666666667
- Min = 0.43333333333333335

#### facing_probas
- Mean = [0.31787145 0.85315344 0.87737674 0.69728588 0.20742675]
- Standard deviation = [0.03718382 0.03355148 0.03118651 0.05380301 0.03722754]
- Max = [0.36417989 0.9112037  0.92771892 0.78225728 0.25554034]
- 75% = [0.33909425 0.87019229 0.90661806 0.74040427 0.23554299]
- Median = [0.32959094 0.85314021 0.86783135 0.69043849 0.21519808]
- 25% = [0.29538112 0.82999024 0.85210251 0.65398396 0.1794208 ]
- Min = [0.25988029 0.80158333 0.83740476 0.62585516 0.14626786]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 239.125 | 0.875 |
| Actual Positive | 25.125 | 34.875 |

### robot-4
#### accuracy
- Mean = 0.8933333333333333
- Standard deviation = 0.020548046676563254
- Max = 0.92
- 75% = 0.905
- Median = 0.8966666666666666
- 25% = 0.8866666666666667
- Min = 0.8466666666666667

#### f1
- Mean = 0.6702838812215142
- Standard deviation = 0.06640822762829676
- Max = 0.7599999999999999
- 75% = 0.701465002712968
- Median = 0.6833767587285045
- 25% = 0.6545744680851064
- Min = 0.5208333333333334

#### precision
- Mean = 0.8760680906618854
- Standard deviation = 0.08093746994990995
- Max = 0.95
- 75% = 0.9436293436293436
- Median = 0.8983193277310924
- 25% = 0.8464939024390243
- Min = 0.6944444444444444

#### recall
- Mean = 0.54375
- Standard deviation = 0.06063180087856353
- Max = 0.6333333333333333
- 75% = 0.5833333333333334
- Median = 0.55
- 25% = 0.525
- Min = 0.4166666666666667

#### facing_probas
- Mean = [0.01180398 0.3770687  0.8069976  0.8898769  0.72558342]
- Standard deviation = [0.01241463 0.06374167 0.04787181 0.03296167 0.054919  ]
- Max = [0.03991667 0.49947024 0.90166336 0.94251653 0.80677513]
- 75% = [0.01552877 0.4219127  0.84360979 0.92108135 0.78559127]
- Median = [0.00567493 0.35104134 0.78787401 0.87462467 0.70449603]
- 25% = [0.00334656 0.33641022 0.76730737 0.86068469 0.68493915]
- Min = [0.00138889 0.29529365 0.75796561 0.85651984 0.66004696]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 235.375 | 4.625 |
| Actual Positive | 27.375 | 32.625 |

### robot-5
#### accuracy
- Mean = 0.9683333333333333
- Standard deviation = 0.011055415967851338
- Max = 0.9866666666666667
- 75% = 0.9750000000000001
- Median = 0.9683333333333334
- 25% = 0.9591666666666666
- Min = 0.9533333333333334

#### f1
- Mean = 0.9152348784255817
- Standard deviation = 0.03101953465360113
- Max = 0.9661016949152542
- 75% = 0.9351179673321234
- Median = 0.9144535651054241
- 25% = 0.8903635778635779
- Min = 0.8727272727272728

#### precision
- Mean = 0.9763560739651003
- Standard deviation = 0.016049100351671824
- Max = 1.0
- 75% = 0.9870689655172413
- Median = 0.9728835978835979
- 25% = 0.9613499245852187
- Min = 0.96

#### recall
- Mean = 0.8625
- Standard deviation = 0.04982608642958915
- Max = 0.95
- 75% = 0.9
- Median = 0.8583333333333334
- 25% = 0.8166666666666667
- Min = 0.8

#### facing_probas
- Mean = [0.01424901 0.01486682 0.1987066  0.87099959 0.8550086 ]
- Standard deviation = [0.00537403 0.01027036 0.05644662 0.04012955 0.039856  ]
- Max = [0.02321759 0.03557011 0.29702315 0.93283201 0.91887698]
- 75% = [0.01754134 0.01724934 0.24009656 0.9107047  0.88935896]
- Median = [0.01491865 0.01190972 0.19335979 0.85652976 0.84397024]
- 25% = [0.00959276 0.00735582 0.14082176 0.83618237 0.83266849]
- Min = [0.00597222 0.0043254  0.13474603 0.82415873 0.79580423]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 238.75 | 1.25 |
| Actual Positive | 8.25 | 51.75 |

### robot-6
#### accuracy
- Mean = 0.7333333333333334
- Standard deviation = 0.026977356760397756
- Max = 0.7666666666666667
- 75% = 0.7541666666666667
- Median = 0.7350000000000001
- 25% = 0.7225
- Min = 0.6766666666666666

#### f1
- Mean = 0.8458706516813189
- Standard deviation = 0.01819834617967204
- Max = 0.8679245283018869
- 75% = 0.8598567109905411
- Median = 0.847210122993784
- 25% = 0.8388961360262697
- Min = 0.8071570576540755

#### precision
- Mean = 1.0
- Standard deviation = 0.0
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 1.0
- Min = 1.0

#### recall
- Mean = 0.7333333333333334
- Standard deviation = 0.026977356760397756
- Max = 0.7666666666666667
- 75% = 0.7541666666666667
- Median = 0.7350000000000001
- 25% = 0.7225
- Min = 0.6766666666666666

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
| Actual Positive | 80.0 | 220.0 |

