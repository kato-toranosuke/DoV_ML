# ExtraTreesClassifier_NoResampler_2022-04-13-08-25_no0
## Constants
- CSV_PATH = ../out/csv/experiment
- OUTPUT_PATH = ../out/experiment_result/data_of_2022-03-23_eval_system/AGC-30deg-0angle-under5m
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
- DISTANCE = [1, 3, 5]
- AGC_STATUS = ['AGC-30deg']
- ANGLES = [30, 60, 90, 120, 150]

## Loaded CSV
- 2022-03-23_raspi_48000Hz_w1_N2^12_overlap80_all.csv

## Estimator
### Type
- resampler = NoResampler
- estimator = ExtraTreesClassifier

### Arguments for hyperparameter search
- resampler = NoResampler
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

- best_estimator
	- base_estimator = ExtraTreeClassifier()
	- n_estimators = 190
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
- gp_auc_min = 0.05664396269784057
- gp_max_val_min = 0.05335280466315906
- gp_max_val_mean = 0.050472799594758325
- ratio_max_to_9th_ave_peaks = 0.04596271298761237
- gp_auc_mean = 0.04453410462882969
- gp_auc_max = 0.044367997293642755
- gp_max_val_max = 0.040432778819325936
- gp_auc_range = 0.037812807214196484
- ratio_max_to_10ms_ave_peaks = 0.03494705526961518
- gp_max_val_range = 0.03373946854333138
- gp_max_val_std = 0.031364350627871275
- ac_auc = 0.03112445385718609
- diff_auc = 0.030601122657996735
- gp_auc_std = 0.029941011060518684
- coe1[1] = 0.029829321511188632
- low_power = 0.02952993730247726
- high_power = 0.02863163384421451
- gp_max_ix_mean = 0.028402095094568577
- hlbr = 0.02823675584608016
- coe1[0] = 0.027314761138951153
- srmr = 0.026999723272963017
- gp_max_ix_std = 0.025763947056317623
- tdoa_mean = 0.023649070657070923
- tdoa_std = 0.021750348429468196
- coe3[3] = 0.021677448071270776
- ac_std = 0.0214080885087065
- diff_std = 0.020466212786307256
- coe3[2] = 0.01987723168435359
- gp_max_ix_max = 0.01552463618397619
- tdoa_min = 0.014498929923191857
- tdoa_max = 0.013511614017351474
- gp_max_ix_range = 0.013018488469153112
- tdoa_range = 0.012794002707178351
- gp_max_ix_min = 0.011818323579326134
- coe3[0] = 0.0
- coe3[1] = 0.0

## Evaluation
cv = 8
### robot-1
#### accuracy
- Mean = 0.875
- Standard deviation = 0.016329931618554526
- Max = 0.9
- 75% = 0.89
- Median = 0.8733333333333333
- 25% = 0.8641666666666667
- Min = 0.85

#### f1
- Mean = 0.5614978232107168
- Standard deviation = 0.07792177674915352
- Max = 0.673913043478261
- 75% = 0.6248579007199697
- Median = 0.5600835945663531
- 25% = 0.5153256704980842
- Min = 0.4155844155844156

#### precision
- Mean = 0.930411742429947
- Standard deviation = 0.0612857862925656
- Max = 1.0
- 75% = 0.9765625
- Median = 0.9383301707779885
- 25% = 0.9087301587301587
- Min = 0.8148148148148148

#### recall
- Mean = 0.40625
- Standard deviation = 0.07450647809269863
- Max = 0.5166666666666667
- 75% = 0.45833333333333337
- Median = 0.4083333333333333
- 25% = 0.3625
- Min = 0.26666666666666666

#### facing_probas
- Mean = [0.44934576 0.10523026 0.06555556 0.02918037 0.00919134]
- Standard deviation = [0.04364926 0.0193874  0.01420292 0.00702419 0.00395373]
- Max = [0.49244883 0.15012427 0.09068713 0.03957602 0.01486842]
- 75% = [0.47953034 0.10958151 0.07512792 0.03516082 0.01225877]
- Median = [0.46504386 0.10116228 0.06495614 0.02772295 0.00968567]
- 25% = [0.44019554 0.09592105 0.05749452 0.02470577 0.0053655 ]
- Min = [0.37336988 0.07966374 0.04401316 0.01731725 0.00332602]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 238.125 | 1.875 |
| Actual Positive | 35.625 | 24.375 |

### robot-2
#### accuracy
- Mean = 0.82625
- Standard deviation = 0.010984521938720078
- Max = 0.8433333333333334
- 75% = 0.8341666666666667
- Median = 0.8266666666666667
- 25% = 0.8191666666666666
- Min = 0.8066666666666666

#### f1
- Mean = 0.3748313525815779
- Standard deviation = 0.047393232065372055
- Max = 0.4597701149425288
- 75% = 0.39188520534388915
- Median = 0.36897334089619965
- 25% = 0.3602272727272727
- Min = 0.2857142857142857

#### precision
- Mean = 0.6787814037814038
- Standard deviation = 0.0812173938679597
- Max = 0.8235294117647058
- 75% = 0.7101851851851851
- Median = 0.6870629370629371
- 25% = 0.6391402714932127
- Min = 0.5294117647058824

#### recall
- Mean = 0.2625
- Standard deviation = 0.04468252206151503
- Max = 0.3333333333333333
- 75% = 0.3
- Median = 0.2583333333333333
- 25% = 0.23333333333333334
- Min = 0.18333333333333332

#### facing_probas
- Mean = [0.25157803 0.40694627 0.28676718 0.09658808 0.03210069]
- Standard deviation = [0.02042035 0.02068611 0.01048962 0.00893547 0.00783963]
- Max = [0.29782895 0.43934211 0.30247076 0.10861111 0.04163743]
- 75% = [0.25508406 0.41913377 0.29248173 0.1022405  0.03940789]
- Median = [0.24582602 0.40484284 0.28770102 0.09992325 0.03283991]
- 25% = [0.23866594 0.3977924  0.28005665 0.09041667 0.02559211]
- Min = [0.22975146 0.37082602 0.26894737 0.08212719 0.01874269]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 232.125 | 7.875 |
| Actual Positive | 44.25 | 15.75 |

### robot-3
#### accuracy
- Mean = 0.7929166666666667
- Standard deviation = 0.01466642992233171
- Max = 0.8166666666666667
- 75% = 0.8
- Median = 0.7933333333333333
- 25% = 0.7841666666666667
- Min = 0.77

#### f1
- Mean = 0.20340763160075276
- Standard deviation = 0.09028589794729937
- Max = 0.3092783505154639
- 75% = 0.2555197421434327
- Median = 0.24048192771084337
- 25% = 0.1635645302897278
- Min = 0.0303030303030303

#### precision
- Mean = 0.44096672520585567
- Standard deviation = 0.15054792660471952
- Max = 0.6923076923076923
- 75% = 0.51
- Median = 0.43167701863354035
- 25% = 0.3840540540540541
- Min = 0.16666666666666666

#### recall
- Mean = 0.13958333333333334
- Standard deviation = 0.07067998105703073
- Max = 0.25
- 75% = 0.175
- Median = 0.15
- 25% = 0.1125
- Min = 0.016666666666666666

#### facing_probas
- Mean = [0.14268092 0.32955135 0.34386879 0.23681561 0.11282529]
- Standard deviation = [0.03511955 0.03417799 0.04104161 0.03490901 0.01264755]
- Max = [0.19633772 0.40785088 0.41069444 0.28092836 0.13543129]
- 75% = [0.17442434 0.33497807 0.36367507 0.26765716 0.11925987]
- Median = [0.13604167 0.32765351 0.34358918 0.2463231  0.11490497]
- 25% = [0.1135508  0.30885965 0.32132675 0.19991594 0.10307566]
- Min = [0.09296784 0.28451023 0.27369883 0.18878655 0.09315058]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 229.5 | 10.5 |
| Actual Positive | 51.625 | 8.375 |

### robot-4
#### accuracy
- Mean = 0.8191666666666666
- Standard deviation = 0.018615256586407246
- Max = 0.8466666666666667
- 75% = 0.8316666666666667
- Median = 0.8200000000000001
- 25% = 0.8116666666666666
- Min = 0.7866666666666666

#### f1
- Mean = 0.3231456527225469
- Standard deviation = 0.08966319927232512
- Max = 0.4367816091954023
- 75% = 0.3878408370323399
- Median = 0.34931009440813365
- 25% = 0.2797961532138748
- Min = 0.15789473684210528

#### precision
- Mean = 0.635086215868244
- Standard deviation = 0.1568342219471587
- Max = 0.9375
- 75% = 0.6976650563607085
- Median = 0.6491228070175439
- 25% = 0.5676470588235294
- Min = 0.375

#### recall
- Mean = 0.21875
- Standard deviation = 0.06689414315834301
- Max = 0.31666666666666665
- 75% = 0.25416666666666665
- Median = 0.24166666666666667
- 25% = 0.18333333333333335
- Min = 0.1

#### facing_probas
- Mean = [0.06767087 0.16291484 0.25628472 0.39513706 0.28826389]
- Standard deviation = [0.01018292 0.0253938  0.02188756 0.03211792 0.03497066]
- Max = [0.08384503 0.21604532 0.30880117 0.45070175 0.35656433]
- 75% = [0.07256396 0.16973684 0.25859649 0.41294408 0.30450841]
- Median = [0.07022295 0.16193348 0.24953216 0.4008845  0.28693348]
- 25% = [0.06412463 0.14979715 0.24201754 0.36872076 0.26582602]
- Min = [0.04878655 0.12253655 0.23709064 0.35157164 0.23273392]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 232.625 | 7.375 |
| Actual Positive | 46.875 | 13.125 |

### robot-5
#### accuracy
- Mean = 0.8512500000000001
- Standard deviation = 0.012686114456365277
- Max = 0.8766666666666667
- 75% = 0.8575
- Median = 0.8500000000000001
- 25% = 0.8425
- Min = 0.8333333333333334

#### f1
- Mean = 0.4779142729146153
- Standard deviation = 0.07033079912277904
- Max = 0.6185567010309277
- 75% = 0.516996699669967
- Median = 0.45861733203505356
- 25% = 0.44047619047619047
- Min = 0.3846153846153846

#### precision
- Mean = 0.814589477153662
- Standard deviation = 0.10655857809756089
- Max = 1.0
- 75% = 0.861842105263158
- Median = 0.8012387387387387
- 25% = 0.7520833333333334
- Min = 0.6585365853658537

#### recall
- Mean = 0.34791666666666665
- Standard deviation = 0.08225869592666514
- Max = 0.5
- 75% = 0.4
- Median = 0.30833333333333335
- 25% = 0.29583333333333334
- Min = 0.25

#### facing_probas
- Mean = [0.01426718 0.06315241 0.16681835 0.34582785 0.44331597]
- Standard deviation = [0.00637792 0.01873763 0.03095106 0.03117391 0.03362205]
- Max = [0.02362573 0.10788012 0.2085307  0.39540205 0.48030702]
- 75% = [0.01805738 0.06322551 0.18565789 0.3602595  0.46516813]
- Median = [0.01472222 0.05943713 0.17969298 0.3465095  0.45935307]
- 25% = [0.00919408 0.05551718 0.14353436 0.33647844 0.42459795]
- Min = [0.00540936 0.03830409 0.11070906 0.2806652  0.3746345 ]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 234.5 | 5.5 |
| Actual Positive | 39.125 | 20.875 |

### robot-6
#### accuracy
- Mean = 0.275
- Standard deviation = 0.02773886162848873
- Max = 0.31666666666666665
- 75% = 0.29333333333333333
- Median = 0.2816666666666667
- 25% = 0.245
- Min = 0.24

#### f1
- Mean = 0.4306287376358736
- Standard deviation = 0.03419321719135941
- Max = 0.4810126582278481
- 75% = 0.4535775887705942
- Median = 0.4395081102287639
- 25% = 0.39356563739865447
- Min = 0.3870967741935484

#### precision
- Mean = 1.0
- Standard deviation = 0.0
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 1.0
- Min = 1.0

#### recall
- Mean = 0.275
- Standard deviation = 0.02773886162848873
- Max = 0.31666666666666665
- 75% = 0.29333333333333333
- Median = 0.2816666666666667
- 25% = 0.245
- Min = 0.24

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
| Actual Positive | 217.5 | 82.5 |

