# ExtraTreesClassifier_SMOTEENN_2022-01-19-20-22_no5
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
- gp_auc_mean = 0.11458268275723518
- high_power = 0.08842979110836253
- coe1[0] = 0.08080324437467294
- coe3[3] = 0.06636150400331074
- coe1[1] = 0.06245670995670997
- gp_max_val_max = 0.05856517425810905
- diff_std = 0.054910628218898895
- gp_max_ix_range = 0.0499837431087431
- gp_max_ix_mean = 0.04629329004329004
- ac_auc = 0.044758898508898505
- gp_auc_min = 0.042871315192743766
- ratio_max_to_9th_ave_peaks = 0.03454435941043084
- hlbr = 0.034259474540804455
- gp_max_val_mean = 0.03333616780045351
- diff_auc = 0.031558061821219716
- low_power = 0.022152777777777778
- gp_max_ix_max = 0.019696275946275953
- tdoa_min = 0.013098155929038286
- gp_auc_range = 0.01294642857142857
- tdoa_mean = 0.01294642857142857
- gp_max_val_min = 0.012275132275132269
- ratio_max_to_10ms_ave_peaks = 0.011534740707877337
- coe3[2] = 0.011507936507936507
- gp_max_val_std = 0.009494047619047626
- gp_max_val_range = 0.009124149659863945
- ac_std = 0.008630952380952382
- srmr = 0.0061649659863945595
- tdoa_range = 0.003835978835978836
- gp_auc_max = 0.002876984126984128
- coe3[0] = 0.0
- coe3[1] = 0.0
- gp_max_ix_std = 0.0
- gp_max_ix_min = 0.0
- gp_auc_std = 0.0
- tdoa_std = 0.0
- tdoa_max = 0.0

## Evaluation
cv = 8
### robot-1
#### accuracy
- Mean = 0.9335981047937569
- Standard deviation = 0.02029889169775777
- Max = 0.9732441471571907
- 75% = 0.9391220735785953
- Median = 0.9331103678929766
- 25% = 0.9255852842809364
- Min = 0.8966666666666666

#### f1
- Mean = 0.8287949786904893
- Standard deviation = 0.04827684243394576
- Max = 0.9354838709677419
- 75% = 0.8335517693315859
- Median = 0.8246087425796007
- 25% = 0.8059568188878533
- Min = 0.7596899224806202

#### precision
- Mean = 0.8635932289239885
- Standard deviation = 0.0676303138025314
- Max = 0.9230769230769231
- 75% = 0.9183673469387755
- Median = 0.8844975490196079
- 25% = 0.8370914043583535
- Min = 0.7101449275362319

#### recall
- Mean = 0.8020833333333334
- Standard deviation = 0.06893913378239291
- Max = 0.9666666666666667
- 75% = 0.8166666666666667
- Median = 0.7916666666666667
- 25% = 0.75
- Min = 0.7333333333333333

#### facing_probas
- Mean = [0.838125   0.68770833 0.219375   0.025625   0.02625   ]
- Standard deviation = [0.06111486 0.09095915 0.09565178 0.03523667 0.03218598]
- Max = [0.945      0.81333333 0.34833333 0.11166667 0.09833333]
- 75% = [0.87166667 0.75125    0.29583333 0.03375    0.03291667]
- Median = [0.82833333 0.70166667 0.22416667 0.00666667 0.01083333]
- 25% = [0.79875    0.61       0.13833333 0.00333333 0.00541667]
- Min = [0.75166667 0.53666667 0.075      0.00166667 0.        ]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 231.25 | 8.0 |
| Actual Positive | 11.875 | 48.125 |

### robot-2
#### accuracy
- Mean = 0.8959852285395763
- Standard deviation = 0.046240695527250575
- Max = 0.9632107023411371
- 75% = 0.923913043478261
- Median = 0.9048216276477146
- 25% = 0.8731939799331104
- Min = 0.8193979933110368

#### f1
- Mean = 0.6926751924029255
- Standard deviation = 0.15294000434768137
- Max = 0.9043478260869566
- 75% = 0.7880952380952381
- Median = 0.7307831434255743
- 25% = 0.621828968903437
- Min = 0.4375

#### precision
- Mean = 0.816761129444953
- Standard deviation = 0.1372350348728014
- Max = 0.972972972972973
- 75% = 0.9479797979797979
- Median = 0.8352272727272727
- 25% = 0.7312091503267975
- Min = 0.5833333333333334

#### recall
- Mean = 0.6083333333333333
- Standard deviation = 0.16520189667999174
- Max = 0.8666666666666667
- 75% = 0.7041666666666666
- Median = 0.6416666666666666
- 25% = 0.5291666666666667
- Min = 0.35

#### facing_probas
- Mean = [0.80375    0.81875    0.70479167 0.225625   0.03479167]
- Standard deviation = [0.05603044 0.052346   0.07044717 0.12084465 0.03860805]
- Max = [0.89166667 0.89166667 0.82833333 0.44333333 0.12666667]
- 75% = [0.8425     0.85791667 0.73666667 0.3025     0.04458333]
- Median = [0.7975     0.81166667 0.71583333 0.19583333 0.02333333]
- 25% = [0.75791667 0.78833333 0.67416667 0.12375    0.005     ]
- Min = [0.72833333 0.73333333 0.56833333 0.09166667 0.00333333]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 231.625 | 7.625 |
| Actual Positive | 23.5 | 36.5 |

### robot-3
#### accuracy
- Mean = 0.8951602564102564
- Standard deviation = 0.015905691798570726
- Max = 0.9130434782608695
- 75% = 0.9105351170568561
- Median = 0.896505016722408
- 25% = 0.8840635451505017
- Min = 0.8695652173913043

#### f1
- Mean = 0.6471583243377507
- Standard deviation = 0.07185826930653005
- Max = 0.7291666666666666
- 75% = 0.7176931690929451
- Median = 0.6544308490915833
- 25% = 0.5920425889604931
- Min = 0.5411764705882353

#### precision
- Mean = 0.9791684704184704
- Standard deviation = 0.02606382578589788
- Max = 1.0
- 75% = 1.0
- Median = 0.9861111111111112
- 25% = 0.970995670995671
- Min = 0.92

#### recall
- Mean = 0.48750000000000004
- Standard deviation = 0.0789470638395684
- Max = 0.5833333333333334
- 75% = 0.5666666666666667
- Median = 0.4916666666666667
- 25% = 0.42083333333333334
- Min = 0.38333333333333336

#### facing_probas
- Mean = [0.44291667 0.83333333 0.91416667 0.80416667 0.26333333]
- Standard deviation = [0.09133938 0.05975645 0.0421637  0.0769289  0.10272333]
- Max = [0.52333333 0.9        0.97       0.89333333 0.44666667]
- 75% = [0.51208333 0.89041667 0.94458333 0.84708333 0.31875   ]
- Median = [0.49333333 0.83916667 0.91583333 0.835      0.25666667]
- 25% = [0.38416667 0.79666667 0.8975     0.78708333 0.20875   ]
- Min = [0.28166667 0.71666667 0.83       0.64333333 0.09333333]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 238.625 | 0.625 |
| Actual Positive | 30.75 | 29.25 |

### robot-4
#### accuracy
- Mean = 0.8663391861761427
- Standard deviation = 0.040856519922280794
- Max = 0.9163879598662207
- 75% = 0.8890886287625418
- Median = 0.8745819397993311
- 25% = 0.8554905239687849
- Min = 0.7792642140468228

#### f1
- Mean = 0.6494080559998021
- Standard deviation = 0.11373452319328162
- Max = 0.7787610619469028
- 75% = 0.7010135135135135
- Median = 0.6642358660707285
- 25% = 0.6435585231736056
- Min = 0.3773584905660377

#### precision
- Mean = 0.6767672606963264
- Standard deviation = 0.12094381940112546
- Max = 0.8148148148148148
- 75% = 0.7644397381594147
- Median = 0.7017482517482517
- 25% = 0.6332712022367195
- Min = 0.425531914893617

#### recall
- Mean = 0.6285663841807909
- Standard deviation = 0.1173984108750094
- Max = 0.7457627118644068
- 75% = 0.7029661016949152
- Median = 0.6440677966101694
- 25% = 0.6245056497175141
- Min = 0.3389830508474576

#### facing_probas
- Mean = [0.06440325 0.31003531 0.84748941 0.91973164 0.73162782]
- Standard deviation = [0.05983566 0.09907506 0.05968086 0.03983067 0.09142229]
- Max = [0.20677966 0.50169492 0.9        0.96610169 0.83220339]
- 75% = [0.07663136 0.38167373 0.88389831 0.94892655 0.81845339]
- Median = [0.04466102 0.27288136 0.8764548  0.92881356 0.74576271]
- 25% = [0.02372881 0.23474576 0.82457627 0.90338983 0.66610169]
- Min = [0.01186441 0.18833333 0.70666667 0.83333333 0.55666667]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 222.0 | 18.0 |
| Actual Positive | 22.0 | 37.25 |

### robot-5
#### accuracy
- Mean = 0.9340133779264215
- Standard deviation = 0.028601463283755506
- Max = 0.9632107023411371
- 75% = 0.955685618729097
- Median = 0.9415551839464883
- 25% = 0.9223327759197325
- Min = 0.8862876254180602

#### f1
- Mean = 0.7971673069246257
- Standard deviation = 0.1051991188587103
- Max = 0.8990825688073394
- 75% = 0.87571403842825
- Median = 0.8299065420560747
- 25% = 0.7573033707865169
- Min = 0.6222222222222223

#### precision
- Mean = 0.9846967473709953
- Standard deviation = 0.022947446167282587
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 0.975421863536317
- Min = 0.9333333333333333

#### recall
- Mean = 0.6791666666666667
- Standard deviation = 0.1340475661845451
- Max = 0.8166666666666667
- 75% = 0.7791666666666667
- Median = 0.7166666666666667
- 25% = 0.6166666666666667
- Min = 0.4666666666666667

#### facing_probas
- Mean = [0.03145833 0.043125   0.38104167 0.87979167 0.8825    ]
- Standard deviation = [0.04275607 0.04394154 0.06946191 0.04098134 0.02786376]
- Max = [0.13666667 0.15333333 0.505      0.94166667 0.90833333]
- 75% = [0.03958333 0.0425     0.41416667 0.90458333 0.89791667]
- Median = [0.01333333 0.0325     0.365      0.87583333 0.89333333]
- 25% = [0.00333333 0.02375    0.34458333 0.86375    0.88083333]
- Min = [0.         0.00166667 0.28166667 0.805      0.81666667]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 238.75 | 0.5 |
| Actual Positive | 19.25 | 40.75 |

### robot-6
#### accuracy
- Mean = 0.6412054069119286
- Standard deviation = 0.09071821336769212
- Max = 0.7926421404682275
- 75% = 0.6989966555183946
- Median = 0.6460702341137123
- 25% = 0.5854849498327759
- Min = 0.47157190635451507

#### f1
- Mean = 0.7775846540831751
- Standard deviation = 0.0688901277252711
- Max = 0.8843283582089552
- 75% = 0.8228210146018364
- Median = 0.7849780904770722
- 25% = 0.7385541954625402
- Min = 0.640909090909091

#### precision
- Mean = 1.0
- Standard deviation = 0.0
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 1.0
- Min = 1.0

#### recall
- Mean = 0.6412054069119286
- Standard deviation = 0.09071821336769212
- Max = 0.7926421404682275
- 75% = 0.6989966555183946
- Median = 0.6460702341137123
- 25% = 0.5854849498327759
- Min = 0.47157190635451507

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
| Actual Positive | 107.375 | 191.875 |

