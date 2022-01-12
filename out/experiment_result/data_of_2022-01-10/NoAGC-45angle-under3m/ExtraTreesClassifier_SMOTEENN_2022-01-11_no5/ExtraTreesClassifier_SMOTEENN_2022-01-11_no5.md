# ExtraTreesClassifier_SMOTEENN_2022-01-11_no5
## Constants
- CSV_PATH = ../out/csv/experiment
- OUTPUT_PATH = ../out/experiment_result/data_of_2022-01-10/NoAGC-45angle-under3m
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
- AGC_STATUS = ['NoAGC']

## Loaded CSV
- 2022-01-10_raspi_48000Hz_w1_N2^12_overlap80.csv

## Estimator
### Type
- resampler = SMOTEENN
- estimator = ExtraTreesClassifier

### Arguments for hyperparameter search
- resampler = SMOTEENN
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
	- smote = None
	- enn = None
	- n_jobs = -1
	- n_features_in_ = 36
	- sampling_strategy_ = auto
	- smote_ = SMOTE(n_jobs=-1, random_state=42)
	- enn_ = EditedNearestNeighbours(n_jobs=-1, sampling_strategy='all')

- best_estimator
	- base_estimator = ExtraTreeClassifier()
	- n_estimators = 100
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
- gp_max_val_mean = 0.16946655218775428
- gp_max_val_min = 0.1540463667545831
- gp_auc_mean = 0.14254502101906597
- srmr = 0.1373686723328896
- gp_auc_min = 0.1053577017806098
- gp_max_val_max = 0.0725512079916536
- ratio_max_to_10ms_ave_peaks = 0.0533772993309703
- gp_auc_max = 0.04825267239518874
- gp_auc_range = 0.01544478055567372
- gp_max_val_range = 0.011823406478578892
- tdoa_range = 0.008801936159079017
- gp_max_val_std = 0.007598760214144831
- gp_max_ix_mean = 0.0073700109414395155
- hlbr = 0.0070009157509157505
- gp_max_ix_std = 0.00574925074925075
- gp_max_ix_range = 0.005241035441704338
- gp_auc_std = 0.004928048142333857
- ac_auc = 0.0048534798534798545
- coe1[1] = 0.004525844525844528
- coe3[2] = 0.004423781346858272
- diff_auc = 0.003930402930402931
- coe3[3] = 0.0038723181580324444
- diff_std = 0.0034486978223241976
- coe1[0] = 0.0031062271062271066
- tdoa_mean = 0.0028021978021978027
- tdoa_min = 0.0022930402930402926
- tdoa_std = 0.002161172161172162
- low_power = 0.0021555367709213875
- high_power = 0.001831501831501832
- gp_max_ix_min = 0.0016941391941391966
- ac_std = 0.0005494505494505497
- gp_max_ix_max = 0.0005494505494505497
- ratio_max_to_9th_ave_peaks = 0.0005494505494505496
- tdoa_max = 0.0003296703296703295
- coe3[0] = 0.0
- coe3[1] = 0.0

## Evaluation
cv = 8
### accuracy
- Scores = [ 0.8421052631578947, 0.9473684210526315, 0.8421052631578947, 0.7368421052631579, 1.0, 0.7368421052631579, 0.8333333333333334, 1.0 ]
- Mean = 0.8673245614035088
- Standard deviation = 0.09879988347388716

### balanced_accuracy
- Scores = [ 0.8333333333333333, 0.9444444444444444, 0.8333333333333333, 0.7222222222222222, 1.0, 0.7333333333333334, 0.8333333333333333, 1.0 ]
- Mean = 0.8624999999999999
- Standard deviation = 0.10212820253527631

### f1
- Scores = [ 0.8695652173913044, 0.9523809523809523, 0.8695652173913044, 0.8, 1.0, 0.761904761904762, 0.8571428571428571, 1.0 ]
- Mean = 0.8888198757763975
- Standard deviation = 0.08254043267880087

### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 53 | 19 |
| Actual Positive | 2 | 76 |

      