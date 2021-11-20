# ExtraTreesClassifier_RandomUnderSampler_2021-11-05_no0
## Constants
- CSV_PATH = ../../out/csv/
- OUTPUT_PATH = ./result/
- FEATURE_ATTRBS = ['low_power', 'high_power', 'hlbr', 'coe1[0]', 'coe1[1]', 'coe3[0]', 'coe3[1]', 'coe3[2]', 'coe3[3]', 'ratio_max_to_10ms_ave_peaks', 'ratio_max_to_9th_ave_peaks', 'ac_std', 'ac_auc', 'diff_std', 'diff_auc', 'srmr', 'gp_max_val_std', 'gp_max_val_range', 'gp_max_val_min', 'gp_max_val_max', 'gp_max_val_mean', 'gp_max_ix_std', 'gp_max_ix_range', 'gp_max_ix_min', 'gp_max_ix_max', 'gp_max_ix_mean', 'gp_auc_std', 'gp_auc_range', 'gp_auc_min', 'gp_auc_max', 'gp_auc_mean', 'tdoa_std', 'tdoa_range', 'tdoa_min', 'tdoa_max', 'tdoa_mean']
- LABEL_ATTRB = ['dov_angle']
- FACING_DOV_ANGLES = [0, 45, 315]
- NCV = 10
- SCORING = ['accuracy', 'balanced_accuracy', 'f1']
- REFIT_SCORING = balanced_accuracy
- PARAM_GRID = [{'est__n_estimators': [10, 100, 1000], 'est__min_samples_split': [2, 5, 10], 'est__min_samples_leaf': [1, 5, 10], 'est__max_features': ['sqrt', 'log2', None], 'est__bootstrap': [False], 'est__n_jobs': [-1], 'est__random_state': [42], 'est__max_samples': [0.01, 0.5, 0.09]}, {'est__n_estimators': [10, 100, 1000], 'est__min_samples_split': [2, 5, 10], 'est__min_samples_leaf': [1, 5, 10], 'est__max_features': ['sqrt', 'log2', None], 'est__bootstrap': [True], 'est__oob_score': [True, False], 'est__n_jobs': [-1], 'est__random_state': [42], 'est__max_samples': [0.01, 0.5, 0.09]}]

## Loaded CSV
- features_mono_ch_matlab.csv

## Estimator
### Type
- resampler = RandomUnderSampler
- estimator = ExtraTreesClassifier

### Arguments for hyperparameter search
- resampler = RandomUnderSampler
- estimator = ExtraTreesClassifier
- param_grid = 
	- {'est__n_estimators': [10, 100, 1000], 'est__min_samples_split': [2, 5, 10], 'est__min_samples_leaf': [1, 5, 10], 'est__max_features': ['sqrt', 'log2', None], 'est__bootstrap': [False], 'est__n_jobs': [-1], 'est__random_state': [42], 'est__max_samples': [0.01, 0.5, 0.09]}
	- {'est__n_estimators': [10, 100, 1000], 'est__min_samples_split': [2, 5, 10], 'est__min_samples_leaf': [1, 5, 10], 'est__max_features': ['sqrt', 'log2', None], 'est__bootstrap': [True], 'est__oob_score': [True, False], 'est__n_jobs': [-1], 'est__random_state': [42], 'est__max_samples': [0.01, 0.5, 0.09]}

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
	- base_estimator = ExtraTreeClassifier()
	- n_estimators = 100
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
	- min_samples_split = 5
	- min_samples_leaf = 1
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
- gp_max_val_mean = 0.1831810606009219
- gp_max_val_max = 0.164476538466516
- gp_max_val_min = 0.08082438130594743
- gp_max_val_range = 0.046315130914195306
- gp_auc_mean = 0.03926462755851709
- gp_max_val_std = 0.03895041955527912
- gp_auc_min = 0.03772323310352296
- gp_auc_max = 0.026758406747575503
- ac_auc = 0.023375835393245205
- diff_auc = 0.020899714530882164
- diff_std = 0.020840806875930974
- high_power = 0.020585621479046714
- tdoa_mean = 0.02020197413210284
- gp_max_ix_mean = 0.019769539271098657
- gp_max_ix_min = 0.0195488135131965
- tdoa_min = 0.017516334516723447
- ratio_max_to_10ms_ave_peaks = 0.016576218628016826
- srmr = 0.016224094202397916
- gp_max_ix_std = 0.01621443398956745
- ratio_max_to_9th_ave_peaks = 0.015991069425900888
- gp_auc_std = 0.015692035611861076
- gp_auc_range = 0.01527213968885248
- tdoa_std = 0.015152746899854814
- hlbr = 0.01478849512764846
- ac_std = 0.013565596337621683
- coe1[0] = 0.011237621462003326
- coe1[1] = 0.010835105480405022
- coe3[2] = 0.010640832408340042
- low_power = 0.009885616984898673
- coe3[3] = 0.008897958691672557
- gp_max_ix_max = 0.0077579128238805806
- gp_max_ix_range = 0.007234287836555609
- tdoa_max = 0.006982295128729152
- tdoa_range = 0.006819101307091721
- coe3[0] = 0.0
- coe3[1] = 0.0

## Evaluation
cv = 10
### accuracy
- Scores = [ 0.7899305555555556, 0.90625, 0.8888888888888888, 0.8871527777777778, 0.8559027777777778, 0.8263888888888888, 0.8541666666666666, 0.8333333333333334, 0.890625, 0.7638888888888888 ]
- Mean = 0.8496527777777778
- Standard deviation = 0.04429091320219026

### balanced_accuracy
- Scores = [ 0.8226851851851852, 0.9046296296296297, 0.8888888888888888, 0.8597222222222223, 0.8402777777777778, 0.7796296296296297, 0.8657407407407407, 0.7944444444444444, 0.8754629629629629, 0.6953703703703704 ]
- Mean = 0.8326851851851853
- Standard deviation = 0.05939589282979092

### f1
- Scores = [ 0.772983114446529, 0.8778280542986425, 0.8571428571428572, 0.832904884318766, 0.801909307875895, 0.7191011235955056, 0.8242677824267782, 0.7419354838709676, 0.8481927710843373, 0.5723270440251572 ]
- Mean = 0.7848592423085436
- Standard deviation = 0.08573735199146575

### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 3242 | 358 |
| Actual Positive | 508 | 1652 |

      