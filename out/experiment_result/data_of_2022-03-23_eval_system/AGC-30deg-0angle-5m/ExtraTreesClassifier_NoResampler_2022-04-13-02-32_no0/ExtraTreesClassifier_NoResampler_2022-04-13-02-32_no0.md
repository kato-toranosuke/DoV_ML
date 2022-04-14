# ExtraTreesClassifier_NoResampler_2022-04-13-02-32_no0
## Constants
- CSV_PATH = ../out/csv/experiment
- OUTPUT_PATH = ../out/experiment_result/data_of_2022-03-23_eval_system/AGC-30deg-0angle-5m
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
- DISTANCE = [5]
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
	- n_estimators = 50
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
	- max_features = None
	- max_leaf_nodes = None
	- min_impurity_decrease = 0.0
	- ccp_alpha = 0.0
	- n_features_in_ = 36
	- n_outputs_ = 1
	- classes_ = [0 1]
	- n_classes_ = 2
	- base_estimator_ = ExtraTreeClassifier()

#### Importance of features
- gp_max_val_max = 0.11838524620798967
- gp_auc_mean = 0.08419472012551477
- gp_max_val_mean = 0.07979360963749721
- gp_max_val_min = 0.06752326649266241
- gp_max_ix_min = 0.05686723639503372
- high_power = 0.05469130618664443
- tdoa_min = 0.050781472209181534
- gp_auc_min = 0.049400750410569294
- gp_auc_max = 0.04872820965602062
- diff_auc = 0.04221077472464636
- gp_max_ix_range = 0.0366227455813071
- gp_max_val_std = 0.029511248449553534
- gp_auc_range = 0.02697023754150094
- diff_std = 0.024307194504494745
- gp_max_ix_std = 0.023391100443927483
- gp_auc_std = 0.0206047330056712
- tdoa_range = 0.017658869047536354
- hlbr = 0.01755740163996035
- tdoa_std = 0.016739108012125317
- gp_max_ix_max = 0.01621865175712513
- tdoa_max = 0.013243737288761782
- ac_auc = 0.013050115618970817
- gp_max_val_range = 0.012935197635832615
- low_power = 0.012451344915877627
- ratio_max_to_9th_ave_peaks = 0.012371874782705803
- coe3[2] = 0.009956495026535913
- coe1[1] = 0.009642957267351718
- coe1[0] = 0.008491396501892963
- coe3[3] = 0.00812693937841867
- ac_std = 0.006534064526341385
- srmr = 0.0057930451695268875
- gp_max_ix_mean = 0.003685463943497397
- ratio_max_to_10ms_ave_peaks = 0.0015594859153244159
- coe3[0] = 0.0
- coe3[1] = 0.0
- tdoa_mean = 0.0

## Evaluation
cv = 8
### robot-1
#### accuracy
- Mean = 0.8225
- Standard deviation = 0.03152380053229621
- Max = 0.89
- 75% = 0.835
- Median = 0.81
- 25% = 0.8
- Min = 0.79

#### f1
- Mean = 0.2084777308315539
- Standard deviation = 0.212659816229633
- Max = 0.6206896551724138
- 75% = 0.30676328502415456
- Median = 0.17090909090909093
- 25% = 0.0
- Min = 0.0

#### precision
- Mean = 0.5321428571428571
- Standard deviation = 0.45128783972727904
- Max = 1.0
- 75% = 1.0
- Median = 0.6285714285714286
- 25% = 0.0
- Min = 0.0

#### recall
- Mean = 0.1375
- Standard deviation = 0.15155444566227677
- Max = 0.45
- 75% = 0.1875
- Median = 0.1
- 25% = 0.0
- Min = 0.0

#### facing_probas
- Mean = [0.30494474 0.04775888 0.01248234 0.00178299 0.00616498]
- Standard deviation = [0.07954528 0.02093567 0.0110962  0.00217205 0.00755815]
- Max = [0.42867183 0.07458849 0.02877421 0.00553175 0.021     ]
- 75% = [0.35731974 0.06679752 0.02469921 0.0025997  0.00740506]
- Median = [0.31389464 0.04430496 0.00754127 0.00080754 0.00291567]
- 25% = [2.60771131e-01 3.46036706e-02 3.23105159e-03 8.33333333e-05
 8.48214286e-04]
- Min = [0.15917698 0.01151944 0.00025397 0.         0.        ]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 79.5 | 0.5 |
| Actual Positive | 17.25 | 2.75 |

### robot-2
#### accuracy
- Mean = 0.86
- Standard deviation = 0.021794494717703387
- Max = 0.9
- 75% = 0.88
- Median = 0.85
- 25% = 0.84
- Min = 0.84

#### f1
- Mean = 0.5970312855257776
- Standard deviation = 0.0723459727263322
- Max = 0.7368421052631577
- 75% = 0.6127906976744186
- Median = 0.5972972972972973
- 25% = 0.5674603174603176
- Min = 0.4666666666666667

#### precision
- Mean = 0.7323165316851378
- Standard deviation = 0.13895087668526704
- Max = 1.0
- 75% = 0.8083333333333333
- Median = 0.6735294117647059
- 25% = 0.6209239130434783
- Min = 0.6

#### recall
- Mean = 0.53125
- Standard deviation = 0.12231491119238078
- Max = 0.7
- 75% = 0.625
- Median = 0.525
- 25% = 0.4375
- Min = 0.35

#### facing_probas
- Mean = [0.29636617 0.52475174 0.18671379 0.05313795 0.01805794]
- Standard deviation = [0.07858437 0.04137186 0.01846098 0.02937751 0.00963434]
- Max = [0.40480714 0.59482341 0.2159381  0.10670556 0.03178294]
- 75% = [0.35451399 0.54214038 0.2009     0.07435754 0.02459335]
- Median = [0.31279464 0.51909444 0.18544385 0.04294365 0.01966151]
- 25% = [0.23090764 0.48909415 0.17889226 0.03321478 0.01213254]
- Min = [1.68709127e-01 4.79646032e-01 1.55295635e-01 1.94730159e-02
 1.66666667e-04]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 75.375 | 4.625 |
| Actual Positive | 9.375 | 10.625 |

### robot-3
#### accuracy
- Mean = 0.8075
- Standard deviation = 0.025372228912730523
- Max = 0.85
- 75% = 0.825
- Median = 0.8
- 25% = 0.7875000000000001
- Min = 0.78

#### f1
- Mean = 0.26064169981815494
- Standard deviation = 0.19034048222207522
- Max = 0.5161290322580645
- 75% = 0.39783653846153844
- Median = 0.32996632996633
- 25% = 0.06521739130434784
- Min = 0.0

#### precision
- Mean = 0.43877997002997005
- Standard deviation = 0.29027668268744494
- Max = 0.8333333333333334
- 75% = 0.6193181818181819
- Median = 0.5164835164835164
- 25% = 0.25
- Min = 0.0

#### recall
- Mean = 0.19375
- Standard deviation = 0.14882351124738322
- Max = 0.4
- 75% = 0.3125
- Median = 0.225
- 25% = 0.037500000000000006
- Min = 0.0

#### facing_probas
- Mean = [0.15564355 0.38727024 0.36027039 0.22563328 0.02372029]
- Standard deviation = [0.0354404  0.04521834 0.03713547 0.06144873 0.01557996]
- Max = [0.20579127 0.45097698 0.40750595 0.31444286 0.04999603]
- 75% = [0.17855744 0.41175357 0.38622173 0.25809355 0.03706815]
- Median = [0.15953155 0.39258194 0.36337083 0.2372123  0.02013214]
- 25% = [0.13640714 0.3681505  0.34181885 0.18917103 0.01058304]
- Min = [0.09091429 0.31354603 0.28312857 0.10724921 0.00309722]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 76.875 | 3.125 |
| Actual Positive | 16.125 | 3.875 |

### robot-4
#### accuracy
- Mean = 0.80625
- Standard deviation = 0.01996089927833912
- Max = 0.84
- 75% = 0.8150000000000001
- Median = 0.8
- 25% = 0.8
- Min = 0.77

#### f1
- Mean = 0.23719406609650512
- Standard deviation = 0.21116345524617283
- Max = 0.6190476190476191
- 75% = 0.3597560975609756
- Median = 0.20761904761904765
- 25% = 0.06818181818181818
- Min = 0.0

#### precision
- Mean = 0.47743506493506493
- Standard deviation = 0.3258245488891157
- Max = 1.0
- 75% = 0.6431818181818182
- Median = 0.5
- 25% = 0.3214285714285714
- Min = 0.0

#### recall
- Mean = 0.20625
- Standard deviation = 0.2214123697989794
- Max = 0.65
- 75% = 0.3
- Median = 0.125
- 25% = 0.037500000000000006
- Min = 0.0

#### facing_probas
- Mean = [0.02005635 0.1063567  0.28943686 0.36821101 0.19465794]
- Standard deviation = [0.01358866 0.01447246 0.04833927 0.10698437 0.04013296]
- Max = [0.04050913 0.12845794 0.39219921 0.53285119 0.24459206]
- 75% = [0.03185139 0.11231419 0.31677688 0.40526657 0.24104335]
- Median = [0.01584663 0.10982718 0.2689494  0.37400516 0.18090099]
- 25% = [0.00863343 0.10210089 0.25702331 0.33492599 0.17171736]
- Min = [0.00334722 0.08214921 0.23694921 0.15845714 0.13686548]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 76.5 | 3.5 |
| Actual Positive | 15.875 | 4.125 |

### robot-5
#### accuracy
- Mean = 0.9025
- Standard deviation = 0.027726341266023528
- Max = 0.94
- 75% = 0.925
- Median = 0.9
- 25% = 0.88
- Min = 0.86

#### f1
- Mean = 0.696472571767813
- Standard deviation = 0.11431724018291256
- Max = 0.85
- 75% = 0.7938596491228069
- Median = 0.6783681214421252
- 25% = 0.6338709677419354
- Min = 0.4999999999999999

#### precision
- Mean = 0.8854617604617605
- Standard deviation = 0.05626548968622851
- Max = 1.0
- 75% = 0.9022727272727273
- Median = 0.8819444444444444
- 25% = 0.86875
- Min = 0.7857142857142857

#### recall
- Mean = 0.59375
- Standard deviation = 0.1628601777599423
- Max = 0.85
- 75% = 0.725
- Median = 0.55
- 25% = 0.4875
- Min = 0.35

#### facing_probas
- Mean = [0.0044939  0.01290942 0.20774296 0.4087937  0.60575481]
- Standard deviation = [0.00585771 0.00955774 0.0391868  0.13754708 0.0407555 ]
- Max = [0.0185     0.02828135 0.26678651 0.60695119 0.65737937]
- 75% = [0.00624812 0.01710714 0.22633988 0.46776468 0.64361796]
- Median = [0.00228175 0.01144365 0.21664484 0.41908849 0.60748611]
- 25% = [0.         0.00616815 0.19114028 0.35573393 0.57630506]
- Min = [0.00000000e+00 5.00000000e-04 1.38988889e-01 1.42620635e-01
 5.35460714e-01]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 78.375 | 1.625 |
| Actual Positive | 8.125 | 11.875 |

### robot-6
#### accuracy
- Mean = 0.3325
- Standard deviation = 0.07529110173187797
- Max = 0.47
- 75% = 0.3725
- Median = 0.33
- 25% = 0.2675
- Min = 0.23

#### f1
- Mean = 0.49434850458047264
- Standard deviation = 0.0835426344082327
- Max = 0.6394557823129251
- 75% = 0.5424488944513975
- Median = 0.49624060150375937
- 25% = 0.4220722409698788
- Min = 0.3739837398373984

#### precision
- Mean = 1.0
- Standard deviation = 0.0
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 1.0
- Min = 1.0

#### recall
- Mean = 0.3325
- Standard deviation = 0.07529110173187797
- Max = 0.47
- 75% = 0.3725
- Median = 0.33
- 25% = 0.2675
- Min = 0.23

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
| Actual Positive | 66.75 | 33.25 |

