# ExtraTreesClassifier_ClusterCentroids_2021-12-29_no1
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
	- sampling_strategy_ = OrderedDict([(0, 24)])
	- estimator_ = KMeans(n_clusters=24, random_state=42)
	- voting_ = soft

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
	- min_samples_leaf = 5
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
- gp_auc_min = 0.12361438157795938
- srmr = 0.11507284871561488
- ratio_max_to_9th_ave_peaks = 0.10228696961420441
- gp_auc_max = 0.0705915738534075
- gp_auc_mean = 0.06532383106631107
- hlbr = 0.06056372009174943
- gp_max_val_mean = 0.05895916109109733
- gp_max_val_max = 0.04812697348850948
- gp_max_val_min = 0.04782857680577575
- gp_max_ix_mean = 0.03820415967261623
- tdoa_mean = 0.03696119292119828
- tdoa_min = 0.027617532309131932
- gp_max_ix_min = 0.024939428599139363
- gp_max_val_range = 0.02376751100636555
- gp_auc_std = 0.01813254814565027
- diff_auc = 0.01786840001740895
- gp_max_ix_range = 0.015959772392813695
- tdoa_std = 0.014593930427527175
- gp_max_val_std = 0.013919588522886408
- gp_auc_range = 0.010132293355393809
- gp_max_ix_max = 0.010098643178337151
- tdoa_range = 0.008862919259923463
- tdoa_max = 0.0073176043557168806
- gp_max_ix_std = 0.0069620727289652585
- high_power = 0.006519333043007772
- diff_std = 0.006406176539607107
- coe1[0] = 0.004462324974959428
- low_power = 0.0036620768450523616
- coe3[3] = 0.003007913927750613
- ac_auc = 0.002804624033354562
- coe3[2] = 0.002611444266487949
- ratio_max_to_10ms_ave_peaks = 0.0018328188510889287
- ac_std = 0.0009876543209876535
- coe1[1] = 0.0
- coe3[0] = 0.0
- coe3[1] = 0.0

## Evaluation
cv = 8
### accuracy
- Scores = [ 0.5217391304347826, 0.8695652173913043, 0.43478260869565216, 0.7727272727272727, 0.5909090909090909, 0.6363636363636364, 0.7272727272727273, 0.6818181818181818 ]
- Mean = 0.654397233201581
- Standard deviation = 0.13064585531447231

### balanced_accuracy
- Scores = [ 0.6944444444444444, 0.9166666666666667, 0.6388888888888888, 0.8529411764705883, 0.75, 0.7777777777777778, 0.8333333333333333, 0.8055555555555556 ]
- Mean = 0.7837009803921569
- Standard deviation = 0.08330905027142974

### f1
- Scores = [ 0.47619047619047616, 0.7692307692307693, 0.4347826086956522, 0.6666666666666666, 0.47058823529411764, 0.5, 0.5714285714285715, 0.5333333333333333 ]
- Mean = 0.5527775826049484
- Standard deviation = 0.10599387037496844

### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 81 | 62 |
| Actual Positive | 0 | 36 |

      