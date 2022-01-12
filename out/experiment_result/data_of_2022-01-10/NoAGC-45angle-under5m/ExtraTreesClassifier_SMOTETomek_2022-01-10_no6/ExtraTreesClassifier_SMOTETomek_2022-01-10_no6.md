# ExtraTreesClassifier_SMOTETomek_2022-01-10_no6
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
	- n_estimators = 150
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
	- min_samples_split = 10
	- min_samples_leaf = 1
	- min_weight_fraction_leaf = 0.0
	- max_features = None
	- max_leaf_nodes = None
	- min_impurity_decrease = 0.0
	- ccp_alpha = 0.0
	- n_features_in_ = 36
	- n_outputs_ = 1
	- classes_ = [0 1]
	- n_classes_ = 2
	- base_estimator_ = ExtraTreeClassifier()

#### Importance of features
- gp_auc_min = 0.16560037835908636
- gp_auc_max = 0.13875162658357743
- gp_max_val_mean = 0.12421084735291517
- gp_max_val_min = 0.12267347767233198
- gp_max_val_max = 0.11163735444493171
- gp_auc_mean = 0.08652473196539714
- ratio_max_to_10ms_ave_peaks = 0.052993128572866866
- hlbr = 0.02579916314772023
- gp_max_ix_min = 0.020460017110898912
- gp_max_ix_mean = 0.019058079793251845
- tdoa_min = 0.016018745181440808
- tdoa_mean = 0.014019386848559176
- gp_auc_std = 0.012694070845235005
- tdoa_range = 0.010241841880847301
- high_power = 0.009844429826126487
- tdoa_std = 0.008674802846825579
- gp_max_val_std = 0.008471646222412385
- srmr = 0.008374429280758445
- gp_max_ix_range = 0.00720840212306731
- gp_max_ix_std = 0.0071081205558273025
- gp_max_val_range = 0.0064830944722583436
- gp_auc_range = 0.00580806844000311
- ac_std = 0.002085411206349133
- gp_max_ix_max = 0.0020608046017166364
- coe1[1] = 0.002018257538267052
- low_power = 0.0019873276299112873
- coe3[3] = 0.001972013731104441
- ac_auc = 0.001423704226137504
- diff_auc = 0.0013531903349740149
- diff_std = 0.0011664036332559105
- coe3[2] = 0.0010546426139837954
- coe1[0] = 0.0008091227849320574
- tdoa_max = 0.0007107700689082914
- ratio_max_to_9th_ave_peaks = 0.0007025081041210471
- coe3[0] = 0.0
- coe3[1] = 0.0

## Evaluation
cv = 8
### accuracy
- Scores = [ 0.896551724137931, 0.9285714285714286, 0.8928571428571429, 0.7857142857142857, 0.7857142857142857, 0.9642857142857143, 0.75, 0.7857142857142857 ]
- Mean = 0.8486761083743842
- Standard deviation = 0.07551690974793748

### balanced_accuracy
- Scores = [ 0.8928571428571428, 0.9333333333333333, 0.9, 0.7794871794871795, 0.7846153846153847, 0.9642857142857143, 0.75, 0.7857142857142858 ]
- Mean = 0.84878663003663
- Standard deviation = 0.07722571166851235

### f1
- Scores = [ 0.9090909090909091, 0.9285714285714286, 0.888888888888889, 0.8125, 0.8000000000000002, 0.9655172413793104, 0.7407407407407408, 0.75 ]
- Mean = 0.8494136510839098
- Standard deviation = 0.07934329599382846

### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 94 | 14 |
| Actual Positive | 17 | 100 |

      