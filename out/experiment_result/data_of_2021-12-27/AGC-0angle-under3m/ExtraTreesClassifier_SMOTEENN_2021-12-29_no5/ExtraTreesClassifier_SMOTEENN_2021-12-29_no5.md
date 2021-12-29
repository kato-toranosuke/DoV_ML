# ExtraTreesClassifier_SMOTEENN_2021-12-29_no5
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
	- n_estimators = 300
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
	- min_samples_leaf = 5
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
	- oob_decision_function_ = [[0.85883616 0.14116384]
 [0.77984257 0.22015743]
 [0.91862923 0.08137077]
 [0.53783372 0.46216628]
 [0.57717052 0.42282948]
 [0.85102117 0.14897883]
 [0.85266639 0.14733361]
 [0.96968584 0.03031416]
 [0.99144667 0.00855333]
 [0.92224516 0.07775484]
 [0.91151285 0.08848715]
 [0.99131576 0.00868424]
 [0.9975781  0.0024219 ]
 [0.57127646 0.42872354]
 [0.69629743 0.30370257]
 [0.86216663 0.13783337]
 [0.91980092 0.08019908]
 [0.99040273 0.00959727]
 [0.99171683 0.00828317]
 [0.72782923 0.27217077]
 [0.68551734 0.31448266]
 [0.99736085 0.00263915]
 [0.94337243 0.05662757]
 [0.98278606 0.01721394]
 [0.99401992 0.00598008]
 [0.96651298 0.03348702]
 [0.22636109 0.77363891]
 [0.2152713  0.7847287 ]
 [0.05541722 0.94458278]
 [0.07132077 0.92867923]
 [0.10804375 0.89195625]
 [0.11734334 0.88265666]
 [0.08555994 0.91444006]
 [0.16587172 0.83412828]
 [0.07416257 0.92583743]
 [0.1111307  0.8888693 ]
 [0.09080966 0.90919034]
 [0.04954614 0.95045386]
 [0.05237018 0.94762982]
 [0.05824253 0.94175747]
 [0.34233272 0.65766728]
 [0.06463347 0.93536653]
 [0.38241263 0.61758737]
 [0.05446493 0.94553507]
 [0.09044243 0.90955757]
 [0.11592152 0.88407848]
 [0.11038946 0.88961054]
 [0.09026376 0.90973624]
 [0.13230445 0.86769555]
 [0.17331603 0.82668397]
 [0.07617469 0.92382531]
 [0.07493634 0.92506366]
 [0.09946453 0.90053547]
 [0.05439904 0.94560096]
 [0.05570953 0.94429047]
 [0.06689848 0.93310152]]
	- oob_score_ = 0.9642857142857143

#### Importance of features
- coe1[0] = 0.1318797083126403
- low_power = 0.13183540462930196
- coe1[1] = 0.10271654978835465
- coe3[3] = 0.09316707188031764
- ac_std = 0.07267705207976967
- ac_auc = 0.06649602814374166
- diff_std = 0.0566258889544522
- diff_auc = 0.05426595051632649
- high_power = 0.05000799171324334
- gp_auc_min = 0.04297476860097016
- coe3[2] = 0.042500762627556726
- gp_max_val_min = 0.030244004747746016
- gp_auc_max = 0.027128579002569504
- gp_max_val_max = 0.018553355145217876
- tdoa_mean = 0.012859220367495514
- gp_max_ix_mean = 0.0121582191654621
- gp_auc_mean = 0.009844284105245793
- gp_max_ix_std = 0.008597498067156529
- tdoa_std = 0.007913312649739771
- srmr = 0.005139108177322014
- gp_max_val_mean = 0.0048539060814408765
- gp_max_val_std = 0.0037573939079081926
- gp_max_val_range = 0.003507043429972387
- gp_auc_range = 0.002897863838032921
- hlbr = 0.0021270229409508065
- ratio_max_to_10ms_ave_peaks = 0.0019165429539905875
- ratio_max_to_9th_ave_peaks = 0.001819632822473432
- gp_auc_std = 0.0010197890714176065
- tdoa_max = 0.0003255447728924475
- tdoa_min = 0.00015151515151515154
- gp_max_ix_range = 3.898635477582851e-05
- coe3[0] = 0.0
- coe3[1] = 0.0
- gp_max_ix_min = 0.0
- gp_max_ix_max = 0.0
- tdoa_range = 0.0

## Evaluation
cv = 8
### accuracy
- Scores = [ 0.42105263157894735, 0.6842105263157895, 0.8947368421052632, 0.8421052631578947, 0.7894736842105263, 0.6111111111111112, 0.5555555555555556, 0.6111111111111112 ]
- Mean = 0.6761695906432749
- Standard deviation = 0.14845301650293202

### balanced_accuracy
- Scores = [ 0.35833333333333334, 0.8, 0.8416666666666667, 0.7166666666666667, 0.8666666666666667, 0.6607142857142857, 0.3333333333333333, 0.6333333333333333 ]
- Mean = 0.6513392857142857
- Standard deviation = 0.1924676746977825

### f1
- Scores = [ 0.15384615384615383, 0.5714285714285715, 0.75, 0.5714285714285715, 0.6666666666666666, 0.46153846153846156, 0.0, 0.36363636363636365 ]
- Mean = 0.4423180985680986
- Standard deviation = 0.24076987505143713

### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 82 | 37 |
| Actual Positive | 11 | 19 |

      