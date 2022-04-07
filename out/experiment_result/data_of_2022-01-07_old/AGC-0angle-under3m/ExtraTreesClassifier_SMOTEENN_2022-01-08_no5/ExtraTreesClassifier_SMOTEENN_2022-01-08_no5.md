# ExtraTreesClassifier_SMOTEENN_2022-01-08_no5
## Constants
- CSV_PATH = ../out/csv/experiment
- OUTPUT_PATH = ../out/experiment_result/data_of_2022-01-07/AGC-0angle-under3m
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
- AGC_STATUS = ['AGC']

## Loaded CSV
- 2021-12-27_raspi_48000Hz_w1_N2^12_overlap80_with2022-01-07.csv

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
	- n_estimators = 150
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
	- min_samples_split = 2
	- min_samples_leaf = 1
	- min_weight_fraction_leaf = 0.0
	- max_features = None
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
	- oob_decision_function_ = [[0.64772727 0.35227273]
 [0.95049505 0.04950495]
 [0.96551724 0.03448276]
 [0.19387755 0.80612245]
 [0.25742574 0.74257426]
 [0.91578947 0.08421053]
 [0.98780488 0.01219512]
 [0.95061728 0.04938272]
 [0.96470588 0.03529412]
 [0.86597938 0.13402062]
 [0.84375    0.15625   ]
 [0.97916667 0.02083333]
 [0.97979798 0.02020202]
 [0.375      0.625     ]
 [0.78095238 0.21904762]
 [0.80612245 0.19387755]
 [0.8988764  0.1011236 ]
 [0.93478261 0.06521739]
 [0.65263158 0.34736842]
 [0.94059406 0.05940594]
 [0.45918367 0.54081633]
 [0.5        0.5       ]
 [0.13636364 0.86363636]
 [0.01098901 0.98901099]
 [0.         1.        ]
 [0.01111111 0.98888889]
 [0.04545455 0.95454545]
 [0.         1.        ]
 [0.02197802 0.97802198]
 [0.1547619  0.8452381 ]
 [0.01136364 0.98863636]
 [0.         1.        ]
 [0.04545455 0.95454545]
 [0.16129032 0.83870968]
 [0.12087912 0.87912088]
 [0.06382979 0.93617021]
 [0.01176471 0.98823529]
 [0.12222222 0.87777778]
 [0.         1.        ]
 [0.01162791 0.98837209]
 [0.01149425 0.98850575]
 [0.31764706 0.68235294]
 [0.01219512 0.98780488]
 [0.13186813 0.86813187]
 [0.02325581 0.97674419]
 [0.02083333 0.97916667]
 [0.17283951 0.82716049]
 [0.         1.        ]
 [0.1122449  0.8877551 ]]
	- oob_score_ = 0.9183673469387755

#### Importance of features
- gp_auc_min = 0.1409948721127514
- gp_max_val_min = 0.13680290659764946
- gp_auc_mean = 0.07252897866176283
- gp_max_val_mean = 0.061580865009173834
- gp_auc_max = 0.048168152936960994
- srmr = 0.043791769813883934
- hlbr = 0.036219358582593876
- gp_max_val_max = 0.036159851679284885
- gp_max_ix_mean = 0.03173069029735697
- diff_auc = 0.031192186379725078
- coe1[1] = 0.02975517815517816
- gp_max_val_std = 0.02894915968104822
- gp_max_val_range = 0.028749406702524797
- low_power = 0.025798544048544054
- ratio_max_to_10ms_ave_peaks = 0.024908038286079442
- tdoa_mean = 0.023651042090313348
- high_power = 0.021685379792397336
- coe1[0] = 0.02111137900560978
- ac_std = 0.020130625583566764
- coe3[3] = 0.019992074603235994
- diff_std = 0.019290129478364778
- gp_auc_range = 0.017967030577447248
- gp_auc_std = 0.01572335214342761
- coe3[2] = 0.014158800719698156
- gp_max_ix_max = 0.010846757409257411
- tdoa_max = 0.009340079146000201
- gp_max_ix_std = 0.0065396825396825415
- ac_auc = 0.005882098565922097
- tdoa_std = 0.005381409230358813
- ratio_max_to_9th_ave_peaks = 0.004406438006438008
- gp_max_ix_range = 0.0034161838161838173
- tdoa_range = 0.0017829577829577832
- tdoa_min = 0.001227868427868428
- gp_max_ix_min = 0.00013675213675213655
- coe3[0] = 0.0
- coe3[1] = 0.0

## Evaluation
cv = 8
### accuracy
- Scores = [ 0.5789473684210527, 0.631578947368421, 0.8947368421052632, 0.8421052631578947, 0.8947368421052632, 0.6842105263157895, 0.6111111111111112, 0.7222222222222222 ]
- Mean = 0.7324561403508772
- Standard deviation = 0.1202035367900261

### balanced_accuracy
- Scores = [ 0.4583333333333333, 0.675, 0.8416666666666667, 0.7166666666666667, 0.8416666666666667, 0.8, 0.36666666666666664, 0.5666666666666667 ]
- Mean = 0.6583333333333333
- Standard deviation = 0.16749792701868152

### f1
- Scores = [ 0.2, 0.46153846153846156, 0.75, 0.5714285714285715, 0.75, 0.5714285714285715, 0.0, 0.28571428571428575 ]
- Mean = 0.44876373626373633
- Standard deviation = 0.2503998055977691

### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 99 | 21 |
| Actual Positive | 12 | 18 |

      