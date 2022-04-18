# ExtraTreesClassifier_SMOTEENN_2022-04-15-05-00_no5
## Constants
- CSV_PATH = ../out/csv/experiment
- OUTPUT_PATH = ../out/experiment_result/data_of_2022-03-23_eval_system/AGC-15deg-0angle-5m
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
- AGC_STATUS = ['AGC-15deg']
- ANGLES = [60, 75, 90, 105, 120]

## Loaded CSV
- 2022-03-23_raspi_48000Hz_w1_N2^12_overlap80_all.csv

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
	- n_estimators = 70
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
- ratio_max_to_10ms_ave_peaks = 0.23786239579934934
- srmr = 0.19199992779562333
- coe3[2] = 0.1338219553041482
- coe3[3] = 0.09965554564155488
- low_power = 0.06478916201163344
- ac_std = 0.05476059587086279
- gp_max_val_min = 0.04390083973562233
- ac_auc = 0.042857142857142864
- coe1[0] = 0.03898392580148558
- coe1[1] = 0.024013033458390055
- gp_max_val_max = 0.013126914019491986
- tdoa_min = 0.007196009148576506
- high_power = 0.006947199142321096
- gp_auc_mean = 0.0058809115412889
- gp_auc_max = 0.004927588320966072
- gp_max_val_mean = 0.004739067271458582
- tdoa_std = 0.004738324708989552
- hlbr = 0.004177411036616815
- gp_max_val_std = 0.0032435459950713556
- diff_std = 0.0029122572417456657
- gp_max_ix_max = 0.002879760451038773
- gp_auc_range = 0.002879760451038773
- gp_max_ix_range = 0.001073914136478603
- ratio_max_to_9th_ave_peaks = 0.000722311396468703
- gp_auc_min = 0.0005946809096415412
- tdoa_range = 0.00047923322683706185
- diff_auc = 0.00041829336307863945
- gp_max_val_range = 0.00041829336307863945
- coe3[0] = 0.0
- coe3[1] = 0.0
- gp_max_ix_std = 0.0
- gp_max_ix_min = 0.0
- gp_max_ix_mean = 0.0
- gp_auc_std = 0.0
- tdoa_max = 0.0
- tdoa_mean = 0.0

## Evaluation
cv = 8
### robot-1
#### accuracy
- Mean = 0.7625
- Standard deviation = 0.06869315832017044
- Max = 0.83
- 75% = 0.8125
- Median = 0.785
- 25% = 0.74
- Min = 0.61

#### f1
- Mean = 0.26115810017257424
- Standard deviation = 0.14182180365248506
- Max = 0.47058823529411764
- 75% = 0.3629032258064516
- Median = 0.26028059990324137
- 25% = 0.1272577996715928
- Min = 0.08000000000000002

#### precision
- Mean = 0.4506616921090605
- Standard deviation = 0.2646582244843141
- Max = 1.0
- 75% = 0.5876623376623377
- Median = 0.381578947368421
- 25% = 0.2196969696969697
- Min = 0.2

#### recall
- Mean = 0.22499999999999998
- Standard deviation = 0.13228756555322954
- Max = 0.4
- 75% = 0.35
- Median = 0.25
- 25% = 0.08750000000000001
- Min = 0.05

#### facing_probas
- Mean = [0.4638226  0.44503483 0.37275223 0.37146092 0.37102966]
- Standard deviation = [0.14551588 0.17370271 0.18226553 0.20980156 0.2465279 ]
- Max = [0.76409439 0.77820266 0.72472988 0.75967517 0.78065816]
- 75% = [0.50647676 0.53850255 0.4822646  0.51723505 0.59827799]
- Median = [0.46874291 0.41529549 0.31120522 0.2979667  0.28931066]
- 25% = [0.35737259 0.33999114 0.25247711 0.20927643 0.16556349]
- Min = [0.25432086 0.18919955 0.16577749 0.11110544 0.07073413]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 71.75 | 8.25 |
| Actual Positive | 15.5 | 4.5 |

### robot-2
#### accuracy
- Mean = 0.73875
- Standard deviation = 0.06112231589198828
- Max = 0.79
- 75% = 0.775
- Median = 0.77
- 25% = 0.72
- Min = 0.6

#### f1
- Mean = 0.2696079363167678
- Standard deviation = 0.15020600019558325
- Max = 0.5106382978723405
- 75% = 0.3365750528541226
- Median = 0.22903225806451613
- 25% = 0.16000000000000003
- Min = 0.08000000000000002

#### precision
- Mean = 0.32945212999560824
- Standard deviation = 0.09828741610803479
- Max = 0.4444444444444444
- 75% = 0.4
- Median = 0.38181818181818183
- 25% = 0.24565217391304348
- Min = 0.16666666666666666

#### recall
- Mean = 0.28750000000000003
- Standard deviation = 0.22465250944514284
- Max = 0.7
- 75% = 0.375
- Median = 0.225
- 25% = 0.1
- Min = 0.05

#### facing_probas
- Mean = [0.54522406 0.58912351 0.54151261 0.53919296 0.43698547]
- Standard deviation = [0.12817396 0.11775727 0.20762041 0.13065706 0.18773818]
- Max = [0.79543339 0.84091865 0.80188974 0.78440533 0.77790958]
- 75% = [0.60385594 0.63278586 0.70821528 0.5951391  0.54765356]
- Median = [0.52644062 0.5686824  0.57968651 0.5390608  0.42803217]
- 25% = [0.50109304 0.52555697 0.42064626 0.44837982 0.29037465]
- Min = [0.31473243 0.41681349 0.18057058 0.34051304 0.19790363]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 68.125 | 11.875 |
| Actual Positive | 14.25 | 5.75 |

### robot-3
#### accuracy
- Mean = 0.72625
- Standard deviation = 0.062437468718710906
- Max = 0.8
- 75% = 0.77
- Median = 0.735
- 25% = 0.69
- Min = 0.6

#### f1
- Mean = 0.21068471731946423
- Standard deviation = 0.1349330391581657
- Max = 0.3939393939393939
- 75% = 0.29836601307189536
- Median = 0.2549194991055456
- 25% = 0.13235294117647056
- Min = 0.0

#### precision
- Mean = 0.23686335403726708
- Standard deviation = 0.1584913265701652
- Max = 0.5
- 75% = 0.3012422360248447
- Median = 0.2704347826086957
- 25% = 0.1607142857142857
- Min = 0.0

#### recall
- Mean = 0.23125
- Standard deviation = 0.1983328956577804
- Max = 0.65
- 75% = 0.3125
- Median = 0.2
- 25% = 0.11249999999999999
- Min = 0.0

#### facing_probas
- Mean = [0.48648165 0.54139257 0.51368931 0.54355708 0.46673714]
- Standard deviation = [0.13517941 0.11025344 0.19254336 0.12191194 0.15488805]
- Max = [0.74876701 0.78752551 0.78380527 0.78166723 0.75791553]
- 75% = [0.53921677 0.56327912 0.64195252 0.59578437 0.54098058]
- Median = [0.48594969 0.52333248 0.55181803 0.54387486 0.46367304]
- 25% = [0.43368516 0.47801063 0.43318559 0.49363421 0.39277891]
- Min = [0.245947   0.42170607 0.1541165  0.33074688 0.22523583]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 68.0 | 12.0 |
| Actual Positive | 15.375 | 4.625 |

### robot-4
#### accuracy
- Mean = 0.7262500000000001
- Standard deviation = 0.019960899278339158
- Max = 0.76
- 75% = 0.74
- Median = 0.725
- 25% = 0.7175
- Min = 0.69

#### f1
- Mean = 0.28192656128444793
- Standard deviation = 0.078189521501167
- Max = 0.3829787234042553
- 75% = 0.33536585365853655
- Median = 0.29742962056303546
- 25% = 0.25833333333333336
- Min = 0.125

#### precision
- Mean = 0.2947772562582345
- Standard deviation = 0.05351508447653637
- Max = 0.3333333333333333
- 75% = 0.3333333333333333
- Median = 0.31534090909090906
- 25% = 0.2902173913043478
- Min = 0.16666666666666666

#### recall
- Mean = 0.28125
- Standard deviation = 0.10588171466310885
- Max = 0.45
- 75% = 0.35
- Median = 0.3
- 25% = 0.225
- Min = 0.1

#### facing_probas
- Mean = [0.43648689 0.53042467 0.51694182 0.57602275 0.49548682]
- Standard deviation = [0.15793327 0.12692194 0.18681863 0.13083955 0.17858293]
- Max = [0.71898271 0.78764881 0.76611054 0.80726361 0.80065448]
- 75% = [0.53514746 0.60866334 0.64074341 0.64922654 0.58633624]
- Median = [0.40475184 0.50624731 0.52959467 0.53578288 0.55377353]
- 25% = [0.36467071 0.42805619 0.44001198 0.50875432 0.36370373]
- Min = [0.15376077 0.38233163 0.15058957 0.36255612 0.2082792 ]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 67.0 | 13.0 |
| Actual Positive | 14.375 | 5.625 |

### robot-5
#### accuracy
- Mean = 0.7262500000000001
- Standard deviation = 0.04385701198212208
- Max = 0.77
- 75% = 0.77
- Median = 0.735
- 25% = 0.6975
- Min = 0.66

#### f1
- Mean = 0.0908462974252448
- Standard deviation = 0.08252187884154846
- Max = 0.2162162162162162
- 75% = 0.15873015873015875
- Median = 0.08596491228070176
- 25% = 0.0
- Min = 0.0

#### precision
- Mean = 0.11424221203632969
- Standard deviation = 0.10487447319588658
- Max = 0.2857142857142857
- 75% = 0.19518716577540107
- Median = 0.10555555555555556
- 25% = 0.0
- Min = 0.0

#### recall
- Mean = 0.08125
- Standard deviation = 0.07880950133074058
- Max = 0.2
- 75% = 0.125
- Median = 0.07500000000000001
- 25% = 0.0
- Min = 0.0

#### facing_probas
- Mean = [0.40552051 0.46830028 0.47441249 0.55546227 0.48694561]
- Standard deviation = [0.13374336 0.15133538 0.18600862 0.11367525 0.16426955]
- Max = [0.6907123  0.75884722 0.7464538  0.7625068  0.76124291]
- 75% = [0.45571662 0.5540416  0.60696981 0.62325248 0.5941233 ]
- Median = [0.39389739 0.43793282 0.49166964 0.55864172 0.48632611]
- 25% = [0.29980279 0.37807894 0.35654592 0.48895139 0.41084056]
- Min = [0.23941327 0.24890051 0.12643367 0.36174263 0.21024518]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 71.0 | 9.0 |
| Actual Positive | 18.375 | 1.625 |

### robot-6
#### accuracy
- Mean = 0.22125
- Standard deviation = 0.06029873547596168
- Max = 0.35
- 75% = 0.23750000000000002
- Median = 0.22
- 25% = 0.1775
- Min = 0.14

#### f1
- Mean = 0.3584761522391109
- Standard deviation = 0.07826198220297112
- Max = 0.5185185185185185
- 75% = 0.383662408052652
- Median = 0.36065573770491804
- 25% = 0.30146313197160657
- Min = 0.24561403508771928

#### precision
- Mean = 1.0
- Standard deviation = 0.0
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 1.0
- Min = 1.0

#### recall
- Mean = 0.22125
- Standard deviation = 0.06029873547596168
- Max = 0.35
- 75% = 0.23750000000000002
- Median = 0.22
- 25% = 0.1775
- Min = 0.14

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
| Actual Positive | 77.875 | 22.125 |

