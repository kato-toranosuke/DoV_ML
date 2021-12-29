# ExtraTreesClassifier_RandomUnderSampler_2021-12-29_no2
## Constants
- CSV_PATH = ../out/csv/experiment
- OUTPUT_PATH = ../out/experiment_result/data_of_2021-12-27/AGC-45angle-under3m
- FEATURE_ATTRBS = ['low_power', 'high_power', 'hlbr', 'coe1[0]', 'coe1[1]', 'coe3[0]', 'coe3[1]', 'coe3[2]', 'coe3[3]', 'ratio_max_to_10ms_ave_peaks', 'ratio_max_to_9th_ave_peaks', 'ac_std', 'ac_auc', 'diff_std', 'diff_auc', 'srmr', 'gp_max_val_std', 'gp_max_val_range', 'gp_max_val_min', 'gp_max_val_max', 'gp_max_val_mean', 'gp_max_ix_std', 'gp_max_ix_range', 'gp_max_ix_min', 'gp_max_ix_max', 'gp_max_ix_mean', 'gp_auc_std', 'gp_auc_range', 'gp_auc_min', 'gp_auc_max', 'gp_auc_mean', 'tdoa_std', 'tdoa_range', 'tdoa_min', 'tdoa_max', 'tdoa_mean']
- LABEL_ATTRB = ['facing2']
- FACING_DOV_ANGLES = [1, 2]
- NCV = 8
- SCORING = ['accuracy', 'balanced_accuracy', 'f1']
- REFIT_SCORING = balanced_accuracy
- PARAM_GRID = [{'est__n_estimators': [50, 100, 150, 200, 300], 'est__min_samples_split': [2, 5, 10], 'est__min_samples_leaf': [1, 5, 10], 'est__max_features': ['sqrt', 'log2', None], 'est__bootstrap': [False], 'est__n_jobs': [-1], 'est__random_state': [42], 'est__max_samples': [0.01, 0.5, 0.09]}, {'est__n_estimators': [50, 100, 150, 200, 300], 'est__min_samples_split': [2, 5, 10], 'est__min_samples_leaf': [1, 5, 10], 'est__max_features': ['sqrt', 'log2', None], 'est__bootstrap': [True], 'est__oob_score': [True, False], 'est__n_jobs': [-1], 'est__random_state': [42], 'est__max_samples': [0.01, 0.5, 0.09]}]
- TRAIN_SET_SESSION = ['trial1', 'trial2']
- TEST_SET_SESSION = ['trial3', 'trial4', 'trial5']
- DISTANCE = [1, 3]
- AGC_STATUS = ['AGC']

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
	- sampling_strategy_ = OrderedDict([(1, 46)])
	- sample_indices_ = [ 4  5  6  7  8  9 14 15 16 17 18 19 26 27 28 29 36 37 38 39 40 41 48 49
 50 51 58 59 60 61 62 63 70 71 72 73 80 81 82 83 84 85 90 91 92 93 35 77
 89 24 79 11 33 96  3 64 25 20 52 12 66 10 69 46 86 65 95 31 21 32 56 68
 47 23  0 88 53 57 75 55 87  1 43  2 76 67 45 94 22 44 34 97]

- best_estimator
	- base_estimator = ExtraTreeClassifier()
	- n_estimators = 150
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
- gp_max_val_min = 0.23257489426291533
- gp_auc_min = 0.17420982453115305
- gp_auc_mean = 0.13717873155865798
- gp_max_val_mean = 0.11132289904186483
- gp_max_val_max = 0.05568983053232426
- srmr = 0.05375147526398829
- gp_auc_max = 0.04602375250919398
- diff_auc = 0.03388842802724765
- diff_std = 0.023154242118145065
- coe1[1] = 0.018980149239496653
- hlbr = 0.010873082798016086
- high_power = 0.010191590786081133
- ratio_max_to_10ms_ave_peaks = 0.01004786578061477
- ratio_max_to_9th_ave_peaks = 0.009622671843649627
- low_power = 0.009109841149340046
- coe1[0] = 0.0090652736426906
- gp_max_val_range = 0.006974582162914318
- coe3[2] = 0.005837051011643887
- gp_max_val_std = 0.0056030110369234085
- ac_std = 0.005291478048211554
- gp_auc_range = 0.004298491541046068
- coe3[3] = 0.003800278939447466
- gp_max_ix_std = 0.0037744067796272136
- tdoa_mean = 0.003581780538302277
- gp_max_ix_mean = 0.0034495121720185657
- gp_auc_std = 0.00320399814454348
- ac_auc = 0.0025503257125273943
- tdoa_std = 0.0020122568063744533
- gp_max_ix_min = 0.0008058608058608059
- tdoa_range = 0.0008019323671497584
- tdoa_min = 0.0007905939890817032
- tdoa_max = 0.0007051016616234006
- gp_max_ix_max = 0.0005249597423510468
- gp_max_ix_range = 0.00030982545497391744
- coe3[0] = 0.0
- coe3[1] = 0.0

## Evaluation
cv = 8
### accuracy
- Scores = [ 0.8421052631578947, 1.0, 1.0, 0.7894736842105263, 1.0, 1.0, 0.9444444444444444, 0.9444444444444444 ]
- Mean = 0.9400584795321638
- Standard deviation = 0.07638801448896568

### balanced_accuracy
- Scores = [ 0.8333333333333333, 1.0, 1.0, 0.788888888888889, 1.0, 1.0, 0.9444444444444444, 0.9444444444444444 ]
- Mean = 0.9388888888888889
- Standard deviation = 0.07797593804232332

### f1
- Scores = [ 0.8695652173913044, 1.0, 1.0, 0.8000000000000002, 1.0, 1.0, 0.9411764705882353, 0.9411764705882353 ]
- Mean = 0.9439897698209718
- Standard deviation = 0.06967467317956129

### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 66 | 5 |
| Actual Positive | 4 | 74 |

      