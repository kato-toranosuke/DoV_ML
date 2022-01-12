# ExtraTreesClassifier_SMOTEENN_2022-01-10_no5
## Constants
- CSV_PATH = ../out/csv/experiment
- OUTPUT_PATH = ../out/experiment_result/data_of_2022-01-10/NoAGC-0angle-under5m
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
- AGC_STATUS = ['NoAGC']

## Loaded CSV
- 2022-01-10_raspi_48000Hz_w1_N2^12_overlap80.csv

## Estimator
### Type
- resampler = SMOTEENN
- estimator = ExtraTreesClassifier

### Arguments for hyperparameter search
- resampler = SMOTEENN
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
	- enn = None
	- n_jobs = -1
	- n_features_in_ = 36
	- sampling_strategy_ = auto
	- smote_ = SMOTE(n_jobs=-1, random_state=42)
	- enn_ = EditedNearestNeighbours(n_jobs=-1, sampling_strategy='all')

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
	- max_samples = 0.09
	- criterion = gini
	- max_depth = None
	- min_samples_split = 2
	- min_samples_leaf = 1
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
	- oob_decision_function_ = [[0.88764045 0.11235955]
 [0.49462366 0.50537634]
 [0.68965517 0.31034483]
 [0.84946237 0.15053763]
 [0.30681818 0.69318182]
 [0.76842105 0.23157895]
 [0.42045455 0.57954545]
 [0.38888889 0.61111111]
 [0.60240964 0.39759036]
 [0.7311828  0.2688172 ]
 [0.76842105 0.23157895]
 [0.62365591 0.37634409]
 [0.61956522 0.38043478]
 [0.35632184 0.64367816]
 [0.71578947 0.28421053]
 [0.35164835 0.64835165]
 [0.30107527 0.69892473]
 [0.28723404 0.71276596]
 [0.79761905 0.20238095]
 [0.80898876 0.19101124]
 [0.67708333 0.32291667]
 [0.69565217 0.30434783]
 [0.58426966 0.41573034]
 [0.61538462 0.38461538]
 [0.33333333 0.66666667]
 [0.79347826 0.20652174]
 [0.84946237 0.15053763]
 [0.36956522 0.63043478]
 [0.90322581 0.09677419]
 [0.89130435 0.10869565]
 [0.87234043 0.12765957]
 [0.35483871 0.64516129]
 [0.88172043 0.11827957]
 [0.81318681 0.18681319]
 [0.73033708 0.26966292]
 [0.27956989 0.72043011]
 [0.32183908 0.67816092]
 [0.27956989 0.72043011]
 [0.28888889 0.71111111]
 [0.43820225 0.56179775]
 [0.36666667 0.63333333]
 [0.42045455 0.57954545]
 [0.4        0.6       ]
 [0.22727273 0.77272727]
 [0.30851064 0.69148936]
 [0.32608696 0.67391304]
 [0.37777778 0.62222222]
 [0.27659574 0.72340426]
 [0.41860465 0.58139535]
 [0.31818182 0.68181818]
 [0.29213483 0.70786517]
 [0.38541667 0.61458333]
 [0.24731183 0.75268817]
 [0.2967033  0.7032967 ]
 [0.2826087  0.7173913 ]
 [0.24731183 0.75268817]
 [0.36781609 0.63218391]
 [0.26373626 0.73626374]
 [0.33707865 0.66292135]
 [0.28723404 0.71276596]
 [0.27058824 0.72941176]
 [0.42045455 0.57954545]
 [0.25       0.75      ]
 [0.34065934 0.65934066]
 [0.27368421 0.72631579]
 [0.36170213 0.63829787]
 [0.31111111 0.68888889]
 [0.21276596 0.78723404]
 [0.25531915 0.74468085]
 [0.31818182 0.68181818]
 [0.27272727 0.72727273]
 [0.36363636 0.63636364]
 [0.34065934 0.65934066]
 [0.32989691 0.67010309]]
	- oob_score_ = 0.8513513513513513

#### Importance of features
- gp_auc_mean = 0.09043367346938776
- gp_max_val_min = 0.07665816326530611
- hlbr = 0.07490079365079365
- gp_auc_max = 0.06666666666666667
- gp_max_val_max = 0.06577380952380951
- gp_auc_min = 0.056760204081632654
- gp_max_val_mean = 0.03714569160997732
- ratio_max_to_9th_ave_peaks = 0.03537414965986395
- tdoa_mean = 0.034863945578231297
- gp_max_ix_mean = 0.03486394557823129
- tdoa_range = 0.030612244897959183
- gp_max_val_std = 0.027168367346938775
- high_power = 0.026842403628117913
- low_power = 0.02665816326530612
- coe3[3] = 0.025056689342403626
- srmr = 0.024872448979591837
- ac_std = 0.023214285714285708
- gp_max_val_range = 0.020918367346938773
- ac_auc = 0.02040816326530612
- coe3[2] = 0.02032312925170068
- gp_auc_std = 0.019515306122448978
- ratio_max_to_10ms_ave_peaks = 0.019019274376417233
- diff_std = 0.018920068027210885
- tdoa_std = 0.01802721088435374
- gp_max_ix_range = 0.0179421768707483
- gp_auc_range = 0.01594387755102041
- gp_max_ix_std = 0.014965986394557823
- diff_auc = 0.014370748299319726
- coe1[1] = 0.014158163265306122
- tdoa_max = 0.011678004535147392
- gp_max_ix_max = 0.011479591836734694
- gp_max_ix_min = 0.002976190476190476
- tdoa_min = 0.001488095238095238
- coe1[0] = 0.0
- coe3[0] = 0.0
- coe3[1] = 0.0

## Evaluation
cv = 8
### accuracy
- Scores = [ 0.6896551724137931, 0.6428571428571429, 0.7857142857142857, 0.5357142857142857, 0.8214285714285714, 0.5357142857142857, 0.6428571428571429, 0.8571428571428571 ]
- Mean = 0.6888854679802956
- Standard deviation = 0.11533357666406116

### balanced_accuracy
- Scores = [ 0.8043478260869565, 0.7121212121212122, 0.7424242424242424, 0.7045454545454546, 0.7651515151515151, 0.4826086956521739, 0.7826086956521738, 0.6 ]
- Mean = 0.6992259552042162
- Standard deviation = 0.10073416293754972

### f1
- Scores = [ 0.5714285714285715, 0.5, 0.5714285714285715, 0.4799999999999999, 0.6153846153846153, 0.23529411764705882, 0.5, 0.33333333333333337 ]
- Mean = 0.47585865115276876
- Standard deviation = 0.12098669102262131

### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 126 | 54 |
| Actual Positive | 13 | 32 |

      