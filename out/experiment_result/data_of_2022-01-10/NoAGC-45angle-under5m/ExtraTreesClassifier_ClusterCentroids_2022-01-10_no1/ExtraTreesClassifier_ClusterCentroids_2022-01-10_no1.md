# ExtraTreesClassifier_ClusterCentroids_2022-01-10_no1
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
- resampler = ClusterCentroids
- estimator = ExtraTreesClassifier

### Arguments for hyperparameter search
- resampler = ClusterCentroids
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
	- estimator = None
	- voting = auto
	- n_jobs = deprecated
	- n_features_in_ = 36
	- sampling_strategy_ = OrderedDict([(1, 72)])
	- estimator_ = KMeans(n_clusters=72, random_state=42)
	- voting_ = soft

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
	- min_samples_split = 10
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
- gp_auc_min = 0.13599102513724584
- gp_max_val_mean = 0.11697393960854202
- gp_max_val_min = 0.11520113378402584
- gp_auc_max = 0.10215930907588733
- gp_max_val_max = 0.06250484765481387
- gp_auc_mean = 0.05628349785475932
- tdoa_mean = 0.041515068836592305
- hlbr = 0.03505166305663133
- gp_max_ix_min = 0.0329774390753342
- gp_max_ix_mean = 0.02953145388917289
- tdoa_min = 0.0282189189883167
- srmr = 0.02462175645356784
- ratio_max_to_10ms_ave_peaks = 0.022520536626550583
- high_power = 0.021936146801778834
- gp_max_ix_range = 0.02045078405901879
- gp_max_val_std = 0.01858331657122145
- tdoa_std = 0.01697864742499095
- tdoa_range = 0.015209715642690524
- gp_auc_std = 0.013649338212746302
- gp_max_ix_std = 0.013532248424313447
- diff_auc = 0.009310936729024897
- gp_max_val_range = 0.00916146666375048
- tdoa_max = 0.008122074838896372
- diff_std = 0.007422528270680161
- coe3[2] = 0.00723518073910691
- gp_auc_range = 0.006873618670267882
- ac_auc = 0.0046338993715245155
- low_power = 0.00437777554861865
- coe1[0] = 0.00409084936464322
- coe3[3] = 0.004019425923466026
- coe1[1] = 0.0032386830007198305
- ratio_max_to_9th_ave_peaks = 0.00258503913812941
- ac_std = 0.0025727541043727227
- gp_max_ix_max = 0.0024649804585985787
- coe3[0] = 0.0
- coe3[1] = 0.0

## Evaluation
cv = 8
### accuracy
- Scores = [ 0.8620689655172413, 0.9642857142857143, 0.8214285714285714, 0.8928571428571429, 0.8214285714285714, 0.9642857142857143, 0.8571428571428571, 0.8214285714285714 ]
- Mean = 0.875615763546798
- Standard deviation = 0.056297762905645324

### balanced_accuracy
- Scores = [ 0.8571428571428572, 0.9666666666666667, 0.8282051282051281, 0.8897435897435897, 0.8179487179487179, 0.9642857142857143, 0.8571428571428571, 0.8214285714285714 ]
- Mean = 0.8753205128205128
- Standard deviation = 0.056506116964546736

### f1
- Scores = [ 0.8823529411764706, 0.9655172413793104, 0.8148148148148148, 0.9032258064516129, 0.8387096774193549, 0.9655172413793104, 0.8571428571428571, 0.8 ]
- Mean = 0.8784100724704663
- Standard deviation = 0.05918994497949091

### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 92 | 16 |
| Actual Positive | 10 | 107 |

      