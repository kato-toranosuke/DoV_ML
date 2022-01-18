# ExtraTreesClassifier_SMOTEENN_2022-01-17-22-10_no5
## Constants
- CSV_PATH = ../out/csv/experiment
- OUTPUT_PATH = ../out/experiment_result/data_of_2022-01-13_eval_system/AGC-0angle-under5m
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
- AGC_STATUS = ['AGC']

## Loaded CSV
- 2021-12-27_AGC.csv
- 2022-01-10_NoAGC.csv
- 2022-01-13_raspi_48000Hz_w1_N2^12_overlap80.csv

## Estimator
### Type
- resampler = SMOTEENN
- estimator = ExtraTreesClassifier

### Arguments for hyperparameter search
- resampler = SMOTEENN
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
	- smote = None
	- enn = None
	- n_jobs = -1
	- n_features_in_ = 36
	- sampling_strategy_ = auto
	- smote_ = SMOTE(n_jobs=-1, random_state=42)
	- enn_ = EditedNearestNeighbours(n_jobs=-1, sampling_strategy='all')

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
- gp_max_val_mean = 0.19271780323970378
- tdoa_min = 0.14564881364392532
- diff_auc = 0.10241153110396001
- gp_max_ix_range = 0.10026141406083894
- gp_max_val_max = 0.09572569740718699
- high_power = 0.08702357974298475
- gp_auc_mean = 0.08610334926465098
- hlbr = 0.06307949593381883
- srmr = 0.030468351947781698
- gp_max_val_min = 0.026666434364436328
- tdoa_std = 0.016141711960493684
- tdoa_mean = 0.016126773211895727
- gp_max_ix_std = 0.013377923705376339
- gp_auc_range = 0.006769566394409152
- gp_max_val_std = 0.006643628295032233
- gp_max_ix_max = 0.003279535821716296
- coe3[2] = 0.002550643792588243
- coe1[1] = 0.0021927027693715777
- gp_auc_min = 0.0018344333109144276
- gp_auc_max = 0.0005221671218768
- ratio_max_to_9th_ave_peaks = 0.0002326453291880568
- tdoa_range = 0.000221797577850064
- low_power = 0.0
- coe1[0] = 0.0
- coe3[0] = 0.0
- coe3[1] = 0.0
- coe3[3] = 0.0
- ratio_max_to_10ms_ave_peaks = 0.0
- ac_std = 0.0
- ac_auc = 0.0
- diff_std = 0.0
- gp_max_val_range = 0.0
- gp_max_ix_min = 0.0
- gp_max_ix_mean = 0.0
- gp_auc_std = 0.0
- tdoa_max = 0.0

## Evaluation
cv = 8
### robot-1
#### accuracy
- Mean = 0.9109935897435897
- Standard deviation = 0.022166622896823255
- Max = 0.9498327759197325
- 75% = 0.9205685618729098
- Median = 0.9163879598662208
- 25% = 0.8990719063545151
- Min = 0.8729096989966555

#### f1
- Mean = 0.7712238657512835
- Standard deviation = 0.07278010228427541
- Max = 0.8837209302325583
- 75% = 0.8033137172481435
- Median = 0.7956006205673758
- 25% = 0.7484579100145138
- Min = 0.6415094339622641

#### precision
- Mean = 0.7885272866787839
- Standard deviation = 0.057760049924602354
- Max = 0.8913043478260869
- 75% = 0.8249427917620138
- Median = 0.7928885630498533
- 25% = 0.7472826086956521
- Min = 0.691358024691358

#### recall
- Mean = 0.7708333333333333
- Standard deviation = 0.13762620470761452
- Max = 0.95
- 75% = 0.8708333333333333
- Median = 0.8
- 25% = 0.6583333333333333
- Min = 0.5666666666666667

#### facing_probas
- Mean = [0.64793097 0.48585977 0.31635568 0.16005033 0.16410917]
- Standard deviation = [0.0499931  0.06231083 0.08198214 0.0592043  0.05229508]
- Max = [0.71080902 0.58516347 0.49661006 0.2747279  0.24757649]
- 75% = [0.66972418 0.52504276 0.34988445 0.18228034 0.19753467]
- Median = [0.65503748 0.48697857 0.28012794 0.15063406 0.15999545]
- 25% = [0.64059464 0.46124762 0.25519116 0.13176492 0.12894436]
- Min = [0.5334659  0.35957559 0.24275788 0.06897034 0.08184452]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 226.25 | 12.875 |
| Actual Positive | 13.75 | 46.25 |

### robot-2
#### accuracy
- Mean = 0.8487290969899666
- Standard deviation = 0.03248287190425159
- Max = 0.8963210702341137
- 75% = 0.8712374581939799
- Median = 0.8531103678929766
- 25% = 0.830267558528428
- Min = 0.7926421404682275

#### f1
- Mean = 0.5033030394375033
- Standard deviation = 0.1692029386913736
- Max = 0.7304347826086957
- 75% = 0.6065656565656565
- Median = 0.5463917525773196
- 25% = 0.4447990543735225
- Min = 0.17647058823529416

#### precision
- Mean = 0.7042597307303189
- Standard deviation = 0.10158730430341191
- Max = 0.7948717948717948
- 75% = 0.7686732186732187
- Median = 0.75
- 25% = 0.6695151033386328
- Min = 0.4666666666666667

#### recall
- Mean = 0.4145833333333333
- Standard deviation = 0.17208635994109986
- Max = 0.7
- 75% = 0.5041666666666667
- Median = 0.44166666666666665
- 25% = 0.3458333333333333
- Min = 0.1

#### facing_probas
- Mean = [0.5703932  0.60292811 0.52956983 0.27531424 0.17329851]
- Standard deviation = [0.04996317 0.06492257 0.05990855 0.07837034 0.05065972]
- Max = [0.62666504 0.66039423 0.63553866 0.46559198 0.26614265]
- 75% = [0.60059022 0.64832185 0.57881664 0.27519904 0.19671131]
- Median = [0.57620068 0.62361287 0.51745548 0.25414133 0.17250391]
- 25% = [0.55884452 0.58488637 0.48139646 0.24216189 0.14609228]
- Min = [0.45686658 0.44820328 0.45060761 0.18115616 0.09152927]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 229.0 | 10.125 |
| Actual Positive | 35.125 | 24.875 |

### robot-3
#### accuracy
- Mean = 0.8880072463768116
- Standard deviation = 0.03682534539727254
- Max = 0.9431438127090301
- 75% = 0.9021739130434783
- Median = 0.8864771460423635
- 25% = 0.8729096989966555
- Min = 0.8327759197324415

#### f1
- Mean = 0.7329226757208898
- Standard deviation = 0.08113281788920058
- Max = 0.8495575221238938
- 75% = 0.7757575757575759
- Median = 0.7251629726205997
- 25% = 0.7041987908369849
- Min = 0.576271186440678

#### precision
- Mean = 0.7224589039138796
- Standard deviation = 0.12090346873630349
- Max = 0.92
- 75% = 0.7695185426154847
- Median = 0.6953161592505854
- 25% = 0.6565517241379311
- Min = 0.5730337078651685

#### recall
- Mean = 0.7562500000000001
- Standard deviation = 0.08816709987291178
- Max = 0.85
- 75% = 0.8125
- Median = 0.7833333333333334
- 25% = 0.7125
- Min = 0.5666666666666667

#### facing_probas
- Mean = [0.38566556 0.59695484 0.69130397 0.54856077 0.33084879]
- Standard deviation = [0.0787263  0.06277801 0.05766937 0.04529419 0.08797264]
- Max = [0.53923134 0.65562087 0.76699822 0.62691869 0.52469494]
- 75% = [0.44541713 0.63014626 0.72190623 0.57836933 0.37730752]
- Median = [0.34445288 0.62596987 0.70388736 0.53571438 0.29017223]
- 25% = [0.33034556 0.58317174 0.67393774 0.5266312  0.26791641]
- Min = [0.30112422 0.44350993 0.56076997 0.47185024 0.2511267 ]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 220.25 | 18.875 |
| Actual Positive | 14.625 | 45.375 |

### robot-4
#### accuracy
- Mean = 0.8554236343366779
- Standard deviation = 0.029072303263848603
- Max = 0.903010033444816
- 75% = 0.8720735785953178
- Median = 0.862876254180602
- 25% = 0.8265217391304348
- Min = 0.8127090301003345

#### f1
- Mean = 0.6509249070570657
- Standard deviation = 0.09939025219155574
- Max = 0.7642276422764227
- 75% = 0.7339901477832513
- Median = 0.6836521842779665
- 25% = 0.5719945355191256
- Min = 0.46153846153846156

#### precision
- Mean = 0.6140515720301745
- Standard deviation = 0.061730522578867325
- Max = 0.734375
- 75% = 0.6481481481481481
- Median = 0.6069200226885989
- 25% = 0.5638888888888889
- Min = 0.5333333333333333

#### recall
- Mean = 0.7064265536723164
- Standard deviation = 0.16351368309811729
- Max = 0.8983050847457628
- 75% = 0.8432203389830508
- Median = 0.7372881355932204
- 25% = 0.5865819209039548
- Min = 0.4067796610169492

#### facing_probas
- Mean = [0.18874985 0.32013947 0.58860202 0.66776545 0.50536645]
- Standard deviation = [0.08961881 0.08163777 0.06120383 0.03967436 0.06669393]
- Max = [0.40110274 0.50994452 0.66391564 0.71872236 0.62634981]
- 75% = [0.19797773 0.3337403  0.6510732  0.69857986 0.54656153]
- Median = [0.18179565 0.30148601 0.57495137 0.67083824 0.49861321]
- 25% = [0.14393181 0.26582361 0.56613113 0.65354999 0.46937302]
- Min = [0.07723386 0.23435195 0.46941939 0.59069323 0.38963888]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 214.125 | 25.875 |
| Actual Positive | 17.375 | 41.75 |

### robot-5
#### accuracy
- Mean = 0.887585005574136
- Standard deviation = 0.019516806981861114
- Max = 0.919732441471572
- 75% = 0.8964074693422519
- Median = 0.8913043478260869
- 25% = 0.882943143812709
- Min = 0.8528428093645485

#### f1
- Mean = 0.6118539516633755
- Standard deviation = 0.0984457155610985
- Max = 0.7599999999999999
- 75% = 0.6588671377273253
- Median = 0.6325670498084291
- 25% = 0.5857704059362724
- Min = 0.4358974358974359

#### precision
- Mean = 0.9691253753753754
- Standard deviation = 0.036672459586895904
- Max = 1.0
- 75% = 1.0
- Median = 0.9833333333333334
- 25% = 0.9486111111111111
- Min = 0.8918918918918919

#### recall
- Mean = 0.45625000000000004
- Standard deviation = 0.10669840022751564
- Max = 0.6333333333333333
- 75% = 0.5
- Median = 0.4666666666666667
- 25% = 0.4166666666666667
- Min = 0.2833333333333333

#### facing_probas
- Mean = [0.17238345 0.18596844 0.37196679 0.61091703 0.63034823]
- Standard deviation = [0.06321457 0.09347896 0.06658381 0.04823737 0.06071315]
- Max = [0.31388084 0.41036526 0.5109994  0.66843976 0.71131482]
- 75% = [0.19017407 0.19024424 0.39173079 0.65321517 0.66763107]
- Median = [0.17106158 0.17452831 0.35479226 0.60535539 0.64006525]
- 25% = [0.12830456 0.13837592 0.33978435 0.59690471 0.61063338]
- Min = [0.09304575 0.07501904 0.27386672 0.508843   0.49370537]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 238.125 | 1.0 |
| Actual Positive | 32.625 | 27.375 |

### robot-6
#### accuracy
- Mean = 0.6205546265328874
- Standard deviation = 0.10312916807760836
- Max = 0.7324414715719063
- 75% = 0.6956521739130435
- Median = 0.6477703455964325
- 25% = 0.5794314381270903
- Min = 0.4180602006688963

#### f1
- Mean = 0.7605461030491961
- Standard deviation = 0.08355113494873176
- Max = 0.8455598455598455
- 75% = 0.820390365448505
- Median = 0.7861454440931301
- 25% = 0.7326628619153674
- Min = 0.589622641509434

#### precision
- Mean = 1.0
- Standard deviation = 0.0
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 1.0
- Min = 1.0

#### recall
- Mean = 0.6205546265328874
- Standard deviation = 0.10312916807760836
- Max = 0.7324414715719063
- 75% = 0.6956521739130435
- Median = 0.6477703455964325
- 25% = 0.5794314381270903
- Min = 0.4180602006688963

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
| Actual Positive | 113.5 | 185.625 |

