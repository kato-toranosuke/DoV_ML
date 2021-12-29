# ExtraTreesClassifier_SMOTE_2021-12-29_no4
## Constants
- CSV_PATH = ../out/csv/experiment
- OUTPUT_PATH = ../out/experiment_result/data_of_2021-12-27/AGC-45angle-under5m
- FEATURE_ATTRBS = ['low_power', 'high_power', 'hlbr', 'coe1[0]', 'coe1[1]', 'coe3[0]', 'coe3[1]', 'coe3[2]', 'coe3[3]', 'ratio_max_to_10ms_ave_peaks', 'ratio_max_to_9th_ave_peaks', 'ac_std', 'ac_auc', 'diff_std', 'diff_auc', 'srmr', 'gp_max_val_std', 'gp_max_val_range', 'gp_max_val_min', 'gp_max_val_max', 'gp_max_val_mean', 'gp_max_ix_std', 'gp_max_ix_range', 'gp_max_ix_min', 'gp_max_ix_max', 'gp_max_ix_mean', 'gp_auc_std', 'gp_auc_range', 'gp_auc_min', 'gp_auc_max', 'gp_auc_mean', 'tdoa_std', 'tdoa_range', 'tdoa_min', 'tdoa_max', 'tdoa_mean']
- LABEL_ATTRB = ['facing2']
- FACING_DOV_ANGLES = [1, 2]
- NCV = 8
- SCORING = ['accuracy', 'balanced_accuracy', 'f1']
- REFIT_SCORING = balanced_accuracy
- PARAM_GRID = [{'est__n_estimators': [50, 100, 150, 200, 300], 'est__min_samples_split': [2, 5, 10], 'est__min_samples_leaf': [1, 5, 10], 'est__max_features': ['sqrt', 'log2', None], 'est__bootstrap': [False], 'est__n_jobs': [-1], 'est__random_state': [42], 'est__max_samples': [0.01, 0.5, 0.09]}, {'est__n_estimators': [50, 100, 150, 200, 300], 'est__min_samples_split': [2, 5, 10], 'est__min_samples_leaf': [1, 5, 10], 'est__max_features': ['sqrt', 'log2', None], 'est__bootstrap': [True], 'est__oob_score': [True, False], 'est__n_jobs': [-1], 'est__random_state': [42], 'est__max_samples': [0.01, 0.5, 0.09]}]
- TRAIN_SET_SESSION = ['trial1', 'trial2']
- TEST_SET_SESSION = ['trial3', 'trial4', 'trial5']
- DISTANCE = [1, 3, 5]
- AGC_STATUS = ['AGC']

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
	- sampling_strategy_ = OrderedDict([(0, 8)])
	- nn_k_ = NearestNeighbors(n_neighbors=6)

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
	- oob_decision_function_ = [[0.12195122 0.87804878]
 [0.04444444 0.95555556]
 [0.11956522 0.88043478]
 [0.08602151 0.91397849]
 [0.07446809 0.92553191]
 [0.11340206 0.88659794]
 [0.88372093 0.11627907]
 [0.92134831 0.07865169]
 [0.97916667 0.02083333]
 [1.         0.        ]
 [0.14893617 0.85106383]
 [0.05319149 0.94680851]
 [0.17391304 0.82608696]
 [0.02298851 0.97701149]
 [0.8556701  0.1443299 ]
 [0.37078652 0.62921348]
 [1.         0.        ]
 [1.         0.        ]
 [0.95454545 0.04545455]
 [0.96202532 0.03797468]
 [0.12631579 0.87368421]
 [0.08988764 0.91011236]
 [0.62222222 0.37777778]
 [0.10204082 0.89795918]
 [0.88297872 0.11702128]
 [0.65853659 0.34146341]
 [1.         0.        ]
 [1.         0.        ]
 [0.98734177 0.01265823]
 [1.         0.        ]
 [0.1372549  0.8627451 ]
 [0.11904762 0.88095238]
 [0.0326087  0.9673913 ]
 [0.03409091 0.96590909]
 [0.1875     0.8125    ]
 [0.16470588 0.83529412]
 [0.64948454 0.35051546]
 [0.80232558 0.19767442]
 [1.         0.        ]
 [1.         0.        ]
 [0.55       0.45      ]
 [0.4875     0.5125    ]
 [0.03846154 0.96153846]
 [0.         1.        ]
 [0.03030303 0.96969697]
 [0.         1.        ]
 [0.78494624 0.21505376]
 [0.86021505 0.13978495]
 [1.         0.        ]
 [1.         0.        ]
 [0.07608696 0.92391304]
 [0.10344828 0.89655172]
 [0.43333333 0.56666667]
 [0.11881188 0.88118812]
 [0.09677419 0.90322581]
 [0.02020202 0.97979798]
 [0.88888889 0.11111111]
 [0.67391304 0.32608696]
 [0.98684211 0.01315789]
 [0.97647059 0.02352941]
 [0.98924731 0.01075269]
 [0.94791667 0.05208333]
 [0.13793103 0.86206897]
 [0.09574468 0.90425532]
 [0.14772727 0.85227273]
 [0.28571429 0.71428571]
 [0.06315789 0.93684211]
 [0.18085106 0.81914894]
 [0.84375    0.15625   ]
 [0.70526316 0.29473684]
 [0.86956522 0.13043478]
 [0.84615385 0.15384615]
 [0.36842105 0.63157895]
 [0.05263158 0.94736842]
 [0.         1.        ]
 [0.         1.        ]
 [0.07446809 0.92553191]
 [0.04255319 0.95744681]
 [0.91397849 0.08602151]
 [0.65517241 0.34482759]
 [0.95744681 0.04255319]
 [0.8452381  0.1547619 ]
 [0.81111111 0.18888889]
 [0.1627907  0.8372093 ]
 [0.07368421 0.92631579]
 [0.05154639 0.94845361]
 [0.12643678 0.87356322]
 [0.05319149 0.94680851]
 [0.8        0.2       ]
 [0.96551724 0.03448276]
 [0.96666667 0.03333333]
 [0.98947368 0.01052632]
 [0.625      0.375     ]
 [0.93103448 0.06896552]
 [0.26966292 0.73033708]
 [0.32222222 0.67777778]
 [0.12903226 0.87096774]
 [0.075      0.925     ]
 [0.09183673 0.90816327]
 [0.19354839 0.80645161]
 [0.97647059 0.02352941]
 [1.         0.        ]
 [0.92045455 0.07954545]
 [0.84536082 0.15463918]
 [0.02352941 0.97647059]
 [0.         1.        ]
 [0.         1.        ]
 [0.         1.        ]
 [0.07142857 0.92857143]
 [0.04819277 0.95180723]
 [1.         0.        ]
 [0.97647059 0.02352941]
 [0.98850575 0.01149425]
 [0.95061728 0.04938272]
 [0.11235955 0.88764045]
 [0.10989011 0.89010989]
 [0.03370787 0.96629213]
 [0.03488372 0.96511628]
 [0.0326087  0.9673913 ]
 [0.34615385 0.65384615]
 [1.         0.        ]
 [0.98901099 0.01098901]
 [0.98148148 0.01851852]
 [0.94047619 0.05952381]
 [0.77906977 0.22093023]
 [0.91011236 0.08988764]
 [0.01041667 0.98958333]
 [0.07291667 0.92708333]
 [0.12       0.88      ]
 [0.08510638 0.91489362]
 [0.98924731 0.01075269]
 [1.         0.        ]
 [0.81927711 0.18072289]
 [0.62637363 0.37362637]
 [0.07291667 0.92708333]
 [0.10638298 0.89361702]
 [0.01234568 0.98765432]
 [0.         1.        ]
 [1.         0.        ]
 [1.         0.        ]
 [1.         0.        ]
 [1.         0.        ]
 [0.82795699 0.17204301]
 [0.98888889 0.01111111]
 [0.08888889 0.91111111]
 [0.06862745 0.93137255]
 [0.02061856 0.97938144]
 [0.02884615 0.97115385]
 [0.91397849 0.08602151]
 [0.99029126 0.00970874]
 [0.94047619 0.05952381]
 [0.93684211 0.06315789]
 [0.98876404 0.01123596]
 [0.82474227 0.17525773]
 [1.         0.        ]
 [0.89534884 0.10465116]]
	- oob_score_ = 0.9615384615384616

#### Importance of features
- gp_max_val_min = 0.08229018029059154
- gp_auc_min = 0.08219964936598673
- gp_max_val_mean = 0.08046833613443254
- gp_auc_mean = 0.07756233409117466
- gp_auc_max = 0.07362776672743614
- high_power = 0.05093806204811381
- gp_max_val_max = 0.05017436473837763
- diff_std = 0.04505048981423236
- diff_auc = 0.044851740557962115
- srmr = 0.0394704336556301
- coe1[1] = 0.03710437126324073
- coe1[0] = 0.03647214689542501
- ratio_max_to_10ms_ave_peaks = 0.033230236696360584
- hlbr = 0.03167120887134066
- low_power = 0.027704005778917833
- coe3[3] = 0.021481150809430062
- ac_std = 0.016613827069270955
- coe3[2] = 0.015913416508171567
- ac_auc = 0.015286882936643213
- tdoa_mean = 0.01246817661401481
- gp_auc_std = 0.012263556700323345
- gp_max_val_range = 0.011964761649726626
- gp_max_val_std = 0.010968285148061366
- gp_max_ix_range = 0.010914424511504766
- tdoa_min = 0.010327208705497946
- gp_max_ix_std = 0.009100616195761437
- tdoa_std = 0.008917862386258158
- gp_max_ix_mean = 0.00888763487940947
- gp_max_ix_min = 0.008724482743992672
- gp_max_ix_max = 0.007719498426822523
- gp_auc_range = 0.0073456419993880835
- tdoa_max = 0.0072778519759163374
- tdoa_range = 0.006265207135628323
- ratio_max_to_9th_ave_peaks = 0.004744186674955976
- coe3[0] = 0.0
- coe3[1] = 0.0

## Evaluation
cv = 8
### accuracy
- Scores = [ 0.8928571428571429, 0.9642857142857143, 0.8571428571428571, 0.9642857142857143, 0.8928571428571429, 0.9642857142857143, 1.0, 0.9642857142857143 ]
- Mean = 0.9375
- Standard deviation = 0.04639421805988065

### balanced_accuracy
- Scores = [ 0.8846153846153846, 0.9666666666666667, 0.8564102564102565, 0.9615384615384616, 0.9, 0.9642857142857143, 1.0, 0.9642857142857143 ]
- Mean = 0.9372252747252747
- Standard deviation = 0.04683443755025361

### f1
- Scores = [ 0.9090909090909091, 0.9655172413793104, 0.8666666666666667, 0.967741935483871, 0.888888888888889, 0.962962962962963, 1.0, 0.962962962962963 ]
- Mean = 0.9404789459294465
- Standard deviation = 0.04332868589639543

### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 101 | 6 |
| Actual Positive | 8 | 109 |

      