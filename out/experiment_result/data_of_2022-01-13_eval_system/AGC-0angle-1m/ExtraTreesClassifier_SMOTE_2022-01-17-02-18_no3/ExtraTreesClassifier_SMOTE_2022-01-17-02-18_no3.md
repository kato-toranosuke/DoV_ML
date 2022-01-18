# ExtraTreesClassifier_SMOTE_2022-01-17-02-18_no3
## Constants
- CSV_PATH = ../out/csv/experiment
- OUTPUT_PATH = ../out/experiment_result/data_of_2022-01-13_eval_system/AGC-0angle-1m
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
	- sampling_strategy_ = OrderedDict([(1, 45)])
	- nn_k_ = NearestNeighbors(n_neighbors=6)

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
- gp_max_val_min = 0.2440078770809112
- gp_auc_mean = 0.1119974691274689
- gp_auc_min = 0.101623204002097
- gp_max_ix_mean = 0.09868653599999172
- gp_auc_max = 0.09626368531460573
- gp_max_val_mean = 0.09140046781101606
- srmr = 0.055991469961933625
- gp_max_val_max = 0.05375815544803962
- gp_max_ix_range = 0.03308128544423441
- gp_max_val_range = 0.030417130499674854
- gp_max_ix_max = 0.0199778437165846
- gp_max_val_std = 0.0175144993185438
- ac_auc = 0.011560349875567267
- ac_std = 0.00768535958604368
- tdoa_max = 0.006474635567294894
- diff_std = 0.004688200934579441
- coe3[3] = 0.003811366918017008
- gp_auc_range = 0.002917030663624741
- tdoa_min = 0.0018952819785759234
- coe1[1] = 0.0016617883108299492
- gp_auc_std = 0.0009323413159730321
- hlbr = 0.0009007386759602403
- tdoa_mean = 0.0008865248226950358
- ratio_max_to_9th_ave_peaks = 0.0005583083257729046
- diff_auc = 0.0004254241580146883
- high_power = 0.0003495824431928543
- tdoa_std = 0.0002765257027095477
- gp_max_ix_std = 0.0002569169960474318
- low_power = 0.0
- coe1[0] = 0.0
- coe3[0] = 0.0
- coe3[1] = 0.0
- coe3[2] = 0.0
- ratio_max_to_10ms_ave_peaks = 0.0
- gp_max_ix_min = 0.0
- tdoa_range = 0.0

## Evaluation
cv = 8
### robot-1
#### accuracy
- Mean = 0.9282449494949495
- Standard deviation = 0.026632110372204032
- Max = 0.96
- 75% = 0.9419191919191919
- Median = 0.9393939393939394
- 25% = 0.9166666666666667
- Min = 0.87

#### f1
- Mean = 0.8441637073872321
- Standard deviation = 0.045452531699216314
- Max = 0.9
- 75% = 0.8701226309921963
- Median = 0.866600790513834
- 25% = 0.8226744186046511
- Min = 0.7547169811320755

#### precision
- Mean = 0.7730427252952996
- Standard deviation = 0.08929514181325099
- Max = 0.9
- 75% = 0.8174342105263157
- Median = 0.7692307692307693
- 25% = 0.732919254658385
- Min = 0.6060606060606061

#### recall
- Mean = 0.9437500000000001
- Standard deviation = 0.06343057228182639
- Max = 1.0
- 75% = 1.0
- Median = 0.975
- 25% = 0.8875
- Min = 0.85

#### facing_probas
- Mean = [8.86506944e-01 1.15521848e-01 4.53273810e-03 0.00000000e+00
 8.03571429e-04]
- Standard deviation = [0.04171772 0.02858805 0.00554568 0.         0.00212605]
- Max = [0.95969246 0.1753373  0.0165     0.         0.00642857]
- 75% = [0.90387252 0.12336062 0.00625    0.         0.        ]
- Median = [0.89177083 0.11435813 0.00238095 0.         0.        ]
- 25% = [0.8680506  0.10389051 0.         0.         0.        ]
- Min = [0.80302976 0.06795833 0.         0.         0.        ]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 73.25 | 6.0 |
| Actual Positive | 1.125 | 18.875 |

### robot-2
#### accuracy
- Mean = 0.8891666666666667
- Standard deviation = 0.02566828204203567
- Max = 0.92
- 75% = 0.9116161616161615
- Median = 0.8888888888888888
- 25% = 0.8665151515151516
- Min = 0.8585858585858586

#### f1
- Mean = 0.6313524635986685
- Standard deviation = 0.11011672041615893
- Max = 0.7647058823529412
- 75% = 0.7329545454545455
- Median = 0.6451612903225807
- 25% = 0.5138888888888888
- Min = 0.4999999999999999

#### precision
- Mean = 0.9274787712287713
- Standard deviation = 0.0644713335904012
- Max = 1.0
- 75% = 1.0
- Median = 0.9258241758241759
- 25% = 0.875
- Min = 0.8181818181818182

#### recall
- Mean = 0.4875
- Standard deviation = 0.11924240017711822
- Max = 0.65
- 75% = 0.6
- Median = 0.5
- 25% = 0.35
- Min = 0.35

#### facing_probas
- Mean = [0.57071456 0.68507506 0.49133405 0.0019375  0.00233333]
- Standard deviation = [0.12774088 0.09162933 0.08479151 0.00337674 0.00476476]
- Max = [0.76733929 0.81740801 0.652125   0.01       0.01438095]
- 75% = [0.6531062  0.74708532 0.53748462 0.001875   0.00107143]
- Median = [0.55470536 0.67701488 0.49537491 0.         0.        ]
- 25% = [0.49512302 0.64974107 0.42577282 0.         0.        ]
- Min = [0.35350992 0.5062381  0.37168452 0.         0.        ]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 78.5 | 0.75 |
| Actual Positive | 10.25 | 9.75 |

### robot-3
#### accuracy
- Mean = 0.943320707070707
- Standard deviation = 0.018173780315050018
- Max = 0.9595959595959596
- 75% = 0.9523989898989899
- Median = 0.9494949494949495
- 25% = 0.9398484848484848
- Min = 0.898989898989899

#### f1
- Mean = 0.8525406985933301
- Standard deviation = 0.042111917876630496
- Max = 0.8947368421052632
- 75% = 0.8708708708708708
- Median = 0.8648648648648648
- 25% = 0.8480263157894736
- Min = 0.75

#### precision
- Mean = 0.9071078431372549
- Standard deviation = 0.07226781713693482
- Max = 1.0
- 75% = 0.9419934640522876
- Median = 0.9411764705882353
- 25% = 0.8791666666666667
- Min = 0.75

#### recall
- Mean = 0.80625
- Standard deviation = 0.029973947020704484
- Max = 0.85
- 75% = 0.8125
- Median = 0.8
- 25% = 0.8
- Min = 0.75

#### facing_probas
- Mean = [0.03978646 0.26086954 0.78125548 0.1320811  0.00099107]
- Standard deviation = [0.02698606 0.14772468 0.05762827 0.06783437 0.00143322]
- Max = [0.10078571 0.50474603 0.87331962 0.24343254 0.004     ]
- 75% = [0.04744345 0.38849058 0.81787946 0.18847421 0.00169643]
- Median = [0.03300496 0.23070238 0.77055456 0.12421329 0.        ]
- 25% = [0.02053472 0.13474603 0.7455248  0.0764881  0.        ]
- Min = [0.012      0.08708929 0.68623214 0.04333333 0.        ]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 77.5 | 1.75 |
| Actual Positive | 3.875 | 16.125 |

### robot-4
#### accuracy
- Mean = 0.931969696969697
- Standard deviation = 0.030647370194967133
- Max = 0.9696969696969697
- 75% = 0.9496212121212121
- Median = 0.9444444444444444
- 25% = 0.9222474747474748
- Min = 0.8686868686868687

#### f1
- Mean = 0.8188079011948226
- Standard deviation = 0.07604721221795756
- Max = 0.9142857142857143
- 75% = 0.873358348968105
- Median = 0.8360071301247771
- 25% = 0.7923186344238975
- Min = 0.6666666666666667

#### precision
- Mean = 0.8637089046144774
- Standard deviation = 0.1142056337658192
- Max = 1.0
- 75% = 0.95
- Median = 0.8697478991596639
- 25% = 0.8217105263157894
- Min = 0.65

#### recall
- Mean = 0.7851973684210526
- Standard deviation = 0.07654160669467074
- Max = 0.9
- 75% = 0.8552631578947368
- Median = 0.743421052631579
- 25% = 0.7368421052631579
- Min = 0.6842105263157895

#### facing_probas
- Mean = [0.         0.         0.09264985 0.69061054 0.09240558]
- Standard deviation = [0.         0.         0.10224447 0.04803756 0.06563613]
- Max = [0.         0.         0.26426274 0.74586884 0.19688919]
- 75% = [0.         0.         0.19710683 0.73408735 0.11939902]
- Median = [0.         0.         0.02838012 0.7037384  0.08496429]
- 25% = [0.         0.         0.01062719 0.65140925 0.03327903]
- Min = [0.         0.         0.         0.60590852 0.01685673]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 77.375 | 2.625 |
| Actual Positive | 4.125 | 15.125 |

### robot-5
#### accuracy
- Mean = 0.9559090909090909
- Standard deviation = 0.021996500542558216
- Max = 0.98989898989899
- 75% = 0.9624242424242424
- Median = 0.9597979797979798
- 25% = 0.9545454545454546
- Min = 0.9090909090909091

#### f1
- Mean = 0.8727550349941242
- Standard deviation = 0.07289816556710094
- Max = 0.9743589743589743
- 75% = 0.8963963963963965
- Median = 0.888888888888889
- 25% = 0.8725490196078431
- Min = 0.7096774193548387

#### precision
- Mean = 1.0
- Standard deviation = 0.0
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 1.0
- Min = 1.0

#### recall
- Mean = 0.78125
- Standard deviation = 0.10879309490955755
- Max = 0.95
- 75% = 0.8125
- Median = 0.8
- 25% = 0.775
- Min = 0.55

#### facing_probas
- Mean = [0.0035     0.         0.02317312 0.43936742 0.7426307 ]
- Standard deviation = [0.00714714 0.         0.0185413  0.06938309 0.07016122]
- Max = [0.02157143 0.         0.06479762 0.52061706 0.83633135]
- 75% = [0.00160714 0.         0.03165079 0.50645161 0.82154812]
- Median = [0.         0.         0.01672222 0.4471121  0.72320734]
- 25% = [0.         0.         0.01189286 0.3862004  0.68286062]
- Min = [0.         0.         0.00166667 0.33574405 0.65122421]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 79.25 | 0.0 |
| Actual Positive | 4.375 | 15.625 |

### robot-6
#### accuracy
- Mean = 0.760669191919192
- Standard deviation = 0.050339499819397664
- Max = 0.8181818181818182
- 75% = 0.8030303030303031
- Median = 0.775
- 25% = 0.7146464646464646
- Min = 0.6767676767676768

#### f1
- Mean = 0.8631283551461226
- Standard deviation = 0.032881454792039196
- Max = 0.9
- 75% = 0.8907303370786517
- Median = 0.8732304957785819
- 25% = 0.8335711799512704
- Min = 0.8072289156626505

#### precision
- Mean = 1.0
- Standard deviation = 0.0
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 1.0
- Min = 1.0

#### recall
- Mean = 0.760669191919192
- Standard deviation = 0.050339499819397664
- Max = 0.8181818181818182
- 75% = 0.8030303030303031
- Median = 0.775
- 25% = 0.7146464646464646
- Min = 0.6767676767676768

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
| Actual Positive | 23.75 | 75.5 |

