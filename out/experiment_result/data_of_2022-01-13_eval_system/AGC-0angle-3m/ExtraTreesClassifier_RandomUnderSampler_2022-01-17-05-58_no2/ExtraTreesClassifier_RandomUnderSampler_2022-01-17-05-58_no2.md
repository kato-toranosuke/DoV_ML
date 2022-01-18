# ExtraTreesClassifier_RandomUnderSampler_2022-01-17-05-58_no2
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
- gp_auc_max = 0.09607949262930572
- srmr = 0.0772572978534656
- gp_max_val_max = 0.07173812784680937
- gp_max_val_mean = 0.06291873042042855
- diff_auc = 0.06223022585519431
- gp_auc_min = 0.05837650072737618
- diff_std = 0.05532066764354724
- gp_auc_mean = 0.054718343802191476
- coe1[0] = 0.05000998744061571
- high_power = 0.04835631974157222
- gp_max_val_min = 0.0467382473665801
- coe1[1] = 0.03279844558485582
- gp_max_ix_std = 0.032108933628992635
- tdoa_std = 0.02570569549459151
- hlbr = 0.022913964065804985
- low_power = 0.019999024370864846
- gp_auc_range = 0.01743161819408597
- coe3[3] = 0.016899543088869314
- gp_max_val_std = 0.015334322765400933
- ac_auc = 0.01514215845147269
- tdoa_mean = 0.01510679932967332
- gp_max_ix_mean = 0.014716010901409095
- gp_max_val_range = 0.014333123612205163
- gp_max_ix_max = 0.013138634756008401
- gp_auc_std = 0.011320008574173769
- ac_std = 0.011047467155135576
- ratio_max_to_9th_ave_peaks = 0.009666540966766437
- ratio_max_to_10ms_ave_peaks = 0.008248872116576794
- coe3[2] = 0.008085616704615979
- tdoa_max = 0.0050646191467389415
- tdoa_range = 0.004005979497664386
- gp_max_ix_range = 0.0031886802670070243
- coe3[0] = 0.0
- coe3[1] = 0.0
- gp_max_ix_min = 0.0
- tdoa_min = 0.0

## Evaluation
cv = 8
### robot-1
#### accuracy
- Mean = 0.96625
- Standard deviation = 0.035685256059050485
- Max = 1.0
- 75% = 0.9924999999999999
- Median = 0.975
- 25% = 0.96
- Min = 0.89

#### f1
- Mean = 0.8979506649599082
- Standard deviation = 0.12235778125720036
- Max = 1.0
- 75% = 0.9807692307692307
- Median = 0.9388004895960833
- 25% = 0.8892773892773893
- Min = 0.6206896551724138

#### precision
- Mean = 0.977116704805492
- Standard deviation = 0.04415052947728774
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 0.9868421052631579
- Min = 0.8695652173913043

#### recall
- Mean = 0.85625
- Standard deviation = 0.187812240016459
- Max = 1.0
- 75% = 1.0
- Median = 0.925
- 25% = 0.8375
- Min = 0.45

#### facing_probas
- Mean = [0.7405506  0.3528125  0.03331101 0.0124628  0.01155506]
- Standard deviation = [0.1059612  0.06354031 0.02353852 0.01157768 0.00651442]
- Max = [0.88190476 0.47130952 0.07642857 0.04142857 0.02482143]
- 75% = [0.8114881  0.38608631 0.04544643 0.01160714 0.01392857]
- Median = [0.75020833 0.34098214 0.03235119 0.00910714 0.01217262]
- 25% = [0.70144345 0.31511905 0.01254464 0.00709821 0.00744048]
- Min = [0.55261905 0.26238095 0.00267857 0.00142857 0.00125   ]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 79.5 | 0.5 |
| Actual Positive | 2.875 | 17.125 |

### robot-2
#### accuracy
- Mean = 0.9475
- Standard deviation = 0.008291561975888477
- Max = 0.96
- 75% = 0.95
- Median = 0.95
- 25% = 0.9475
- Min = 0.93

#### f1
- Mean = 0.8501819237113355
- Standard deviation = 0.028867818555964434
- Max = 0.888888888888889
- 75% = 0.8648648648648648
- Median = 0.8571428571428571
- 25% = 0.8487394957983193
- Min = 0.787878787878788

#### precision
- Mean = 0.9852941176470589
- Standard deviation = 0.02547133540542467
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 0.9852941176470589
- Min = 0.9411764705882353

#### recall
- Mean = 0.75
- Standard deviation = 0.05000000000000002
- Max = 0.8
- 75% = 0.8
- Median = 0.75
- 25% = 0.7375
- Min = 0.65

#### facing_probas
- Mean = [0.41934524 0.7021875  0.16837798 0.02268601 0.01026042]
- Standard deviation = [0.07433761 0.0502695  0.05720305 0.01902972 0.00459481]
- Max = [0.56386905 0.77559524 0.28642857 0.0597619  0.02071429]
- 75% = [0.4414881  0.73669643 0.17891369 0.02677083 0.01111607]
- Median = [0.41505952 0.6935119  0.16782738 0.01467262 0.01      ]
- 25% = [0.38160714 0.68619048 0.14779762 0.01130952 0.00766369]
- Min = [0.31339286 0.60130952 0.075      0.0039881  0.00375   ]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 79.75 | 0.25 |
| Actual Positive | 5.0 | 15.0 |

### robot-3
#### accuracy
- Mean = 0.9874999999999999
- Standard deviation = 0.01561249499599601
- Max = 1.0
- 75% = 1.0
- Median = 0.99
- 25% = 0.9875
- Min = 0.95

#### f1
- Mean = 0.9692034083802377
- Standard deviation = 0.03813117112108043
- Max = 1.0
- 75% = 1.0
- Median = 0.975609756097561
- 25% = 0.9682692307692308
- Min = 0.8780487804878048

#### precision
- Mean = 0.9639880952380953
- Standard deviation = 0.04619043783749023
- Max = 1.0
- 75% = 1.0
- Median = 0.9761904761904762
- 25% = 0.9517857142857142
- Min = 0.8571428571428571

#### recall
- Mean = 0.9750000000000001
- Standard deviation = 0.03535533905932738
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 0.95
- Min = 0.9

#### facing_probas
- Mean = [0.06982143 0.59238095 0.87979911 0.29729911 0.04161458]
- Standard deviation = [0.029124   0.13510908 0.03578046 0.10577216 0.02278694]
- Max = [0.13738095 0.77666667 0.92559524 0.48327381 0.09559524]
- 75% = [0.07982143 0.68537202 0.90177083 0.36081845 0.04574405]
- Median = [0.05803571 0.61333333 0.88464286 0.27595238 0.0327381 ]
- 25% = [0.05142857 0.5313244  0.87229167 0.23401786 0.0275744 ]
- Min = [0.04107143 0.30535714 0.79678571 0.13660714 0.02083333]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 79.25 | 0.75 |
| Actual Positive | 0.5 | 19.5 |

### robot-4
#### accuracy
- Mean = 0.955
- Standard deviation = 0.016583123951776982
- Max = 0.98
- 75% = 0.96
- Median = 0.96
- 25% = 0.955
- Min = 0.92

#### f1
- Mean = 0.8884615606869612
- Standard deviation = 0.0349201095025217
- Max = 0.9500000000000001
- 75% = 0.9022727272727273
- Median = 0.8918128654970761
- 25% = 0.8791666666666667
- Min = 0.8260869565217392

#### precision
- Mean = 0.901068376068376
- Standard deviation = 0.08663838274796988
- Max = 1.0
- 75% = 0.9624999999999999
- Median = 0.9222222222222223
- 25% = 0.8458333333333333
- Min = 0.7307692307692307

#### recall
- Mean = 0.8875
- Standard deviation = 0.06959705453537525
- Max = 1.0
- 75% = 0.95
- Median = 0.875
- 25% = 0.8375
- Min = 0.8

#### facing_probas
- Mean = [0.01906994 0.07274554 0.4219122  0.78865327 0.22541667]
- Standard deviation = [0.01443811 0.04083421 0.09074081 0.04870052 0.0807821 ]
- Max = [0.04863095 0.14291667 0.54214286 0.85059524 0.39529762]
- 75% = [0.02544643 0.09647321 0.485625   0.84001488 0.25063988]
- Median = [0.01360119 0.07571429 0.44369048 0.77797619 0.19958333]
- 25% = [0.0072619  0.03668155 0.34159226 0.74293155 0.17059524]
- Min = [0.00625    0.01928571 0.28857143 0.73696429 0.14428571]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 77.75 | 2.25 |
| Actual Positive | 2.25 | 17.75 |

### robot-5
#### accuracy
- Mean = 0.9475
- Standard deviation = 0.02277608394786072
- Max = 0.98
- 75% = 0.965
- Median = 0.945
- 25% = 0.9275
- Min = 0.92

#### f1
- Mean = 0.8440220984725628
- Standard deviation = 0.07483184441407449
- Max = 0.9473684210526316
- 75% = 0.9035087719298246
- Median = 0.8403361344537814
- 25% = 0.7784090909090909
- Min = 0.7499999999999999

#### precision
- Mean = 1.0
- Standard deviation = 0.0
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 1.0
- Min = 1.0

#### recall
- Mean = 0.7375
- Standard deviation = 0.11388041973930375
- Max = 0.9
- 75% = 0.8250000000000001
- Median = 0.725
- 25% = 0.6375
- Min = 0.6

#### facing_probas
- Mean = [0.00989583 0.02114583 0.06947917 0.58567708 0.74759673]
- Standard deviation = [0.00623473 0.01409702 0.02629635 0.11116767 0.058824  ]
- Max = [0.0197619  0.04196429 0.11708333 0.78196429 0.86970238]
- 75% = [0.01348214 0.0365625  0.07638393 0.64941964 0.78116071]
- Median = [0.010625   0.01514881 0.06110119 0.57553571 0.72916667]
- 25% = [0.00504464 0.00958333 0.05589286 0.49315476 0.70912202]
- Min = [0.00071429 0.00434524 0.03660714 0.43125    0.67470238]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 80.0 | 0.0 |
| Actual Positive | 5.25 | 14.75 |

### robot-6
#### accuracy
- Mean = 0.84125
- Standard deviation = 0.06071192222290447
- Max = 0.92
- 75% = 0.8725
- Median = 0.865
- 25% = 0.8225
- Min = 0.72

#### f1
- Mean = 0.9125633216876877
- Standard deviation = 0.03695881447017257
- Max = 0.9583333333333334
- 75% = 0.9319035157583342
- Median = 0.9276062331090794
- 25% = 0.9022967329894376
- Min = 0.8372093023255813

#### precision
- Mean = 1.0
- Standard deviation = 0.0
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 1.0
- Min = 1.0

#### recall
- Mean = 0.84125
- Standard deviation = 0.06071192222290447
- Max = 0.92
- 75% = 0.8725
- Median = 0.865
- 25% = 0.8225
- Min = 0.72

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
| Actual Positive | 15.875 | 84.125 |

