# ExtraTreesClassifier_RandomOverSampler_2022-04-12-23-33_no3
## Constants
- CSV_PATH = ../out/csv/experiment
- OUTPUT_PATH = ../out/experiment_result/data_of_2022-03-23_eval_system/AGC-30deg-0angle-3m
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
- AGC_STATUS = ['AGC-30deg']
- ANGLES = [30, 60, 90, 120, 150]

## Loaded CSV
- 2022-03-23_raspi_48000Hz_w1_N2^12_overlap80_all.csv

## Estimator
### Type
- resampler = RandomOverSampler
- estimator = ExtraTreesClassifier

### Arguments for hyperparameter search
- resampler = RandomOverSampler
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
	- shrinkage = None
	- n_features_in_ = 36
	- sampling_strategy_ = OrderedDict([(1, 45)])
	- shrinkage_ = None
	- sample_indices_ = [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23
 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47
 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71
 72 73 74 36 18 72 74 55 37 72 19 36 54  2 36 55 55 37 19 18 37 37  2 20
 19  1 37 56 73 20  1 56 19  0 56 54 20 72 56 38  0 55 55 74 54 56 56 74]

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
	- max_samples = 0.09
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
	- oob_decision_function_ = [[0.55       0.45      ]
 [0.28333333 0.71666667]
 [0.22916667 0.77083333]
 [0.49074074 0.50925926]
 [0.38888889 0.61111111]
 [0.51851852 0.48148148]
 [0.56666667 0.43333333]
 [0.66666667 0.33333333]
 [0.35416667 0.64583333]
 [0.7962963  0.2037037 ]
 [0.85       0.15      ]
 [0.66666667 0.33333333]
 [0.8125     0.1875    ]
 [0.66666667 0.33333333]
 [0.75       0.25      ]
 [0.63888889 0.36111111]
 [0.62962963 0.37037037]
 [0.09259259 0.90740741]
 [0.46296296 0.53703704]
 [0.33333333 0.66666667]
 [0.55833333 0.44166667]
 [0.42592593 0.57407407]
 [0.50833333 0.49166667]
 [0.35185185 0.64814815]
 [0.80833333 0.19166667]
 [0.49074074 0.50925926]
 [0.41666667 0.58333333]
 [0.85       0.15      ]
 [0.95       0.05      ]
 [0.90740741 0.09259259]
 [0.81666667 0.18333333]
 [0.7962963  0.2037037 ]
 [0.64583333 0.35416667]
 [0.59166667 0.40833333]
 [0.4        0.6       ]
 [0.51851852 0.48148148]
 [0.33333333 0.66666667]
 [0.33333333 0.66666667]
 [0.48148148 0.51851852]
 [0.66666667 0.33333333]
 [0.58333333 0.41666667]
 [0.39583333 0.60416667]
 [0.38888889 0.61111111]
 [0.5        0.5       ]
 [0.5        0.5       ]
 [0.83333333 0.16666667]
 [0.79166667 0.20833333]
 [0.80555556 0.19444444]
 [0.72222222 0.27777778]
 [0.69444444 0.30555556]
 [0.80555556 0.19444444]
 [0.475      0.525     ]
 [0.50833333 0.49166667]
 [0.24166667 0.75833333]
 [0.60185185 0.39814815]
 [0.30555556 0.69444444]
 [0.04166667 0.95833333]
 [0.08333333 0.91666667]
 [0.03703704 0.96296296]
 [0.38333333 0.61666667]
 [0.84375    0.15625   ]
 [0.85       0.15      ]
 [0.825      0.175     ]
 [0.86111111 0.13888889]
 [0.825      0.175     ]
 [0.75       0.25      ]
 [0.80555556 0.19444444]
 [0.80555556 0.19444444]
 [0.775      0.225     ]
 [0.60185185 0.39814815]
 [0.47222222 0.52777778]
 [0.28571429 0.71428571]
 [0.08333333 0.91666667]
 [0.23333333 0.76666667]
 [0.16666667 0.83333333]
 [0.33333333 0.66666667]
 [0.46875    0.53125   ]
 [0.10416667 0.89583333]
 [0.13333333 0.86666667]
 [0.275      0.725     ]
 [0.33333333 0.66666667]
 [0.10416667 0.89583333]
 [0.38888889 0.61111111]
 [0.31481481 0.68518519]
 [0.72916667 0.27083333]
 [0.2037037  0.7962963 ]
 [0.33333333 0.66666667]
 [0.275      0.725     ]
 [0.30208333 0.69791667]
 [0.42857143 0.57142857]
 [0.35       0.65      ]
 [0.5        0.5       ]
 [0.27083333 0.72916667]
 [0.33333333 0.66666667]
 [0.2037037  0.7962963 ]
 [0.55833333 0.44166667]
 [0.35       0.65      ]
 [0.28333333 0.71666667]
 [0.37037037 0.62962963]
 [0.04166667 0.95833333]
 [0.25925926 0.74074074]
 [0.53125    0.46875   ]
 [0.31481481 0.68518519]
 [0.0952381  0.9047619 ]
 [0.35       0.65      ]
 [0.57407407 0.42592593]
 [0.08333333 0.91666667]
 [0.64814815 0.35185185]
 [0.55833333 0.44166667]
 [0.11904762 0.88095238]
 [0.07407407 0.92592593]
 [0.43333333 0.56666667]
 [0.55       0.45      ]
 [0.30555556 0.69444444]
 [0.30208333 0.69791667]
 [0.19047619 0.80952381]
 [0.61666667 0.38333333]
 [0.07407407 0.92592593]
 [0.07407407 0.92592593]
 [0.13333333 0.86666667]]
	- oob_score_ = 0.75

#### Importance of features
- gp_auc_mean = 0.1315410159100861
- high_power = 0.11405439595192914
- diff_std = 0.09050814956855223
- gp_max_val_max = 0.08533333333333333
- diff_auc = 0.06451960784313725
- gp_auc_max = 0.06378959276018102
- gp_max_val_range = 0.06285714285714283
- gp_max_val_mean = 0.05955882352941175
- gp_max_ix_max = 0.05546218487394955
- coe3[2] = 0.043676470588235275
- ac_auc = 0.037142857142857144
- tdoa_mean = 0.03548387096774192
- tdoa_range = 0.035374203372624216
- gp_auc_min = 0.03119747899159662
- tdoa_std = 0.027710309930423786
- gp_max_val_std = 0.024264705882352935
- tdoa_max = 0.019038461538461508
- gp_auc_range = 0.009243697478991605
- gp_max_val_min = 0.009243697478991604
- low_power = 0.0
- hlbr = 0.0
- coe1[0] = 0.0
- coe1[1] = 0.0
- coe3[0] = 0.0
- coe3[1] = 0.0
- coe3[3] = 0.0
- ratio_max_to_10ms_ave_peaks = 0.0
- ratio_max_to_9th_ave_peaks = 0.0
- ac_std = 0.0
- srmr = 0.0
- gp_max_ix_std = 0.0
- gp_max_ix_range = 0.0
- gp_max_ix_min = 0.0
- gp_max_ix_mean = 0.0
- gp_auc_std = 0.0
- tdoa_min = 0.0

## Evaluation
cv = 8
### robot-1
#### accuracy
- Mean = 0.87375
- Standard deviation = 0.02689679348918751
- Max = 0.9
- 75% = 0.89
- Median = 0.885
- 25% = 0.8674999999999999
- Min = 0.81

#### f1
- Mean = 0.6961723596156477
- Standard deviation = 0.06114542568252519
- Max = 0.7755102040816326
- 75% = 0.7513888888888889
- Median = 0.70795892169448
- 25% = 0.630827067669173
- Min = 0.6122448979591838

#### precision
- Mean = 0.6798652162014232
- Standard deviation = 0.06890852703763121
- Max = 0.75
- 75% = 0.725
- Median = 0.6971428571428572
- 25% = 0.6637931034482758
- Min = 0.5172413793103449

#### recall
- Mean = 0.73125
- Standard deviation = 0.12231491119238076
- Max = 0.95
- 75% = 0.775
- Median = 0.75
- 25% = 0.6375
- Min = 0.55

#### facing_probas
- Mean = [0.61507292 0.40394792 0.25658333 0.22644792 0.19571875]
- Standard deviation = [0.04575358 0.0759288  0.08703665 0.07033079 0.04711135]
- Max = [0.70808333 0.48683333 0.41733333 0.3795     0.27666667]
- 75% = [0.63460417 0.463375   0.31652083 0.243125   0.21027083]
- Median = [0.60008333 0.423125   0.2265     0.23020833 0.18825   ]
- 25% = [0.588625   0.37383333 0.2128125  0.1771875  0.1696875 ]
- Min = [0.55708333 0.24       0.12583333 0.13958333 0.13625   ]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 72.75 | 7.25 |
| Actual Positive | 5.375 | 14.625 |

### robot-2
#### accuracy
- Mean = 0.8
- Standard deviation = 0.04242640687119284
- Max = 0.85
- 75% = 0.835
- Median = 0.8
- 25% = 0.7775000000000001
- Min = 0.72

#### f1
- Mean = 0.4072087332956898
- Standard deviation = 0.17685501757518662
- Max = 0.6666666666666665
- 75% = 0.5276679841897234
- Median = 0.4285714285714286
- 25% = 0.3125
- Min = 0.08333333333333334

#### precision
- Mean = 0.5090034965034965
- Standard deviation = 0.1680293449471327
- Max = 0.75
- 75% = 0.6230769230769231
- Median = 0.5307692307692308
- 25% = 0.3795454545454546
- Min = 0.25

#### recall
- Mean = 0.38749999999999996
- Standard deviation = 0.21323402636539976
- Max = 0.75
- 75% = 0.4875
- Median = 0.4
- 25% = 0.2625
- Min = 0.05

#### facing_probas
- Mean = [0.58296875 0.60439583 0.56430208 0.36454167 0.22973958]
- Standard deviation = [0.07201278 0.04361769 0.06855078 0.07987264 0.09416119]
- Max = [0.72025    0.6545     0.683      0.51291667 0.37233333]
- 75% = [0.63339583 0.64158333 0.578125   0.4196875  0.29716667]
- Median = [0.55529167 0.603375   0.54354167 0.36016667 0.22866667]
- 25% = [0.54035417 0.5915     0.52814583 0.29558333 0.1496875 ]
- Min = [0.49958333 0.50875    0.47425    0.25333333 0.1025    ]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 72.25 | 7.75 |
| Actual Positive | 12.25 | 7.75 |

### robot-3
#### accuracy
- Mean = 0.74125
- Standard deviation = 0.03950870157319778
- Max = 0.79
- 75% = 0.7725
- Median = 0.745
- 25% = 0.7275
- Min = 0.67

#### f1
- Mean = 0.4043392348920684
- Standard deviation = 0.13553743819228165
- Max = 0.5818181818181818
- 75% = 0.5088028169014085
- Median = 0.423763386027537
- 25% = 0.3213682432432432
- Min = 0.13333333333333333

#### precision
- Mean = 0.3761839110644258
- Standard deviation = 0.08018707054879107
- Max = 0.47058823529411764
- 75% = 0.4267857142857143
- Median = 0.3893995098039216
- 25% = 0.3480392156862745
- Min = 0.2

#### recall
- Mean = 0.5
- Standard deviation = 0.2715695122800054
- Max = 0.95
- 75% = 0.6875
- Median = 0.47500000000000003
- 25% = 0.2875
- Min = 0.1

#### facing_probas
- Mean = [0.48382292 0.60880208 0.66770833 0.57007292 0.31195833]
- Standard deviation = [0.05970223 0.0806317  0.06738694 0.07232742 0.0970185 ]
- Max = [0.59875    0.69716667 0.81633333 0.66375    0.461     ]
- 75% = [0.511125   0.68285417 0.67402083 0.62133333 0.38872917]
- Median = [0.46420833 0.62266667 0.65070833 0.58820833 0.298875  ]
- 25% = [0.44089583 0.56039583 0.6295     0.51991667 0.2318125 ]
- Min = [0.415      0.45125    0.59166667 0.42958333 0.19125   ]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 64.125 | 15.875 |
| Actual Positive | 10.0 | 10.0 |

### robot-4
#### accuracy
- Mean = 0.76875
- Standard deviation = 0.0407546009672528
- Max = 0.81
- 75% = 0.8025
- Median = 0.78
- 25% = 0.74
- Min = 0.69

#### f1
- Mean = 0.41368634915799907
- Standard deviation = 0.11290587761564802
- Max = 0.5777777777777778
- 75% = 0.5091463414634148
- Median = 0.403954802259887
- 25% = 0.3082706766917293
- Min = 0.28571428571428575

#### precision
- Mean = 0.439670902014652
- Standard deviation = 0.07410310774412678
- Max = 0.5238095238095238
- 75% = 0.505
- Median = 0.453125
- 25% = 0.37099358974358976
- Min = 0.3333333333333333

#### recall
- Mean = 0.44375
- Standard deviation = 0.20068242947502904
- Max = 0.7
- 75% = 0.65
- Median = 0.42500000000000004
- 25% = 0.275
- Min = 0.2

#### facing_probas
- Mean = [0.29653125 0.49803125 0.63190625 0.65771875 0.54588542]
- Standard deviation = [0.06890454 0.09740481 0.05610219 0.05307262 0.08239023]
- Max = [0.40191667 0.58891667 0.73825    0.735      0.64208333]
- 75% = [0.34577083 0.5769375  0.64147917 0.70339583 0.61733333]
- Median = [0.27979167 0.52129167 0.61925    0.64925    0.5615    ]
- 25% = [0.244875   0.47875    0.60266667 0.62452083 0.480625  ]
- Min = [0.20983333 0.30333333 0.55541667 0.56458333 0.40416667]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 68.0 | 12.0 |
| Actual Positive | 11.125 | 8.875 |

### robot-5
#### accuracy
- Mean = 0.8362499999999999
- Standard deviation = 0.03425547401511179
- Max = 0.88
- 75% = 0.8725
- Median = 0.83
- 25% = 0.8075000000000001
- Min = 0.79

#### f1
- Mean = 0.37621800108932457
- Standard deviation = 0.22010403328257708
- Max = 0.6666666666666665
- 75% = 0.5506535947712418
- Median = 0.3854166666666667
- 25% = 0.22166666666666668
- Min = 0.0

#### precision
- Mean = 0.6523809523809524
- Standard deviation = 0.30110576636737224
- Max = 1.0
- 75% = 0.8392857142857143
- Median = 0.675
- 25% = 0.5625
- Min = 0.0

#### recall
- Mean = 0.2875
- Standard deviation = 0.1996089927833914
- Max = 0.6
- 75% = 0.4
- Median = 0.275
- 25% = 0.1375
- Min = 0.0

#### facing_probas
- Mean = [0.27544792 0.22705208 0.56827083 0.61173958 0.57489583]
- Standard deviation = [0.05729089 0.10251928 0.07976716 0.02565301 0.06340137]
- Max = [0.35291667 0.37225    0.722      0.64291667 0.66666667]
- 75% = [0.31791667 0.29664583 0.6125625  0.63827083 0.64079167]
- Median = [0.288875   0.22841667 0.54958333 0.61291667 0.54979167]
- 25% = [0.2396875  0.13472917 0.49954167 0.5910625  0.52335417]
- Min = [0.1775     0.09083333 0.47741667 0.57083333 0.505     ]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 77.875 | 2.125 |
| Actual Positive | 14.25 | 5.75 |

### robot-6
#### accuracy
- Mean = 0.47
- Standard deviation = 0.025495097567963924
- Max = 0.51
- 75% = 0.4825
- Median = 0.475
- 25% = 0.4575
- Min = 0.42

#### f1
- Mean = 0.6390429783007181
- Standard deviation = 0.02380691393412804
- Max = 0.6754966887417219
- 75% = 0.6509160166878287
- Median = 0.6440522154807868
- 25% = 0.6277751535191309
- Min = 0.5915492957746479

#### precision
- Mean = 1.0
- Standard deviation = 0.0
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 1.0
- Min = 1.0

#### recall
- Mean = 0.47
- Standard deviation = 0.025495097567963924
- Max = 0.51
- 75% = 0.4825
- Median = 0.475
- 25% = 0.4575
- Min = 0.42

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
| Actual Positive | 53.0 | 47.0 |

