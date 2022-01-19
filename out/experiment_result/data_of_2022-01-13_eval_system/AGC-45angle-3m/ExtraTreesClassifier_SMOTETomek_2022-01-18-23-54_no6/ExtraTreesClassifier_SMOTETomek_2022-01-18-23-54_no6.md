# ExtraTreesClassifier_SMOTETomek_2022-01-18-23-54_no6
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
- resampler = SMOTETomek
- estimator = ExtraTreesClassifier

### Arguments for hyperparameter search
- resampler = SMOTETomek
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
	- tomek = None
	- n_jobs = -1
	- n_features_in_ = 36
	- sampling_strategy_ = auto
	- smote_ = SMOTE(n_jobs=-1, random_state=42)
	- tomek_ = TomekLinks(n_jobs=-1, sampling_strategy='all')

- best_estimator
	- base_estimator = ExtraTreeClassifier()
	- n_estimators = 350
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
- gp_max_val_mean = 0.10351092323314866
- gp_max_val_max = 0.09895101316022921
- gp_auc_max = 0.0941373713765292
- gp_max_val_min = 0.09190133055936052
- gp_auc_mean = 0.09117273670556851
- gp_auc_min = 0.08464475274243012
- diff_std = 0.07928143769171735
- srmr = 0.05967779676389785
- diff_auc = 0.05339983078065493
- coe1[1] = 0.045274295901039686
- coe1[0] = 0.03655457262412918
- high_power = 0.030893068569288244
- low_power = 0.027555221054421906
- hlbr = 0.018274692647756323
- coe3[3] = 0.016625588122023735
- gp_max_ix_mean = 0.008559816886230935
- ratio_max_to_10ms_ave_peaks = 0.007412723550319106
- ac_std = 0.005940576550294777
- ac_auc = 0.005507907913970341
- tdoa_mean = 0.004991107562569178
- gp_max_ix_std = 0.004367940053000291
- tdoa_std = 0.0042689049979972435
- coe3[2] = 0.004236457277947805
- gp_max_val_range = 0.004078942266028647
- gp_max_val_std = 0.0036634410426174533
- gp_auc_range = 0.0030669540562869866
- ratio_max_to_9th_ave_peaks = 0.0028875922396471936
- gp_auc_std = 0.002441355193063978
- tdoa_max = 0.0015999695511307048
- tdoa_range = 0.0012199698005162132
- gp_max_ix_min = 0.0011736571785373917
- tdoa_min = 0.0010584182965206739
- gp_max_ix_max = 0.0010209687315345373
- gp_max_ix_range = 0.0006486649195912534
- coe3[0] = 0.0
- coe3[1] = 0.0

## Evaluation
cv = 8
### robot-1
#### accuracy
- Mean = 0.9575
- Standard deviation = 0.022776083947860716
- Max = 0.99
- 75% = 0.9724999999999999
- Median = 0.965
- 25% = 0.93
- Min = 0.93

#### f1
- Mean = 0.8920611689393143
- Standard deviation = 0.06598576912356736
- Max = 0.975609756097561
- 75% = 0.9357696566998892
- Median = 0.919661733615222
- 25% = 0.8382978723404255
- Min = 0.787878787878788

#### precision
- Mean = 0.8885012129577348
- Standard deviation = 0.07461589238654898
- Max = 1.0
- 75% = 0.9380952380952381
- Median = 0.8893280632411067
- 25% = 0.8605072463768115
- Min = 0.7407407407407407

#### recall
- Mean = 0.91875
- Standard deviation = 0.14128318194321643
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 0.925
- Min = 0.65

#### facing_probas
- Mean = [0.99280357 0.89425    0.14294643 0.00658929 0.00894643]
- Standard deviation = [0.00304719 0.04822094 0.11514986 0.00917251 0.01147267]
- Max = [0.998      0.93857143 0.35742857 0.02928571 0.03628571]
- 75% = [0.99453571 0.93071429 0.1705     0.00603571 0.00803571]
- Median = [0.99321429 0.92421429 0.08971429 0.0025     0.00428571]
- 25% = [0.991      0.85192857 0.06610714 0.00157143 0.002     ]
- Min = [9.87857143e-01 8.13571429e-01 4.71428571e-02 2.85714286e-04
 5.71428571e-04]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 77.375 | 2.625 |
| Actual Positive | 1.625 | 18.375 |

### robot-2
#### accuracy
- Mean = 0.9575
- Standard deviation = 0.022776083947860716
- Max = 0.99
- 75% = 0.9724999999999999
- Median = 0.965
- 25% = 0.93
- Min = 0.93

#### f1
- Mean = 0.8914801480310999
- Standard deviation = 0.0571007485197392
- Max = 0.9743589743589743
- 75% = 0.926031294452347
- Median = 0.9039039039039038
- 25% = 0.8494089834515366
- Min = 0.787878787878788

#### precision
- Mean = 0.9375925925925925
- Standard deviation = 0.10819998123679758
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 0.94
- Min = 0.7407407407407407

#### recall
- Mean = 0.8687499999999999
- Standard deviation = 0.10288798520721454
- Max = 1.0
- 75% = 0.95
- Median = 0.875
- 25% = 0.8375
- Min = 0.65

#### facing_probas
- Mean = [0.90648214 0.95705357 0.67894643 0.03417857 0.00485714]
- Standard deviation = [0.02540578 0.01455951 0.0900932  0.02542774 0.00607521]
- Max = [0.95328571 0.97542857 0.811      0.08971429 0.02028571]
- 75% = [0.91789286 0.96839286 0.76428571 0.04521429 0.00482143]
- Median = [0.90778571 0.96064286 0.67557143 0.02492857 0.00235714]
- 25% = [0.88010714 0.94610714 0.59457143 0.01489286 0.00185714]
- Min = [8.77571429e-01 9.31142857e-01 5.55714286e-01 8.85714286e-03
 2.85714286e-04]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 78.375 | 1.625 |
| Actual Positive | 2.625 | 17.375 |

### robot-3
#### accuracy
- Mean = 0.99
- Standard deviation = 0.010000000000000009
- Max = 1.0
- 75% = 1.0
- Median = 0.99
- 25% = 0.9875
- Min = 0.97

#### f1
- Mean = 0.9736705328810593
- Standard deviation = 0.026857691378360422
- Max = 1.0
- 75% = 1.0
- Median = 0.9743589743589743
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
- Mean = 0.95
- Standard deviation = 0.05
- Max = 1.0
- 75% = 1.0
- Median = 0.95
- 25% = 0.9375
- Min = 0.85

#### facing_probas
- Mean = [0.150125   0.988625   0.99425    0.95296429 0.07257143]
- Standard deviation = [0.04230432 0.00755184 0.00430813 0.01413812 0.02831123]
- Max = [0.20671429 0.99528571 0.999      0.97342857 0.12228571]
- 75% = [0.18628571 0.9945     0.99753571 0.96146429 0.09646429]
- Median = [0.15528571 0.99114286 0.995      0.95614286 0.05671429]
- 25% = [0.11367857 0.98625    0.99225    0.94571429 0.05317857]
- Min = [0.08585714 0.97157143 0.98528571 0.92757143 0.04285714]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 80.0 | 0.0 |
| Actual Positive | 1.0 | 19.0 |

### robot-4
#### accuracy
- Mean = 0.95
- Standard deviation = 0.025495097567963917
- Max = 1.0
- 75% = 0.9624999999999999
- Median = 0.945
- 25% = 0.9375
- Min = 0.91

#### f1
- Mean = 0.8663911631103265
- Standard deviation = 0.07886233546327476
- Max = 1.0
- 75% = 0.9111295681063123
- Median = 0.8535714285714285
- 25% = 0.8408812729498165
- Min = 0.7096774193548387

#### precision
- Mean = 0.9068373956960913
- Standard deviation = 0.07768426910368767
- Max = 1.0
- 75% = 1.0
- Median = 0.8792270531400965
- 25% = 0.8602272727272727
- Min = 0.782608695652174

#### recall
- Mean = 0.85
- Standard deviation = 0.1414213562373095
- Max = 1.0
- 75% = 0.9624999999999999
- Median = 0.875
- 25% = 0.7875000000000001
- Min = 0.55

#### facing_probas
- Mean = [0.00125    0.161125   0.965125   0.99464286 0.75525   ]
- Standard deviation = [0.00066911 0.06024628 0.02030148 0.00346925 0.09580243]
- Max = [0.00214286 0.26057143 0.98971429 0.99971429 0.88528571]
- 75% = [0.00189286 0.18864286 0.97753571 0.99660714 0.81142857]
- Median = [0.00121429 0.15128571 0.9705     0.99485714 0.77678571]
- 25% = [5.71428571e-04 1.39000000e-01 9.58678571e-01 9.93500000e-01
 7.27178571e-01]
- Min = [4.28571429e-04 5.87142857e-02 9.24285714e-01 9.87285714e-01
 5.64142857e-01]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 78.0 | 2.0 |
| Actual Positive | 3.0 | 17.0 |

### robot-5
#### accuracy
- Mean = 0.98
- Standard deviation = 0.01732050807568879
- Max = 1.0
- 75% = 1.0
- Median = 0.975
- 25% = 0.97
- Min = 0.95

#### f1
- Mean = 0.9451585043690307
- Standard deviation = 0.04852828344287578
- Max = 1.0
- 75% = 1.0
- Median = 0.9331436699857752
- 25% = 0.9189189189189189
- Min = 0.8571428571428571

#### precision
- Mean = 1.0
- Standard deviation = 0.0
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 1.0
- Min = 1.0

#### recall
- Mean = 0.9
- Standard deviation = 0.08660254037844387
- Max = 1.0
- 75% = 1.0
- Median = 0.875
- 25% = 0.85
- Min = 0.75

#### facing_probas
- Mean = [0.00142857 0.00266071 0.21085714 0.99285714 0.99219643]
- Standard deviation = [0.00158919 0.0021007  0.06644117 0.00202031 0.00621426]
- Max = [0.00542857 0.00771429 0.309      0.99685714 0.998     ]
- 75% = [0.00135714 0.00278571 0.25571429 0.99382143 0.99585714]
- Median = [0.00114286 0.002      0.19764286 0.9925     0.99335714]
- 25% = [3.92857143e-04 1.14285714e-03 1.70000000e-01 9.91535714e-01
 9.91964286e-01]
- Min = [1.42857143e-04 1.00000000e-03 1.06285714e-01 9.89857143e-01
 9.77000000e-01]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 80.0 | 0.0 |
| Actual Positive | 2.0 | 18.0 |

### robot-6
#### accuracy
- Mean = 0.8975
- Standard deviation = 0.04145780987944248
- Max = 0.96
- 75% = 0.94
- Median = 0.885
- 25% = 0.8725
- Min = 0.84

#### f1
- Mean = 0.9454797413927808
- Standard deviation = 0.02297093635358651
- Max = 0.9795918367346939
- 75% = 0.9690721649484536
- Median = 0.9389845772824497
- 25% = 0.9318573893041978
- Min = 0.9130434782608696

#### precision
- Mean = 1.0
- Standard deviation = 0.0
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 1.0
- Min = 1.0

#### recall
- Mean = 0.8975
- Standard deviation = 0.04145780987944248
- Max = 0.96
- 75% = 0.94
- Median = 0.885
- 25% = 0.8725
- Min = 0.84

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
| Actual Positive | 10.25 | 89.75 |

