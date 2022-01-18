# ExtraTreesClassifier_ClusterCentroids_2022-01-17-00-14_no0
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
- resampler = ClusterCentroids
- estimator = ExtraTreesClassifier

### Arguments for hyperparameter search
- resampler = ClusterCentroids
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
	- estimator = None
	- voting = auto
	- n_jobs = deprecated
	- n_features_in_ = 36
	- sampling_strategy_ = OrderedDict([(0, 15)])
	- estimator_ = KMeans(n_clusters=15, random_state=42)
	- voting_ = soft

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
	- min_samples_split = 10
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
- tdoa_mean = 0.10996927262128937
- gp_max_ix_std = 0.10260402572918359
- gp_auc_min = 0.0957238036861086
- gp_auc_mean = 0.07580250752193768
- gp_max_val_max = 0.07534449907116195
- tdoa_range = 0.07382588438574259
- gp_max_ix_range = 0.07078538202175437
- gp_max_val_min = 0.06762522051345041
- gp_max_ix_mean = 0.05609788945859503
- gp_max_val_mean = 0.055091042740492764
- gp_auc_max = 0.05295598463614658
- tdoa_max = 0.02851497249518141
- gp_auc_range = 0.0249678157279525
- tdoa_min = 0.019640570032726897
- gp_max_val_std = 0.01722595466671296
- gp_max_ix_max = 0.011437908496732029
- diff_std = 0.010913647755753023
- gp_max_ix_min = 0.010256410256410256
- srmr = 0.008996870794623605
- gp_max_val_range = 0.005281385281385281
- ac_auc = 0.004878048780487805
- gp_auc_std = 0.004210526315789476
- tdoa_std = 0.0040404040404040395
- ac_std = 0.0034401057110220444
- diff_auc = 0.003213811420982736
- coe3[3] = 0.0028350681836520576
- low_power = 0.0024691358024691366
- coe3[2] = 0.001851851851851852
- high_power = 0.0
- hlbr = 0.0
- coe1[0] = 0.0
- coe1[1] = 0.0
- coe3[0] = 0.0
- coe3[1] = 0.0
- ratio_max_to_10ms_ave_peaks = 0.0
- ratio_max_to_9th_ave_peaks = 0.0

## Evaluation
cv = 8
### robot-1
#### accuracy
- Mean = 0.9406565656565657
- Standard deviation = 0.017080491487965498
- Max = 0.9696969696969697
- 75% = 0.952020202020202
- Median = 0.9393939393939394
- 25% = 0.9267676767676768
- Min = 0.9191919191919192

#### f1
- Mean = 0.8674018028425658
- Standard deviation = 0.0335433228779093
- Max = 0.9268292682926829
- 75% = 0.888981173864895
- Median = 0.8636363636363635
- 25% = 0.8362403100775194
- Min = 0.8260869565217392

#### precision
- Mean = 0.8006852748700575
- Standard deviation = 0.059458599560104214
- Max = 0.9047619047619048
- 75% = 0.8354743083003953
- Median = 0.7916666666666666
- 25% = 0.7696488294314381
- Min = 0.7142857142857143

#### recall
- Mean = 0.95
- Standard deviation = 0.024999999999999994
- Max = 1.0
- 75% = 0.95
- Median = 0.95
- 25% = 0.95
- Min = 0.9

#### facing_probas
- Mean = [0.9478631  0.4769809  0.29295337 0.01024223 0.06079365]
- Standard deviation = [0.02042683 0.09058313 0.08233991 0.01166651 0.03237789]
- Max = [0.97178836 0.60370899 0.44113624 0.03972222 0.12333333]
- 75% = [0.9616336  0.5305787  0.35417659 0.00973545 0.07899471]
- Median = [0.95206118 0.48202943 0.2823793  0.00517857 0.04735714]
- 25% = [0.94134094 0.41335847 0.22176637 0.00333333 0.03630952]
- Min = [0.9041541  0.33161376 0.18260582 0.00291667 0.02833333]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 74.125 | 4.875 |
| Actual Positive | 1.0 | 19.0 |

### robot-2
#### accuracy
- Mean = 0.8737373737373737
- Standard deviation = 0.02314432169169616
- Max = 0.9090909090909091
- 75% = 0.8914141414141414
- Median = 0.8737373737373737
- 25% = 0.8560606060606061
- Min = 0.8383838383838383

#### f1
- Mean = 0.6050845636565882
- Standard deviation = 0.09071992771543588
- Max = 0.7272727272727274
- 75% = 0.671875
- Median = 0.6236559139784945
- 25% = 0.5425646551724139
- Min = 0.4666666666666667

#### precision
- Mean = 0.810232128982129
- Standard deviation = 0.07572652407249886
- Max = 0.9230769230769231
- 75% = 0.8637820512820513
- Median = 0.797979797979798
- 25% = 0.75
- Min = 0.7

#### recall
- Mean = 0.48749999999999993
- Standard deviation = 0.0960143218483576
- Max = 0.6
- 75% = 0.5625
- Median = 0.5
- 25% = 0.425
- Min = 0.35

#### facing_probas
- Mean = [0.89943444 0.93626389 0.91633846 0.06783722 0.04309309]
- Standard deviation = [0.03361505 0.02164072 0.02873187 0.01866992 0.01810563]
- Max = [0.96301323 0.97696362 0.96610714 0.09440212 0.07458333]
- 75% = [0.91889914 0.94697239 0.92852216 0.08199901 0.05118618]
- Median = [0.89356085 0.93433399 0.91004497 0.07003505 0.04549107]
- 25% = [0.87126736 0.9203244  0.90069147 0.04808862 0.02407738]
- Min = [0.86424339 0.9090873  0.87478439 0.04423611 0.02137103]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 76.75 | 2.25 |
| Actual Positive | 10.25 | 9.75 |

### robot-3
#### accuracy
- Mean = 0.9128787878787878
- Standard deviation = 0.031107790390795254
- Max = 0.9494949494949495
- 75% = 0.9318181818181819
- Median = 0.9191919191919192
- 25% = 0.9090909090909092
- Min = 0.8484848484848485

#### f1
- Mean = 0.8008073386567176
- Standard deviation = 0.05567720281085314
- Max = 0.8648648648648648
- 75% = 0.8458333333333333
- Median = 0.8181818181818182
- 25% = 0.7681159420289855
- Min = 0.6938775510204082

#### precision
- Mean = 0.7707786901232642
- Standard deviation = 0.10891117600369374
- Max = 0.9411764705882353
- 75% = 0.85625
- Median = 0.755
- 25% = 0.7259615384615384
- Min = 0.5862068965517241

#### recall
- Mean = 0.85
- Standard deviation = 0.07071067811865477
- Max = 0.95
- 75% = 0.9
- Median = 0.85
- 25% = 0.8375
- Min = 0.7

#### facing_probas
- Mean = [0.50687202 0.78275942 0.93892692 0.55904621 0.25027951]
- Standard deviation = [0.09283858 0.07623144 0.02276628 0.08769213 0.05863977]
- Max = [0.64613095 0.91754167 0.98239087 0.69922156 0.34908862]
- 75% = [0.55986045 0.82060599 0.94842758 0.59322636 0.28265079]
- Median = [0.54134226 0.8088006  0.93679299 0.54934325 0.23462037]
- 25% = [0.44674239 0.70979663 0.92737682 0.51947156 0.2099003 ]
- Min = [0.3651078  0.67377447 0.90036111 0.42831283 0.17029365]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 73.375 | 5.625 |
| Actual Positive | 3.0 | 17.0 |

### robot-4
#### accuracy
- Mean = 0.898989898989899
- Standard deviation = 0.02368896848395672
- Max = 0.9292929292929293
- 75% = 0.9191919191919192
- Median = 0.904040404040404
- 25% = 0.8838383838383839
- Min = 0.8585858585858586

#### f1
- Mean = 0.7935216420648764
- Standard deviation = 0.03799566503213913
- Max = 0.8444444444444443
- 75% = 0.8260869565217391
- Median = 0.8000886524822695
- 25% = 0.767907162865146
- Min = 0.7307692307692308

#### precision
- Mean = 0.6593451737040099
- Standard deviation = 0.05170837006690492
- Max = 0.7307692307692307
- 75% = 0.7037037037037037
- Median = 0.666871921182266
- 25% = 0.6234375
- Min = 0.5757575757575758

#### recall
- Mean = 1.0
- Standard deviation = 0.0
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 1.0
- Min = 1.0

#### facing_probas
- Mean = [0.00701885 0.01159687 0.53046514 0.93441912 0.61968759]
- Standard deviation = [0.00793531 0.0053143  0.09246728 0.0238397  0.08478917]
- Max = [0.02475634 0.02156085 0.68993317 0.97917711 0.78964773]
- 75% = [0.00806791 0.01383772 0.57154396 0.94741559 0.65404449]
- Median = [0.00416667 0.01183514 0.50897208 0.9312413  0.58120893]
- 25% = [0.00153509 0.00932018 0.47759781 0.91677005 0.57154884]
- Min = [0.         0.00263158 0.38935881 0.90359649 0.51535784]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 70.0 | 10.0 |
| Actual Positive | 0.0 | 19.0 |

### robot-5
#### accuracy
- Mean = 0.9103535353535354
- Standard deviation = 0.024966818097582326
- Max = 0.9494949494949495
- 75% = 0.9242424242424243
- Median = 0.9141414141414141
- 25% = 0.8863636363636364
- Min = 0.8787878787878788

#### f1
- Mean = 0.7067370607864948
- Standard deviation = 0.10249103433316932
- Max = 0.8571428571428571
- 75% = 0.7683823529411764
- Median = 0.7298387096774193
- 25% = 0.6083743842364533
- Min = 0.5714285714285715

#### precision
- Mean = 1.0
- Standard deviation = 0.0
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 1.0
- Min = 1.0

#### recall
- Mean = 0.55625
- Standard deviation = 0.12358574958303241
- Max = 0.75
- 75% = 0.625
- Median = 0.575
- 25% = 0.4375
- Min = 0.4

#### facing_probas
- Mean = [0.10435888 0.00436797 0.02879605 0.85213724 0.89008309]
- Standard deviation = [0.03543611 0.00567853 0.01178823 0.03626302 0.02735038]
- Max = [0.19354167 0.01793981 0.05054497 0.90982143 0.94947751]
- 75% = [0.09991667 0.00605159 0.03488426 0.87765939 0.8999962 ]
- Median = [0.09454365 0.00224537 0.02811111 0.84325959 0.87992063]
- 25% = [0.08738442 0.         0.02155423 0.81881498 0.87323512]
- Min = [0.07181151 0.         0.01118056 0.81234656 0.85736111]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 79.0 | 0.0 |
| Actual Positive | 8.875 | 11.125 |

### robot-6
#### accuracy
- Mean = 0.7664141414141414
- Standard deviation = 0.0414749184486284
- Max = 0.8282828282828283
- 75% = 0.7878787878787878
- Median = 0.7676767676767676
- 25% = 0.7449494949494949
- Min = 0.7070707070707071

#### f1
- Mean = 0.8671367380567759
- Standard deviation = 0.02666621926127406
- Max = 0.9060773480662984
- 75% = 0.8812500000000001
- Median = 0.8685714285714284
- 25% = 0.8536523158539073
- Min = 0.8284023668639052

#### precision
- Mean = 1.0
- Standard deviation = 0.0
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 1.0
- Min = 1.0

#### recall
- Mean = 0.7664141414141414
- Standard deviation = 0.0414749184486284
- Max = 0.8282828282828283
- 75% = 0.7878787878787878
- Median = 0.7676767676767676
- 25% = 0.7449494949494949
- Min = 0.7070707070707071

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
| Actual Positive | 23.125 | 75.875 |

