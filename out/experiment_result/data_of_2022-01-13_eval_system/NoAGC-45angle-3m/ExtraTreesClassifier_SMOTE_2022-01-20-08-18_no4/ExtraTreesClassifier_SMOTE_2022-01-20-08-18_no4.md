# ExtraTreesClassifier_SMOTE_2022-01-20-08-18_no4
## Constants
- CSV_PATH = ../out/csv/experiment
- OUTPUT_PATH = ../out/experiment_result/data_of_2022-01-13_eval_system/NoAGC-45angle-3m
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
- AGC_STATUS = ['NoAGC']

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
	- n_estimators = 170
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
- gp_auc_mean = 0.13309181095097988
- gp_max_val_mean = 0.12595405072601676
- gp_auc_max = 0.11946797408481427
- gp_max_val_min = 0.11320776250643316
- gp_auc_min = 0.10410796804917165
- gp_max_val_max = 0.08186099986852381
- srmr = 0.07728656042353724
- diff_auc = 0.020003154146384632
- diff_std = 0.01958589040966244
- hlbr = 0.015515310759061108
- ac_std = 0.014451575028845892
- coe1[0] = 0.014180239806310054
- gp_max_ix_mean = 0.012235819410595832
- gp_max_ix_max = 0.011960003755064223
- coe1[1] = 0.011803861445012182
- tdoa_mean = 0.011478322806322942
- high_power = 0.010788953560616751
- coe3[2] = 0.010344038447622337
- gp_max_ix_std = 0.010103957293260591
- low_power = 0.009818149271397384
- ac_auc = 0.009449841182947326
- coe3[3] = 0.008705311568705049
- tdoa_std = 0.006872369055550275
- tdoa_max = 0.006121705687448144
- gp_auc_std = 0.005894629970869924
- gp_max_val_std = 0.005576212545943189
- ratio_max_to_10ms_ave_peaks = 0.005072222070759364
- gp_auc_range = 0.004777374687402284
- gp_max_val_range = 0.004704762870104238
- ratio_max_to_9th_ave_peaks = 0.0041119820790906205
- gp_max_ix_range = 0.003981442168409054
- tdoa_range = 0.0036395951914145546
- gp_max_ix_min = 0.0019756761638582243
- tdoa_min = 0.0018704720078646642
- coe3[0] = 0.0
- coe3[1] = 0.0

## Evaluation
cv = 8
### robot-1
#### accuracy
- Mean = 0.9862500000000001
- Standard deviation = 0.014947825928876762
- Max = 1.0
- 75% = 1.0
- Median = 0.99
- 25% = 0.9775
- Min = 0.96

#### f1
- Mean = 0.9680106714990435
- Standard deviation = 0.03442486209562824
- Max = 1.0
- 75% = 1.0
- Median = 0.9761904761904762
- 25% = 0.946843853820598
- Min = 0.9090909090909091

#### precision
- Mean = 0.9401350461133069
- Standard deviation = 0.06388410823606988
- Max = 1.0
- 75% = 1.0
- Median = 0.9545454545454546
- 25% = 0.8992094861660078
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
- Mean = [0.96775735 0.75889706 0.03724265 0.0025     0.00231618]
- Standard deviation = [0.01386644 0.03757454 0.00912113 0.00206407 0.00139851]
- Max = [0.99264706 0.81735294 0.05735294 0.00647059 0.00441176]
- 75% = [0.97897059 0.77529412 0.04058824 0.00375    0.00323529]
- Median = [0.96352941 0.75661765 0.03411765 0.00220588 0.00235294]
- 25% = [9.57720588e-01 7.38235294e-01 3.13970588e-02 5.14705882e-04
 1.10294118e-03]
- Min = [9.50294118e-01 7.08235294e-01 2.67647059e-02 2.94117647e-04
 2.94117647e-04]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 78.625 | 1.375 |
| Actual Positive | 0.0 | 20.0 |

### robot-2
#### accuracy
- Mean = 0.98375
- Standard deviation = 0.014086784586980818
- Max = 1.0
- 75% = 1.0
- Median = 0.98
- 25% = 0.9775
- Min = 0.96

#### f1
- Mean = 0.9562391338707128
- Standard deviation = 0.03858426297407174
- Max = 1.0
- 75% = 1.0
- Median = 0.9473684210526316
- 25% = 0.9402560455192035
- Min = 0.888888888888889

#### precision
- Mean = 1.0
- Standard deviation = 0.0
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 1.0
- Min = 1.0

#### recall
- Mean = 0.91875
- Standard deviation = 0.07043392293490403
- Max = 1.0
- 75% = 1.0
- Median = 0.9
- 25% = 0.8875
- Min = 0.8

#### facing_probas
- Mean = [0.96591912 0.96169118 0.86051471 0.09047794 0.00268382]
- Standard deviation = [0.02333765 0.02480754 0.05527314 0.06675773 0.00261598]
- Max = [0.99176471 0.99411765 0.94676471 0.23176471 0.00941176]
- 75% = [0.98823529 0.98698529 0.91823529 0.12808824 0.0025    ]
- Median = [0.97132353 0.95897059 0.83808824 0.05617647 0.00161765]
- 25% = [0.94088235 0.93985294 0.80867647 0.04301471 0.00139706]
- Min = [9.34117647e-01 9.26470588e-01 8.05294118e-01 2.58823529e-02
 8.82352941e-04]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 80.0 | 0.0 |
| Actual Positive | 1.625 | 18.375 |

### robot-3
#### accuracy
- Mean = 0.98625
- Standard deviation = 0.01576190026614813
- Max = 1.0
- 75% = 1.0
- Median = 0.99
- 25% = 0.98
- Min = 0.95

#### f1
- Mean = 0.9625747059957586
- Standard deviation = 0.04480238946154059
- Max = 1.0
- 75% = 1.0
- Median = 0.9743589743589743
- 25% = 0.9473684210526316
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
- Mean = 0.9312499999999999
- Standard deviation = 0.07880950133074056
- Max = 1.0
- 75% = 1.0
- Median = 0.95
- 25% = 0.9
- Min = 0.75

#### facing_probas
- Mean = [0.20169118 0.91720588 0.96147059 0.88580882 0.09011029]
- Standard deviation = [0.08054807 0.03866389 0.02800612 0.06041125 0.06506135]
- Max = [0.35235294 0.98029412 0.99088235 0.96264706 0.21735294]
- 75% = [0.23367647 0.94323529 0.98919118 0.94522059 0.13316176]
- Median = [0.20397059 0.91205882 0.96338235 0.89044118 0.07441176]
- 25% = [0.1375     0.88051471 0.93433824 0.82580882 0.02897059]
- Min = [0.09911765 0.87529412 0.92882353 0.80058824 0.02382353]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 80.0 | 0.0 |
| Actual Positive | 1.375 | 18.625 |

### robot-4
#### accuracy
- Mean = 0.955
- Standard deviation = 0.01732050807568876
- Max = 0.97
- 75% = 0.97
- Median = 0.96
- 25% = 0.9475
- Min = 0.92

#### f1
- Mean = 0.8735000757059581
- Standard deviation = 0.05272113685897074
- Max = 0.9189189189189189
- 75% = 0.9189189189189189
- Median = 0.888030888030888
- 25% = 0.8511904761904762
- Min = 0.7647058823529412

#### precision
- Mean = 0.9832589285714286
- Standard deviation = 0.029082174599989685
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 0.984375
- Min = 0.9285714285714286

#### recall
- Mean = 0.7875000000000001
- Standard deviation = 0.06959705453537525
- Max = 0.85
- 75% = 0.85
- Median = 0.8
- 25% = 0.75
- Min = 0.65

#### facing_probas
- Mean = [0.00386029 0.24047794 0.92738971 0.96852941 0.81356618]
- Standard deviation = [0.00261598 0.07734245 0.04427287 0.0254246  0.07528671]
- Max = [0.00823529 0.43647059 0.97764706 0.99823529 0.89970588]
- 75% = [0.00595588 0.23448529 0.97191176 0.99536765 0.87794118]
- Median = [0.00294118 0.21279412 0.92823529 0.96544118 0.83411765]
- 25% = [0.00198529 0.2        0.88911765 0.94272059 0.74433824]
- Min = [8.82352941e-04 1.78529412e-01 8.71470588e-01 9.42058824e-01
 6.91470588e-01]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 79.75 | 0.25 |
| Actual Positive | 4.25 | 15.75 |

### robot-5
#### accuracy
- Mean = 0.9975
- Standard deviation = 0.004330127018922197
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 0.9975
- Min = 0.99

#### f1
- Mean = 0.9935897435897436
- Standard deviation = 0.011102889792108196
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 0.9935897435897436
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
- Mean = 0.9875
- Standard deviation = 0.021650635094610987
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 0.9875
- Min = 0.95

#### facing_probas
- Mean = [0.00261029 0.00488971 0.11183824 0.94033088 0.945625  ]
- Standard deviation = [0.00148112 0.00258061 0.0421104  0.03496892 0.02132831]
- Max = [0.005      0.00882353 0.19470588 0.98147059 0.97294118]
- 75% = [0.00367647 0.00669118 0.12198529 0.97448529 0.96426471]
- Median = [0.00264706 0.00470588 0.10147059 0.94264706 0.94867647]
- 25% = [0.00110294 0.00286765 0.07573529 0.90595588 0.92470588]
- Min = [8.82352941e-04 1.47058824e-03 7.32352941e-02 8.98235294e-01
 9.18235294e-01]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 80.0 | 0.0 |
| Actual Positive | 0.25 | 19.75 |

### robot-6
#### accuracy
- Mean = 0.925
- Standard deviation = 0.033911649915626334
- Max = 0.97
- 75% = 0.95
- Median = 0.925
- 25% = 0.9175
- Min = 0.85

#### f1
- Mean = 0.9607106573759517
- Standard deviation = 0.018640611483781797
- Max = 0.9847715736040609
- 75% = 0.9743589743589743
- Median = 0.9610319516407599
- 25% = 0.9569698952879582
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
- Mean = 0.925
- Standard deviation = 0.033911649915626334
- Max = 0.97
- 75% = 0.95
- Median = 0.925
- 25% = 0.9175
- Min = 0.85

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
| Actual Positive | 7.5 | 92.5 |

