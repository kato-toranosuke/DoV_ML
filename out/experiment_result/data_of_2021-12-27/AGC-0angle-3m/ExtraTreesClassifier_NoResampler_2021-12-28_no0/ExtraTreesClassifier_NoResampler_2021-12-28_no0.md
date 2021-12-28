# ExtraTreesClassifier_NoResampler_2021-12-28_no0
## Constants
- CSV_PATH = ../out/csv/experiment
- OUTPUT_PATH = ../out/experiment_result/2021-12-27-3m
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
	- min_samples_split = 5
	- min_samples_leaf = 1
	- min_weight_fraction_leaf = 0.0
	- max_features = sqrt
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
	- oob_decision_function_ = [[0.81075269 0.18924731]
 [0.63455285 0.36544715]
 [0.82666667 0.17333333]
 [0.74427083 0.25572917]
 [1.         0.        ]
 [0.96875    0.03125   ]
 [1.         0.        ]
 [1.         0.        ]
 [0.96       0.04      ]
 [0.92643678 0.07356322]
 [0.96774194 0.03225806]
 [0.91919192 0.08080808]
 [0.52380952 0.47619048]
 [0.22916667 0.77083333]
 [0.70740741 0.29259259]
 [0.38047619 0.61952381]
 [1.         0.        ]
 [0.98958333 0.01041667]
 [1.         0.        ]
 [1.         0.        ]
 [0.90178571 0.09821429]
 [0.97058824 0.02941176]
 [0.90151515 0.09848485]
 [0.77388889 0.22611111]
 [0.24375    0.75625   ]
 [0.44784946 0.55215054]
 [0.6654321  0.3345679 ]
 [0.74252874 0.25747126]
 [1.         0.        ]
 [1.         0.        ]
 [0.95967742 0.04032258]
 [1.         0.        ]
 [1.         0.        ]
 [1.         0.        ]
 [0.74888889 0.25111111]
 [0.53678161 0.46321839]
 [0.56594203 0.43405797]
 [0.46666667 0.53333333]
 [0.70444444 0.29555556]
 [0.36896552 0.63103448]
 [0.94642857 0.05357143]
 [1.         0.        ]
 [1.         0.        ]
 [0.95952381 0.04047619]
 [0.77843137 0.22156863]
 [0.73611111 0.26388889]
 [0.53489583 0.46510417]
 [0.40308642 0.59691358]]
	- oob_score_ = 0.8541666666666666

#### Importance of features
- high_power = 0.1080975072625735
- gp_max_val_max = 0.0755561901738852
- diff_auc = 0.07311023587595124
- coe1[0] = 0.07010007436351935
- gp_auc_max = 0.05888529519732207
- coe3[3] = 0.04995007809523452
- ac_auc = 0.04919746387128917
- hlbr = 0.04770158600794836
- low_power = 0.0473987266071159
- diff_std = 0.04614228743321852
- gp_max_ix_mean = 0.04570321343915934
- gp_auc_min = 0.03786170449010473
- gp_auc_range = 0.02969577102516956
- gp_max_val_mean = 0.027796734873577967
- coe3[2] = 0.027618681456744662
- gp_max_val_min = 0.025862667364167334
- gp_auc_mean = 0.022897568251049025
- srmr = 0.02135934339337605
- gp_max_val_range = 0.020943901255114066
- gp_max_val_std = 0.018551432442670702
- tdoa_std = 0.016761954261954256
- tdoa_max = 0.013974861603046165
- ratio_max_to_9th_ave_peaks = 0.013200972862263172
- ac_std = 0.010351238095238096
- gp_max_ix_std = 0.008888888888888885
- tdoa_mean = 0.008016893297072468
- coe1[1] = 0.007676306642177879
- gp_max_ix_range = 0.007267633475912134
- ratio_max_to_10ms_ave_peaks = 0.006136670347196658
- gp_auc_std = 0.0032941176470588232
- coe3[0] = 0.0
- coe3[1] = 0.0
- gp_max_ix_min = 0.0
- gp_max_ix_max = 0.0
- tdoa_range = 0.0
- tdoa_min = 0.0

## Evaluation
cv = 8
### accuracy
- Scores = [ 1.0, 0.9, 0.8888888888888888, 0.7777777777777778, 0.8888888888888888, 0.8888888888888888, 0.6666666666666666, 0.6666666666666666 ]
- Mean = 0.8347222222222221
- Standard deviation = 0.11186377021368338

### balanced_accuracy
- Scores = [ 1.0, 0.75, 0.9285714285714286, 0.5, 0.9285714285714286, 0.75, 0.42857142857142855, 0.375 ]
- Mean = 0.7075892857142858
- Standard deviation = 0.22867211440316076

### f1
- Scores = [ 1.0, 0.6666666666666666, 0.8, 0.0, 0.8, 0.6666666666666666, 0.0, 0.0 ]
- Mean = 0.4916666666666667
- Standard deviation = 0.39290584113754273

### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 54 | 5 |
| Actual Positive | 7 | 8 |

      