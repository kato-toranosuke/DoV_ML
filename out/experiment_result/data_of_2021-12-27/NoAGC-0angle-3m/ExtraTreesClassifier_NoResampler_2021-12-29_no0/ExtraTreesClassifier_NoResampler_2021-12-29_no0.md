# ExtraTreesClassifier_NoResampler_2021-12-29_no0
## Constants
- CSV_PATH = ../out/csv/experiment
- OUTPUT_PATH = ../out/experiment_result/data_of_2021-12-27/NoAGC-0angle-3m
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
- 2021-12-27_raspi_48000Hz_w1_N2^12_overlap80_new.csv

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
	- oob_decision_function_ = [[0.35483871 0.64516129]
 [0.16666667 0.83333333]
 [0.92       0.08      ]
 [0.84848485 0.15151515]
 [1.         0.        ]
 [0.83870968 0.16129032]
 [0.96875    0.03125   ]
 [1.         0.        ]
 [1.         0.        ]
 [0.96296296 0.03703704]
 [0.87096774 0.12903226]
 [0.67647059 0.32352941]
 [1.         0.        ]
 [0.34782609 0.65217391]
 [0.86111111 0.13888889]
 [0.82352941 0.17647059]
 [1.         0.        ]
 [0.9375     0.0625    ]
 [1.         0.        ]
 [1.         0.        ]
 [0.86206897 0.13793103]
 [0.88235294 0.11764706]
 [0.96666667 0.03333333]
 [0.83333333 0.16666667]
 [0.56521739 0.43478261]
 [0.74193548 0.25806452]
 [0.7037037  0.2962963 ]
 [0.53571429 0.46428571]
 [1.         0.        ]
 [1.         0.        ]
 [1.         0.        ]
 [1.         0.        ]
 [1.         0.        ]
 [1.         0.        ]
 [0.86206897 0.13793103]
 [0.5        0.5       ]
 [0.30434783 0.69565217]
 [0.22727273 0.77272727]
 [0.67741935 0.32258065]
 [0.82142857 0.17857143]]
	- oob_score_ = 0.925

#### Importance of features
- high_power = 0.20122423602166442
- diff_auc = 0.147953633297839
- srmr = 0.08125843988911356
- coe1[0] = 0.06507569289524177
- hlbr = 0.0594434945841196
- gp_auc_min = 0.057081906775868246
- gp_max_val_mean = 0.05017755991285403
- gp_auc_max = 0.03874103487548867
- diff_std = 0.03862017035681897
- gp_max_val_min = 0.03821428571428572
- ratio_max_to_9th_ave_peaks = 0.03733935665769577
- gp_auc_mean = 0.027381776239907736
- gp_max_val_max = 0.023571428571428577
- gp_max_val_range = 0.0216069246657482
- gp_auc_std = 0.01864954870837224
- ac_auc = 0.013008680555555556
- gp_max_ix_max = 0.012592592592592591
- coe3[3] = 0.011547619047619051
- ratio_max_to_10ms_ave_peaks = 0.011439257220465635
- gp_max_ix_std = 0.0092871997283762
- gp_auc_range = 0.00919270833333334
- coe1[1] = 0.007936507936507936
- tdoa_std = 0.005166666666666669
- tdoa_mean = 0.004166666666666669
- coe3[2] = 0.004166666666666668
- ac_std = 0.003888888888888888
- low_power = 0.0012670565302144298
- coe3[0] = 0.0
- coe3[1] = 0.0
- gp_max_val_std = 0.0
- gp_max_ix_range = 0.0
- gp_max_ix_min = 0.0
- gp_max_ix_mean = 0.0
- tdoa_range = 0.0
- tdoa_min = 0.0
- tdoa_max = 0.0

## Evaluation
cv = 8
### accuracy
- Scores = [ 0.875, 0.875, 1.0, 0.75, 1.0, 1.0, 1.0, 0.2857142857142857 ]
- Mean = 0.8482142857142857
- Standard deviation = 0.22903134532822608

### balanced_accuracy
- Scores = [ 0.75, 0.75, 1.0, 0.5, 1.0, 1.0, 1.0, 0.5833333333333334 ]
- Mean = 0.8229166666666667
- Standard deviation = 0.19291936643179308

### f1
- Scores = [ 0.6666666666666666, 0.6666666666666666, 1.0, 0.0, 1.0, 1.0, 1.0, 0.2857142857142857 ]
- Mean = 0.7023809523809523
- Standard deviation = 0.35773760003135047

### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 43 | 5 |
| Actual Positive | 4 | 8 |

      