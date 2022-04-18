# ExtraTreesClassifier_NoResampler_2022-04-15-01-24_no0
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
- ac_auc = 0.07096955614530544
- diff_auc = 0.05973759528310926
- diff_std = 0.051977165611460305
- high_power = 0.049621014573689885
- coe3[3] = 0.04516213669503279
- gp_max_val_min = 0.042896204586582345
- gp_max_val_max = 0.042177778041733546
- coe1[0] = 0.04182152007856854
- gp_auc_range = 0.04159987174757548
- coe1[1] = 0.03828749175411105
- gp_auc_mean = 0.03821831229034642
- gp_auc_max = 0.037385991553665184
- gp_max_val_mean = 0.036297062201727
- hlbr = 0.03482566617343715
- srmr = 0.03291643420730653
- gp_auc_min = 0.03288146137144599
- gp_auc_std = 0.02889260577548474
- gp_max_val_range = 0.028306698953036672
- ratio_max_to_9th_ave_peaks = 0.027739368967591962
- ac_std = 0.027473144941772984
- tdoa_max = 0.027356398488892195
- ratio_max_to_10ms_ave_peaks = 0.023236168220494253
- gp_max_ix_mean = 0.02207096980206225
- gp_max_ix_min = 0.019308073156172983
- gp_max_ix_std = 0.01915306122448981
- coe3[2] = 0.018828917579566267
- tdoa_mean = 0.01558737222614824
- gp_max_val_std = 0.011528297682003983
- gp_max_ix_max = 0.010957687603410494
- low_power = 0.010805995178702451
- tdoa_range = 0.0057769199911675275
- tdoa_std = 0.0031375625061280414
- tdoa_min = 0.0030654953877783833
- coe3[0] = 0.0
- coe3[1] = 0.0
- gp_max_ix_range = 0.0

## Evaluation
cv = 8
### robot-1
#### accuracy
- Mean = 0.7962500000000001
- Standard deviation = 0.009921567416492224
- Max = 0.81
- 75% = 0.8
- Median = 0.8
- 25% = 0.795
- Min = 0.78

#### f1
- Mean = 0.051167582417582416
- Standard deviation = 0.07772081861956832
- Max = 0.23076923076923075
- 75% = 0.08630952380952381
- Median = 0.0
- 25% = 0.0
- Min = 0.0

#### precision
- Mean = 0.21875
- Standard deviation = 0.34089725358236606
- Max = 1.0
- 75% = 0.3125
- Median = 0.0
- 25% = 0.0
- Min = 0.0

#### recall
- Mean = 0.03125
- Standard deviation = 0.04960783708246107
- Max = 0.15
- 75% = 0.05
- Median = 0.0
- 25% = 0.0
- Min = 0.0

#### facing_probas
- Mean = [0.16119792 0.14953125 0.11270833 0.06833333 0.04760417]
- Standard deviation = [0.03691055 0.03802551 0.09231447 0.05013177 0.02713917]
- Max = [0.21875    0.22083333 0.3175     0.18458333 0.07916667]
- 75% = [0.18625    0.16739583 0.15625    0.07729167 0.06958333]
- Median = [0.173125   0.15541667 0.070625   0.05854167 0.05833333]
- 25% = [0.11947917 0.12270833 0.0515625  0.0409375  0.02625   ]
- Min = [0.1125     0.095      0.01666667 0.01375    0.        ]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 79.0 | 1.0 |
| Actual Positive | 19.375 | 0.625 |

### robot-2
#### accuracy
- Mean = 0.8175
- Standard deviation = 0.038649062084350747
- Max = 0.86
- 75% = 0.85
- Median = 0.835
- 25% = 0.78
- Min = 0.75

#### f1
- Mean = 0.4256487110210515
- Standard deviation = 0.20273624835319629
- Max = 0.6808510638297872
- 75% = 0.5694444444444444
- Median = 0.4603174603174603
- 25% = 0.34444444444444444
- Min = 0.0

#### precision
- Mean = 0.5413833273208273
- Standard deviation = 0.24525229443867017
- Max = 0.8571428571428571
- 75% = 0.6941964285714286
- Median = 0.6087962962962963
- 25% = 0.4409090909090909
- Min = 0.0

#### recall
- Mean = 0.38749999999999996
- Standard deviation = 0.2328492001274645
- Max = 0.8
- 75% = 0.5125
- Median = 0.4
- 25% = 0.2375
- Min = 0.0

#### facing_probas
- Mean = [0.17989583 0.47083333 0.324375   0.28598958 0.17041667]
- Standard deviation = [0.06259741 0.11504905 0.08085749 0.06202876 0.10154727]
- Max = [0.30833333 0.70875    0.46958333 0.42375    0.415     ]
- 75% = [0.21395833 0.51697917 0.36239583 0.30072917 0.164375  ]
- Median = [0.15625    0.47375    0.31145833 0.274375   0.15958333]
- 25% = [0.13364583 0.36770833 0.26583333 0.24635417 0.1415625 ]
- Min = [0.10875    0.33916667 0.22125    0.21125    0.03875   ]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 74.0 | 6.0 |
| Actual Positive | 12.25 | 7.75 |

### robot-3
#### accuracy
- Mean = 0.77125
- Standard deviation = 0.03099899191909314
- Max = 0.8
- 75% = 0.7925
- Median = 0.78
- 25% = 0.76
- Min = 0.7

#### f1
- Mean = 0.04966108619641229
- Standard deviation = 0.03924207147395972
- Max = 0.09090909090909091
- 75% = 0.08173913043478262
- Median = 0.06971153846153846
- 25% = 0.0
- Min = 0.0

#### precision
- Mean = 0.16041666666666665
- Standard deviation = 0.16954545031413323
- Max = 0.5
- 75% = 0.23333333333333334
- Median = 0.125
- 25% = 0.0
- Min = 0.0

#### recall
- Mean = 0.03125
- Standard deviation = 0.024206145913796356
- Max = 0.05
- 75% = 0.05
- Median = 0.05
- 25% = 0.0
- Min = 0.0

#### facing_probas
- Mean = [0.16572917 0.33401042 0.25203125 0.25390625 0.17776042]
- Standard deviation = [0.06558258 0.09678556 0.06394219 0.05333127 0.05395268]
- Max = [0.2575     0.50208333 0.34958333 0.37041667 0.27375   ]
- 75% = [0.21458333 0.39010417 0.30375    0.27208333 0.22166667]
- Median = [0.16770833 0.358125   0.2375     0.243125   0.16708333]
- 25% = [0.1078125  0.24041667 0.19520833 0.2240625  0.13760417]
- Min = [0.07083333 0.21       0.17666667 0.17916667 0.10375   ]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 76.5 | 3.5 |
| Actual Positive | 19.375 | 0.625 |

### robot-4
#### accuracy
- Mean = 0.7837500000000001
- Standard deviation = 0.014086784586980818
- Max = 0.8
- 75% = 0.8
- Median = 0.78
- 25% = 0.7775000000000001
- Min = 0.76

#### f1
- Mean = 0.21235474295819123
- Standard deviation = 0.06829821261356323
- Max = 0.28571428571428575
- 75% = 0.27142857142857146
- Median = 0.22844827586206895
- 25% = 0.16346153846153846
- Min = 0.08333333333333334

#### precision
- Mean = 0.39375
- Standard deviation = 0.09049919428738946
- Max = 0.5
- 75% = 0.5
- Median = 0.3666666666666667
- 25% = 0.3333333333333333
- Min = 0.25

#### recall
- Mean = 0.15
- Standard deviation = 0.05590169943749474
- Max = 0.2
- 75% = 0.2
- Median = 0.175
- 25% = 0.1
- Min = 0.05

#### facing_probas
- Mean = [0.17973958 0.26645833 0.268125   0.33005208 0.23473958]
- Standard deviation = [0.07057949 0.0835853  0.05096848 0.05848212 0.07723828]
- Max = [0.27708333 0.38458333 0.365      0.43583333 0.38166667]
- 75% = [0.23270833 0.34291667 0.29927083 0.36333333 0.274375  ]
- Median = [0.1975     0.27083333 0.25791667 0.313125   0.24333333]
- 25% = [0.12166667 0.175      0.2275     0.27885417 0.15739583]
- Min = [0.05666667 0.16375    0.20875    0.26708333 0.13666667]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 75.375 | 4.625 |
| Actual Positive | 17.0 | 3.0 |

### robot-5
#### accuracy
- Mean = 0.7825
- Standard deviation = 0.03526683994916474
- Max = 0.8
- 75% = 0.8
- Median = 0.795
- 25% = 0.79
- Min = 0.69

#### f1
- Mean = 0.10450940070505288
- Standard deviation = 0.06835116570928215
- Max = 0.16666666666666669
- 75% = 0.16666666666666669
- Median = 0.1245593419506463
- 25% = 0.06521739130434784
- Min = 0.0

#### precision
- Mean = 0.29289215686274506
- Standard deviation = 0.19908464478728824
- Max = 0.5
- 75% = 0.5
- Median = 0.3333333333333333
- 25% = 0.1323529411764706
- Min = 0.0

#### recall
- Mean = 0.06875
- Standard deviation = 0.04960783708246107
- Max = 0.15
- 75% = 0.1
- Median = 0.07500000000000001
- 25% = 0.037500000000000006
- Min = 0.0

#### facing_probas
- Mean = [0.10375    0.20588542 0.15442708 0.2846875  0.25265625]
- Standard deviation = [0.03474673 0.05363053 0.06190373 0.03467905 0.05767972]
- Max = [0.15125    0.28541667 0.25958333 0.34583333 0.34083333]
- 75% = [0.12583333 0.2534375  0.19197917 0.296875   0.28052083]
- Median = [0.12145833 0.20625    0.139375   0.29       0.25104167]
- 25% = [0.066875   0.14875    0.11666667 0.27416667 0.21239583]
- Min = [0.05       0.13791667 0.05666667 0.22583333 0.17416667]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 76.875 | 3.125 |
| Actual Positive | 18.625 | 1.375 |

### robot-6
#### accuracy
- Mean = 0.13374999999999998
- Standard deviation = 0.0591475908216049
- Max = 0.25
- 75% = 0.165
- Median = 0.125
- 25% = 0.0875
- Min = 0.06

#### f1
- Mean = 0.2312659839700826
- Standard deviation = 0.08975659869333966
- Max = 0.4
- 75% = 0.28316773816481594
- Median = 0.22134387351778656
- 25% = 0.16089024804621133
- Min = 0.11320754716981131

#### precision
- Mean = 1.0
- Standard deviation = 0.0
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 1.0
- Min = 1.0

#### recall
- Mean = 0.13374999999999998
- Standard deviation = 0.0591475908216049
- Max = 0.25
- 75% = 0.165
- Median = 0.125
- 25% = 0.0875
- Min = 0.06

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
| Actual Positive | 86.625 | 13.375 |

