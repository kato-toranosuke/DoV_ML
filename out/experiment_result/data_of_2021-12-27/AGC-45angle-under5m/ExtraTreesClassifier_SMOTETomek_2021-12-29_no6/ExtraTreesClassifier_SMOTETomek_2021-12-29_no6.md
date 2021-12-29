# ExtraTreesClassifier_SMOTETomek_2021-12-29_no6
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
	- n_estimators = 50
	- estimator_params = ('criterion', 'max_depth', 'min_samples_split', 'min_samples_leaf', 'min_weight_fraction_leaf', 'max_features', 'max_leaf_nodes', 'min_impurity_decrease', 'min_impurity_split', 'random_state', 'ccp_alpha')
	- bootstrap = False
	- oob_score = False
	- n_jobs = -1
	- random_state = 42
	- verbose = 0
	- warm_start = False
	- class_weight = None
	- max_samples = 0.01
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

#### Importance of features
- gp_auc_max = 0.10491098970316244
- diff_auc = 0.10133353233764097
- gp_auc_min = 0.0875419269376774
- coe1[0] = 0.06336470584485374
- gp_max_val_min = 0.057224996795377195
- high_power = 0.053341756793856505
- gp_max_val_mean = 0.05042050886352372
- gp_auc_mean = 0.043391711882260785
- coe1[1] = 0.04279185660363508
- gp_max_val_max = 0.039115309779787305
- coe3[3] = 0.03828786908455279
- diff_std = 0.027107005933710238
- low_power = 0.026811315560438753
- coe3[2] = 0.026512320978824704
- srmr = 0.025506266341316006
- ratio_max_to_10ms_ave_peaks = 0.02025682443110601
- hlbr = 0.018785592279117382
- tdoa_min = 0.018399667641890292
- gp_max_ix_range = 0.01700945984031615
- gp_max_ix_std = 0.016397751059996715
- tdoa_std = 0.016331937555399204
- gp_max_ix_min = 0.013605819612231462
- ac_auc = 0.013174992891619617
- ac_std = 0.011858821781493091
- gp_max_ix_mean = 0.011372207071816045
- tdoa_mean = 0.00925810137286845
- gp_max_val_std = 0.00779774120718453
- gp_auc_range = 0.007736248310429915
- ratio_max_to_9th_ave_peaks = 0.005625358987340319
- gp_max_val_range = 0.0055593659380538405
- gp_max_ix_max = 0.0053360613117630195
- tdoa_range = 0.005190637605767678
- gp_auc_std = 0.004522503661356396
- tdoa_max = 0.004118833999632409
- coe3[0] = 0.0
- coe3[1] = 0.0

## Evaluation
cv = 8
### accuracy
- Scores = [ 0.8928571428571429, 0.8214285714285714, 0.8214285714285714, 0.9642857142857143, 0.8928571428571429, 0.9642857142857143, 0.9642857142857143, 0.9642857142857143 ]
- Mean = 0.9107142857142857
- Standard deviation = 0.05922544268491787

### balanced_accuracy
- Scores = [ 0.8846153846153846, 0.8179487179487179, 0.823076923076923, 0.9615384615384616, 0.9, 0.9642857142857143, 0.9642857142857143, 0.9642857142857143 ]
- Mean = 0.9100045787545787
- Standard deviation = 0.059445844791548345

### f1
- Scores = [ 0.9090909090909091, 0.8387096774193549, 0.8275862068965518, 0.967741935483871, 0.888888888888889, 0.962962962962963, 0.9655172413793104, 0.962962962962963 ]
- Mean = 0.9154325981356015
- Standard deviation = 0.054898986740852126

### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 97 | 10 |
| Actual Positive | 10 | 107 |

      