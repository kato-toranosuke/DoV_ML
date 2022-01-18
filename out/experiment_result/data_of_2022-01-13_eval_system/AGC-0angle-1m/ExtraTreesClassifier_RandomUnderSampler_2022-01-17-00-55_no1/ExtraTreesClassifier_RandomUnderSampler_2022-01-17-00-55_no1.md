# ExtraTreesClassifier_RandomUnderSampler_2022-01-17-00-55_no1
## Constants
- CSV_PATH = ../out/csv/experiment
- OUTPUT_PATH = ../out/experiment_result/data_of_2022-01-13_eval_system/AGC-0angle-1m
- FEATURE_ATTRBS = ['low_power', 'high_power', 'hlbr', 'coe1[0]', 'coe1[1]', 'coe3[0]', 'coe3[1]', 'coe3[2]', 'coe3[3]', 'ratio_max_to_10ms_ave_peaks', 'ratio_max_to_9th_ave_peaks', 'ac_std', 'ac_auc', 'diff_std', 'diff_auc', 'srmr', 'gp_max_val_std', 'gp_max_val_range', 'gp_max_val_min', 'gp_max_val_max', 'gp_max_val_mean', 'gp_max_ix_std', 'gp_max_ix_range', 'gp_max_ix_min', 'gp_max_ix_max', 'gp_max_ix_mean', 'gp_auc_std', 'gp_auc_range', 'gp_auc_min', 'gp_auc_max', 'gp_auc_mean', 'tdoa_std', 'tdoa_range', 'tdoa_min', 'tdoa_max', 'tdoa_mean']
- LABEL_ATTRB = ['facing']
- FACING_DOV_ANGLES = [1]
- NCV = 8
- SCORING = ['accuracy', 'balanced_accuracy', 'f1']
- REFIT_SCORING = balanced_accuracy
- PARAM_GRID = [{'est__n_estimators': range(10, 400, 20), 'est__min_samples_split': [2, 5, 10], 'est__min_samples_leaf': [1, 5, 10], 'est__max_features': ['sqrt', 'log2', None], 'est__bootstrap': [False], 'est__n_jobs': [-1], 'est__random_state': [42], 'est__max_samples': [0.01, 0.5, 0.09]}, {'est__n_estimators': range(10, 400, 20), 'est__min_samples_split': [2, 5, 10], 'est__min_samples_leaf': [1, 5, 10], 'est__max_features': ['sqrt', 'log2', None], 'est__bootstrap': [True], 'est__oob_score': [True, False], 'est__n_jobs': [-1], 'est__random_state': [42], 'est__max_samples': [0.01, 0.5, 0.09]}]
- HP_SET_SESSION = ['trial1', 'trial21']
- TRAIN_SET_SESSION = None
- TEST_SET_SESSION = None
- DISTANCE = [1]
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
	- sampling_strategy_ = OrderedDict([(0, 15)])
	- sample_indices_ = [ 3  8 45 57 16 66 42 60 15 69 58 62 40  6 64  0  1  2 18 19 20 36 37 38
 54 55 56 72 73 74]

- best_estimator
	- base_estimator = ExtraTreeClassifier()
	- n_estimators = 30
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
- gp_max_ix_range = 0.1255689352919754
- tdoa_min = 0.10255274904777074
- gp_max_val_min = 0.0997619399582277
- gp_auc_max = 0.0774980164494267
- gp_max_ix_min = 0.06014861807700682
- gp_max_ix_std = 0.05742180200550681
- gp_auc_std = 0.052083333333333336
- tdoa_range = 0.05168274071281276
- gp_max_val_mean = 0.04956388654575509
- hlbr = 0.04949272754906753
- gp_auc_min = 0.04754710851202079
- tdoa_max = 0.040782009602619886
- gp_auc_range = 0.040390954864639075
- gp_max_val_std = 0.029527715838253737
- gp_max_val_range = 0.021975229293899102
- gp_auc_mean = 0.015714285714285712
- gp_max_val_max = 0.012828668363019515
- gp_max_ix_mean = 0.012653559222186675
- tdoa_mean = 0.01201923076923077
- tdoa_std = 0.01166666666666667
- srmr = 0.010358056265984657
- gp_max_ix_max = 0.006451890355633669
- coe3[3] = 0.0028447226569292302
- diff_std = 0.0021155513784817154
- coe1[0] = 0.0016413786942984
- coe1[1] = 0.0014428028011949678
- high_power = 0.0011811023622047242
- diff_auc = 0.0009148997966889328
- ratio_max_to_10ms_ave_peaks = 0.0007889546351084798
- low_power = 0.000788954635108478
- ac_std = 0.0005915086006619225
- coe3[0] = 0.0
- coe3[1] = 0.0
- coe3[2] = 0.0
- ratio_max_to_9th_ave_peaks = 0.0
- ac_auc = 0.0

## Evaluation
cv = 8
### robot-1
#### accuracy
- Mean = 0.9583333333333334
- Standard deviation = 0.01281425702663158
- Max = 0.9797979797979798
- 75% = 0.9696969696969697
- Median = 0.9545454545454546
- 25% = 0.9494949494949495
- Min = 0.9393939393939394

#### f1
- Mean = 0.898117685160368
- Standard deviation = 0.030248936282259227
- Max = 0.9500000000000001
- 75% = 0.924015009380863
- Median = 0.8890243902439023
- 25% = 0.8764853033145715
- Min = 0.8571428571428572

#### precision
- Mean = 0.8911668375484165
- Standard deviation = 0.0426286729702342
- Max = 0.95
- 75% = 0.9154135338345865
- Median = 0.8973684210526316
- 25% = 0.8571428571428571
- Min = 0.8181818181818182

#### recall
- Mean = 0.90625
- Standard deviation = 0.02997394702070448
- Max = 0.95
- 75% = 0.9125
- Median = 0.9
- 25% = 0.9
- Min = 0.85

#### facing_probas
- Mean = [0.81696857 0.34324488 0.27999438 0.03304939 0.06229516]
- Standard deviation = [0.02158883 0.07300526 0.05421468 0.01496063 0.02309328]
- Max = [0.84938796 0.45703214 0.35494417 0.05426936 0.09414985]
- 75% = [0.83137745 0.41842669 0.31502115 0.04367922 0.08400393]
- Median = [0.81830103 0.30750273 0.29484587 0.03774676 0.06371147]
- 25% = [0.80563806 0.29265621 0.25014072 0.01779689 0.04218914]
- Min = [0.77508347 0.26034498 0.17804762 0.011337   0.02918421]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 76.75 | 2.25 |
| Actual Positive | 1.875 | 18.125 |

### robot-2
#### accuracy
- Mean = 0.8207070707070707
- Standard deviation = 0.024613117032345873
- Max = 0.8686868686868687
- 75% = 0.8308080808080808
- Median = 0.8181818181818182
- 25% = 0.8080808080808081
- Min = 0.7777777777777778

#### f1
- Mean = 0.32160082733358597
- Standard deviation = 0.13387239538183276
- Max = 0.5517241379310346
- 75% = 0.417487684729064
- Median = 0.30769230769230765
- 25% = 0.24
- Min = 0.08333333333333334

#### precision
- Mean = 0.6361111111111111
- Standard deviation = 0.17005808738904407
- Max = 0.8888888888888888
- 75% = 0.6875
- Median = 0.6666666666666666
- 25% = 0.6
- Min = 0.25

#### recall
- Mean = 0.21875
- Standard deviation = 0.10288798520721455
- Max = 0.4
- 75% = 0.3
- Median = 0.2
- 25% = 0.15
- Min = 0.05

#### facing_probas
- Mean = [0.56474721 0.689109   0.7435688  0.07251809 0.07643878]
- Standard deviation = [0.05473532 0.02427772 0.03676984 0.01920842 0.02806244]
- Max = [0.67558741 0.72721169 0.80251057 0.09943929 0.10879269]
- 75% = [0.58898348 0.70800449 0.76857751 0.09291986 0.09338071]
- Median = [0.54363578 0.68300017 0.74348071 0.06754406 0.09005217]
- 25% = [0.52939721 0.67643466 0.72484393 0.0566833  0.06349356]
- Min = [0.49836139 0.64983074 0.68573479 0.04711134 0.0261105 ]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 76.875 | 2.125 |
| Actual Positive | 15.625 | 4.375 |

### robot-3
#### accuracy
- Mean = 0.8282828282828283
- Standard deviation = 0.02525252525252525
- Max = 0.8787878787878788
- 75% = 0.8383838383838383
- Median = 0.8282828282828283
- 25% = 0.8156565656565657
- Min = 0.7878787878787878

#### f1
- Mean = 0.6677411201301038
- Standard deviation = 0.03548934667549679
- Max = 0.75
- 75% = 0.68
- Median = 0.6594202898550725
- 25% = 0.641132075471698
- Min = 0.631578947368421

#### precision
- Mean = 0.5521870815988463
- Standard deviation = 0.0444615374567773
- Max = 0.6428571428571429
- 75% = 0.5692307692307692
- Median = 0.55
- 25% = 0.5258467023172906
- Min = 0.4864864864864865

#### recall
- Mean = 0.85
- Standard deviation = 0.05
- Max = 0.9
- 75% = 0.9
- Median = 0.85
- 25% = 0.8375
- Min = 0.75

#### facing_probas
- Mean = [0.33636594 0.47421005 0.73359921 0.37236669 0.21348065]
- Standard deviation = [0.0891826  0.05508807 0.0287723  0.09129934 0.0668822 ]
- Max = [0.48244428 0.56674908 0.79173465 0.52821972 0.30072621]
- 75% = [0.41249738 0.52487377 0.73869213 0.45843006 0.29201319]
- Median = [0.28160706 0.44965776 0.73087191 0.32128415 0.18920915]
- 25% = [0.27837448 0.44156517 0.72474862 0.29785692 0.15355453]
- Min = [0.23343684 0.39807984 0.68266861 0.28641024 0.13308471]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 65.0 | 14.0 |
| Actual Positive | 3.0 | 17.0 |

### robot-4
#### accuracy
- Mean = 0.898989898989899
- Standard deviation = 0.0404040404040404
- Max = 0.9595959595959596
- 75% = 0.9343434343434344
- Median = 0.8888888888888888
- 25% = 0.8686868686868687
- Min = 0.8383838383838383

#### f1
- Mean = 0.7694186465988793
- Standard deviation = 0.09042654544010106
- Max = 0.9047619047619047
- 75% = 0.8542635658914728
- Median = 0.7386363636363636
- 25% = 0.7077519379844961
- Min = 0.6363636363636364

#### precision
- Mean = 0.6878991479534958
- Standard deviation = 0.08679346456464501
- Max = 0.8260869565217391
- 75% = 0.7459935897435896
- Median = 0.6771428571428572
- 25% = 0.6225961538461539
- Min = 0.56

#### recall
- Mean = 0.875
- Standard deviation = 0.10170805811671255
- Max = 1.0
- 75% = 1.0
- Median = 0.8421052631578947
- 25% = 0.7894736842105263
- Min = 0.7368421052631579

#### facing_probas
- Mean = [0.03119522 0.03786258 0.34687773 0.69028231 0.36229059]
- Standard deviation = [0.0201127  0.00866247 0.10824653 0.04408442 0.10533451]
- Max = [0.05873514 0.05486519 0.53293315 0.77913382 0.55057885]
- 75% = [0.04362757 0.03980926 0.45462792 0.70972021 0.43145533]
- Median = [0.03453883 0.03775817 0.28253532 0.69488364 0.30611298]
- 25% = [0.01527882 0.0360976  0.25771957 0.65414599 0.28690405]
- Min = [0.00240602 0.02088101 0.24856179 0.62947112 0.25200091]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 72.375 | 7.625 |
| Actual Positive | 2.375 | 16.625 |

### robot-5
#### accuracy
- Mean = 0.9116161616161615
- Standard deviation = 0.03416098297593102
- Max = 0.9797979797979798
- 75% = 0.9267676767676768
- Median = 0.898989898989899
- 25% = 0.8863636363636364
- Min = 0.8787878787878788

#### f1
- Mean = 0.7127495724154658
- Standard deviation = 0.12344742139595473
- Max = 0.9473684210526316
- 75% = 0.7767857142857142
- Median = 0.6673387096774194
- 25% = 0.6206896551724138
- Min = 0.5714285714285715

#### precision
- Mean = 0.9791666666666667
- Standard deviation = 0.05511981898051229
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 1.0
- Min = 0.8333333333333334

#### recall
- Mean = 0.575
- Standard deviation = 0.1600781059358212
- Max = 0.9
- 75% = 0.6375
- Median = 0.525
- 25% = 0.45
- Min = 0.4

#### facing_probas
- Mean = [0.11852851 0.02993532 0.08149424 0.55328009 0.61289945]
- Standard deviation = [0.02995746 0.01836222 0.02278653 0.06188646 0.0541305 ]
- Max = [0.15379698 0.05953704 0.12842659 0.67296276 0.72926107]
- 75% = [0.14689208 0.03999306 0.08648217 0.57504854 0.62871338]
- Median = [0.11548831 0.03476757 0.07453284 0.55048709 0.61146613]
- 25% = [0.10470129 0.01576316 0.06890903 0.50995763 0.56441925]
- Min = [0.059116   0.00269841 0.05648381 0.46685929 0.5524139 ]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 78.75 | 0.25 |
| Actual Positive | 8.5 | 11.5 |

### robot-6
#### accuracy
- Mean = 0.6830808080808081
- Standard deviation = 0.0443000121031536
- Max = 0.7676767676767676
- 75% = 0.7121212121212122
- Median = 0.6717171717171717
- 25% = 0.643939393939394
- Min = 0.6363636363636364

#### f1
- Mean = 0.8108924504288832
- Standard deviation = 0.03080002066827304
- Max = 0.8685714285714284
- 75% = 0.8318280909374026
- Median = 0.8036144578313253
- 25% = 0.7834014996591684
- Min = 0.7777777777777778

#### precision
- Mean = 1.0
- Standard deviation = 0.0
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 1.0
- Min = 1.0

#### recall
- Mean = 0.6830808080808081
- Standard deviation = 0.0443000121031536
- Max = 0.7676767676767676
- 75% = 0.7121212121212122
- Median = 0.6717171717171717
- 25% = 0.643939393939394
- Min = 0.6363636363636364

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
| Actual Positive | 31.375 | 67.625 |

