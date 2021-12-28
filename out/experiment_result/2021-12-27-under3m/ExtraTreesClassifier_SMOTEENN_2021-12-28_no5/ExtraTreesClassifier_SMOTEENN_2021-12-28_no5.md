# ExtraTreesClassifier_SMOTEENN_2021-12-28_no5
## Constants
- CSV_PATH = ../out/csv/experiment
- OUTPUT_PATH = ../out/experiment_result/2021-12-27-under3m
- FEATURE_ATTRBS = ['low_power', 'high_power', 'hlbr', 'coe1[0]', 'coe1[1]', 'coe3[0]', 'coe3[1]', 'coe3[2]', 'coe3[3]', 'ratio_max_to_10ms_ave_peaks', 'ratio_max_to_9th_ave_peaks', 'ac_std', 'ac_auc', 'diff_std', 'diff_auc', 'srmr', 'gp_max_val_std', 'gp_max_val_range', 'gp_max_val_min', 'gp_max_val_max', 'gp_max_val_mean', 'gp_max_ix_std', 'gp_max_ix_range', 'gp_max_ix_min', 'gp_max_ix_max', 'gp_max_ix_mean', 'gp_auc_std', 'gp_auc_range', 'gp_auc_min', 'gp_auc_max', 'gp_auc_mean', 'tdoa_std', 'tdoa_range', 'tdoa_min', 'tdoa_max', 'tdoa_mean']
- LABEL_ATTRB = ['facing']
- FACING_DOV_ANGLES = [1]
- NCV = 8
- SCORING = ['accuracy', 'balanced_accuracy', 'f1']
- REFIT_SCORING = balanced_accuracy
- PARAM_GRID = [{'est__n_estimators': [50, 100, 150, 200, 300], 'est__min_samples_split': [2, 5, 10], 'est__min_samples_leaf': [1, 5, 10], 'est__max_features': ['sqrt', 'log2', None], 'est__bootstrap': [False], 'est__n_jobs': [-1], 'est__random_state': [42], 'est__max_samples': [0.01, 0.5, 0.09]}, {'est__n_estimators': [50, 100, 150, 200, 300], 'est__min_samples_split': [2, 5, 10], 'est__min_samples_leaf': [1, 5, 10], 'est__max_features': ['sqrt', 'log2', None], 'est__bootstrap': [True], 'est__oob_score': [True, False], 'est__n_jobs': [-1], 'est__random_state': [42], 'est__max_samples': [0.01, 0.5, 0.09]}]
- TRAIN_SET_SESSION = ['trial1', 'trial2']
- TEST_SET_SESSION = ['trial3', 'trial4', 'trial5']

## Loaded CSV
- 2021-12-27_raspi_48000Hz_w1_N2^12_overlap80_withfacing.csv

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
	- min_samples_split = 10
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

#### Importance of features
- coe1[1] = 0.14532213228501625
- coe1[0] = 0.14153251501018027
- low_power = 0.12428733839892483
- gp_auc_min = 0.10891351237363084
- coe3[3] = 0.07000294907169215
- ac_std = 0.062303602058319044
- gp_max_val_mean = 0.057888252310450125
- diff_std = 0.05507675089309083
- high_power = 0.03750942301000545
- coe3[2] = 0.035917968098180916
- ac_auc = 0.034568859775689326
- diff_auc = 0.024447089947089957
- gp_auc_max = 0.018888888888888893
- gp_max_val_max = 0.013220535434588784
- gp_max_val_min = 0.01258688622278723
- gp_auc_range = 0.01207726692209451
- gp_auc_mean = 0.010179767996186244
- hlbr = 0.009637571956120344
- tdoa_mean = 0.009450000000000002
- gp_max_ix_std = 0.00756249590995354
- tdoa_range = 0.004412047140986469
- srmr = 0.0014555256064690027
- gp_max_val_std = 0.0013793103448275852
- gp_max_val_range = 0.0013793103448275852
- coe3[0] = 0.0
- coe3[1] = 0.0
- ratio_max_to_10ms_ave_peaks = 0.0
- ratio_max_to_9th_ave_peaks = 0.0
- gp_max_ix_range = 0.0
- gp_max_ix_min = 0.0
- gp_max_ix_max = 0.0
- gp_max_ix_mean = 0.0
- gp_auc_std = 0.0
- tdoa_std = 0.0
- tdoa_min = 0.0
- tdoa_max = 0.0

## Evaluation
cv = 8
### accuracy
- Scores = [ 0.42105263157894735, 0.6842105263157895, 0.7894736842105263, 0.8421052631578947, 0.7894736842105263, 0.7222222222222222, 0.7222222222222222, 0.7222222222222222 ]
- Mean = 0.7116228070175438
- Standard deviation = 0.11972191336362795

### balanced_accuracy
- Scores = [ 0.35833333333333334, 0.8, 0.6833333333333333, 0.7166666666666667, 0.6833333333333333, 0.7321428571428572, 0.43333333333333335, 0.7 ]
- Mean = 0.6383928571428572
- Standard deviation = 0.14549493050133158

### f1
- Scores = [ 0.15384615384615383, 0.5714285714285715, 0.5, 0.5714285714285715, 0.5, 0.5454545454545454, 0.0, 0.4444444444444444 ]
- Mean = 0.4108252858252859
- Standard deviation = 0.20048755108178903

### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 90 | 29 |
| Actual Positive | 14 | 16 |

      