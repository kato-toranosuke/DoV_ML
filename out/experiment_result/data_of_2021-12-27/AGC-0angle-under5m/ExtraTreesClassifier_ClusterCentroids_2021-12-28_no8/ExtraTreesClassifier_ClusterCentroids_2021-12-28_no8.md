# ExtraTreesClassifier_ClusterCentroids_2021-12-28_no8
## Constants
- CSV_PATH = ../out/csv/experiment
- OUTPUT_PATH = ../out/experiment_result/data_of_2021-12-27/AGC-0angle-under5m
- FEATURE_ATTRBS = ['low_power', 'high_power', 'hlbr', 'coe1[0]', 'coe1[1]', 'coe3[0]', 'coe3[1]', 'coe3[2]', 'coe3[3]', 'ratio_max_to_10ms_ave_peaks', 'ratio_max_to_9th_ave_peaks', 'ac_std', 'ac_auc', 'diff_std', 'diff_auc', 'srmr', 'gp_max_val_std', 'gp_max_val_range', 'gp_max_val_min', 'gp_max_val_max', 'gp_max_val_mean', 'gp_max_ix_std', 'gp_max_ix_range', 'gp_max_ix_min', 'gp_max_ix_max', 'gp_max_ix_mean', 'gp_auc_std', 'gp_auc_range', 'gp_auc_min', 'gp_auc_max', 'gp_auc_mean', 'tdoa_std', 'tdoa_range', 'tdoa_min', 'tdoa_max', 'tdoa_mean']
- LABEL_ATTRB = ['facing']
- FACING_DOV_ANGLES = [1]
- NCV = 8
- SCORING = ['accuracy', 'balanced_accuracy', 'f1']
- REFIT_SCORING = balanced_accuracy
- PARAM_GRID = [{'est__n_estimators': [50, 100, 150, 200, 300], 'est__min_samples_split': [2, 5, 10], 'est__min_samples_leaf': [1, 5, 10], 'est__max_features': ['sqrt', 'log2', None], 'est__bootstrap': [False], 'est__n_jobs': [-1], 'est__random_state': [42], 'est__max_samples': [0.01, 0.5, 0.09]}, {'est__n_estimators': [50, 100, 150, 200, 300], 'est__min_samples_split': [2, 5, 10], 'est__min_samples_leaf': [1, 5, 10], 'est__max_features': ['sqrt', 'log2', None], 'est__bootstrap': [True], 'est__oob_score': [True, False], 'est__n_jobs': [-1], 'est__random_state': [42], 'est__max_samples': [0.01, 0.5, 0.09]}]
- TRAIN_SET_SESSION = ['trial1', 'trial2']
- TEST_SET_SESSION = ['trial3', 'trial4', 'trial5']
- DISTANCE = [1, 3, 5]
- AGC_STATUS = ['AGC']

## Loaded CSV
- 2021-12-27_raspi_48000Hz_w1_N2^12_overlap80_new.csv

## Estimator
### Type
- resampler = ClusterCentroids
- estimator = ExtraTreesClassifier

### Arguments for hyperparameter search
- resampler = ClusterCentroids
- estimator = ExtraTreesClassifier
- param_grid = 
	- {'est__n_estimators': [50, 100, 150, 200, 300], 'est__min_samples_split': [2, 5, 10], 'est__min_samples_leaf': [1, 5, 10], 'est__max_features': ['sqrt', 'log2', None], 'est__bootstrap': [False], 'est__n_jobs': [-1], 'est__random_state': [42], 'est__max_samples': [0.01, 0.5, 0.09]}
	- {'est__n_estimators': [50, 100, 150, 200, 300], 'est__min_samples_split': [2, 5, 10], 'est__min_samples_leaf': [1, 5, 10], 'est__max_features': ['sqrt', 'log2', None], 'est__bootstrap': [True], 'est__oob_score': [True, False], 'est__n_jobs': [-1], 'est__random_state': [42], 'est__max_samples': [0.01, 0.5, 0.09]}

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
	- sampling_strategy_ = OrderedDict([(0, 30)])
	- estimator_ = KMeans(n_clusters=30, random_state=42)
	- voting_ = soft

- best_estimator
	- base_estimator = ExtraTreeClassifier()
	- n_estimators = 50
	- estimator_params = ('criterion', 'max_depth', 'min_samples_split', 'min_samples_leaf', 'min_weight_fraction_leaf', 'max_features', 'max_leaf_nodes', 'min_impurity_decrease', 'min_impurity_split', 'random_state', 'ccp_alpha')
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
	- min_samples_split = 5
	- min_samples_leaf = 1
	- min_weight_fraction_leaf = 0.0
	- max_features = sqrt
	- max_leaf_nodes = None
	- min_impurity_decrease = 0.0
	- min_impurity_split = None
	- ccp_alpha = 0.0
	- n_features_in_ = 36
	- n_features_ = 36
	- n_outputs_ = 1
	- classes_ = [0 1]
	- n_classes_ = 2
	- base_estimator_ = ExtraTreeClassifier()
	- oob_decision_function_ = [[0.73958333 0.26041667]
 [0.69503968 0.30496032]
 [0.30384615 0.69615385]
 [0.73737374 0.26262626]
 [0.95       0.05      ]
 [0.921875   0.078125  ]
 [0.94010417 0.05989583]
 [0.54807692 0.45192308]
 [0.89032258 0.10967742]
 [0.36532258 0.63467742]
 [0.55241935 0.44758065]
 [0.72630208 0.27369792]
 [0.90802469 0.09197531]
 [0.984      0.016     ]
 [0.97222222 0.02777778]
 [0.45119048 0.54880952]
 [0.91071429 0.08928571]
 [0.63978495 0.36021505]
 [0.90804598 0.09195402]
 [0.79       0.21      ]
 [0.8637931  0.1362069 ]
 [0.65269608 0.34730392]
 [0.80208333 0.19791667]
 [0.74137931 0.25862069]
 [0.95208333 0.04791667]
 [0.96129032 0.03870968]
 [1.         0.        ]
 [0.50714286 0.49285714]
 [0.63661616 0.36338384]
 [0.92307692 0.07692308]
 [0.215      0.785     ]
 [0.12592593 0.87407407]
 [0.35196078 0.64803922]
 [0.31130952 0.68869048]
 [0.52277778 0.47722222]
 [0.29596774 0.70403226]
 [0.125      0.875     ]
 [0.32608696 0.67391304]
 [0.14942529 0.85057471]
 [0.04285714 0.95714286]
 [0.765      0.235     ]
 [0.40208333 0.59791667]
 [0.22068966 0.77931034]
 [0.17407407 0.82592593]
 [0.00735294 0.99264706]
 [0.05833333 0.94166667]
 [0.33619792 0.66380208]
 [0.33796296 0.66203704]
 [0.0137931  0.9862069 ]
 [0.10833333 0.89166667]
 [0.17204301 0.82795699]
 [0.1308642  0.8691358 ]
 [0.24305556 0.75694444]
 [0.25714286 0.74285714]
 [0.38548387 0.61451613]
 [0.07878788 0.92121212]
 [0.11666667 0.88333333]
 [0.046875   0.953125  ]
 [0.43813131 0.56186869]
 [0.39136905 0.60863095]]
	- oob_score_ = 0.9166666666666666

#### Importance of features
- gp_auc_min = 0.11014907153396582
- gp_max_val_mean = 0.10634944813943614
- gp_max_val_min = 0.09970945977764395
- gp_auc_mean = 0.06790422366437446
- gp_auc_max = 0.06265713956269159
- high_power = 0.05893290677718624
- gp_max_val_max = 0.048732023199867774
- coe1[1] = 0.04623017262795382
- gp_max_ix_std = 0.045879213385191825
- srmr = 0.04056920566734739
- hlbr = 0.028654646014948982
- coe1[0] = 0.020837036257769448
- gp_max_ix_max = 0.020660466075281235
- diff_auc = 0.01954175697609946
- tdoa_max = 0.019252897611467434
- tdoa_mean = 0.017838021773521742
- gp_max_ix_range = 0.017571348936845445
- ratio_max_to_10ms_ave_peaks = 0.015916650641616306
- gp_max_ix_mean = 0.014839818715815727
- ac_std = 0.014419837436134526
- coe3[2] = 0.01405998246100096
- tdoa_min = 0.013960843693024843
- ratio_max_to_9th_ave_peaks = 0.01204653836559791
- coe3[3] = 0.0114568927682524
- low_power = 0.01075387353122849
- tdoa_std = 0.010196026813985865
- diff_std = 0.010092376429274826
- tdoa_range = 0.009555283551225414
- ac_auc = 0.0071952505513688935
- gp_max_val_std = 0.0070144888752962774
- gp_max_ix_min = 0.00604984051535058
- gp_auc_std = 0.004507039268361177
- gp_max_val_range = 0.0038293153610660696
- gp_auc_range = 0.00263690303980704
- coe3[0] = 0.0
- coe3[1] = 0.0

## Evaluation
cv = 8
### accuracy
- Scores = [ 0.6785714285714286, 0.75, 0.5714285714285714, 0.7142857142857143, 0.6785714285714286, 0.5, 0.8214285714285714, 0.8571428571428571 ]
- Mean = 0.6964285714285714
- Standard deviation = 0.11151782139997139

### balanced_accuracy
- Scores = [ 0.7954545454545454, 0.7803030303030303, 0.5454545454545454, 0.8181818181818181, 0.7954545454545454, 0.6956521739130435, 0.8130434782608695, 0.8347826086956522 ]
- Mean = 0.7597908432147562
- Standard deviation = 0.09006072989814258

### f1
- Scores = [ 0.5714285714285715, 0.5882352941176471, 0.3333333333333333, 0.6, 0.5714285714285715, 0.4166666666666667, 0.6153846153846154, 0.6666666666666666 ]
- Mean = 0.545392964878259
- Standard deviation = 0.10447427203899624

### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 117 | 62 |
| Actual Positive | 6 | 39 |

      