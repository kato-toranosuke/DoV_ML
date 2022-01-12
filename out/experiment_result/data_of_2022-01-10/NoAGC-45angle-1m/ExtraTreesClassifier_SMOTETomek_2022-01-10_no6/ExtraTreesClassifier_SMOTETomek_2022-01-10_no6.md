# ExtraTreesClassifier_SMOTETomek_2022-01-10_no6
## Constants
- CSV_PATH = ../out/csv/experiment
- OUTPUT_PATH = ../out/experiment_result/data_of_2022-01-10/NoAGC-45angle-1m
- FEATURE_ATTRBS = ['low_power', 'high_power', 'hlbr', 'coe1[0]', 'coe1[1]', 'coe3[0]', 'coe3[1]', 'coe3[2]', 'coe3[3]', 'ratio_max_to_10ms_ave_peaks', 'ratio_max_to_9th_ave_peaks', 'ac_std', 'ac_auc', 'diff_std', 'diff_auc', 'srmr', 'gp_max_val_std', 'gp_max_val_range', 'gp_max_val_min', 'gp_max_val_max', 'gp_max_val_mean', 'gp_max_ix_std', 'gp_max_ix_range', 'gp_max_ix_min', 'gp_max_ix_max', 'gp_max_ix_mean', 'gp_auc_std', 'gp_auc_range', 'gp_auc_min', 'gp_auc_max', 'gp_auc_mean', 'tdoa_std', 'tdoa_range', 'tdoa_min', 'tdoa_max', 'tdoa_mean']
- LABEL_ATTRB = ['facing2']
- FACING_DOV_ANGLES = [1, 2]
- NCV = 8
- SCORING = ['accuracy', 'balanced_accuracy', 'f1']
- REFIT_SCORING = balanced_accuracy
- PARAM_GRID = [{'est__n_estimators': [50, 100, 150, 200, 300], 'est__min_samples_split': [2, 5, 10], 'est__min_samples_leaf': [1, 5, 10], 'est__max_features': ['sqrt', 'log2', None], 'est__bootstrap': [False], 'est__n_jobs': [-1], 'est__random_state': [42], 'est__max_samples': [0.01, 0.5, 0.09]}, {'est__n_estimators': [50, 100, 150, 200, 300], 'est__min_samples_split': [2, 5, 10], 'est__min_samples_leaf': [1, 5, 10], 'est__max_features': ['sqrt', 'log2', None], 'est__bootstrap': [True], 'est__oob_score': [True, False], 'est__n_jobs': [-1], 'est__random_state': [42], 'est__max_samples': [0.01, 0.5, 0.09]}]
- TRAIN_SET_SESSION = ['trial1', 'trial2']
- TEST_SET_SESSION = ['trial3', 'trial4', 'trial5']
- DISTANCE = [1]
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
- gp_auc_max = 0.1126753679032726
- gp_max_ix_range = 0.10048444871474582
- gp_max_val_max = 0.08859033359253389
- gp_max_val_mean = 0.08007399472829936
- gp_max_ix_min = 0.06343418838798098
- tdoa_range = 0.06137344429449693
- gp_auc_mean = 0.06113179980163084
- tdoa_min = 0.04700322543803835
- tdoa_mean = 0.040970243070447825
- gp_max_ix_std = 0.036053776786340266
- tdoa_std = 0.03570716449567943
- gp_auc_min = 0.03208537267850825
- srmr = 0.03194358663460864
- gp_max_ix_mean = 0.022465696831343335
- ratio_max_to_10ms_ave_peaks = 0.020281568729725752
- gp_max_val_min = 0.01881093716533287
- gp_max_val_std = 0.017583256589128533
- hlbr = 0.017224893098360256
- gp_auc_range = 0.015287016266719978
- gp_max_ix_max = 0.014411966344759771
- coe3[2] = 0.01130026989308791
- gp_max_val_range = 0.011144072353839284
- coe1[1] = 0.010225120638260922
- diff_std = 0.009663824497915656
- low_power = 0.008167129277357682
- ac_std = 0.007340697257105927
- coe1[0] = 0.0061613588000877005
- coe3[3] = 0.004516129032258064
- diff_auc = 0.004374424552429669
- tdoa_max = 0.0027756385573097183
- high_power = 0.0025103324348607387
- gp_auc_std = 0.0017777777777777774
- ac_auc = 0.001738512949039265
- ratio_max_to_9th_ave_peaks = 0.0007124304267161413
- coe3[0] = 0.0
- coe3[1] = 0.0

## Evaluation
cv = 8
### accuracy
- Scores = [ 0.8, 1.0, 1.0, 1.0, 0.8888888888888888, 0.8888888888888888, 1.0, 0.7777777777777778 ]
- Mean = 0.9194444444444444
- Standard deviation = 0.08814795362568016

### balanced_accuracy
- Scores = [ 0.8, 1.0, 1.0, 1.0, 0.9, 0.9, 1.0, 0.8 ]
- Mean = 0.925
- Standard deviation = 0.08291561975888498

### f1
- Scores = [ 0.8333333333333333, 1.0, 1.0, 1.0, 0.888888888888889, 0.888888888888889, 1.0, 0.8 ]
- Mean = 0.9263888888888889
- Standard deviation = 0.0783584475107585

### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 32 | 4 |
| Actual Positive | 3 | 36 |

      