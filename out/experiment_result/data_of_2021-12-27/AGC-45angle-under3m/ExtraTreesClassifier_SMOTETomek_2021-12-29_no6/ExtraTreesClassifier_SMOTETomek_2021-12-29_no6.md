# ExtraTreesClassifier_SMOTETomek_2021-12-29_no6
## Constants
- CSV_PATH = ../out/csv/experiment
- OUTPUT_PATH = ../out/experiment_result/data_of_2021-12-27/AGC-45angle-under3m
- FEATURE_ATTRBS = ['low_power', 'high_power', 'hlbr', 'coe1[0]', 'coe1[1]', 'coe3[0]', 'coe3[1]', 'coe3[2]', 'coe3[3]', 'ratio_max_to_10ms_ave_peaks', 'ratio_max_to_9th_ave_peaks', 'ac_std', 'ac_auc', 'diff_std', 'diff_auc', 'srmr', 'gp_max_val_std', 'gp_max_val_range', 'gp_max_val_min', 'gp_max_val_max', 'gp_max_val_mean', 'gp_max_ix_std', 'gp_max_ix_range', 'gp_max_ix_min', 'gp_max_ix_max', 'gp_max_ix_mean', 'gp_auc_std', 'gp_auc_range', 'gp_auc_min', 'gp_auc_max', 'gp_auc_mean', 'tdoa_std', 'tdoa_range', 'tdoa_min', 'tdoa_max', 'tdoa_mean']
- LABEL_ATTRB = ['facing2']
- FACING_DOV_ANGLES = [1, 2]
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
- resampler = SMOTETomek
- estimator = ExtraTreesClassifier

### Arguments for hyperparameter search
- resampler = SMOTETomek
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
	- tomek = None
	- n_jobs = -1
	- n_features_in_ = 36
	- sampling_strategy_ = auto
	- smote_ = SMOTE(n_jobs=-1, random_state=42)
	- tomek_ = TomekLinks(n_jobs=-1, sampling_strategy='all')

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
	- oob_decision_function_ = [[0.34814815 0.65185185]
 [0.30215827 0.69784173]
 [0.28148148 0.71851852]
 [0.18439716 0.81560284]
 [0.17910448 0.82089552]
 [0.90070922 0.09929078]
 [0.87218045 0.12781955]
 [0.20895522 0.79104478]
 [0.3203125  0.6796875 ]
 [0.14788732 0.85211268]
 [0.69064748 0.30935252]
 [0.91304348 0.08695652]
 [0.84558824 0.15441176]
 [0.38461538 0.61538462]
 [0.31428571 0.68571429]
 [0.26428571 0.73571429]
 [0.45588235 0.54411765]
 [0.69285714 0.30714286]
 [0.95348837 0.04651163]
 [0.93478261 0.06521739]
 [0.53146853 0.46853147]
 [0.16058394 0.83941606]
 [0.08955224 0.91044776]
 [0.10948905 0.89051095]
 [0.67175573 0.32824427]
 [0.69852941 0.30147059]
 [0.92753623 0.07246377]
 [0.91851852 0.08148148]
 [0.79562044 0.20437956]
 [0.85185185 0.14814815]
 [0.3115942  0.6884058 ]
 [0.28571429 0.71428571]
 [0.25735294 0.74264706]
 [0.24087591 0.75912409]
 [0.15441176 0.84558824]
 [0.20979021 0.79020979]
 [0.61940299 0.38059701]
 [0.55797101 0.44202899]
 [0.48507463 0.51492537]
 [0.21481481 0.78518519]
 [0.0962963  0.9037037 ]
 [0.21804511 0.78195489]
 [0.16176471 0.83823529]
 [0.67669173 0.32330827]
 [0.92198582 0.07801418]
 [0.94160584 0.05839416]
 [0.05384615 0.94615385]
 [0.08633094 0.91366906]
 [0.27272727 0.72727273]
 [0.90225564 0.09774436]
 [0.86567164 0.13432836]
 [0.78169014 0.21830986]
 [0.19852941 0.80147059]
 [0.1119403  0.8880597 ]
 [0.10144928 0.89855072]
 [0.0942029  0.9057971 ]
 [0.2238806  0.7761194 ]
 [0.13868613 0.86131387]
 [0.90441176 0.09558824]
 [0.91549296 0.08450704]
 [0.91729323 0.08270677]
 [0.87969925 0.12030075]
 [0.72992701 0.27007299]
 [0.18382353 0.81617647]
 [0.1048951  0.8951049 ]
 [0.94927536 0.05072464]
 [0.94776119 0.05223881]
 [0.78676471 0.21323529]
 [0.35416667 0.64583333]
 [0.15555556 0.84444444]
 [0.87596899 0.12403101]
 [0.75373134 0.24626866]
 [0.87022901 0.12977099]
 [0.82638889 0.17361111]]
	- oob_score_ = 0.9459459459459459

#### Importance of features
- gp_max_val_min = 0.10973173515981736
- gp_max_val_mean = 0.1083904109589041
- srmr = 0.09988584474885845
- gp_auc_min = 0.09885844748858447
- gp_auc_mean = 0.08969748858447489
- gp_auc_max = 0.05779109589041096
- coe1[1] = 0.05194063926940639
- ratio_max_to_10ms_ave_peaks = 0.04223744292237443
- coe1[0] = 0.03809931506849315
- high_power = 0.03724315068493151
- gp_max_val_max = 0.03710045662100457
- diff_std = 0.036301369863013695
- diff_auc = 0.03424657534246575
- low_power = 0.030251141552511417
- coe3[3] = 0.023544520547945206
- gp_max_ix_mean = 0.0136986301369863
- gp_auc_range = 0.013042237442922374
- hlbr = 0.010702054794520547
- ratio_max_to_9th_ave_peaks = 0.009845890410958904
- ac_auc = 0.00684931506849315
- gp_max_ix_std = 0.00684931506849315
- gp_max_ix_max = 0.00684931506849315
- tdoa_range = 0.00684931506849315
- tdoa_min = 0.00684931506849315
- tdoa_max = 0.0067066210045662105
- gp_max_val_range = 0.006392694063926939
- tdoa_std = 0.003852739726027397
- gp_max_ix_range = 0.00319634703196347
- coe3[2] = 0.0029965753424657533
- coe3[0] = 0.0
- coe3[1] = 0.0
- ac_std = 0.0
- gp_max_val_std = 0.0
- gp_max_ix_min = 0.0
- gp_auc_std = 0.0
- tdoa_mean = 0.0

## Evaluation
cv = 8
### accuracy
- Scores = [ 0.8421052631578947, 1.0, 0.9473684210526315, 0.9473684210526315, 1.0, 1.0, 0.8888888888888888, 0.8888888888888888 ]
- Mean = 0.9393274853801169
- Standard deviation = 0.05669329756430189

### balanced_accuracy
- Scores = [ 0.8333333333333333, 1.0, 0.95, 0.9444444444444444, 1.0, 1.0, 0.8888888888888888, 0.8888888888888888 ]
- Mean = 0.9381944444444444
- Standard deviation = 0.05862608418539979

### f1
- Scores = [ 0.8695652173913044, 1.0, 0.9473684210526316, 0.9523809523809523, 1.0, 1.0, 0.8750000000000001, 0.8750000000000001 ]
- Mean = 0.939914323853111
- Standard deviation = 0.055247829695592214

### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 67 | 4 |
| Actual Positive | 5 | 73 |

      