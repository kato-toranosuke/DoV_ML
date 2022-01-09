# ExtraTreesClassifier_ClusterCentroids_2022-01-09_no1
## Constants
- CSV_PATH = ../out/csv/experiment
- OUTPUT_PATH = ../out/experiment_result/data_of_2022-01-07_new2/AGC-0angle-under5m
- FEATURE_ATTRBS = ['low_power', 'high_power', 'hlbr', 'coe1[0]', 'coe1[1]', 'coe3[0]', 'coe3[1]', 'coe3[2]', 'coe3[3]', 'ratio_max_to_10ms_ave_peaks', 'ratio_max_to_9th_ave_peaks', 'ac_std', 'ac_auc', 'diff_std', 'diff_auc', 'srmr', 'gp_max_val_std', 'gp_max_val_range', 'gp_max_val_min', 'gp_max_val_max', 'gp_max_val_mean', 'gp_max_ix_std', 'gp_max_ix_range', 'gp_max_ix_min', 'gp_max_ix_max', 'gp_max_ix_mean', 'gp_auc_std', 'gp_auc_range', 'gp_auc_min', 'gp_auc_max', 'gp_auc_mean', 'tdoa_std', 'tdoa_range', 'tdoa_min', 'tdoa_max', 'tdoa_mean']
- LABEL_ATTRB = ['facing']
- FACING_DOV_ANGLES = [1]
- NCV = 8
- SCORING = ['accuracy', 'balanced_accuracy', 'f1']
- REFIT_SCORING = balanced_accuracy
- PARAM_GRID = [{'est__n_estimators': range(10, 1000, 25), 'est__min_samples_split': [2, 5, 10], 'est__min_samples_leaf': [1, 5, 10], 'est__max_features': ['sqrt', 'log2', None], 'est__bootstrap': [False], 'est__n_jobs': [-1], 'est__random_state': [42], 'est__max_samples': [0.01, 0.5, 0.09]}]
- TRAIN_SET_SESSION = ['trial1', 'trial2']
- TEST_SET_SESSION = ['trial3', 'trial4', 'trial5']
- DISTANCE = [1, 3, 5]
- AGC_STATUS = ['AGC']

## Loaded CSV
- 2021-12-27_raspi_48000Hz_w1_N2^12_overlap80_with2022-01-07.csv

## Estimator
### Type
- resampler = ClusterCentroids
- estimator = ExtraTreesClassifier

### Arguments for hyperparameter search
- resampler = ClusterCentroids
- estimator = ExtraTreesClassifier
- param_grid = 
	- {'est__n_estimators': range(10, 1000, 25), 'est__min_samples_split': [2, 5, 10], 'est__min_samples_leaf': [1, 5, 10], 'est__max_features': ['sqrt', 'log2', None], 'est__bootstrap': [False], 'est__n_jobs': [-1], 'est__random_state': [42], 'est__max_samples': [0.01, 0.5, 0.09]}

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
	- sampling_strategy_ = OrderedDict([(0, 30)])
	- estimator_ = KMeans(n_clusters=30, random_state=42)
	- voting_ = soft

- best_estimator
	- base_estimator = ExtraTreeClassifier()
	- n_estimators = 160
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
- gp_max_val_min = 0.18948289007424735
- gp_auc_min = 0.16848299954290039
- gp_auc_mean = 0.08934006663028866
- gp_max_val_mean = 0.08714976148751262
- diff_auc = 0.08322081566916142
- high_power = 0.05890093420491491
- gp_auc_max = 0.052300515420474966
- gp_max_val_max = 0.04893644614575572
- diff_std = 0.043718417703019895
- gp_max_ix_max = 0.031531767092889997
- tdoa_max = 0.026247070230265884
- tdoa_min = 0.0112122526245453
- hlbr = 0.009952259112352441
- coe1[0] = 0.009627544510109939
- gp_max_ix_min = 0.009276437247681842
- srmr = 0.007867365978831843
- tdoa_range = 0.007807675773035852
- gp_max_ix_range = 0.007077371545409503
- ratio_max_to_10ms_ave_peaks = 0.006897056147678646
- gp_max_ix_mean = 0.006320121829490696
- coe1[1] = 0.006055367197664317
- ratio_max_to_9th_ave_peaks = 0.006021818036606635
- tdoa_mean = 0.005140010396516703
- gp_max_val_std = 0.0040745997133731
- ac_auc = 0.0034015894749494526
- gp_max_val_range = 0.003367498411425551
- gp_auc_range = 0.0031136922019825175
- coe3[3] = 0.0028152083862935133
- tdoa_std = 0.002640016432613297
- ac_std = 0.002138620270590123
- gp_max_ix_std = 0.0018534439331853122
- low_power = 0.0018316988851450812
- gp_auc_std = 0.0013803411584742552
- coe3[2] = 0.0008163265306122449
- coe3[0] = 0.0
- coe3[1] = 0.0

## Evaluation
cv = 8
### accuracy
- Scores = [ 0.6896551724137931, 0.7857142857142857, 0.7142857142857143, 0.75, 0.7857142857142857, 0.5714285714285714, 0.9285714285714286, 0.8571428571428571 ]
- Mean = 0.760314039408867
- Standard deviation = 0.10116329349006052

### balanced_accuracy
- Scores = [ 0.8043478260869565, 0.8636363636363636, 0.6363636363636364, 0.8409090909090908, 0.8636363636363636, 0.7391304347826086, 0.8782608695652174, 0.9130434782608696 ]
- Mean = 0.8174160079051382
- Standard deviation = 0.08422488302893416

### f1
- Scores = [ 0.5714285714285715, 0.6666666666666666, 0.42857142857142855, 0.631578947368421, 0.6666666666666666, 0.45454545454545453, 0.8000000000000002, 0.7142857142857143 ]
- Mean = 0.6167179311916153
- Standard deviation = 0.11835990449419684

### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 125 | 55 |
| Actual Positive | 3 | 42 |

      