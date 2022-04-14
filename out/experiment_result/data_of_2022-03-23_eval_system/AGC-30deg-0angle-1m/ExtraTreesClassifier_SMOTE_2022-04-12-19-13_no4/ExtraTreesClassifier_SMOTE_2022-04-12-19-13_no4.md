# ExtraTreesClassifier_SMOTE_2022-04-12-19-13_no4
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
- resampler = SMOTE
- estimator = ExtraTreesClassifier

### Arguments for hyperparameter search
- resampler = SMOTE
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
	- k_neighbors = 5
	- n_jobs = -1
	- n_features_in_ = 36
	- sampling_strategy_ = OrderedDict([(1, 45)])
	- nn_k_ = NearestNeighbors(n_neighbors=6)

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
	- min_samples_split = 10
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
- gp_max_ix_range = 0.14136923606224852
- tdoa_range = 0.09035391359240433
- tdoa_mean = 0.0839222393026992
- tdoa_max = 0.07787711535900634
- gp_auc_min = 0.062249560000774355
- gp_auc_max = 0.050530625252266245
- gp_max_ix_std = 0.04847120406902241
- gp_max_val_max = 0.04320196504872779
- gp_max_val_std = 0.03663780185276621
- ac_auc = 0.03431206156835708
- gp_auc_mean = 0.03352336149297089
- gp_max_val_range = 0.026157994310968616
- gp_max_val_mean = 0.02599045907544064
- gp_max_ix_min = 0.02474414430876678
- gp_max_ix_mean = 0.022606902859292014
- tdoa_std = 0.019580016395785837
- gp_max_ix_max = 0.01907844325493338
- gp_max_val_min = 0.018685492436494935
- ratio_max_to_9th_ave_peaks = 0.015974325124190187
- srmr = 0.014792438106844259
- coe1[0] = 0.014693678458467165
- coe3[3] = 0.013582047317277626
- diff_std = 0.01355218089899269
- gp_auc_range = 0.010402652301785787
- high_power = 0.010205968003445974
- ac_std = 0.010008851775091409
- gp_auc_std = 0.007880666126522511
- diff_auc = 0.005769474041535826
- tdoa_min = 0.005382339213618582
- coe3[2] = 0.005323957154090419
- coe1[1] = 0.005192172259831789
- low_power = 0.004053528115902731
- ratio_max_to_10ms_ave_peaks = 0.0035510413302671843
- hlbr = 0.00034214352921050647
- coe3[0] = 0.0
- coe3[1] = 0.0

## Evaluation
cv = 8
### robot-1
#### accuracy
- Mean = 0.97625
- Standard deviation = 0.016535945694153707
- Max = 1.0
- 75% = 0.99
- Median = 0.98
- 25% = 0.96
- Min = 0.95

#### f1
- Mean = 0.9388501815062402
- Standard deviation = 0.04166461578872278
- Max = 1.0
- 75% = 0.9743589743589743
- Median = 0.9473684210526316
- 25% = 0.8932748538011697
- Min = 0.8837209302325583

#### precision
- Mean = 0.971316425120773
- Standard deviation = 0.05782536932668489
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 0.9861111111111112
- Min = 0.8260869565217391

#### recall
- Mean = 0.9125000000000001
- Standard deviation = 0.05994789404140897
- Max = 1.0
- 75% = 0.95
- Median = 0.925
- 25% = 0.8875
- Min = 0.8

#### facing_probas
- Mean = [0.75812847 0.05253398 0.01883978 0.00703125 0.00604167]
- Standard deviation = [0.0538512  0.04339766 0.02329793 0.00914163 0.00785889]
- Max = [0.82085913 0.12914087 0.0581746  0.0275     0.02      ]
- 75% = [0.79348016 0.08183333 0.02968353 0.009375   0.00833333]
- Median = [0.78121925 0.02708333 0.00510714 0.003125   0.0025    ]
- 25% = [0.71115873 0.02087004 0.001875   0.         0.        ]
- Min = [0.66729365 0.01107143 0.00071429 0.         0.        ]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 79.375 | 0.625 |
| Actual Positive | 1.75 | 18.25 |

### robot-2
#### accuracy
- Mean = 0.8775
- Standard deviation = 0.03269174207655506
- Max = 0.94
- 75% = 0.8925000000000001
- Median = 0.88
- 25% = 0.855
- Min = 0.83

#### f1
- Mean = 0.6816260349348584
- Standard deviation = 0.09494966035487785
- Max = 0.8571428571428572
- 75% = 0.7145270270270271
- Median = 0.6909090909090909
- 25% = 0.6352941176470588
- Min = 0.5142857142857143

#### precision
- Mean = 0.7054502482811307
- Standard deviation = 0.0816915620525886
- Max = 0.8181818181818182
- 75% = 0.7699579831932772
- Median = 0.725
- 25% = 0.61875
- Min = 0.6

#### recall
- Mean = 0.66875
- Standard deviation = 0.12975337182516686
- Max = 0.9
- 75% = 0.75
- Median = 0.675
- 25% = 0.5875
- Min = 0.45

#### facing_probas
- Mean = [2.29154514e-01 6.74344246e-01 5.28193700e-01 1.00031746e-01
 6.25000000e-04]
- Standard deviation = [0.10329578 0.07804489 0.06731465 0.06278802 0.00165359]
- Max = [0.43754563 0.81377579 0.59169841 0.22259921 0.005     ]
- 75% = [0.26694742 0.71535169 0.57573413 0.11662897 0.        ]
- Median = [0.23894345 0.68803274 0.56340278 0.09145238 0.        ]
- 25% = [0.13444643 0.59485615 0.49353075 0.05424702 0.        ]
- Min = [0.10283135 0.57124405 0.4162996  0.02309524 0.        ]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 74.375 | 5.625 |
| Actual Positive | 6.625 | 13.375 |

### robot-3
#### accuracy
- Mean = 0.83375
- Standard deviation = 0.022325713874364675
- Max = 0.88
- 75% = 0.84
- Median = 0.835
- 25% = 0.825
- Min = 0.8

#### f1
- Mean = 0.4147753597753598
- Standard deviation = 0.1565434541775566
- Max = 0.6
- 75% = 0.4987714987714988
- Median = 0.4666666666666667
- 25% = 0.38142857142857134
- Min = 0.09090909090909091

#### precision
- Mean = 0.6692024886877829
- Standard deviation = 0.11432586057535776
- Max = 0.9
- 75% = 0.7124999999999999
- Median = 0.6576923076923077
- 25% = 0.5970588235294118
- Min = 0.5

#### recall
- Mean = 0.31875
- Standard deviation = 0.14128318194321646
- Max = 0.5
- 75% = 0.41250000000000003
- Median = 0.35
- 25% = 0.2625
- Min = 0.05

#### facing_probas
- Mean = [0.04165303 0.48007564 0.47913963 0.27554687 0.11263864]
- Standard deviation = [0.04623659 0.09552546 0.10588058 0.13352175 0.06609274]
- Max = [0.13265278 0.66560317 0.60126587 0.43479167 0.23281746]
- 75% = [0.07189583 0.53103919 0.54351687 0.39866369 0.12836359]
- Median = [0.0103373  0.44227877 0.5037996  0.28121528 0.08861607]
- 25% = [0.00759524 0.41743056 0.43996577 0.20130109 0.06786954]
- Min = [0.00625    0.37016468 0.29575    0.03828571 0.04673016]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 77.0 | 3.0 |
| Actual Positive | 13.625 | 6.375 |

### robot-4
#### accuracy
- Mean = 0.7975
- Standard deviation = 0.05068283733178323
- Max = 0.88
- 75% = 0.8374999999999999
- Median = 0.78
- 25% = 0.7675000000000001
- Min = 0.72

#### f1
- Mean = 0.48126853560620453
- Standard deviation = 0.10115058905497386
- Max = 0.6470588235294117
- 75% = 0.5860832137733142
- Median = 0.424812030075188
- 25% = 0.41506410256410253
- Min = 0.3529411764705882

#### precision
- Mean = 0.5164663552821447
- Standard deviation = 0.1472997403254301
- Max = 0.7857142857142857
- 75% = 0.6071428571428571
- Median = 0.4365079365079365
- 25% = 0.4180622009569378
- Min = 0.35714285714285715

#### recall
- Mean = 0.4625
- Standard deviation = 0.08926785535678562
- Max = 0.6
- 75% = 0.5125
- Median = 0.475
- 25% = 0.4
- Min = 0.3

#### facing_probas
- Mean = [0.01       0.11588864 0.18340427 0.59899454 0.52292237]
- Standard deviation = [0.01205376 0.02549592 0.05001953 0.05548957 0.04467485]
- Max = [0.03277778 0.15041667 0.27705952 0.69685913 0.58507738]
- 75% = [0.0175     0.13463046 0.22199603 0.62597321 0.55646429]
- Median = [0.00333333 0.11925992 0.16567857 0.60023611 0.52910813]
- 25% = [4.16666667e-04 1.03441468e-01 1.51915179e-01 5.80271329e-01
 4.89971726e-01]
- Min = [0.         0.06800794 0.1199504  0.49425397 0.44752778]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 70.5 | 9.5 |
| Actual Positive | 10.75 | 9.25 |

### robot-5
#### accuracy
- Mean = 0.8225
- Standard deviation = 0.06077622890571609
- Max = 0.91
- 75% = 0.8925000000000001
- Median = 0.785
- 25% = 0.7775000000000001
- Min = 0.76

#### f1
- Mean = 0.44870495175373226
- Standard deviation = 0.24988338608884636
- Max = 0.7804878048780488
- 75% = 0.7075825825825827
- Median = 0.4252136752136752
- 25% = 0.26573426573426573
- Min = 0.07692307692307691

#### precision
- Mean = 0.5168637799249254
- Standard deviation = 0.22103329246002637
- Max = 0.8125
- 75% = 0.7626050420168067
- Median = 0.45559210526315785
- 25% = 0.3717948717948718
- Min = 0.16666666666666666

#### recall
- Mean = 0.4125
- Standard deviation = 0.25586861863073407
- Max = 0.8
- 75% = 0.65
- Median = 0.4
- 25% = 0.2125
- Min = 0.05

#### facing_probas
- Mean = [0.00145833 0.02505754 0.01364683 0.5726193  0.58958755]
- Standard deviation = [0.00198737 0.01704528 0.01631079 0.12069079 0.10733058]
- Max = [0.005      0.05684722 0.04472222 0.73558333 0.74215079]
- 75% = [0.00291667 0.0354003  0.01833333 0.66288591 0.67277728]
- Median = [0.         0.02327381 0.00460714 0.59411607 0.60913393]
- 25% = [0.         0.0142877  0.00285714 0.48768056 0.51294544]
- Min = [0.         0.00222222 0.         0.39298016 0.38722817]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 74.0 | 6.0 |
| Actual Positive | 11.75 | 8.25 |

### robot-6
#### accuracy
- Mean = 0.555
- Standard deviation = 0.06020797289396147
- Max = 0.62
- 75% = 0.5925
- Median = 0.565
- 25% = 0.5475000000000001
- Min = 0.41

#### f1
- Mean = 0.7117712794396296
- Standard deviation = 0.05312242235218216
- Max = 0.7654320987654321
- 75% = 0.7441037735849056
- Median = 0.7220316838151233
- 25% = 0.7075827398408043
- Min = 0.5815602836879432

#### precision
- Mean = 1.0
- Standard deviation = 0.0
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 1.0
- Min = 1.0

#### recall
- Mean = 0.555
- Standard deviation = 0.06020797289396147
- Max = 0.62
- 75% = 0.5925
- Median = 0.565
- 25% = 0.5475000000000001
- Min = 0.41

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
| Actual Positive | 44.5 | 55.5 |

