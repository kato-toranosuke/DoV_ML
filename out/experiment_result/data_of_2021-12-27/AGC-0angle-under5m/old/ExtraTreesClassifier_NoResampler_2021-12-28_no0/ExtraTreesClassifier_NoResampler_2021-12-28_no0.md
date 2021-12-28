# ExtraTreesClassifier_NoResampler_2021-12-28_no0
## Constants
- CSV_PATH = ../out/csv/experiment
- OUTPUT_PATH = ../out/experiment_result
- FEATURE_ATTRBS = ['low_power', 'high_power', 'hlbr', 'coe1[0]', 'coe1[1]', 'coe3[0]', 'coe3[1]', 'coe3[2]', 'coe3[3]', 'ratio_max_to_10ms_ave_peaks', 'ratio_max_to_9th_ave_peaks', 'ac_std', 'ac_auc', 'diff_std', 'diff_auc', 'srmr', 'gp_max_val_std', 'gp_max_val_range', 'gp_max_val_min', 'gp_max_val_max', 'gp_max_val_mean', 'gp_max_ix_std', 'gp_max_ix_range', 'gp_max_ix_min', 'gp_max_ix_max', 'gp_max_ix_mean', 'gp_auc_std', 'gp_auc_range', 'gp_auc_min', 'gp_auc_max', 'gp_auc_mean', 'tdoa_std', 'tdoa_range', 'tdoa_min', 'tdoa_max', 'tdoa_mean']
- LABEL_ATTRB = ['facing']
- FACING_DOV_ANGLES = [1]
- NCV = 8
- SCORING = ['accuracy', 'balanced_accuracy', 'f1']
- REFIT_SCORING = balanced_accuracy
- PARAM_GRID = [{'est__n_estimators': [50, 100, 150, 200, 300], 'est__min_samples_split': [2, 5, 10], 'est__min_samples_leaf': [1, 5, 10], 'est__max_features': ['sqrt', 'log2', None], 'est__bootstrap': [False], 'est__n_jobs': [-1], 'est__random_state': [42], 'est__max_samples': [0.01, 0.5, 0.09]}, {'est__n_estimators': [50, 100, 150, 200, 300], 'est__min_samples_split': [2, 5, 10], 'est__min_samples_leaf': [1, 5, 10], 'est__max_features': ['sqrt', 'log2', None], 'est__bootstrap': [True], 'est__oob_score': [True, False], 'est__n_jobs': [-1], 'est__random_state': [42], 'est__max_samples': [0.01, 0.5, 0.09]}]
- TRAIN_SET_SESSION = ['trial1', 'trial2']
- TEST_SET_SESSION = ['trial3', 'trial4', 'trial5']

## Loaded CSV
- 2021-12-27_raspi_48000Hz_w1_N2^12_overlap80_withfacing.csv

## Estimator
### Type
- resampler = NoResampler
- estimator = ExtraTreesClassifier

### Arguments for hyperparameter search
- resampler = NoResampler
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
	- oob_decision_function_ = [[0.59259259 0.40740741]
 [0.46666667 0.53333333]
 [0.78125    0.21875   ]
 [0.7037037  0.2962963 ]
 [0.39393939 0.60606061]
 [0.79310345 0.20689655]
 [1.         0.        ]
 [1.         0.        ]
 [1.         0.        ]
 [1.         0.        ]
 [0.82758621 0.17241379]
 [0.93939394 0.06060606]
 [0.53571429 0.46428571]
 [0.59259259 0.40740741]
 [0.96428571 0.03571429]
 [0.93548387 0.06451613]
 [1.         0.        ]
 [1.         0.        ]
 [0.96666667 0.03333333]
 [0.96428571 0.03571429]
 [0.87096774 0.12903226]
 [0.54285714 0.45714286]
 [1.         0.        ]
 [0.86666667 0.13333333]
 [0.96666667 0.03333333]
 [0.96296296 0.03703704]
 [1.         0.        ]
 [1.         0.        ]
 [0.96       0.04      ]
 [1.         0.        ]
 [0.23809524 0.76190476]
 [0.60714286 0.39285714]
 [0.42307692 0.57692308]
 [0.6875     0.3125    ]
 [0.66666667 0.33333333]
 [0.7        0.3       ]
 [0.93939394 0.06060606]
 [1.         0.        ]
 [1.         0.        ]
 [1.         0.        ]
 [1.         0.        ]
 [1.         0.        ]
 [0.57692308 0.42307692]
 [0.27272727 0.72727273]
 [0.78378378 0.21621622]
 [0.1875     0.8125    ]
 [0.94117647 0.05882353]
 [0.97058824 0.02941176]
 [1.         0.        ]
 [1.         0.        ]
 [0.77419355 0.22580645]
 [0.66666667 0.33333333]
 [0.96774194 0.03225806]
 [0.5483871  0.4516129 ]
 [0.76666667 0.23333333]
 [0.54545455 0.45454545]
 [0.92857143 0.07142857]
 [1.         0.        ]
 [1.         0.        ]
 [1.         0.        ]
 [0.96428571 0.03571429]
 [1.         0.        ]
 [0.66666667 0.33333333]
 [0.8125     0.1875    ]
 [0.92307692 0.07692308]
 [0.64516129 0.35483871]
 [0.9375     0.0625    ]
 [0.86666667 0.13333333]
 [0.90909091 0.09090909]
 [0.91176471 0.08823529]
 [1.         0.        ]
 [0.96153846 0.03846154]
 [0.91428571 0.08571429]
 [0.83870968 0.16129032]
 [0.23076923 0.76923077]
 [0.37931034 0.62068966]
 [0.74193548 0.25806452]
 [0.76923077 0.23076923]
 [0.92857143 0.07142857]
 [0.9375     0.0625    ]
 [1.         0.        ]
 [1.         0.        ]
 [1.         0.        ]
 [0.96551724 0.03448276]
 [0.46428571 0.53571429]
 [0.21212121 0.78787879]
 [0.6875     0.3125    ]
 [0.48275862 0.51724138]
 [1.         0.        ]
 [1.         0.        ]
 [1.         0.        ]
 [1.         0.        ]
 [0.85294118 0.14705882]
 [1.         0.        ]
 [0.42857143 0.57142857]
 [0.54166667 0.45833333]
 [0.28125    0.71875   ]
 [0.44       0.56      ]
 [0.94736842 0.05263158]
 [0.9        0.1       ]
 [1.         0.        ]
 [1.         0.        ]
 [0.97142857 0.02857143]
 [0.97058824 0.02941176]
 [0.55555556 0.44444444]
 [0.33333333 0.66666667]
 [0.29032258 0.70967742]
 [0.23076923 0.76923077]
 [0.91428571 0.08571429]
 [0.31034483 0.68965517]
 [1.         0.        ]
 [1.         0.        ]
 [1.         0.        ]
 [1.         0.        ]
 [0.875      0.125     ]
 [0.76666667 0.23333333]
 [0.34285714 0.65714286]
 [0.37931034 0.62068966]
 [0.68965517 0.31034483]
 [0.81481481 0.18518519]
 [1.         0.        ]
 [0.94444444 0.05555556]
 [1.         0.        ]
 [0.96       0.04      ]
 [0.92857143 0.07142857]
 [0.96551724 0.03448276]
 [0.52777778 0.47222222]
 [0.86206897 0.13793103]
 [0.78125    0.21875   ]
 [0.5483871  0.4516129 ]
 [1.         0.        ]
 [1.         0.        ]
 [0.96428571 0.03571429]
 [0.90322581 0.09677419]
 [0.51428571 0.48571429]
 [0.6875     0.3125    ]
 [0.59259259 0.40740741]
 [0.20689655 0.79310345]
 [1.         0.        ]
 [1.         0.        ]
 [1.         0.        ]
 [1.         0.        ]
 [1.         0.        ]
 [1.         0.        ]
 [0.83870968 0.16129032]
 [0.93939394 0.06060606]
 [0.21212121 0.78787879]
 [0.70588235 0.29411765]]
	- oob_score_ = 0.8513513513513513

#### Importance of features
- high_power = 0.09628190587910115
- gp_auc_min = 0.09083893841122279
- diff_auc = 0.06697579448531268
- gp_max_val_min = 0.06686636577373345
- coe1[1] = 0.04411370705853921
- gp_auc_mean = 0.04361605289698761
- coe1[0] = 0.042489230606204034
- low_power = 0.042474754675285414
- gp_max_val_mean = 0.042204657709981476
- diff_std = 0.038763914230221255
- coe3[2] = 0.03525255800756679
- srmr = 0.033521880700760204
- ratio_max_to_9th_ave_peaks = 0.03257182741630555
- ratio_max_to_10ms_ave_peaks = 0.030276466859855376
- coe3[3] = 0.030023823083603476
- gp_max_val_std = 0.028154588126487495
- gp_auc_max = 0.027022825981989695
- ac_std = 0.025977341515568967
- gp_auc_range = 0.022783672760344955
- ac_auc = 0.021600858147144127
- gp_auc_std = 0.01930421584458273
- tdoa_range = 0.014027967268140058
- tdoa_max = 0.013899523193629108
- hlbr = 0.013749047350326907
- gp_max_val_max = 0.013426609221377736
- tdoa_std = 0.01336984863410768
- gp_max_val_range = 0.009654103476767532
- gp_max_ix_mean = 0.008402227566484347
- tdoa_mean = 0.00764970429574213
- gp_max_ix_min = 0.006425486189551526
- gp_max_ix_max = 0.005630079142017711
- gp_max_ix_range = 0.004493632269658887
- gp_max_ix_std = 0.004138390746354094
- tdoa_min = 0.004018000475043818
- coe3[0] = 0.0
- coe3[1] = 0.0

## Evaluation
cv = 8
### accuracy
- Scores = [ 0.7857142857142857, 0.8571428571428571, 0.8571428571428571, 0.8214285714285714, 0.8928571428571429, 0.8928571428571429, 0.7857142857142857, 0.8571428571428571 ]
- Mean = 0.84375
- Standard deviation = 0.03967943936301604

### balanced_accuracy
- Scores = [ 0.5606060606060607, 0.6666666666666666, 0.7272727272727273, 0.5833333333333334, 0.8712121212121212, 0.9347826086956521, 0.5565217391304348, 0.6782608695652175 ]
- Mean = 0.6973320158102767
- Standard deviation = 0.13244565584980902

### f1
- Scores = [ 0.25, 0.5, 0.6, 0.2857142857142857, 0.7692307692307692, 0.7692307692307693, 0.25, 0.5 ]
- Mean = 0.490521978021978
- Standard deviation = 0.20160918826506743

### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 169 | 10 |
| Actual Positive | 25 | 20 |

      