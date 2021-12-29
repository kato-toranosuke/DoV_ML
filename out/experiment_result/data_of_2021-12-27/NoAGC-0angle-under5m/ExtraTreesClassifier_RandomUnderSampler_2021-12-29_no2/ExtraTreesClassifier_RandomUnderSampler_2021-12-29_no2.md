# ExtraTreesClassifier_RandomUnderSampler_2021-12-29_no2
## Constants
- CSV_PATH = ../out/csv/experiment
- OUTPUT_PATH = ../out/experiment_result/data_of_2021-12-27/NoAGC-0angle-under5m
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
- 2021-12-27_raspi_48000Hz_w1_N2^12_overlap80_new.csv

## Estimator
### Type
- resampler = RandomUnderSampler
- estimator = ExtraTreesClassifier

### Arguments for hyperparameter search
- resampler = RandomUnderSampler
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
	- replacement = False
	- n_features_in_ = 36
	- sampling_strategy_ = OrderedDict([(0, 24)])
	- sample_indices_ = [100  95  91 118  41  99  87  54   2  14  80  38  24   6  39  34  16  28
  67 105  50  83  19  86   0   1  10  11  20  21  32  33  42  43  52  53
  64  65  74  75  84  85  96  97 106 107 116 117]

- best_estimator
	- base_estimator = ExtraTreeClassifier()
	- n_estimators = 100
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
- gp_auc_min = 0.15058791716032424
- gp_max_val_min = 0.14504982277325065
- gp_max_val_max = 0.10404685948816166
- gp_auc_max = 0.0914472345610613
- gp_auc_mean = 0.0831991240885136
- gp_max_val_mean = 0.08279600006892147
- gp_auc_range = 0.04683360847918053
- gp_max_val_range = 0.03475065470195807
- hlbr = 0.03178609591797005
- srmr = 0.028384745032248415
- gp_max_val_std = 0.026309472518448875
- ratio_max_to_10ms_ave_peaks = 0.024960968534235194
- gp_auc_std = 0.018965944837454552
- diff_auc = 0.018895310593912376
- diff_std = 0.018250566170176195
- coe1[1] = 0.012175026353886547
- ratio_max_to_9th_ave_peaks = 0.010824647490972939
- ac_auc = 0.010452032797685076
- coe1[0] = 0.007515191801434423
- gp_max_ix_mean = 0.005424929640122384
- tdoa_min = 0.005057230215483458
- low_power = 0.005025322180714974
- coe3[3] = 0.004683667013445982
- high_power = 0.004514867451125338
- tdoa_range = 0.0037067685846305072
- coe3[2] = 0.003615161590414193
- tdoa_std = 0.0034170815292817584
- gp_max_ix_range = 0.003378216389226817
- tdoa_mean = 0.003370480111744201
- ac_std = 0.00297264751604601
- gp_max_ix_std = 0.0029450770606692872
- tdoa_max = 0.002595122152533109
- gp_max_ix_min = 0.0016802538667183313
- gp_max_ix_max = 0.0003819513280474773
- coe3[0] = 0.0
- coe3[1] = 0.0

## Evaluation
cv = 8
### accuracy
- Scores = [ 0.5217391304347826, 0.8695652173913043, 0.4782608695652174, 1.0, 0.45454545454545453, 0.7727272727272727, 0.8636363636363636, 0.7727272727272727 ]
- Mean = 0.7166501976284585
- Standard deviation = 0.19205566109518596

### balanced_accuracy
- Scores = [ 0.4777777777777778, 0.7722222222222221, 0.6666666666666666, 1.0, 0.5694444444444444, 0.6666666666666667, 0.9166666666666667, 0.8611111111111112 ]
- Mean = 0.7413194444444444
- Standard deviation = 0.16699872881067904

### f1
- Scores = [ 0.26666666666666666, 0.6666666666666665, 0.45454545454545453, 1.0, 0.3333333333333333, 0.4444444444444445, 0.7272727272727273, 0.6153846153846153 ]
- Mean = 0.5635392385392385
- Standard deviation = 0.2229969615297019

### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 100 | 43 |
| Actual Positive | 8 | 28 |

      