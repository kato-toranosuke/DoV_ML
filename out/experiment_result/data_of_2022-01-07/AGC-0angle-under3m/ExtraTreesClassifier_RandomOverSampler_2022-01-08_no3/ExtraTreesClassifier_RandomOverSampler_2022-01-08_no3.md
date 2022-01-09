# ExtraTreesClassifier_RandomOverSampler_2022-01-08_no3
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
	- sampling_strategy_ = OrderedDict([(1, 60)])
	- shrinkage_ = None
	- sample_indices_ = [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23
 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47
 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71
 72 73 74 75 76 77 78 79 80 81 82 83 84 85 86 87 88 89 90 91 92 93 94 95
 96 97 98 99 32 99 76 54 33 32 98 54 54 11 33 10  1 55 23  1  0 55 55 88
 45 77 76 76 98 55 99 10 22 98 32 44 32 89 11 67 89 44  1 99 76 32 55 33
 76 10 67 88 11 89 33 11  1 23 45 11 89 55  1 45]

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
	- oob_decision_function_ = [[0.15853659 0.84146341]
 [0.03333333 0.96666667]
 [0.51648352 0.48351648]
 [0.58064516 0.41935484]
 [0.23404255 0.76595745]
 [0.66315789 0.33684211]
 [0.97619048 0.02380952]
 [0.97752809 0.02247191]
 [0.98969072 0.01030928]
 [1.         0.        ]
 [0.09677419 0.90322581]
 [0.06382979 0.93617021]
 [0.54444444 0.45555556]
 [0.50574713 0.49425287]
 [0.97938144 0.02061856]
 [0.94382022 0.05617978]
 [1.         0.        ]
 [1.         0.        ]
 [1.         0.        ]
 [1.         0.        ]
 [0.17894737 0.82105263]
 [0.34444444 0.65555556]
 [0.13186813 0.86813187]
 [0.23232323 0.76767677]
 [0.4787234  0.5212766 ]
 [0.57831325 0.42168675]
 [0.92134831 0.07865169]
 [0.95959596 0.04040404]
 [1.         0.        ]
 [0.99       0.01      ]
 [0.62745098 0.37254902]
 [0.89411765 0.10588235]
 [0.02197802 0.97802198]
 [0.04545455 0.95454545]
 [0.65625    0.34375   ]
 [0.24418605 0.75581395]
 [1.         0.        ]
 [0.98837209 0.01162791]
 [1.         0.        ]
 [1.         0.        ]
 [0.97530864 0.02469136]
 [0.95       0.05      ]
 [0.51898734 0.48101266]
 [0.66019417 0.33980583]
 [0.25       0.75      ]
 [0.15909091 0.84090909]
 [0.66666667 0.33333333]
 [0.77173913 0.22826087]
 [0.91666667 0.08333333]
 [0.85057471 0.14942529]
 [0.93548387 0.06451613]
 [0.98863636 0.01136364]
 [0.8988764  0.1011236 ]
 [0.83168317 0.16831683]
 [0.0212766  0.9787234 ]
 [0.         1.        ]
 [0.8        0.2       ]
 [0.7826087  0.2173913 ]
 [0.98684211 0.01315789]
 [0.98795181 0.01204819]
 [1.         0.        ]
 [1.         0.        ]
 [0.90804598 0.09195402]
 [0.95744681 0.04255319]
 [0.43181818 0.56818182]
 [0.32967033 0.67032967]
 [0.17894737 0.82105263]
 [0.11827957 0.88172043]
 [0.79166667 0.20833333]
 [0.6        0.4       ]
 [0.9673913  0.0326087 ]
 [1.         0.        ]
 [0.9893617  0.0106383 ]
 [0.98947368 0.01052632]
 [0.56666667 0.43333333]
 [0.5        0.5       ]
 [0.02150538 0.97849462]
 [0.14130435 0.85869565]
 [0.66666667 0.33333333]
 [0.70930233 0.29069767]
 [0.98947368 0.01052632]
 [0.98809524 0.01190476]
 [0.98901099 0.01098901]
 [0.95348837 0.04651163]
 [0.94736842 0.05263158]
 [0.94897959 0.05102041]
 [0.53409091 0.46590909]
 [0.74468085 0.25531915]
 [0.22619048 0.77380952]
 [0.02272727 0.97727273]
 [0.95555556 0.04444444]
 [1.         0.        ]
 [1.         0.        ]
 [1.         0.        ]
 [0.98863636 0.01136364]
 [0.98876404 0.01123596]
 [0.87096774 0.12903226]
 [0.90123457 0.09876543]
 [0.08080808 0.91919192]
 [0.06451613 0.93548387]
 [0.02325581 0.97674419]
 [0.06451613 0.93548387]
 [0.02222222 0.97777778]
 [0.02083333 0.97916667]
 [0.04761905 0.95238095]
 [0.02597403 0.97402597]
 [0.08163265 0.91836735]
 [0.02272727 0.97727273]
 [0.02380952 0.97619048]
 [0.07228916 0.92771084]
 [0.04705882 0.95294118]
 [0.10588235 0.89411765]
 [0.03448276 0.96551724]
 [0.         1.        ]
 [0.25842697 0.74157303]
 [0.03296703 0.96703297]
 [0.14606742 0.85393258]
 [0.         1.        ]
 [0.         1.        ]
 [0.24050633 0.75949367]
 [0.14141414 0.85858586]
 [0.14285714 0.85714286]
 [0.01851852 0.98148148]
 [0.02380952 0.97619048]
 [0.09302326 0.90697674]
 [0.         1.        ]
 [0.06315789 0.93684211]
 [0.09473684 0.90526316]
 [0.12121212 0.87878788]
 [0.08602151 0.91397849]
 [0.02173913 0.97826087]
 [0.26595745 0.73404255]
 [0.02439024 0.97560976]
 [0.02197802 0.97802198]
 [0.06185567 0.93814433]
 [0.11956522 0.88043478]
 [0.02439024 0.97560976]
 [0.28409091 0.71590909]
 [0.03296703 0.96703297]
 [0.06382979 0.93617021]
 [0.02083333 0.97916667]
 [0.02247191 0.97752809]
 [0.         1.        ]
 [0.04494382 0.95505618]
 [0.02222222 0.97777778]
 [0.08737864 0.91262136]
 [0.11578947 0.88421053]
 [0.18269231 0.81730769]
 [0.06451613 0.93548387]
 [0.01941748 0.98058252]
 [0.04761905 0.95238095]
 [0.06315789 0.93684211]
 [0.03370787 0.96629213]
 [0.23469388 0.76530612]
 [0.16091954 0.83908046]
 [0.06976744 0.93023256]
 [0.02150538 0.97849462]
 [0.         1.        ]
 [0.03125    0.96875   ]
 [0.1372549  0.8627451 ]]
	- oob_score_ = 0.95625

#### Importance of features
- gp_max_val_min = 0.09864255037895586
- gp_max_val_mean = 0.08787493231123827
- gp_auc_min = 0.08308965975412522
- gp_auc_max = 0.0753473513844251
- gp_auc_mean = 0.07027623478937076
- gp_max_val_max = 0.055858651182075336
- diff_auc = 0.05120181806865182
- high_power = 0.0357051892728476
- srmr = 0.03342234464838732
- diff_std = 0.029681770938421916
- coe1[1] = 0.02607483224303347
- hlbr = 0.025456793878677966
- gp_auc_range = 0.021668915342246558
- coe1[0] = 0.021530878640593294
- low_power = 0.02139947978584897
- gp_max_ix_mean = 0.019086274930691996
- ratio_max_to_10ms_ave_peaks = 0.01886972095898923
- gp_max_val_range = 0.01840814133230646
- ratio_max_to_9th_ave_peaks = 0.016362585855601
- gp_auc_std = 0.01628340652116533
- coe3[3] = 0.015053510177612509
- ac_std = 0.014866048960591105
- gp_max_val_std = 0.014835191788775246
- tdoa_mean = 0.014567632129012712
- gp_max_ix_range = 0.014304484115182465
- ac_auc = 0.013853350922198289
- tdoa_std = 0.01321551886308444
- coe3[2] = 0.013004454028197188
- gp_max_ix_std = 0.012579145186056255
- gp_max_ix_max = 0.012237818918964622
- tdoa_range = 0.012193984566024938
- tdoa_max = 0.011706290621975328
- gp_max_ix_min = 0.006447571003812821
- tdoa_min = 0.0048934665008584
- coe3[0] = 0.0
- coe3[1] = 0.0

## Evaluation
cv = 8
### accuracy
- Scores = [ 0.47368421052631576, 0.6842105263157895, 0.9473684210526315, 0.7894736842105263, 0.9473684210526315, 0.8421052631578947, 0.7222222222222222, 0.8888888888888888 ]
- Mean = 0.7869152046783625
- Standard deviation = 0.14907576872506995

### balanced_accuracy
- Scores = [ 0.39166666666666666, 0.7083333333333333, 0.9666666666666667, 0.5916666666666667, 0.875, 0.9, 0.43333333333333335, 0.8 ]
- Mean = 0.7083333333333333
- Standard deviation = 0.20284435741063478

### f1
- Scores = [ 0.16666666666666666, 0.5, 0.888888888888889, 0.3333333333333333, 0.8571428571428571, 0.7272727272727273, 0.0, 0.6666666666666666 ]
- Mean = 0.5174963924963925
- Standard deviation = 0.3050934605852249

### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 100 | 20 |
| Actual Positive | 13 | 17 |

      