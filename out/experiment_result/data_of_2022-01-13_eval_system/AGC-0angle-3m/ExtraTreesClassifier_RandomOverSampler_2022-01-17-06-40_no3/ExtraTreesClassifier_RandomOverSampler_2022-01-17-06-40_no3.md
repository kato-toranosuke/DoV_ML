# ExtraTreesClassifier_RandomOverSampler_2022-01-17-06-40_no3
## Constants
- CSV_PATH = ../out/csv/experiment
- OUTPUT_PATH = ../out/experiment_result/data_of_2022-01-13_eval_system/AGC-0angle-3m
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
- DISTANCE = [3]
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
	- sampling_strategy_ = OrderedDict([(1, 45)])
	- shrinkage_ = None
	- sample_indices_ = [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23
 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47
 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71
 72 73 74 26 18 62 74 50 37 62 24 26 49 12 26 50 50 37 24 18 37 37 12 25
 24  6 37 61 73 25  6 61 24  0 61 49 25 62 61 38  0 50 50 74 49 61 61 74]

- best_estimator
	- base_estimator = ExtraTreeClassifier()
	- n_estimators = 30
	- estimator_params = ('criterion', 'max_depth', 'min_samples_split', 'min_samples_leaf', 'min_weight_fraction_leaf', 'max_features', 'max_leaf_nodes', 'min_impurity_decrease', 'random_state', 'ccp_alpha')
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
	- oob_decision_function_ = [[0.34889441 0.65110559]
 [0.37621252 0.62378748]
 [0.94732804 0.05267196]
 [1.         0.        ]
 [1.         0.        ]
 [0.77394769 0.22605231]
 [0.16414683 0.83585317]
 [0.45671711 0.54328289]
 [0.98765432 0.01234568]
 [1.         0.        ]
 [1.         0.        ]
 [0.79525613 0.20474387]
 [0.44797663 0.55202337]
 [0.65094383 0.34905617]
 [0.91836735 0.08163265]
 [0.95454545 0.04545455]
 [0.97638889 0.02361111]
 [0.4126636  0.5873364 ]
 [0.17581699 0.82418301]
 [0.48486051 0.51513949]
 [0.99479167 0.00520833]
 [0.99404762 0.00595238]
 [0.97251462 0.02748538]
 [0.78718533 0.21281467]
 [0.00666667 0.99333333]
 [0.27426901 0.72573099]
 [0.16650327 0.83349673]
 [0.489553   0.510447  ]
 [0.60717338 0.39282662]
 [0.98154762 0.01845238]
 [0.98524203 0.01475797]
 [1.         0.        ]
 [1.         0.        ]
 [1.         0.        ]
 [1.         0.        ]
 [0.75804674 0.24195326]
 [0.54427083 0.45572917]
 [0.01842105 0.98157895]
 [0.51200397 0.48799603]
 [0.44681055 0.55318945]
 [0.44684569 0.55315431]
 [0.9593254  0.0406746 ]
 [0.93580766 0.06419234]
 [1.         0.        ]
 [1.         0.        ]
 [1.         0.        ]
 [0.97321429 0.02678571]
 [0.81871345 0.18128655]
 [0.75706022 0.24293978]
 [0.07843137 0.92156863]
 [0.01884058 0.98115942]
 [0.66424752 0.33575248]
 [0.64251243 0.35748757]
 [0.94775132 0.05224868]
 [0.83657407 0.16342593]
 [1.         0.        ]
 [0.98214286 0.01785714]
 [0.9447619  0.0552381 ]
 [0.95952381 0.04047619]
 [0.50098039 0.49901961]
 [0.6013431  0.3986569 ]
 [0.1173545  0.8826455 ]
 [0.28555556 0.71444444]
 [0.31931913 0.68068087]
 [0.13874034 0.86125966]
 [0.99375    0.00625   ]
 [0.94736842 0.05263158]
 [1.         0.        ]
 [0.94444444 0.05555556]
 [0.88436949 0.11563051]
 [0.9296875  0.0703125 ]
 [0.90885417 0.09114583]
 [0.88921958 0.11078042]
 [0.67124607 0.32875393]
 [0.12175926 0.87824074]
 [0.12989418 0.87010582]
 [0.13888889 0.86111111]
 [0.17127946 0.82872054]
 [0.1237259  0.8762741 ]
 [0.01666667 0.98333333]
 [0.015625   0.984375  ]
 [0.30078563 0.69921437]
 [0.00526316 0.99473684]
 [0.13954248 0.86045752]
 [0.05479798 0.94520202]
 [0.37796537 0.62203463]
 [0.13179012 0.86820988]
 [0.02222222 0.97777778]
 [0.0254902  0.9745098 ]
 [0.         1.        ]
 [0.00526316 0.99473684]
 [0.1380719  0.8619281 ]
 [0.01184211 0.98815789]
 [0.0140625  0.9859375 ]
 [0.38417297 0.61582703]
 [0.33865741 0.66134259]
 [0.0047619  0.9952381 ]
 [0.1095679  0.8904321 ]
 [0.01944444 0.98055556]
 [0.10119048 0.89880952]
 [0.59433119 0.40566881]
 [0.29112374 0.70887626]
 [0.0703125  0.9296875 ]
 [0.1095679  0.8904321 ]
 [0.00555556 0.99444444]
 [0.3512949  0.6487051 ]
 [0.07600733 0.92399267]
 [0.12793561 0.87206439]
 [0.24516908 0.75483092]
 [0.24548611 0.75451389]
 [0.14206349 0.85793651]
 [0.48806416 0.51193584]
 [0.30267642 0.69732358]
 [0.0254902  0.9745098 ]
 [0.02380952 0.97619048]
 [0.15646465 0.84353535]
 [0.10677609 0.89322391]
 [0.1157477  0.8842523 ]
 [0.10746965 0.89253035]
 [0.09943182 0.90056818]]
	- oob_score_ = 0.9

#### Importance of features
- gp_auc_max = 0.18420139601610025
- gp_max_val_max = 0.10894730667682918
- gp_max_val_mean = 0.08361828423537397
- gp_auc_min = 0.07630806719381415
- gp_max_val_min = 0.06477069798226447
- gp_auc_mean = 0.06404242106666294
- tdoa_std = 0.05248432346855683
- high_power = 0.04257286852237895
- ratio_max_to_10ms_ave_peaks = 0.04016014507932002
- diff_auc = 0.03232515874122312
- tdoa_mean = 0.026848646134716707
- gp_auc_std = 0.020529288810387604
- tdoa_min = 0.01960131275899675
- gp_auc_range = 0.018006208584344617
- gp_max_ix_range = 0.015599878673025858
- gp_max_ix_std = 0.015178236294910951
- ratio_max_to_9th_ave_peaks = 0.014434700921197304
- gp_max_ix_mean = 0.013806587215224856
- coe1[0] = 0.012439435196223998
- gp_max_val_range = 0.011723669551010901
- low_power = 0.01158673531354794
- coe1[1] = 0.009425269284406434
- gp_max_ix_max = 0.009380570565979348
- hlbr = 0.008623322339021283
- ac_std = 0.008099117717935709
- ac_auc = 0.007365193907181164
- tdoa_max = 0.006572057974030165
- diff_std = 0.005770373086928489
- gp_max_ix_min = 0.005465313874450222
- coe3[3] = 0.004957925179174919
- srmr = 0.003727962535546229
- tdoa_range = 0.0007384481110339537
- gp_max_val_std = 0.000689076988200702
- coe3[0] = 0.0
- coe3[1] = 0.0
- coe3[2] = 0.0

## Evaluation
cv = 8
### robot-1
#### accuracy
- Mean = 0.98375
- Standard deviation = 0.011110243021644496
- Max = 1.0
- 75% = 0.9924999999999999
- Median = 0.98
- 25% = 0.9775
- Min = 0.97

#### f1
- Mean = 0.9587320668755199
- Standard deviation = 0.02850192591626605
- Max = 1.0
- 75% = 0.9807692307692307
- Median = 0.9511904761904761
- 25% = 0.9422336328626444
- Min = 0.9189189189189189

#### precision
- Mean = 0.9704816017316018
- Standard deviation = 0.04009998582269643
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 0.9397727272727272
- Min = 0.9047619047619048

#### recall
- Mean = 0.95
- Standard deviation = 0.05
- Max = 1.0
- 75% = 1.0
- Median = 0.95
- 25% = 0.9375
- Min = 0.85

#### facing_probas
- Mean = [0.75239123 0.31924959 0.0225534  0.01467141 0.01881562]
- Standard deviation = [0.03131116 0.04184187 0.01234565 0.00698766 0.01188631]
- Max = [0.82321861 0.39858947 0.04455844 0.02718254 0.04095833]
- 75% = [0.75673664 0.34120632 0.02798313 0.01945833 0.02551389]
- Median = [0.74716064 0.310406   0.02425812 0.01246011 0.02094643]
- 25% = [0.74445109 0.2889458  0.01361332 0.00859491 0.00725997]
- Min = [0.70202736 0.2652756  0.00370014 0.00766667 0.00296296]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 79.375 | 0.625 |
| Actual Positive | 1.0 | 19.0 |

### robot-2
#### accuracy
- Mean = 0.9375
- Standard deviation = 0.013919410907075018
- Max = 0.96
- 75% = 0.95
- Median = 0.935
- 25% = 0.9275
- Min = 0.92

#### f1
- Mean = 0.81499843999844
- Standard deviation = 0.049974148870789846
- Max = 0.888888888888889
- 75% = 0.859073359073359
- Median = 0.8106060606060607
- 25% = 0.7784090909090909
- Min = 0.7499999999999999

#### precision
- Mean = 0.9848345588235294
- Standard deviation = 0.026283390106302953
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 0.9852941176470589
- Min = 0.9375

#### recall
- Mean = 0.7
- Standard deviation = 0.0790569415042095
- Max = 0.8
- 75% = 0.7625
- Median = 0.7
- 25% = 0.6375
- Min = 0.6

#### facing_probas
- Mean = [0.4201167  0.64605382 0.11338387 0.01546814 0.01311342]
- Standard deviation = [0.04629461 0.01857004 0.0288008  0.00732055 0.00695039]
- Max = [0.50026135 0.68987867 0.18197024 0.02967063 0.02452381]
- 75% = [0.46121102 0.64843357 0.11641983 0.01797672 0.01728125]
- Median = [0.40768311 0.64382819 0.10211814 0.0141131  0.01472222]
- 25% = [0.37844322 0.63748399 0.09545527 0.00995279 0.00736806]
- Min = [0.36782063 0.62172307 0.08931301 0.00735251 0.0025641 ]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 79.75 | 0.25 |
| Actual Positive | 6.0 | 14.0 |

### robot-3
#### accuracy
- Mean = 0.99
- Standard deviation = 0.008660254037844395
- Max = 1.0
- 75% = 1.0
- Median = 0.99
- 25% = 0.98
- Min = 0.98

#### f1
- Mean = 0.9741655969191272
- Standard deviation = 0.022805389281812357
- Max = 1.0
- 75% = 1.0
- Median = 0.975609756097561
- 25% = 0.9473684210526316
- Min = 0.9473684210526316

#### precision
- Mean = 0.9880952380952381
- Standard deviation = 0.020619652471058087
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 0.9880952380952381
- Min = 0.9523809523809523

#### recall
- Mean = 0.9624999999999999
- Standard deviation = 0.0484122918275927
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 0.9
- Min = 0.9

#### facing_probas
- Mean = [0.0498124  0.50086268 0.84534692 0.26464732 0.03604109]
- Standard deviation = [0.01767996 0.10573204 0.03176449 0.03982874 0.00891838]
- Max = [0.08300232 0.66267623 0.88755297 0.31478677 0.05072884]
- 75% = [0.06022694 0.58067729 0.8733389  0.30545849 0.04298794]
- Median = [0.04990079 0.5066118  0.84299581 0.26399263 0.03409068]
- 25% = [0.03565413 0.42218433 0.82098624 0.23466851 0.03085127]
- Min = [0.02593651 0.33494007 0.80179331 0.19807431 0.02203836]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 79.75 | 0.25 |
| Actual Positive | 0.75 | 19.25 |

### robot-4
#### accuracy
- Mean = 0.95
- Standard deviation = 0.016583123951776964
- Max = 0.97
- 75% = 0.9624999999999999
- Median = 0.955
- 25% = 0.93
- Min = 0.93

#### f1
- Mean = 0.8836462019105241
- Standard deviation = 0.036702122352721946
- Max = 0.9302325581395349
- 75% = 0.9102787456445993
- Median = 0.8942414174972315
- 25% = 0.8426356589147287
- Min = 0.8372093023255814

#### precision
- Mean = 0.8316130246565029
- Standard deviation = 0.048481861717430054
- Max = 0.9047619047619048
- 75% = 0.8651185770750989
- Median = 0.8448616600790514
- 25% = 0.782608695652174
- Min = 0.76

#### recall
- Mean = 0.94375
- Standard deviation = 0.029973947020704484
- Max = 1.0
- 75% = 0.95
- Median = 0.95
- 25% = 0.9375
- Min = 0.9

#### facing_probas
- Mean = [0.00904307 0.05092358 0.41268741 0.74970299 0.16551865]
- Standard deviation = [0.00274265 0.02271092 0.07750163 0.0597976  0.02547683]
- Max = [0.01326389 0.08977849 0.50555435 0.80151782 0.20897421]
- 75% = [0.01089484 0.06262599 0.46730475 0.80004069 0.18298765]
- Median = [0.00826389 0.047036   0.43839242 0.78109999 0.15912792]
- 25% = [0.00787318 0.03169048 0.36958779 0.70539633 0.14950481]
- Min = [0.00423077 0.02548653 0.26611601 0.6332123  0.1298306 ]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 76.125 | 3.875 |
| Actual Positive | 1.125 | 18.875 |

### robot-5
#### accuracy
- Mean = 0.9275
- Standard deviation = 0.018540496217739132
- Max = 0.96
- 75% = 0.935
- Median = 0.925
- 25% = 0.9175
- Min = 0.9

#### f1
- Mean = 0.7747666759763534
- Standard deviation = 0.06828485326084932
- Max = 0.888888888888889
- 75% = 0.8051948051948052
- Median = 0.7689393939393939
- 25% = 0.7399193548387096
- Min = 0.6666666666666666

#### precision
- Mean = 1.0
- Standard deviation = 0.0
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 1.0
- Min = 1.0

#### recall
- Mean = 0.6375
- Standard deviation = 0.0927024810886958
- Max = 0.8
- 75% = 0.675
- Median = 0.625
- 25% = 0.5875
- Min = 0.5

#### facing_probas
- Mean = [0.01294474 0.007041   0.07352743 0.61277058 0.71135762]
- Standard deviation = [0.00877226 0.00557486 0.01474574 0.04005702 0.0495785 ]
- Max = [0.03379167 0.01533333 0.08986442 0.67440011 0.77917809]
- 75% = [0.01509615 0.01342361 0.08638125 0.63307149 0.75220677]
- Median = [0.01030423 0.00399306 0.07801805 0.61150737 0.71272694]
- 25% = [0.00824653 0.00286325 0.0623969  0.59441505 0.68122108]
- Min = [2.50000000e-03 5.55555556e-04 4.85587422e-02 5.41709938e-01
 6.33838657e-01]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 80.0 | 0.0 |
| Actual Positive | 7.25 | 12.75 |

### robot-6
#### accuracy
- Mean = 0.83875
- Standard deviation = 0.03443744328488976
- Max = 0.9
- 75% = 0.8625
- Median = 0.835
- 25% = 0.8075000000000001
- Min = 0.8

#### f1
- Mean = 0.9119255136719726
- Standard deviation = 0.02024084830482658
- Max = 0.9473684210526316
- 75% = 0.9261687079523893
- Median = 0.9100089100089099
- 25% = 0.8934929404542664
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
- Mean = 0.83875
- Standard deviation = 0.03443744328488976
- Max = 0.9
- 75% = 0.8625
- Median = 0.835
- 25% = 0.8075000000000001
- Min = 0.8

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
| Actual Positive | 16.125 | 83.875 |

