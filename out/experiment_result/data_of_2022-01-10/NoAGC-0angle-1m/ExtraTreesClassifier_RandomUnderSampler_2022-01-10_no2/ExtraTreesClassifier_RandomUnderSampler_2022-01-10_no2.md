# ExtraTreesClassifier_RandomUnderSampler_2022-01-10_no2
## Constants
- CSV_PATH = ../out/csv/experiment
- OUTPUT_PATH = ../out/experiment_result/data_of_2022-01-10/NoAGC-0angle-1m
- FEATURE_ATTRBS = ['low_power', 'high_power', 'hlbr', 'coe1[0]', 'coe1[1]', 'coe3[0]', 'coe3[1]', 'coe3[2]', 'coe3[3]', 'ratio_max_to_10ms_ave_peaks', 'ratio_max_to_9th_ave_peaks', 'ac_std', 'ac_auc', 'diff_std', 'diff_auc', 'srmr', 'gp_max_val_std', 'gp_max_val_range', 'gp_max_val_min', 'gp_max_val_max', 'gp_max_val_mean', 'gp_max_ix_std', 'gp_max_ix_range', 'gp_max_ix_min', 'gp_max_ix_max', 'gp_max_ix_mean', 'gp_auc_std', 'gp_auc_range', 'gp_auc_min', 'gp_auc_max', 'gp_auc_mean', 'tdoa_std', 'tdoa_range', 'tdoa_min', 'tdoa_max', 'tdoa_mean']
- LABEL_ATTRB = ['facing']
- FACING_DOV_ANGLES = [1]
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
	- sampling_strategy_ = OrderedDict([(0, 10)])
	- sample_indices_ = [23 20 19 32  6 16 45 33 47  8  0  1 12 13 24 25 36 37 48 49]

- best_estimator
	- base_estimator = ExtraTreeClassifier()
	- n_estimators = 100
	- estimator_params = ('criterion', 'max_depth', 'min_samples_split', 'min_samples_leaf', 'min_weight_fraction_leaf', 'max_features', 'max_leaf_nodes', 'min_impurity_decrease', 'random_state', 'ccp_alpha')
	- bootstrap = True
	- oob_score = True
	- n_jobs = -1
	- random_state = 42
	- verbose = 0
	- warm_start = False
	- class_weight = None
	- max_samples = 0.09
	- criterion = gini
	- max_depth = None
	- min_samples_split = 2
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
	- oob_decision_function_ = [[0.39361702 0.60638298]
 [0.61363636 0.38636364]
 [0.6        0.4       ]
 [0.61458333 0.38541667]
 [0.63736264 0.36263736]
 [0.48913043 0.51086957]
 [0.49425287 0.50574713]
 [0.49438202 0.50561798]
 [0.4        0.6       ]
 [0.64516129 0.35483871]
 [0.41052632 0.58947368]
 [0.43820225 0.56179775]
 [0.37647059 0.62352941]
 [0.36263736 0.63736264]
 [0.46590909 0.53409091]
 [0.47126437 0.52873563]
 [0.45555556 0.54444444]
 [0.43617021 0.56382979]
 [0.43820225 0.56179775]
 [0.48863636 0.51136364]]
	- oob_score_ = 0.75

#### Importance of features
- high_power = 0.10344827586206896
- gp_auc_max = 0.10344827586206896
- gp_max_val_min = 0.06896551724137931
- hlbr = 0.05172413793103448
- ratio_max_to_9th_ave_peaks = 0.05172413793103448
- gp_max_val_std = 0.05172413793103448
- tdoa_std = 0.05172413793103448
- coe3[2] = 0.034482758620689655
- ratio_max_to_10ms_ave_peaks = 0.034482758620689655
- gp_max_val_range = 0.034482758620689655
- gp_max_val_mean = 0.034482758620689655
- gp_max_ix_std = 0.034482758620689655
- gp_max_ix_min = 0.034482758620689655
- gp_auc_mean = 0.034482758620689655
- low_power = 0.017241379310344827
- coe1[0] = 0.017241379310344827
- coe1[1] = 0.017241379310344827
- coe3[3] = 0.017241379310344827
- ac_std = 0.017241379310344827
- ac_auc = 0.017241379310344827
- diff_std = 0.017241379310344827
- diff_auc = 0.017241379310344827
- gp_max_val_max = 0.017241379310344827
- gp_max_ix_range = 0.017241379310344827
- gp_max_ix_max = 0.017241379310344827
- gp_max_ix_mean = 0.017241379310344827
- gp_auc_std = 0.017241379310344827
- gp_auc_min = 0.017241379310344827
- tdoa_range = 0.017241379310344827
- tdoa_max = 0.017241379310344827
- coe3[0] = 0.0
- coe3[1] = 0.0
- srmr = 0.0
- gp_auc_range = 0.0
- tdoa_min = 0.0
- tdoa_mean = 0.0

## Evaluation
cv = 8
### accuracy
- Scores = [ 0.4, 0.6, 0.7, 0.5555555555555556, 0.7777777777777778, 0.7777777777777778, 0.6666666666666666, 0.3333333333333333 ]
- Mean = 0.6013888888888889
- Standard deviation = 0.154404221380916

### balanced_accuracy
- Scores = [ 0.625, 0.75, 0.8125, 0.7142857142857143, 0.8571428571428572, 0.8571428571428572, 0.7857142857142857, 0.625 ]
- Mean = 0.7533482142857143
- Standard deviation = 0.08701779255589644

### f1
- Scores = [ 0.4, 0.5, 0.5714285714285715, 0.5, 0.6666666666666666, 0.6666666666666666, 0.5714285714285715, 0.25 ]
- Mean = 0.5157738095238096
- Standard deviation = 0.1305129939187384

### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 30 | 30 |
| Actual Positive | 0 | 15 |

      