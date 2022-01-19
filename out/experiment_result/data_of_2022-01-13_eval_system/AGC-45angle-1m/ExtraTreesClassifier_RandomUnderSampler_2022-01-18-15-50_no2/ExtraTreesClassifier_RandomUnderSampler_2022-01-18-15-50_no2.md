# ExtraTreesClassifier_RandomUnderSampler_2022-01-18-15-50_no2
## Constants
- CSV_PATH = ../out/csv/experiment
- OUTPUT_PATH = ../out/experiment_result/data_of_2022-01-13_eval_system/AGC-45angle-1m
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
- DISTANCE = [1]
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
	- sample_indices_ = [ 6  7  8  9 10 11 12 13 14 24 25 26 27 28 29 30 31 32 42 43 44 45 46 47
 48 49 50 60 61 62 63 64 65 66 67 68 69 72  4 22 57 53 15 54 51 33 35 17
 34 21 37 18 59  0 52  5 20  1 73 39  2 56 71  3 70 41 58 19 40 36 38 16]

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
- high_power = 0.09153540237157898
- gp_max_ix_std = 0.07373438935355481
- hlbr = 0.06945153500816852
- gp_max_val_mean = 0.06820226218412276
- srmr = 0.0673571289507462
- gp_auc_max = 0.06389393578050354
- tdoa_mean = 0.058747180261261016
- gp_max_val_max = 0.05432698815293924
- tdoa_range = 0.04943976162110001
- gp_max_ix_range = 0.04491882611207085
- gp_max_ix_mean = 0.04365572476121038
- tdoa_std = 0.04267144231429946
- diff_auc = 0.036943757598519505
- diff_std = 0.03576724794466628
- gp_auc_mean = 0.031409076026180933
- gp_auc_min = 0.03081568676442172
- tdoa_min = 0.020665987451701735
- gp_max_ix_min = 0.01909973524780566
- coe3[2] = 0.012765367453024099
- gp_max_val_min = 0.010195847310693253
- ratio_max_to_10ms_ave_peaks = 0.009798829328727046
- gp_max_val_std = 0.008709092661455453
- coe3[3] = 0.008256029684601115
- coe1[1] = 0.008182593420688658
- gp_auc_range = 0.007155138758615308
- gp_auc_std = 0.00623612510203989
- coe1[0] = 0.006183052241830819
- gp_max_val_range = 0.005639294567865998
- low_power = 0.0045812635131572
- ac_auc = 0.0037761114546828846
- ac_std = 0.00215027036455608
- tdoa_max = 0.0014623298287647836
- gp_max_ix_max = 0.0012522072488849907
- ratio_max_to_9th_ave_peaks = 0.0010203791555608605
- coe3[0] = 0.0
- coe3[1] = 0.0

## Evaluation
cv = 8
### robot-1
#### accuracy
- Mean = 1.0
- Standard deviation = 0.0
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 1.0
- Min = 1.0

#### f1
- Mean = 1.0
- Standard deviation = 0.0
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 1.0
- Min = 1.0

#### precision
- Mean = 1.0
- Standard deviation = 0.0
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 1.0
- Min = 1.0

#### recall
- Mean = 1.0
- Standard deviation = 0.0
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 1.0
- Min = 1.0

#### facing_probas
- Mean = [9.45625000e-01 7.49285714e-01 4.01785714e-02 8.92857143e-05
 1.33928571e-03]
- Standard deviation = [0.028881   0.05037867 0.0160744  0.00023623 0.00354342]
- Max = [9.75000000e-01 8.22857143e-01 7.42857143e-02 7.14285714e-04
 1.07142857e-02]
- 75% = [0.9725     0.79625    0.04785714 0.         0.        ]
- Median = [0.94857143 0.74714286 0.03714286 0.         0.        ]
- 25% = [0.93660714 0.69660714 0.02767857 0.         0.        ]
- Min = [0.88642857 0.68714286 0.02214286 0.         0.        ]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 79.25 | 0.0 |
| Actual Positive | 0.0 | 20.0 |

### robot-2
#### accuracy
- Mean = 0.9987373737373737
- Standard deviation = 0.0033405950897280033
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 1.0
- Min = 0.98989898989899

#### f1
- Mean = 0.9969512195121951
- Standard deviation = 0.008066314972757905
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 1.0
- Min = 0.975609756097561

#### precision
- Mean = 0.9940476190476191
- Standard deviation = 0.01574851970871782
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 1.0
- Min = 0.9523809523809523

#### recall
- Mean = 1.0
- Standard deviation = 0.0
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 1.0
- Min = 1.0

#### facing_probas
- Mean = [0.95696429 0.96410714 0.94098214 0.02276786 0.00732143]
- Standard deviation = [0.01487083 0.01899164 0.01994232 0.00979013 0.00714955]
- Max = [0.97928571 0.99071429 0.97785714 0.04357143 0.02      ]
- 75% = [0.96767857 0.97803571 0.95214286 0.0275     0.01035714]
- Median = [0.95892857 0.96785714 0.93392857 0.02107143 0.005     ]
- 25% = [0.94553571 0.95446429 0.92571429 0.01607143 0.00125   ]
- Min = [9.31428571e-01 9.33571429e-01 9.19285714e-01 1.07142857e-02
 7.14285714e-04]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 79.125 | 0.125 |
| Actual Positive | 0.0 | 20.0 |

### robot-3
#### accuracy
- Mean = 0.9105555555555556
- Standard deviation = 0.023452187563642188
- Max = 0.9393939393939394
- 75% = 0.929469696969697
- Median = 0.9145959595959596
- 25% = 0.9015151515151515
- Min = 0.8686868686868687

#### f1
- Mean = 0.7073236145223811
- Standard deviation = 0.10150692150537992
- Max = 0.8235294117647058
- 75% = 0.787878787878788
- Median = 0.7298387096774193
- 25% = 0.6751152073732719
- Min = 0.5185185185185185

#### precision
- Mean = 1.0
- Standard deviation = 0.0
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 1.0
- Min = 1.0

#### recall
- Mean = 0.55625
- Standard deviation = 0.11575161985907584
- Max = 0.7
- 75% = 0.65
- Median = 0.575
- 25% = 0.5125000000000001
- Min = 0.35

#### facing_probas
- Mean = [0.40848214 0.92107143 0.960625   0.87964286 0.13151786]
- Standard deviation = [0.08089143 0.02498979 0.01520455 0.02070505 0.04254415]
- Max = [0.56357143 0.94928571 0.97642857 0.92142857 0.22214286]
- 75% = [0.455      0.94       0.97178571 0.89089286 0.14892857]
- Median = [0.38357143 0.93107143 0.96714286 0.8725     0.12892857]
- 25% = [0.3575     0.90428571 0.95339286 0.86482143 0.09160714]
- Min = [0.30857143 0.87142857 0.93214286 0.85642857 0.09      ]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 79.25 | 0.0 |
| Actual Positive | 8.875 | 11.125 |

### robot-4
#### accuracy
- Mean = 0.9660101010101011
- Standard deviation = 0.015040671996310607
- Max = 0.98989898989899
- 75% = 0.972449494949495
- Median = 0.9696969696969697
- 25% = 0.9571969696969697
- Min = 0.9393939393939394

#### f1
- Mean = 0.9021129454033865
- Standard deviation = 0.04721644212776071
- Max = 0.972972972972973
- 75% = 0.9253003003003002
- Median = 0.9142857142857143
- 25% = 0.8760504201680672
- Min = 0.8125000000000001

#### precision
- Mean = 1.0
- Standard deviation = 0.0
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 1.0
- Min = 1.0

#### recall
- Mean = 0.825
- Standard deviation = 0.0772627276626484
- Max = 0.9473684210526315
- 75% = 0.8611842105263158
- Median = 0.8421052631578947
- 25% = 0.7796052631578947
- Min = 0.6842105263157895

#### facing_probas
- Mean = [0.         0.02853853 0.9181344  0.97343515 0.76578947]
- Standard deviation = [0.         0.02083658 0.02586401 0.01066548 0.06387213]
- Max = [0.         0.06240602 0.95639098 0.99357143 0.84360902]
- 75% = [0.         0.04586466 0.93217105 0.98157895 0.80808271]
- Median = [0.         0.02761278 0.92180451 0.96954887 0.78406015]
- 25% = [0.         0.00988722 0.90524436 0.96654135 0.74161654]
- Min = [0.00000000e+00 7.51879699e-04 8.73684211e-01 9.58571429e-01
 6.58646617e-01]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 80.0 | 0.0 |
| Actual Positive | 3.375 | 15.875 |

### robot-5
#### accuracy
- Mean = 1.0
- Standard deviation = 0.0
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 1.0
- Min = 1.0

#### f1
- Mean = 1.0
- Standard deviation = 0.0
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 1.0
- Min = 1.0

#### precision
- Mean = 1.0
- Standard deviation = 0.0
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 1.0
- Min = 1.0

#### recall
- Mean = 1.0
- Standard deviation = 0.0
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 1.0
- Min = 1.0

#### facing_probas
- Mean = [1.14285714e-02 8.92857143e-05 4.18750000e-02 9.65089286e-01
 9.77857143e-01]
- Standard deviation = [0.01145087 0.00023623 0.03173941 0.01397172 0.01234082]
- Max = [3.35714286e-02 7.14285714e-04 1.05714286e-01 9.86428571e-01
 9.95714286e-01]
- 75% = [0.02035714 0.         0.05982143 0.97571429 0.98928571]
- Median = [0.00678571 0.         0.03142857 0.96392857 0.975     ]
- 25% = [0.00125    0.         0.02267857 0.95660714 0.96928571]
- Min = [7.14285714e-04 0.00000000e+00 3.57142857e-03 9.40000000e-01
 9.61428571e-01]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 79.25 | 0.0 |
| Actual Positive | 0.0 | 20.0 |

### robot-6
#### accuracy
- Mean = 0.8765656565656565
- Standard deviation = 0.014124087509453346
- Max = 0.898989898989899
- 75% = 0.8822222222222222
- Median = 0.8793939393939394
- 25% = 0.8686868686868687
- Min = 0.8484848484848485

#### f1
- Mean = 0.934162690508862
- Standard deviation = 0.008049780744095205
- Max = 0.9468085106382979
- 75% = 0.937421777221527
- Median = 0.9358270418668497
- 25% = 0.9297297297297298
- Min = 0.9180327868852458

#### precision
- Mean = 1.0
- Standard deviation = 0.0
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 1.0
- Min = 1.0

#### recall
- Mean = 0.8765656565656565
- Standard deviation = 0.014124087509453346
- Max = 0.898989898989899
- 75% = 0.8822222222222222
- Median = 0.8793939393939394
- 25% = 0.8686868686868687
- Min = 0.8484848484848485

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
| Actual Positive | 12.25 | 87.0 |

