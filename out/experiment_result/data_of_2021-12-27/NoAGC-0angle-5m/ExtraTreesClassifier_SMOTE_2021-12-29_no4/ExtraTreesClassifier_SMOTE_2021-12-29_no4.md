# ExtraTreesClassifier_SMOTE_2021-12-29_no4
## Constants
- CSV_PATH = ../out/csv/experiment
- OUTPUT_PATH = ../out/experiment_result/data_of_2021-12-27/NoAGC-0angle-5m
- FEATURE_ATTRBS = ['low_power', 'high_power', 'hlbr', 'coe1[0]', 'coe1[1]', 'coe3[0]', 'coe3[1]', 'coe3[2]', 'coe3[3]', 'ratio_max_to_10ms_ave_peaks', 'ratio_max_to_9th_ave_peaks', 'ac_std', 'ac_auc', 'diff_std', 'diff_auc', 'srmr', 'gp_max_val_std', 'gp_max_val_range', 'gp_max_val_min', 'gp_max_val_max', 'gp_max_val_mean', 'gp_max_ix_std', 'gp_max_ix_range', 'gp_max_ix_min', 'gp_max_ix_max', 'gp_max_ix_mean', 'gp_auc_std', 'gp_auc_range', 'gp_auc_min', 'gp_auc_max', 'gp_auc_mean', 'tdoa_std', 'tdoa_range', 'tdoa_min', 'tdoa_max', 'tdoa_mean']
- LABEL_ATTRB = ['facing']
- FACING_DOV_ANGLES = [1]
- NCV = 8
- SCORING = ['accuracy', 'balanced_accuracy', 'f1']
- REFIT_SCORING = balanced_accuracy
- PARAM_GRID = [{'est__n_estimators': [50, 100, 150, 200, 300], 'est__min_samples_split': [2, 5, 10], 'est__min_samples_leaf': [1, 5, 10], 'est__max_features': ['sqrt', 'log2', None], 'est__bootstrap': [False], 'est__n_jobs': [-1], 'est__random_state': [42], 'est__max_samples': [0.01, 0.5, 0.09]}, {'est__n_estimators': [50, 100, 150, 200, 300], 'est__min_samples_split': [2, 5, 10], 'est__min_samples_leaf': [1, 5, 10], 'est__max_features': ['sqrt', 'log2', None], 'est__bootstrap': [True], 'est__oob_score': [True, False], 'est__n_jobs': [-1], 'est__random_state': [42], 'est__max_samples': [0.01, 0.5, 0.09]}]
- TRAIN_SET_SESSION = ['trial1', 'trial2']
- TEST_SET_SESSION = ['trial3', 'trial4', 'trial5']
- DISTANCE = [5]
- AGC_STATUS = ['NoAGC']

## Loaded CSV
- 2021-12-27_raspi_48000Hz_w1_N2^12_overlap80_new.csv

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
	- sampling_strategy_ = OrderedDict([(1, 24)])
	- nn_k_ = NearestNeighbors(n_neighbors=6)

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
	- min_samples_split = 2
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
	- oob_decision_function_ = [[0.37288136 0.62711864]
 [0.08108108 0.91891892]
 [0.64285714 0.35714286]
 [0.36619718 0.63380282]
 [1.         0.        ]
 [0.96969697 0.03030303]
 [1.         0.        ]
 [1.         0.        ]
 [1.         0.        ]
 [0.96825397 0.03174603]
 [0.88333333 0.11666667]
 [0.81538462 0.18461538]
 [0.17460317 0.82539683]
 [0.16666667 0.83333333]
 [0.88571429 0.11428571]
 [0.27142857 0.72857143]
 [1.         0.        ]
 [1.         0.        ]
 [1.         0.        ]
 [1.         0.        ]
 [0.98529412 0.01470588]
 [0.98571429 0.01428571]
 [0.75       0.25      ]
 [0.60344828 0.39655172]
 [0.10638298 0.89361702]
 [0.03333333 0.96666667]
 [0.62068966 0.37931034]
 [0.63265306 0.36734694]
 [1.         0.        ]
 [1.         0.        ]
 [0.98360656 0.01639344]
 [0.98305085 0.01694915]
 [0.9516129  0.0483871 ]
 [1.         0.        ]
 [0.75       0.25      ]
 [0.1147541  0.8852459 ]
 [0.05882353 0.94117647]
 [0.03636364 0.96363636]
 [0.22222222 0.77777778]
 [0.60377358 0.39622642]
 [0.09433962 0.90566038]
 [0.01886792 0.98113208]
 [0.19642857 0.80357143]
 [0.08196721 0.91803279]
 [0.03278689 0.96721311]
 [0.03125    0.96875   ]
 [0.06557377 0.93442623]
 [0.13461538 0.86538462]
 [0.125      0.875     ]
 [0.03846154 0.96153846]
 [0.14285714 0.85714286]
 [0.01754386 0.98245614]
 [0.03508772 0.96491228]
 [0.08064516 0.91935484]
 [0.30645161 0.69354839]
 [0.10447761 0.89552239]
 [0.37735849 0.62264151]
 [0.03076923 0.96923077]
 [0.16129032 0.83870968]
 [0.03448276 0.96551724]
 [0.32258065 0.67741935]
 [0.05357143 0.94642857]
 [0.125      0.875     ]
 [0.14545455 0.85454545]]
	- oob_score_ = 0.9375

#### Importance of features
- gp_auc_max = 0.1040225069700445
- gp_auc_min = 0.08135023960163265
- gp_max_val_max = 0.07512443988045332
- high_power = 0.07226282673401271
- gp_max_val_min = 0.06446628343603264
- gp_auc_mean = 0.06289977365186472
- hlbr = 0.06042609969200597
- gp_max_val_mean = 0.05407823820367596
- srmr = 0.04517784285601339
- diff_auc = 0.026362791451550547
- ratio_max_to_9th_ave_peaks = 0.02585838309078585
- gp_auc_std = 0.025127449179435546
- gp_max_val_std = 0.022758473876944362
- coe1[0] = 0.0201874403635158
- tdoa_mean = 0.020043328080376364
- tdoa_max = 0.019189319136022516
- gp_max_ix_std = 0.019107143984244828
- gp_max_ix_mean = 0.017242244981867938
- tdoa_std = 0.017029774589478127
- gp_auc_range = 0.016784266272656365
- coe3[2] = 0.016700520122193432
- tdoa_range = 0.016361413274239626
- ac_auc = 0.013633192580182306
- diff_std = 0.01293173394373085
- coe1[1] = 0.012669848221469963
- ac_std = 0.012408388453067626
- ratio_max_to_10ms_ave_peaks = 0.011863171141764686
- gp_max_val_range = 0.011438296657058023
- gp_max_ix_max = 0.010126622323236668
- low_power = 0.009426872084023305
- gp_max_ix_range = 0.008581614463967406
- coe3[3] = 0.007697971205713421
- tdoa_min = 0.00666148949673854
- coe3[0] = 0.0
- coe3[1] = 0.0
- gp_max_ix_min = 0.0

## Evaluation
cv = 8
### accuracy
- Scores = [ 0.75, 1.0, 0.875, 1.0, 1.0, 1.0, 1.0, 0.8571428571428571 ]
- Mean = 0.9352678571428572
- Standard deviation = 0.09014652011744943

### balanced_accuracy
- Scores = [ 0.8333333333333333, 1.0, 0.9166666666666667, 1.0, 1.0, 1.0, 1.0, 0.9166666666666667 ]
- Mean = 0.9583333333333334
- Standard deviation = 0.05892556509887897

### f1
- Scores = [ 0.6666666666666666, 1.0, 0.8, 1.0, 1.0, 1.0, 1.0, 0.6666666666666666 ]
- Mean = 0.8916666666666666
- Standard deviation = 0.1450574598794101

### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 44 | 4 |
| Actual Positive | 0 | 12 |

      