# ExtraTreesClassifier_SMOTE_2022-01-10_no4
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
- resampler = SMOTE
- estimator = ExtraTreesClassifier

### Arguments for hyperparameter search
- resampler = SMOTE
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
	- k_neighbors = 5
	- n_jobs = -1
	- n_features_in_ = 36
	- sampling_strategy_ = OrderedDict([(1, 90)])
	- nn_k_ = NearestNeighbors(n_neighbors=6)

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
	- min_samples_split = 2
	- min_samples_leaf = 10
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
- gp_auc_max = 0.14398733699872074
- gp_auc_min = 0.11940118290945488
- hlbr = 0.10573357023663332
- gp_max_val_min = 0.10336994155465141
- gp_auc_mean = 0.09659545249325757
- gp_max_val_mean = 0.09335423004554023
- gp_max_val_max = 0.07527519108317748
- gp_auc_std = 0.029490314765363842
- gp_max_ix_mean = 0.024554849034548316
- srmr = 0.02420594082549178
- tdoa_range = 0.0182185031230706
- high_power = 0.014539488269934064
- gp_max_ix_std = 0.014241463891111463
- gp_max_ix_range = 0.013758859733594905
- tdoa_max = 0.01157086635353936
- tdoa_min = 0.009605440889655467
- gp_max_ix_min = 0.00957594974626681
- tdoa_mean = 0.009463696225640982
- gp_max_ix_max = 0.008851841002447706
- coe1[1] = 0.008845705636362871
- coe3[3] = 0.008180431716748187
- gp_max_val_std = 0.008016077686992992
- low_power = 0.007509315733275288
- coe3[2] = 0.006620368548859227
- ac_std = 0.0063726773505620475
- diff_std = 0.0052674368168803675
- tdoa_std = 0.004533394813706654
- ac_auc = 0.0038358979328650634
- ratio_max_to_9th_ave_peaks = 0.003150177571794616
- coe1[0] = 0.0031267328810152227
- gp_max_val_range = 0.0029779661135152903
- ratio_max_to_10ms_ave_peaks = 0.002319414898142554
- diff_auc = 0.0017908632564625536
- gp_auc_range = 0.0016594198607161575
- coe3[0] = 0.0
- coe3[1] = 0.0

## Evaluation
cv = 8
### accuracy
- Scores = [ 0.8275862068965517, 0.75, 0.8214285714285714, 0.5714285714285714, 0.7142857142857143, 0.6428571428571429, 0.8214285714285714, 0.8214285714285714 ]
- Mean = 0.7463054187192117
- Standard deviation = 0.09073271160785153

### balanced_accuracy
- Scores = [ 0.8913043478260869, 0.7803030303030303, 0.7045454545454546, 0.606060606060606, 0.6363636363636364, 0.6260869565217391, 0.6565217391304348, 0.5782608695652174 ]
- Mean = 0.6849308300395256
- Standard deviation = 0.09765888452778873

### f1
- Scores = [ 0.7058823529411764, 0.5882352941176471, 0.5454545454545454, 0.4, 0.42857142857142855, 0.37499999999999994, 0.4444444444444445, 0.28571428571428575 ]
- Mean = 0.4716627939054409
- Standard deviation = 0.1252731894727927

### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 147 | 33 |
| Actual Positive | 13 | 32 |

      