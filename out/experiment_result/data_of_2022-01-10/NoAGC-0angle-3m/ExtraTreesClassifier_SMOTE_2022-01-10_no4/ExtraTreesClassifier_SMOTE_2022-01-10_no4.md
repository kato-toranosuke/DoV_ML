# ExtraTreesClassifier_SMOTE_2022-01-10_no4
## Constants
- CSV_PATH = ../out/csv/experiment
- OUTPUT_PATH = ../out/experiment_result/data_of_2022-01-10/NoAGC-0angle-3m
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
	- sampling_strategy_ = OrderedDict([(1, 30)])
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
	- min_samples_split = 2
	- min_samples_leaf = 10
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
	- oob_decision_function_ = [[0.19446627 0.80553373]
 [0.2953207  0.7046793 ]
 [0.25889796 0.74110204]
 [0.59309071 0.40690929]
 [0.89698975 0.10301025]
 [0.91741018 0.08258982]
 [0.92812268 0.07187732]
 [0.92069329 0.07930671]
 [0.93725566 0.06274434]
 [0.93224735 0.06775265]
 [0.83261946 0.16738054]
 [0.84598677 0.15401323]
 [0.16683584 0.83316416]
 [0.20415194 0.79584806]
 [0.24193041 0.75806959]
 [0.15202508 0.84797492]
 [0.92862682 0.07137318]
 [0.89058364 0.10941636]
 [0.93376082 0.06623918]
 [0.92929961 0.07070039]
 [0.91432687 0.08567313]
 [0.90777235 0.09222765]
 [0.58866636 0.41133364]
 [0.8832638  0.1167362 ]
 [0.15045873 0.84954127]
 [0.12363091 0.87636909]
 [0.78730821 0.21269179]
 [0.70628335 0.29371665]
 [0.93188653 0.06811347]
 [0.94228714 0.05771286]
 [0.94732108 0.05267892]
 [0.92258638 0.07741362]
 [0.91971989 0.08028011]
 [0.93069623 0.06930377]
 [0.7992515  0.2007485 ]
 [0.72569496 0.27430504]
 [0.24646032 0.75353968]
 [0.30323598 0.69676402]
 [0.38637382 0.61362618]
 [0.61727282 0.38272718]
 [0.93189233 0.06810767]
 [0.93439121 0.06560879]
 [0.94157348 0.05842652]
 [0.94440808 0.05559192]
 [0.93478595 0.06521405]
 [0.8926492  0.1073508 ]
 [0.85776203 0.14223797]
 [0.88982485 0.11017515]
 [0.15284265 0.84715735]
 [0.17509619 0.82490381]
 [0.20787038 0.79212962]
 [0.13312932 0.86687068]
 [0.15175947 0.84824053]
 [0.14888638 0.85111362]
 [0.1653122  0.8346878 ]
 [0.16359256 0.83640744]
 [0.16224911 0.83775089]
 [0.17548068 0.82451932]
 [0.25342993 0.74657007]
 [0.19593736 0.80406264]
 [0.16335811 0.83664189]
 [0.11857047 0.88142953]
 [0.27942049 0.72057951]
 [0.32265961 0.67734039]
 [0.16269845 0.83730155]
 [0.13088825 0.86911175]
 [0.17954376 0.82045624]
 [0.13265912 0.86734088]
 [0.1417956  0.8582044 ]
 [0.13011584 0.86988416]
 [0.1286975  0.8713025 ]
 [0.18454075 0.81545925]
 [0.16718001 0.83281999]
 [0.16675048 0.83324952]
 [0.20131287 0.79868713]
 [0.14494826 0.85505174]
 [0.32541012 0.67458988]
 [0.11906906 0.88093094]
 [0.12911752 0.87088248]
 [0.22465125 0.77534875]]
	- oob_score_ = 0.95

#### Importance of features
- gp_max_val_max = 0.1771017746665702
- gp_auc_max = 0.15528448478904536
- gp_auc_min = 0.13074419060175682
- gp_max_val_mean = 0.1189719471023819
- gp_auc_mean = 0.10853905748211957
- gp_max_val_min = 0.08911728863908722
- hlbr = 0.08098816990191432
- high_power = 0.030000000000000002
- srmr = 0.029976019184652283
- gp_max_ix_range = 0.021181295659497088
- diff_std = 0.020000000000000004
- tdoa_max = 0.012551835778407168
- gp_auc_range = 0.012094312033909135
- ratio_max_to_10ms_ave_peaks = 0.005967209481736705
- tdoa_std = 0.0018763088091581746
- tdoa_mean = 0.0015893197711379537
- gp_max_ix_max = 0.0011804187280861594
- tdoa_range = 0.0010083258276399917
- coe3[2] = 0.0006666666666666666
- gp_max_ix_mean = 0.0005247813411078719
- ac_std = 0.00037037037037037095
- gp_max_ix_std = 0.0002502094387042723
- ratio_max_to_9th_ave_peaks = 1.6013726050900747e-05
- low_power = 0.0
- coe1[0] = 0.0
- coe1[1] = 0.0
- coe3[0] = 0.0
- coe3[1] = 0.0
- coe3[3] = 0.0
- ac_auc = 0.0
- diff_auc = 0.0
- gp_max_val_std = 0.0
- gp_max_val_range = 0.0
- gp_max_ix_min = 0.0
- gp_auc_std = 0.0
- tdoa_min = 0.0

## Evaluation
cv = 8
### accuracy
- Scores = [ 0.7, 0.8, 1.0, 0.7777777777777778, 0.7777777777777778, 0.8888888888888888, 0.6666666666666666, 1.0 ]
- Mean = 0.8263888888888888
- Standard deviation = 0.1178429458073041

### balanced_accuracy
- Scores = [ 0.8125, 0.875, 1.0, 0.8571428571428572, 0.6785714285714286, 0.9285714285714286, 0.7857142857142857, 1.0 ]
- Mean = 0.8671875
- Standard deviation = 0.10272102189254134

### f1
- Scores = [ 0.5714285714285715, 0.6666666666666666, 1.0, 0.6666666666666666, 0.5, 0.8, 0.5714285714285715, 1.0 ]
- Mean = 0.7220238095238096
- Standard deviation = 0.18076333326496616

### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 48 | 12 |
| Actual Positive | 0 | 15 |

      