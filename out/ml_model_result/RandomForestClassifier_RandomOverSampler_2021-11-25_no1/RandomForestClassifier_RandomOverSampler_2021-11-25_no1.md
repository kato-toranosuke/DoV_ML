# RandomForestClassifier_RandomOverSampler_2021-11-25_no1
## Constants
- CSV_PATH = ../../out/csv/
- OUTPUT_PATH = ./result/
- FEATURE_ATTRBS = ['low_power', 'high_power', 'hlbr', 'coe1[0]', 'coe1[1]', 'coe3[0]', 'coe3[1]', 'coe3[2]', 'coe3[3]', 'ratio_max_to_10ms_ave_peaks', 'ratio_max_to_9th_ave_peaks', 'ac_std', 'ac_auc', 'diff_std', 'diff_auc', 'srmr', 'gp_max_val_std', 'gp_max_val_range', 'gp_max_val_mean', 'gp_max_ix_std', 'gp_max_ix_range', 'gp_max_ix_mean', 'gp_auc_std', 'gp_auc_range', 'gp_auc_mean', 'tdoa_std', 'tdoa_range', 'tdoa_mean']
- LABEL_ATTRB = ['dov_angle']
- FACING_DOV_ANGLES = [0, 45, 315]
- NCV = 10
- SCORING = ['accuracy', 'balanced_accuracy', 'f1']
- REFIT_SCORING = balanced_accuracy
- PARAM_GRID = [{'est__n_estimators': range(100, 1600, 100), 'est__min_samples_split': [2, 5, 10], 'est__min_samples_leaf': [1, 5, 10], 'est__max_features': ['sqrt', 'log2', None], 'est__bootstrap': [False], 'est__n_jobs': [-1], 'est__random_state': [42], 'est__max_samples': [0.01, 0.5, 0.09]}, {'est__n_estimators': range(100, 1600, 100), 'est__min_samples_split': [2, 5, 10], 'est__min_samples_leaf': [1, 5, 10], 'est__max_features': ['sqrt', 'log2', None], 'est__bootstrap': [True], 'est__oob_score': [True, False], 'est__n_jobs': [-1], 'est__random_state': [42], 'est__max_samples': [0.01, 0.5, 0.09]}]

## Loaded CSV
- features_mono_ch_python.csv

## Estimator
### Type
- resampler = RandomOverSampler
- estimator = RandomForestClassifier

### Arguments for hyperparameter search
- resampler = RandomOverSampler
- estimator = RandomForestClassifier
- param_grid = 
	- {'est__n_estimators': range(100, 1600, 100), 'est__min_samples_split': [2, 5, 10], 'est__min_samples_leaf': [1, 5, 10], 'est__max_features': ['sqrt', 'log2', None], 'est__bootstrap': [False], 'est__n_jobs': [-1], 'est__random_state': [42], 'est__max_samples': [0.01, 0.5, 0.09]}
	- {'est__n_estimators': range(100, 1600, 100), 'est__min_samples_split': [2, 5, 10], 'est__min_samples_leaf': [1, 5, 10], 'est__max_features': ['sqrt', 'log2', None], 'est__bootstrap': [True], 'est__oob_score': [True, False], 'est__n_jobs': [-1], 'est__random_state': [42], 'est__max_samples': [0.01, 0.5, 0.09]}

- scoring = ['accuracy', 'balanced_accuracy', 'f1']
- refit = balanced_accuracy
- cv = 10

### Parameters of the best estimator
#### The best hyper-parameters
- best_resampler
	- sampling_strategy = auto
	- random_state = 42
	- shrinkage = None
	- n_features_in_ = 28
	- sampling_strategy_ = OrderedDict([(1, 1440)])
	- shrinkage_ = None
	- sample_indices_ = [   0    1    2 ... 1375 3697 2545]

- best_estimator
	- base_estimator = DecisionTreeClassifier()
	- n_estimators = 800
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
	- max_features = log2
	- max_leaf_nodes = None
	- min_impurity_decrease = 0.0
	- min_impurity_split = None
	- ccp_alpha = 0.0
	- n_features_in_ = 28
	- n_features_ = 28
	- n_outputs_ = 1
	- classes_ = [0 1]
	- n_classes_ = 2
	- base_estimator_ = DecisionTreeClassifier()

#### Importance of features
- gp_max_val_mean = 0.2135355930285881
- high_power = 0.08456236661494809
- gp_max_val_range = 0.08360921280172387
- gp_auc_mean = 0.058520797325036414
- hlbr = 0.058415424601405065
- gp_max_val_std = 0.05822663729057889
- diff_std = 0.04842297128369683
- gp_max_ix_mean = 0.045933540501035285
- tdoa_mean = 0.0428312248587517
- gp_max_ix_std = 0.04097382356352747
- tdoa_std = 0.03289243844257286
- diff_auc = 0.030594652973217645
- srmr = 0.029108249465586863
- coe1[1] = 0.026330591676901275
- ac_auc = 0.02051571994470395
- low_power = 0.017775865146011982
- tdoa_range = 0.017372322432341956
- gp_max_ix_range = 0.017121683401235068
- ac_std = 0.016622213049650825
- ratio_max_to_10ms_ave_peaks = 0.015314742457060703
- coe3[3] = 0.014143272126193478
- ratio_max_to_9th_ave_peaks = 0.011720132361688382
- coe3[2] = 0.007392880709842028
- gp_auc_range = 0.00650212123888998
- gp_auc_std = 0.0015008757567703502
- coe1[0] = 6.064694804078909e-05
- coe3[0] = 0.0
- coe3[1] = 0.0

## Evaluation
cv = 10
### accuracy
- Scores = [ 0.7413194444444444, 0.8628472222222222, 0.8680555555555556, 0.8333333333333334, 0.8576388888888888, 0.7864583333333334, 0.8333333333333334, 0.796875, 0.8611111111111112, 0.7552083333333334 ]
- Mean = 0.8196180555555556
- Standard deviation = 0.044333425251401506

### balanced_accuracy
- Scores = [ 0.7828703703703703, 0.8643518518518518, 0.8546296296296296, 0.7962962962962963, 0.8361111111111111, 0.7393518518518518, 0.8416666666666667, 0.763425925925926, 0.8472222222222222, 0.6810185185185185 ]
- Mean = 0.8006944444444445
- Standard deviation = 0.05645386771855485

### f1
- Scores = [ 0.7334525939177101, 0.8263736263736264, 0.8199052132701422, 0.7446808510638299, 0.7980295566502463, 0.6592797783933517, 0.7974683544303797, 0.6992287917737788, 0.8104265402843601, 0.5407166123778502 ]
- Mean = 0.7429561918535276
- Standard deviation = 0.08564139629409019

### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 3155 | 445 |
| Actual Positive | 594 | 1566 |

      