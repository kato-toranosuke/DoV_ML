# ExtraTreesClassifier_ClusterCentroids_2022-01-10_no1
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
	- sampling_strategy_ = OrderedDict([(0, 30)])
	- estimator_ = KMeans(n_clusters=30, random_state=42)
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
	- min_samples_split = 5
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
- gp_auc_min = 0.10332791847294122
- gp_auc_max = 0.07979033337747853
- gp_max_val_mean = 0.07435389555949277
- tdoa_mean = 0.07390619297089814
- gp_max_val_min = 0.06285385260523846
- gp_max_val_max = 0.05509164218770832
- gp_max_ix_mean = 0.05358678378012436
- gp_max_ix_max = 0.0399385263948075
- gp_auc_mean = 0.034070139914035534
- gp_max_ix_range = 0.03359433221670026
- gp_max_ix_std = 0.030654193813709738
- low_power = 0.025184508911226252
- coe3[2] = 0.024229947863753824
- gp_max_ix_min = 0.02380073925486491
- coe1[0] = 0.023704920941141707
- tdoa_max = 0.02331727439867738
- tdoa_std = 0.02115417411264781
- hlbr = 0.02071190394184057
- gp_max_val_std = 0.02022106583581837
- coe3[3] = 0.01894132291457106
- srmr = 0.01882285572665956
- ac_auc = 0.017316979874881646
- tdoa_min = 0.014898521942665473
- tdoa_range = 0.014195327662596381
- diff_auc = 0.014097617341633277
- gp_max_val_range = 0.013339118240765637
- gp_auc_std = 0.013081121648094171
- ac_std = 0.01240500557291692
- gp_auc_range = 0.00998382941626354
- coe1[1] = 0.009361899226466939
- ratio_max_to_10ms_ave_peaks = 0.006621532194802831
- high_power = 0.006214909669969503
- diff_std = 0.00447177373084895
- ratio_max_to_9th_ave_peaks = 0.0027558382837584465
- coe3[0] = 0.0
- coe3[1] = 0.0

## Evaluation
cv = 8
### accuracy
- Scores = [ 0.6206896551724138, 0.6785714285714286, 0.7857142857142857, 0.7142857142857143, 0.6428571428571429, 0.5357142857142857, 0.6785714285714286, 0.8571428571428571 ]
- Mean = 0.6891933497536946
- Standard deviation = 0.09271881458692836

### balanced_accuracy
- Scores = [ 0.6376811594202898, 0.7348484848484849, 0.8636363636363636, 0.8181818181818181, 0.7727272727272727, 0.717391304347826, 0.8043478260869565, 0.9130434782608696 ]
- Mean = 0.7827322134387351
- Standard deviation = 0.08135770509021924

### f1
- Scores = [ 0.42105263157894735, 0.5263157894736842, 0.6666666666666666, 0.6, 0.5454545454545454, 0.4347826086956522, 0.5263157894736842, 0.7142857142857143 ]
- Mean = 0.5543592182036118
- Standard deviation = 0.096172956605491

### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 121 | 59 |
| Actual Positive | 7 | 38 |

      