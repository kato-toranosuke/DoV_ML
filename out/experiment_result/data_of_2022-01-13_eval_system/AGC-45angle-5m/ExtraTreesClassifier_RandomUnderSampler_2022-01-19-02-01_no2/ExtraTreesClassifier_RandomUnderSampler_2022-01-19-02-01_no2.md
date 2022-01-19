# ExtraTreesClassifier_RandomUnderSampler_2022-01-19-02-01_no2
## Constants
- CSV_PATH = ../out/csv/experiment
- OUTPUT_PATH = ../out/experiment_result/data_of_2022-01-13_eval_system/AGC-45angle-5m
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
- AGC_STATUS = ['AGC']

## Loaded CSV
- 2021-12-27_AGC.csv
- 2022-01-10_NoAGC.csv
- 2022-01-13_raspi_48000Hz_w1_N2^12_overlap80.csv

## Estimator
### Type
- resampler = RandomUnderSampler
- estimator = ExtraTreesClassifier

### Arguments for hyperparameter search
- resampler = RandomUnderSampler
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
	- replacement = False
	- n_features_in_ = 36
	- sampling_strategy_ = OrderedDict([(1, 36)])
	- sample_indices_ = [ 2  3  4  8  9 10 14 15 16 20 21 22 29 30 31 32 33 34 41 42 43 44 45 46
 53 54 55 56 57 58 65 66 67 68 69 70 63 72  7 25 60 50 12 51 48 27 35 17
 28 24 37 18 62  0 49 11 23  1 73 39  5 59 71  6 64 47 61 19 40 36 38 13]

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
	- oob_decision_function_ = [[0.57142857 0.42857143]
 [1.         0.        ]
 [1.         0.        ]
 [0.33333333 0.66666667]
 [0.5        0.5       ]
 [0.83333333 0.16666667]
 [0.83333333 0.16666667]
 [1.         0.        ]
 [1.         0.        ]
 [1.         0.        ]
 [1.         0.        ]
 [0.75       0.25      ]
 [1.         0.        ]
 [0.42857143 0.57142857]
 [1.         0.        ]
 [1.         0.        ]
 [1.         0.        ]
 [1.         0.        ]
 [1.         0.        ]
 [1.         0.        ]
 [1.         0.        ]
 [1.         0.        ]
 [1.         0.        ]
 [1.         0.        ]
 [0.875      0.125     ]
 [0.85714286 0.14285714]
 [1.         0.        ]
 [1.         0.        ]
 [1.         0.        ]
 [0.85714286 0.14285714]
 [1.         0.        ]
 [1.         0.        ]
 [1.         0.        ]
 [1.         0.        ]
 [1.         0.        ]
 [0.85714286 0.14285714]
 [0.125      0.875     ]
 [0.         1.        ]
 [0.         1.        ]
 [0.         1.        ]
 [0.16666667 0.83333333]
 [0.         1.        ]
 [0.         1.        ]
 [0.         1.        ]
 [0.11111111 0.88888889]
 [0.16666667 0.83333333]
 [0.         1.        ]
 [0.28571429 0.71428571]
 [0.         1.        ]
 [0.         1.        ]
 [0.14285714 0.85714286]
 [0.25       0.75      ]
 [0.28571429 0.71428571]
 [0.14285714 0.85714286]
 [0.         1.        ]
 [0.375      0.625     ]
 [0.         1.        ]
 [0.16666667 0.83333333]
 [0.         1.        ]
 [0.         1.        ]
 [0.         1.        ]
 [0.33333333 0.66666667]
 [0.         1.        ]
 [0.         1.        ]
 [0.         1.        ]
 [0.16666667 0.83333333]
 [0.125      0.875     ]
 [0.         1.        ]
 [0.14285714 0.85714286]
 [0.         1.        ]
 [0.25       0.75      ]
 [0.         1.        ]]
	- oob_score_ = 0.9722222222222222

#### Importance of features
- gp_max_val_max = 0.16970151130334196
- gp_auc_mean = 0.15493619944017037
- gp_auc_min = 0.09272575250836121
- diff_std = 0.0741853354614157
- tdoa_min = 0.06688963210702341
- gp_max_val_mean = 0.06506751812256094
- high_power = 0.05523809523809524
- gp_max_val_min = 0.053750597228858096
- hlbr = 0.05
- coe1[1] = 0.04790547798066593
- gp_max_ix_std = 0.031932773109243695
- gp_auc_range = 0.03083011719738063
- coe3[2] = 0.02934782608695652
- coe1[0] = 0.0175
- coe3[3] = 0.014059183673469384
- gp_max_ix_min = 0.010836120401337789
- diff_auc = 0.00903010033444816
- gp_max_ix_range = 0.008193979933110364
- tdoa_range = 0.008043374394981208
- tdoa_max = 0.00761904761904762
- low_power = 0.0016053511705685665
- gp_auc_std = 0.0006020066889632085
- coe3[0] = 0.0
- coe3[1] = 0.0
- ratio_max_to_10ms_ave_peaks = 0.0
- ratio_max_to_9th_ave_peaks = 0.0
- ac_std = 0.0
- ac_auc = 0.0
- srmr = 0.0
- gp_max_val_std = 0.0
- gp_max_val_range = 0.0
- gp_max_ix_max = 0.0
- gp_max_ix_mean = 0.0
- gp_auc_max = 0.0
- tdoa_std = 0.0
- tdoa_mean = 0.0

## Evaluation
cv = 8
### robot-1
#### accuracy
- Mean = 0.9625
- Standard deviation = 0.021650635094610987
- Max = 1.0
- 75% = 0.975
- Median = 0.96
- 25% = 0.94
- Min = 0.94

#### f1
- Mean = 0.9165899730741034
- Standard deviation = 0.04660088836265788
- Max = 1.0
- 75% = 0.9415768576290414
- Median = 0.9090909090909091
- 25% = 0.8695652173913044
- Min = 0.8695652173913044

#### precision
- Mean = 0.849538143016404
- Standard deviation = 0.08176912017972368
- Max = 1.0
- 75% = 0.8902691511387163
- Median = 0.8333333333333334
- 25% = 0.7692307692307693
- Min = 0.7692307692307693

#### recall
- Mean = 1.0
- Standard deviation = 0.0
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 1.0
- Min = 1.0

#### facing_probas
- Mean = [0.969375 0.874375 0.13625  0.01625  0.00625 ]
- Standard deviation = [0.04318836 0.04186567 0.03594701 0.0181573  0.00695971]
- Max = [1.    0.945 0.2   0.05  0.02 ]
- 75% = [0.9925 0.8975 0.15   0.025  0.01  ]
- Median = [0.985  0.8825 0.1325 0.01   0.005 ]
- 25% = [0.97125 0.8425  0.115   0.      0.     ]
- Min = [0.86  0.805 0.085 0.    0.   ]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 76.25 | 3.75 |
| Actual Positive | 0.0 | 20.0 |

### robot-2
#### accuracy
- Mean = 0.9625
- Standard deviation = 0.021650635094610987
- Max = 1.0
- 75% = 0.975
- Median = 0.96
- 25% = 0.94
- Min = 0.94

#### f1
- Mean = 0.8927054882937235
- Standard deviation = 0.06447060330871528
- Max = 1.0
- 75% = 0.9327789327789328
- Median = 0.888888888888889
- 25% = 0.8235294117647058
- Min = 0.8235294117647058

#### precision
- Mean = 1.0
- Standard deviation = 0.0
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 1.0
- Min = 1.0

#### recall
- Mean = 0.8125
- Standard deviation = 0.10825317547305482
- Max = 1.0
- 75% = 0.875
- Median = 0.8
- 25% = 0.7
- Min = 0.7

#### facing_probas
- Mean = [0.918125 0.956875 0.735625 0.1575   0.0025  ]
- Standard deviation = [0.04152842 0.02999349 0.07935039 0.09024273 0.00661438]
- Max = [0.985 0.99  0.885 0.33  0.02 ]
- 75% = [0.94625 0.98125 0.77    0.225   0.     ]
- Median = [0.92   0.9675 0.7425 0.115  0.    ]
- 25% = [0.89875 0.93375 0.6925  0.10375 0.     ]
- Min = [0.85  0.9   0.615 0.035 0.   ]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 80.0 | 0.0 |
| Actual Positive | 3.75 | 16.25 |

### robot-3
#### accuracy
- Mean = 0.9762500000000001
- Standard deviation = 0.02394655507583504
- Max = 1.0
- 75% = 1.0
- Median = 0.98
- 25% = 0.9624999999999999
- Min = 0.94

#### f1
- Mean = 0.9324069544657779
- Standard deviation = 0.07030195961170607
- Max = 1.0
- 75% = 1.0
- Median = 0.9466389466389467
- 25% = 0.8950715421303657
- Min = 0.8235294117647058

#### precision
- Mean = 1.0
- Standard deviation = 0.0
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 1.0
- Min = 1.0

#### recall
- Mean = 0.88125
- Standard deviation = 0.11973277537917512
- Max = 1.0
- 75% = 1.0
- Median = 0.8999999999999999
- 25% = 0.8125
- Min = 0.7

#### facing_probas
- Mean = [0.286875 0.974375 0.974375 0.933125 0.11625 ]
- Standard deviation = [0.06864481 0.01844544 0.02855231 0.04022884 0.04715334]
- Max = [0.405 1.    1.    0.995 0.195]
- 75% = [0.3175  0.995   0.99625 0.95    0.13625]
- Median = [0.2775 0.97   0.985  0.945  0.1075]
- 25% = [0.25375 0.955   0.965   0.925   0.085  ]
- Min = [0.18  0.955 0.92  0.86  0.055]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 80.0 | 0.0 |
| Actual Positive | 2.375 | 17.625 |

### robot-4
#### accuracy
- Mean = 0.9212500000000001
- Standard deviation = 0.017633419974582336
- Max = 0.95
- 75% = 0.9325
- Median = 0.92
- 25% = 0.91
- Min = 0.89

#### f1
- Mean = 0.7792633904859049
- Standard deviation = 0.0507376238734809
- Max = 0.8648648648648648
- 75% = 0.8083333333333333
- Median = 0.7836257309941519
- 25% = 0.7305986696230597
- Min = 0.7096774193548387

#### precision
- Mean = 0.8947132218271925
- Standard deviation = 0.08222001535144675
- Max = 1.0
- 75% = 0.9384191176470589
- Median = 0.9282051282051282
- 25% = 0.8645833333333334
- Min = 0.7142857142857143

#### recall
- Mean = 0.7
- Standard deviation = 0.07905694150420949
- Max = 0.8
- 75% = 0.75
- Median = 0.725
- 25% = 0.6749999999999999
- Min = 0.55

#### facing_probas
- Mean = [0.0125   0.299375 0.90875  0.980625 0.768125]
- Standard deviation = [0.01089725 0.07117046 0.04188899 0.02639099 0.07441176]
- Max = [0.035 0.41  0.965 1.    0.89 ]
- 75% = [0.01375 0.37    0.95125 0.995   0.805  ]
- Median = [0.01   0.2725 0.9    0.995  0.77  ]
- 25% = [0.005   0.2425  0.88375 0.975   0.72875]
- Min = [0.    0.21  0.835 0.915 0.65 ]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 78.125 | 1.875 |
| Actual Positive | 6.0 | 14.0 |

### robot-5
#### accuracy
- Mean = 0.97875
- Standard deviation = 0.016909686573085867
- Max = 1.0
- 75% = 0.99
- Median = 0.98
- 25% = 0.9775
- Min = 0.94

#### f1
- Mean = 0.9423168375567756
- Standard deviation = 0.05022728327328292
- Max = 1.0
- 75% = 0.9743589743589743
- Median = 0.9500000000000001
- 25% = 0.9402560455192035
- Min = 0.8235294117647058

#### precision
- Mean = 0.9875
- Standard deviation = 0.021650635094610987
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 0.9875
- Min = 0.95

#### recall
- Mean = 0.90625
- Standard deviation = 0.08816709987291178
- Max = 1.0
- 75% = 0.95
- Median = 0.95
- 25% = 0.8875
- Min = 0.7

#### facing_probas
- Mean = [0.0025   0.016875 0.22     0.9425   0.93125 ]
- Standard deviation = [0.00353553 0.01836054 0.07390873 0.03436932 0.0437857 ]
- Max = [0.01  0.06  0.37  0.995 0.975]
- 75% = [0.005   0.02125 0.26125 0.96125 0.9625 ]
- Median = [0.     0.0125 0.2125 0.9475 0.95  ]
- 25% = [0.      0.00375 0.15625 0.92875 0.91   ]
- Min = [0.    0.    0.135 0.87  0.845]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 79.75 | 0.25 |
| Actual Positive | 1.875 | 18.125 |

### robot-6
#### accuracy
- Mean = 0.86
- Standard deviation = 0.018027756377319962
- Max = 0.88
- 75% = 0.8725
- Median = 0.86
- 25% = 0.8574999999999999
- Min = 0.82

#### f1
- Mean = 0.9246291346699115
- Standard deviation = 0.010529424898523277
- Max = 0.9361702127659575
- 75% = 0.9319035157583342
- Median = 0.924731182795699
- 25% = 0.923278116826504
- Min = 0.9010989010989011

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
- Standard deviation = 0.018027756377319962
- Max = 0.88
- 75% = 0.8725
- Median = 0.86
- 25% = 0.8574999999999999
- Min = 0.82

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

