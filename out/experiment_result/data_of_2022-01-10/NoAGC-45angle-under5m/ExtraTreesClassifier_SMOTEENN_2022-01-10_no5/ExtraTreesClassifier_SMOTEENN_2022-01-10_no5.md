# ExtraTreesClassifier_SMOTEENN_2022-01-10_no5
## Constants
- CSV_PATH = ../out/csv/experiment
- OUTPUT_PATH = ../out/experiment_result/data_of_2022-01-10/NoAGC-45angle-under5m
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
- AGC_STATUS = ['NoAGC']

## Loaded CSV
- 2022-01-10_raspi_48000Hz_w1_N2^12_overlap80.csv

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
	- min_samples_split = 5
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
- gp_auc_min = 0.11809583538609772
- gp_auc_max = 0.08652595866289442
- gp_max_val_mean = 0.08281839623002103
- srmr = 0.07263908086127055
- gp_max_val_min = 0.06676668670910392
- gp_auc_mean = 0.05232708353997905
- gp_max_ix_range = 0.05149655983725578
- gp_max_val_max = 0.04680578563761952
- tdoa_min = 0.04188875909425805
- tdoa_range = 0.04066675950541547
- tdoa_mean = 0.03364200405846907
- gp_max_ix_std = 0.03095088902658659
- gp_max_ix_min = 0.030287757637341848
- tdoa_std = 0.028867984750901254
- ac_auc = 0.023969647678265243
- gp_max_ix_mean = 0.02263307746201655
- ratio_max_to_10ms_ave_peaks = 0.02146300285311353
- ac_std = 0.017629841985621075
- gp_auc_range = 0.014691810477063782
- coe3[2] = 0.014504801193378783
- diff_std = 0.01440853450508623
- high_power = 0.014175548589341691
- low_power = 0.011171493257700154
- hlbr = 0.011117200362361655
- gp_max_val_range = 0.00872108420679849
- coe1[0] = 0.00815138047138047
- coe1[1] = 0.007400475252007818
- coe3[3] = 0.006469609026196576
- gp_auc_std = 0.006222222222222223
- gp_max_val_std = 0.005094650205761315
- diff_auc = 0.0027857142857142855
- tdoa_max = 0.002587878787878788
- gp_max_ix_max = 0.002528659080383218
- ratio_max_to_9th_ave_peaks = 0.0004938271604938274
- coe3[0] = 0.0
- coe3[1] = 0.0

## Evaluation
cv = 8
### accuracy
- Scores = [ 0.7931034482758621, 0.8928571428571429, 0.6071428571428571, 0.75, 0.8214285714285714, 0.75, 0.6071428571428571, 0.75 ]
- Mean = 0.7464593596059114
- Standard deviation = 0.0922524720470357

### balanced_accuracy
- Scores = [ 0.7928571428571429, 0.9, 0.6230769230769231, 0.7307692307692308, 0.823076923076923, 0.75, 0.6071428571428571, 0.75 ]
- Mean = 0.7471153846153846
- Standard deviation = 0.0911714432669746

### f1
- Scores = [ 0.8000000000000002, 0.888888888888889, 0.5217391304347827, 0.8108108108108109, 0.8275862068965518, 0.7407407407407408, 0.5217391304347826, 0.6666666666666666 ]
- Mean = 0.7222714468591531
- Standard deviation = 0.1306679684689345

### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 91 | 17 |
| Actual Positive | 40 | 77 |

      