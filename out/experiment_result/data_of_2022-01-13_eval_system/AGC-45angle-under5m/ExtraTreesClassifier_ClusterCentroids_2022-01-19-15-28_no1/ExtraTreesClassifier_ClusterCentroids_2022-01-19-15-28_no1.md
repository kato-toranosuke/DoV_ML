# ExtraTreesClassifier_ClusterCentroids_2022-01-19-15-28_no1
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
- resampler = ClusterCentroids
- estimator = ExtraTreesClassifier

### Arguments for hyperparameter search
- resampler = ClusterCentroids
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
	- estimator = None
	- voting = auto
	- n_jobs = deprecated
	- n_features_in_ = 36
	- sampling_strategy_ = OrderedDict([(1, 108)])
	- estimator_ = KMeans(n_clusters=108, random_state=42)
	- voting_ = soft

- best_estimator
	- base_estimator = ExtraTreeClassifier()
	- n_estimators = 170
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
- gp_max_val_min = 0.09648781291651115
- gp_auc_min = 0.08609210941745721
- gp_max_val_mean = 0.08184570042903043
- gp_auc_max = 0.07323888625209131
- gp_max_val_max = 0.0658479873965542
- gp_auc_mean = 0.062312283475838275
- diff_std = 0.05261415994779506
- diff_auc = 0.04823928122783208
- srmr = 0.046535809659628675
- high_power = 0.04276829249032092
- hlbr = 0.03584392335206887
- tdoa_mean = 0.03559215511869022
- gp_max_ix_mean = 0.027000783296027262
- tdoa_std = 0.021240808726711618
- coe1[1] = 0.019811419319116216
- gp_max_ix_min = 0.01763832489140374
- gp_max_ix_std = 0.016946822942181396
- tdoa_min = 0.01618267439993397
- ratio_max_to_10ms_ave_peaks = 0.015888956172717576
- gp_max_ix_range = 0.015864615564327757
- tdoa_range = 0.014120223443153581
- gp_max_ix_max = 0.011953326519346457
- gp_max_val_std = 0.011378078162701609
- gp_auc_std = 0.011369197876427676
- gp_auc_range = 0.009780515490687564
- gp_max_val_range = 0.009583447786754937
- coe3[2] = 0.009094785306140895
- coe1[0] = 0.007530995025898514
- ratio_max_to_9th_ave_peaks = 0.007279983364780431
- tdoa_max = 0.007019526112433062
- low_power = 0.006139042084857933
- ac_auc = 0.0056556779433812885
- coe3[3] = 0.005566447566094606
- ac_std = 0.005535946321103626
- coe3[0] = 0.0
- coe3[1] = 0.0

## Evaluation
cv = 8
### robot-1
#### accuracy
- Mean = 0.9715719063545151
- Standard deviation = 0.009005292319622911
- Max = 0.9866220735785953
- 75% = 0.9765886287625418
- Median = 0.9715719063545151
- 25% = 0.9690635451505016
- Min = 0.9531772575250836

#### f1
- Mean = 0.9318722710890647
- Standard deviation = 0.02126488531374418
- Max = 0.9666666666666667
- 75% = 0.9442204724409449
- Median = 0.9322539682539682
- 25% = 0.9255081967213115
- Min = 0.888888888888889

#### precision
- Mean = 0.9000183494887395
- Standard deviation = 0.030296355311150873
- Max = 0.9666666666666667
- 75% = 0.9043424317617865
- Median = 0.8947308909995477
- 25% = 0.8923076923076924
- Min = 0.8484848484848485

#### recall
- Mean = 0.9666666666666666
- Standard deviation = 0.022047927592204905
- Max = 1.0
- 75% = 0.9833333333333333
- Median = 0.9666666666666667
- 25% = 0.9583333333333334
- Min = 0.9333333333333333

#### facing_probas
- Mean = [0.96735294 0.76933824 0.11862745 0.00232843 0.00245098]
- Standard deviation = [0.01457194 0.02807556 0.0226723  0.00239432 0.00170726]
- Max = [0.97794118 0.82254902 0.15088235 0.00656863 0.00558824]
- 75% = [0.97534314 0.7795098  0.13240196 0.00281863 0.00387255]
- Median = [0.97205882 0.77235294 0.12156863 0.00107843 0.00156863]
- 25% = [9.67132353e-01 7.59828431e-01 1.10980392e-01 9.31372549e-04
 1.02941176e-03]
- Min = [9.30196078e-01 7.18921569e-01 7.34313725e-02 1.96078431e-04
 8.82352941e-04]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 232.5 | 6.5 |
| Actual Positive | 2.0 | 58.0 |

### robot-2
#### accuracy
- Mean = 0.9644648829431438
- Standard deviation = 0.01016324898088897
- Max = 0.9765886287625418
- 75% = 0.9698996655518395
- Median = 0.9665551839464883
- 25% = 0.9632107023411371
- Min = 0.939799331103679

#### f1
- Mean = 0.9064910915530967
- Standard deviation = 0.02756705373150186
- Max = 0.9401709401709402
- 75% = 0.9192776847644104
- Median = 0.912280701754386
- 25% = 0.9051508963013388
- Min = 0.8392857142857143

#### precision
- Mean = 0.9584881435365546
- Standard deviation = 0.02770132137326796
- Max = 1.0
- 75% = 0.9689672293942403
- Median = 0.9629629629629629
- 25% = 0.9541542535584244
- Min = 0.9038461538461539

#### recall
- Mean = 0.8604166666666666
- Standard deviation = 0.03529390488770295
- Max = 0.9166666666666666
- 75% = 0.8708333333333333
- Median = 0.8666666666666667
- 25% = 0.85
- Min = 0.7833333333333333

#### facing_probas
- Mean = [0.92372549 0.93960784 0.8075     0.09841912 0.00655637]
- Standard deviation = [0.01352222 0.01345604 0.02390308 0.02047063 0.00560722]
- Max = [0.94352941 0.95833333 0.85745098 0.13421569 0.01941176]
- 75% = [0.93127451 0.95017157 0.81544118 0.11156863 0.00615196]
- Median = [0.92558824 0.93911765 0.8070098  0.09455882 0.00416667]
- 25% = [0.91791667 0.93237745 0.78936275 0.08754902 0.00384804]
- Min = [0.89715686 0.91323529 0.77441176 0.06343137 0.00137255]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 236.75 | 2.25 |
| Actual Positive | 8.375 | 51.625 |

### robot-3
#### accuracy
- Mean = 0.9506688963210703
- Standard deviation = 0.008149493599338592
- Max = 0.959866220735786
- 75% = 0.959866220735786
- Median = 0.9498327759197325
- 25% = 0.9448160535117057
- Min = 0.939799331103679

#### f1
- Mean = 0.8592447138507072
- Standard deviation = 0.02647068605148933
- Max = 0.888888888888889
- 75% = 0.888888888888889
- Median = 0.8570391872278664
- 25% = 0.840497737556561
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
- Mean = 0.7541666666666667
- Standard deviation = 0.040611643103370725
- Max = 0.8
- 75% = 0.8
- Median = 0.75
- 25% = 0.725
- Min = 0.7

#### facing_probas
- Mean = [0.31254902 0.94224265 0.96584559 0.904375   0.12539216]
- Standard deviation = [0.03082297 0.01465165 0.01130473 0.01226626 0.01133848]
- Max = [0.35970588 0.96127451 0.97970588 0.92107843 0.14323529]
- 75% = [0.3295098  0.95627451 0.97463235 0.91186275 0.13046569]
- Median = [0.31102941 0.93941176 0.96563725 0.9075     0.12397059]
- 25% = [0.30139706 0.93392157 0.95977941 0.89367647 0.12044118]
- Min = [0.24990196 0.91764706 0.94421569 0.885      0.10735294]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 239.0 | 0.0 |
| Actual Positive | 14.75 | 45.25 |

### robot-4
#### accuracy
- Mean = 0.9431438127090301
- Standard deviation = 0.00868921809817162
- Max = 0.9565217391304348
- 75% = 0.9506688963210703
- Median = 0.9414715719063546
- 25% = 0.9364548494983278
- Min = 0.9297658862876255

#### f1
- Mean = 0.8518496605135606
- Standard deviation = 0.022189145554082693
- Max = 0.8785046728971962
- 75% = 0.8747604304879847
- Median = 0.8523002421307506
- 25% = 0.8338126048406421
- Min = 0.8205128205128206

#### precision
- Mean = 0.8801827911641251
- Standard deviation = 0.04762558939678812
- Max = 0.9791666666666666
- 75% = 0.9109848484848484
- Median = 0.8583333333333334
- 25% = 0.8468001168907071
- Min = 0.8275862068965517

#### recall
- Mean = 0.8283898305084745
- Standard deviation = 0.04014257483367884
- Max = 0.8813559322033898
- 75% = 0.8516949152542372
- Median = 0.8389830508474576
- 25% = 0.8093220338983051
- Min = 0.7457627118644068

#### facing_probas
- Mean = [0.01202642 0.14177468 0.90634347 0.97058824 0.75331505]
- Standard deviation = [0.00373843 0.02640625 0.0172615  0.00979748 0.03660933]
- Max = [0.01674975 0.18255234 0.93080758 0.98215354 0.79351944]
- 75% = [0.01375872 0.16119143 0.91542871 0.9778664  0.78028415]
- Median = [0.01316052 0.14207378 0.91335992 0.97372881 0.76734796]
- 25% = [0.01134098 0.12320538 0.89705882 0.96505484 0.72926221]
- Min = [0.00319043 0.0996012  0.87676969 0.94975075 0.68065803]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 233.125 | 6.875 |
| Actual Positive | 10.125 | 48.875 |

### robot-5
#### accuracy
- Mean = 0.9770066889632107
- Standard deviation = 0.009954749916212917
- Max = 0.9966555183946488
- 75% = 0.984113712374582
- Median = 0.9715719063545151
- 25% = 0.9698996655518395
- Min = 0.9665551839464883

#### f1
- Mean = 0.9385068391980378
- Standard deviation = 0.027358029997991636
- Max = 0.9915966386554621
- 75% = 0.9587706146926537
- Median = 0.9237451737451737
- 25% = 0.9189189189189189
- Min = 0.9090909090909091

#### precision
- Mean = 1.0
- Standard deviation = 0.0
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 1.0
- Min = 1.0

#### recall
- Mean = 0.8854166666666666
- Standard deviation = 0.04960783708246106
- Max = 0.9833333333333333
- 75% = 0.9208333333333333
- Median = 0.8583333333333334
- 25% = 0.85
- Min = 0.8333333333333334

#### facing_probas
- Mean = [0.00444853 0.00279412 0.22382353 0.95053922 0.95039216]
- Standard deviation = [0.00406506 0.0018679  0.02574206 0.00709058 0.01189592]
- Max = [0.01284314 0.00578431 0.25676471 0.96303922 0.96509804]
- 75% = [0.0057598  0.00411765 0.24502451 0.95416667 0.95696078]
- Median = [0.00254902 0.00215686 0.23083333 0.94931373 0.95406863]
- 25% = [0.00156863 0.00120098 0.20071078 0.94696078 0.94497549]
- Min = [8.82352941e-04 7.84313725e-04 1.81176471e-01 9.39313725e-01
 9.29607843e-01]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 239.0 | 0.0 |
| Actual Positive | 6.875 | 53.125 |

### robot-6
#### accuracy
- Mean = 0.859113712374582
- Standard deviation = 0.0200276581388018
- Max = 0.8795986622073578
- 75% = 0.8762541806020067
- Median = 0.8662207357859532
- 25% = 0.8453177257525084
- Min = 0.8193979933110368

#### f1
- Mean = 0.9240926932708476
- Standard deviation = 0.011685719899825494
- Max = 0.9359430604982205
- 75% = 0.9340463458110517
- Median = 0.9283016443987666
- 25% = 0.9161751361161524
- Min = 0.900735294117647

#### precision
- Mean = 1.0
- Standard deviation = 0.0
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 1.0
- Min = 1.0

#### recall
- Mean = 0.859113712374582
- Standard deviation = 0.0200276581388018
- Max = 0.8795986622073578
- 75% = 0.8762541806020067
- Median = 0.8662207357859532
- 25% = 0.8453177257525084
- Min = 0.8193979933110368

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
| Actual Positive | 42.125 | 256.875 |

