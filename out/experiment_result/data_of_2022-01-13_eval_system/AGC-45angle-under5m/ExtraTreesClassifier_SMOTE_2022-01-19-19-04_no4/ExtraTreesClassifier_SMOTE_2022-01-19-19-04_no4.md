# ExtraTreesClassifier_SMOTE_2022-01-19-19-04_no4
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
	- sampling_strategy_ = OrderedDict([(0, 8)])
	- nn_k_ = NearestNeighbors(n_neighbors=6)

- best_estimator
	- base_estimator = ExtraTreeClassifier()
	- n_estimators = 30
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
- gp_max_val_min = 0.10035109598714391
- gp_auc_max = 0.09045921917698829
- gp_max_val_mean = 0.07875051375888371
- gp_auc_min = 0.07766657418934342
- gp_max_val_max = 0.07107778306295903
- gp_auc_mean = 0.060863264553107255
- high_power = 0.05758937320394273
- srmr = 0.041032095643402294
- hlbr = 0.038987038548525074
- diff_auc = 0.03254452698347672
- coe1[0] = 0.02972551108149888
- gp_max_ix_mean = 0.02966184702565757
- gp_max_ix_std = 0.02916721874252675
- diff_std = 0.028645393007702285
- tdoa_mean = 0.027644183085377548
- tdoa_std = 0.022664691634030953
- gp_max_ix_min = 0.01970874507803623
- coe1[1] = 0.01777562511477748
- gp_auc_std = 0.01763937692239022
- gp_max_val_std = 0.014736519438968022
- gp_max_val_range = 0.01278593311299878
- gp_auc_range = 0.012755313661728681
- ratio_max_to_10ms_ave_peaks = 0.0117380994619069
- gp_max_ix_range = 0.010930533493483737
- tdoa_min = 0.010405277624905894
- tdoa_range = 0.009242000784828446
- gp_max_ix_max = 0.00864211200022174
- coe3[2] = 0.007303778910179279
- low_power = 0.006302844348831746
- ac_auc = 0.006034519466287001
- tdoa_max = 0.004650785756740031
- coe3[3] = 0.004548994318154061
- ac_std = 0.004059801192287581
- ratio_max_to_9th_ave_peaks = 0.003909409628707877
- coe3[0] = 0.0
- coe3[1] = 0.0

## Evaluation
cv = 8
### robot-1
#### accuracy
- Mean = 0.9699358974358975
- Standard deviation = 0.0033531648242024585
- Max = 0.9733333333333334
- 75% = 0.9732664437012264
- Median = 0.9698996655518395
- 25% = 0.9690914158305463
- Min = 0.9632107023411371

#### f1
- Mean = 0.9272850813874703
- Standard deviation = 0.009198676464926774
- Max = 0.9365079365079364
- 75% = 0.9357398873527905
- Median = 0.9279815632801998
- 25% = 0.9243736061917881
- Min = 0.9075630252100839

#### precision
- Mean = 0.8989453263159157
- Standard deviation = 0.013741381436109885
- Max = 0.9180327868852459
- 75% = 0.908501059322034
- Median = 0.8993506493506493
- 25% = 0.8906037991858887
- Min = 0.8787878787878788

#### recall
- Mean = 0.9583333333333333
- Standard deviation = 0.02763853991962831
- Max = 0.9833333333333333
- 75% = 0.9833333333333333
- Median = 0.9666666666666667
- 25% = 0.9458333333333333
- Min = 0.9

#### facing_probas
- Mean = [0.96409722 0.76354167 0.1275     0.00263889 0.00277778]
- Standard deviation = [0.01387482 0.02931567 0.0188991  0.00288341 0.00279163]
- Max = [0.98166667 0.81444444 0.16666667 0.00722222 0.00777778]
- 75% = [0.97375    0.78291667 0.13680556 0.00569444 0.00347222]
- Median = [9.68888889e-01 7.58888889e-01 1.20833333e-01 8.33333333e-04
 1.66666667e-03]
- 25% = [9.55972222e-01 7.40416667e-01 1.12638889e-01 4.16666667e-04
 5.55555556e-04]
- Min = [9.36666667e-01 7.27222222e-01 1.08333333e-01 0.00000000e+00
 5.55555556e-04]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 232.875 | 6.5 |
| Actual Positive | 2.5 | 57.5 |

### robot-2
#### accuracy
- Mean = 0.9645052954292085
- Standard deviation = 0.006895286086323014
- Max = 0.9733333333333334
- 75% = 0.9699247491638796
- Median = 0.9648829431438127
- 25% = 0.9624080267558528
- Min = 0.9498327759197325

#### f1
- Mean = 0.9073471406920648
- Standard deviation = 0.01744814301639181
- Max = 0.9310344827586207
- 75% = 0.9203539823008849
- Median = 0.9098010316875461
- 25% = 0.8993598862019915
- Min = 0.8717948717948718

#### precision
- Mean = 0.9528265421068411
- Standard deviation = 0.028433024757329152
- Max = 0.9811320754716981
- 75% = 0.9805771365149833
- Median = 0.9548701298701299
- 25% = 0.9410919540229885
- Min = 0.8947368421052632

#### recall
- Mean = 0.8666666666666667
- Standard deviation = 0.02204792759220493
- Max = 0.9
- 75% = 0.875
- Median = 0.8666666666666667
- 25% = 0.85
- Min = 0.8333333333333334

#### facing_probas
- Mean = [0.93618056 0.94777778 0.82604167 0.09840278 0.00708333]
- Standard deviation = [0.0088821  0.00798822 0.0161313  0.01586361 0.00362976]
- Max = [0.95       0.96111111 0.84333333 0.12833333 0.01444444]
- 75% = [0.94361111 0.95347222 0.83652778 0.10152778 0.00805556]
- Median = [0.93638889 0.94805556 0.83138889 0.09361111 0.00722222]
- 25% = [0.92888889 0.94277778 0.82263889 0.08708333 0.00555556]
- Min = [0.92222222 0.93555556 0.79111111 0.08166667 0.00111111]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 236.75 | 2.625 |
| Actual Positive | 8.0 | 52.0 |

### robot-3
#### accuracy
- Mean = 0.9515635451505018
- Standard deviation = 0.009902346721675477
- Max = 0.9698996655518395
- 75% = 0.9541666666666667
- Median = 0.9531772575250836
- 25% = 0.9482859531772575
- Min = 0.9331103678929766

#### f1
- Mean = 0.861661436271914
- Standard deviation = 0.03204638476959111
- Max = 0.9189189189189189
- 75% = 0.8705695644507143
- Median = 0.8679245283018869
- 25% = 0.8515950069348127
- Min = 0.8

#### precision
- Mean = 1.0
- Standard deviation = 0.0
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 1.0
- Min = 1.0

#### recall
- Mean = 0.7583333333333333
- Standard deviation = 0.04930066485916348
- Max = 0.85
- 75% = 0.7708333333333334
- Median = 0.7666666666666667
- 25% = 0.7416666666666667
- Min = 0.6666666666666666

#### facing_probas
- Mean = [0.31145833 0.94416667 0.96875    0.90034722 0.11694444]
- Standard deviation = [0.03287643 0.01556299 0.013399   0.03061476 0.02875235]
- Max = [0.38       0.96888889 0.98666667 0.93944444 0.17666667]
- 75% = [0.31944444 0.95263889 0.97805556 0.92       0.12847222]
- Median = [0.30055556 0.94555556 0.96944444 0.9        0.11138889]
- 25% = [0.29041667 0.93694444 0.96013889 0.89208333 0.09361111]
- Min = [0.27777778 0.91722222 0.945      0.83277778 0.08444444]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 239.375 | 0.0 |
| Actual Positive | 14.5 | 45.5 |

### robot-4
#### accuracy
- Mean = 0.9348704013377926
- Standard deviation = 0.014806972769760214
- Max = 0.95
- 75% = 0.9498327759197325
- Median = 0.9365663322185062
- 25% = 0.9272575250836121
- Min = 0.9066666666666666

#### f1
- Mean = 0.8290681286207795
- Standard deviation = 0.04125952170431346
- Max = 0.8739495798319329
- 75% = 0.8701226309921962
- Median = 0.833435960591133
- 25% = 0.8060740144810942
- Min = 0.7543859649122806

#### precision
- Mean = 0.8612860792010396
- Standard deviation = 0.03152166788398251
- Max = 0.9090909090909091
- 75% = 0.8811808718282368
- Median = 0.861904761904762
- 25% = 0.8496732026143791
- Min = 0.7962962962962963

#### recall
- Mean = 0.8001059322033899
- Standard deviation = 0.05513070976359685
- Max = 0.8813559322033898
- 75% = 0.8411016949152543
- Median = 0.7983050847457627
- 25% = 0.7669491525423728
- Min = 0.7166666666666667

#### facing_probas
- Mean = [0.01404896 0.14305791 0.90443856 0.9715984  0.74331921]
- Standard deviation = [0.00798645 0.0266723  0.0110032  0.01004066 0.03664035]
- Max = [0.03333333 0.18870056 0.9259887  0.98926554 0.79322034]
- 75% = [0.01430556 0.15829567 0.91102401 0.97757062 0.77457627]
- Median = [0.01355932 0.13954802 0.90225047 0.96945857 0.74218456]
- 25% = [0.00889831 0.11833333 0.89833333 0.96486111 0.71252354]
- Min = [0.00611111 0.11412429 0.88870056 0.95932203 0.68666667]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 232.375 | 7.625 |
| Actual Positive | 11.875 | 47.5 |

### robot-5
#### accuracy
- Mean = 0.9741151059085842
- Standard deviation = 0.00570525669881696
- Max = 0.9833333333333333
- 75% = 0.9774247491638797
- Median = 0.9732441471571907
- 25% = 0.9724331103678929
- Min = 0.9633333333333334

#### f1
- Mean = 0.9308867617938387
- Standard deviation = 0.016273759397288014
- Max = 0.9565217391304348
- 75% = 0.9403819282720075
- Median = 0.9285714285714286
- 25% = 0.9265170670037927
- Min = 0.8990825688073394

#### precision
- Mean = 0.9976415094339622
- Standard deviation = 0.006239979507227806
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 1.0
- Min = 0.9811320754716981

#### recall
- Mean = 0.8729166666666667
- Standard deviation = 0.027559909490256145
- Max = 0.9166666666666666
- 75% = 0.8875
- Median = 0.8666666666666667
- 25% = 0.8666666666666667
- Min = 0.8166666666666667

#### facing_probas
- Mean = [0.00444444 0.00298611 0.22090278 0.95597222 0.95069444]
- Standard deviation = [0.00225668 0.00311727 0.02460951 0.01013318 0.01272862]
- Max = [0.00777778 0.01       0.25055556 0.97333333 0.96888889]
- 75% = [0.00597222 0.00444444 0.24027778 0.96138889 0.96013889]
- Median = [0.00444444 0.00194444 0.22472222 0.95527778 0.95027778]
- 25% = [2.91666667e-03 5.55555556e-04 2.13750000e-01 9.50000000e-01
 9.45694444e-01]
- Min = [0.00111111 0.         0.17111111 0.94055556 0.92722222]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 239.25 | 0.125 |
| Actual Positive | 7.625 | 52.375 |

### robot-6
#### accuracy
- Mean = 0.8513559085841694
- Standard deviation = 0.010962938195321575
- Max = 0.8662207357859532
- 75% = 0.8583333333333334
- Median = 0.8528428093645485
- 25% = 0.8462904124860646
- Min = 0.8327759197324415

#### f1
- Mean = 0.9196727110238396
- Standard deviation = 0.006413491911634286
- Max = 0.9283154121863798
- 75% = 0.9237642237516982
- Median = 0.9205776173285198
- 25% = 0.9167369536893303
- Min = 0.9087591240875912

#### precision
- Mean = 1.0
- Standard deviation = 0.0
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 1.0
- Min = 1.0

#### recall
- Mean = 0.8513559085841694
- Standard deviation = 0.010962938195321575
- Max = 0.8662207357859532
- 75% = 0.8583333333333334
- Median = 0.8528428093645485
- 25% = 0.8462904124860646
- Min = 0.8327759197324415

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
| Actual Positive | 44.5 | 254.875 |

