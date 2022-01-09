# ExtraTreesClassifier_SMOTETomek_2022-01-09_no6
## Constants
- CSV_PATH = ../out/csv/experiment
- OUTPUT_PATH = ../out/experiment_result/data_of_2022-01-07_new/AGC-45angle-under5m
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
- 2021-12-27_raspi_48000Hz_w1_N2^12_overlap80_with2022-01-07.csv

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
	- n_estimators = 100
	- estimator_params = ('criterion', 'max_depth', 'min_samples_split', 'min_samples_leaf', 'min_weight_fraction_leaf', 'max_features', 'max_leaf_nodes', 'min_impurity_decrease', 'random_state', 'ccp_alpha')
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
	- max_features = sqrt
	- max_leaf_nodes = None
	- min_impurity_decrease = 0.0
	- ccp_alpha = 0.0
	- n_features_in_ = 36
	- n_outputs_ = 1
	- classes_ = [0 1]
	- n_classes_ = 2
	- base_estimator_ = ExtraTreeClassifier()

#### Importance of features
- gp_max_val_mean = 0.08369073348844504
- gp_max_val_min = 0.07591780693925083
- diff_auc = 0.07197854388853643
- gp_auc_min = 0.07056371407123042
- gp_auc_max = 0.06954394497036048
- diff_std = 0.048675926276960886
- gp_auc_mean = 0.0482234831478044
- gp_max_val_max = 0.04815430401612571
- high_power = 0.045167901714399716
- coe1[1] = 0.043789625205707165
- coe3[3] = 0.03391755392884469
- coe1[0] = 0.030966601366395966
- hlbr = 0.02944211899129438
- ac_auc = 0.02858232759291453
- low_power = 0.027259746672469307
- ratio_max_to_10ms_ave_peaks = 0.02642382378645573
- srmr = 0.0189173929965955
- coe3[2] = 0.017316110859507437
- gp_max_ix_std = 0.016477444600855096
- gp_max_ix_range = 0.015260821106946931
- tdoa_min = 0.014540036541476986
- tdoa_range = 0.01431009412143563
- ac_std = 0.014005742306178827
- gp_max_ix_mean = 0.013572906811131479
- gp_auc_range = 0.013089273931720739
- gp_max_val_std = 0.01180798923371387
- tdoa_mean = 0.011516804741557618
- gp_max_val_range = 0.011185447327948827
- gp_max_ix_min = 0.010890840148027603
- gp_auc_std = 0.010796262384647731
- tdoa_std = 0.009217944569846516
- gp_max_ix_max = 0.006528069571588267
- tdoa_max = 0.004961356131094791
- ratio_max_to_9th_ave_peaks = 0.0033073065585305494
- coe3[0] = 0.0
- coe3[1] = 0.0

## Evaluation
cv = 8
### accuracy
- Scores = [ 0.8620689655172413, 0.8928571428571429, 0.8928571428571429, 0.9642857142857143, 0.8571428571428571, 1.0, 1.0, 1.0 ]
- Mean = 0.9336514778325123
- Standard deviation = 0.059635157694375496

### balanced_accuracy
- Scores = [ 0.8571428571428572, 0.8948717948717949, 0.9, 0.9666666666666667, 0.8615384615384616, 1.0, 1.0, 1.0 ]
- Mean = 0.9350274725274725
- Standard deviation = 0.059130551445175726

### f1
- Scores = [ 0.8823529411764706, 0.896551724137931, 0.888888888888889, 0.9655172413793104, 0.8571428571428571, 1.0, 1.0, 1.0 ]
- Mean = 0.9363067065906823
- Standard deviation = 0.057042302444986766

### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 101 | 7 |
| Actual Positive | 8 | 109 |

      