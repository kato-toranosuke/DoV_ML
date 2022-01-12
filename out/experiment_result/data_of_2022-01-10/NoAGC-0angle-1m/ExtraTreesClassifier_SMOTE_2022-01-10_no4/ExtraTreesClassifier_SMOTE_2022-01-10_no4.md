# ExtraTreesClassifier_SMOTE_2022-01-10_no4
## Constants
- CSV_PATH = ../out/csv/experiment
- OUTPUT_PATH = ../out/experiment_result/data_of_2022-01-10/NoAGC-0angle-1m
- FEATURE_ATTRBS = ['low_power', 'high_power', 'hlbr', 'coe1[0]', 'coe1[1]', 'coe3[0]', 'coe3[1]', 'coe3[2]', 'coe3[3]', 'ratio_max_to_10ms_ave_peaks', 'ratio_max_to_9th_ave_peaks', 'ac_std', 'ac_auc', 'diff_std', 'diff_auc', 'srmr', 'gp_max_val_std', 'gp_max_val_range', 'gp_max_val_min', 'gp_max_val_max', 'gp_max_val_mean', 'gp_max_ix_std', 'gp_max_ix_range', 'gp_max_ix_min', 'gp_max_ix_max', 'gp_max_ix_mean', 'gp_auc_std', 'gp_auc_range', 'gp_auc_min', 'gp_auc_max', 'gp_auc_mean', 'tdoa_std', 'tdoa_range', 'tdoa_min', 'tdoa_max', 'tdoa_mean']
- LABEL_ATTRB = ['facing']
- FACING_DOV_ANGLES = [1]
- NCV = 8
- SCORING = ['accuracy', 'balanced_accuracy', 'f1']
- REFIT_SCORING = balanced_accuracy
- PARAM_GRID = [{'est__n_estimators': [50, 100, 150, 200, 300], 'est__min_samples_split': [2, 5, 10], 'est__min_samples_leaf': [1, 5, 10], 'est__max_features': ['sqrt', 'log2', None], 'est__bootstrap': [False], 'est__n_jobs': [-1], 'est__random_state': [42], 'est__max_samples': [0.01, 0.5, 0.09]}, {'est__n_estimators': [50, 100, 150, 200, 300], 'est__min_samples_split': [2, 5, 10], 'est__min_samples_leaf': [1, 5, 10], 'est__max_features': ['sqrt', 'log2', None], 'est__bootstrap': [True], 'est__oob_score': [True, False], 'est__n_jobs': [-1], 'est__random_state': [42], 'est__max_samples': [0.01, 0.5, 0.09]}]
- TRAIN_SET_SESSION = ['trial1', 'trial2']
- TEST_SET_SESSION = ['trial3', 'trial4', 'trial5']
- DISTANCE = [1]
- AGC_STATUS = ['NoAGC']

## Loaded CSV
- 2022-01-10_raspi_48000Hz_w1_N2^12_overlap80.csv

## Estimator
### Type
- resampler = SMOTE
- estimator = ExtraTreesClassifier

### Arguments for hyperparameter search
- resampler = SMOTE
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
	- k_neighbors = 5
	- n_jobs = -1
	- n_features_in_ = 36
	- sampling_strategy_ = OrderedDict([(1, 30)])
	- nn_k_ = NearestNeighbors(n_neighbors=6)

- best_estimator
	- base_estimator = ExtraTreeClassifier()
	- n_estimators = 100
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
	- min_samples_leaf = 5
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
	- oob_decision_function_ = [[0.28959058 0.71040942]
 [0.26100237 0.73899763]
 [0.36085035 0.63914965]
 [0.30860449 0.69139551]
 [0.6746295  0.3253705 ]
 [0.65990716 0.34009284]
 [0.88024117 0.11975883]
 [0.88180699 0.11819301]
 [0.91370739 0.08629261]
 [0.90905947 0.09094053]
 [0.44917891 0.55082109]
 [0.26942874 0.73057126]
 [0.34835452 0.65164548]
 [0.32054154 0.67945846]
 [0.37736126 0.62263874]
 [0.43709784 0.56290216]
 [0.6517257  0.3482743 ]
 [0.77827377 0.22172623]
 [0.87069201 0.12930799]
 [0.87573632 0.12426368]
 [0.83760741 0.16239259]
 [0.67465833 0.32534167]
 [0.37812795 0.62187205]
 [0.44285297 0.55714703]
 [0.41180841 0.58819159]
 [0.44518076 0.55481924]
 [0.50185417 0.49814583]
 [0.56344634 0.43655366]
 [0.74451347 0.25548653]
 [0.82259508 0.17740492]
 [0.88338978 0.11661022]
 [0.88784389 0.11215611]
 [0.80961175 0.19038825]
 [0.51885698 0.48114302]
 [0.42131509 0.57868491]
 [0.39851668 0.60148332]
 [0.48658236 0.51341764]
 [0.41695738 0.58304262]
 [0.30798279 0.69201721]
 [0.34009845 0.65990155]
 [0.87549315 0.12450685]
 [0.88010536 0.11989464]
 [0.85403038 0.14596962]
 [0.89349049 0.10650951]
 [0.63636582 0.36363418]
 [0.63469002 0.36530998]
 [0.45483181 0.54516819]
 [0.43553239 0.56446761]
 [0.22109649 0.77890351]
 [0.24522968 0.75477032]
 [0.24066537 0.75933463]
 [0.29923578 0.70076422]
 [0.31282117 0.68717883]
 [0.40942335 0.59057665]
 [0.27831121 0.72168879]
 [0.46417366 0.53582634]
 [0.22180041 0.77819959]
 [0.29528545 0.70471455]
 [0.48551523 0.51448477]
 [0.26783893 0.73216107]
 [0.26844109 0.73155891]
 [0.22221381 0.77778619]
 [0.43670986 0.56329014]
 [0.46749657 0.53250343]
 [0.21726972 0.78273028]
 [0.26487554 0.73512446]
 [0.370743   0.629257  ]
 [0.26524373 0.73475627]
 [0.32314524 0.67685476]
 [0.20149794 0.79850206]
 [0.29380574 0.70619426]
 [0.35799684 0.64200316]
 [0.26030501 0.73969499]
 [0.45856954 0.54143046]
 [0.4016202  0.5983798 ]
 [0.31158568 0.68841432]
 [0.38097877 0.61902123]
 [0.25238796 0.74761204]
 [0.3615863  0.6384137 ]
 [0.333355   0.666645  ]]
	- oob_score_ = 0.825

#### Importance of features
- gp_auc_max = 0.10716897522190837
- gp_max_val_mean = 0.06852356154284303
- hlbr = 0.0669046311932891
- gp_max_val_max = 0.05997278550092977
- gp_max_val_min = 0.05514280638765203
- tdoa_range = 0.050851872302224196
- gp_max_ix_range = 0.04875479331979219
- gp_max_ix_min = 0.04343821583830269
- tdoa_mean = 0.03763810630409015
- tdoa_min = 0.03473443894093705
- tdoa_max = 0.03375874308024428
- gp_auc_min = 0.03327128503115955
- gp_auc_mean = 0.0323340155707932
- diff_std = 0.031026135482176018
- gp_max_ix_std = 0.030792502343164392
- gp_max_ix_max = 0.028679491626365777
- gp_max_ix_mean = 0.027428034747645876
- gp_max_val_std = 0.022779087297042408
- high_power = 0.02088536688041954
- srmr = 0.018820151784464306
- diff_auc = 0.01856122810323806
- coe3[2] = 0.015129315928184145
- tdoa_std = 0.01488264087403145
- gp_auc_std = 0.014093114147381321
- coe1[0] = 0.01341061800783388
- low_power = 0.0111357636999455
- gp_auc_range = 0.0111081341533191
- ratio_max_to_10ms_ave_peaks = 0.010344394383077592
- gp_max_val_range = 0.010132891368294263
- coe1[1] = 0.010129069690985894
- ratio_max_to_9th_ave_peaks = 0.00949945452864731
- ac_std = 0.004522391695773713
- ac_auc = 0.0022806280628067327
- coe3[3] = 0.001865354961036943
- coe3[0] = 0.0
- coe3[1] = 0.0

## Evaluation
cv = 8
### accuracy
- Scores = [ 0.5, 0.6, 0.8, 0.5555555555555556, 0.8888888888888888, 0.7777777777777778, 0.6666666666666666, 0.4444444444444444 ]
- Mean = 0.6541666666666667
- Standard deviation = 0.1467169000675522

### balanced_accuracy
- Scores = [ 0.6875, 0.75, 0.875, 0.7142857142857143, 0.9285714285714286, 0.8571428571428572, 0.7857142857142857, 0.6875 ]
- Mean = 0.7857142857142857
- Standard deviation = 0.08598821555472422

### f1
- Scores = [ 0.4444444444444445, 0.5, 0.6666666666666666, 0.5, 0.8, 0.6666666666666666, 0.5714285714285715, 0.2857142857142857 ]
- Mean = 0.5543650793650794
- Standard deviation = 0.14833150737323825

### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 37 | 23 |
| Actual Positive | 2 | 13 |

      