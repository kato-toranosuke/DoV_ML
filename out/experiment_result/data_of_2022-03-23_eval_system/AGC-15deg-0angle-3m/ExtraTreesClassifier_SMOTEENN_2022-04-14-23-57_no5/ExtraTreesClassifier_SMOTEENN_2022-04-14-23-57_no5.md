# ExtraTreesClassifier_SMOTEENN_2022-04-14-23-57_no5
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
	- min_samples_leaf = 5
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
- ac_auc = 0.47367489308992805
- srmr = 0.06192293206970939
- gp_auc_std = 0.0411237439131851
- ratio_max_to_10ms_ave_peaks = 0.03603925986520743
- coe3[2] = 0.03268238003498326
- low_power = 0.032488892999779875
- gp_auc_range = 0.02476302154254451
- coe3[3] = 0.024216014457475912
- ac_std = 0.023183214990990644
- ratio_max_to_9th_ave_peaks = 0.022859682497166633
- gp_auc_mean = 0.022006768546962447
- gp_max_val_range = 0.01928285168298745
- gp_max_val_std = 0.019205876301130447
- gp_max_val_min = 0.018876656122440612
- diff_auc = 0.017618524013834364
- coe1[0] = 0.01651098676711602
- gp_max_ix_max = 0.013999105013876712
- gp_max_val_max = 0.013813120586779132
- diff_std = 0.013415837709948303
- gp_auc_min = 0.012134342805134207
- gp_max_val_mean = 0.011618144056641567
- gp_max_ix_range = 0.01102187789380978
- tdoa_range = 0.009042783204590104
- tdoa_max = 0.007960161107208704
- coe1[1] = 0.0063180278087497715
- gp_max_ix_mean = 0.006035245361851164
- tdoa_std = 0.002817178881008668
- gp_max_ix_std = 0.0023632173418777253
- tdoa_mean = 0.0016999019287348806
- high_power = 0.001305357404347009
- hlbr = 0.0
- coe3[0] = 0.0
- coe3[1] = 0.0
- gp_max_ix_min = 0.0
- gp_auc_max = 0.0
- tdoa_min = 0.0

## Evaluation
cv = 8
### robot-1
#### accuracy
- Mean = 0.795
- Standard deviation = 0.08660254037844387
- Max = 0.91
- 75% = 0.8775
- Median = 0.78
- 25% = 0.7475
- Min = 0.65

#### f1
- Mean = 0.43577163598172003
- Standard deviation = 0.2859542407274681
- Max = 0.761904761904762
- 75% = 0.7367346938775511
- Median = 0.4411764705882353
- 25% = 0.1991991991991992
- Min = 0.0

#### precision
- Mean = 0.4470814096697431
- Standard deviation = 0.26573393476789137
- Max = 0.8666666666666667
- 75% = 0.6473354231974922
- Median = 0.42050691244239635
- 25% = 0.27310924369747897
- Min = 0.0

#### recall
- Mean = 0.45625
- Standard deviation = 0.3320744457196308
- Max = 0.9
- 75% = 0.7625
- Median = 0.45
- 25% = 0.17500000000000002
- Min = 0.0

#### facing_probas
- Mean = [0.55755032 0.42377727 0.36116916 0.38265037 0.31050726]
- Standard deviation = [0.16072391 0.21481588 0.1643354  0.27019279 0.25027715]
- Max = [0.85247143 0.91870952 0.78471905 0.99292857 0.89491905]
- 75% = [0.61511269 0.47402996 0.34853731 0.44999339 0.39560729]
- Median = [0.58595933 0.34433005 0.31034028 0.30871429 0.20062004]
- 25% = [0.49559306 0.26186012 0.26792485 0.17385804 0.15703065]
- Min = [0.24649473 0.24405725 0.24799802 0.12265238 0.06565278]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 70.375 | 9.625 |
| Actual Positive | 10.875 | 9.125 |

### robot-2
#### accuracy
- Mean = 0.74875
- Standard deviation = 0.03515590277606311
- Max = 0.81
- 75% = 0.7725
- Median = 0.745
- 25% = 0.725
- Min = 0.7

#### f1
- Mean = 0.2919251885138112
- Standard deviation = 0.1690564134157586
- Max = 0.4912280701754387
- 75% = 0.42706378986866794
- Median = 0.35846030473135526
- 25% = 0.15719696969696972
- Min = 0.0

#### precision
- Mean = 0.3168563350288894
- Standard deviation = 0.15297206962156457
- Max = 0.5555555555555556
- 75% = 0.3909266409266409
- Median = 0.34578804347826086
- 25% = 0.2451923076923077
- Min = 0.0

#### recall
- Mean = 0.31875
- Standard deviation = 0.2317562027217395
- Max = 0.7
- 75% = 0.47500000000000003
- Median = 0.325
- 25% = 0.125
- Min = 0.0

#### facing_probas
- Mean = [0.57427995 0.59310522 0.45850561 0.51505766 0.3584564 ]
- Standard deviation = [0.17667587 0.14891302 0.09882168 0.20596483 0.19014824]
- Max = [0.85913333 0.81366667 0.63889524 0.96259048 0.83454286]
- 75% = [0.69414276 0.67610645 0.49189504 0.57961498 0.36990714]
- Median = [0.55794881 0.61136429 0.46025    0.45318539 0.29825857]
- 25% = [0.4697495  0.54434446 0.42572728 0.38840833 0.23232153]
- Min = [0.25718961 0.3470127  0.26586429 0.26985437 0.21257969]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 68.5 | 11.5 |
| Actual Positive | 13.625 | 6.375 |

### robot-3
#### accuracy
- Mean = 0.775
- Standard deviation = 0.02598076211353318
- Max = 0.81
- 75% = 0.7925
- Median = 0.78
- 25% = 0.7625
- Min = 0.73

#### f1
- Mean = 0.09798319327731092
- Standard deviation = 0.10885918107809091
- Max = 0.24
- 75% = 0.23025210084033615
- Median = 0.04000000000000001
- 25% = 0.0
- Min = 0.0

#### precision
- Mean = 0.16904761904761906
- Standard deviation = 0.2012855509366557
- Max = 0.6
- 75% = 0.2714285714285714
- Median = 0.1
- 25% = 0.0
- Min = 0.0

#### recall
- Mean = 0.07500000000000001
- Standard deviation = 0.08660254037844387
- Max = 0.2
- 75% = 0.1625
- Median = 0.025
- 25% = 0.0
- Min = 0.0

#### facing_probas
- Mean = [0.55356967 0.62921314 0.51677242 0.60154287 0.50752043]
- Standard deviation = [0.16564538 0.18918952 0.14279882 0.17857206 0.12746487]
- Max = [0.80410476 0.85035238 0.70575238 0.93692857 0.78131429]
- 75% = [0.6585904  0.77846657 0.64691825 0.70565    0.53872688]
- Median = [0.56465159 0.6679623  0.52176071 0.59061153 0.50989762]
- 25% = [0.45824643 0.53367351 0.40754067 0.46466458 0.43111238]
- Min = [0.25790141 0.29734318 0.29855397 0.35621075 0.3151873 ]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 76.0 | 4.0 |
| Actual Positive | 18.5 | 1.5 |

### robot-4
#### accuracy
- Mean = 0.6737500000000001
- Standard deviation = 0.12598983093885
- Max = 0.79
- 75% = 0.7575000000000001
- Median = 0.72
- 25% = 0.6525
- Min = 0.42

#### f1
- Mean = 0.26964795393490726
- Standard deviation = 0.14461447590396448
- Max = 0.4878048780487805
- 75% = 0.371685606060606
- Median = 0.27884615384615385
- 25% = 0.19519704433497534
- Min = 0.0

#### precision
- Mean = 0.26685202589807855
- Standard deviation = 0.1285176552941497
- Max = 0.47619047619047616
- 75% = 0.33059210526315785
- Median = 0.25
- 25% = 0.23976608187134502
- Min = 0.0

#### recall
- Mean = 0.36875
- Standard deviation = 0.3040739013792535
- Max = 0.95
- 75% = 0.55
- Median = 0.275
- 25% = 0.1375
- Min = 0.0

#### facing_probas
- Mean = [0.45672089 0.53814399 0.46537479 0.57533797 0.45919147]
- Standard deviation = [0.122813   0.15737352 0.10444625 0.17775326 0.11049727]
- Max = [0.73583333 0.81627619 0.66921429 0.94667143 0.69666667]
- 75% = [0.49019901 0.5988501  0.51866419 0.66199613 0.48483254]
- Median = [0.43631587 0.57547937 0.4656506  0.53782937 0.44921769]
- 25% = [0.38183065 0.44974692 0.38198162 0.44997093 0.40088639]
- Min = [0.32274293 0.28673921 0.33216548 0.36161649 0.2909746 ]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 60.0 | 20.0 |
| Actual Positive | 12.625 | 7.375 |

### robot-5
#### accuracy
- Mean = 0.7725
- Standard deviation = 0.037996710383926664
- Max = 0.81
- 75% = 0.7925
- Median = 0.785
- 25% = 0.7675000000000001
- Min = 0.68

#### f1
- Mean = 0.19777448397013614
- Standard deviation = 0.10377426672383405
- Max = 0.33333333333333326
- 75% = 0.275974025974026
- Median = 0.21825396825396823
- 25% = 0.15043478260869567
- Min = 0.0

#### precision
- Mean = 0.3494047619047619
- Standard deviation = 0.18881155046050963
- Max = 0.6666666666666666
- 75% = 0.4464285714285714
- Median = 0.375
- 25% = 0.2375
- Min = 0.0

#### recall
- Mean = 0.15625
- Standard deviation = 0.10135796712641784
- Max = 0.3
- 75% = 0.225
- Median = 0.15
- 25% = 0.08750000000000001
- Min = 0.0

#### facing_probas
- Mean = [0.28992776 0.39993967 0.3241597  0.53310005 0.45166225]
- Standard deviation = [0.18995463 0.1549416  0.11402035 0.1687397  0.10749544]
- Max = [0.75594762 0.77020476 0.56819524 0.88776667 0.63680952]
- 75% = [0.30549362 0.41458442 0.38206294 0.5910627  0.49409444]
- Median = [0.22574365 0.36906445 0.28360615 0.47690041 0.47077917]
- 25% = [0.20111399 0.30927411 0.23272133 0.43111885 0.38728155]
- Min = [0.09264405 0.2379996  0.21594643 0.34757897 0.25501508]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 74.125 | 5.875 |
| Actual Positive | 16.875 | 3.125 |

### robot-6
#### accuracy
- Mean = 0.27499999999999997
- Standard deviation = 0.09874208829065749
- Max = 0.37
- 75% = 0.37
- Median = 0.3
- 25% = 0.2
- Min = 0.11

#### f1
- Mean = 0.42160630273960353
- Standard deviation = 0.126289476774583
- Max = 0.5401459854014599
- 75% = 0.5401459854014599
- Median = 0.45825426944971537
- 25% = 0.33298015116196933
- Min = 0.19819819819819817

#### precision
- Mean = 1.0
- Standard deviation = 0.0
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 1.0
- Min = 1.0

#### recall
- Mean = 0.27499999999999997
- Standard deviation = 0.09874208829065749
- Max = 0.37
- 75% = 0.37
- Median = 0.3
- 25% = 0.2
- Min = 0.11

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
| Actual Positive | 72.5 | 27.5 |

