# ExtraTreesClassifier_SMOTE_2021-12-29_no4
## Constants
- CSV_PATH = ../out/csv/experiment
- OUTPUT_PATH = ../out/experiment_result/data_of_2021-12-27/AGC-0angle-under3m
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
	- sampling_strategy_ = OrderedDict([(1, 58)])
	- nn_k_ = NearestNeighbors(n_neighbors=6)

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
	- min_samples_leaf = 10
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
	- oob_decision_function_ = [[0.35094165 0.64905835]
 [0.34804552 0.65195448]
 [0.48776342 0.51223658]
 [0.50776388 0.49223612]
 [0.34530224 0.65469776]
 [0.55875915 0.44124085]
 [0.98814519 0.01185481]
 [0.99611609 0.00388391]
 [0.97907407 0.02092593]
 [0.99487578 0.00512422]
 [0.30961552 0.69038448]
 [0.5132068  0.4867932 ]
 [0.38953406 0.61046594]
 [0.35096162 0.64903838]
 [0.96430539 0.03569461]
 [0.82716507 0.17283493]
 [0.99077295 0.00922705]
 [0.99590062 0.00409938]
 [0.99521739 0.00478261]
 [0.93956307 0.06043693]
 [0.24612975 0.75387025]
 [0.33514636 0.66485364]
 [0.35546856 0.64453144]
 [0.4024011  0.5975989 ]
 [0.5549073  0.4450927 ]
 [0.51682408 0.48317592]
 [0.72271343 0.27728657]
 [0.89669205 0.10330795]
 [0.97968944 0.02031056]
 [0.98158291 0.01841709]
 [0.8786186  0.1213814 ]
 [0.88268419 0.11731581]
 [0.39722953 0.60277047]
 [0.08084951 0.91915049]
 [0.50000523 0.49999477]
 [0.14311291 0.85688709]
 [0.96100788 0.03899212]
 [0.95927586 0.04072414]
 [0.99107059 0.00892941]
 [0.99855072 0.00144928]
 [0.92949639 0.07050361]
 [0.95132325 0.04867675]
 [0.59337777 0.40662223]
 [0.60235225 0.39764775]
 [0.52033871 0.47966129]
 [0.38991163 0.61008837]
 [0.44668991 0.55331009]
 [0.50751    0.49249   ]
 [0.84040632 0.15959368]
 [0.86143674 0.13856326]
 [0.96533877 0.03466123]
 [0.96643694 0.03356306]
 [0.78059179 0.21940821]
 [0.54107995 0.45892005]
 [0.10250938 0.89749062]
 [0.13568388 0.86431612]
 [0.40983778 0.59016222]
 [0.49963963 0.50036037]
 [0.9753937  0.0246063 ]
 [0.95103114 0.04896886]
 [0.98579932 0.01420068]
 [0.98987551 0.01012449]
 [0.74300019 0.25699981]
 [0.95995673 0.04004327]
 [0.3246375  0.6753625 ]
 [0.35044298 0.64955702]
 [0.145079   0.854921  ]
 [0.20320409 0.79679591]
 [0.56704229 0.43295771]
 [0.51418121 0.48581879]
 [0.97135699 0.02864301]
 [0.99832776 0.00167224]
 [0.96393004 0.03606996]
 [0.95539194 0.04460806]
 [0.38180937 0.61819063]
 [0.28388706 0.71611294]
 [0.17956498 0.82043502]
 [0.09953716 0.90046284]
 [0.53290647 0.46709353]
 [0.41845244 0.58154756]
 [0.99838969 0.00161031]
 [0.99294872 0.00705128]
 [0.99368132 0.00631868]
 [0.97324287 0.02675713]
 [0.89020826 0.10979174]
 [0.93353701 0.06646299]
 [0.39993722 0.60006278]
 [0.47126972 0.52873028]
 [0.58660039 0.41339961]
 [0.31004615 0.68995385]
 [0.98966372 0.01033628]
 [0.98613391 0.01386609]
 [0.97639858 0.02360142]
 [0.93939288 0.06060712]
 [0.79009718 0.20990282]
 [0.51944916 0.48055084]
 [0.39617562 0.60382438]
 [0.18876045 0.81123955]
 [0.15911995 0.84088005]
 [0.28159121 0.71840879]
 [0.16670205 0.83329795]
 [0.23069156 0.76930844]
 [0.26007473 0.73992527]
 [0.334072   0.665928  ]
 [0.6059588  0.3940412 ]
 [0.28452902 0.71547098]
 [0.06985501 0.93014499]
 [0.08725343 0.91274657]
 [0.25329667 0.74670333]
 [0.07438981 0.92561019]
 [0.3396136  0.6603864 ]
 [0.35113869 0.64886131]
 [0.291086   0.708914  ]
 [0.0824291  0.9175709 ]
 [0.32071359 0.67928641]
 [0.23414729 0.76585271]
 [0.3280197  0.6719803 ]
 [0.09041725 0.90958275]
 [0.29388071 0.70611929]
 [0.44754742 0.55245258]
 [0.09161393 0.90838607]
 [0.31879903 0.68120097]
 [0.27731426 0.72268574]
 [0.19632519 0.80367481]
 [0.10753629 0.89246371]
 [0.32243824 0.67756176]
 [0.2135729  0.7864271 ]
 [0.37002992 0.62997008]
 [0.19495972 0.80504028]
 [0.12596948 0.87403052]
 [0.41482645 0.58517355]
 [0.23113113 0.76886887]
 [0.1283663  0.8716337 ]
 [0.08927576 0.91072424]
 [0.3037653  0.6962347 ]
 [0.16141551 0.83858449]
 [0.19628962 0.80371038]
 [0.56923068 0.43076932]
 [0.23546956 0.76453044]
 [0.10345908 0.89654092]
 [0.14093363 0.85906637]
 [0.3172183  0.6827817 ]
 [0.29505516 0.70494484]
 [0.06876287 0.93123713]
 [0.33843787 0.66156213]
 [0.32029295 0.67970705]
 [0.10992431 0.89007569]
 [0.08872522 0.91127478]
 [0.17037753 0.82962247]
 [0.37351666 0.62648334]
 [0.19658055 0.80341945]
 [0.08594733 0.91405267]
 [0.46104215 0.53895785]
 [0.41460352 0.58539648]
 [0.20286142 0.79713858]
 [0.10400846 0.89599154]]
	- oob_score_ = 0.8589743589743589

#### Importance of features
- gp_auc_min = 0.1961544563789145
- gp_max_val_min = 0.13655362823893666
- gp_max_val_mean = 0.1086539752725427
- gp_auc_mean = 0.09744470567442073
- gp_max_val_max = 0.09513282508259367
- gp_auc_max = 0.05918057867747902
- diff_auc = 0.0540406406884785
- low_power = 0.03460111197889221
- coe1[1] = 0.03214577894781578
- coe1[0] = 0.02689768526637039
- srmr = 0.020075716304897347
- hlbr = 0.017932080400607467
- gp_max_ix_max = 0.01734803077769526
- gp_max_val_std = 0.013254581116665025
- diff_std = 0.012205672561722758
- high_power = 0.01060832193972731
- coe3[2] = 0.009916158227107858
- ac_std = 0.009720925184134848
- tdoa_std = 0.008702164691963755
- tdoa_max = 0.008116154160597007
- gp_auc_range = 0.008083985524392615
- ratio_max_to_9th_ave_peaks = 0.005786515600795232
- coe3[3] = 0.003784514497188929
- ac_auc = 0.0033359436735010996
- tdoa_range = 0.002839124022866083
- gp_max_ix_min = 0.0022617133289778344
- gp_auc_std = 0.001853831411116663
- gp_max_ix_range = 0.0010704103871300636
- tdoa_mean = 0.0009316759407526983
- gp_max_ix_std = 0.0008034103951467461
- ratio_max_to_10ms_ave_peaks = 0.000563683646569259
- coe3[0] = 0.0
- coe3[1] = 0.0
- gp_max_val_range = 0.0
- gp_max_ix_mean = 0.0
- tdoa_min = 0.0

## Evaluation
cv = 8
### accuracy
- Scores = [ 0.5789473684210527, 0.631578947368421, 0.8947368421052632, 0.6842105263157895, 0.8947368421052632, 0.6666666666666666, 0.6666666666666666, 0.6666666666666666 ]
- Mean = 0.7105263157894737
- Standard deviation = 0.11060982642910958

### balanced_accuracy
- Scores = [ 0.7333333333333334, 0.675, 0.9333333333333333, 0.7083333333333333, 0.9333333333333333, 0.6964285714285714, 0.4, 0.4 ]
- Mean = 0.684970238095238
- Standard deviation = 0.19003290820380775

### f1
- Scores = [ 0.5, 0.46153846153846156, 0.8, 0.5, 0.8, 0.5, 0.0, 0.0 ]
- Mean = 0.44519230769230766
- Standard deviation = 0.2866723357886298

### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 85 | 34 |
| Actual Positive | 9 | 21 |

      