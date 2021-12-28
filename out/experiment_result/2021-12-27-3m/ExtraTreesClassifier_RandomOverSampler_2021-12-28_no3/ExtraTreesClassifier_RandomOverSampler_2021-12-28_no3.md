# ExtraTreesClassifier_RandomOverSampler_2021-12-28_no3
## Constants
- CSV_PATH = ../out/csv/experiment
- OUTPUT_PATH = ../out/experiment_result/2021-12-27-3m
- FEATURE_ATTRBS = ['low_power', 'high_power', 'hlbr', 'coe1[0]', 'coe1[1]', 'coe3[0]', 'coe3[1]', 'coe3[2]', 'coe3[3]', 'ratio_max_to_10ms_ave_peaks', 'ratio_max_to_9th_ave_peaks', 'ac_std', 'ac_auc', 'diff_std', 'diff_auc', 'srmr', 'gp_max_val_std', 'gp_max_val_range', 'gp_max_val_min', 'gp_max_val_max', 'gp_max_val_mean', 'gp_max_ix_std', 'gp_max_ix_range', 'gp_max_ix_min', 'gp_max_ix_max', 'gp_max_ix_mean', 'gp_auc_std', 'gp_auc_range', 'gp_auc_min', 'gp_auc_max', 'gp_auc_mean', 'tdoa_std', 'tdoa_range', 'tdoa_min', 'tdoa_max', 'tdoa_mean']
- LABEL_ATTRB = ['facing']
- FACING_DOV_ANGLES = [1]
- NCV = 8
- SCORING = ['accuracy', 'balanced_accuracy', 'f1']
- REFIT_SCORING = balanced_accuracy
- PARAM_GRID = [{'est__n_estimators': [50, 100, 150, 200, 300], 'est__min_samples_split': [2, 5, 10], 'est__min_samples_leaf': [1, 5, 10], 'est__max_features': ['sqrt', 'log2', None], 'est__bootstrap': [False], 'est__n_jobs': [-1], 'est__random_state': [42], 'est__max_samples': [0.01, 0.5, 0.09]}, {'est__n_estimators': [50, 100, 150, 200, 300], 'est__min_samples_split': [2, 5, 10], 'est__min_samples_leaf': [1, 5, 10], 'est__max_features': ['sqrt', 'log2', None], 'est__bootstrap': [True], 'est__oob_score': [True, False], 'est__n_jobs': [-1], 'est__random_state': [42], 'est__max_samples': [0.01, 0.5, 0.09]}]
- TRAIN_SET_SESSION = ['trial1', 'trial2']
- TEST_SET_SESSION = ['trial3', 'trial4', 'trial5']

## Loaded CSV
- 2021-12-27_raspi_48000Hz_w1_N2^12_overlap80_withfacing.csv

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
	- sampling_strategy_ = OrderedDict([(1, 28)])
	- shrinkage_ = None
	- sample_indices_ = [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23
 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47
 36 13 37 24 36 47 12 36 37 24 13 37 37 12 25 24  1 37 25  1 24  0 47 25
 46  0 47 12]

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
- gp_max_val_max = 0.08854109868055954
- gp_auc_max = 0.07624618514488302
- diff_auc = 0.06743419275371917
- gp_max_val_min = 0.06356791788382198
- gp_max_val_mean = 0.06043055348528984
- diff_std = 0.05984821481436343
- coe1[0] = 0.054109027923411185
- gp_auc_mean = 0.048041574263190084
- gp_auc_min = 0.043797239946092796
- high_power = 0.04325657634842129
- coe3[2] = 0.042873229580137666
- coe3[3] = 0.041542800366444185
- coe1[1] = 0.03964112352253713
- ac_std = 0.03654711034909397
- hlbr = 0.03245279184868698
- low_power = 0.028809444377170382
- tdoa_mean = 0.02230436718506819
- gp_max_ix_mean = 0.021471322414322213
- srmr = 0.02107820610325572
- ac_auc = 0.01759515179972027
- gp_max_ix_max = 0.011739544241246628
- gp_auc_range = 0.010668545494700183
- ratio_max_to_9th_ave_peaks = 0.009911888436163264
- gp_max_val_range = 0.00845898226862519
- tdoa_std = 0.007898992823838344
- tdoa_max = 0.007558801321703644
- gp_max_ix_std = 0.007288605749070787
- gp_max_val_std = 0.00712975454505065
- gp_auc_std = 0.005119675826161847
- gp_max_ix_range = 0.005092899270811191
- tdoa_range = 0.004849017044754764
- ratio_max_to_10ms_ave_peaks = 0.004695164187684619
- coe3[0] = 0.0
- coe3[1] = 0.0
- gp_max_ix_min = 0.0
- tdoa_min = 0.0

## Evaluation
cv = 8
### accuracy
- Scores = [ 0.8, 0.9, 0.8888888888888888, 0.8888888888888888, 0.7777777777777778, 0.8888888888888888, 0.6666666666666666, 0.7777777777777778 ]
- Mean = 0.8236111111111111
- Standard deviation = 0.07746713759657967

### balanced_accuracy
- Scores = [ 0.875, 0.75, 0.9285714285714286, 0.75, 0.8571428571428572, 0.75, 0.42857142857142855, 0.875 ]
- Mean = 0.7767857142857143
- Standard deviation = 0.14671139933174093

### f1
- Scores = [ 0.6666666666666666, 0.6666666666666666, 0.8, 0.6666666666666666, 0.6666666666666666, 0.6666666666666666, 0.0, 0.5 ]
- Mean = 0.5791666666666666
- Standard deviation = 0.23150323971815168

### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 51 | 8 |
| Actual Positive | 5 | 10 |

      