# ExtraTreesClassifier_SMOTEENN_2021-12-29_no5
## Constants
- CSV_PATH = ../out/csv/experiment
- OUTPUT_PATH = ../out/experiment_result/data_of_2021-12-27/NoAGC-0angle-under5m
- FEATURE_ATTRBS = ['low_power', 'high_power', 'hlbr', 'coe1[0]', 'coe1[1]', 'coe3[0]', 'coe3[1]', 'coe3[2]', 'coe3[3]', 'ratio_max_to_10ms_ave_peaks', 'ratio_max_to_9th_ave_peaks', 'ac_std', 'ac_auc', 'diff_std', 'diff_auc', 'srmr', 'gp_max_val_std', 'gp_max_val_range', 'gp_max_val_min', 'gp_max_val_max', 'gp_max_val_mean', 'gp_max_ix_std', 'gp_max_ix_range', 'gp_max_ix_min', 'gp_max_ix_max', 'gp_max_ix_mean', 'gp_auc_std', 'gp_auc_range', 'gp_auc_min', 'gp_auc_max', 'gp_auc_mean', 'tdoa_std', 'tdoa_range', 'tdoa_min', 'tdoa_max', 'tdoa_mean']
- LABEL_ATTRB = ['facing']
- FACING_DOV_ANGLES = [1]
- NCV = 8
- SCORING = ['accuracy', 'balanced_accuracy', 'f1']
- REFIT_SCORING = balanced_accuracy
- PARAM_GRID = [{'est__n_estimators': [50, 100, 150, 200, 300], 'est__min_samples_split': [2, 5, 10], 'est__min_samples_leaf': [1, 5, 10], 'est__max_features': ['sqrt', 'log2', None], 'est__bootstrap': [False], 'est__n_jobs': [-1], 'est__random_state': [42], 'est__max_samples': [0.01, 0.5, 0.09]}, {'est__n_estimators': [50, 100, 150, 200, 300], 'est__min_samples_split': [2, 5, 10], 'est__min_samples_leaf': [1, 5, 10], 'est__max_features': ['sqrt', 'log2', None], 'est__bootstrap': [True], 'est__oob_score': [True, False], 'est__n_jobs': [-1], 'est__random_state': [42], 'est__max_samples': [0.01, 0.5, 0.09]}]
- TRAIN_SET_SESSION = ['trial1', 'trial2']
- TEST_SET_SESSION = ['trial3', 'trial4', 'trial5']
- DISTANCE = [1, 3, 5]
- AGC_STATUS = ['NoAGC']

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
	- oob_decision_function_ = [[0.50417293 0.49582707]
 [0.43246991 0.56753009]
 [0.8500512  0.1499488 ]
 [0.83616071 0.16383929]
 [0.96388889 0.03611111]
 [0.96121748 0.03878252]
 [0.84384058 0.15615942]
 [0.65212885 0.34787115]
 [0.52940075 0.47059925]
 [0.88095238 0.11904762]
 [0.44860689 0.55139311]
 [0.98443223 0.01556777]
 [0.96938776 0.03061224]
 [0.94507576 0.05492424]
 [0.78005013 0.21994987]
 [0.72229663 0.27770337]
 [0.94749104 0.05250896]
 [0.91736015 0.08263985]
 [0.86206897 0.13793103]
 [0.71992754 0.28007246]
 [0.9702381  0.0297619 ]
 [0.80772595 0.19227405]
 [0.7751004  0.2248996 ]
 [0.57113402 0.42886598]
 [0.53826331 0.46173669]
 [0.41865079 0.58134921]
 [0.78670412 0.21329588]
 [0.66278051 0.33721949]
 [0.35498339 0.64501661]
 [0.64526426 0.35473574]
 [0.96100324 0.03899676]
 [0.63836996 0.36163004]
 [0.62096774 0.37903226]
 [0.76795846 0.23204154]
 [0.76701389 0.23298611]
 [0.99014337 0.00985663]
 [0.94341737 0.05658263]
 [0.59026217 0.40973783]
 [0.77265122 0.22734878]
 [0.63885512 0.36114488]
 [0.17263374 0.82736626]
 [0.12364341 0.87635659]
 [0.36488849 0.63511151]
 [0.22222222 0.77777778]
 [0.12204762 0.87795238]
 [0.24446228 0.75553772]
 [0.36638322 0.63361678]
 [0.1322807  0.8677193 ]
 [0.60721649 0.39278351]
 [0.15634921 0.84365079]
 [0.05666667 0.94333333]
 [0.08085809 0.91914191]
 [0.11494253 0.88505747]
 [0.25497592 0.74502408]
 [0.0874031  0.9125969 ]
 [0.44207969 0.55792031]
 [0.07242798 0.92757202]
 [0.05912698 0.94087302]
 [0.10555556 0.89444444]
 [0.14971219 0.85028781]
 [0.25703704 0.74296296]
 [0.43820225 0.56179775]
 [0.08164794 0.91835206]
 [0.32196078 0.67803922]
 [0.34190476 0.65809524]
 [0.11560333 0.88439667]
 [0.06783009 0.93216991]
 [0.29027569 0.70972431]
 [0.15452381 0.84547619]
 [0.05649123 0.94350877]
 [0.10058824 0.89941176]
 [0.43342732 0.56657268]
 [0.69693487 0.30306513]
 [0.08138298 0.91861702]
 [0.08992674 0.91007326]
 [0.55089893 0.44910107]
 [0.21924399 0.78075601]
 [0.27554348 0.72445652]
 [0.3376947  0.6623053 ]
 [0.05860806 0.94139194]
 [0.57109929 0.42890071]
 [0.16007752 0.83992248]
 [0.153      0.847     ]
 [0.22439863 0.77560137]
 [0.05764256 0.94235744]
 [0.12768158 0.87231842]
 [0.10306513 0.89693487]
 [0.23814815 0.76185185]
 [0.37849462 0.62150538]]
	- oob_score_ = 0.898876404494382

#### Importance of features
- gp_max_ix_max = 0.05479830201551652
- gp_max_val_min = 0.05382332477541374
- coe3[3] = 0.053558554768258555
- tdoa_max = 0.0429168244144386
- gp_max_val_mean = 0.04258313780894025
- gp_auc_min = 0.04175752698597091
- low_power = 0.03925581963550048
- gp_auc_max = 0.03774317196923672
- gp_max_val_max = 0.03647355225280089
- ratio_max_to_10ms_ave_peaks = 0.03313302777122791
- tdoa_mean = 0.032932348509309275
- gp_max_ix_std = 0.03275813456603995
- coe1[0] = 0.03183795526541658
- hlbr = 0.03097898942201993
- gp_max_val_range = 0.030814493873301044
- coe1[1] = 0.02994142261985603
- gp_max_ix_mean = 0.029917642452796014
- diff_auc = 0.028074153216831762
- gp_auc_mean = 0.025747013906991554
- high_power = 0.02397140572833812
- ac_std = 0.02362616398427927
- coe3[2] = 0.022955915393488464
- ac_auc = 0.022419468830493186
- gp_max_val_std = 0.021958019666149988
- gp_auc_range = 0.02117332401544875
- tdoa_range = 0.02095645914394303
- diff_std = 0.020787331646971
- gp_max_ix_range = 0.0196012078252974
- tdoa_std = 0.019244424657438995
- tdoa_min = 0.01823438091160456
- gp_auc_std = 0.017212650057734806
- ratio_max_to_9th_ave_peaks = 0.015228401781396714
- srmr = 0.012541836738329365
- gp_max_ix_min = 0.011043613389219553
- coe3[0] = 0.0
- coe3[1] = 0.0

## Evaluation
cv = 8
### accuracy
- Scores = [ 0.782608695652174, 0.7391304347826086, 0.7391304347826086, 0.8181818181818182, 0.6818181818181818, 0.8181818181818182, 0.7272727272727273, 0.6818181818181818 ]
- Mean = 0.7485177865612649
- Standard deviation = 0.05048962334316395

### balanced_accuracy
- Scores = [ 0.6444444444444444, 0.4722222222222222, 0.6888888888888889, 0.6, 0.6111111111111112, 0.7916666666666667, 0.7361111111111112, 0.8055555555555556 ]
- Mean = 0.66875
- Standard deviation = 0.10370034510103657

### f1
- Scores = [ 0.4444444444444445, 0.0, 0.5, 0.33333333333333337, 0.36363636363636365, 0.6, 0.5, 0.5333333333333333 ]
- Mean = 0.40934343434343434
- Standard deviation = 0.17493621937407064

### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 116 | 27 |
| Actual Positive | 18 | 18 |

      