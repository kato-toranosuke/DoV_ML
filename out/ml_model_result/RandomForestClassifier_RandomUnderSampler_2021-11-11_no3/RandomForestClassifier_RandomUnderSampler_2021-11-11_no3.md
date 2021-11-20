# RandomForestClassifier_RandomUnderSampler_2021-11-11_no3
## Constants
- CSV_PATH = ../../out/csv/
- OUTPUT_PATH = ./result/
- FEATURE_ATTRBS = ['low_power', 'high_power', 'hlbr', 'coe1[0]', 'coe1[1]', 'coe3[0]', 'coe3[1]', 'coe3[2]', 'coe3[3]', 'ratio_max_to_10ms_ave_peaks', 'ratio_max_to_9th_ave_peaks', 'ac_std', 'ac_auc', 'diff_std', 'diff_auc', 'srmr', 'gp_max_val_std', 'gp_max_val_range', 'gp_max_val_min', 'gp_max_val_max', 'gp_max_val_mean', 'gp_max_ix_std', 'gp_max_ix_range', 'gp_max_ix_min', 'gp_max_ix_max', 'gp_max_ix_mean', 'gp_auc_std', 'gp_auc_range', 'gp_auc_min', 'gp_auc_max', 'gp_auc_mean', 'tdoa_std', 'tdoa_range', 'tdoa_min', 'tdoa_max', 'tdoa_mean']
- LABEL_ATTRB = ['dov_angle']
- FACING_DOV_ANGLES = [0, 45, 315]
- NCV = 10
- SCORING = ['accuracy', 'balanced_accuracy', 'f1']
- REFIT_SCORING = balanced_accuracy
- PARAM_GRID = [{'est__n_estimators': [10, 100, 500, 800, 1000], 'est__min_samples_split': [2, 5, 10], 'est__min_samples_leaf': [1, 5, 10], 'est__max_features': ['sqrt', 'log2', None], 'est__bootstrap': [False], 'est__n_jobs': [-1], 'est__random_state': [42], 'est__max_samples': [0.01, 0.5, 0.09]}, {'est__n_estimators': [10, 100, 500, 800, 1000], 'est__min_samples_split': [2, 5, 10], 'est__min_samples_leaf': [1, 5, 10], 'est__max_features': ['sqrt', 'log2', None], 'est__bootstrap': [True], 'est__oob_score': [True, False], 'est__n_jobs': [-1], 'est__random_state': [42], 'est__max_samples': [0.01, 0.5, 0.09]}]

## Loaded CSV
- features_mono_ch_matlab.csv

## Estimator
### Type
- resampler = RandomUnderSampler
- estimator = RandomForestClassifier

### Arguments for hyperparameter search
- resampler = RandomUnderSampler
- estimator = RandomForestClassifier
- param_grid = 
	- {'est__n_estimators': [10, 100, 500, 800, 1000], 'est__min_samples_split': [2, 5, 10], 'est__min_samples_leaf': [1, 5, 10], 'est__max_features': ['sqrt', 'log2', None], 'est__bootstrap': [False], 'est__n_jobs': [-1], 'est__random_state': [42], 'est__max_samples': [0.01, 0.5, 0.09]}
	- {'est__n_estimators': [10, 100, 500, 800, 1000], 'est__min_samples_split': [2, 5, 10], 'est__min_samples_leaf': [1, 5, 10], 'est__max_features': ['sqrt', 'log2', None], 'est__bootstrap': [True], 'est__oob_score': [True, False], 'est__n_jobs': [-1], 'est__random_state': [42], 'est__max_samples': [0.01, 0.5, 0.09]}

- scoring = ['accuracy', 'balanced_accuracy', 'f1']
- refit = balanced_accuracy
- cv = 10

### Parameters of the best estimator
#### The best hyper-parameters
- best_resampler
	- sampling_strategy = auto
	- random_state = 42
	- replacement = False
	- n_features_in_ = 36
	- sampling_strategy_ = OrderedDict([(0, 2160)])
	- sample_indices_ = [2146 2563 5678 ... 5752 5753 5759]

- best_estimator
	- base_estimator = DecisionTreeClassifier()
	- n_estimators = 500
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
	- max_features = log2
	- max_leaf_nodes = None
	- min_impurity_decrease = 0.0
	- min_impurity_split = None
	- ccp_alpha = 0.0
	- n_features_in_ = 36
	- n_features_ = 36
	- n_outputs_ = 1
	- classes_ = [0 1]
	- n_classes_ = 2
	- base_estimator_ = DecisionTreeClassifier()

#### Importance of features
- gp_max_val_mean = 0.12913189493518124
- gp_max_val_max = 0.1054889125520641
- gp_max_val_min = 0.06603565640929536
- high_power = 0.058325214991774496
- gp_max_val_range = 0.05568364801285339
- gp_max_val_std = 0.04861570443761713
- hlbr = 0.03910602084181885
- diff_std = 0.03905449658691967
- gp_auc_max = 0.03227333506462303
- diff_auc = 0.02807237754212288
- gp_auc_min = 0.027057691671153995
- srmr = 0.026969414227979903
- ac_auc = 0.02676198286534122
- gp_auc_mean = 0.02482449591703147
- coe1[1] = 0.023114459116104366
- ac_std = 0.021622519499495386
- ratio_max_to_10ms_ave_peaks = 0.021309501745906928
- tdoa_mean = 0.021182785667497102
- low_power = 0.020871577365828824
- gp_max_ix_std = 0.020711122267301374
- tdoa_std = 0.020208594063976945
- gp_max_ix_mean = 0.019768244457098027
- ratio_max_to_9th_ave_peaks = 0.019689815270440766
- coe3[3] = 0.019165974093861466
- gp_auc_range = 0.016707766793730434
- coe3[2] = 0.01422874983589041
- gp_auc_std = 0.010782579217609715
- gp_max_ix_min = 0.009740571977419253
- tdoa_min = 0.009302571202499794
- tdoa_range = 0.005745859803964204
- gp_max_ix_range = 0.005707273137624443
- tdoa_max = 0.005054408259558155
- gp_max_ix_max = 0.004954155447250247
- coe1[0] = 0.002730624721165352
- coe3[0] = 0.0
- coe3[1] = 0.0

## Evaluation
cv = 10
### accuracy
- Scores = [ 0.75, 0.8993055555555556, 0.8975694444444444, 0.8697916666666666, 0.8732638888888888, 0.8090277777777778, 0.8541666666666666, 0.8211805555555556, 0.8975694444444444, 0.7604166666666666 ]
- Mean = 0.8432291666666666
- Standard deviation = 0.05289899502607321

### balanced_accuracy
- Scores = [ 0.7925925925925925, 0.8972222222222221, 0.8921296296296296, 0.8365740740740741, 0.8541666666666667, 0.7583333333333333, 0.8685185185185185, 0.7837962962962963, 0.8819444444444444, 0.6898148148148148 ]
- Mean = 0.8255092592592593
- Standard deviation = 0.06427168267675516

### f1
- Scores = [ 0.7428571428571429, 0.8687782805429864, 0.8643678160919539, 0.8021108179419525, 0.8215158924205379, 0.6857142857142857, 0.8264462809917356, 0.7267904509283821, 0.8571428571428571, 0.5605095541401274 ]
- Mean = 0.7756233378771962
- Standard deviation = 0.09295450203505912

### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 3227 | 373 |
| Actual Positive | 530 | 1630 |

      