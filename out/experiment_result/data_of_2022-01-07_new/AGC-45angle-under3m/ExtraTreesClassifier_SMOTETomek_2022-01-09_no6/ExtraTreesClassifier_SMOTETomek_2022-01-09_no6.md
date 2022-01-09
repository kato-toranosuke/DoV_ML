# ExtraTreesClassifier_SMOTETomek_2022-01-09_no6
## Constants
- CSV_PATH = ../out/csv/experiment
- OUTPUT_PATH = ../out/experiment_result/data_of_2022-01-07_new/AGC-45angle-under3m
- FEATURE_ATTRBS = ['low_power', 'high_power', 'hlbr', 'coe1[0]', 'coe1[1]', 'coe3[0]', 'coe3[1]', 'coe3[2]', 'coe3[3]', 'ratio_max_to_10ms_ave_peaks', 'ratio_max_to_9th_ave_peaks', 'ac_std', 'ac_auc', 'diff_std', 'diff_auc', 'srmr', 'gp_max_val_std', 'gp_max_val_range', 'gp_max_val_min', 'gp_max_val_max', 'gp_max_val_mean', 'gp_max_ix_std', 'gp_max_ix_range', 'gp_max_ix_min', 'gp_max_ix_max', 'gp_max_ix_mean', 'gp_auc_std', 'gp_auc_range', 'gp_auc_min', 'gp_auc_max', 'gp_auc_mean', 'tdoa_std', 'tdoa_range', 'tdoa_min', 'tdoa_max', 'tdoa_mean']
- LABEL_ATTRB = ['facing2']
- FACING_DOV_ANGLES = [1, 2]
- NCV = 8
- SCORING = ['accuracy', 'balanced_accuracy', 'f1']
- REFIT_SCORING = balanced_accuracy
- PARAM_GRID = [{'est__n_estimators': [50, 100, 150, 200, 300], 'est__min_samples_split': [2, 5, 10], 'est__min_samples_leaf': [1, 5, 10], 'est__max_features': ['sqrt', 'log2', None], 'est__bootstrap': [False], 'est__n_jobs': [-1], 'est__random_state': [42], 'est__max_samples': [0.01, 0.5, 0.09]}, {'est__n_estimators': [50, 100, 150, 200, 300], 'est__min_samples_split': [2, 5, 10], 'est__min_samples_leaf': [1, 5, 10], 'est__max_features': ['sqrt', 'log2', None], 'est__bootstrap': [True], 'est__oob_score': [True, False], 'est__n_jobs': [-1], 'est__random_state': [42], 'est__max_samples': [0.01, 0.5, 0.09]}]
- TRAIN_SET_SESSION = ['trial1', 'trial2']
- TEST_SET_SESSION = ['trial3', 'trial4', 'trial5']
- DISTANCE = [1, 3]
- AGC_STATUS = ['AGC']

## Loaded CSV
- 2021-12-27_raspi_48000Hz_w1_N2^12_overlap80_with2022-01-07.csv

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
	- min_samples_split = 5
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
	- oob_decision_function_ = [[0.14418546 0.85581454]
 [0.12354788 0.87645212]
 [0.12255504 0.87744496]
 [0.05734767 0.94265233]
 [0.99450549 0.00549451]
 [1.         0.        ]
 [0.98913043 0.01086957]
 [0.02392157 0.97607843]
 [0.07624339 0.92375661]
 [0.16283525 0.83716475]
 [0.75789474 0.24210526]
 [0.45287807 0.54712193]
 [0.99234694 0.00765306]
 [0.99329502 0.00670498]
 [0.98064516 0.01935484]
 [0.98085106 0.01914894]
 [0.20305383 0.79694617]
 [0.10766667 0.89233333]
 [0.1757526  0.8242474 ]
 [0.15478751 0.84521249]
 [0.42082119 0.57917881]
 [0.82043651 0.17956349]
 [1.         0.        ]
 [1.         0.        ]
 [0.63832473 0.36167527]
 [0.05294118 0.94705882]
 [0.07129014 0.92870986]
 [0.03023256 0.96976744]
 [0.79252101 0.20747899]
 [0.99175824 0.00824176]
 [0.98252427 0.01747573]
 [0.77932195 0.22067805]
 [0.83713768 0.16286232]
 [0.12570922 0.87429078]
 [0.11013746 0.88986254]
 [0.13760881 0.86239119]
 [0.13979201 0.86020799]
 [0.05347985 0.94652015]
 [0.09797297 0.90202703]
 [0.75890937 0.24109063]
 [0.62895356 0.37104644]
 [0.94333333 0.05666667]
 [0.45421941 0.54578059]
 [0.02956989 0.97043011]
 [0.03418367 0.96581633]
 [0.09944444 0.90055556]
 [0.07961672 0.92038328]
 [0.97395833 0.02604167]
 [0.98453608 0.01546392]
 [0.1845515  0.8154485 ]
 [0.05792079 0.94207921]
 [0.04856657 0.95143343]
 [0.09770115 0.90229885]
 [0.07556818 0.92443182]
 [0.97988506 0.02011494]
 [0.95257732 0.04742268]
 [0.02322163 0.97677837]
 [0.02420635 0.97579365]
 [0.03197674 0.96802326]
 [0.00549451 0.99450549]
 [0.0489011  0.9510989 ]
 [0.99425287 0.00574713]
 [0.98295455 0.01704545]
 [0.98823529 0.01176471]
 [0.88156863 0.11843137]
 [0.7219888  0.2780112 ]
 [0.0531746  0.9468254 ]
 [0.15268817 0.84731183]
 [0.07409733 0.92590267]
 [0.96134021 0.03865979]
 [0.99411765 0.00588235]
 [0.97721519 0.02278481]
 [0.90656146 0.09343854]
 [0.04166667 0.95833333]
 [0.95555556 0.04444444]
 [0.93112245 0.06887755]
 [0.98847518 0.01152482]
 [0.99450549 0.00549451]]
	- oob_score_ = 0.9487179487179487

#### Importance of features
- gp_max_val_min = 0.13350124427646254
- gp_max_val_mean = 0.12995467916087503
- gp_auc_mean = 0.09966706959727555
- gp_auc_min = 0.0983631511798823
- gp_auc_max = 0.09288355814639816
- gp_max_val_max = 0.07731557873340512
- srmr = 0.056413733881646506
- diff_auc = 0.05004233658077436
- diff_std = 0.0326324134230275
- ratio_max_to_10ms_ave_peaks = 0.02784772267249727
- hlbr = 0.026535470041374132
- coe1[1] = 0.017046998971665714
- tdoa_min = 0.01547699017873113
- low_power = 0.013806933027806263
- tdoa_range = 0.011400122423201707
- gp_max_ix_mean = 0.011279279982010946
- gp_max_ix_range = 0.010927370465249305
- coe1[0] = 0.010283909672188037
- high_power = 0.010037537052778689
- gp_max_val_std = 0.008427691273605948
- tdoa_std = 0.007292642990986219
- gp_auc_range = 0.006771636513006079
- coe3[3] = 0.0066336033199055535
- ac_std = 0.005783045426536612
- gp_auc_std = 0.005738395217513224
- coe3[2] = 0.005109062239886567
- gp_max_val_range = 0.004989706003468465
- tdoa_mean = 0.004672708891774576
- ratio_max_to_9th_ave_peaks = 0.004029600695825394
- gp_max_ix_std = 0.0038038853571777816
- ac_auc = 0.0034425130756179072
- gp_max_ix_min = 0.0031789350604043065
- gp_max_ix_max = 0.0025434446047985647
- tdoa_max = 0.00216702986224252
- coe3[0] = 0.0
- coe3[1] = 0.0

## Evaluation
cv = 8
### accuracy
- Scores = [ 0.8421052631578947, 1.0, 0.9473684210526315, 0.9473684210526315, 1.0, 1.0, 1.0, 1.0 ]
- Mean = 0.9671052631578947
- Standard deviation = 0.05221877587627483

### balanced_accuracy
- Scores = [ 0.8333333333333333, 1.0, 0.95, 0.9444444444444444, 1.0, 1.0, 1.0, 1.0 ]
- Mean = 0.9659722222222222
- Standard deviation = 0.054887476083931935

### f1
- Scores = [ 0.8695652173913044, 1.0, 0.9473684210526316, 0.9523809523809523, 1.0, 1.0, 1.0, 1.0 ]
- Mean = 0.971164323853111
- Standard deviation = 0.04387328281829072

### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 67 | 5 |
| Actual Positive | 1 | 77 |

      