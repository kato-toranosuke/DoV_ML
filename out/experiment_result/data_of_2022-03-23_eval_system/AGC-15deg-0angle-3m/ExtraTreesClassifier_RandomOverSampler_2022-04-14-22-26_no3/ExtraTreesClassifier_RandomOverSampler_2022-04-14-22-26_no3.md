# ExtraTreesClassifier_RandomOverSampler_2022-04-14-22-26_no3
## Constants
- CSV_PATH = ../out/csv/experiment
- OUTPUT_PATH = ../out/experiment_result/data_of_2022-03-23_eval_system/AGC-15deg-0angle-3m
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
- AGC_STATUS = ['AGC-15deg']
- ANGLES = [60, 75, 90, 105, 120]

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
	- oob_decision_function_ = [[0.48418457 0.51581543]
 [0.43717166 0.56282834]
 [0.47484129 0.52515871]
 [0.51066066 0.48933934]
 [0.47262918 0.52737082]
 [0.40562752 0.59437248]
 [0.40902527 0.59097473]
 [0.39552186 0.60447814]
 [0.37010187 0.62989813]
 [0.44431452 0.55568548]
 [0.47053452 0.52946548]
 [0.62669082 0.37330918]
 [0.42958525 0.57041475]
 [0.47350338 0.52649662]
 [0.51918022 0.48081978]
 [0.44605818 0.55394182]
 [0.38666667 0.61333333]
 [0.51990743 0.48009257]
 [0.48620032 0.51379968]
 [0.47147819 0.52852181]
 [0.43160159 0.56839841]
 [0.47801804 0.52198196]
 [0.44286583 0.55713417]
 [0.47046377 0.52953623]
 [0.47630616 0.52369384]
 [0.51128681 0.48871319]
 [0.50295212 0.49704788]
 [0.42919641 0.57080359]
 [0.57180748 0.42819252]
 [0.47551292 0.52448708]
 [0.47106431 0.52893569]
 [0.50263772 0.49736228]
 [0.46522989 0.53477011]
 [0.51072249 0.48927751]
 [0.40538676 0.59461324]
 [0.39726308 0.60273692]
 [0.51051804 0.48948196]
 [0.43958549 0.56041451]
 [0.48647151 0.51352849]
 [0.48686684 0.51313316]
 [0.43721273 0.56278727]
 [0.4372549  0.5627451 ]
 [0.39853546 0.60146454]
 [0.51215884 0.48784116]
 [0.43303698 0.56696302]
 [0.40854701 0.59145299]
 [0.51143162 0.48856838]
 [0.50327808 0.49672192]
 [0.46468184 0.53531816]
 [0.44008267 0.55991733]
 [0.38813439 0.61186561]
 [0.52013778 0.47986222]
 [0.4091133  0.5908867 ]
 [0.48407031 0.51592969]
 [0.47953668 0.52046332]
 [0.44616069 0.55383931]
 [0.40555556 0.59444444]
 [0.46583085 0.53416915]
 [0.45752813 0.54247187]
 [0.53445434 0.46554566]
 [0.31588943 0.68411057]
 [0.47413004 0.52586996]
 [0.48918531 0.51081469]
 [0.48641908 0.51358092]
 [0.4393654  0.5606346 ]
 [0.41789829 0.58210171]
 [0.42039711 0.57960289]
 [0.4362832  0.5637168 ]
 [0.44616812 0.55383188]
 [0.48993573 0.51006427]
 [0.48997896 0.51002104]
 [0.47914934 0.52085066]
 [0.50550923 0.49449077]
 [0.52992961 0.47007039]
 [0.4578882  0.5421118 ]
 [0.48075046 0.51924954]
 [0.49355161 0.50644839]
 [0.51569899 0.48430101]
 [0.45676183 0.54323817]
 [0.43911169 0.56088831]
 [0.45952381 0.54047619]
 [0.49625455 0.50374545]
 [0.47262918 0.52737082]
 [0.54886016 0.45113984]
 [0.50904762 0.49095238]
 [0.51874934 0.48125066]
 [0.51236076 0.48763924]
 [0.45510511 0.54489489]
 [0.47916667 0.52083333]
 [0.4715799  0.5284201 ]
 [0.43528377 0.56471623]
 [0.47229111 0.52770889]
 [0.42163031 0.57836969]
 [0.43441837 0.56558163]
 [0.46134269 0.53865731]
 [0.46055612 0.53944388]
 [0.50650772 0.49349228]
 [0.4335421  0.5664579 ]
 [0.42277311 0.57722689]
 [0.569613   0.430387  ]
 [0.47324534 0.52675466]
 [0.38059641 0.61940359]
 [0.45735162 0.54264838]
 [0.46052377 0.53947623]
 [0.46814542 0.53185458]
 [0.48180362 0.51819638]
 [0.57457445 0.42542555]
 [0.50714286 0.49285714]
 [0.37850523 0.62149477]
 [0.47913985 0.52086015]
 [0.49636564 0.50363436]
 [0.450981   0.549019  ]
 [0.43996688 0.56003312]
 [0.54047619 0.45952381]
 [0.50776249 0.49223751]
 [0.52852339 0.47147661]
 [0.47263736 0.52736264]
 [0.5421935  0.4578065 ]
 [0.55606447 0.44393553]
 [0.51155824 0.48844176]]
	- oob_score_ = 0.4666666666666667

#### Importance of features
- high_power = 0.16666666666666666
- coe3[2] = 0.16666666666666666
- gp_max_val_max = 0.16666666666666666
- gp_max_val_mean = 0.16666666666666666
- gp_max_val_std = 0.1416172180525825
- hlbr = 0.12400477800062641
- gp_max_ix_max = 0.04266188866604028
- diff_auc = 0.025049448614084136
- low_power = 0.0
- coe1[0] = 0.0
- coe1[1] = 0.0
- coe3[0] = 0.0
- coe3[1] = 0.0
- coe3[3] = 0.0
- ratio_max_to_10ms_ave_peaks = 0.0
- ratio_max_to_9th_ave_peaks = 0.0
- ac_std = 0.0
- ac_auc = 0.0
- diff_std = 0.0
- srmr = 0.0
- gp_max_val_range = 0.0
- gp_max_val_min = 0.0
- gp_max_ix_std = 0.0
- gp_max_ix_range = 0.0
- gp_max_ix_min = 0.0
- gp_max_ix_mean = 0.0
- gp_auc_std = 0.0
- gp_auc_range = 0.0
- gp_auc_min = 0.0
- gp_auc_max = 0.0
- gp_auc_mean = 0.0
- tdoa_std = 0.0
- tdoa_range = 0.0
- tdoa_min = 0.0
- tdoa_max = 0.0
- tdoa_mean = 0.0

## Evaluation
cv = 8
### robot-1
#### accuracy
- Mean = 0.73375
- Standard deviation = 0.07873015622999867
- Max = 0.83
- 75% = 0.805
- Median = 0.74
- 25% = 0.6775
- Min = 0.59

#### f1
- Mean = 0.3888030085728919
- Standard deviation = 0.16658752388197975
- Max = 0.6153846153846154
- 75% = 0.5232142857142857
- Median = 0.3765182186234818
- 25% = 0.324468085106383
- Min = 0.046511627906976744

#### precision
- Mean = 0.37153852839994145
- Standard deviation = 0.16860055802023283
- Max = 0.6
- 75% = 0.5125
- Median = 0.35353535353535354
- 25% = 0.2991898148148148
- Min = 0.043478260869565216

#### recall
- Mean = 0.425
- Standard deviation = 0.2
- Max = 0.8
- 75% = 0.5125
- Median = 0.4
- 25% = 0.35
- Min = 0.05

#### facing_probas
- Mean = [0.53389806 0.52124482 0.47780874 0.50933891 0.47287452]
- Standard deviation = [0.01455778 0.02187069 0.03447228 0.02998366 0.02579601]
- Max = [0.55690632 0.54878181 0.5077718  0.55415754 0.50573965]
- 75% = [0.54243949 0.5408735  0.50403497 0.52826775 0.4939042 ]
- Median = [0.53148616 0.52209112 0.49449135 0.50477622 0.47246032]
- 25% = [0.52390994 0.50623164 0.45786324 0.4903873  0.46625597]
- Min = [0.51140467 0.48894415 0.40237096 0.46157415 0.41805763]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 64.875 | 15.125 |
| Actual Positive | 11.5 | 8.5 |

### robot-2
#### accuracy
- Mean = 0.69875
- Standard deviation = 0.045397549493337186
- Max = 0.76
- 75% = 0.75
- Median = 0.685
- 25% = 0.6675
- Min = 0.63

#### f1
- Mean = 0.1360389016574388
- Standard deviation = 0.12497293570625981
- Max = 0.36842105263157887
- 75% = 0.21060606060606063
- Median = 0.13873295910184444
- 25% = 0.0
- Min = 0.0

#### precision
- Mean = 0.15615477517651433
- Standard deviation = 0.1401920834936797
- Max = 0.3888888888888889
- 75% = 0.24358974358974358
- Median = 0.16521739130434782
- 25% = 0.0
- Min = 0.0

#### recall
- Mean = 0.125
- Standard deviation = 0.11726039399558574
- Max = 0.35
- 75% = 0.2
- Median = 0.125
- 25% = 0.0
- Min = 0.0

#### facing_probas
- Mean = [0.53608012 0.51711339 0.50015057 0.52178706 0.46385244]
- Standard deviation = [0.01061165 0.01868993 0.02688247 0.01254382 0.03662263]
- Max = [0.55087198 0.5398785  0.53141852 0.5335775  0.50355041]
- 75% = [0.54336072 0.52749026 0.51964031 0.53133632 0.49182934]
- Median = [0.53812435 0.52090444 0.50880463 0.52525576 0.47762617]
- 25% = [0.5314633  0.51392607 0.48124259 0.51949923 0.44261548]
- Min = [0.51865331 0.4733238  0.45526808 0.49293045 0.40265837]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 67.375 | 12.625 |
| Actual Positive | 17.5 | 2.5 |

### robot-3
#### accuracy
- Mean = 0.73375
- Standard deviation = 0.05677532474587882
- Max = 0.8
- 75% = 0.78
- Median = 0.76
- 25% = 0.6675
- Min = 0.66

#### f1
- Mean = 0.12070360195360194
- Standard deviation = 0.06630140232684535
- Max = 0.21428571428571425
- 75% = 0.15705128205128205
- Median = 0.1519230769230769
- 25% = 0.06746031746031747
- Min = 0.0

#### precision
- Mean = 0.21296600877192984
- Standard deviation = 0.1604142847035385
- Max = 0.5
- 75% = 0.34375
- Median = 0.1539473684210526
- 25% = 0.109375
- Min = 0.0

#### recall
- Mean = 0.09375
- Standard deviation = 0.05266343608235224
- Max = 0.15
- 75% = 0.15
- Median = 0.1
- 25% = 0.05
- Min = 0.0

#### facing_probas
- Mean = [0.52850139 0.53035022 0.52485895 0.54572274 0.50552685]
- Standard deviation = [0.01316051 0.00851585 0.01206838 0.01863371 0.01788963]
- Max = [0.54879729 0.54461478 0.54215749 0.57596845 0.53366538]
- 75% = [0.53734032 0.53382003 0.53658204 0.55814074 0.51317418]
- Median = [0.52813917 0.53057138 0.52203478 0.54351358 0.50877103]
- 25% = [0.52141917 0.52664817 0.51639233 0.53381852 0.49704583]
- Min = [0.50828547 0.5176649  0.50668074 0.51695057 0.47535257]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 71.5 | 8.5 |
| Actual Positive | 18.125 | 1.875 |

### robot-4
#### accuracy
- Mean = 0.62875
- Standard deviation = 0.0666028340237861
- Max = 0.74
- 75% = 0.68
- Median = 0.615
- 25% = 0.5675
- Min = 0.55

#### f1
- Mean = 0.3282879995731954
- Standard deviation = 0.11028464187270641
- Max = 0.45714285714285713
- 75% = 0.37912549926424216
- Median = 0.3542483660130719
- 25% = 0.3205128205128205
- Min = 0.07142857142857144

#### precision
- Mean = 0.2565273432067863
- Standard deviation = 0.05866302574894002
- Max = 0.32
- 75% = 0.30340425531914894
- Median = 0.25245098039215685
- 25% = 0.24333333333333332
- Min = 0.125

#### recall
- Mean = 0.5062500000000001
- Standard deviation = 0.2283603238305639
- Max = 0.8
- 75% = 0.6625
- Median = 0.575
- 25% = 0.375
- Min = 0.05

#### facing_probas
- Mean = [0.49227968 0.50974353 0.50802648 0.54146136 0.50208266]
- Standard deviation = [0.01927119 0.02039584 0.0202445  0.01458112 0.01973645]
- Max = [0.51715213 0.53457985 0.54042717 0.56002589 0.52500871]
- 75% = [0.50736975 0.51678893 0.51765531 0.54943573 0.52368935]
- Median = [0.49380849 0.51479253 0.50280857 0.54395416 0.49919781]
- 25% = [0.48126296 0.51034084 0.49522218 0.53869791 0.49193257]
- Min = [0.45934477 0.45945259 0.48133167 0.50761835 0.47082696]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 52.75 | 27.25 |
| Actual Positive | 9.875 | 10.125 |

### robot-5
#### accuracy
- Mean = 0.7775000000000001
- Standard deviation = 0.017139136501002624
- Max = 0.81
- 75% = 0.79
- Median = 0.775
- 25% = 0.76
- Min = 0.76

#### f1
- Mean = 0.1971651381026381
- Standard deviation = 0.15061250173887863
- Max = 0.4285714285714286
- 75% = 0.3053977272727273
- Median = 0.22814814814814818
- 25% = 0.05769230769230768
- Min = 0.0

#### precision
- Mean = 0.29355852480852485
- Standard deviation = 0.19805018531151244
- Max = 0.5714285714285714
- 75% = 0.4109848484848485
- Median = 0.39230769230769236
- 25% = 0.125
- Min = 0.0

#### recall
- Mean = 0.1625
- Standard deviation = 0.14523687548277814
- Max = 0.45
- 75% = 0.25
- Median = 0.15000000000000002
- 25% = 0.037500000000000006
- Min = 0.0

#### facing_probas
- Mean = [0.45679704 0.47029102 0.48389568 0.52998353 0.50076626]
- Standard deviation = [0.03807043 0.03456657 0.04264657 0.01453445 0.02735723]
- Max = [0.49935868 0.51212117 0.53297985 0.55121669 0.53370977]
- 75% = [0.48842033 0.49232542 0.50567902 0.53895338 0.52414271]
- Median = [0.47040385 0.49014296 0.4899748  0.53117265 0.50233282]
- 25% = [0.4318798  0.44272527 0.47742146 0.52069617 0.48847617]
- Min = [0.38635984 0.41456487 0.38300646 0.5034982  0.4477942 ]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 74.5 | 5.5 |
| Actual Positive | 16.75 | 3.25 |

### robot-6
#### accuracy
- Mean = 0.2625
- Standard deviation = 0.04763139720814413
- Max = 0.34
- 75% = 0.28250000000000003
- Median = 0.26
- 25% = 0.2425
- Min = 0.18

#### f1
- Mean = 0.41358066633422563
- Standard deviation = 0.05998570194535714
- Max = 0.5074626865671642
- 75% = 0.4401097590073968
- Median = 0.41269841269841273
- 25% = 0.39016393442622954
- Min = 0.3050847457627119

#### precision
- Mean = 1.0
- Standard deviation = 0.0
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 1.0
- Min = 1.0

#### recall
- Mean = 0.2625
- Standard deviation = 0.04763139720814413
- Max = 0.34
- 75% = 0.28250000000000003
- Median = 0.26
- 25% = 0.2425
- Min = 0.18

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
| Actual Positive | 73.75 | 26.25 |

