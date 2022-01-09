# ExtraTreesClassifier_SMOTEENN_2022-01-09_no5
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
	- max_features = log2
	- max_leaf_nodes = None
	- min_impurity_decrease = 0.0
	- ccp_alpha = 0.0
	- n_features_in_ = 36
	- n_outputs_ = 1
	- classes_ = [0 1]
	- n_classes_ = 2
	- base_estimator_ = ExtraTreeClassifier()

#### Importance of features
- diff_auc = 0.07460099893174904
- gp_max_ix_mean = 0.06865551810104298
- tdoa_std = 0.06107608907142596
- high_power = 0.05486985755840799
- gp_auc_min = 0.047895709112872255
- low_power = 0.04751182674876242
- gp_max_ix_std = 0.04682620127125623
- gp_max_val_min = 0.0465624957256196
- tdoa_mean = 0.04562691129720482
- gp_max_val_mean = 0.044808552824034405
- ratio_max_to_10ms_ave_peaks = 0.04097862851434281
- diff_std = 0.037075003108601665
- gp_auc_mean = 0.03524264958453583
- hlbr = 0.03239408736867529
- srmr = 0.032033074520825
- gp_max_val_max = 0.031114681628292437
- coe3[3] = 0.030893953573898632
- gp_auc_max = 0.030720485702845454
- coe3[2] = 0.02564626907955419
- ac_auc = 0.02542749969810409
- coe1[1] = 0.02510346247159434
- gp_auc_std = 0.022438918621863965
- coe1[0] = 0.020827318827788755
- gp_max_val_std = 0.018432854919805473
- ac_std = 0.010471459714374694
- tdoa_range = 0.009861639088125837
- gp_max_ix_min = 0.007466802428340889
- gp_max_ix_range = 0.005148604143109636
- ratio_max_to_9th_ave_peaks = 0.004832025117739404
- gp_max_ix_max = 0.004380065635721744
- tdoa_max = 0.0037534621971435146
- gp_auc_range = 0.0031634615384615395
- gp_max_val_range = 0.0024691764279676366
- tdoa_min = 0.001690255445911555
- coe3[0] = 0.0
- coe3[1] = 0.0

## Evaluation
cv = 8
### accuracy
- Scores = [ 0.8275862068965517, 0.5714285714285714, 0.8928571428571429, 0.7857142857142857, 0.8571428571428571, 0.9642857142857143, 1.0, 0.9285714285714286 ]
- Mean = 0.853448275862069
- Standard deviation = 0.1253816155418427

### balanced_accuracy
- Scores = [ 0.8214285714285714, 0.5948717948717949, 0.8897435897435897, 0.7846153846153847, 0.8564102564102565, 0.9642857142857143, 1.0, 0.9285714285714286 ]
- Mean = 0.8549908424908425
- Standard deviation = 0.11902622905892511

### f1
- Scores = [ 0.8571428571428571, 0.4, 0.9032258064516129, 0.8000000000000002, 0.8666666666666667, 0.9655172413793104, 1.0, 0.9333333333333333 ]
- Mean = 0.8407357381217225
- Standard deviation = 0.176869955678424

### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 88 | 20 |
| Actual Positive | 27 | 90 |

      