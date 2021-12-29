# ExtraTreesClassifier_RandomOverSampler_2021-12-28_no3
## Constants
- CSV_PATH = ../out/csv/experiment
- OUTPUT_PATH = ../out/experiment_result/data_of_2021-12-27/AGC-0angle-5m
- FEATURE_ATTRBS = ['low_power', 'high_power', 'hlbr', 'coe1[0]', 'coe1[1]', 'coe3[0]', 'coe3[1]', 'coe3[2]', 'coe3[3]', 'ratio_max_to_10ms_ave_peaks', 'ratio_max_to_9th_ave_peaks', 'ac_std', 'ac_auc', 'diff_std', 'diff_auc', 'srmr', 'gp_max_val_std', 'gp_max_val_range', 'gp_max_val_min', 'gp_max_val_max', 'gp_max_val_mean', 'gp_max_ix_std', 'gp_max_ix_range', 'gp_max_ix_min', 'gp_max_ix_max', 'gp_max_ix_mean', 'gp_auc_std', 'gp_auc_range', 'gp_auc_min', 'gp_auc_max', 'gp_auc_mean', 'tdoa_std', 'tdoa_range', 'tdoa_min', 'tdoa_max', 'tdoa_mean']
- LABEL_ATTRB = ['facing']
- FACING_DOV_ANGLES = [1]
- NCV = 8
- SCORING = ['accuracy', 'balanced_accuracy', 'f1']
- REFIT_SCORING = balanced_accuracy
- PARAM_GRID = [{'est__n_estimators': [50, 100, 150, 200, 300], 'est__min_samples_split': [2, 5, 10], 'est__min_samples_leaf': [1, 5, 10], 'est__max_features': ['sqrt', 'log2', None], 'est__bootstrap': [False], 'est__n_jobs': [-1], 'est__random_state': [42], 'est__max_samples': [0.01, 0.5, 0.09]}, {'est__n_estimators': [50, 100, 150, 200, 300], 'est__min_samples_split': [2, 5, 10], 'est__min_samples_leaf': [1, 5, 10], 'est__max_features': ['sqrt', 'log2', None], 'est__bootstrap': [True], 'est__oob_score': [True, False], 'est__n_jobs': [-1], 'est__random_state': [42], 'est__max_samples': [0.01, 0.5, 0.09]}]
- TRAIN_SET_SESSION = ['trial1', 'trial2']
- TEST_SET_SESSION = ['trial3', 'trial4', 'trial5']
- DISTANCE = [5]
- AGC_STATUS = ['AGC']

## Loaded CSV
- 2021-12-27_raspi_48000Hz_w1_N2^12_overlap80_new.csv

## Estimator
### Type
- resampler = RandomOverSampler
- estimator = ExtraTreesClassifier

### Arguments for hyperparameter search
- resampler = RandomOverSampler
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
	- shrinkage = None
	- n_features_in_ = 36
	- sampling_strategy_ = OrderedDict([(1, 30)])
	- shrinkage_ = None
	- sample_indices_ = [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23
 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47
 48 49 36 13 37 24 36 49 12 36 37 24 13 37 37 12 25 24  1 37 25  1 24  0
 49 25 48  0 49 12 36 13]

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
	- min_samples_leaf = 10
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
- high_power = 0.2137698283044081
- gp_auc_max = 0.1019420276152588
- gp_max_val_max = 0.0985118095377751
- hlbr = 0.08410503385971672
- diff_auc = 0.07419137357401885
- gp_auc_min = 0.07058917554049075
- gp_max_val_mean = 0.06255097706747137
- gp_max_val_min = 0.042754362937341146
- diff_std = 0.03725682233661965
- gp_auc_mean = 0.0338283086999302
- coe1[0] = 0.029141278866875325
- srmr = 0.026213421389039357
- coe3[3] = 0.02590573903914155
- low_power = 0.02015830910601592
- ac_auc = 0.019331151586490875
- coe1[1] = 0.010464553287338458
- gp_max_ix_range = 0.007555421331013534
- tdoa_max = 0.006735237530268624
- tdoa_range = 0.005538311702445936
- gp_max_ix_max = 0.005494527036822027
- ratio_max_to_10ms_ave_peaks = 0.004550073075017687
- coe3[2] = 0.004383945213411188
- tdoa_min = 0.0024739151773521487
- tdoa_mean = 0.002296079031371709
- tdoa_std = 0.0013807480398580442
- ratio_max_to_9th_ave_peaks = 0.0013713259267461454
- ac_std = 0.0012538699690402486
- gp_auc_range = 0.0012244119081364887
- gp_auc_std = 0.0010869581029707828
- gp_max_ix_min = 0.0010382694877406318
- gp_max_ix_std = 0.0008851255997742017
- gp_max_val_range = 0.0008077935228381886
- gp_max_val_std = 0.0007798173238410172
- gp_max_ix_mean = 0.0004299972734192309
- coe3[0] = 0.0
- coe3[1] = 0.0

## Evaluation
cv = 8
### accuracy
- Scores = [ 0.8, 0.9, 0.7, 0.8888888888888888, 0.7777777777777778, 0.8888888888888888, 0.7777777777777778, 0.7777777777777778 ]
- Mean = 0.8138888888888889
- Standard deviation = 0.06684005230842202

### balanced_accuracy
- Scores = [ 0.875, 0.9375, 0.625, 0.9285714285714286, 0.8571428571428572, 0.9285714285714286, 0.8571428571428572, 0.875 ]
- Mean = 0.8604910714285715
- Standard deviation = 0.09427335848085718

### f1
- Scores = [ 0.6666666666666666, 0.8, 0.4, 0.8, 0.6666666666666666, 0.8, 0.6666666666666666, 0.5 ]
- Mean = 0.6625000000000001
- Standard deviation = 0.13787826756478583

### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 47 | 13 |
| Actual Positive | 1 | 14 |

      