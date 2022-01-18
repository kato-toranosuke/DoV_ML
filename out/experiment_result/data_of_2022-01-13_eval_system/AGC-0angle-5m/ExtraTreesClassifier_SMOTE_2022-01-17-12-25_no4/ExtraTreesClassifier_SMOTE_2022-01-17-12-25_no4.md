# ExtraTreesClassifier_SMOTE_2022-01-17-12-25_no4
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

#### Importance of features
- gp_max_val_min = 0.12181312783181983
- gp_auc_max = 0.11153750175056745
- gp_auc_mean = 0.10858641750141955
- gp_max_val_max = 0.10441548791042878
- gp_auc_min = 0.09604216435519246
- srmr = 0.07838491638070141
- gp_max_val_mean = 0.07287999208948011
- hlbr = 0.06622179208570703
- ratio_max_to_10ms_ave_peaks = 0.03959239917007329
- gp_auc_range = 0.028905526984976955
- gp_max_val_range = 0.026104502879435432
- high_power = 0.0249615831912172
- ratio_max_to_9th_ave_peaks = 0.01449440080374233
- ac_std = 0.013191662573697275
- gp_auc_std = 0.010703263927531206
- coe3[3] = 0.009604575691460934
- diff_std = 0.009262226281219414
- coe3[2] = 0.008138852529277062
- ac_auc = 0.007833266823811578
- coe1[0] = 0.006715815313792674
- coe1[1] = 0.006700773822316376
- diff_auc = 0.006412871006988652
- gp_max_val_std = 0.006012740950010651
- tdoa_max = 0.003955911102782224
- gp_max_ix_range = 0.003514189060415473
- low_power = 0.003177200556405693
- gp_max_ix_min = 0.0029489346165816753
- tdoa_mean = 0.0022500152040381923
- gp_max_ix_max = 0.001761616161616161
- gp_max_ix_mean = 0.0015037037037037037
- tdoa_range = 0.001150345517366794
- gp_max_ix_std = 0.0007777777777777776
- tdoa_min = 0.0004444444444444443
- coe3[0] = 0.0
- coe3[1] = 0.0
- tdoa_std = 0.0

## Evaluation
cv = 8
### robot-1
#### accuracy
- Mean = 0.94
- Standard deviation = 0.03122498999199197
- Max = 0.99
- 75% = 0.9624999999999999
- Median = 0.94
- 25% = 0.9175
- Min = 0.89

#### f1
- Mean = 0.8198023282285267
- Standard deviation = 0.1106929480402787
- Max = 0.975609756097561
- 75% = 0.9047297297297298
- Median = 0.8329637841832964
- 25% = 0.7443181818181818
- Min = 0.6206896551724138

#### precision
- Mean = 0.9540750915750916
- Standard deviation = 0.05210580463594611
- Max = 1.0
- 75% = 1.0
- Median = 0.9761904761904762
- 25% = 0.9173076923076924
- Min = 0.8571428571428571

#### recall
- Mean = 0.7437499999999999
- Standard deviation = 0.181034354474503
- Max = 1.0
- 75% = 0.9
- Median = 0.75
- 25% = 0.6
- Min = 0.45

#### facing_probas
- Mean = [0.686875 0.134    0.00125  0.000875 0.000875]
- Standard deviation = [0.12603416 0.04413049 0.00192029 0.00136359 0.00231503]
- Max = [0.895 0.185 0.006 0.004 0.007]
- 75% = [0.79825 0.17225 0.00125 0.00125 0.     ]
- Median = [6.520e-01 1.335e-01 5.000e-04 0.000e+00 0.000e+00]
- 25% = [0.6095  0.11925 0.      0.      0.     ]
- Min = [0.483 0.04  0.    0.    0.   ]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 79.125 | 0.875 |
| Actual Positive | 5.125 | 14.875 |

### robot-2
#### accuracy
- Mean = 0.8975
- Standard deviation = 0.035619517121937526
- Max = 0.95
- 75% = 0.9225000000000001
- Median = 0.9
- 25% = 0.88
- Min = 0.84

#### f1
- Mean = 0.6961605900088039
- Standard deviation = 0.1348264393164023
- Max = 0.8780487804878048
- 75% = 0.8
- Median = 0.7235772357723578
- 25% = 0.6102540834845736
- Min = 0.4444444444444444

#### precision
- Mean = 0.8333485958485958
- Standard deviation = 0.10878407298870583
- Max = 1.0
- 75% = 0.8761904761904762
- Median = 0.8516483516483516
- 25% = 0.7904761904761906
- Min = 0.6111111111111112

#### recall
- Mean = 0.6312500000000001
- Standard deviation = 0.19029171684547913
- Max = 0.9
- 75% = 0.8
- Median = 0.625
- 25% = 0.525
- Min = 0.3

#### facing_probas
- Mean = [0.206875 0.619625 0.029125 0.001625 0.00125 ]
- Standard deviation = [0.11360506 0.10381346 0.01671405 0.00211763 0.00238485]
- Max = [0.382 0.738 0.059 0.005 0.007]
- 75% = [0.31525 0.7205  0.03875 0.004   0.00075]
- Median = [0.155  0.644  0.0295 0.     0.    ]
- 25% = [0.12975 0.50925 0.019   0.      0.     ]
- Min = [0.053 0.468 0.006 0.    0.   ]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 77.125 | 2.875 |
| Actual Positive | 7.375 | 12.625 |

### robot-3
#### accuracy
- Mean = 0.93625
- Standard deviation = 0.0249687304442977
- Max = 0.97
- 75% = 0.96
- Median = 0.935
- 25% = 0.9225000000000001
- Min = 0.9

#### f1
- Mean = 0.8203968731886508
- Standard deviation = 0.07638235449933126
- Max = 0.9302325581395349
- 75% = 0.8903508771929824
- Median = 0.8166666666666667
- 25% = 0.7714646464646465
- Min = 0.7058823529411764

#### precision
- Mean = 0.9193107315389923
- Standard deviation = 0.0631750500779721
- Max = 1.0
- 75% = 0.9583333333333333
- Median = 0.9354166666666667
- 25% = 0.8664596273291925
- Min = 0.8125

#### recall
- Mean = 0.75
- Standard deviation = 0.1224744871391589
- Max = 1.0
- 75% = 0.8125
- Median = 0.725
- 25% = 0.65
- Min = 0.6

#### facing_probas
- Mean = [2.75000e-03 4.57000e-01 7.38375e-01 1.36250e-01 3.75000e-04]
- Standard deviation = [0.00486698 0.1244759  0.08523781 0.06560059 0.00069597]
- Max = [0.015 0.735 0.857 0.23  0.002]
- 75% = [3.2500e-03 4.8700e-01 8.0425e-01 2.0025e-01 2.5000e-04]
- Median = [0.     0.452  0.7275 0.1295 0.    ]
- 25% = [0.      0.35525 0.69075 0.08525 0.     ]
- Min = [0.    0.314 0.601 0.035 0.   ]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 78.625 | 1.375 |
| Actual Positive | 5.0 | 15.0 |

### robot-4
#### accuracy
- Mean = 0.9137500000000001
- Standard deviation = 0.015761900266148106
- Max = 0.94
- 75% = 0.9225000000000001
- Median = 0.915
- 25% = 0.9
- Min = 0.89

#### f1
- Mean = 0.7709989087168048
- Standard deviation = 0.0439018929550792
- Max = 0.8421052631578948
- 75% = 0.8
- Median = 0.7736572890025575
- 25% = 0.7482142857142857
- Min = 0.6857142857142857

#### precision
- Mean = 0.8324710012210013
- Standard deviation = 0.080867773872509
- Max = 0.9333333333333333
- 75% = 0.8988095238095237
- Median = 0.8333333333333334
- 25% = 0.7875000000000001
- Min = 0.6923076923076923

#### recall
- Mean = 0.73125
- Standard deviation = 0.0933324032691755
- Max = 0.9
- 75% = 0.8
- Median = 0.725
- 25% = 0.65
- Min = 0.6

#### facing_probas
- Mean = [0.001125 0.007125 0.303375 0.72375  0.119125]
- Standard deviation = [0.00105327 0.00669771 0.06298995 0.0681391  0.06438058]
- Max = [0.003 0.019 0.437 0.854 0.253]
- 75% = [0.002   0.01275 0.31875 0.75225 0.14975]
- Median = [0.001  0.0035 0.292  0.7205 0.092 ]
- 25% = [0.      0.0025  0.2675  0.68975 0.0785 ]
- Min = [0.    0.    0.223 0.623 0.049]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 76.75 | 3.25 |
| Actual Positive | 5.375 | 14.625 |

### robot-5
#### accuracy
- Mean = 0.91875
- Standard deviation = 0.02803457686500725
- Max = 0.96
- 75% = 0.9325
- Median = 0.925
- 25% = 0.9075
- Min = 0.86

#### f1
- Mean = 0.735238297148439
- Standard deviation = 0.12209734034608685
- Max = 0.8947368421052632
- 75% = 0.7967914438502675
- Median = 0.7689393939393939
- 25% = 0.6989247311827957
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
- Mean = 0.6
- Standard deviation = 0.15
- Max = 0.85
- 75% = 0.6625
- Median = 0.625
- 25% = 0.5375000000000001
- Min = 0.3

#### facing_probas
- Mean = [5.00000e-04 7.50000e-04 8.75000e-04 3.68750e-01 6.54625e-01]
- Standard deviation = [0.001      0.00082916 0.00078062 0.09182967 0.08204715]
- Max = [0.003 0.002 0.002 0.51  0.817]
- 75% = [2.5000e-04 1.2500e-03 1.2500e-03 4.6425e-01 6.9225e-01]
- Median = [0.000e+00 5.000e-04 1.000e-03 3.395e-01 6.400e-01]
- 25% = [0.     0.     0.     0.2965 0.615 ]
- Min = [0.    0.    0.    0.252 0.521]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 79.875 | 0.125 |
| Actual Positive | 8.0 | 12.0 |

### robot-6
#### accuracy
- Mean = 0.69125
- Standard deviation = 0.06734936896512099
- Max = 0.76
- 75% = 0.7525
- Median = 0.71
- 25% = 0.6325000000000001
- Min = 0.59

#### f1
- Mean = 0.8155429744940603
- Standard deviation = 0.047717170340031784
- Max = 0.8636363636363636
- 75% = 0.8587662337662337
- Median = 0.8297690333618477
- 25% = 0.7748068474473564
- Min = 0.7421383647798743

#### precision
- Mean = 1.0
- Standard deviation = 0.0
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 1.0
- Min = 1.0

#### recall
- Mean = 0.69125
- Standard deviation = 0.06734936896512099
- Max = 0.76
- 75% = 0.7525
- Median = 0.71
- 25% = 0.6325000000000001
- Min = 0.59

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
| Actual Positive | 30.875 | 69.125 |

