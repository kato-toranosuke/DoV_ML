# ExtraTreesClassifier_SMOTEENN_2022-01-20-22-53_no5
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
	- min_samples_leaf = 5
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
- gp_max_val_mean = 0.20386599070152855
- gp_auc_mean = 0.11755175976325657
- gp_max_val_max = 0.11157851569708846
- gp_auc_min = 0.07891775924596134
- gp_max_val_min = 0.0785625979008153
- gp_auc_max = 0.06798070342681739
- diff_std = 0.0509874147994555
- high_power = 0.035132237228474146
- coe1[0] = 0.028698610309614257
- gp_max_val_range = 0.02780254089713093
- coe1[1] = 0.02608335130604746
- ratio_max_to_10ms_ave_peaks = 0.02532736450495158
- tdoa_min = 0.024079696151855373
- coe3[3] = 0.023805312995377192
- coe3[2] = 0.022931002717795614
- srmr = 0.022788359555630192
- diff_auc = 0.021303599468136307
- tdoa_mean = 0.01830435942406037
- tdoa_std = 0.005309454659326577
- gp_max_ix_std = 0.0043693067365657215
- gp_max_ix_max = 0.0019206167333664721
- gp_auc_range = 0.0007615953867043235
- gp_max_ix_min = 0.0007444063044258315
- gp_max_val_std = 0.0006279664110989427
- tdoa_max = 0.0005654776745156236
- low_power = 0.0
- hlbr = 0.0
- coe3[0] = 0.0
- coe3[1] = 0.0
- ratio_max_to_9th_ave_peaks = 0.0
- ac_std = 0.0
- ac_auc = 0.0
- gp_max_ix_range = 0.0
- gp_max_ix_mean = 0.0
- gp_auc_std = 0.0
- tdoa_range = 0.0

## Evaluation
cv = 8
### robot-1
#### accuracy
- Mean = 0.94
- Standard deviation = 0.026034165586355518
- Max = 0.97
- 75% = 0.9608333333333333
- Median = 0.9516666666666667
- 25% = 0.9141666666666666
- Min = 0.9

#### f1
- Mean = 0.8363911157906465
- Standard deviation = 0.08607446770406553
- Max = 0.9217391304347826
- 75% = 0.9022727272727273
- Median = 0.8758676709496382
- 25% = 0.7882427780272414
- Min = 0.673913043478261

#### precision
- Mean = 0.8971349981866732
- Standard deviation = 0.06926307993372291
- Max = 0.96875
- 75% = 0.9614973262032086
- Median = 0.9008196721311476
- 25% = 0.8744239631336406
- Min = 0.7464788732394366

#### recall
- Mean = 0.8020833333333334
- Standard deviation = 0.14079079732394126
- Max = 0.9166666666666666
- 75% = 0.8875
- Median = 0.8833333333333333
- 25% = 0.7666666666666666
- Min = 0.5166666666666667

#### facing_probas
- Mean = [0.8051717  0.6683926  0.30980615 0.08170615 0.06254354]
- Standard deviation = [0.0596432  0.05502726 0.06589409 0.04626376 0.04201822]
- Max = [0.88376735 0.74439787 0.41837103 0.12529493 0.13134921]
- 75% = [0.84458732 0.70232645 0.36366064 0.11976924 0.0873325 ]
- Median = [0.82266709 0.68448746 0.30891611 0.10708565 0.07386673]
- 25% = [0.77058883 0.61700091 0.25468167 0.04173133 0.01871059]
- Min = [0.68084884 0.59166005 0.21004538 0.00473611 0.00718056]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 233.875 | 6.125 |
| Actual Positive | 11.875 | 48.125 |

### robot-2
#### accuracy
- Mean = 0.8941666666666667
- Standard deviation = 0.042287048187884244
- Max = 0.94
- 75% = 0.9225000000000001
- Median = 0.9066666666666667
- 25% = 0.8833333333333333
- Min = 0.8033333333333333

#### f1
- Mean = 0.7116825878346869
- Standard deviation = 0.10707181221783425
- Max = 0.8333333333333334
- 75% = 0.7823299282764618
- Median = 0.756043956043956
- 25% = 0.6562264150943397
- Min = 0.5042016806722689

#### precision
- Mean = 0.798147061710965
- Standard deviation = 0.14030728307305623
- Max = 0.9375
- 75% = 0.9105415860735009
- Median = 0.8583333333333334
- 25% = 0.7119565217391304
- Min = 0.5084745762711864

#### recall
- Mean = 0.65
- Standard deviation = 0.10929064207170001
- Max = 0.8333333333333334
- 75% = 0.725
- Median = 0.6583333333333333
- 25% = 0.5541666666666667
- Min = 0.5

#### facing_probas
- Mean = [0.79030624 0.84155326 0.71797163 0.35457648 0.11320375]
- Standard deviation = [0.05287854 0.04447088 0.06075757 0.07411067 0.04450999]
- Max = [0.84256202 0.8904471  0.80314677 0.44240829 0.18308829]
- 75% = [0.830473   0.88296277 0.76187958 0.42785913 0.14242194]
- Median = [0.81263476 0.84931474 0.71873594 0.36336665 0.12204993]
- 25% = [0.75994064 0.81017909 0.68955679 0.2877015  0.07268231]
- Min = [0.67785169 0.76326093 0.59482588 0.23811554 0.05028054]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 229.25 | 10.75 |
| Actual Positive | 21.0 | 39.0 |

### robot-3
#### accuracy
- Mean = 0.8341666666666667
- Standard deviation = 0.03213469914109805
- Max = 0.8833333333333333
- 75% = 0.8575
- Median = 0.8366666666666667
- 25% = 0.81
- Min = 0.78

#### f1
- Mean = 0.35504721524035665
- Standard deviation = 0.1400328147696598
- Max = 0.5882352941176471
- 75% = 0.45288461538461544
- Median = 0.35591435591435594
- 25% = 0.24358568261007285
- Min = 0.1739130434782609

#### precision
- Mean = 0.779103004838299
- Standard deviation = 0.21991156037624476
- Max = 1.0
- 75% = 1.0
- Median = 0.8071428571428572
- 25% = 0.6470588235294117
- Min = 0.36363636363636365

#### recall
- Mean = 0.23333333333333334
- Standard deviation = 0.10103629710818451
- Max = 0.4166666666666667
- 75% = 0.3
- Median = 0.22499999999999998
- 25% = 0.15833333333333333
- Min = 0.1

#### facing_probas
- Mean = [0.50589976 0.79171968 0.80216038 0.6167595  0.35144952]
- Standard deviation = [0.06994446 0.04950268 0.05365365 0.07427364 0.06052084]
- Max = [0.63504696 0.86328704 0.86603935 0.7227439  0.48389054]
- 75% = [0.55356628 0.84127582 0.84172327 0.67195706 0.36437435]
- Median = [0.4994147  0.77605883 0.81752472 0.63756278 0.32736579]
- 25% = [0.44718594 0.76493677 0.76785577 0.55108578 0.31434526]
- Min = [0.41286518 0.71462877 0.69631358 0.50363738 0.28921367]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 236.25 | 3.75 |
| Actual Positive | 46.0 | 14.0 |

### robot-4
#### accuracy
- Mean = 0.7808333333333334
- Standard deviation = 0.046599654266719366
- Max = 0.8366666666666667
- 75% = 0.8183333333333334
- Median = 0.7833333333333333
- 25% = 0.7641666666666667
- Min = 0.68

#### f1
- Mean = 0.315393913413609
- Standard deviation = 0.15479432024209072
- Max = 0.5242718446601942
- 75% = 0.4195681773973935
- Median = 0.3829022988505747
- 25% = 0.18166810221073787
- Min = 0.07692307692307691

#### precision
- Mean = 0.41684379061148524
- Standard deviation = 0.18673407630380057
- Max = 0.6296296296296297
- 75% = 0.5826524198617222
- Median = 0.44105351170568563
- 25% = 0.30723443223443225
- Min = 0.09090909090909091

#### recall
- Mean = 0.26041666666666663
- Standard deviation = 0.13742106320033734
- Max = 0.45
- 75% = 0.35416666666666663
- Median = 0.31666666666666665
- 25% = 0.12916666666666665
- Min = 0.06666666666666667

#### facing_probas
- Mean = [0.13858211 0.54543636 0.75649558 0.76067714 0.65094266]
- Standard deviation = [0.07569487 0.06587441 0.05968495 0.07557501 0.05350764]
- Max = [0.24241865 0.66910417 0.83578373 0.84426489 0.74155225]
- 75% = [0.20075468 0.59322243 0.78755343 0.81150848 0.68945255]
- Median = [0.14987103 0.53245823 0.76670934 0.79239552 0.65618124]
- 25% = [0.05405689 0.49880637 0.73986201 0.71261035 0.60013884]
- Min = [0.0413254  0.4484586  0.64651812 0.61551442 0.57360693]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 218.625 | 21.375 |
| Actual Positive | 44.375 | 15.625 |

### robot-5
#### accuracy
- Mean = 0.9025000000000001
- Standard deviation = 0.025698573241848776
- Max = 0.9266666666666666
- 75% = 0.9241666666666667
- Median = 0.9133333333333333
- 25% = 0.8858333333333334
- Min = 0.8533333333333334

#### f1
- Mean = 0.6906988018243019
- Standard deviation = 0.11354634285298623
- Max = 0.7843137254901961
- 75% = 0.7742079207920792
- Median = 0.731958762886598
- 25% = 0.6593406593406594
- Min = 0.4210526315789474

#### precision
- Mean = 0.9295883697708048
- Standard deviation = 0.08747560757732091
- Max = 1.0
- 75% = 0.9734797297297297
- Median = 0.9518002322880371
- 25% = 0.9433304272013949
- Min = 0.7037037037037037

#### recall
- Mean = 0.5666666666666667
- Standard deviation = 0.12583057392117916
- Max = 0.6666666666666666
- 75% = 0.65
- Median = 0.6166666666666667
- 25% = 0.5583333333333333
- Min = 0.26666666666666666

#### facing_probas
- Mean = [0.10605061 0.14790362 0.44160352 0.74429254 0.74934595]
- Standard deviation = [0.06934478 0.07879531 0.0663629  0.06918767 0.05597001]
- Max = [0.21231746 0.25706999 0.56731614 0.81850967 0.82835946]
- 75% = [0.14667982 0.20454944 0.47694726 0.80537434 0.79311148]
- Median = [0.10840961 0.15965647 0.42662006 0.76835736 0.74695122]
- 25% = [0.03447055 0.06710629 0.39199091 0.6960226  0.70950601]
- Min = [0.02081159 0.04127561 0.35203166 0.61963795 0.66338767]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 236.75 | 3.25 |
| Actual Positive | 26.0 | 34.0 |

### robot-6
#### accuracy
- Mean = 0.5025
- Standard deviation = 0.09300164275729518
- Max = 0.6133333333333333
- 75% = 0.5708333333333333
- Median = 0.515
- 25% = 0.4625
- Min = 0.30333333333333334

#### f1
- Mean = 0.6634381300767189
- Standard deviation = 0.08822269498210977
- Max = 0.7603305785123966
- 75% = 0.7267041956981382
- Median = 0.6795979237682057
- 25% = 0.6324451410658307
- Min = 0.4654731457800512

#### precision
- Mean = 1.0
- Standard deviation = 0.0
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 1.0
- Min = 1.0

#### recall
- Mean = 0.5025
- Standard deviation = 0.09300164275729518
- Max = 0.6133333333333333
- 75% = 0.5708333333333333
- Median = 0.515
- 25% = 0.4625
- Min = 0.30333333333333334

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
| Actual Positive | 149.25 | 150.75 |

