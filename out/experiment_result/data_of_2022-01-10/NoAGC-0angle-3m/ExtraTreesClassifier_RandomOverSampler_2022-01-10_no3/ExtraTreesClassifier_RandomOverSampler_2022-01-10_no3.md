# ExtraTreesClassifier_RandomOverSampler_2022-01-10_no3
## Constants
- CSV_PATH = ../out/csv/experiment
- OUTPUT_PATH = ../out/experiment_result/data_of_2022-01-10/NoAGC-0angle-3m
- FEATURE_ATTRBS = ['low_power', 'high_power', 'hlbr', 'coe1[0]', 'coe1[1]', 'coe3[0]', 'coe3[1]', 'coe3[2]', 'coe3[3]', 'ratio_max_to_10ms_ave_peaks', 'ratio_max_to_9th_ave_peaks', 'ac_std', 'ac_auc', 'diff_std', 'diff_auc', 'srmr', 'gp_max_val_std', 'gp_max_val_range', 'gp_max_val_min', 'gp_max_val_max', 'gp_max_val_mean', 'gp_max_ix_std', 'gp_max_ix_range', 'gp_max_ix_min', 'gp_max_ix_max', 'gp_max_ix_mean', 'gp_auc_std', 'gp_auc_range', 'gp_auc_min', 'gp_auc_max', 'gp_auc_mean', 'tdoa_std', 'tdoa_range', 'tdoa_min', 'tdoa_max', 'tdoa_mean']
- LABEL_ATTRB = ['facing']
- FACING_DOV_ANGLES = [1]
- NCV = 8
- SCORING = ['accuracy', 'balanced_accuracy', 'f1']
- REFIT_SCORING = balanced_accuracy
- PARAM_GRID = [{'est__n_estimators': [50, 100, 150, 200, 300], 'est__min_samples_split': [2, 5, 10], 'est__min_samples_leaf': [1, 5, 10], 'est__max_features': ['sqrt', 'log2', None], 'est__bootstrap': [False], 'est__n_jobs': [-1], 'est__random_state': [42], 'est__max_samples': [0.01, 0.5, 0.09]}, {'est__n_estimators': [50, 100, 150, 200, 300], 'est__min_samples_split': [2, 5, 10], 'est__min_samples_leaf': [1, 5, 10], 'est__max_features': ['sqrt', 'log2', None], 'est__bootstrap': [True], 'est__oob_score': [True, False], 'est__n_jobs': [-1], 'est__random_state': [42], 'est__max_samples': [0.01, 0.5, 0.09]}]
- TRAIN_SET_SESSION = ['trial1', 'trial2']
- TEST_SET_SESSION = ['trial3', 'trial4', 'trial5']
- DISTANCE = [3]
- AGC_STATUS = ['NoAGC']

## Loaded CSV
- 2022-01-10_raspi_48000Hz_w1_N2^12_overlap80.csv

## Estimator
### Type
- resampler = RandomOverSampler
- estimator = ExtraTreesClassifier

### Arguments for hyperparameter search
- resampler = RandomOverSampler
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
	- shrinkage = None
	- n_features_in_ = 36
	- sampling_strategy_ = OrderedDict([(1, 30)])
	- shrinkage_ = None
	- sample_indices_ = [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23
 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47
 48 49 36 13 37 24 36 49 12 36 37 24 13 37 37 12 25 24  1 37 25  1 24  0
 49 25 48  0 49 12 36 13]

- best_estimator
	- base_estimator = ExtraTreeClassifier()
	- n_estimators = 50
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
	- min_samples_split = 10
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
	- oob_decision_function_ = [[0.11737542 0.88262458]
 [0.22623437 0.77376563]
 [0.27429572 0.72570428]
 [0.50671296 0.49328704]
 [0.92679543 0.07320457]
 [0.92671128 0.07328872]
 [0.9865814  0.0134186 ]
 [0.97264957 0.02735043]
 [0.98241701 0.01758299]
 [0.99691358 0.00308642]
 [0.73325563 0.26674437]
 [0.77915331 0.22084669]
 [0.17998985 0.82001015]
 [0.23450553 0.76549447]
 [0.23371443 0.76628557]
 [0.18158541 0.81841459]
 [0.93909465 0.06090535]
 [0.91051757 0.08948243]
 [0.94192666 0.05807334]
 [0.94426523 0.05573477]
 [0.92291667 0.07708333]
 [0.94380952 0.05619048]
 [0.70244478 0.29755522]
 [0.93140524 0.06859476]
 [0.06202553 0.93797447]
 [0.04126984 0.95873016]
 [0.72030073 0.27969927]
 [0.53842055 0.46157945]
 [0.95143745 0.04856255]
 [1.         0.        ]
 [0.98787879 0.01212121]
 [1.         0.        ]
 [0.99666667 0.00333333]
 [0.98115079 0.01884921]
 [0.91234144 0.08765856]
 [0.83181442 0.16818558]
 [0.23659832 0.76340168]
 [0.23701378 0.76298622]
 [0.30401355 0.69598645]
 [0.52088938 0.47911062]
 [0.93181818 0.06818182]
 [0.95238095 0.04761905]
 [0.96066434 0.03933566]
 [0.94819159 0.05180841]
 [0.96599822 0.03400178]
 [0.98927739 0.01072261]
 [0.91122248 0.08877752]
 [0.97189685 0.02810315]
 [0.20733675 0.79266325]
 [0.15950044 0.84049956]
 [0.1704009  0.8295991 ]
 [0.18685254 0.81314746]
 [0.2508347  0.7491653 ]
 [0.0777417  0.9222583 ]
 [0.2046358  0.7953642 ]
 [0.15875143 0.84124857]
 [0.12926646 0.87073354]
 [0.22114616 0.77885384]
 [0.17771447 0.82228553]
 [0.05999744 0.94000256]
 [0.23781371 0.76218629]
 [0.25863442 0.74136558]
 [0.21488341 0.78511659]
 [0.16664932 0.83335068]
 [0.07428571 0.92571429]
 [0.0712585  0.9287415 ]
 [0.2328108  0.7671892 ]
 [0.20095705 0.79904295]
 [0.04585253 0.95414747]
 [0.20310282 0.79689718]
 [0.08575838 0.91424162]
 [0.12515372 0.87484628]
 [0.16694727 0.83305273]
 [0.02663139 0.97336861]
 [0.23213048 0.76786952]
 [0.13141115 0.86858885]
 [0.15993934 0.84006066]
 [0.20263741 0.79736259]
 [0.15206532 0.84793468]
 [0.22828893 0.77171107]]
	- oob_score_ = 0.95

#### Importance of features
- gp_auc_min = 0.1377082037800897
- gp_auc_max = 0.13536344895997576
- gp_max_val_max = 0.12187974898572614
- gp_max_val_mean = 0.10190814805089479
- gp_auc_mean = 0.07505362715048258
- gp_max_val_min = 0.07050658612658538
- hlbr = 0.047889785111209365
- srmr = 0.030400936342933366
- gp_max_ix_min = 0.02219804582770506
- tdoa_range = 0.02217668793450975
- gp_max_val_std = 0.020533898867089947
- ratio_max_to_10ms_ave_peaks = 0.01975220129567001
- gp_max_ix_range = 0.018845030390126263
- gp_max_ix_std = 0.017347791145888823
- tdoa_mean = 0.015979647486625885
- tdoa_std = 0.014794292404186464
- coe3[3] = 0.01292907226418891
- ac_auc = 0.012588117578877164
- ac_std = 0.012570837020294967
- diff_std = 0.011733887970077583
- coe1[1] = 0.011618925160498363
- high_power = 0.010901505097647592
- coe1[0] = 0.008263713300595554
- low_power = 0.008134145024188353
- tdoa_max = 0.006399950115358235
- gp_max_ix_mean = 0.00606147552658146
- gp_auc_std = 0.005919933665996068
- gp_max_val_range = 0.005777338075741115
- diff_auc = 0.004963020522543124
- tdoa_min = 0.004197426198080007
- gp_auc_range = 0.0024223422725351915
- ratio_max_to_9th_ave_peaks = 0.0023788303200067908
- gp_max_ix_max = 0.000704744314737825
- coe3[2] = 9.665571235260079e-05
- coe3[0] = 0.0
- coe3[1] = 0.0

## Evaluation
cv = 8
### accuracy
- Scores = [ 0.7, 0.7, 1.0, 0.7777777777777778, 1.0, 0.8888888888888888, 0.8888888888888888, 1.0 ]
- Mean = 0.8694444444444445
- Standard deviation = 0.1213033642272114

### balanced_accuracy
- Scores = [ 0.8125, 0.8125, 1.0, 0.8571428571428572, 1.0, 0.9285714285714286, 0.9285714285714286, 1.0 ]
- Mean = 0.9174107142857143
- Standard deviation = 0.0761222897543747

### f1
- Scores = [ 0.5714285714285715, 0.5714285714285715, 1.0, 0.6666666666666666, 1.0, 0.8, 0.8, 1.0 ]
- Mean = 0.8011904761904762
- Standard deviation = 0.17401732522498456

### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 51 | 9 |
| Actual Positive | 3 | 12 |

      