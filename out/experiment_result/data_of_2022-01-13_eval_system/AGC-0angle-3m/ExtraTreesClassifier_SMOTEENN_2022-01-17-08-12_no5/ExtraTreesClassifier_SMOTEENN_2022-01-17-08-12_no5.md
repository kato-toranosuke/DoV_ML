# ExtraTreesClassifier_SMOTEENN_2022-01-17-08-12_no5
## Constants
- CSV_PATH = ../out/csv/experiment
- OUTPUT_PATH = ../out/experiment_result/data_of_2022-01-13_eval_system/AGC-0angle-3m
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
	- n_estimators = 230
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
	- min_samples_split = 10
	- min_samples_leaf = 1
	- min_weight_fraction_leaf = 0.0
	- max_features = log2
	- max_leaf_nodes = None
	- min_impurity_decrease = 0.0
	- ccp_alpha = 0.0
	- n_features_in_ = 36
	- n_outputs_ = 1
	- classes_ = [0 1]
	- n_classes_ = 2
	- base_estimator_ = ExtraTreeClassifier()

#### Importance of features
- gp_auc_max = 0.10825886075011569
- gp_auc_mean = 0.0775278757065741
- gp_max_val_mean = 0.07427034995132561
- gp_max_val_max = 0.07193762708141904
- gp_auc_min = 0.06929724574739901
- ac_auc = 0.06864909134888443
- gp_max_val_min = 0.06756869049358974
- diff_auc = 0.06038147403712497
- high_power = 0.05906745426600452
- hlbr = 0.055037176283481454
- srmr = 0.05433743294014268
- diff_std = 0.043215225262750706
- ac_std = 0.030216170060960716
- coe1[0] = 0.020737418882517657
- low_power = 0.01836957810103434
- coe3[2] = 0.017714740442892177
- coe3[3] = 0.015962803835949207
- coe1[1] = 0.01217693798317075
- gp_max_val_range = 0.01095792941122166
- gp_auc_std = 0.010946396434564696
- gp_auc_range = 0.008638747331397712
- ratio_max_to_10ms_ave_peaks = 0.007711647747839712
- gp_max_val_std = 0.006413720835815228
- tdoa_std = 0.005473866039885781
- tdoa_mean = 0.005223629850558549
- tdoa_min = 0.0041596478057300745
- gp_max_ix_mean = 0.003263275134040126
- gp_max_ix_min = 0.0032266674700036748
- gp_max_ix_std = 0.0031368402555350637
- tdoa_range = 0.001971900565428749
- gp_max_ix_range = 0.0018645714840563575
- gp_max_ix_max = 0.0016551202277188947
- tdoa_max = 0.00046132677025721583
- ratio_max_to_9th_ave_peaks = 0.00016855946060972585
- coe3[0] = 0.0
- coe3[1] = 0.0

## Evaluation
cv = 8
### robot-1
#### accuracy
- Mean = 0.95875
- Standard deviation = 0.04702060718451007
- Max = 1.0
- 75% = 0.9924999999999999
- Median = 0.975
- 25% = 0.945
- Min = 0.85

#### f1
- Mean = 0.9130698951423568
- Standard deviation = 0.08752380296307048
- Max = 1.0
- 75% = 0.9807692307692307
- Median = 0.9384146341463415
- 25% = 0.875968992248062
- Min = 0.7272727272727273

#### precision
- Mean = 0.8760998964803313
- Standard deviation = 0.14128555223416678
- Max = 1.0
- 75% = 1.0
- Median = 0.9273809523809524
- 25% = 0.7956521739130435
- Min = 0.5714285714285714

#### recall
- Mean = 0.96875
- Standard deviation = 0.03479852726768764
- Max = 1.0
- 75% = 1.0
- Median = 0.975
- 25% = 0.95
- Min = 0.9

#### facing_probas
- Mean = [0.79097796 0.43517607 0.05269948 0.0173901  0.01793658]
- Standard deviation = [0.05097791 0.06855361 0.03021321 0.01750183 0.01575023]
- Max = [0.8816426  0.53684722 0.12384619 0.05522378 0.05181936]
- 75% = [0.80914877 0.47263995 0.05730575 0.02001128 0.02104881]
- Median = [0.78478313 0.45224534 0.03801298 0.00941283 0.01259252]
- 25% = [0.74325226 0.40185054 0.03478101 0.00523521 0.00621109]
- Min = [0.7383549  0.31872015 0.02671515 0.00343961 0.00394367]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 76.5 | 3.5 |
| Actual Positive | 0.625 | 19.375 |

### robot-2
#### accuracy
- Mean = 0.91625
- Standard deviation = 0.039350190596742975
- Max = 0.96
- 75% = 0.95
- Median = 0.92
- 25% = 0.9
- Min = 0.83

#### f1
- Mean = 0.741662787189103
- Standard deviation = 0.17101832751507048
- Max = 0.8947368421052632
- 75% = 0.8648648648648648
- Median = 0.7623604465709728
- 25% = 0.7344497607655501
- Min = 0.32000000000000006

#### precision
- Mean = 0.8881787330316742
- Standard deviation = 0.08265701790294808
- Max = 1.0
- 75% = 0.9419934640522876
- Median = 0.9321266968325792
- 25% = 0.7944444444444445
- Min = 0.7777777777777778

#### recall
- Mean = 0.6625000000000001
- Standard deviation = 0.19162137145944866
- Max = 0.85
- 75% = 0.8
- Median = 0.7
- 25% = 0.6375
- Min = 0.2

#### facing_probas
- Mean = [0.55807219 0.67660524 0.2008577  0.04408925 0.0166357 ]
- Standard deviation = [0.11363749 0.03677182 0.06980998 0.03125842 0.01581618]
- Max = [0.73594306 0.7403568  0.31989683 0.10580961 0.05292788]
- 75% = [0.65027226 0.69104682 0.24019919 0.05753949 0.01788201]
- Median = [0.49970191 0.66912875 0.19117654 0.02624944 0.01064635]
- 25% = [0.4622783  0.65477198 0.1513574  0.02085619 0.00730601]
- Min = [0.44986853 0.62730857 0.11010809 0.01971877 0.00310688]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 78.375 | 1.625 |
| Actual Positive | 6.75 | 13.25 |

### robot-3
#### accuracy
- Mean = 0.94875
- Standard deviation = 0.04484347778663025
- Max = 0.99
- 75% = 0.98
- Median = 0.96
- 25% = 0.945
- Min = 0.84

#### f1
- Mean = 0.8750784184994711
- Standard deviation = 0.09438431958504295
- Max = 0.9743589743589743
- 75% = 0.9500000000000001
- Median = 0.8973684210526316
- 25% = 0.8486486486486486
- Min = 0.6666666666666666

#### precision
- Mean = 0.8987978524743231
- Standard deviation = 0.12635740178520988
- Max = 1.0
- 75% = 0.95
- Median = 0.9428104575163399
- 25% = 0.925
- Min = 0.5714285714285714

#### recall
- Mean = 0.8625
- Standard deviation = 0.08569568250501304
- Max = 0.95
- 75% = 0.95
- Median = 0.875
- 25% = 0.8
- Min = 0.7

#### facing_probas
- Mean = [0.1114742  0.60377225 0.81229852 0.41569085 0.07244344]
- Standard deviation = [0.04413442 0.13655672 0.06210477 0.10876714 0.03525497]
- Max = [0.18806599 0.75989165 0.88823154 0.60772645 0.14087664]
- 75% = [0.12770342 0.72177491 0.87576693 0.46236823 0.09211316]
- Median = [0.10277256 0.64634295 0.81049538 0.38874426 0.05627057]
- 25% = [0.07312403 0.50090034 0.77485367 0.34531811 0.04448523]
- Min = [0.06473637 0.37240286 0.71709601 0.26067797 0.03960507]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 77.625 | 2.375 |
| Actual Positive | 2.75 | 17.25 |

### robot-4
#### accuracy
- Mean = 0.8775000000000001
- Standard deviation = 0.05068283733178325
- Max = 0.98
- 75% = 0.9
- Median = 0.86
- 25% = 0.845
- Min = 0.82

#### f1
- Mean = 0.72982775581322
- Standard deviation = 0.1349505730316914
- Max = 0.9523809523809523
- 75% = 0.7777777777777779
- Median = 0.7310395856455789
- 25% = 0.696078431372549
- Min = 0.45161290322580644

#### precision
- Mean = 0.6605215341268473
- Standard deviation = 0.11492832141190852
- Max = 0.9090909090909091
- 75% = 0.7000000000000001
- Median = 0.624633431085044
- 25% = 0.5794232649071359
- Min = 0.5294117647058824

#### recall
- Mean = 0.85625
- Standard deviation = 0.19595519258238606
- Max = 1.0
- 75% = 0.95
- Median = 0.925
- 25% = 0.8875
- Min = 0.35

#### facing_probas
- Mean = [0.02192488 0.10379175 0.56919676 0.78646462 0.28608535]
- Standard deviation = [0.01841688 0.0459152  0.1147939  0.08188649 0.02100898]
- Max = [0.06037871 0.18698344 0.77886154 0.88652648 0.31878822]
- 75% = [0.03155392 0.1198345  0.65438231 0.85888848 0.30616839]
- Median = [0.01641529 0.08230249 0.53255707 0.79230961 0.28039898]
- 25% = [0.00542361 0.07212526 0.47712071 0.73231192 0.27319923]
- Min = [0.00456332 0.0592349  0.42909653 0.64523447 0.25222792]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 70.625 | 9.375 |
| Actual Positive | 2.875 | 17.125 |

### robot-5
#### accuracy
- Mean = 0.8987499999999999
- Standard deviation = 0.042260353760942414
- Max = 0.97
- 75% = 0.935
- Median = 0.88
- 25% = 0.8674999999999999
- Min = 0.85

#### f1
- Mean = 0.6384596691048303
- Standard deviation = 0.18227266628706035
- Max = 0.9189189189189189
- 75% = 0.8051948051948052
- Median = 0.5818399044205496
- 25% = 0.5042735042735043
- Min = 0.4

#### precision
- Mean = 0.9886363636363636
- Standard deviation = 0.030065355807552176
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 1.0
- Min = 0.9090909090909091

#### recall
- Mean = 0.5
- Standard deviation = 0.21065374432940895
- Max = 0.85
- 75% = 0.675
- Median = 0.425
- 25% = 0.33749999999999997
- Min = 0.25

#### facing_probas
- Mean = [0.01650664 0.02533076 0.14042742 0.74384191 0.74905576]
- Standard deviation = [0.01338808 0.01882737 0.06384131 0.07348353 0.05698695]
- Max = [0.0425509  0.06420376 0.27456643 0.8413034  0.82456496]
- 75% = [0.0235933  0.03488854 0.1556905  0.8164059  0.78750567]
- Median = [0.01235585 0.01766925 0.12361849 0.72592133 0.75705599]
- 25% = [0.00578319 0.01325584 0.1006517  0.69596418 0.70777487]
- Min = [0.00254909 0.00556159 0.06980461 0.63353278 0.65848499]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 79.875 | 0.125 |
| Actual Positive | 10.0 | 10.0 |

### robot-6
#### accuracy
- Mean = 0.77
- Standard deviation = 0.08351646544245034
- Max = 0.92
- 75% = 0.7975
- Median = 0.75
- 25% = 0.725
- Min = 0.65

#### f1
- Mean = 0.867595744591226
- Standard deviation = 0.05220820538639809
- Max = 0.9583333333333334
- 75% = 0.8865849260728453
- Median = 0.8569935665066457
- 25% = 0.8405503160598993
- Min = 0.787878787878788

#### precision
- Mean = 1.0
- Standard deviation = 0.0
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 1.0
- Min = 1.0

#### recall
- Mean = 0.77
- Standard deviation = 0.08351646544245034
- Max = 0.92
- 75% = 0.7975
- Median = 0.75
- 25% = 0.725
- Min = 0.65

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
| Actual Positive | 23.0 | 77.0 |

