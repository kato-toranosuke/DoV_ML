# ExtraTreesClassifier_SMOTETomek_2022-01-10_no6
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
	- oob_decision_function_ = [[0.23935253 0.76064747]
 [0.30036901 0.69963099]
 [0.37494422 0.62505578]
 [0.65193175 0.34806825]
 [0.78096717 0.21903283]
 [0.79445698 0.20554302]
 [0.80895446 0.19104554]
 [0.79489163 0.20510837]
 [0.80234088 0.19765912]
 [0.81080995 0.18919005]
 [0.70752904 0.29247096]
 [0.31932833 0.68067167]
 [0.31032236 0.68967764]
 [0.33439317 0.66560683]
 [0.29712806 0.70287194]
 [0.80876417 0.19123583]
 [0.80504145 0.19495855]
 [0.73887439 0.26112561]
 [0.71276327 0.28723673]
 [0.58858372 0.41141628]
 [0.20319053 0.79680947]
 [0.20814304 0.79185696]
 [0.71440408 0.28559592]
 [0.63407851 0.36592149]
 [0.80137369 0.19862631]
 [0.81055846 0.18944154]
 [0.82902949 0.17097051]
 [0.8078089  0.1921911 ]
 [0.74781443 0.25218557]
 [0.82662256 0.17337744]
 [0.64595957 0.35404043]
 [0.61657625 0.38342375]
 [0.37803347 0.62196653]
 [0.41195624 0.58804376]
 [0.42340768 0.57659232]
 [0.58543653 0.41456347]
 [0.8389848  0.1610152 ]
 [0.75870485 0.24129515]
 [0.70814516 0.29185484]
 [0.65438394 0.34561606]
 [0.29001651 0.70998349]
 [0.27405027 0.72594973]
 [0.21839832 0.78160168]
 [0.19910397 0.80089603]
 [0.21395584 0.78604416]
 [0.21113493 0.78886507]
 [0.31540871 0.68459129]
 [0.32839735 0.67160265]
 [0.31595425 0.68404575]
 [0.32085811 0.67914189]
 [0.40271248 0.59728752]
 [0.26931184 0.73068816]
 [0.23197964 0.76802036]
 [0.22979804 0.77020196]
 [0.20700878 0.79299122]
 [0.20943128 0.79056872]
 [0.25247728 0.74752272]
 [0.24123725 0.75876275]
 [0.20793353 0.79206647]
 [0.22277189 0.77722811]
 [0.36797783 0.63202217]
 [0.22372814 0.77627186]
 [0.22365888 0.77634112]
 [0.29502043 0.70497957]]
	- oob_score_ = 0.9375

#### Importance of features
- gp_max_val_mean = 0.11409395973154363
- tdoa_max = 0.10067114093959731
- gp_max_val_max = 0.09395973154362416
- gp_auc_max = 0.09395973154362416
- gp_max_val_min = 0.087248322147651
- gp_auc_min = 0.08053691275167785
- gp_auc_mean = 0.08053691275167785
- hlbr = 0.06711409395973154
- srmr = 0.06711409395973154
- gp_max_ix_max = 0.040268456375838924
- diff_auc = 0.03355704697986577
- gp_max_ix_range = 0.03355704697986577
- coe3[3] = 0.013422818791946308
- ratio_max_to_9th_ave_peaks = 0.013422818791946308
- gp_max_val_range = 0.013422818791946308
- tdoa_range = 0.013422818791946308
- low_power = 0.006711409395973154
- high_power = 0.006711409395973154
- coe3[2] = 0.006711409395973154
- ac_auc = 0.006711409395973154
- diff_std = 0.006711409395973154
- gp_max_val_std = 0.006711409395973154
- gp_max_ix_std = 0.006711409395973154
- gp_auc_range = 0.006711409395973154
- coe1[0] = 0.0
- coe1[1] = 0.0
- coe3[0] = 0.0
- coe3[1] = 0.0
- ratio_max_to_10ms_ave_peaks = 0.0
- ac_std = 0.0
- gp_max_ix_min = 0.0
- gp_max_ix_mean = 0.0
- gp_auc_std = 0.0
- tdoa_std = 0.0
- tdoa_min = 0.0
- tdoa_mean = 0.0

## Evaluation
cv = 8
### accuracy
- Scores = [ 0.7, 0.8, 1.0, 1.0, 0.8888888888888888, 0.8888888888888888, 0.6666666666666666, 1.0 ]
- Mean = 0.8680555555555556
- Standard deviation = 0.1257615689398881

### balanced_accuracy
- Scores = [ 0.8125, 0.875, 1.0, 1.0, 0.75, 0.9285714285714286, 0.7857142857142857, 1.0 ]
- Mean = 0.8939732142857143
- Standard deviation = 0.09641591145399758

### f1
- Scores = [ 0.5714285714285715, 0.6666666666666666, 1.0, 1.0, 0.6666666666666666, 0.8, 0.5714285714285715, 1.0 ]
- Mean = 0.7845238095238096
- Standard deviation = 0.1796278276397759

### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 49 | 11 |
| Actual Positive | 0 | 15 |

      