# ExtraTreesClassifier_SMOTE_2022-01-18-17-13_no4
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
	- sampling_strategy_ = OrderedDict([(0, 3)])
	- nn_k_ = NearestNeighbors(n_neighbors=6)

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
- gp_auc_max = 0.15893616336146665
- high_power = 0.10413396426361979
- hlbr = 0.08811856428025731
- gp_max_val_mean = 0.0783560235758707
- gp_max_val_max = 0.06559864239847894
- diff_auc = 0.06555661310627514
- gp_auc_mean = 0.054091133193715696
- gp_max_ix_range = 0.04343348795330893
- gp_auc_min = 0.04188011710298764
- diff_std = 0.03277759260887395
- gp_max_ix_min = 0.03143862115885072
- tdoa_range = 0.030039409838806524
- gp_max_val_min = 0.029966514321915026
- srmr = 0.027043147903200494
- gp_max_ix_std = 0.02159985983515395
- tdoa_min = 0.021481148446242177
- gp_max_ix_mean = 0.015015612336461086
- coe1[0] = 0.012721050602187553
- tdoa_std = 0.01252748515731117
- gp_auc_std = 0.009296194883239415
- tdoa_mean = 0.008948289667243918
- gp_max_val_std = 0.007551214217880885
- coe1[1] = 0.005554877221543886
- gp_max_val_range = 0.0053200379867046526
- coe3[2] = 0.0041725501027826606
- ratio_max_to_9th_ave_peaks = 0.003991243991243993
- ac_std = 0.0034382284382284386
- ratio_max_to_10ms_ave_peaks = 0.00293040293040293
- ac_auc = 0.002918940452877104
- gp_auc_range = 0.0026189859523192823
- coe3[3] = 0.002457264957264957
- gp_max_ix_max = 0.0024216524216524216
- tdoa_max = 0.0021787471787471837
- low_power = 0.0014862181528848216
- coe3[0] = 0.0
- coe3[1] = 0.0

## Evaluation
cv = 8
### robot-1
#### accuracy
- Mean = 0.9911616161616161
- Standard deviation = 0.013773626407368338
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 0.9873737373737375
- Min = 0.9595959595959596

#### f1
- Mean = 0.9796352021961778
- Standard deviation = 0.031243240442851115
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 0.9698025551684089
- Min = 0.9090909090909091

#### precision
- Mean = 0.9618506493506493
- Standard deviation = 0.05773520442947198
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 0.9415584415584415
- Min = 0.8333333333333334

#### recall
- Mean = 1.0
- Standard deviation = 0.0
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 1.0
- Min = 1.0

#### facing_probas
- Mean = [0.91916667 0.75375    0.05583333 0.         0.00166667]
- Standard deviation = [0.0720243  0.07238856 0.0220794  0.         0.00288675]
- Max = [0.99       0.855      0.09166667 0.         0.00666667]
- 75% = [0.97708333 0.79333333 0.07333333 0.         0.00166667]
- Median = [0.95166667 0.765      0.05083333 0.         0.        ]
- 25% = [0.86416667 0.69166667 0.03583333 0.         0.        ]
- Min = [0.78166667 0.645      0.03       0.         0.        ]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 78.125 | 0.875 |
| Actual Positive | 0.0 | 20.0 |

### robot-2
#### accuracy
- Mean = 0.9924242424242424
- Standard deviation = 0.011007320564496645
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 0.9873737373737375
- Min = 0.9696969696969697

#### f1
- Mean = 0.9800807892913157
- Standard deviation = 0.029213625600132898
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 0.9676113360323887
- Min = 0.9189189189189189

#### precision
- Mean = 1.0
- Standard deviation = 0.0
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 1.0
- Min = 1.0

#### recall
- Mean = 0.9624999999999999
- Standard deviation = 0.05448623679425842
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 0.9375
- Min = 0.85

#### facing_probas
- Mean = [0.95125    0.94770833 0.93125    0.02375    0.01166667]
- Standard deviation = [0.01798437 0.02834482 0.02293938 0.01079319 0.00677003]
- Max = [0.97833333 0.98166667 0.97333333 0.04       0.02333333]
- 75% = [0.96166667 0.97083333 0.94125    0.03041667 0.01583333]
- Median = [0.95       0.95666667 0.92583333 0.0275     0.01083333]
- 25% = [0.94375    0.92458333 0.91416667 0.01458333 0.00791667]
- Min = [0.91666667 0.905      0.90333333 0.005      0.        ]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 79.0 | 0.0 |
| Actual Positive | 0.75 | 19.25 |

### robot-3
#### accuracy
- Mean = 0.9015151515151515
- Standard deviation = 0.03489968424516477
- Max = 0.9494949494949495
- 75% = 0.9141414141414141
- Median = 0.9090909090909091
- 25% = 0.898989898989899
- Min = 0.8282828282828283

#### f1
- Mean = 0.6578899257721137
- Standard deviation = 0.17477706112101588
- Max = 0.8571428571428571
- 75% = 0.729227761485826
- Median = 0.7096774193548387
- 25% = 0.6618876941457587
- Min = 0.2608695652173913

#### precision
- Mean = 1.0
- Standard deviation = 0.0
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 1.0
- Min = 1.0

#### recall
- Mean = 0.5125
- Standard deviation = 0.17275343701356566
- Max = 0.75
- 75% = 0.5750000000000001
- Median = 0.55
- 25% = 0.5
- Min = 0.15

#### facing_probas
- Mean = [0.450625   0.93791667 0.9625     0.87375    0.15729167]
- Standard deviation = [0.09847073 0.02220094 0.01543355 0.03406234 0.06083868]
- Max = [0.64333333 0.96166667 0.98666667 0.925      0.24166667]
- 75% = [0.49291667 0.95791667 0.9725     0.895      0.215     ]
- Median = [0.43083333 0.94166667 0.96583333 0.8825     0.14833333]
- 25% = [0.37625    0.9225     0.94958333 0.84625    0.10541667]
- Min = [0.32333333 0.89666667 0.94       0.81833333 0.075     ]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 79.0 | 0.0 |
| Actual Positive | 9.75 | 10.25 |

### robot-4
#### accuracy
- Mean = 0.970959595959596
- Standard deviation = 0.017080491487965505
- Max = 0.98989898989899
- 75% = 0.9823232323232323
- Median = 0.9747474747474747
- 25% = 0.9646464646464646
- Min = 0.9393939393939394

#### f1
- Mean = 0.9166311400686402
- Standard deviation = 0.052783894622674625
- Max = 0.972972972972973
- 75% = 0.9515765765765766
- Median = 0.9293650793650794
- 25% = 0.9
- Min = 0.8125000000000001

#### precision
- Mean = 0.9921875
- Standard deviation = 0.020669932117692115
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 1.0
- Min = 0.9375

#### recall
- Mean = 0.8552631578947368
- Standard deviation = 0.08217102629471576
- Max = 0.9473684210526315
- 75% = 0.9078947368421053
- Median = 0.868421052631579
- 25% = 0.8289473684210527
- Min = 0.6842105263157895

#### facing_probas
- Mean = [0.         0.01973684 0.92083333 0.98464912 0.79385965]
- Standard deviation = [0.         0.02204793 0.04189859 0.01014477 0.06889735]
- Max = [0.         0.05964912 0.96842105 0.99473684 0.88596491]
- 75% = [0.         0.0377193  0.94780702 0.99078947 0.83114035]
- Median = [0.         0.00701754 0.92280702 0.9877193  0.79561404]
- 25% = [0.         0.00263158 0.91578947 0.98070175 0.7627193 ]
- Min = [0.         0.         0.82105263 0.96140351 0.65614035]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 79.875 | 0.125 |
| Actual Positive | 2.75 | 16.25 |

### robot-5
#### accuracy
- Mean = 0.9987373737373737
- Standard deviation = 0.0033405950897280033
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 1.0
- Min = 0.98989898989899

#### f1
- Mean = 0.9967948717948718
- Standard deviation = 0.008479972150848053
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 1.0
- Min = 0.9743589743589743

#### precision
- Mean = 1.0
- Standard deviation = 0.0
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 1.0
- Min = 1.0

#### recall
- Mean = 0.99375
- Standard deviation = 0.016535945694153707
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 1.0
- Min = 0.95

#### facing_probas
- Mean = [0.01958333 0.         0.044375   0.975      0.983125  ]
- Standard deviation = [0.01053269 0.         0.0469185  0.00905232 0.01008428]
- Max = [0.03666667 0.         0.14166667 0.98666667 0.99666667]
- 75% = [0.02375    0.         0.075      0.98041667 0.99041667]
- Median = [0.0175     0.         0.01833333 0.9775     0.98666667]
- 25% = [0.01416667 0.         0.01       0.97125    0.975     ]
- Min = [0.00333333 0.         0.00333333 0.955      0.96666667]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 79.0 | 0.0 |
| Actual Positive | 0.125 | 19.875 |

### robot-6
#### accuracy
- Mean = 0.86489898989899
- Standard deviation = 0.022551226135721882
- Max = 0.8888888888888888
- 75% = 0.8813131313131313
- Median = 0.8686868686868687
- 25% = 0.8560606060606061
- Min = 0.8181818181818182

#### f1
- Mean = 0.9273974446192152
- Standard deviation = 0.01310106190471633
- Max = 0.9411764705882353
- 75% = 0.9369070208728653
- Median = 0.9296984572230014
- 25% = 0.9224429793300071
- Min = 0.9

#### precision
- Mean = 1.0
- Standard deviation = 0.0
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 1.0
- Min = 1.0

#### recall
- Mean = 0.86489898989899
- Standard deviation = 0.022551226135721882
- Max = 0.8888888888888888
- 75% = 0.8813131313131313
- Median = 0.8686868686868687
- 25% = 0.8560606060606061
- Min = 0.8181818181818182

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
| Actual Positive | 13.375 | 85.625 |

