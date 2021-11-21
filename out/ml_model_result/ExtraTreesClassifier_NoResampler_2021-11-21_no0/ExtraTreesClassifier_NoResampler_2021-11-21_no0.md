# ExtraTreesClassifier_NoResampler_2021-11-21_no0
## Constants
- DATASET_PATH = None
- CSV_PATH = ../out/csv
- OUTPUT_PATH = ../out/ml_model_result
- FEATURE_ATTRBS = ['low_power', 'high_power', 'hlbr', 'coe1[0]', 'coe1[1]', 'coe3[0]', 'coe3[1]', 'coe3[2]', 'coe3[3]', 'ratio_max_to_10ms_ave_peaks', 'ratio_max_to_9th_ave_peaks', 'ac_std', 'ac_auc', 'diff_std', 'diff_auc', 'srmr', 'gp_max_val_std', 'gp_max_val_range', 'gp_max_val_min', 'gp_max_val_max', 'gp_max_val_mean', 'gp_max_ix_std', 'gp_max_ix_range', 'gp_max_ix_min', 'gp_max_ix_max', 'gp_max_ix_mean', 'gp_auc_std', 'gp_auc_range', 'gp_auc_min', 'gp_auc_max', 'gp_auc_mean', 'tdoa_std', 'tdoa_range', 'tdoa_min', 'tdoa_max', 'tdoa_mean']
- LABEL_ATTRB = ['dov_angle']
- FACING_DOV_ANGLES = [0]
- NCV = 10
- SCORING = ['accuracy', 'balanced_accuracy', 'f1']
- REFIT_SCORING = balanced_accuracy
- PARAM_GRID = [{'est__n_estimators': range(10, 30, 10), 'est__min_samples_split': [2], 'est__min_samples_leaf': [5], 'est__max_features': [None], 'est__bootstrap': [False], 'est__n_jobs': [-1], 'est__random_state': [42], 'est__max_samples': [0.5]}]

## Loaded CSV
- features_mono_ch_python.csv

## Estimator
### Type
- resampler = NoResampler
- estimator = ExtraTreesClassifier

### Arguments for hyperparameter search
- resampler = NoResampler
- estimator = ExtraTreesClassifier
- param_grid = 
	- {'est__n_estimators': range(10, 30, 10), 'est__min_samples_split': [2], 'est__min_samples_leaf': [5], 'est__max_features': [None], 'est__bootstrap': [False], 'est__n_jobs': [-1], 'est__random_state': [42], 'est__max_samples': [0.5]}

- scoring = ['accuracy', 'balanced_accuracy', 'f1']
- refit = balanced_accuracy
- cv = 10

### Parameters of the best estimator
#### The best hyper-parameters
- best_resampler

- best_estimator
	- base_estimator = ExtraTreeClassifier()
	- n_estimators = 10
	- estimator_params = ('criterion', 'max_depth', 'min_samples_split', 'min_samples_leaf', 'min_weight_fraction_leaf', 'max_features', 'max_leaf_nodes', 'min_impurity_decrease', 'min_impurity_split', 'random_state', 'ccp_alpha')
	- bootstrap = False
	- oob_score = False
	- n_jobs = -1
	- random_state = 42
	- verbose = 0
	- warm_start = False
	- class_weight = None
	- max_samples = 0.5
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
- gp_auc_max = 0.1261729974671094
- gp_max_val_max = 0.12245885428069743
- gp_auc_mean = 0.05507484987035266
- gp_max_val_mean = 0.04726638482661525
- gp_max_val_min = 0.04233087791433186
- gp_max_val_std = 0.038139228557595585
- gp_max_ix_min = 0.03480217730208135
- gp_max_ix_mean = 0.032583265781931596
- gp_auc_min = 0.02962387540257538
- srmr = 0.027020260649335017
- gp_auc_std = 0.02631544961938106
- diff_auc = 0.02566759968477463
- gp_max_ix_max = 0.024290299989481633
- tdoa_min = 0.024118737002286533
- ratio_max_to_10ms_ave_peaks = 0.023101302033000377
- gp_auc_range = 0.023037294598892286
- diff_std = 0.022189780332588015
- gp_max_ix_std = 0.02136410592158978
- coe1[1] = 0.020841858411886623
- ratio_max_to_9th_ave_peaks = 0.018804214238796423
- high_power = 0.01860445076445485
- coe1[0] = 0.018596449642321027
- low_power = 0.017456235615910316
- ac_std = 0.017329271715180065
- gp_max_val_range = 0.017089824083893434
- tdoa_mean = 0.016699297777239823
- tdoa_max = 0.015839826219454144
- hlbr = 0.014751019565008544
- tdoa_std = 0.014737928925578028
- coe3[2] = 0.014648604885811906
- coe3[3] = 0.01304883875476514
- ac_auc = 0.012999013031165638
- tdoa_range = 0.011650511831809658
- gp_max_ix_range = 0.01134531330210474
- coe3[0] = 0.0
- coe3[1] = 0.0

## Evaluation
cv = 10
### accuracy
- Scores = [ 0.8836805555555556, 0.8871527777777778, 0.9184027777777778, 0.90625, 0.9045138888888888, 0.8802083333333334, 0.8680555555555556, 0.8784722222222222, 0.8958333333333334, 0.875 ]
- Mean = 0.8897569444444444
- Standard deviation = 0.015159938538691816

### balanced_accuracy
- Scores = [ 0.7311507936507937, 0.6736111111111112, 0.7033730158730159, 0.6607142857142857, 0.6597222222222222, 0.5625, 0.626984126984127, 0.5793650793650793, 0.6369047619047619, 0.5119047619047619 ]
- Mean = 0.634623015873016
- Standard deviation = 0.06344562103523171

### f1
- Scores = [ 0.5314685314685313, 0.4628099173553719, 0.5607476635514019, 0.47058823529411764, 0.46601941747572817, 0.22471910112359547, 0.3666666666666667, 0.2708333333333333, 0.4117647058823529, 0.05263157894736842 ]
- Mean = 0.38182491510984684
- Standard deviation = 0.14914038950229105

### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 4913 | 127 |
| Actual Positive | 508 | 212 |

      