# ExtraTreesClassifier_RandomOverSampler_2022-04-12-18-31_no3
## Constants
- CSV_PATH = ../out/csv/experiment
- OUTPUT_PATH = ../out/experiment_result/data_of_2022-03-23_eval_system/AGC-30deg-0angle-1m
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
- AGC_STATUS = ['AGC-30deg']
- ANGLES = [30, 60, 90, 120, 150]

## Loaded CSV
- 2022-03-23_raspi_48000Hz_w1_N2^12_overlap80_all.csv

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
	- sampling_strategy_ = OrderedDict([(1, 45)])
	- shrinkage_ = None
	- sample_indices_ = [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23
 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47
 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71
 72 73 74 36 18 72 74 55 37 72 19 36 54  2 36 55 55 37 19 18 37 37  2 20
 19  1 37 56 73 20  1 56 19  0 56 54 20 72 56 38  0 55 55 74 54 56 56 74]

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
	- min_samples_split = 2
	- min_samples_leaf = 10
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
- gp_max_ix_range = 0.17008087113087383
- gp_auc_max = 0.13716643973113862
- tdoa_mean = 0.09050804446219426
- gp_auc_min = 0.07753295344208265
- gp_auc_mean = 0.07303508566353581
- gp_max_val_max = 0.06048491738090626
- tdoa_range = 0.058102092401290294
- tdoa_min = 0.05322986543206175
- gp_max_ix_std = 0.052419730006287926
- gp_max_val_mean = 0.04785603470711379
- gp_max_ix_mean = 0.03167292098370594
- gp_max_ix_min = 0.02624916762331238
- gp_max_val_std = 0.025088588869092855
- coe1[1] = 0.02032622456000032
- tdoa_std = 0.019946810546966547
- coe3[3] = 0.016664293242657245
- gp_max_val_range = 0.012193856400266084
- gp_auc_range = 0.008873396435848087
- coe1[0] = 0.007902458437929314
- ratio_max_to_10ms_ave_peaks = 0.0038714672861014246
- coe3[2] = 0.002522259254443295
- gp_max_ix_max = 0.0024455646222461755
- tdoa_max = 0.0017846519928613903
- ac_std = 4.230538708376547e-05
- low_power = 0.0
- high_power = 0.0
- hlbr = 0.0
- coe3[0] = 0.0
- coe3[1] = 0.0
- ratio_max_to_9th_ave_peaks = 0.0
- ac_auc = 0.0
- diff_std = 0.0
- diff_auc = 0.0
- srmr = 0.0
- gp_max_val_min = 0.0
- gp_auc_std = 0.0

## Evaluation
cv = 8
### robot-1
#### accuracy
- Mean = 0.99375
- Standard deviation = 0.0048412291827592754
- Max = 1.0
- 75% = 1.0
- Median = 0.99
- 25% = 0.99
- Min = 0.99

#### f1
- Mean = 0.983974358974359
- Standard deviation = 0.012413408160921218
- Max = 1.0
- 75% = 1.0
- Median = 0.9743589743589743
- 25% = 0.9743589743589743
- Min = 0.9743589743589743

#### precision
- Mean = 1.0
- Standard deviation = 0.0
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 1.0
- Min = 1.0

#### recall
- Mean = 0.96875
- Standard deviation = 0.024206145913796377
- Max = 1.0
- 75% = 1.0
- Median = 0.95
- 25% = 0.95
- Min = 0.95

#### facing_probas
- Mean = [0.75154733 0.09239898 0.04069566 0.03019024 0.05115332]
- Standard deviation = [0.03734367 0.03431306 0.02226283 0.0232308  0.03828302]
- Max = [0.83512495 0.15112159 0.07907572 0.06595783 0.10285683]
- 75% = [0.76416257 0.11197364 0.05617194 0.04579509 0.08576389]
- Median = [0.74374275 0.10154992 0.04292837 0.02293452 0.04971377]
- 25% = [0.73430938 0.05592274 0.02148848 0.01510302 0.0138141 ]
- Min = [0.69824742 0.04756448 0.00633109 0.         0.        ]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 80.0 | 0.0 |
| Actual Positive | 0.625 | 19.375 |

### robot-2
#### accuracy
- Mean = 0.855
- Standard deviation = 0.03708099243547832
- Max = 0.91
- 75% = 0.875
- Median = 0.86
- 25% = 0.8374999999999999
- Min = 0.78

#### f1
- Mean = 0.6852785589023838
- Standard deviation = 0.08190537847242667
- Max = 0.7999999999999999
- 75% = 0.7470449172576832
- Median = 0.7003205128205128
- 25% = 0.6225913621262458
- Min = 0.5416666666666667

#### precision
- Mean = 0.6134226571063208
- Standard deviation = 0.08396781850740977
- Max = 0.7333333333333333
- 75% = 0.6799999999999999
- Median = 0.5976890756302521
- 25% = 0.5645380434782609
- Min = 0.4642857142857143

#### recall
- Mean = 0.8
- Standard deviation = 0.15
- Max = 1.0
- 75% = 0.9
- Median = 0.875
- 25% = 0.65
- Min = 0.55

#### facing_probas
- Mean = [0.41491783 0.75736195 0.67527462 0.25495744 0.0201488 ]
- Standard deviation = [0.08203502 0.02543556 0.03191881 0.10539072 0.01919403]
- Max = [0.51843189 0.80710852 0.72867598 0.44552755 0.0519011 ]
- 75% = [0.5135204  0.76519091 0.69200619 0.31228276 0.03144087]
- Median = [0.3817638  0.74567177 0.68313737 0.26337426 0.01356571]
- 25% = [0.35098568 0.73780062 0.65462516 0.15122407 0.00495536]
- Min = [0.30758885 0.73696128 0.62284717 0.1190238  0.        ]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 69.5 | 10.5 |
| Actual Positive | 4.0 | 16.0 |

### robot-3
#### accuracy
- Mean = 0.8225
- Standard deviation = 0.04493050188902857
- Max = 0.89
- 75% = 0.845
- Median = 0.815
- 25% = 0.7975000000000001
- Min = 0.75

#### f1
- Mean = 0.3958246705423775
- Standard deviation = 0.18176516009951216
- Max = 0.6666666666666667
- 75% = 0.5219298245614036
- Median = 0.3603896103896104
- 25% = 0.25565217391304346
- Min = 0.13793103448275865

#### precision
- Mean = 0.637633547008547
- Standard deviation = 0.23515043272471314
- Max = 1.0
- 75% = 0.8461538461538461
- Median = 0.6125
- 25% = 0.4903846153846154
- Min = 0.2222222222222222

#### recall
- Mean = 0.3125
- Standard deviation = 0.1709349291397168
- Max = 0.55
- 75% = 0.47500000000000003
- Median = 0.275
- 25% = 0.15
- Min = 0.1

#### facing_probas
- Mean = [0.11289809 0.61707319 0.59369653 0.48288203 0.22370935]
- Standard deviation = [0.0767569  0.02455701 0.02192369 0.06402748 0.04721958]
- Max = [0.29041382 0.63948929 0.6277303  0.60682119 0.32707423]
- 75% = [0.118847   0.63565867 0.60440419 0.51814032 0.23025537]
- Median = [0.09554216 0.62861513 0.59460405 0.47456012 0.21467278]
- 25% = [0.05696543 0.60645205 0.58212112 0.42703707 0.19562474]
- Min = [0.04476959 0.5708615  0.56066685 0.40726578 0.16777702]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 76.0 | 4.0 |
| Actual Positive | 13.75 | 6.25 |

### robot-4
#### accuracy
- Mean = 0.78125
- Standard deviation = 0.051341381944782105
- Max = 0.87
- 75% = 0.805
- Median = 0.78
- 25% = 0.76
- Min = 0.68

#### f1
- Mean = 0.5445130779584562
- Standard deviation = 0.13498760394230708
- Max = 0.7346938775510204
- 75% = 0.61
- Median = 0.5798319327731092
- 25% = 0.5117647058823529
- Min = 0.2727272727272727

#### precision
- Mean = 0.4604939129897417
- Standard deviation = 0.10085827510593376
- Max = 0.6206896551724138
- 75% = 0.5083333333333333
- Median = 0.467741935483871
- 25% = 0.43333333333333335
- Min = 0.25

#### recall
- Mean = 0.675
- Standard deviation = 0.19685019685029528
- Max = 0.9
- 75% = 0.8
- Median = 0.75
- 25% = 0.625
- Min = 0.3

#### facing_probas
- Mean = [0.04107847 0.38086483 0.36688934 0.691208   0.63459937]
- Standard deviation = [0.02325187 0.05524125 0.06350123 0.05042042 0.02139152]
- Max = [0.07263468 0.440484   0.45911309 0.77620314 0.67005202]
- 75% = [0.06375274 0.43219889 0.40868964 0.71732586 0.64932685]
- Median = [0.03375702 0.39979116 0.38079971 0.69608316 0.63351591]
- 25% = [0.02745491 0.31834062 0.30416321 0.66992909 0.62599818]
- Min = [0.00380952 0.30541649 0.28173973 0.61423354 0.59798492]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 64.625 | 15.375 |
| Actual Positive | 6.5 | 13.5 |

### robot-5
#### accuracy
- Mean = 0.8075
- Standard deviation = 0.05562148865321748
- Max = 0.89
- 75% = 0.8474999999999999
- Median = 0.795
- 25% = 0.7875000000000001
- Min = 0.7

#### f1
- Mean = 0.3658105869059216
- Standard deviation = 0.1875693137811945
- Max = 0.6285714285714286
- 75% = 0.5051724137931035
- Median = 0.35414725069897485
- 25% = 0.2115384615384615
- Min = 0.11764705882352941

#### precision
- Mean = 0.5405695611577964
- Standard deviation = 0.24762814862871924
- Max = 1.0
- 75% = 0.7083333333333333
- Median = 0.4852941176470588
- 25% = 0.41666666666666663
- Min = 0.14285714285714285

#### recall
- Mean = 0.2875
- Standard deviation = 0.1615355997915011
- Max = 0.55
- 75% = 0.41250000000000003
- Median = 0.275
- 25% = 0.1375
- Min = 0.1

#### facing_probas
- Mean = [0.02669402 0.17525805 0.06694925 0.71524459 0.65166474]
- Standard deviation = [0.02303967 0.03928287 0.02172817 0.02849405 0.04417576]
- Max = [0.06843697 0.24032811 0.10794065 0.76703922 0.70337806]
- 75% = [0.03476177 0.19051092 0.08210597 0.72740062 0.69766971]
- Median = [0.02375    0.17720824 0.06392697 0.71824219 0.65100112]
- 25% = [0.00840659 0.16094692 0.04912143 0.69663251 0.614925  ]
- Min = [0.         0.1111277  0.03869314 0.66502811 0.58595144]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 75.0 | 5.0 |
| Actual Positive | 14.25 | 5.75 |

### robot-6
#### accuracy
- Mean = 0.60875
- Standard deviation = 0.05372092236736075
- Max = 0.68
- 75% = 0.6525000000000001
- Median = 0.62
- 25% = 0.56
- Min = 0.52

#### f1
- Mean = 0.7553973859231797
- Standard deviation = 0.041979847025323695
- Max = 0.8095238095238095
- 75% = 0.7897042716319825
- Median = 0.7652439024390243
- 25% = 0.717948717948718
- Min = 0.6842105263157895

#### precision
- Mean = 1.0
- Standard deviation = 0.0
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 1.0
- Min = 1.0

#### recall
- Mean = 0.60875
- Standard deviation = 0.05372092236736075
- Max = 0.68
- 75% = 0.6525000000000001
- Median = 0.62
- 25% = 0.56
- Min = 0.52

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
| Actual Positive | 39.125 | 60.875 |

