# ExtraTreesClassifier_RandomOverSampler_2022-04-15-03-29_no3
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
	- n_estimators = 30
	- estimator_params = ('criterion', 'max_depth', 'min_samples_split', 'min_samples_leaf', 'min_weight_fraction_leaf', 'max_features', 'max_leaf_nodes', 'min_impurity_decrease', 'random_state', 'ccp_alpha')
	- bootstrap = True
	- oob_score = True
	- n_jobs = -1
	- random_state = 42
	- verbose = 0
	- warm_start = False
	- class_weight = None
	- max_samples = 0.5
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
	- oob_decision_function_ = [[0.23529412 0.76470588]
 [0.38888889 0.61111111]
 [0.4        0.6       ]
 [0.53333333 0.46666667]
 [0.73684211 0.26315789]
 [0.57894737 0.42105263]
 [0.65       0.35      ]
 [0.73684211 0.26315789]
 [0.44444444 0.55555556]
 [0.70588235 0.29411765]
 [0.33333333 0.66666667]
 [0.72222222 0.27777778]
 [0.85714286 0.14285714]
 [0.82352941 0.17647059]
 [0.61904762 0.38095238]
 [0.86363636 0.13636364]
 [0.94444444 0.05555556]
 [0.63636364 0.36363636]
 [0.05882353 0.94117647]
 [0.04761905 0.95238095]
 [0.04166667 0.95833333]
 [0.61904762 0.38095238]
 [0.36842105 0.63157895]
 [0.84210526 0.15789474]
 [0.66666667 0.33333333]
 [0.57894737 0.42105263]
 [0.94117647 0.05882353]
 [0.59090909 0.40909091]
 [0.69230769 0.30769231]
 [0.5        0.5       ]
 [0.86363636 0.13636364]
 [0.6875     0.3125    ]
 [0.66666667 0.33333333]
 [0.27777778 0.72222222]
 [0.68181818 0.31818182]
 [0.5        0.5       ]
 [0.125      0.875     ]
 [0.         1.        ]
 [0.5        0.5       ]
 [0.45       0.55      ]
 [0.25       0.75      ]
 [0.71428571 0.28571429]
 [0.58823529 0.41176471]
 [0.52631579 0.47368421]
 [0.45454545 0.54545455]
 [0.78947368 0.21052632]
 [0.75       0.25      ]
 [0.89473684 0.10526316]
 [0.66666667 0.33333333]
 [0.29411765 0.70588235]
 [0.7826087  0.2173913 ]
 [0.82352941 0.17647059]
 [0.83333333 0.16666667]
 [0.80952381 0.19047619]
 [0.27777778 0.72222222]
 [0.05263158 0.94736842]
 [0.         1.        ]
 [0.73333333 0.26666667]
 [0.33333333 0.66666667]
 [0.52941176 0.47058824]
 [0.92307692 0.07692308]
 [0.73333333 0.26666667]
 [0.95       0.05      ]
 [0.68421053 0.31578947]
 [0.82352941 0.17647059]
 [0.8        0.2       ]
 [0.84210526 0.15789474]
 [0.63636364 0.36363636]
 [0.77777778 0.22222222]
 [0.72222222 0.27777778]
 [0.5        0.5       ]
 [0.6875     0.3125    ]
 [0.27777778 0.72222222]
 [0.23529412 0.76470588]
 [0.05555556 0.94444444]
 [0.0952381  0.9047619 ]
 [0.0625     0.9375    ]
 [0.33333333 0.66666667]
 [0.04545455 0.95454545]
 [0.05       0.95      ]
 [0.         1.        ]
 [0.27777778 0.72222222]
 [0.05263158 0.94736842]
 [0.11764706 0.88235294]
 [0.33333333 0.66666667]
 [0.3        0.7       ]
 [0.11111111 0.88888889]
 [0.06666667 0.93333333]
 [0.05882353 0.94117647]
 [0.         1.        ]
 [0.05263158 0.94736842]
 [0.05882353 0.94117647]
 [0.         1.        ]
 [0.         1.        ]
 [0.28571429 0.71428571]
 [0.08333333 0.91666667]
 [0.04761905 0.95238095]
 [0.38888889 0.61111111]
 [0.         1.        ]
 [0.         1.        ]
 [0.25       0.75      ]
 [0.05       0.95      ]
 [0.4375     0.5625    ]
 [0.         1.        ]
 [0.05555556 0.94444444]
 [0.21052632 0.78947368]
 [0.         1.        ]
 [0.3125     0.6875    ]
 [0.04347826 0.95652174]
 [0.3125     0.6875    ]
 [0.         1.        ]
 [0.5        0.5       ]
 [0.19047619 0.80952381]
 [0.05882353 0.94117647]
 [0.07142857 0.92857143]
 [0.06666667 0.93333333]
 [0.27777778 0.72222222]
 [0.         1.        ]
 [0.         1.        ]
 [0.05       0.95      ]]
	- oob_score_ = 0.9083333333333333

#### Importance of features
- ratio_max_to_10ms_ave_peaks = 0.05827805557556576
- gp_max_val_max = 0.05461200961003239
- gp_auc_min = 0.05024641381892005
- gp_max_val_min = 0.050081784350938977
- gp_auc_mean = 0.048449991819250825
- srmr = 0.04783541315910108
- gp_auc_max = 0.045030326201484915
- gp_auc_std = 0.03735475322710595
- gp_max_val_mean = 0.03681474907471763
- ratio_max_to_9th_ave_peaks = 0.03633866230165577
- ac_auc = 0.036022350769421646
- hlbr = 0.03549478236487086
- diff_auc = 0.03298928978303273
- coe3[3] = 0.030641093558205726
- gp_auc_range = 0.030354510473358187
- gp_max_ix_std = 0.02991824679221016
- ac_std = 0.028093538717661088
- diff_std = 0.02804490640945932
- tdoa_std = 0.026331870162044604
- coe3[2] = 0.024701834803806746
- high_power = 0.024304153799418762
- coe1[1] = 0.023920404486620014
- tdoa_mean = 0.021608158524077704
- low_power = 0.020648281903053883
- tdoa_max = 0.01984846466298285
- gp_max_val_std = 0.019819673700875496
- coe1[0] = 0.019657603327330315
- tdoa_range = 0.016887380410385497
- gp_max_ix_range = 0.01547920197793852
- gp_max_ix_mean = 0.015252264906863452
- gp_max_ix_max = 0.012055047566318165
- gp_max_val_range = 0.009894668458509594
- tdoa_min = 0.009818326979142419
- gp_max_ix_min = 0.0031717863236390767
- coe3[0] = 0.0
- coe3[1] = 0.0

## Evaluation
cv = 8
### robot-1
#### accuracy
- Mean = 0.79125
- Standard deviation = 0.013635890143294655
- Max = 0.81
- 75% = 0.8025
- Median = 0.79
- 25% = 0.78
- Min = 0.77

#### f1
- Mean = 0.07302536231884059
- Standard deviation = 0.08637852704441382
- Max = 0.24
- 75% = 0.10869565217391305
- Median = 0.04166666666666667
- 25% = 0.0
- Min = 0.0

#### precision
- Mean = 0.23125
- Standard deviation = 0.2622601417380164
- Max = 0.6666666666666666
- 75% = 0.39999999999999997
- Median = 0.125
- 25% = 0.0
- Min = 0.0

#### recall
- Mean = 0.043750000000000004
- Standard deviation = 0.05266343608235224
- Max = 0.15
- 75% = 0.0625
- Median = 0.025
- 25% = 0.0
- Min = 0.0

#### facing_probas
- Mean = [0.2875     0.29604167 0.24604167 0.20208333 0.150625  ]
- Standard deviation = [0.034339   0.04531477 0.07397887 0.07354491 0.05511313]
- Max = [0.33       0.345      0.39666667 0.365      0.24666667]
- 75% = [0.31791667 0.33208333 0.26333333 0.23291667 0.17666667]
- Median = [0.29166667 0.30916667 0.22916667 0.17666667 0.13916667]
- 25% = [0.26541667 0.27333333 0.20625    0.16041667 0.10916667]
- Min = [0.22333333 0.20333333 0.15166667 0.11166667 0.08333333]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 78.25 | 1.75 |
| Actual Positive | 19.125 | 0.875 |

### robot-2
#### accuracy
- Mean = 0.8174999999999999
- Standard deviation = 0.0635904867098845
- Max = 0.89
- 75% = 0.865
- Median = 0.83
- 25% = 0.7875000000000001
- Min = 0.68

#### f1
- Mean = 0.5648003135154703
- Standard deviation = 0.16250099595594522
- Max = 0.7272727272727272
- 75% = 0.6756756756756757
- Median = 0.6192135390741662
- 25% = 0.5125
- Min = 0.20000000000000004

#### precision
- Mean = 0.5401111118428562
- Standard deviation = 0.1597843234516512
- Max = 0.7647058823529411
- 75% = 0.6439393939393939
- Median = 0.5615763546798029
- 25% = 0.4725
- Min = 0.2

#### recall
- Mean = 0.6000000000000001
- Standard deviation = 0.18540496217739158
- Max = 0.8
- 75% = 0.725
- Median = 0.625
- 25% = 0.5625
- Min = 0.2

#### facing_probas
- Mean = [0.30666667 0.61875    0.49916667 0.426875   0.37083333]
- Standard deviation = [0.08210765 0.0674627  0.05002083 0.049857   0.09468515]
- Max = [0.44       0.685      0.59666667 0.49333333 0.55333333]
- 75% = [0.37166667 0.67708333 0.52666667 0.47708333 0.43958333]
- Median = [0.30833333 0.64083333 0.48666667 0.41833333 0.33083333]
- 25% = [0.25125    0.58       0.45583333 0.37833333 0.3125    ]
- Min = [0.18166667 0.48166667 0.44333333 0.37       0.24      ]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 69.75 | 10.25 |
| Actual Positive | 8.0 | 12.0 |

### robot-3
#### accuracy
- Mean = 0.765
- Standard deviation = 0.033541019662496854
- Max = 0.82
- 75% = 0.79
- Median = 0.765
- 25% = 0.7424999999999999
- Min = 0.72

#### f1
- Mean = 0.21174560359342967
- Standard deviation = 0.1261777522765885
- Max = 0.3636363636363636
- 75% = 0.30608108108108106
- Median = 0.26785714285714285
- 25% = 0.08605072463768117
- Min = 0.0

#### precision
- Mean = 0.3316176470588235
- Standard deviation = 0.19142188245310823
- Max = 0.75
- 75% = 0.3382352941176471
- Median = 0.3333333333333333
- 25% = 0.2875
- Min = 0.0

#### recall
- Mean = 0.1875
- Standard deviation = 0.13635890143294643
- Max = 0.4
- 75% = 0.3
- Median = 0.2
- 25% = 0.05
- Min = 0.0

#### facing_probas
- Mean = [0.28916667 0.44791667 0.456875   0.38229167 0.37645833]
- Standard deviation = [0.0523543  0.04244891 0.05869198 0.03507866 0.06154514]
- Max = [0.35       0.50333333 0.545      0.43166667 0.50166667]
- 75% = [0.32041667 0.48416667 0.49791667 0.40166667 0.39791667]
- Median = [0.30416667 0.44833333 0.45583333 0.39333333 0.38083333]
- 25% = [0.27208333 0.42333333 0.40041667 0.3625     0.345     ]
- Min = [0.175      0.38333333 0.38833333 0.31333333 0.28      ]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 72.75 | 7.25 |
| Actual Positive | 16.25 | 3.75 |

### robot-4
#### accuracy
- Mean = 0.78125
- Standard deviation = 0.038870779513665535
- Max = 0.83
- 75% = 0.8075
- Median = 0.785
- 25% = 0.7625
- Min = 0.71

#### f1
- Mean = 0.3859666929378883
- Standard deviation = 0.12896489849447904
- Max = 0.5238095238095238
- 75% = 0.47835497835497837
- Median = 0.40998838559814166
- 25% = 0.35917312661498707
- Min = 0.08695652173913045

#### precision
- Mean = 0.4642630919804833
- Standard deviation = 0.13268181527239742
- Max = 0.7142857142857143
- 75% = 0.5288461538461539
- Median = 0.44155844155844154
- 25% = 0.3560606060606061
- Min = 0.30434782608695654

#### recall
- Mean = 0.36875
- Standard deviation = 0.1477698802192111
- Max = 0.55
- 75% = 0.4625
- Median = 0.4
- 25% = 0.32499999999999996
- Min = 0.05

#### facing_probas
- Mean = [0.27458333 0.406875   0.435      0.50916667 0.38083333]
- Standard deviation = [0.03782957 0.0491203  0.03912232 0.04168333 0.06578585]
- Max = [0.32       0.49666667 0.50833333 0.58666667 0.53833333]
- 75% = [0.30041667 0.44       0.4575     0.525      0.3875    ]
- Median = [0.28166667 0.39333333 0.42083333 0.50416667 0.36416667]
- 25% = [0.26166667 0.37       0.40958333 0.48583333 0.35291667]
- Min = [0.19166667 0.345      0.385      0.44833333 0.295     ]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 70.75 | 9.25 |
| Actual Positive | 12.625 | 7.375 |

### robot-5
#### accuracy
- Mean = 0.7775
- Standard deviation = 0.046569840025492894
- Max = 0.82
- 75% = 0.8025
- Median = 0.8
- 25% = 0.7725
- Min = 0.68

#### f1
- Mean = 0.17013333385615995
- Standard deviation = 0.11163429410314755
- Max = 0.35714285714285715
- 75% = 0.2526455026455027
- Median = 0.14583333333333334
- 25% = 0.0899209486166008
- Min = 0.0

#### precision
- Mean = 0.36546266233766234
- Standard deviation = 0.20591070066667028
- Max = 0.625
- 75% = 0.5178571428571428
- Median = 0.41666666666666663
- 25% = 0.2121212121212121
- Min = 0.0

#### recall
- Mean = 0.125
- Standard deviation = 0.09013878188659974
- Max = 0.25
- 75% = 0.21250000000000002
- Median = 0.1
- 25% = 0.05
- Min = 0.0

#### facing_probas
- Mean = [0.21208333 0.374375   0.31833333 0.43958333 0.395625  ]
- Standard deviation = [0.05640719 0.05944732 0.04606758 0.04758581 0.06699366]
- Max = [0.315      0.48666667 0.38333333 0.495      0.53833333]
- 75% = [0.24208333 0.39583333 0.36416667 0.48333333 0.42875   ]
- Median = [0.20416667 0.36083333 0.30833333 0.44583333 0.37166667]
- 25% = [0.17208333 0.33625    0.28666667 0.39875    0.34416667]
- Min = [0.13333333 0.30166667 0.25666667 0.375      0.32833333]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 75.25 | 4.75 |
| Actual Positive | 17.5 | 2.5 |

### robot-6
#### accuracy
- Mean = 0.265
- Standard deviation = 0.049749371855331
- Max = 0.33
- 75% = 0.28750000000000003
- Median = 0.275
- 25% = 0.2575
- Min = 0.16

#### f1
- Mean = 0.41642931896371105
- Standard deviation = 0.06472407691175786
- Max = 0.49624060150375937
- 75% = 0.44644561068702293
- Median = 0.43134842519685046
- 25% = 0.40906157222150513
- Min = 0.2758620689655173

#### precision
- Mean = 1.0
- Standard deviation = 0.0
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 1.0
- Min = 1.0

#### recall
- Mean = 0.265
- Standard deviation = 0.049749371855331
- Max = 0.33
- 75% = 0.28750000000000003
- Median = 0.275
- 25% = 0.2575
- Min = 0.16

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
| Actual Positive | 73.5 | 26.5 |

