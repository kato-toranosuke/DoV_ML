# RandomForestClassifier_SMOTE_2021-11-12_no3
## Constants
- CSV_PATH = ../../out/csv/
- OUTPUT_PATH = ./result/
- FEATURE_ATTRBS = ['low_power', 'high_power', 'hlbr', 'coe1[0]', 'coe1[1]', 'coe3[0]', 'coe3[1]', 'coe3[2]', 'coe3[3]', 'ratio_max_to_10ms_ave_peaks', 'ratio_max_to_9th_ave_peaks', 'ac_std', 'ac_auc', 'diff_std', 'diff_auc', 'srmr', 'gp_max_val_std', 'gp_max_val_range', 'gp_max_val_min', 'gp_max_val_max', 'gp_max_val_mean', 'gp_max_ix_std', 'gp_max_ix_range', 'gp_max_ix_min', 'gp_max_ix_max', 'gp_max_ix_mean', 'gp_auc_std', 'gp_auc_range', 'gp_auc_min', 'gp_auc_max', 'gp_auc_mean', 'tdoa_std', 'tdoa_range', 'tdoa_min', 'tdoa_max', 'tdoa_mean']
- LABEL_ATTRB = ['dov_angle']
- FACING_DOV_ANGLES = [0, 45, 315]
- NCV = 10
- SCORING = ['accuracy', 'balanced_accuracy', 'f1']
- REFIT_SCORING = balanced_accuracy
- PARAM_GRID = [{'est__n_estimators': [10, 100, 500, 800, 1000], 'est__min_samples_split': [2, 5, 10], 'est__min_samples_leaf': [1, 5, 10], 'est__max_features': ['sqrt', 'log2', None], 'est__bootstrap': [False], 'est__n_jobs': [-1], 'est__random_state': [42], 'est__max_samples': [0.01, 0.5, 0.09]}, {'est__n_estimators': [10, 100, 500, 800, 1000], 'est__min_samples_split': [2, 5, 10], 'est__min_samples_leaf': [1, 5, 10], 'est__max_features': ['sqrt', 'log2', None], 'est__bootstrap': [True], 'est__oob_score': [True, False], 'est__n_jobs': [-1], 'est__random_state': [42], 'est__max_samples': [0.01, 0.5, 0.09]}]

## Loaded CSV
- features_mono_ch_python.csv

## Estimator
### Type
- resampler = SMOTE
- estimator = RandomForestClassifier

### Arguments for hyperparameter search
- resampler = SMOTE
- estimator = RandomForestClassifier
- param_grid = 
	- {'est__n_estimators': [10, 100, 500, 800, 1000], 'est__min_samples_split': [2, 5, 10], 'est__min_samples_leaf': [1, 5, 10], 'est__max_features': ['sqrt', 'log2', None], 'est__bootstrap': [False], 'est__n_jobs': [-1], 'est__random_state': [42], 'est__max_samples': [0.01, 0.5, 0.09]}
	- {'est__n_estimators': [10, 100, 500, 800, 1000], 'est__min_samples_split': [2, 5, 10], 'est__min_samples_leaf': [1, 5, 10], 'est__max_features': ['sqrt', 'log2', None], 'est__bootstrap': [True], 'est__oob_score': [True, False], 'est__n_jobs': [-1], 'est__random_state': [42], 'est__max_samples': [0.01, 0.5, 0.09]}

- scoring = ['accuracy', 'balanced_accuracy', 'f1']
- refit = balanced_accuracy
- cv = 10

### Parameters of the best estimator
#### The best hyper-parameters
- best_resampler
	- sampling_strategy = auto
	- random_state = 42
	- k_neighbors = 5
	- n_jobs = -1
	- n_features_in_ = 36
	- sampling_strategy_ = OrderedDict([(1, 1440)])
	- nn_k_ = NearestNeighbors(n_neighbors=6)

- best_estimator
	- base_estimator = DecisionTreeClassifier()
	- n_estimators = 500
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
	- min_samples_split = 2
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
	- base_estimator_ = DecisionTreeClassifier()

#### Importance of features
- gp_max_val_mean = 0.1322519174780688
- gp_max_val_max = 0.10798864345738773
- high_power = 0.0725314415751968
- gp_max_val_min = 0.06133499593076914
- gp_max_val_range = 0.04601952093230821
- gp_max_val_std = 0.042407454444810484
- hlbr = 0.0415277105691841
- diff_std = 0.03269550011571994
- gp_max_ix_std = 0.02821671769680546
- gp_max_ix_mean = 0.027344958451209232
- diff_auc = 0.027187201960164456
- srmr = 0.026932910968099633
- tdoa_mean = 0.025864075585640234
- tdoa_std = 0.022170348405015538
- ac_auc = 0.021992849034756595
- gp_max_ix_min = 0.01974252805552226
- coe1[1] = 0.019706338425378084
- ratio_max_to_10ms_ave_peaks = 0.019659484671557117
- gp_max_ix_max = 0.018657117694372866
- tdoa_min = 0.018524290011816474
- tdoa_range = 0.018034019352618585
- gp_max_ix_range = 0.017971603769040067
- low_power = 0.017921770431698087
- ac_std = 0.0178478116444035
- ratio_max_to_9th_ave_peaks = 0.017647949286446234
- tdoa_max = 0.017240397691993856
- coe3[3] = 0.016547980924326654
- gp_auc_max = 0.013065547578961329
- gp_auc_min = 0.012009626390985396
- coe3[2] = 0.011735092120629703
- gp_auc_mean = 0.01114629554022677
- gp_auc_range = 0.009329135408366858
- gp_auc_std = 0.004631237489436911
- coe1[0] = 0.0021155269070829365
- coe3[0] = 0.0
- coe3[1] = 0.0

## Evaluation
cv = 10
### accuracy
- Scores = [ 0.765625, 0.8715277777777778, 0.8836805555555556, 0.8472222222222222, 0.8663194444444444, 0.8020833333333334, 0.8506944444444444, 0.8177083333333334, 0.8802083333333334, 0.7673611111111112 ]
- Mean = 0.8352430555555556
- Standard deviation = 0.04230165739044269

### balanced_accuracy
- Scores = [ 0.8023148148148148, 0.8657407407407407, 0.8736111111111111, 0.8157407407407407, 0.8449074074074074, 0.7564814814814815, 0.8638888888888889, 0.7884259259259259, 0.8652777777777778, 0.6962962962962963 ]
- Mean = 0.8172685185185186
- Standard deviation = 0.05491218906791508

### f1
- Scores = [ 0.7522935779816514, 0.8310502283105022, 0.8430913348946135, 0.7720207253886009, 0.8098765432098766, 0.6850828729281768, 0.8215767634854771, 0.7341772151898733, 0.8345323741007193, 0.5705128205128205 ]
- Mean = 0.7654214456002312
- Standard deviation = 0.08116741736671726

### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 3201 | 399 |
| Actual Positive | 550 | 1610 |

      