# ExtraTreesClassifier_SMOTEENN_2022-01-18-22-58_no5
## Constants
- CSV_PATH = ../out/csv/experiment
- OUTPUT_PATH = ../out/experiment_result/data_of_2022-01-13_eval_system/AGC-45angle-3m
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
- DISTANCE = [3]
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
	- n_estimators = 170
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
	- max_features = sqrt
	- max_leaf_nodes = None
	- min_impurity_decrease = 0.0
	- ccp_alpha = 0.0
	- n_features_in_ = 36
	- n_outputs_ = 1
	- classes_ = [0 1]
	- n_classes_ = 2
	- base_estimator_ = ExtraTreeClassifier()
	- oob_decision_function_ = [[0.60377358 0.39622642]
 [0.8411215  0.1588785 ]
 [0.94059406 0.05940594]
 [0.91743119 0.08256881]
 [0.94174757 0.05825243]
 [0.74336283 0.25663717]
 [0.85393258 0.14606742]
 [0.82653061 0.17346939]
 [0.01086957 0.98913043]
 [0.00980392 0.99019608]
 [0.10784314 0.89215686]
 [0.05940594 0.94059406]
 [0.04950495 0.95049505]
 [0.01041667 0.98958333]
 [0.03       0.97      ]
 [0.         1.        ]
 [0.         1.        ]
 [0.02752294 0.97247706]
 [0.04081633 0.95918367]
 [0.03809524 0.96190476]
 [0.         1.        ]
 [0.16666667 0.83333333]]
	- oob_score_ = 1.0

#### Importance of features
- gp_max_val_mean = 0.09279243091056279
- gp_auc_max = 0.08192800788954635
- gp_auc_mean = 0.07850509533201841
- gp_max_val_min = 0.07773942581634889
- gp_auc_min = 0.07421495883034344
- diff_auc = 0.06246888794965718
- srmr = 0.05340941110171879
- diff_std = 0.052664287279671894
- high_power = 0.043207342108441
- coe1[1] = 0.04030928117466579
- ac_std = 0.03875328731097962
- coe1[0] = 0.03868832378447763
- gp_max_val_max = 0.035728961209730445
- low_power = 0.035126287530133686
- coe3[3] = 0.0334689349112426
- gp_max_ix_mean = 0.03013466234620081
- tdoa_mean = 0.024738776181083874
- hlbr = 0.018393287624056856
- tdoa_std = 0.0162790379136533
- coe3[2] = 0.015891800507185125
- tdoa_min = 0.011851538774615696
- ac_auc = 0.009903611345919038
- gp_auc_std = 0.008734854888701044
- gp_max_ix_min = 0.0051550123665508275
- gp_max_ix_std = 0.005084374315143547
- ratio_max_to_10ms_ave_peaks = 0.004804170188785574
- gp_auc_range = 0.0038508500046961587
- gp_max_val_std = 0.003099464637926176
- gp_max_val_range = 0.0030736357659434583
- coe3[0] = 0.0
- coe3[1] = 0.0
- ratio_max_to_9th_ave_peaks = 0.0
- gp_max_ix_range = 0.0
- gp_max_ix_max = 0.0
- tdoa_range = 0.0
- tdoa_max = 0.0

## Evaluation
cv = 8
### robot-1
#### accuracy
- Mean = 0.94
- Standard deviation = 0.026457513110645887
- Max = 0.98
- 75% = 0.955
- Median = 0.94
- 25% = 0.9275
- Min = 0.89

#### f1
- Mean = 0.8440009773987296
- Standard deviation = 0.09040846230763383
- Max = 0.9523809523809523
- 75% = 0.8953488372093024
- Median = 0.8603145235892693
- 25% = 0.8260233918128655
- Min = 0.6451612903225806

#### precision
- Mean = 0.8484617988694075
- Standard deviation = 0.059705290808839476
- Max = 0.9090909090909091
- 75% = 0.8939393939393939
- Median = 0.8722826086956521
- 25% = 0.8118729096989967
- Min = 0.7407407407407407

#### recall
- Mean = 0.8687499999999999
- Standard deviation = 0.1748883572454153
- Max = 1.0
- 75% = 1.0
- Median = 0.975
- 25% = 0.775
- Min = 0.5

#### facing_probas
- Mean = [0.92165441 0.79727941 0.32621324 0.14128676 0.13198529]
- Standard deviation = [0.03916156 0.07077667 0.12669904 0.08203786 0.07079622]
- Max = [0.99176471 0.93735294 0.50205882 0.30441176 0.27941176]
- 75% = [0.94       0.82323529 0.46779412 0.18183824 0.15080882]
- Median = [0.92323529 0.77338235 0.27941176 0.14323529 0.13161765]
- 25% = [0.88852941 0.75080882 0.21838235 0.08676471 0.09411765]
- Min = [0.87029412 0.72205882 0.17529412 0.02205882 0.02588235]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 76.625 | 3.375 |
| Actual Positive | 2.625 | 17.375 |

### robot-2
#### accuracy
- Mean = 0.9112499999999999
- Standard deviation = 0.057973593126526154
- Max = 0.98
- 75% = 0.955
- Median = 0.935
- 25% = 0.855
- Min = 0.82

#### f1
- Mean = 0.7556959904096127
- Standard deviation = 0.15639491491814864
- Max = 0.9473684210526316
- 75% = 0.8783783783783783
- Median = 0.8057040998217468
- 25% = 0.6165413533834586
- Min = 0.5

#### precision
- Mean = 0.8524955436720142
- Standard deviation = 0.17966409038456171
- Max = 1.0
- 75% = 1.0
- Median = 0.9705882352941176
- 25% = 0.6666666666666666
- Min = 0.5454545454545454

#### recall
- Mean = 0.6875
- Standard deviation = 0.15155444566227677
- Max = 0.9
- 75% = 0.8125
- Median = 0.675
- 25% = 0.6
- Min = 0.4

#### facing_probas
- Mean = [0.84073529 0.87544118 0.64099265 0.30382353 0.12959559]
- Standard deviation = [0.05671401 0.04212433 0.08637111 0.13701195 0.07394061]
- Max = [0.93558824 0.95235294 0.80558824 0.49588235 0.27264706]
- 75% = [0.87110294 0.89852941 0.68294118 0.45470588 0.14977941]
- Median = [0.83352941 0.86205882 0.61705882 0.25455882 0.13117647]
- 25% = [0.79308824 0.85169118 0.57661765 0.19352941 0.08147059]
- Min = [0.77529412 0.81558824 0.54       0.12852941 0.02147059]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 77.375 | 2.625 |
| Actual Positive | 6.25 | 13.75 |

### robot-3
#### accuracy
- Mean = 0.91
- Standard deviation = 0.08746427842267948
- Max = 1.0
- 75% = 0.99
- Median = 0.95
- 25% = 0.8
- Min = 0.8

#### f1
- Mean = 0.5819394569394569
- Standard deviation = 0.45479219614845623
- Max = 1.0
- 75% = 0.9743589743589743
- Median = 0.8533988533988535
- 25% = 0.0
- Min = 0.0

#### precision
- Mean = 0.625
- Standard deviation = 0.4841229182759271
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 0.0
- Min = 0.0

#### recall
- Mean = 0.55
- Standard deviation = 0.4373213921133975
- Max = 1.0
- 75% = 0.95
- Median = 0.75
- 25% = 0.0
- Min = 0.0

#### facing_probas
- Mean = [0.46136029 0.89084559 0.93055147 0.83852941 0.38264706]
- Standard deviation = [0.14931888 0.05047899 0.03894601 0.06083207 0.15597285]
- Max = [0.71970588 0.99029412 0.99911765 0.95470588 0.63470588]
- 75% = [0.57595588 0.92345588 0.95808824 0.85316176 0.52720588]
- Median = [0.42691176 0.88161765 0.92397059 0.81338235 0.34397059]
- 25% = [0.31786765 0.85448529 0.89705882 0.79794118 0.23529412]
- Min = [0.30617647 0.82852941 0.88323529 0.77705882 0.21676471]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 80.0 | 0.0 |
| Actual Positive | 9.0 | 11.0 |

### robot-4
#### accuracy
- Mean = 0.79375
- Standard deviation = 0.1360089611018333
- Max = 0.93
- 75% = 0.92
- Median = 0.8400000000000001
- 25% = 0.6625000000000001
- Min = 0.61

#### f1
- Mean = 0.507059557033046
- Standard deviation = 0.32154214957068117
- Max = 0.8205128205128205
- 75% = 0.8116883116883117
- Median = 0.6031746031746031
- 25% = 0.24045599151643687
- Min = 0.04878048780487805

#### precision
- Mean = 0.5016740386806176
- Standard deviation = 0.3288872736135228
- Max = 0.875
- 75% = 0.7900717703349283
- Median = 0.5795454545454546
- 25% = 0.21382783882783882
- Min = 0.047619047619047616

#### recall
- Mean = 0.51875
- Standard deviation = 0.3239767545673609
- Max = 0.9
- 75% = 0.8125
- Median = 0.575
- 25% = 0.27499999999999997
- Min = 0.05

#### facing_probas
- Mean = [0.17455882 0.47308824 0.87286765 0.91511029 0.71426471]
- Standard deviation = [0.09724892 0.1564258  0.05193441 0.04744669 0.09077116]
- Max = [0.34558824 0.75058824 0.98470588 0.99529412 0.90029412]
- 75% = [0.23286765 0.56830882 0.88948529 0.94470588 0.74698529]
- Median = [0.14632353 0.45470588 0.85926471 0.91382353 0.68808824]
- 25% = [0.11838235 0.38169118 0.83279412 0.87742647 0.66455882]
- Min = [0.04676471 0.20529412 0.81823529 0.85117647 0.58911765]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 69.0 | 11.0 |
| Actual Positive | 9.625 | 10.375 |

### robot-5
#### accuracy
- Mean = 0.8899999999999999
- Standard deviation = 0.07382411530116696
- Max = 0.98
- 75% = 0.955
- Median = 0.905
- 25% = 0.8075000000000001
- Min = 0.8

#### f1
- Mean = 0.5200895278294659
- Standard deviation = 0.3982462001569536
- Max = 0.9473684210526316
- 75% = 0.8725868725868725
- Median = 0.6710239651416121
- 25% = 0.07142857142857142
- Min = 0.0

#### precision
- Mean = 0.75
- Standard deviation = 0.4330127018922193
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 0.75
- Min = 0.0

#### recall
- Mean = 0.45
- Standard deviation = 0.369120576505835
- Max = 0.9
- 75% = 0.775
- Median = 0.5249999999999999
- 25% = 0.037500000000000006
- Min = 0.0

#### facing_probas
- Mean = [0.12944853 0.19084559 0.535      0.92408088 0.91136029]
- Standard deviation = [0.0777362  0.09726487 0.13733389 0.03689373 0.04392185]
- Max = [0.28088235 0.34235294 0.76764706 0.99205882 0.99529412]
- 75% = [0.15330882 0.26507353 0.64330882 0.94058824 0.94220588]
- Median = [0.11897059 0.17441176 0.52161765 0.91676471 0.90367647]
- 25% = [0.06904412 0.12411765 0.41522059 0.89602941 0.87095588]
- Min = [0.03323529 0.05470588 0.34735294 0.87647059 0.86029412]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 80.0 | 0.0 |
| Actual Positive | 11.0 | 9.0 |

### robot-6
#### accuracy
- Mean = 0.615
- Standard deviation = 0.27622454633866267
- Max = 0.9
- 75% = 0.85
- Median = 0.74
- 25% = 0.3175
- Min = 0.23

#### f1
- Mean = 0.7214449777028675
- Standard deviation = 0.23555757298641108
- Max = 0.9473684210526316
- 75% = 0.9188251618871416
- Median = 0.8467656415694591
- 25% = 0.48059701492537316
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
- Mean = 0.615
- Standard deviation = 0.27622454633866267
- Max = 0.9
- 75% = 0.85
- Median = 0.74
- 25% = 0.3175
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
| Actual Positive | 38.5 | 61.5 |

