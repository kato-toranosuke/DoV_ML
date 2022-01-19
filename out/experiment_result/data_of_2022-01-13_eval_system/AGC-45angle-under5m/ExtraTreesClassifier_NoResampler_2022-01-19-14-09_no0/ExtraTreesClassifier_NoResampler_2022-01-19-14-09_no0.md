# ExtraTreesClassifier_NoResampler_2022-01-19-14-09_no0
## Constants
- CSV_PATH = ../out/csv/experiment
- OUTPUT_PATH = ../out/experiment_result/data_of_2022-01-13_eval_system/AGC-45angle-under5m
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
- DISTANCE = [1, 3, 5]
- AGC_STATUS = ['AGC']

## Loaded CSV
- 2021-12-27_AGC.csv
- 2022-01-10_NoAGC.csv
- 2022-01-13_raspi_48000Hz_w1_N2^12_overlap80.csv

## Estimator
### Type
- resampler = NoResampler
- estimator = ExtraTreesClassifier

### Arguments for hyperparameter search
- resampler = NoResampler
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

- best_estimator
	- base_estimator = ExtraTreeClassifier()
	- n_estimators = 150
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
- gp_max_val_mean = 0.09984464371134169
- gp_max_val_min = 0.09519290061335017
- gp_auc_max = 0.07950313522410674
- gp_auc_min = 0.07700849498572068
- gp_auc_mean = 0.06329318620744852
- gp_max_val_max = 0.06270005089336907
- diff_auc = 0.055524930715030826
- high_power = 0.04841700083138243
- diff_std = 0.04714561507052779
- srmr = 0.03265272792721321
- coe1[1] = 0.02674233040241881
- hlbr = 0.024883222703745378
- tdoa_mean = 0.020660260148949058
- coe1[0] = 0.020347392632332952
- tdoa_min = 0.02032228718347111
- gp_max_ix_min = 0.019391553729592434
- gp_max_ix_mean = 0.01937747023217449
- gp_max_ix_std = 0.016036834624013903
- tdoa_std = 0.013704669606062423
- gp_max_val_range = 0.01365355062213841
- gp_max_val_std = 0.013490951011028308
- ratio_max_to_10ms_ave_peaks = 0.013017908962931332
- low_power = 0.012644690469639433
- gp_max_ix_range = 0.012427623530965657
- gp_auc_std = 0.012243081721845624
- tdoa_range = 0.011541607507651878
- coe3[3] = 0.011367873846443515
- gp_auc_range = 0.011308335920279024
- ac_auc = 0.01092175732213368
- ac_std = 0.007978414883009627
- gp_max_ix_max = 0.007295560616000776
- tdoa_max = 0.0072400787722089145
- coe3[2] = 0.006499679555301262
- ratio_max_to_9th_ave_peaks = 0.005620177816171007
- coe3[0] = 0.0
- coe3[1] = 0.0

## Evaluation
cv = 8
### robot-1
#### accuracy
- Mean = 0.9695080824972129
- Standard deviation = 0.005385785011087567
- Max = 0.9766666666666667
- 75% = 0.9715719063545151
- Median = 0.9698996655518395
- 25% = 0.9682274247491639
- Min = 0.96

#### f1
- Mean = 0.9252277659947896
- Standard deviation = 0.0126515773939785
- Max = 0.9421487603305784
- 75% = 0.930416068866571
- Median = 0.9268292682926829
- 25% = 0.9212773109243697
- Min = 0.9016393442622951

#### precision
- Mean = 0.9117609658892407
- Standard deviation = 0.02318053680638244
- Max = 0.9491525423728814
- 75% = 0.9327590997499305
- Median = 0.9047619047619048
- 25% = 0.9003456221198156
- Min = 0.8769230769230769

#### recall
- Mean = 0.9395833333333333
- Standard deviation = 0.014282613750835503
- Max = 0.95
- 75% = 0.95
- Median = 0.95
- 25% = 0.9291666666666667
- Min = 0.9166666666666666

#### facing_probas
- Mean = [0.9665     0.791125   0.13319444 0.002625   0.00229167]
- Standard deviation = [0.01098076 0.02386875 0.02347896 0.00173467 0.00188311]
- Max = [0.98377778 0.84188889 0.16788889 0.00511111 0.00633333]
- 75% = [0.97283333 0.80133333 0.15086111 0.00430556 0.00283333]
- Median = [0.96788889 0.78322222 0.13194444 0.0025     0.00133333]
- 25% = [0.95644444 0.77230556 0.11644444 0.00108333 0.00105556]
- Min = [9.51777778e-01 7.67444444e-01 9.76666667e-02 2.22222222e-04
 6.66666667e-04]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 233.75 | 5.5 |
| Actual Positive | 3.625 | 56.375 |

### robot-2
#### accuracy
- Mean = 0.9611496655518394
- Standard deviation = 0.0072767723666476635
- Max = 0.9766666666666667
- 75% = 0.964046822742475
- Median = 0.959866220735786
- 25% = 0.9557246376811595
- Min = 0.9531772575250836

#### f1
- Mean = 0.899301574473685
- Standard deviation = 0.02023586998649838
- Max = 0.9421487603305784
- 75% = 0.9067091454272864
- Median = 0.8974284044418469
- 25% = 0.8835444003661885
- Min = 0.8749999999999999

#### precision
- Mean = 0.9331365103560114
- Standard deviation = 0.013309827779327701
- Max = 0.9464285714285714
- 75% = 0.9439108061749572
- Median = 0.9383669609079446
- 25% = 0.9248768472906405
- Min = 0.9107142857142857

#### recall
- Mean = 0.8687499999999999
- Standard deviation = 0.037673211083385665
- Max = 0.95
- 75% = 0.8833333333333333
- Median = 0.8666666666666667
- 25% = 0.8458333333333333
- Min = 0.8166666666666667

#### facing_probas
- Mean = [0.92418056 0.9355     0.82591667 0.11047222 0.00915278]
- Standard deviation = [0.01628147 0.01422157 0.01773273 0.01821898 0.00780964]
- Max = [0.94844444 0.952      0.85566667 0.15511111 0.02388889]
- 75% = [0.93266667 0.95002778 0.83866667 0.10875    0.01244444]
- Median = [0.92911111 0.93544444 0.81744444 0.103      0.00522222]
- 25% = [0.91488889 0.92691667 0.81536111 0.10025    0.00388889]
- Min = [0.89811111 0.90977778 0.80244444 0.09666667 0.00133333]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 235.5 | 3.75 |
| Actual Positive | 7.875 | 52.125 |

### robot-3
#### accuracy
- Mean = 0.9456953734671126
- Standard deviation = 0.012029441964919445
- Max = 0.96
- 75% = 0.9573578595317727
- Median = 0.9449219620958751
- 25% = 0.93561872909699
- Min = 0.9297658862876255

#### f1
- Mean = 0.8419810178866591
- Standard deviation = 0.04017025717282749
- Max = 0.888888888888889
- 75% = 0.8811007268951195
- Median = 0.8399028582103494
- 25% = 0.808910891089109
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
- Mean = 0.7291666666666667
- Standard deviation = 0.05994789404140901
- Max = 0.8
- 75% = 0.7875
- Median = 0.7250000000000001
- 25% = 0.6791666666666667
- Min = 0.65

#### facing_probas
- Mean = [0.33388889 0.95302778 0.97027778 0.91044444 0.12077778]
- Standard deviation = [0.03834183 0.00721148 0.01129883 0.01253858 0.03584681]
- Max = [0.392      0.96433333 0.98488889 0.92888889 0.20711111]
- 75% = [0.36152778 0.95555556 0.97619444 0.91758333 0.12394444]
- Median = [0.32544444 0.95411111 0.97155556 0.91005556 0.11288889]
- 25% = [0.31583333 0.95155556 0.96769444 0.90208333 0.09972222]
- Min = [0.26433333 0.93766667 0.94444444 0.89011111 0.08466667]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 239.25 | 0.0 |
| Actual Positive | 16.25 | 43.75 |

### robot-4
#### accuracy
- Mean = 0.9385953177257526
- Standard deviation = 0.012620552981644407
- Max = 0.9531772575250836
- 75% = 0.9474581939799331
- Median = 0.9431438127090301
- 25% = 0.9316053511705686
- Min = 0.9130434782608695

#### f1
- Mean = 0.8416997785641853
- Standard deviation = 0.03629899881973897
- Max = 0.8813559322033898
- 75% = 0.867948717948718
- Median = 0.8559218559218559
- 25% = 0.8237742130750605
- Min = 0.7678571428571428

#### precision
- Mean = 0.8555758567390433
- Standard deviation = 0.021037867507919143
- Max = 0.8813559322033898
- 75% = 0.8698275862068966
- Median = 0.8560344827586206
- 25% = 0.8479993493819129
- Min = 0.8113207547169812

#### recall
- Mean = 0.8290607344632768
- Standard deviation = 0.051951187333998824
- Max = 0.8813559322033898
- 75% = 0.8649717514124294
- Median = 0.8559322033898304
- 25% = 0.8031779661016949
- Min = 0.7288135593220338

#### facing_probas
- Mean = [0.01588089 0.15157745 0.91678319 0.9747992  0.7617959 ]
- Standard deviation = [0.00875797 0.02606871 0.02049401 0.00520198 0.03465407]
- Max = [0.03581921 0.18903955 0.93129944 0.98566667 0.79694915]
- 75% = [0.0180226  0.17213889 0.92702354 0.97652542 0.78442514]
- Median = [0.01276742 0.15440678 0.92410264 0.97531073 0.76949153]
- 25% = [0.01048446 0.12951977 0.91816384 0.97015913 0.75815819]
- Min = [0.00644068 0.10779661 0.8639548  0.96870056 0.67943503]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 231.75 | 8.25 |
| Actual Positive | 10.125 | 49.125 |

### robot-5
#### accuracy
- Mean = 0.971595596432553
- Standard deviation = 0.004095774235856027
- Max = 0.9765886287625418
- 75% = 0.9741471571906355
- Median = 0.9716220735785953
- 25% = 0.9698996655518395
- Min = 0.9632107023411371

#### f1
- Mean = 0.9240427216090933
- Standard deviation = 0.011375725259412781
- Max = 0.9380530973451328
- 75% = 0.9309418457648546
- Median = 0.9244627054361567
- 25% = 0.9189189189189189
- Min = 0.9009009009009009

#### precision
- Mean = 0.9951905290418054
- Standard deviation = 0.008332301612693466
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 0.9952830188679245
- Min = 0.9803921568627451

#### recall
- Mean = 0.8625
- Standard deviation = 0.01613743060919756
- Max = 0.8833333333333333
- 75% = 0.8708333333333333
- Median = 0.8666666666666667
- 25% = 0.85
- Min = 0.8333333333333334

#### facing_probas
- Mean = [0.00402778 0.00468056 0.23455556 0.95855556 0.95375   ]
- Standard deviation = [0.0030529  0.00379711 0.02333809 0.0064291  0.01683936]
- Max = [0.00911111 0.01222222 0.26644444 0.97033333 0.96733333]
- 75% = [0.00619444 0.00769444 0.25461111 0.96369444 0.96294444]
- Median = [0.00327778 0.00266667 0.23733333 0.95638889 0.95811111]
- 25% = [0.00127778 0.00186111 0.21830556 0.95336111 0.95491667]
- Min = [6.66666667e-04 7.77777778e-04 1.98777778e-01 9.51333333e-01
 9.10777778e-01]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 239.0 | 0.25 |
| Actual Positive | 8.25 | 51.75 |

### robot-6
#### accuracy
- Mean = 0.8458584169453736
- Standard deviation = 0.020070397160321222
- Max = 0.8695652173913043
- 75% = 0.8596488294314382
- Median = 0.8480824972129319
- 25% = 0.8436454849498327
- Min = 0.7993311036789298

#### f1
- Mean = 0.9163633344023225
- Standard deviation = 0.011951842624146825
- Max = 0.9302325581395349
- 75% = 0.9245281194399319
- Median = 0.9177965935723099
- 25% = 0.9151867030965392
- Min = 0.8884758364312267

#### precision
- Mean = 1.0
- Standard deviation = 0.0
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 1.0
- Min = 1.0

#### recall
- Mean = 0.8458584169453736
- Standard deviation = 0.020070397160321222
- Max = 0.8695652173913043
- 75% = 0.8596488294314382
- Median = 0.8480824972129319
- 25% = 0.8436454849498327
- Min = 0.7993311036789298

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
| Actual Positive | 46.125 | 253.125 |

