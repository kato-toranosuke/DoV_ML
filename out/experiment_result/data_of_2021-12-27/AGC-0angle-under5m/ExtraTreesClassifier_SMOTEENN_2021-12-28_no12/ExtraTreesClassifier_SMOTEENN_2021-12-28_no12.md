# ExtraTreesClassifier_SMOTEENN_2021-12-28_no12
## Constants
- CSV_PATH = ../out/csv/experiment
- OUTPUT_PATH = ../out/experiment_result/data_of_2021-12-27/AGC-0angle-under5m
- FEATURE_ATTRBS = ['low_power', 'high_power', 'hlbr', 'coe1[0]', 'coe1[1]', 'coe3[0]', 'coe3[1]', 'coe3[2]', 'coe3[3]', 'ratio_max_to_10ms_ave_peaks', 'ratio_max_to_9th_ave_peaks', 'ac_std', 'ac_auc', 'diff_std', 'diff_auc', 'srmr', 'gp_max_val_std', 'gp_max_val_range', 'gp_max_val_min', 'gp_max_val_max', 'gp_max_val_mean', 'gp_max_ix_std', 'gp_max_ix_range', 'gp_max_ix_min', 'gp_max_ix_max', 'gp_max_ix_mean', 'gp_auc_std', 'gp_auc_range', 'gp_auc_min', 'gp_auc_max', 'gp_auc_mean', 'tdoa_std', 'tdoa_range', 'tdoa_min', 'tdoa_max', 'tdoa_mean']
- LABEL_ATTRB = ['facing']
- FACING_DOV_ANGLES = [1]
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
	- n_estimators = 200
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
	- min_samples_leaf = 5
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
- coe3[3] = 0.06762861361666489
- ac_std = 0.06440500322369015
- coe3[2] = 0.06282174978764096
- low_power = 0.06236775404140787
- ac_auc = 0.06150942198518201
- high_power = 0.05884621838101959
- coe1[0] = 0.05775234859412151
- diff_auc = 0.05315388372958521
- coe1[1] = 0.05211026827442775
- gp_auc_min = 0.051579409408821775
- gp_max_val_min = 0.045106599144149544
- diff_std = 0.041977569351053796
- hlbr = 0.03284452754656397
- gp_max_val_mean = 0.032682521970925346
- gp_auc_mean = 0.029599868846451372
- gp_max_ix_mean = 0.027943194187355223
- gp_max_val_max = 0.026928048261058157
- tdoa_mean = 0.025119947443474268
- gp_auc_max = 0.023519837860422294
- tdoa_std = 0.01935369205720646
- gp_max_ix_std = 0.017741091059808287
- srmr = 0.015184879571001378
- gp_auc_std = 0.01081460733810852
- tdoa_range = 0.009449699069520931
- gp_max_val_std = 0.009069388031286886
- tdoa_min = 0.0069977561681813715
- gp_max_ix_max = 0.006711100939512739
- gp_auc_range = 0.006556390289730599
- tdoa_max = 0.004936453741661433
- gp_max_ix_range = 0.004134968995706861
- gp_max_val_range = 0.0039855731219567035
- gp_max_ix_min = 0.0035230339771160145
- ratio_max_to_10ms_ave_peaks = 0.002922600816691157
- ratio_max_to_9th_ave_peaks = 0.0007219791684950513
- coe3[0] = 0.0
- coe3[1] = 0.0

## Evaluation
cv = 8
### accuracy
- Scores = [ 0.6785714285714286, 0.8571428571428571, 0.75, 0.5714285714285714, 0.7142857142857143, 0.7857142857142857, 0.7142857142857143, 0.7857142857142857 ]
- Mean = 0.7321428571428571
- Standard deviation = 0.07985957062499248

### balanced_accuracy
- Scores = [ 0.553030303030303, 0.9090909090909092, 0.6590909090909092, 0.36363636363636365, 0.696969696969697, 0.8695652173913043, 0.5130434782608696, 0.8695652173913043 ]
- Mean = 0.6792490118577076
- Standard deviation = 0.1834240208038201

### f1
- Scores = [ 0.30769230769230765, 0.7499999999999999, 0.4615384615384615, 0.0, 0.5, 0.625, 0.20000000000000004, 0.625 ]
- Mean = 0.43365384615384617
- Standard deviation = 0.2337191266831082

### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 138 | 41 |
| Actual Positive | 19 | 26 |

      