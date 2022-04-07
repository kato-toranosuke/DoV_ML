# ExtraTreesClassifier_NoResampler_2022-01-20-10-34_no0
## Constants
- CSV_PATH = ../out/csv/experiment
- OUTPUT_PATH = ../out/experiment_result/data_of_2022-01-13_eval_system/NoAGC-45angle-5m
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
- DISTANCE = [5]
- AGC_STATUS = ['NoAGC']

## Loaded CSV
- 2021-12-27_AGC.csv
- 2022-01-10_NoAGC.csv
- 2022-01-13_raspi_48000Hz_w1_N2^12_overlap80.csv

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
	- n_estimators = 30
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
- gp_auc_min = 0.11860470217419543
- gp_auc_mean = 0.11688011348830954
- gp_max_val_min = 0.11523876259516526
- gp_max_val_mean = 0.09740074222343979
- gp_max_val_max = 0.09197647988002505
- gp_auc_max = 0.07349171386279671
- srmr = 0.049482023214610704
- tdoa_min = 0.045429071988734734
- gp_max_ix_max = 0.027848887135935068
- tdoa_mean = 0.02747488190455084
- gp_auc_std = 0.024181199423149963
- gp_max_ix_range = 0.021775222902115532
- ratio_max_to_10ms_ave_peaks = 0.017774721762288115
- tdoa_max = 0.016140962331584824
- coe1[1] = 0.014460594406376938
- gp_max_val_range = 0.014059003866491471
- gp_max_val_std = 0.01308005314614331
- gp_max_ix_mean = 0.010817281648627405
- coe3[3] = 0.010540177331546587
- hlbr = 0.010345216444016429
- high_power = 0.00889100915567626
- tdoa_range = 0.008704807791980816
- gp_auc_range = 0.008421014379479215
- gp_max_ix_std = 0.008156727157541004
- coe3[2] = 0.007605102875130419
- low_power = 0.007424400769356403
- diff_std = 0.006933896706521005
- diff_auc = 0.005423110686066839
- ac_auc = 0.005091840341314524
- coe1[0] = 0.004971110351778969
- ac_std = 0.003826372848452813
- tdoa_std = 0.003589237799314523
- gp_max_ix_min = 0.002052304828762411
- ratio_max_to_9th_ave_peaks = 0.0019072525785212525
- coe3[0] = 0.0
- coe3[1] = 0.0

## Evaluation
cv = 8
### robot-1
#### accuracy
- Mean = 0.9875
- Standard deviation = 0.016393596310755015
- Max = 1.0
- 75% = 1.0
- Median = 0.995
- 25% = 0.9824999999999999
- Min = 0.96

#### f1
- Mean = 0.9700929152148664
- Standard deviation = 0.03901103658203756
- Max = 1.0
- 75% = 1.0
- Median = 0.9878048780487805
- 25% = 0.9578977932636469
- Min = 0.9047619047619048

#### precision
- Mean = 0.954004329004329
- Standard deviation = 0.05567811063849763
- Max = 1.0
- 75% = 1.0
- Median = 0.9761904761904762
- 25% = 0.9301948051948051
- Min = 0.8636363636363636

#### recall
- Mean = 0.9875
- Standard deviation = 0.021650635094610987
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 0.9875
- Min = 0.95

#### facing_probas
- Mean = [0.96083333 0.77138889 0.06710069 0.01680556 0.00835069]
- Standard deviation = [0.03391414 0.08039495 0.04394398 0.01291387 0.00623974]
- Max = [0.98458333 0.89986111 0.15819444 0.04       0.02083333]
- 75% = [0.98211806 0.81427083 0.08961806 0.025      0.00993056]
- Median = [0.97916667 0.77243056 0.06305556 0.01611111 0.00833333]
- 25% = [0.95652778 0.72357639 0.0303125  0.0075     0.0059375 ]
- Min = [0.90111111 0.64055556 0.01083333 0.         0.        ]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 79.0 | 1.0 |
| Actual Positive | 0.25 | 19.75 |

### robot-2
#### accuracy
- Mean = 0.9625
- Standard deviation = 0.04465142774872938
- Max = 1.0
- 75% = 0.9924999999999999
- Median = 0.98
- 25% = 0.9525
- Min = 0.86

#### f1
- Mean = 0.8764738698949225
- Standard deviation = 0.1702336618428269
- Max = 1.0
- 75% = 0.9807692307692307
- Median = 0.9466389466389467
- 25% = 0.8680223285486444
- Min = 0.4615384615384615

#### precision
- Mean = 0.9930555555555556
- Standard deviation = 0.01837327299350411
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 1.0
- Min = 0.9444444444444444

#### recall
- Mean = 0.81875
- Standard deviation = 0.22351943427809584
- Max = 1.0
- 75% = 0.9624999999999999
- Median = 0.8999999999999999
- 25% = 0.8
- Min = 0.3

#### facing_probas
- Mean = [0.915      0.96875    0.79232639 0.21276042 0.00387153]
- Standard deviation = [0.04068147 0.02063225 0.08949287 0.16727553 0.00289296]
- Max = [0.96402778 0.99166667 0.89486111 0.54527778 0.00819444]
- 75% = [0.94006944 0.9853125  0.87284722 0.25638889 0.00524306]
- Median = [0.93041667 0.97576389 0.81319444 0.18       0.00409722]
- 25% = [0.9025     0.95618056 0.72628472 0.10506944 0.00125   ]
- Min = [0.83708333 0.93194444 0.65444444 0.02791667 0.        ]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 79.875 | 0.125 |
| Actual Positive | 3.625 | 16.375 |

### robot-3
#### accuracy
- Mean = 0.98375
- Standard deviation = 0.01494782592887676
- Max = 1.0
- 75% = 1.0
- Median = 0.985
- 25% = 0.97
- Min = 0.96

#### f1
- Mean = 0.9569054631554632
- Standard deviation = 0.04052365024602718
- Max = 1.0
- 75% = 1.0
- Median = 0.9621794871794872
- 25% = 0.9220374220374221
- Min = 0.888888888888889

#### precision
- Mean = 0.9871710526315789
- Standard deviation = 0.022230125893253905
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 0.9875
- Min = 0.9473684210526315

#### recall
- Mean = 0.9312499999999999
- Standard deviation = 0.07043392293490403
- Max = 1.0
- 75% = 1.0
- Median = 0.95
- 25% = 0.8875
- Min = 0.8

#### facing_probas
- Mean = [0.16039931 0.89555556 0.94628472 0.90161458 0.07364583]
- Standard deviation = [0.085322   0.02518719 0.03521037 0.08109687 0.04574079]
- Max = [0.30791667 0.92861111 0.97861111 0.97402778 0.15652778]
- 75% = [0.20069444 0.9125     0.97003472 0.94364583 0.09541667]
- Median = [0.15666667 0.89958333 0.96125    0.94145833 0.07763889]
- 25% = [0.11152778 0.87857639 0.93565972 0.90034722 0.04333333]
- Min = [0.03833333 0.84736111 0.87583333 0.745      0.00652778]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 79.75 | 0.25 |
| Actual Positive | 1.375 | 18.625 |

### robot-4
#### accuracy
- Mean = 0.91625
- Standard deviation = 0.049733665660194375
- Max = 0.96
- 75% = 0.9524999999999999
- Median = 0.9299999999999999
- 25% = 0.905
- Min = 0.8

#### f1
- Mean = 0.7311253802596307
- Standard deviation = 0.1873481695362067
- Max = 0.888888888888889
- 75% = 0.8650793650793651
- Median = 0.7867647058823528
- 25% = 0.6935483870967742
- Min = 0.28571428571428575

#### precision
- Mean = 0.9261363636363636
- Standard deviation = 0.16379017392499517
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 0.9772727272727273
- Min = 0.5

#### recall
- Mean = 0.6124999999999999
- Standard deviation = 0.18833148966649205
- Max = 0.8
- 75% = 0.7625
- Median = 0.6499999999999999
- 25% = 0.5375000000000001
- Min = 0.2

#### facing_probas
- Mean = [0.00772569 0.37456597 0.94371528 0.98477431 0.72666667]
- Standard deviation = [0.00494371 0.12279467 0.03741018 0.01589549 0.11333559]
- Max = [0.01680556 0.58777778 0.98236111 0.99861111 0.86125   ]
- 75% = [0.01118056 0.46847222 0.97336806 0.99454861 0.79284722]
- Median = [0.00638889 0.35465278 0.95909722 0.99166667 0.77902778]
- 25% = [0.00399306 0.29670139 0.918125   0.98368056 0.68197917]
- Min = [0.00125    0.20097222 0.87902778 0.9525     0.50138889]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 79.375 | 0.625 |
| Actual Positive | 7.75 | 12.25 |

### robot-5
#### accuracy
- Mean = 0.99
- Standard deviation = 0.013228756555322966
- Max = 1.0
- 75% = 1.0
- Median = 0.995
- 25% = 0.9875
- Min = 0.96

#### f1
- Mean = 0.9731219073324336
- Standard deviation = 0.036488408404443895
- Max = 1.0
- 75% = 1.0
- Median = 0.9871794871794872
- 25% = 0.9676113360323887
- Min = 0.888888888888889

#### precision
- Mean = 1.0
- Standard deviation = 0.0
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 1.0
- Min = 1.0

#### recall
- Mean = 0.95
- Standard deviation = 0.06614378277661476
- Max = 1.0
- 75% = 1.0
- Median = 0.975
- 25% = 0.9375
- Min = 0.8

#### facing_probas
- Mean = [0.00626736 0.00354167 0.18345486 0.94607639 0.92434028]
- Standard deviation = [0.00458251 0.00394063 0.10557564 0.04876651 0.03309775]
- Max = [0.01430556 0.01208333 0.36166667 0.99194444 0.96388889]
- 75% = [0.0084375  0.00416667 0.23555556 0.97586806 0.94527778]
- Median = [0.00673611 0.00243056 0.15625    0.96333333 0.93784722]
- 25% = [3.12500000e-03 6.25000000e-04 1.21944444e-01 9.38125000e-01
 9.02951389e-01]
- Min = [0.         0.         0.04375    0.85902778 0.86972222]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 80.0 | 0.0 |
| Actual Positive | 1.0 | 19.0 |

### robot-6
#### accuracy
- Mean = 0.86
- Standard deviation = 0.07968688725254612
- Max = 0.96
- 75% = 0.95
- Median = 0.845
- 25% = 0.8075
- Min = 0.74

#### f1
- Mean = 0.9227502866937689
- Standard deviation = 0.046262171434330146
- Max = 0.9795918367346939
- 75% = 0.9743589743589743
- Median = 0.9159811985898942
- 25% = 0.8933383001179611
- Min = 0.8505747126436781

#### precision
- Mean = 1.0
- Standard deviation = 0.0
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 1.0
- Min = 1.0

#### recall
- Mean = 0.86
- Standard deviation = 0.07968688725254612
- Max = 0.96
- 75% = 0.95
- Median = 0.845
- 25% = 0.8075
- Min = 0.74

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
| Actual Positive | 14.0 | 86.0 |

