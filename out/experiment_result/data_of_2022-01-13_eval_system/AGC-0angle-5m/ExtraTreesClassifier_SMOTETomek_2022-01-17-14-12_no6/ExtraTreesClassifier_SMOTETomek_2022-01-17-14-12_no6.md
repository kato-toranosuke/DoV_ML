# ExtraTreesClassifier_SMOTETomek_2022-01-17-14-12_no6
## Constants
- CSV_PATH = ../out/csv/experiment
- OUTPUT_PATH = ../out/experiment_result/data_of_2022-01-13_eval_system/AGC-0angle-5m
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
- AGC_STATUS = ['AGC']

## Loaded CSV
- 2021-12-27_AGC.csv
- 2022-01-10_NoAGC.csv
- 2022-01-13_raspi_48000Hz_w1_N2^12_overlap80.csv

## Estimator
### Type
- resampler = SMOTETomek
- estimator = ExtraTreesClassifier

### Arguments for hyperparameter search
- resampler = SMOTETomek
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
	- tomek = None
	- n_jobs = -1
	- n_features_in_ = 36
	- sampling_strategy_ = auto
	- smote_ = SMOTE(n_jobs=-1, random_state=42)
	- tomek_ = TomekLinks(n_jobs=-1, sampling_strategy='all')

- best_estimator
	- base_estimator = ExtraTreeClassifier()
	- n_estimators = 310
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
	- oob_decision_function_ = [[0.93650794 0.06349206]
 [0.99447514 0.00552486]
 [1.         0.        ]
 [0.30612245 0.69387755]
 [0.36216216 0.63783784]
 [0.2974359  0.7025641 ]
 [0.92105263 0.07894737]
 [1.         0.        ]
 [0.99428571 0.00571429]
 [0.20418848 0.79581152]
 [1.         0.        ]
 [0.98974359 0.01025641]
 [0.96842105 0.03157895]
 [0.77222222 0.22777778]
 [0.22222222 0.77777778]
 [0.64021164 0.35978836]
 [0.95918367 0.04081633]
 [0.33333333 0.66666667]
 [0.5027027  0.4972973 ]
 [0.10769231 0.89230769]
 [0.68367347 0.31632653]
 [0.49489796 0.50510204]
 [0.97590361 0.02409639]
 [0.97395833 0.02604167]
 [1.         0.        ]
 [0.20108696 0.79891304]
 [0.12371134 0.87628866]
 [0.30054645 0.69945355]
 [0.98870056 0.01129944]
 [1.         0.        ]
 [1.         0.        ]
 [0.98924731 0.01075269]
 [0.9144385  0.0855615 ]
 [0.98941799 0.01058201]
 [0.92655367 0.07344633]
 [0.98395722 0.01604278]
 [0.98850575 0.01149425]
 [0.98477157 0.01522843]
 [0.9939759  0.0060241 ]
 [0.63101604 0.36898396]
 [0.44680851 0.55319149]
 [0.02150538 0.97849462]
 [0.25280899 0.74719101]
 [0.99487179 0.00512821]
 [0.97512438 0.02487562]
 [1.         0.        ]
 [0.98351648 0.01648352]
 [0.86934673 0.13065327]
 [0.65533981 0.34466019]
 [0.00564972 0.99435028]
 [0.05555556 0.94444444]
 [0.015625   0.984375  ]
 [0.02659574 0.97340426]
 [0.16666667 0.83333333]
 [0.13297872 0.86702128]
 [0.04371585 0.95628415]
 [0.01129944 0.98870056]
 [0.24404762 0.75595238]
 [0.02173913 0.97826087]
 [0.01578947 0.98421053]
 [0.02645503 0.97354497]
 [0.08888889 0.91111111]
 [0.33513514 0.66486486]
 [0.10404624 0.89595376]
 [0.00609756 0.99390244]
 [0.35106383 0.64893617]
 [0.05235602 0.94764398]
 [0.37823834 0.62176166]
 [0.08762887 0.91237113]
 [0.18134715 0.81865285]
 [0.08648649 0.91351351]
 [0.04268293 0.95731707]
 [0.06951872 0.93048128]
 [0.01554404 0.98445596]
 [0.03645833 0.96354167]
 [0.0199005  0.9800995 ]
 [0.33333333 0.66666667]
 [0.12765957 0.87234043]
 [0.32160804 0.67839196]
 [0.41397849 0.58602151]
 [0.00534759 0.99465241]
 [0.02824859 0.97175141]
 [0.23589744 0.76410256]
 [0.05913978 0.94086022]]
	- oob_score_ = 0.8928571428571429

#### Importance of features
- gp_max_val_min = 0.16233106155793986
- gp_auc_min = 0.13432747026162925
- high_power = 0.08618354604524632
- gp_max_val_mean = 0.0756915799810687
- gp_max_val_max = 0.07296826371807531
- gp_auc_mean = 0.07280279092302919
- diff_std = 0.05246983724859312
- gp_auc_max = 0.0475039442613881
- hlbr = 0.037098017672072665
- diff_auc = 0.032109124883376874
- ratio_max_to_9th_ave_peaks = 0.023740558241083905
- srmr = 0.023257581984554434
- ac_auc = 0.01798507405101038
- ac_std = 0.015376557485891177
- tdoa_mean = 0.014074205849545645
- ratio_max_to_10ms_ave_peaks = 0.012914712062887683
- gp_max_ix_mean = 0.010658745464207066
- gp_max_val_range = 0.009998403880789387
- gp_auc_range = 0.009010287905197416
- tdoa_max = 0.00855714224361917
- gp_auc_std = 0.0084709601757224
- coe3[3] = 0.007383036666291403
- gp_max_val_std = 0.007088814499958055
- low_power = 0.007075070142674698
- tdoa_std = 0.006080490941293067
- coe1[0] = 0.005858995367675
- gp_max_ix_std = 0.005749132050628986
- coe1[1] = 0.005370479241281765
- gp_max_ix_min = 0.005268042364983053
- coe3[2] = 0.005183486374518172
- tdoa_range = 0.004853528411831151
- gp_max_ix_max = 0.004825158444593479
- tdoa_min = 0.004021905802827916
- gp_max_ix_range = 0.003711993794515195
- coe3[0] = 0.0
- coe3[1] = 0.0

## Evaluation
cv = 8
### robot-1
#### accuracy
- Mean = 0.9612499999999999
- Standard deviation = 0.03982383080518498
- Max = 0.99
- 75% = 0.9824999999999999
- Median = 0.975
- 25% = 0.96
- Min = 0.86

#### f1
- Mean = 0.8802717019822283
- Standard deviation = 0.16038863324602554
- Max = 0.9743589743589743
- 75% = 0.9578754578754578
- Median = 0.9352226720647774
- 25% = 0.9068181818181817
- Min = 0.4615384615384615

#### precision
- Mean = 0.9487240829346093
- Standard deviation = 0.05892640147146858
- Max = 1.0
- 75% = 1.0
- Median = 0.9736842105263157
- 25% = 0.9068181818181817
- Min = 0.8333333333333334

#### recall
- Mean = 0.8625
- Standard deviation = 0.21614520582238228
- Max = 1.0
- 75% = 0.9624999999999999
- Median = 0.925
- 25% = 0.9
- Min = 0.3

#### facing_probas
- Mean = [0.79155242 0.17788306 0.0083871  0.00453629 0.00135081]
- Standard deviation = [0.12735556 0.06676959 0.00331725 0.00349431 0.00167606]
- Max = [0.91112903 0.26758065 0.01370968 0.01177419 0.00532258]
- 75% = [0.8625     0.21241935 0.01052419 0.00568548 0.00165323]
- Median = [8.25483871e-01 2.03467742e-01 8.30645161e-03 3.54838710e-03
 8.06451613e-04]
- 25% = [7.80887097e-01 1.57056452e-01 5.24193548e-03 1.77419355e-03
 1.20967742e-04]
- Min = [0.47548387 0.03870968 0.00435484 0.00080645 0.        ]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 78.875 | 1.125 |
| Actual Positive | 2.75 | 17.25 |

### robot-2
#### accuracy
- Mean = 0.9275
- Standard deviation = 0.03526683994916469
- Max = 0.97
- 75% = 0.9524999999999999
- Median = 0.94
- 25% = 0.905
- Min = 0.86

#### f1
- Mean = 0.813165467770731
- Standard deviation = 0.09277842228667176
- Max = 0.9189189189189189
- 75% = 0.8739177489177489
- Median = 0.849624060150376
- 25% = 0.7564102564102564
- Min = 0.631578947368421

#### precision
- Mean = 0.8421467969165337
- Standard deviation = 0.11162825954708133
- Max = 1.0
- 75% = 0.9166666666666666
- Median = 0.8276515151515151
- 25% = 0.7763157894736842
- Min = 0.6666666666666666

#### recall
- Mean = 0.79375
- Standard deviation = 0.11301963325015701
- Max = 0.95
- 75% = 0.875
- Median = 0.775
- 25% = 0.7375
- Min = 0.6

#### facing_probas
- Mean = [0.38921371 0.69163306 0.09697581 0.01163306 0.00245968]
- Standard deviation = [0.10484406 0.07299307 0.04014896 0.00674361 0.00380723]
- Max = [0.53483871 0.83096774 0.15758065 0.02516129 0.01225806]
- 75% = [0.45532258 0.72693548 0.12576613 0.01483871 0.00229839]
- Median = [0.40177419 0.69282258 0.09209677 0.00919355 0.00112903]
- 25% = [3.17822581e-01 6.36693548e-01 6.11290323e-02 7.50000000e-03
 2.82258065e-04]
- Min = [0.19725806 0.58806452 0.04419355 0.0033871  0.        ]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 76.875 | 3.125 |
| Actual Positive | 4.125 | 15.875 |

### robot-3
#### accuracy
- Mean = 0.95375
- Standard deviation = 0.026427968139832454
- Max = 0.99
- 75% = 0.965
- Median = 0.96
- 25% = 0.945
- Min = 0.9

#### f1
- Mean = 0.8738143052568599
- Standard deviation = 0.07040737973517401
- Max = 0.975609756097561
- 75% = 0.9078947368421053
- Median = 0.888888888888889
- 25% = 0.8398268398268398
- Min = 0.75

#### precision
- Mean = 0.9558531746031746
- Standard deviation = 0.08082578170692911
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 0.9503968253968254
- Min = 0.75

#### recall
- Mean = 0.8125
- Standard deviation = 0.09921567416492214
- Max = 1.0
- 75% = 0.8625
- Median = 0.8
- 25% = 0.75
- Min = 0.65

#### facing_probas
- Mean = [0.01802419 0.68252016 0.81606855 0.25649194 0.00502016]
- Standard deviation = [0.00799476 0.1104315  0.07779123 0.09956454 0.00325734]
- Max = [0.03129032 0.89806452 0.95241935 0.38306452 0.01209677]
- 75% = [0.02290323 0.72572581 0.84556452 0.32891129 0.00516129]
- Median = [0.01524194 0.70459677 0.83040323 0.27524194 0.00362903]
- 25% = [0.01233871 0.59854839 0.79564516 0.20931452 0.00334677]
- Min = [0.00758065 0.51548387 0.68016129 0.05258065 0.0016129 ]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 79.125 | 0.875 |
| Actual Positive | 3.75 | 16.25 |

### robot-4
#### accuracy
- Mean = 0.925
- Standard deviation = 0.03240370349203929
- Max = 0.96
- 75% = 0.95
- Median = 0.93
- 25% = 0.9175
- Min = 0.85

#### f1
- Mean = 0.8242595195836508
- Standard deviation = 0.061697757749549414
- Max = 0.9
- 75% = 0.8780487804878048
- Median = 0.8336951801997394
- 25% = 0.7911764705882354
- Min = 0.7058823529411764

#### precision
- Mean = 0.8109039438294166
- Standard deviation = 0.11921200672941229
- Max = 0.9333333333333333
- 75% = 0.9071428571428571
- Median = 0.8571428571428571
- 25% = 0.7279693486590038
- Min = 0.5806451612903226

#### recall
- Mean = 0.86875
- Standard deviation = 0.11973277537917511
- Max = 1.0
- 75% = 0.925
- Median = 0.9
- 25% = 0.85
- Min = 0.65

#### facing_probas
- Mean = [0.00360887 0.02512097 0.46620968 0.81352823 0.24068548]
- Standard deviation = [0.0042505  0.00924566 0.08706085 0.08011119 0.06588694]
- Max = [0.0133871  0.04129032 0.55822581 0.92032258 0.32774194]
- 75% = [0.00399194 0.03193548 0.52169355 0.86096774 0.28552419]
- Median = [0.00177419 0.02419355 0.48741935 0.82596774 0.24451613]
- 25% = [0.00108871 0.01645161 0.44629032 0.78975806 0.21125   ]
- Min = [0.         0.01387097 0.28274194 0.64274194 0.11064516]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 75.125 | 4.875 |
| Actual Positive | 2.625 | 17.375 |

### robot-5
#### accuracy
- Mean = 0.9412499999999999
- Standard deviation = 0.02934173648576373
- Max = 0.98
- 75% = 0.9624999999999999
- Median = 0.95
- 25% = 0.9175
- Min = 0.89

#### f1
- Mean = 0.8197174208808963
- Standard deviation = 0.10720023115590548
- Max = 0.9473684210526316
- 75% = 0.8983739837398375
- Median = 0.8571428571428571
- 25% = 0.7399193548387096
- Min = 0.6206896551724138

#### precision
- Mean = 0.9880952380952381
- Standard deviation = 0.031497039417435604
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 1.0
- Min = 0.9047619047619048

#### recall
- Mean = 0.71875
- Standard deviation = 0.16189792308735773
- Max = 0.95
- 75% = 0.8250000000000001
- Median = 0.75
- 25% = 0.5875
- Min = 0.45

#### facing_probas
- Mean = [0.00209677 0.00330645 0.00987903 0.526875   0.75919355]
- Standard deviation = [0.00191861 0.00464183 0.00440588 0.13222799 0.0712436 ]
- Max = [0.005      0.015      0.01935484 0.73532258 0.86903226]
- 75% = [0.00395161 0.00326613 0.01241935 0.5875     0.79830645]
- Median = [0.00137097 0.00112903 0.00806452 0.54532258 0.7741129 ]
- 25% = [3.22580645e-04 8.06451613e-04 6.65322581e-03 4.55967742e-01
 7.08588710e-01]
- Min = [0.         0.         0.00532258 0.26645161 0.65032258]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 79.75 | 0.25 |
| Actual Positive | 5.625 | 14.375 |

### robot-6
#### accuracy
- Mean = 0.81125
- Standard deviation = 0.08695365144719341
- Max = 0.9
- 75% = 0.86
- Median = 0.82
- 25% = 0.8075000000000001
- Min = 0.6

#### f1
- Mean = 0.8930250746458219
- Standard deviation = 0.057673915409614404
- Max = 0.9473684210526316
- 75% = 0.9246389246389246
- Median = 0.9010989010989011
- 25% = 0.8934929404542664
- Min = 0.7499999999999999

#### precision
- Mean = 1.0
- Standard deviation = 0.0
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 1.0
- Min = 1.0

#### recall
- Mean = 0.81125
- Standard deviation = 0.08695365144719341
- Max = 0.9
- 75% = 0.86
- Median = 0.82
- 25% = 0.8075000000000001
- Min = 0.6

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
| Actual Positive | 18.875 | 81.125 |

