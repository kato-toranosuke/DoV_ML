# ExtraTreesClassifier_RandomUnderSampler_2022-04-14-21-44_no2
## Constants
- CSV_PATH = ../out/csv/experiment
- OUTPUT_PATH = ../out/experiment_result/data_of_2022-03-23_eval_system/AGC-15deg-0angle-3m
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
- DISTANCE = [3]
- AGC_STATUS = ['AGC-15deg']
- ANGLES = [60, 75, 90, 105, 120]

## Loaded CSV
- 2022-03-23_raspi_48000Hz_w1_N2^12_overlap80_all.csv

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
	- sampling_strategy_ = OrderedDict([(0, 15)])
	- sample_indices_ = [ 3  8 45 57 16 66 42 60 15 69 58 62 40  6 64  0  1  2 18 19 20 36 37 38
 54 55 56 72 73 74]

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
	- min_samples_leaf = 5
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
- tdoa_mean = 0.18445970770695574
- tdoa_max = 0.1591269841269841
- diff_auc = 0.11706349206349205
- gp_auc_mean = 0.11328244784222392
- gp_max_ix_range = 0.09514007642451497
- gp_max_val_mean = 0.07687335815215486
- high_power = 0.05464546025387286
- gp_max_val_max = 0.05357142857142856
- gp_max_val_min = 0.049574361542313476
- gp_max_ix_mean = 0.047531397407056385
- ratio_max_to_10ms_ave_peaks = 0.030886482150020052
- gp_max_val_std = 0.014372581536760659
- coe1[0] = 0.0021701388888888886
- gp_max_val_range = 0.0013020833333333363
- low_power = 0.0
- hlbr = 0.0
- coe1[1] = 0.0
- coe3[0] = 0.0
- coe3[1] = 0.0
- coe3[2] = 0.0
- coe3[3] = 0.0
- ratio_max_to_9th_ave_peaks = 0.0
- ac_std = 0.0
- ac_auc = 0.0
- diff_std = 0.0
- srmr = 0.0
- gp_max_ix_std = 0.0
- gp_max_ix_min = 0.0
- gp_max_ix_max = 0.0
- gp_auc_std = 0.0
- gp_auc_range = 0.0
- gp_auc_min = 0.0
- gp_auc_max = 0.0
- tdoa_std = 0.0
- tdoa_range = 0.0
- tdoa_min = 0.0

## Evaluation
cv = 8
### robot-1
#### accuracy
- Mean = 0.8562500000000001
- Standard deviation = 0.04060095442227928
- Max = 0.92
- 75% = 0.8775
- Median = 0.86
- 25% = 0.8325
- Min = 0.79

#### f1
- Mean = 0.6815702869183442
- Standard deviation = 0.07526728283051533
- Max = 0.8000000000000002
- 75% = 0.7300531914893618
- Median = 0.6888888888888889
- 25% = 0.6335748792270531
- Min = 0.5714285714285714

#### precision
- Mean = 0.6249139159052952
- Standard deviation = 0.10043055729420107
- Max = 0.8
- 75% = 0.6675
- Median = 0.6148148148148148
- 25% = 0.5626923076923076
- Min = 0.4827586206896552

#### recall
- Mean = 0.75625
- Standard deviation = 0.0582961190818051
- Max = 0.85
- 75% = 0.8
- Median = 0.75
- 25% = 0.7375
- Min = 0.65

#### facing_probas
- Mean = [0.58423526 0.33759449 0.45460365 0.3160397  0.33816978]
- Standard deviation = [0.0167578  0.0511317  0.03438427 0.07781252 0.07514732]
- Max = [0.60555339 0.40700152 0.5081071  0.48310853 0.47554249]
- 75% = [0.59761353 0.37921023 0.48189304 0.33814419 0.37304839]
- Median = [0.58869909 0.34203785 0.44885543 0.31092316 0.32280839]
- 25% = [0.57262368 0.29995432 0.42766235 0.24251109 0.26749691]
- Min = [0.55685548 0.25811905 0.40384722 0.24050325 0.26331349]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 70.5 | 9.5 |
| Actual Positive | 4.875 | 15.125 |

### robot-2
#### accuracy
- Mean = 0.6849999999999999
- Standard deviation = 0.0570087712549569
- Max = 0.77
- 75% = 0.715
- Median = 0.7
- 25% = 0.6575
- Min = 0.58

#### f1
- Mean = 0.4519271230439336
- Standard deviation = 0.054434275606866485
- Max = 0.5490196078431372
- 75% = 0.48498023715415023
- Median = 0.4358054226475279
- 25% = 0.4061224489795918
- Min = 0.39215686274509803

#### precision
- Mean = 0.3532144874320575
- Standard deviation = 0.044890041680789056
- Max = 0.45161290322580644
- 75% = 0.36836734693877554
- Median = 0.3524137931034483
- 25% = 0.3180224403927069
- Min = 0.30357142857142855

#### recall
- Mean = 0.65625
- Standard deviation = 0.15499495959546555
- Max = 0.9
- 75% = 0.7374999999999999
- Median = 0.675
- 25% = 0.5
- Min = 0.45

#### facing_probas
- Mean = [0.55506439 0.65714776 0.57418428 0.41364771 0.4360277 ]
- Standard deviation = [0.04401074 0.03492277 0.02704748 0.05119586 0.06064699]
- Max = [0.62474907 0.71420696 0.61607474 0.51917666 0.53888741]
- 75% = [0.588842   0.68671694 0.58769118 0.43732264 0.45785882]
- Median = [0.5594011  0.65605671 0.57489221 0.39710406 0.42434406]
- 25% = [0.51415298 0.62774514 0.55726452 0.37181602 0.39838075]
- Min = [0.49190583 0.6042302  0.52774363 0.36409253 0.35227543]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 55.375 | 24.625 |
| Actual Positive | 6.875 | 13.125 |

### robot-3
#### accuracy
- Mean = 0.72125
- Standard deviation = 0.0544144971491973
- Max = 0.79
- 75% = 0.75
- Median = 0.725
- 25% = 0.72
- Min = 0.59

#### f1
- Mean = 0.17306128411699373
- Standard deviation = 0.0874790975598118
- Max = 0.2631578947368421
- 75% = 0.2356007944389275
- Median = 0.2078853046594982
- 25% = 0.1185133239831697
- Min = 0.0

#### precision
- Mean = 0.22190656565656566
- Standard deviation = 0.0964933776756815
- Max = 0.3333333333333333
- 75% = 0.2777777777777778
- Median = 0.26136363636363635
- 25% = 0.18181818181818182
- Min = 0.0

#### recall
- Mean = 0.1625
- Standard deviation = 0.09921567416492214
- Max = 0.3
- 75% = 0.25
- Median = 0.175
- 25% = 0.08750000000000001
- Min = 0.0

#### facing_probas
- Mean = [0.56401681 0.66404725 0.62760652 0.4876364  0.56966571]
- Standard deviation = [0.04263839 0.03424202 0.04906971 0.05885531 0.01514186]
- Max = [0.6422029  0.7183398  0.69375422 0.5834749  0.60009756]
- 75% = [0.58390197 0.69017483 0.67255257 0.52704448 0.57459092]
- Median = [0.57375595 0.65243822 0.63069666 0.47938297 0.56886869]
- 25% = [0.52731557 0.63732359 0.57529858 0.44707987 0.56035462]
- Min = [0.50220317 0.62596364 0.56349542 0.39658347 0.54564976]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 68.875 | 11.125 |
| Actual Positive | 16.75 | 3.25 |

### robot-4
#### accuracy
- Mean = 0.79125
- Standard deviation = 0.023150323971815188
- Max = 0.8
- 75% = 0.8
- Median = 0.8
- 25% = 0.8
- Min = 0.73

#### f1
- Mean = 0.02272727272727273
- Standard deviation = 0.060130711615104346
- Max = 0.18181818181818185
- 75% = 0.0
- Median = 0.0
- 25% = 0.0
- Min = 0.0

#### precision
- Mean = 0.028846153846153848
- Standard deviation = 0.07631974935763243
- Max = 0.23076923076923078
- 75% = 0.0
- Median = 0.0
- 25% = 0.0
- Min = 0.0

#### recall
- Mean = 0.01875
- Standard deviation = 0.049607837082461075
- Max = 0.15
- 75% = 0.0
- Median = 0.0
- 25% = 0.0
- Min = 0.0

#### facing_probas
- Mean = [0.54919894 0.60259909 0.56090419 0.44096988 0.53942426]
- Standard deviation = [0.02307144 0.02207388 0.03430599 0.0569894  0.01381094]
- Max = [0.57978626 0.64399565 0.6105494  0.54510661 0.55219099]
- 75% = [0.56228857 0.61164326 0.59737825 0.46928174 0.54802345]
- Median = [0.55087437 0.59687493 0.54668466 0.42734299 0.54328045]
- 25% = [0.54347194 0.58773495 0.53976943 0.39191901 0.53817255]
- Min = [0.49863582 0.57606169 0.51088763 0.37625974 0.50552994]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 78.75 | 1.25 |
| Actual Positive | 19.625 | 0.375 |

### robot-5
#### accuracy
- Mean = 0.8300000000000001
- Standard deviation = 0.03240370349203928
- Max = 0.88
- 75% = 0.8525
- Median = 0.835
- 25% = 0.7975000000000001
- Min = 0.79

#### f1
- Mean = 0.4588183557623286
- Standard deviation = 0.14124834302466213
- Max = 0.7
- 75% = 0.5363636363636364
- Median = 0.49490662139219016
- 25% = 0.3485023041474654
- Min = 0.2222222222222222

#### precision
- Mean = 0.6159621628371629
- Standard deviation = 0.12934958055716592
- Max = 0.8
- 75% = 0.7068181818181818
- Median = 0.6586538461538461
- 25% = 0.48863636363636365
- Min = 0.42857142857142855

#### recall
- Mean = 0.38125
- Standard deviation = 0.15799030824705673
- Max = 0.7
- 75% = 0.45
- Median = 0.4
- 25% = 0.25
- Min = 0.15

#### facing_probas
- Mean = [0.41633077 0.46499693 0.48195499 0.40772552 0.52251164]
- Standard deviation = [0.06587421 0.05574885 0.02357517 0.06551464 0.02827448]
- Max = [0.53983947 0.5574605  0.52841306 0.56034641 0.55587639]
- 75% = [0.45114656 0.48665072 0.49196461 0.42516027 0.54960396]
- Median = [0.39986619 0.46316366 0.47715327 0.39509497 0.52405071]
- 25% = [0.36589159 0.43989031 0.47065481 0.36695951 0.50624393]
- Min = [0.33789286 0.36148611 0.44270004 0.3291645  0.47116198]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 75.375 | 4.625 |
| Actual Positive | 12.375 | 7.625 |

### robot-6
#### accuracy
- Mean = 0.395
- Standard deviation = 0.0421307488658818
- Max = 0.46
- 75% = 0.425
- Median = 0.4
- 25% = 0.35
- Min = 0.34

#### f1
- Mean = 0.5650010599519955
- Standard deviation = 0.04329345001787225
- Max = 0.6301369863013699
- 75% = 0.5964397496087637
- Median = 0.5713556814123169
- 25% = 0.5185185185185185
- Min = 0.5074626865671642

#### precision
- Mean = 1.0
- Standard deviation = 0.0
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 1.0
- Min = 1.0

#### recall
- Mean = 0.395
- Standard deviation = 0.0421307488658818
- Max = 0.46
- 75% = 0.425
- Median = 0.4
- 25% = 0.35
- Min = 0.34

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
| Actual Positive | 60.5 | 39.5 |

