# ExtraTreesClassifier_NoResampler_2022-01-10_no0
## Constants
- CSV_PATH = ../out/csv/experiment
- OUTPUT_PATH = ../out/experiment_result/data_of_2022-01-10/NoAGC-0angle-under5m
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
- AGC_STATUS = ['NoAGC']

## Loaded CSV
- 2022-01-10_raspi_48000Hz_w1_N2^12_overlap80.csv

## Estimator
### Type
- resampler = NoResampler
- estimator = ExtraTreesClassifier

### Arguments for hyperparameter search
- resampler = NoResampler
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
- gp_auc_min = 0.12824382788688335
- gp_max_val_min = 0.0907882385895094
- gp_auc_mean = 0.08506115018003213
- hlbr = 0.08428479258183641
- gp_max_val_mean = 0.06212997543435006
- gp_max_val_max = 0.06157732980101008
- gp_auc_max = 0.06041981426914249
- gp_auc_std = 0.0357902721609761
- gp_max_val_std = 0.031544759890133785
- ratio_max_to_9th_ave_peaks = 0.026027653230936906
- gp_max_val_range = 0.025071215417609417
- gp_max_ix_max = 0.024888690049441248
- tdoa_std = 0.02369473896674625
- gp_max_ix_mean = 0.021595728762486926
- high_power = 0.020956834328647783
- srmr = 0.01939190998453943
- ratio_max_to_10ms_ave_peaks = 0.01926570451546365
- gp_max_ix_std = 0.018185005667307054
- ac_auc = 0.015109638593049266
- tdoa_max = 0.014912389355727163
- coe3[3] = 0.014489000616689326
- gp_auc_range = 0.013741326348453613
- low_power = 0.013244648507748839
- coe3[2] = 0.012932140755863351
- diff_auc = 0.01218358592465814
- coe1[1] = 0.011596513089958746
- tdoa_mean = 0.010739070781287951
- diff_std = 0.010702534908991231
- coe1[0] = 0.009005583554430702
- tdoa_range = 0.007879538992227183
- gp_max_ix_range = 0.0060046367575411486
- ac_std = 0.005006902303685498
- gp_max_ix_min = 0.002188998675460376
- tdoa_min = 0.0013458491171749597
- coe3[0] = 0.0
- coe3[1] = 0.0

## Evaluation
cv = 8
### accuracy
- Scores = [ 0.8275862068965517, 0.7857142857142857, 0.7857142857142857, 0.8214285714285714, 0.8571428571428571, 0.7142857142857143, 0.7857142857142857, 0.8214285714285714 ]
- Mean = 0.7998768472906405
- Standard deviation = 0.04016175827369538

### balanced_accuracy
- Scores = [ 0.7065217391304348, 0.7424242424242424, 0.5606060606060607, 0.6439393939393939, 0.7878787878787878, 0.6695652173913043, 0.5565217391304348, 0.5 ]
- Mean = 0.6459321475625823
- Standard deviation = 0.09371774023249523

### f1
- Scores = [ 0.5454545454545454, 0.5714285714285715, 0.25, 0.4444444444444444, 0.6666666666666666, 0.42857142857142855, 0.25, 0.0 ]
- Mean = 0.39457070707070707
- Standard deviation = 0.20285823510688178

### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 160 | 20 |
| Actual Positive | 26 | 19 |

      