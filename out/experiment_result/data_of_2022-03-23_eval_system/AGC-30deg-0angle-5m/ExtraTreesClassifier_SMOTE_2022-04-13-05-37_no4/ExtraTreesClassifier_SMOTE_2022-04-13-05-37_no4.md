# ExtraTreesClassifier_SMOTE_2022-04-13-05-37_no4
## Constants
- CSV_PATH = ../out/csv/experiment
- OUTPUT_PATH = ../out/experiment_result/data_of_2022-03-23_eval_system/AGC-30deg-0angle-5m
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
- AGC_STATUS = ['AGC-30deg']
- ANGLES = [30, 60, 90, 120, 150]

## Loaded CSV
- 2022-03-23_raspi_48000Hz_w1_N2^12_overlap80_all.csv

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
	- n_estimators = 250
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
	- oob_decision_function_ = [[0.33039648 0.66960352]
 [0.52586207 0.47413793]
 [0.37444934 0.62555066]
 [0.38888889 0.61111111]
 [0.38427948 0.61572052]
 [0.34199134 0.65800866]
 [0.56108597 0.43891403]
 [0.42666667 0.57333333]
 [0.6713615  0.3286385 ]
 [0.83333333 0.16666667]
 [0.78448276 0.21551724]
 [0.74782609 0.25217391]
 [0.77631579 0.22368421]
 [0.86936937 0.13063063]
 [0.89082969 0.10917031]
 [0.71244635 0.28755365]
 [0.76651982 0.23348018]
 [0.61471861 0.38528139]
 [0.4380531  0.5619469 ]
 [0.31896552 0.68103448]
 [0.34188034 0.65811966]
 [0.59825328 0.40174672]
 [0.27312775 0.72687225]
 [0.51111111 0.48888889]
 [0.57589286 0.42410714]
 [0.56578947 0.43421053]
 [0.38222222 0.61777778]
 [0.84482759 0.15517241]
 [0.75784753 0.24215247]
 [0.82882883 0.17117117]
 [0.72961373 0.27038627]
 [0.77682403 0.22317597]
 [0.79399142 0.20600858]
 [0.4025974  0.5974026 ]
 [0.3930131  0.6069869 ]
 [0.52401747 0.47598253]
 [0.40969163 0.59030837]
 [0.38626609 0.61373391]
 [0.46724891 0.53275109]
 [0.40611354 0.59388646]
 [0.36123348 0.63876652]
 [0.28       0.72      ]
 [0.6419214  0.3580786 ]
 [0.64732143 0.35267857]
 [0.45021645 0.54978355]
 [0.83856502 0.16143498]
 [0.79534884 0.20465116]
 [0.87234043 0.12765957]
 [0.66956522 0.33043478]
 [0.74778761 0.25221239]
 [0.77092511 0.22907489]
 [0.58974359 0.41025641]
 [0.43049327 0.56950673]
 [0.66964286 0.33035714]
 [0.31578947 0.68421053]
 [0.21681416 0.78318584]
 [0.35087719 0.64912281]
 [0.52678571 0.47321429]
 [0.45021645 0.54978355]
 [0.26315789 0.73684211]
 [0.84140969 0.15859031]
 [0.88340807 0.11659193]
 [0.83406114 0.16593886]
 [0.85281385 0.14718615]
 [0.82173913 0.17826087]
 [0.85652174 0.14347826]
 [0.62608696 0.37391304]
 [0.77092511 0.22907489]
 [0.82845188 0.17154812]
 [0.26406926 0.73593074]
 [0.52727273 0.47272727]
 [0.64383562 0.35616438]
 [0.33628319 0.66371681]
 [0.38655462 0.61344538]
 [0.29741379 0.70258621]
 [0.21459227 0.78540773]
 [0.36681223 0.63318777]
 [0.25217391 0.74782609]
 [0.28634361 0.71365639]
 [0.42672414 0.57327586]
 [0.29824561 0.70175439]
 [0.30222222 0.69777778]
 [0.27350427 0.72649573]
 [0.21212121 0.78787879]
 [0.34070796 0.65929204]
 [0.21702128 0.78297872]
 [0.30593607 0.69406393]
 [0.37053571 0.62946429]
 [0.20704846 0.79295154]
 [0.30630631 0.69369369]
 [0.23478261 0.76521739]
 [0.40528634 0.59471366]
 [0.42477876 0.57522124]
 [0.36486486 0.63513514]
 [0.28125    0.71875   ]
 [0.36480687 0.63519313]
 [0.3580786  0.6419214 ]
 [0.35555556 0.64444444]
 [0.34763948 0.65236052]
 [0.3125     0.6875    ]
 [0.42731278 0.57268722]
 [0.34468085 0.65531915]
 [0.31168831 0.68831169]
 [0.31555556 0.68444444]
 [0.31034483 0.68965517]
 [0.2246696  0.7753304 ]
 [0.19650655 0.80349345]
 [0.22566372 0.77433628]
 [0.26267281 0.73732719]
 [0.28699552 0.71300448]
 [0.53508772 0.46491228]
 [0.30666667 0.69333333]
 [0.3377193  0.6622807 ]
 [0.36363636 0.63636364]
 [0.35555556 0.64444444]
 [0.40639269 0.59360731]
 [0.36244541 0.63755459]
 [0.26363636 0.73636364]
 [0.37391304 0.62608696]
 [0.23913043 0.76086957]]
	- oob_score_ = 0.85

#### Importance of features
- hlbr = 0.07174135676492818
- high_power = 0.05674460884353742
- gp_max_val_max = 0.05039760959939531
- gp_max_val_mean = 0.04760302910052911
- gp_auc_max = 0.04495449735449736
- gp_max_val_min = 0.0413220918367347
- gp_auc_mean = 0.040080634920634926
- low_power = 0.03761599584278155
- srmr = 0.036223047367094974
- diff_auc = 0.03410022108843538
- diff_std = 0.032444642857142866
- ratio_max_to_9th_ave_peaks = 0.0317912358276644
- gp_max_val_range = 0.030786303854875286
- gp_auc_std = 0.030750381708238857
- gp_max_ix_range = 0.029430404383975817
- coe3[2] = 0.02731487528344671
- gp_max_val_std = 0.026457830687830686
- gp_max_ix_min = 0.02610318405139834
- ac_auc = 0.025820425170068034
- ac_std = 0.02560257180650038
- gp_auc_min = 0.024486632653061224
- coe1[1] = 0.023647645502645503
- gp_auc_range = 0.022827768959435626
- gp_max_ix_std = 0.022383223733938022
- tdoa_range = 0.020140119047619046
- coe3[3] = 0.01860395124716553
- tdoa_min = 0.018589697656840518
- ratio_max_to_10ms_ave_peaks = 0.018039814814814818
- tdoa_std = 0.015617509448223736
- tdoa_max = 0.015417157974300833
- gp_max_ix_mean = 0.01523677626606198
- gp_max_ix_max = 0.014099603174603174
- tdoa_mean = 0.012138450491307635
- coe1[0] = 0.011486700680272108
- coe3[0] = 0.0
- coe3[1] = 0.0

## Evaluation
cv = 8
### robot-1
#### accuracy
- Mean = 0.88625
- Standard deviation = 0.02642796813983249
- Max = 0.92
- 75% = 0.9025000000000001
- Median = 0.895
- 25% = 0.8725
- Min = 0.84

#### f1
- Mean = 0.7146455471052245
- Standard deviation = 0.04617694121853293
- Max = 0.8000000000000002
- 75% = 0.7291666666666667
- Median = 0.7161172161172161
- 25% = 0.6989247311827957
- Min = 0.6363636363636365

#### precision
- Mean = 0.7455617025518342
- Standard deviation = 0.12442283272592844
- Max = 1.0
- 75% = 0.8031250000000001
- Median = 0.743421052631579
- 25% = 0.6613636363636364
- Min = 0.5833333333333334

#### recall
- Mean = 0.70625
- Standard deviation = 0.07261843774138906
- Max = 0.8
- 75% = 0.75
- Median = 0.725
- 25% = 0.6875
- Min = 0.55

#### facing_probas
- Mean = [0.5613   0.266175 0.202875 0.127525 0.143225]
- Standard deviation = [0.03258589 0.04494502 0.0193649  0.0169257  0.03202693]
- Max = [0.6112 0.3394 0.2286 0.1538 0.1884]
- 75% = [0.57865 0.3037  0.21745 0.14105 0.16815]
- Median = [0.5733 0.2666 0.2038 0.1256 0.1478]
- 25% = [0.5411  0.2177  0.18965 0.11855 0.1064 ]
- Min = [0.4984 0.2132 0.1716 0.1    0.1052]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 74.5 | 5.5 |
| Actual Positive | 5.875 | 14.125 |

### robot-2
#### accuracy
- Mean = 0.855
- Standard deviation = 0.04301162633521313
- Max = 0.93
- 75% = 0.88
- Median = 0.86
- 25% = 0.8325
- Min = 0.78

#### f1
- Mean = 0.6477076884720128
- Standard deviation = 0.10941165665961038
- Max = 0.8205128205128205
- 75% = 0.7302371541501975
- Median = 0.6387814313346228
- 25% = 0.5859133126934983
- Min = 0.45

#### precision
- Mean = 0.6351916784482574
- Standard deviation = 0.11124302811048069
- Max = 0.8421052631578947
- 75% = 0.6785714285714286
- Median = 0.6394230769230769
- 25% = 0.587962962962963
- Min = 0.45

#### recall
- Mean = 0.6749999999999999
- Standard deviation = 0.1436140661634507
- Max = 0.85
- 75% = 0.8
- Median = 0.725
- 25% = 0.5375000000000001
- Min = 0.45

#### facing_probas
- Mean = [0.602575 0.64495  0.480425 0.248725 0.17175 ]
- Standard deviation = [0.05365225 0.03823581 0.0252989  0.01680653 0.02334904]
- Max = [0.67   0.7074 0.5126 0.273  0.2012]
- 75% = [0.6449  0.67805 0.4935  0.26255 0.1936 ]
- Median = [0.6067 0.6199 0.4891 0.2504 0.1771]
- 25% = [0.5767  0.61755 0.4738  0.23455 0.1468 ]
- Min = [0.4928 0.608  0.4234 0.2204 0.1374]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 72.0 | 8.0 |
| Actual Positive | 6.5 | 13.5 |

### robot-3
#### accuracy
- Mean = 0.8162499999999999
- Standard deviation = 0.03314268395890711
- Max = 0.88
- 75% = 0.835
- Median = 0.8049999999999999
- 25% = 0.79
- Min = 0.78

#### f1
- Mean = 0.39031251489775143
- Standard deviation = 0.17344571550502424
- Max = 0.5714285714285715
- 75% = 0.5019342359767892
- Median = 0.4413793103448276
- 25% = 0.3188585607940446
- Min = 0.0

#### precision
- Mean = 0.5578153328153328
- Standard deviation = 0.2727249396703855
- Max = 1.0
- 75% = 0.6944444444444444
- Median = 0.5484330484330484
- 25% = 0.4636363636363636
- Min = 0.0

#### recall
- Mean = 0.325
- Standard deviation = 0.17500000000000002
- Max = 0.65
- 75% = 0.4
- Median = 0.35
- 25% = 0.2375
- Min = 0.0

#### facing_probas
- Mean = [0.363925 0.55525  0.55895  0.451175 0.222175]
- Standard deviation = [0.04010498 0.02471047 0.01491736 0.0361301  0.03066504]
- Max = [0.4304 0.6014 0.5764 0.521  0.2848]
- 75% = [0.38015 0.5691  0.57215 0.46985 0.23165]
- Median = [0.3632 0.5521 0.5616 0.4542 0.2271]
- 25% = [0.34855 0.5375  0.54585 0.42545 0.199  ]
- Min = [0.291  0.5252 0.5352 0.4012 0.1802]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 75.125 | 4.875 |
| Actual Positive | 13.5 | 6.5 |

### robot-4
#### accuracy
- Mean = 0.845
- Standard deviation = 0.0229128784747792
- Max = 0.88
- 75% = 0.8625
- Median = 0.845
- 25% = 0.8274999999999999
- Min = 0.81

#### f1
- Mean = 0.5739173424899313
- Standard deviation = 0.08076341693421107
- Max = 0.6666666666666665
- 75% = 0.6277310924369748
- Median = 0.5880398671096345
- 25% = 0.5582386363636365
- Min = 0.3846153846153846

#### precision
- Mean = 0.6732219159989146
- Standard deviation = 0.10843818292591342
- Max = 0.8333333333333334
- 75% = 0.75
- Median = 0.7128205128205127
- 25% = 0.5602766798418972
- Min = 0.5161290322580645

#### recall
- Mean = 0.5437500000000001
- Standard deviation = 0.1529654781315052
- Max = 0.8
- 75% = 0.6125
- Median = 0.575
- 25% = 0.45
- Min = 0.25

#### facing_probas
- Mean = [0.1905   0.36285  0.54755  0.5999   0.430925]
- Standard deviation = [0.02729963 0.02722458 0.02763345 0.04283375 0.02366663]
- Max = [0.2372 0.4164 0.6074 0.653  0.4734]
- 75% = [0.21265 0.3689  0.5543  0.6389  0.44445]
- Median = [0.1866 0.3564 0.5439 0.6083 0.4301]
- 25% = [0.16275 0.34595 0.53285 0.55395 0.41365]
- Min = [0.1592 0.329  0.507  0.5438 0.395 ]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 73.625 | 6.375 |
| Actual Positive | 9.125 | 10.875 |

### robot-5
#### accuracy
- Mean = 0.9375
- Standard deviation = 0.029047375096555604
- Max = 0.97
- 75% = 0.9624999999999999
- Median = 0.945
- 25% = 0.915
- Min = 0.89

#### f1
- Mean = 0.8190103022242734
- Standard deviation = 0.09842342387438148
- Max = 0.9230769230769231
- 75% = 0.8963963963963965
- Median = 0.8600770218228497
- 25% = 0.738970588235294
- Min = 0.6451612903225806

#### precision
- Mean = 0.932454241664768
- Standard deviation = 0.058839947848714824
- Max = 1.0
- 75% = 1.0
- Median = 0.9282296650717703
- 25% = 0.8809523809523809
- Min = 0.8571428571428571

#### recall
- Mean = 0.74375
- Standard deviation = 0.14456291882775474
- Max = 0.9
- 75% = 0.8625
- Median = 0.8
- 25% = 0.6
- Min = 0.5

#### facing_probas
- Mean = [0.128375 0.212175 0.47955  0.64665  0.69905 ]
- Standard deviation = [0.01366398 0.02864724 0.02096038 0.04314276 0.04092258]
- Max = [0.1486 0.2514 0.5178 0.7032 0.7692]
- 75% = [0.1416  0.24335 0.4877  0.67465 0.72995]
- Median = [0.1242 0.2048 0.4718 0.6578 0.6864]
- 25% = [0.1163  0.1911  0.46335 0.60675 0.67175]
- Min = [0.1116 0.173  0.4596 0.5844 0.6484]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 78.875 | 1.125 |
| Actual Positive | 5.125 | 14.875 |

### robot-6
#### accuracy
- Mean = 0.59875
- Standard deviation = 0.04013648589500581
- Max = 0.66
- 75% = 0.6174999999999999
- Median = 0.6
- 25% = 0.585
- Min = 0.52

#### f1
- Mean = 0.7482247979546551
- Standard deviation = 0.03179726260514782
- Max = 0.7951807228915663
- 75% = 0.7634449325859718
- Median = 0.7499511699675769
- 25% = 0.7381324360052879
- Min = 0.6842105263157895

#### precision
- Mean = 1.0
- Standard deviation = 0.0
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 1.0
- Min = 1.0

#### recall
- Mean = 0.59875
- Standard deviation = 0.04013648589500581
- Max = 0.66
- 75% = 0.6174999999999999
- Median = 0.6
- 25% = 0.585
- Min = 0.52

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
| Actual Positive | 40.125 | 59.875 |

