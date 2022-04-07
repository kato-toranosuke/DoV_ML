# ExtraTreesClassifier_ClusterCentroids_2022-01-20-17-59_no1
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
	- n_estimators = 270
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
- gp_auc_min = 0.08834547200731407
- gp_max_val_min = 0.08794814183620918
- gp_max_val_mean = 0.08307064417047244
- gp_auc_max = 0.07407907281137266
- gp_max_val_max = 0.07406246509213583
- gp_auc_mean = 0.06871114968265311
- srmr = 0.05273859344644004
- diff_std = 0.03454467999776154
- tdoa_mean = 0.028876534336445808
- diff_auc = 0.02846552469699839
- ratio_max_to_10ms_ave_peaks = 0.02635232830056038
- hlbr = 0.026143033320226692
- gp_max_ix_mean = 0.025446000888190143
- high_power = 0.02284675978880731
- gp_auc_std = 0.018538112087456367
- tdoa_std = 0.018313825867057643
- coe3[3] = 0.016979248901456738
- coe1[1] = 0.016637642600471937
- gp_max_val_std = 0.016027269103413004
- gp_max_val_range = 0.016002400907802077
- gp_max_ix_std = 0.015927309868603863
- low_power = 0.015415918446986242
- gp_auc_range = 0.014978090362694511
- gp_max_ix_min = 0.01397048640430013
- ac_std = 0.013376224860040958
- coe3[2] = 0.013372943935765021
- coe1[0] = 0.01307914433327544
- tdoa_min = 0.012927849069143826
- tdoa_range = 0.012767053205162615
- gp_max_ix_range = 0.012434960858920716
- ac_auc = 0.010382819815504547
- gp_max_ix_max = 0.010123972159044198
- ratio_max_to_9th_ave_peaks = 0.009335922406150181
- tdoa_max = 0.00777840443116259
- coe3[0] = 0.0
- coe3[1] = 0.0

## Evaluation
cv = 8
### robot-1
#### accuracy
- Mean = 0.9791666666666667
- Standard deviation = 0.009965217285917845
- Max = 0.9966666666666667
- 75% = 0.985
- Median = 0.9766666666666666
- 25% = 0.97
- Min = 0.97

#### f1
- Mean = 0.9473838698437629
- Standard deviation = 0.025362715283025705
- Max = 0.9917355371900827
- 75% = 0.9628099173553719
- Median = 0.9408173525820585
- 25% = 0.9243697478991596
- Min = 0.9230769230769231

#### precision
- Mean = 0.9535092593946661
- Standard deviation = 0.020427704605178464
- Max = 0.9836065573770492
- 75% = 0.971023871153293
- Median = 0.9490940465918896
- 25% = 0.9322033898305084
- Min = 0.9322033898305084

#### recall
- Mean = 0.9416666666666667
- Standard deviation = 0.03435921354681384
- Max = 1.0
- 75% = 0.9708333333333333
- Median = 0.925
- 25% = 0.9166666666666666
- Min = 0.9

#### facing_probas
- Mean = [0.92679012 0.78734568 0.07652778 0.0063966  0.00344907]
- Standard deviation = [0.03173607 0.03755329 0.02128665 0.00583349 0.00211447]
- Max = [0.97111111 0.84580247 0.11790123 0.01802469 0.00604938]
- 75% = [0.95189815 0.81057099 0.08958333 0.00992284 0.00537037]
- Median = [0.9282716  0.78444444 0.07240741 0.00555556 0.0037963 ]
- 25% = [0.89824074 0.75703704 0.0603858  0.00101852 0.00135802]
- Min = [8.84629630e-01 7.35617284e-01 4.96296296e-02 2.46913580e-04
 7.40740741e-04]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 237.25 | 2.75 |
| Actual Positive | 3.5 | 56.5 |

### robot-2
#### accuracy
- Mean = 0.9616666666666667
- Standard deviation = 0.010801234497346443
- Max = 0.9766666666666667
- 75% = 0.9733333333333334
- Median = 0.9583333333333334
- 25% = 0.9533333333333334
- Min = 0.9466666666666667

#### f1
- Mean = 0.8982495816377394
- Standard deviation = 0.029150236120399416
- Max = 0.9401709401709402
- 75% = 0.9288847117794486
- Median = 0.8890469416785206
- 25% = 0.8766447368421052
- Min = 0.8571428571428571

#### precision
- Mean = 0.955502798285306
- Standard deviation = 0.028147030111326594
- Max = 1.0
- 75% = 0.9806644880174291
- Median = 0.9536099865047234
- 25% = 0.9259259259259259
- Min = 0.9230769230769231

#### recall
- Mean = 0.8479166666666668
- Standard deviation = 0.035782425077745116
- Max = 0.9166666666666666
- 75% = 0.8708333333333333
- Median = 0.8333333333333334
- 25% = 0.8291666666666667
- Min = 0.8

#### facing_probas
- Mean = [0.90962191 0.93166667 0.82905093 0.15911265 0.02347994]
- Standard deviation = [0.0275311  0.01581048 0.03735287 0.04414915 0.01103061]
- Max = [0.94197531 0.96234568 0.89092593 0.22969136 0.03851852]
- 75% = [0.93871914 0.93680556 0.85479938 0.1920679  0.03299383]
- Median = [0.90700617 0.93237654 0.82160494 0.16092593 0.02367284]
- 25% = [0.88467593 0.92239198 0.79828704 0.11790123 0.01611111]
- Min = [0.87419753 0.90981481 0.78197531 0.10444444 0.00444444]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 237.625 | 2.375 |
| Actual Positive | 9.125 | 50.875 |

### robot-3
#### accuracy
- Mean = 0.9383333333333334
- Standard deviation = 0.01322875655532294
- Max = 0.96
- 75% = 0.9458333333333333
- Median = 0.9383333333333334
- 25% = 0.9283333333333333
- Min = 0.92

#### f1
- Mean = 0.8169736851522983
- Standard deviation = 0.04677095677436282
- Max = 0.890909090909091
- 75% = 0.8455525606469002
- Median = 0.819047619047619
- 25% = 0.7816307403936271
- Min = 0.7499999999999999

#### precision
- Mean = 0.9919444444444445
- Standard deviation = 0.01041944407417282
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 0.9794444444444445
- Min = 0.9777777777777777

#### recall
- Mean = 0.6979166666666667
- Standard deviation = 0.07141306875417754
- Max = 0.8166666666666667
- 75% = 0.7416666666666667
- Median = 0.7
- 25% = 0.6416666666666667
- Min = 0.6

#### facing_probas
- Mean = [0.24761574 0.88776235 0.90891975 0.76366512 0.15757716]
- Standard deviation = [0.05156116 0.03231889 0.03900348 0.05377489 0.04364347]
- Max = [0.33419753 0.9404321  0.95160494 0.84802469 0.24080247]
- 75% = [0.27935185 0.91998457 0.94617284 0.81089506 0.19023148]
- Median = [0.23959877 0.8757716  0.9129321  0.75311728 0.14558642]
- 25% = [0.20266975 0.85822531 0.87180556 0.71722222 0.11703704]
- Min = [0.19141975 0.85419753 0.85703704 0.69876543 0.11179012]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 239.625 | 0.375 |
| Actual Positive | 18.125 | 41.875 |

### robot-4
#### accuracy
- Mean = 0.9195833333333333
- Standard deviation = 0.0247452296188354
- Max = 0.96
- 75% = 0.935
- Median = 0.9199999999999999
- 25% = 0.9083333333333333
- Min = 0.8833333333333333

#### f1
- Mean = 0.761748046093139
- Standard deviation = 0.08262534579865734
- Max = 0.890909090909091
- 75% = 0.8228021978021979
- Median = 0.7620868883004805
- 25% = 0.7249253299932557
- Min = 0.6153846153846154

#### precision
- Mean = 0.9203743556223365
- Standard deviation = 0.06696749081766294
- Max = 0.98
- 75% = 0.9740479115479116
- Median = 0.9394752534287418
- 25% = 0.8985732009925558
- Min = 0.7659574468085106

#### recall
- Mean = 0.65625
- Standard deviation = 0.10339295994731297
- Max = 0.8166666666666667
- 75% = 0.7291666666666667
- Median = 0.6416666666666666
- 25% = 0.6
- Min = 0.4666666666666667

#### facing_probas
- Mean = [0.0116821  0.31779321 0.83479167 0.92415895 0.77997685]
- Standard deviation = [0.00885742 0.05132979 0.04258391 0.04235373 0.04797066]
- Max = [0.02604938 0.41135802 0.90820988 0.97290123 0.84864198]
- 75% = [0.01924383 0.33751543 0.86146605 0.96412037 0.82024691]
- Median = [0.00969136 0.30549383 0.82018519 0.92685185 0.77830247]
- 25% = [0.00341049 0.27766975 0.81041667 0.88067901 0.73438272]
- Min = [0.00246914 0.25802469 0.77209877 0.87549383 0.71765432]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 236.5 | 3.5 |
| Actual Positive | 20.625 | 39.375 |

### robot-5
#### accuracy
- Mean = 0.9741666666666666
- Standard deviation = 0.009391189724653876
- Max = 0.9966666666666667
- 75% = 0.9741666666666667
- Median = 0.9733333333333334
- 25% = 0.9691666666666666
- Min = 0.9633333333333334

#### f1
- Mean = 0.9328277389414793
- Standard deviation = 0.024947457296378296
- Max = 0.9915966386554621
- 75% = 0.9330584707646177
- Median = 0.9310344827586207
- 25% = 0.920104196403083
- Min = 0.8990825688073394

#### precision
- Mean = 0.9683040500183779
- Standard deviation = 0.032478709110252794
- Max = 1.0
- 75% = 0.9863636363636363
- Median = 0.9727088948787062
- 25% = 0.9642857142857143
- Min = 0.890625

#### recall
- Mean = 0.9020833333333333
- Standard deviation = 0.046724294775012075
- Max = 0.9833333333333333
- 75% = 0.9125
- Median = 0.9
- 25% = 0.8916666666666667
- Min = 0.8166666666666667

#### facing_probas
- Mean = [0.00636574 0.01056327 0.16626543 0.91138889 0.89987654]
- Standard deviation = [0.00291179 0.00604808 0.04493428 0.04733901 0.04391712]
- Max = [0.01111111 0.01925926 0.23962963 0.96839506 0.94932099]
- 75% = [0.00839506 0.01595679 0.19021605 0.95498457 0.94393519]
- Median = [0.00648148 0.01108025 0.16123457 0.91231481 0.89987654]
- 25% = [0.00429012 0.00445988 0.14108025 0.86861111 0.86001543]
- Min = [0.00179012 0.00265432 0.09938272 0.85333333 0.84092593]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 238.125 | 1.875 |
| Actual Positive | 5.875 | 54.125 |

### robot-6
#### accuracy
- Mean = 0.8091666666666667
- Standard deviation = 0.02665364265286579
- Max = 0.8566666666666667
- 75% = 0.825
- Median = 0.805
- 25% = 0.7875000000000001
- Min = 0.7766666666666666

#### f1
- Mean = 0.894280263073848
- Standard deviation = 0.016182630287989032
- Max = 0.9228007181328546
- 75% = 0.9040850453893933
- Median = 0.8919582565991406
- 25% = 0.8811122967798632
- Min = 0.874296435272045

#### precision
- Mean = 1.0
- Standard deviation = 0.0
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 1.0
- Min = 1.0

#### recall
- Mean = 0.8091666666666667
- Standard deviation = 0.02665364265286579
- Max = 0.8566666666666667
- 75% = 0.825
- Median = 0.805
- 25% = 0.7875000000000001
- Min = 0.7766666666666666

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
| Actual Positive | 57.25 | 242.75 |

