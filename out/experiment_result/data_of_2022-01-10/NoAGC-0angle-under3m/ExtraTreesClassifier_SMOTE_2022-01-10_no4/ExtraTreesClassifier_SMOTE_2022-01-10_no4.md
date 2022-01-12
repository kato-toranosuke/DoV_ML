# ExtraTreesClassifier_SMOTE_2022-01-10_no4
## Constants
- CSV_PATH = ../out/csv/experiment
- OUTPUT_PATH = ../out/experiment_result/data_of_2022-01-10/NoAGC-0angle-under3m
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
- AGC_STATUS = ['NoAGC']

## Loaded CSV
- 2022-01-10_raspi_48000Hz_w1_N2^12_overlap80.csv

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
	- sampling_strategy_ = OrderedDict([(1, 60)])
	- nn_k_ = NearestNeighbors(n_neighbors=6)

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
	- max_samples = 0.5
	- criterion = gini
	- max_depth = None
	- min_samples_split = 10
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
	- oob_decision_function_ = [[0.07218481 0.92781519]
 [0.12659788 0.87340212]
 [0.36349461 0.63650539]
 [0.42642738 0.57357262]
 [0.80003608 0.19996392]
 [0.82632409 0.17367591]
 [1.         0.        ]
 [1.         0.        ]
 [1.         0.        ]
 [1.         0.        ]
 [0.08521168 0.91478832]
 [0.21434142 0.78565858]
 [0.55589827 0.44410173]
 [0.86584629 0.13415371]
 [0.984375   0.015625  ]
 [0.98245614 0.01754386]
 [1.         0.        ]
 [1.         0.        ]
 [1.         0.        ]
 [1.         0.        ]
 [0.57481019 0.42518981]
 [0.3397505  0.6602495 ]
 [0.27805344 0.72194656]
 [0.31798059 0.68201941]
 [0.50626837 0.49373163]
 [0.39633774 0.60366226]
 [0.94590643 0.05409357]
 [0.85948118 0.14051882]
 [1.         0.        ]
 [0.99428571 0.00571429]
 [0.92766667 0.07233333]
 [0.93734568 0.06265432]
 [0.17579074 0.82420926]
 [0.4028647  0.5971353 ]
 [0.43735836 0.56264164]
 [0.20850497 0.79149503]
 [1.         0.        ]
 [1.         0.        ]
 [1.         0.        ]
 [1.         0.        ]
 [1.         0.        ]
 [0.98167517 0.01832483]
 [0.39595122 0.60404878]
 [0.58957113 0.41042887]
 [0.55116683 0.44883317]
 [0.50605001 0.49394999]
 [0.5581675  0.4418325 ]
 [0.65340745 0.34659255]
 [0.41232997 0.58767003]
 [0.87015939 0.12984061]
 [0.99354839 0.00645161]
 [1.         0.        ]
 [0.88883664 0.11116336]
 [0.98059701 0.01940299]
 [0.04479843 0.95520157]
 [0.03008658 0.96991342]
 [0.90281501 0.09718499]
 [0.89434002 0.10565998]
 [1.         0.        ]
 [1.         0.        ]
 [1.         0.        ]
 [1.         0.        ]
 [0.96428507 0.03571493]
 [0.72455933 0.27544067]
 [0.54028787 0.45971213]
 [0.49603293 0.50396707]
 [0.54568509 0.45431491]
 [0.57547695 0.42452305]
 [0.50512091 0.49487909]
 [0.32826199 0.67173801]
 [1.         0.        ]
 [1.         0.        ]
 [1.         0.        ]
 [1.         0.        ]
 [0.9547619  0.0452381 ]
 [0.76817953 0.23182047]
 [0.35057496 0.64942504]
 [0.37118652 0.62881348]
 [0.65668484 0.34331516]
 [0.78264589 0.21735411]
 [1.         0.        ]
 [1.         0.        ]
 [1.         0.        ]
 [1.         0.        ]
 [0.78731646 0.21268354]
 [0.90863837 0.09136163]
 [0.74741467 0.25258533]
 [0.31998143 0.68001857]
 [0.31502058 0.68497942]
 [0.11834711 0.88165289]
 [0.99298246 0.00701754]
 [1.         0.        ]
 [1.         0.        ]
 [1.         0.        ]
 [0.99298246 0.00701754]
 [1.         0.        ]
 [0.97875    0.02125   ]
 [0.98979592 0.01020408]
 [0.18501856 0.81498144]
 [0.35607239 0.64392761]
 [0.03855219 0.96144781]
 [0.2778003  0.7221997 ]
 [0.00324786 0.99675214]
 [0.37183919 0.62816081]
 [0.2580468  0.7419532 ]
 [0.19738248 0.80261752]
 [0.11855212 0.88144788]
 [0.03509259 0.96490741]
 [0.06425337 0.93574663]
 [0.11499646 0.88500354]
 [0.0037037  0.9962963 ]
 [0.25085237 0.74914763]
 [0.18819464 0.81180536]
 [0.13169526 0.86830474]
 [0.28363895 0.71636105]
 [0.37347657 0.62652343]
 [0.1336392  0.8663608 ]
 [0.01363636 0.98636364]
 [0.05017487 0.94982513]
 [0.23190473 0.76809527]
 [0.12728501 0.87271499]
 [0.00670297 0.99329703]
 [0.21489422 0.78510578]
 [0.13757086 0.86242914]
 [0.00910747 0.99089253]
 [0.54764161 0.45235839]
 [0.13992537 0.86007463]
 [0.28407726 0.71592274]
 [0.         1.        ]
 [0.28519334 0.71480666]
 [0.16832495 0.83167505]
 [0.01454545 0.98545455]
 [0.05216586 0.94783414]
 [0.02093154 0.97906846]
 [0.03259301 0.96740699]
 [0.39655868 0.60344132]
 [0.02685185 0.97314815]
 [0.1706134  0.8293866 ]
 [0.22742576 0.77257424]
 [0.04403778 0.95596222]
 [0.18207988 0.81792012]
 [0.03089652 0.96910348]
 [0.27251327 0.72748673]
 [0.07784744 0.92215256]
 [0.09833822 0.90166178]
 [0.02867133 0.97132867]
 [0.17461453 0.82538547]
 [0.10699856 0.89300144]
 [0.21557472 0.78442528]
 [0.03295973 0.96704027]
 [0.00171527 0.99828473]
 [0.03243371 0.96756629]
 [0.19178455 0.80821545]
 [0.23619726 0.76380274]
 [0.08851675 0.91148325]
 [0.00584795 0.99415205]
 [0.01420455 0.98579545]
 [0.04261738 0.95738262]
 [0.12822455 0.87177545]
 [0.21885281 0.78114719]]
	- oob_score_ = 0.9

#### Importance of features
- gp_max_val_min = 0.14771048557197983
- gp_auc_min = 0.1377538819522237
- gp_auc_mean = 0.133649385841418
- gp_max_val_mean = 0.12353418468521064
- gp_max_val_max = 0.0839509399370272
- gp_auc_max = 0.06653760878083476
- hlbr = 0.05599845603603717
- srmr = 0.04804242321778776
- gp_max_ix_max = 0.03502557106524378
- tdoa_max = 0.031469041221212656
- tdoa_range = 0.01712672053903243
- ratio_max_to_10ms_ave_peaks = 0.009539664038781613
- ac_auc = 0.009106830400116558
- gp_auc_std = 0.009061950382730406
- gp_max_ix_std = 0.008211423752447568
- ac_std = 0.007936284557295496
- tdoa_std = 0.0079096218479161
- gp_max_ix_range = 0.007509834076164218
- coe1[0] = 0.006620345644337458
- high_power = 0.006266316371776307
- ratio_max_to_9th_ave_peaks = 0.005774651086503812
- gp_max_ix_mean = 0.005702001530624396
- tdoa_min = 0.004685415102767875
- diff_auc = 0.004260232083079439
- gp_auc_range = 0.004249323650959792
- gp_max_val_std = 0.004139372441272362
- coe3[3] = 0.0036769170091973283
- tdoa_mean = 0.0030866331362037593
- gp_max_ix_min = 0.0028910737657130633
- gp_max_val_range = 0.0028539085187100394
- low_power = 0.0019499831306921296
- diff_std = 0.001692106979778212
- coe1[1] = 0.001202276593218506
- coe3[2] = 0.0008751350517055097
- coe3[0] = 0.0
- coe3[1] = 0.0

## Evaluation
cv = 8
### accuracy
- Scores = [ 0.7894736842105263, 0.7368421052631579, 0.8947368421052632, 0.7368421052631579, 0.8421052631578947, 0.8421052631578947, 0.6111111111111112, 0.7222222222222222 ]
- Mean = 0.7719298245614035
- Standard deviation = 0.08369164784422052

### balanced_accuracy
- Scores = [ 0.8666666666666667, 0.7416666666666667, 0.8416666666666667, 0.65, 0.625, 0.9, 0.36666666666666664, 0.5666666666666667 ]
- Mean = 0.6947916666666667
- Standard deviation = 0.1682186851739921

### f1
- Scores = [ 0.6666666666666666, 0.5454545454545454, 0.75, 0.4444444444444445, 0.4, 0.7272727272727273, 0.0, 0.28571428571428575 ]
- Mean = 0.47744408369408375
- Standard deviation = 0.2368890611285876

### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 105 | 15 |
| Actual Positive | 13 | 17 |

      