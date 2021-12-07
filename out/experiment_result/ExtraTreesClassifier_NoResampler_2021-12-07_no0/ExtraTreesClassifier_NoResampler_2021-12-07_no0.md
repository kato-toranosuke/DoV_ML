# ExtraTreesClassifier_NoResampler_2021-12-07_no0
## Constants
- CSV_PATH = ../out/csv/experiment
- OUTPUT_PATH = ../out/experiment_result
- FEATURE_ATTRBS = ['low_power', 'high_power', 'hlbr', 'coe1[0]', 'coe1[1]', 'coe3[0]', 'coe3[1]', 'coe3[2]', 'coe3[3]', 'ratio_max_to_10ms_ave_peaks', 'ratio_max_to_9th_ave_peaks', 'ac_std', 'ac_auc', 'diff_std', 'diff_auc', 'srmr', 'gp_max_val_std', 'gp_max_val_range', 'gp_max_val_min', 'gp_max_val_max', 'gp_max_val_mean', 'gp_max_ix_std', 'gp_max_ix_range', 'gp_max_ix_min', 'gp_max_ix_max', 'gp_max_ix_mean', 'gp_auc_std', 'gp_auc_range', 'gp_auc_min', 'gp_auc_max', 'gp_auc_mean', 'tdoa_std', 'tdoa_range', 'tdoa_min', 'tdoa_max', 'tdoa_mean']
- LABEL_ATTRB = ['dov_angle']
- FACING_DOV_ANGLES = [0, 45, 315]
- NCV = 8
- SCORING = ['accuracy', 'balanced_accuracy', 'f1']
- REFIT_SCORING = balanced_accuracy
- PARAM_GRID = [{'est__n_estimators': [100, 500, 1000], 'est__min_samples_split': [2, 5, 10], 'est__min_samples_leaf': [1, 5, 10], 'est__max_features': ['sqrt', 'log2', None], 'est__bootstrap': [False], 'est__n_jobs': [-1], 'est__random_state': [42], 'est__max_samples': [0.01, 0.5, 0.09]}, {'est__n_estimators': [100, 500, 1000], 'est__min_samples_split': [2, 5, 10], 'est__min_samples_leaf': [1, 5, 10], 'est__max_features': ['sqrt', 'log2', None], 'est__bootstrap': [True], 'est__oob_score': [True, False], 'est__n_jobs': [-1], 'est__random_state': [42], 'est__max_samples': [0.01, 0.5, 0.09]}]
- TRAIN_SET_SESSION = ['trial1']
- TEST_SET_SESSION = ['trial2', 'trial3']

## Loaded CSV
- 2021-12-01_mac_48000Hz_w1_N2^12_overlap80.csv

## Estimator
### Type
- resampler = NoResampler
- estimator = ExtraTreesClassifier

### Arguments for hyperparameter search
- resampler = NoResampler
- estimator = ExtraTreesClassifier
- param_grid = 
	- {'est__n_estimators': [100, 500, 1000], 'est__min_samples_split': [2, 5, 10], 'est__min_samples_leaf': [1, 5, 10], 'est__max_features': ['sqrt', 'log2', None], 'est__bootstrap': [False], 'est__n_jobs': [-1], 'est__random_state': [42], 'est__max_samples': [0.01, 0.5, 0.09]}
	- {'est__n_estimators': [100, 500, 1000], 'est__min_samples_split': [2, 5, 10], 'est__min_samples_leaf': [1, 5, 10], 'est__max_features': ['sqrt', 'log2', None], 'est__bootstrap': [True], 'est__oob_score': [True, False], 'est__n_jobs': [-1], 'est__random_state': [42], 'est__max_samples': [0.01, 0.5, 0.09]}

- scoring = ['accuracy', 'balanced_accuracy', 'f1']
- refit = balanced_accuracy
- cv = 8

### Parameters of the best estimator
#### The best hyper-parameters
- best_resampler

- best_estimator
	- base_estimator = ExtraTreeClassifier()
	- n_estimators = 100
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
	- min_samples_split = 10
	- min_samples_leaf = 1
	- min_weight_fraction_leaf = 0.0
	- max_features = log2
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
	- oob_decision_function_ = [[0.12275553 0.87724447]
 [0.27384428 0.72615572]
 [0.63380718 0.36619282]
 [0.7725634  0.2274366 ]
 [0.82292208 0.17707792]
 [0.54066924 0.45933076]
 [0.3022973  0.6977027 ]
 [0.20326859 0.79673141]
 [0.1193423  0.8806577 ]
 [0.30975817 0.69024183]
 [0.76818515 0.23181485]
 [0.78861134 0.21138866]
 [0.84575716 0.15424284]
 [0.75026918 0.24973082]
 [0.3801292  0.6198708 ]
 [0.12709096 0.87290904]
 [0.1975018  0.8024982 ]
 [0.2699922  0.7300078 ]
 [0.55717533 0.44282467]
 [0.83289021 0.16710979]
 [0.92775712 0.07224288]
 [0.73694972 0.26305028]
 [0.19598928 0.80401072]
 [0.39582826 0.60417174]
 [0.35798363 0.64201637]
 [0.62540357 0.37459643]
 [0.68355146 0.31644854]
 [0.9703594  0.0296406 ]
 [0.67084067 0.32915933]
 [0.97212067 0.02787933]
 [0.29166185 0.70833815]
 [0.28627848 0.71372152]
 [0.27085312 0.72914688]
 [0.55101971 0.44898029]
 [0.84763336 0.15236664]
 [0.85520772 0.14479228]
 [0.93444076 0.06555924]
 [0.85986665 0.14013335]
 [0.67523502 0.32476498]
 [0.17853021 0.82146979]
 [0.3072059  0.6927941 ]
 [0.31724062 0.68275938]
 [0.55588422 0.44411578]
 [0.94708305 0.05291695]
 [0.64049363 0.35950637]
 [0.90270971 0.09729029]
 [0.75221755 0.24778245]
 [0.47785129 0.52214871]
 [0.31416603 0.68583397]
 [0.43011413 0.56988587]
 [0.86778015 0.13221985]
 [0.94650039 0.05349961]
 [0.7768933  0.2231067 ]
 [0.95495956 0.04504044]
 [0.86282051 0.13717949]
 [0.2466782  0.7533218 ]
 [0.3826857  0.6173143 ]
 [0.80924145 0.19075855]
 [0.79842406 0.20157594]
 [0.95376908 0.04623092]
 [0.84552849 0.15447151]
 [0.82102949 0.17897051]
 [0.7885622  0.2114378 ]
 [0.51888394 0.48111606]
 [0.65991014 0.34008986]
 [0.86449099 0.13550901]
 [0.93691191 0.06308809]
 [0.79284271 0.20715729]
 [0.91431273 0.08568727]
 [0.95092403 0.04907597]
 [0.77577459 0.22422541]
 [0.55110376 0.44889624]]
	- oob_score_ = 0.8472222222222222

#### Importance of features
- diff_std = 0.06978472161312613
- gp_max_val_min = 0.051436031726250636
- coe1[0] = 0.0503384802182411
- diff_auc = 0.04918116867406726
- gp_max_ix_mean = 0.04602234520102398
- low_power = 0.04309153132739803
- gp_auc_mean = 0.04235815191682959
- gp_auc_std = 0.041021861926465085
- gp_max_val_mean = 0.040574975195704105
- gp_auc_max = 0.04026797345412673
- high_power = 0.039943953490766355
- gp_auc_min = 0.03676041821300137
- gp_max_val_range = 0.03173220448990465
- gp_max_ix_std = 0.03155531101367253
- hlbr = 0.030925798072696
- tdoa_mean = 0.029749278898772234
- gp_max_val_max = 0.029023324355475427
- gp_max_val_std = 0.028907285087133004
- tdoa_std = 0.028798995277794035
- gp_auc_range = 0.028722983893880952
- coe1[1] = 0.02645045712009068
- srmr = 0.02351897179843004
- gp_max_ix_min = 0.022550929407391382
- tdoa_range = 0.021620186217725636
- coe3[3] = 0.021491829803871734
- tdoa_max = 0.017313902576359952
- ratio_max_to_10ms_ave_peaks = 0.01327933624476305
- gp_max_ix_range = 0.012662899696935766
- tdoa_min = 0.012404619795847874
- coe3[2] = 0.011697937043714012
- ac_std = 0.010002110491164487
- ratio_max_to_9th_ave_peaks = 0.007179778023407481
- gp_max_ix_max = 0.005770824848324924
- ac_auc = 0.0038594228856436243
- coe3[0] = 0.0
- coe3[1] = 0.0

## Evaluation
cv = 8
### accuracy
- Scores = [ 0.8888888888888888, 0.7777777777777778, 1.0, 0.8888888888888888, 0.8888888888888888, 0.8333333333333334, 0.8888888888888888, 0.9444444444444444 ]
- Mean = 0.8888888888888888
- Standard deviation = 0.06211299937499415

### balanced_accuracy
- Scores = [ 0.9090909090909092, 0.7402597402597402, 1.0, 0.8571428571428572, 0.9090909090909092, 0.8376623376623377, 0.875, 0.9166666666666667 ]
- Mean = 0.8806141774891775
- Standard deviation = 0.07009034842624096

### f1
- Scores = [ 0.8750000000000001, 0.6666666666666666, 1.0, 0.8333333333333333, 0.8750000000000001, 0.7999999999999999, 0.8333333333333334, 0.9090909090909091 ]
- Mean = 0.8490530303030304
- Standard deviation = 0.08937367355029735

### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 82 | 8 |
| Actual Positive | 8 | 46 |

      