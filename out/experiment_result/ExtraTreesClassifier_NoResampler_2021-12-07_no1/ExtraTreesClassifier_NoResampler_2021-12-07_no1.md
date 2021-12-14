# ExtraTreesClassifier_NoResampler_2021-12-07_no1
## Constants
- CSV_PATH = ../out/csv/experiment
- OUTPUT_PATH = ../out/experiment_result
- FEATURE_ATTRBS = ['low_power', 'high_power', 'hlbr', 'coe1[0]', 'coe1[1]', 'coe3[0]', 'coe3[1]', 'coe3[2]', 'coe3[3]', 'ratio_max_to_10ms_ave_peaks', 'ratio_max_to_9th_ave_peaks', 'ac_std', 'ac_auc', 'diff_std', 'diff_auc', 'srmr', 'gp_max_val_std', 'gp_max_val_range', 'gp_max_val_min', 'gp_max_val_max', 'gp_max_val_mean', 'gp_max_ix_std', 'gp_max_ix_range', 'gp_max_ix_min', 'gp_max_ix_max', 'gp_max_ix_mean', 'gp_auc_std', 'gp_auc_range', 'gp_auc_min', 'gp_auc_max', 'gp_auc_mean', 'tdoa_std', 'tdoa_range', 'tdoa_min', 'tdoa_max', 'tdoa_mean']
- LABEL_ATTRB = ['dov_angle']
- FACING_DOV_ANGLES = [0, 45, 315]
- NCV = 8
- SCORING = ['accuracy', 'balanced_accuracy', 'f1']
- REFIT_SCORING = balanced_accuracy
- PARAM_GRID = [{'est__n_estimators': [100, 500, 1000], 'est__min_samples_split': [2, 5, 10], 'est__min_samples_leaf': [1, 5, 10], 'est__max_features': ['sqrt', 'log2', None], 'est__bootstrap': [False], 'est__n_jobs': [-1], 'est__random_state': [42], 'est__max_samples': [0.01, 0.5, 0.09]}, {'est__n_estimators': [100, 500, 1000], 'est__min_samples_split': [2, 5, 10], 'est__min_samples_leaf': [1, 5, 10], 'est__max_features': ['sqrt', 'log2', None], 'est__bootstrap': [True], 'est__oob_score': [True, False], 'est__n_jobs': [-1], 'est__random_state': [42], 'est__max_samples': [0.01, 0.5, 0.09]}]
- TRAIN_SET_SESSION = ['trial4']
- TEST_SET_SESSION = ['trial5', 'trial6']

## Loaded CSV
- 2021-12-01_mac_48000Hz_w1_N2^12_overlap80.csv

## Estimator
### Type
- resampler = NoResampler
- estimator = ExtraTreesClassifier

### Arguments for hyperparameter search
- resampler = NoResampler
- estimator = ExtraTreesClassifier
- param_grid = 
	- {'est__n_estimators': [100, 500, 1000], 'est__min_samples_split': [2, 5, 10], 'est__min_samples_leaf': [1, 5, 10], 'est__max_features': ['sqrt', 'log2', None], 'est__bootstrap': [False], 'est__n_jobs': [-1], 'est__random_state': [42], 'est__max_samples': [0.01, 0.5, 0.09]}
	- {'est__n_estimators': [100, 500, 1000], 'est__min_samples_split': [2, 5, 10], 'est__min_samples_leaf': [1, 5, 10], 'est__max_features': ['sqrt', 'log2', None], 'est__bootstrap': [True], 'est__oob_score': [True, False], 'est__n_jobs': [-1], 'est__random_state': [42], 'est__max_samples': [0.01, 0.5, 0.09]}

- scoring = ['accuracy', 'balanced_accuracy', 'f1']
- refit = balanced_accuracy
- cv = 8

### Parameters of the best estimator
#### The best hyper-parameters
- best_resampler

- best_estimator
	- base_estimator = ExtraTreeClassifier()
	- n_estimators = 100
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
	- min_samples_split = 10
	- min_samples_leaf = 1
	- min_weight_fraction_leaf = 0.0
	- max_features = log2
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
- gp_max_val_min = 0.07126080641668889
- high_power = 0.06953952315914236
- diff_std = 0.062223616483363206
- gp_auc_mean = 0.052584482717060406
- gp_max_val_mean = 0.0520095988734871
- srmr = 0.05168283113600646
- gp_auc_max = 0.05114053343109801
- gp_auc_min = 0.05086376095386048
- diff_auc = 0.04991680580533805
- gp_max_val_max = 0.04723771615475787
- hlbr = 0.038367382606649916
- coe1[0] = 0.03538957011340204
- gp_max_ix_std = 0.035210494216554845
- tdoa_range = 0.03473105577902127
- tdoa_std = 0.033278870344803355
- gp_max_val_std = 0.026602454220570847
- tdoa_max = 0.02188013205434786
- gp_auc_range = 0.017755739134553986
- ac_std = 0.017563998939217926
- gp_max_ix_min = 0.017061410871364414
- gp_max_ix_max = 0.016902088744840123
- gp_max_val_range = 0.016689537041300634
- gp_auc_std = 0.01573239023867566
- coe3[3] = 0.01562977257309519
- coe1[1] = 0.01512855526213031
- low_power = 0.014939754076658367
- gp_max_ix_range = 0.014852056976524006
- coe3[2] = 0.013064301862403814
- gp_max_ix_mean = 0.01092328283317867
- tdoa_min = 0.009758595044309183
- tdoa_mean = 0.0065835895569180515
- ac_auc = 0.005954808867713265
- ratio_max_to_9th_ave_peaks = 0.0058732812814318615
- ratio_max_to_10ms_ave_peaks = 0.001667202229531623
- coe3[0] = 0.0
- coe3[1] = 0.0

## Evaluation
cv = 8
### accuracy
- Scores = [ 0.8333333333333334, 0.9166666666666666, 0.8333333333333334, 0.8333333333333334, 0.8333333333333334, 0.9166666666666666, 0.75, 0.9166666666666666 ]
- Mean = 0.8541666666666667
- Standard deviation = 0.05511981898051228

### balanced_accuracy
- Scores = [ 0.8285714285714285, 0.9, 0.8285714285714285, 0.8285714285714285, 0.8125, 0.9375, 0.625, 0.875 ]
- Mean = 0.8294642857142858
- Standard deviation = 0.08718968296952645

### f1
- Scores = [ 0.8000000000000002, 0.888888888888889, 0.8000000000000002, 0.8000000000000002, 0.75, 0.888888888888889, 0.4, 0.8571428571428571 ]
- Mean = 0.7731150793650794
- Standard deviation = 0.14823350818804584

### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 55 | 5 |
| Actual Positive | 9 | 27 |

      