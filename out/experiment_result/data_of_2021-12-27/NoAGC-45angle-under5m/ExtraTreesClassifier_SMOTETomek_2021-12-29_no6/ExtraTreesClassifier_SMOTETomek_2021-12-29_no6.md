# ExtraTreesClassifier_SMOTETomek_2021-12-29_no6
## Constants
- CSV_PATH = ../out/csv/experiment
- OUTPUT_PATH = ../out/experiment_result/data_of_2021-12-27/NoAGC-45angle-under5m
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
	- base_estimator_ = ExtraTreeClassifier()

#### Importance of features
- gp_auc_min = 0.10729140590747194
- gp_max_val_max = 0.07886963171159779
- gp_max_val_min = 0.0710098695928366
- gp_auc_max = 0.06492982797852492
- diff_auc = 0.05572462561405099
- srmr = 0.05554260143604961
- gp_auc_mean = 0.051463921136249854
- gp_max_val_mean = 0.04925091593512868
- hlbr = 0.040371107693108574
- diff_std = 0.033939340308708335
- gp_max_ix_mean = 0.03218963023071536
- coe1[0] = 0.031236712685086612
- tdoa_mean = 0.030641661005093357
- tdoa_max = 0.02857143484311966
- high_power = 0.0264329777920226
- gp_max_ix_std = 0.02245548798086428
- low_power = 0.021254012303390225
- coe1[1] = 0.02045998174486153
- tdoa_range = 0.019963110390737487
- gp_max_ix_max = 0.018804852545300642
- tdoa_std = 0.0164656925746282
- gp_max_ix_range = 0.014101501154066191
- gp_max_ix_min = 0.013649118829567923
- gp_max_val_std = 0.01326878615164911
- gp_max_val_range = 0.012787022123252069
- ac_auc = 0.012205203630942074
- coe3[3] = 0.011314934984797569
- gp_auc_std = 0.01090093750645699
- tdoa_min = 0.008123449162530548
- gp_auc_range = 0.007344939616470719
- ratio_max_to_10ms_ave_peaks = 0.007240799410627117
- coe3[2] = 0.004968022470696269
- ratio_max_to_9th_ave_peaks = 0.003909921886913161
- ac_std = 0.003316561662483221
- coe3[0] = 0.0
- coe3[1] = 0.0

## Evaluation
cv = 8
### accuracy
- Scores = [ 0.9130434782608695, 1.0, 0.9565217391304348, 0.9090909090909091, 1.0, 0.8636363636363636, 1.0, 0.9545454545454546 ]
- Mean = 0.9496047430830039
- Standard deviation = 0.047513103874194905

### balanced_accuracy
- Scores = [ 0.9, 1.0, 0.9583333333333333, 0.9083333333333333, 1.0, 0.8583333333333334, 1.0, 0.9583333333333333 ]
- Mean = 0.9479166666666666
- Standard deviation = 0.05030290194854013

### f1
- Scores = [ 0.9285714285714286, 1.0, 0.9565217391304348, 0.9166666666666666, 1.0, 0.8799999999999999, 1.0, 0.9565217391304348 ]
- Mean = 0.9547851966873706
- Standard deviation = 0.04164158991989983

### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 76 | 5 |
| Actual Positive | 4 | 94 |

      