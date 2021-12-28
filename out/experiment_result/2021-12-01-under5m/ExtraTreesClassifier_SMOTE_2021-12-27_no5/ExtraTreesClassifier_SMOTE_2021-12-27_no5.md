# ExtraTreesClassifier_SMOTE_2021-12-27_no5
## Constants
- CSV_PATH = ../out/csv/experiment
- OUTPUT_PATH = ../out/experiment_result
- FEATURE_ATTRBS = ['low_power', 'high_power', 'hlbr', 'coe1[0]', 'coe1[1]', 'coe3[0]', 'coe3[1]', 'coe3[2]', 'coe3[3]', 'ratio_max_to_10ms_ave_peaks', 'ratio_max_to_9th_ave_peaks', 'ac_std', 'ac_auc', 'diff_std', 'diff_auc', 'srmr', 'gp_max_val_std', 'gp_max_val_range', 'gp_max_val_min', 'gp_max_val_max', 'gp_max_val_mean', 'gp_max_ix_std', 'gp_max_ix_range', 'gp_max_ix_min', 'gp_max_ix_max', 'gp_max_ix_mean', 'gp_auc_std', 'gp_auc_range', 'gp_auc_min', 'gp_auc_max', 'gp_auc_mean', 'tdoa_std', 'tdoa_range', 'tdoa_min', 'tdoa_max', 'tdoa_mean']
- LABEL_ATTRB = ['dov_angle']
- FACING_DOV_ANGLES = [0]
- NCV = 8
- SCORING = ['accuracy', 'balanced_accuracy', 'f1']
- REFIT_SCORING = balanced_accuracy
- PARAM_GRID = [{'est__n_estimators': [50, 100, 150, 200, 300], 'est__min_samples_split': [2, 5, 10], 'est__min_samples_leaf': [1, 5, 10], 'est__max_features': ['sqrt', 'log2', None], 'est__bootstrap': [False], 'est__n_jobs': [-1], 'est__random_state': [42], 'est__max_samples': [0.01, 0.5, 0.09]}, {'est__n_estimators': [50, 100, 150, 200, 300], 'est__min_samples_split': [2, 5, 10], 'est__min_samples_leaf': [1, 5, 10], 'est__max_features': ['sqrt', 'log2', None], 'est__bootstrap': [True], 'est__oob_score': [True, False], 'est__n_jobs': [-1], 'est__random_state': [42], 'est__max_samples': [0.01, 0.5, 0.09]}]
- TRAIN_SET_SESSION = ['trial1']
- TEST_SET_SESSION = ['trial2', 'trial3']

## Loaded CSV
- 2021-12-01_mac_48000Hz_w1_N2^12_overlap80.csv

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
	- sampling_strategy_ = OrderedDict([(1, 54)])
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
	- max_samples = 0.09
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
	- oob_decision_function_ = [[0.2508467  0.7491533 ]
 [0.41201299 0.58798701]
 [0.70291971 0.29708029]
 [0.63335482 0.36664518]
 [0.74060606 0.25939394]
 [0.5972898  0.4027102 ]
 [0.43444976 0.56555024]
 [0.30813397 0.69186603]
 [0.24526949 0.75473051]
 [0.26304302 0.73695698]
 [0.70482684 0.29517316]
 [0.63799869 0.36200131]
 [0.6711682  0.3288318 ]
 [0.69033949 0.30966051]
 [0.46629605 0.53370395]
 [0.22354978 0.77645022]
 [0.33690236 0.66309764]
 [0.38931764 0.61068236]
 [0.64762551 0.35237449]
 [0.73205628 0.26794372]
 [0.77283323 0.22716677]
 [0.61276266 0.38723734]
 [0.41879666 0.58120334]
 [0.37526738 0.62473262]
 [0.51575295 0.48424705]
 [0.70204216 0.29795784]
 [0.61919192 0.38080808]
 [0.77241302 0.22758698]
 [0.6001106  0.3998894 ]
 [0.79385092 0.20614908]
 [0.5462987  0.4537013 ]
 [0.41168831 0.58831169]
 [0.41057288 0.58942712]
 [0.52125572 0.47874428]
 [0.70935634 0.29064366]
 [0.72816275 0.27183725]
 [0.76413778 0.23586222]
 [0.7653127  0.2346873 ]
 [0.66503844 0.33496156]
 [0.18964831 0.81035169]
 [0.28195387 0.71804613]
 [0.28285844 0.71714156]
 [0.59938958 0.40061042]
 [0.77265993 0.22734007]
 [0.64259496 0.35740504]
 [0.74569964 0.25430036]
 [0.59803377 0.40196623]
 [0.56052189 0.43947811]
 [0.48163861 0.51836139]
 [0.63844414 0.36155586]
 [0.74741533 0.25258467]
 [0.7573837  0.2426163 ]
 [0.69521886 0.30478114]
 [0.76458616 0.23541384]
 [0.76045123 0.23954877]
 [0.41957532 0.58042468]
 [0.44554433 0.55445567]
 [0.68074866 0.31925134]
 [0.72225936 0.27774064]
 [0.73895792 0.26104208]
 [0.69938516 0.30061484]
 [0.68001337 0.31998663]
 [0.69338642 0.30661358]
 [0.59725516 0.40274484]
 [0.54960017 0.45039983]
 [0.69914977 0.30085023]
 [0.77492915 0.22507085]
 [0.69037037 0.30962963]
 [0.7418846  0.2581154 ]
 [0.76003513 0.23996487]
 [0.73319454 0.26680546]
 [0.62388592 0.37611408]
 [0.23923445 0.76076555]
 [0.20516196 0.79483804]
 [0.21803138 0.78196862]
 [0.37490397 0.62509603]
 [0.24775575 0.75224425]
 [0.28697191 0.71302809]
 [0.30891775 0.69108225]
 [0.54502472 0.45497528]
 [0.37857448 0.62142552]
 [0.25120549 0.74879451]
 [0.25045561 0.74954439]
 [0.38900433 0.61099567]
 [0.28565062 0.71434938]
 [0.40406866 0.59593134]
 [0.3773911  0.6226089 ]
 [0.23576203 0.76423797]
 [0.32381594 0.67618406]
 [0.29495687 0.70504313]
 [0.3557405  0.6442595 ]
 [0.24536607 0.75463393]
 [0.22383838 0.77616162]
 [0.33741171 0.66258829]
 [0.34815062 0.65184938]
 [0.37109222 0.62890778]
 [0.51689557 0.48310443]
 [0.32337344 0.67662656]
 [0.28730786 0.71269214]
 [0.2527668  0.7472332 ]
 [0.33750549 0.66249451]
 [0.28440348 0.71559652]
 [0.30959965 0.69040035]
 [0.2703168  0.7296832 ]
 [0.49226827 0.50773173]
 [0.22873338 0.77126662]
 [0.48566689 0.51433311]
 [0.27828283 0.72171717]
 [0.43381543 0.56618457]
 [0.25775803 0.74224197]
 [0.25607167 0.74392833]
 [0.25887767 0.74112233]
 [0.36677412 0.63322588]
 [0.45010522 0.54989478]
 [0.24422906 0.75577094]
 [0.32438228 0.67561772]
 [0.31685468 0.68314532]
 [0.43887767 0.56112233]
 [0.31182723 0.68817277]
 [0.26114719 0.73885281]
 [0.46392391 0.53607609]
 [0.27715107 0.72284893]
 [0.21939836 0.78060164]
 [0.25452267 0.74547733]
 [0.23541126 0.76458874]
 [0.4380325  0.5619675 ]]
	- oob_score_ = 0.8650793650793651

#### Importance of features
- low_power = 0.0915492957746479
- coe1[1] = 0.06338028169014086
- coe1[0] = 0.05633802816901409
- gp_auc_std = 0.05633802816901409
- gp_auc_max = 0.05633802816901409
- gp_auc_min = 0.04929577464788733
- diff_std = 0.04225352112676057
- gp_max_val_std = 0.04225352112676057
- gp_max_val_range = 0.04225352112676057
- gp_max_val_max = 0.03521126760563381
- gp_auc_mean = 0.03521126760563381
- tdoa_max = 0.03521126760563381
- high_power = 0.028169014084507046
- ratio_max_to_9th_ave_peaks = 0.028169014084507046
- ac_std = 0.028169014084507046
- diff_auc = 0.028169014084507046
- gp_auc_range = 0.028169014084507046
- coe3[2] = 0.021126760563380285
- coe3[3] = 0.021126760563380285
- ratio_max_to_10ms_ave_peaks = 0.021126760563380285
- gp_max_ix_std = 0.021126760563380285
- gp_max_ix_range = 0.021126760563380285
- tdoa_mean = 0.021126760563380285
- ac_auc = 0.014084507042253523
- gp_max_val_min = 0.014084507042253523
- gp_max_ix_min = 0.014084507042253523
- gp_max_ix_max = 0.014084507042253523
- gp_max_ix_mean = 0.014084507042253523
- tdoa_std = 0.014084507042253523
- tdoa_range = 0.014084507042253523
- hlbr = 0.007042253521126762
- srmr = 0.007042253521126762
- gp_max_val_mean = 0.007042253521126762
- tdoa_min = 0.007042253521126762
- coe3[0] = 0.0
- coe3[1] = 0.0

## Evaluation
cv = 8
### accuracy
- Scores = [ 0.8333333333333334, 0.8333333333333334, 0.8888888888888888, 0.8888888888888888, 0.8888888888888888, 0.8888888888888888, 0.8888888888888888, 0.8888888888888888 ]
- Mean = 0.875
- Standard deviation = 0.02405626121623437

### balanced_accuracy
- Scores = [ 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5 ]
- Mean = 0.5
- Standard deviation = 0.0

### f1
- Scores = [ 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0 ]
- Mean = 0.0
- Standard deviation = 0.0

### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 126 | 0 |
| Actual Positive | 18 | 0 |

      