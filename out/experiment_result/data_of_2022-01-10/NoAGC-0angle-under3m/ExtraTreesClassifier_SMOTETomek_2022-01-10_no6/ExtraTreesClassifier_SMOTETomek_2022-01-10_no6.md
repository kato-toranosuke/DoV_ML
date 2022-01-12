# ExtraTreesClassifier_SMOTETomek_2022-01-10_no6
## Constants
- CSV_PATH = ../out/csv/experiment
- OUTPUT_PATH = ../out/experiment_result/data_of_2022-01-10/NoAGC-0angle-under3m
- FEATURE_ATTRBS = ['low_power', 'high_power', 'hlbr', 'coe1[0]', 'coe1[1]', 'coe3[0]', 'coe3[1]', 'coe3[2]', 'coe3[3]', 'ratio_max_to_10ms_ave_peaks', 'ratio_max_to_9th_ave_peaks', 'ac_std', 'ac_auc', 'diff_std', 'diff_auc', 'srmr', 'gp_max_val_std', 'gp_max_val_range', 'gp_max_val_min', 'gp_max_val_max', 'gp_max_val_mean', 'gp_max_ix_std', 'gp_max_ix_range', 'gp_max_ix_min', 'gp_max_ix_max', 'gp_max_ix_mean', 'gp_auc_std', 'gp_auc_range', 'gp_auc_min', 'gp_auc_max', 'gp_auc_mean', 'tdoa_std', 'tdoa_range', 'tdoa_min', 'tdoa_max', 'tdoa_mean']
- LABEL_ATTRB = ['facing']
- FACING_DOV_ANGLES = [1]
- NCV = 8
- SCORING = ['accuracy', 'balanced_accuracy', 'f1']
- REFIT_SCORING = balanced_accuracy
- PARAM_GRID = [{'est__n_estimators': [50, 100, 150, 200, 300], 'est__min_samples_split': [2, 5, 10], 'est__min_samples_leaf': [1, 5, 10], 'est__max_features': ['sqrt', 'log2', None], 'est__bootstrap': [False], 'est__n_jobs': [-1], 'est__random_state': [42], 'est__max_samples': [0.01, 0.5, 0.09]}, {'est__n_estimators': [50, 100, 150, 200, 300], 'est__min_samples_split': [2, 5, 10], 'est__min_samples_leaf': [1, 5, 10], 'est__max_features': ['sqrt', 'log2', None], 'est__bootstrap': [True], 'est__oob_score': [True, False], 'est__n_jobs': [-1], 'est__random_state': [42], 'est__max_samples': [0.01, 0.5, 0.09]}]
- TRAIN_SET_SESSION = ['trial1', 'trial2']
- TEST_SET_SESSION = ['trial3', 'trial4', 'trial5']
- DISTANCE = [1, 3]
- AGC_STATUS = ['NoAGC']

## Loaded CSV
- 2022-01-10_raspi_48000Hz_w1_N2^12_overlap80.csv

## Estimator
### Type
- resampler = SMOTETomek
- estimator = ExtraTreesClassifier

### Arguments for hyperparameter search
- resampler = SMOTETomek
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
	- smote = None
	- tomek = None
	- n_jobs = -1
	- n_features_in_ = 36
	- sampling_strategy_ = auto
	- smote_ = SMOTE(n_jobs=-1, random_state=42)
	- tomek_ = TomekLinks(n_jobs=-1, sampling_strategy='all')

- best_estimator
	- base_estimator = ExtraTreeClassifier()
	- n_estimators = 150
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
	- max_features = None
	- max_leaf_nodes = None
	- min_impurity_decrease = 0.0
	- ccp_alpha = 0.0
	- n_features_in_ = 36
	- n_outputs_ = 1
	- classes_ = [0 1]
	- n_classes_ = 2
	- base_estimator_ = ExtraTreeClassifier()
	- oob_decision_function_ = [[0.13584346 0.86415654]
 [0.11998314 0.88001686]
 [0.25327    0.74673   ]
 [0.69239758 0.30760242]
 [0.6737387  0.3262613 ]
 [0.96850499 0.03149501]
 [0.97527778 0.02472222]
 [0.99307359 0.00692641]
 [0.98334998 0.01665002]
 [0.10608854 0.89391146]
 [0.26386418 0.73613582]
 [0.77880946 0.22119054]
 [0.97804072 0.02195928]
 [0.96117342 0.03882658]
 [1.         0.        ]
 [0.99810606 0.00189394]
 [0.40673312 0.59326688]
 [0.25628774 0.74371226]
 [0.36312674 0.63687326]
 [0.3589911  0.6410089 ]
 [0.42199915 0.57800085]
 [0.88285469 0.11714531]
 [0.70839896 0.29160104]
 [0.96397569 0.03602431]
 [0.9355042  0.0644958 ]
 [0.32552819 0.67447181]
 [0.3347424  0.6652576 ]
 [0.96638258 0.03361742]
 [0.97240134 0.02759866]
 [0.98501684 0.01498316]
 [1.         0.        ]
 [0.44826491 0.55173509]
 [0.45377741 0.54622259]
 [0.49615671 0.50384329]
 [0.37002089 0.62997911]
 [0.70381861 0.29618139]
 [0.9512465  0.0487535 ]
 [0.94792994 0.05207006]
 [0.65207626 0.34792374]
 [0.08541863 0.91458137]
 [0.06235775 0.93764225]
 [0.97561778 0.02438222]
 [0.95530168 0.04469832]
 [0.79732088 0.20267912]
 [0.41752744 0.58247256]
 [0.47522661 0.52477339]
 [0.30820255 0.69179745]
 [0.33566318 0.66433682]
 [0.99575672 0.00424328]
 [1.         0.        ]
 [0.95413853 0.04586147]
 [0.98367331 0.01632669]
 [0.54068899 0.45931101]
 [0.34456251 0.65543749]
 [0.41245679 0.58754321]
 [0.51930198 0.48069802]
 [0.61681829 0.38318171]
 [0.94386338 0.05613662]
 [1.         0.        ]
 [0.65063786 0.34936214]
 [0.77189524 0.22810476]
 [0.61961606 0.38038394]
 [0.99656085 0.00343915]
 [0.99786096 0.00213904]
 [0.99831933 0.00168067]
 [0.99681691 0.00318309]
 [0.94462398 0.05537602]
 [0.78615303 0.21384697]
 [0.84804962 0.15195038]
 [0.26113702 0.73886298]
 [0.0847114  0.9152886 ]
 [0.25481266 0.74518734]
 [0.33038596 0.66961404]
 [0.18529457 0.81470543]
 [0.09655601 0.90344399]
 [0.12382057 0.87617943]
 [0.33478229 0.66521771]
 [0.21616472 0.78383528]
 [0.15429538 0.84570462]
 [0.35823528 0.64176472]
 [0.33649666 0.66350334]
 [0.11216365 0.88783635]
 [0.01932066 0.98067934]
 [0.04932622 0.95067378]
 [0.23893816 0.76106184]
 [0.34030703 0.65969297]
 [0.18042199 0.81957801]
 [0.04419476 0.95580524]
 [0.47548413 0.52451587]
 [0.37073879 0.62926121]
 [0.03737651 0.96262349]
 [0.25581317 0.74418683]
 [0.06608064 0.93391936]
 [0.06009361 0.93990639]
 [0.24690012 0.75309988]
 [0.11010823 0.88989177]
 [0.28093687 0.71906313]
 [0.06196463 0.93803537]
 [0.36905332 0.63094668]
 [0.20499867 0.79500133]
 [0.15497752 0.84502248]
 [0.0690767  0.9309233 ]
 [0.15376761 0.84623239]
 [0.28537949 0.71462051]
 [0.10361681 0.89638319]
 [0.03955107 0.96044893]
 [0.22976312 0.77023688]
 [0.3594164  0.6405836 ]
 [0.01640899 0.98359101]
 [0.02178974 0.97821026]
 [0.09439956 0.90560044]
 [0.12291184 0.87708816]]
	- oob_score_ = 0.9017857142857143

#### Importance of features
- gp_max_val_min = 0.1837662408578201
- gp_auc_min = 0.14384513481958866
- gp_auc_mean = 0.1385465132134334
- gp_max_val_mean = 0.12051425323608016
- gp_auc_max = 0.07507583337281223
- gp_max_val_max = 0.0642416235912037
- tdoa_max = 0.052975506746839075
- gp_max_ix_max = 0.04859371863291099
- srmr = 0.03887237352127605
- hlbr = 0.015587445372577719
- tdoa_range = 0.015549771601311295
- gp_max_ix_mean = 0.012001290789878754
- gp_max_ix_range = 0.008114723617435607
- ac_auc = 0.00776665780891125
- gp_max_val_std = 0.006458902955902166
- tdoa_min = 0.005693495569885292
- gp_max_ix_std = 0.005051624628695496
- coe3[3] = 0.004960265891481637
- tdoa_std = 0.00491926148060044
- gp_max_ix_min = 0.0046423311067462164
- low_power = 0.004286614263783447
- ac_std = 0.003976561616991678
- tdoa_mean = 0.003914591019166438
- diff_auc = 0.003882889869855382
- coe1[1] = 0.003842865918358375
- gp_max_val_range = 0.0036831450439353697
- ratio_max_to_10ms_ave_peaks = 0.003569495577417742
- ratio_max_to_9th_ave_peaks = 0.0035291724959885013
- gp_auc_range = 0.0033014022223006347
- high_power = 0.003020779487361878
- gp_auc_std = 0.0029245089236966584
- coe1[0] = 0.0018855092575156128
- coe3[2] = 0.0007290023063753396
- diff_std = 0.0002764931818626658
- coe3[0] = 0.0
- coe3[1] = 0.0

## Evaluation
cv = 8
### accuracy
- Scores = [ 0.6842105263157895, 0.7368421052631579, 0.9473684210526315, 0.7894736842105263, 0.8421052631578947, 0.8421052631578947, 0.6666666666666666, 0.8333333333333334 ]
- Mean = 0.7927631578947368
- Standard deviation = 0.08749285465262997

### balanced_accuracy
- Scores = [ 0.8, 0.7416666666666667, 0.9666666666666667, 0.8666666666666667, 0.625, 0.9, 0.5333333333333333, 0.7666666666666666 ]
- Mean = 0.7749999999999999
- Standard deviation = 0.13391798899990165

### f1
- Scores = [ 0.5714285714285715, 0.5454545454545454, 0.888888888888889, 0.6666666666666666, 0.4, 0.7272727272727273, 0.25, 0.5714285714285715 ]
- Mean = 0.5776424963924964
- Standard deviation = 0.1827596022127352

### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 91 | 29 |
| Actual Positive | 6 | 24 |

      