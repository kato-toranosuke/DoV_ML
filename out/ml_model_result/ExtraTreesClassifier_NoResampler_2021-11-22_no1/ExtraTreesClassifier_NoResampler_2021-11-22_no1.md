# ExtraTreesClassifier_NoResampler_2021-11-22_no1
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
- PARAM_GRID = [{'est__n_estimators': range(100, 1600, 100), 'est__min_samples_split': [2, 5, 10], 'est__min_samples_leaf': [1, 5, 10], 'est__max_features': ['sqrt', 'log2', None], 'est__bootstrap': [False], 'est__n_jobs': [-1], 'est__random_state': [42], 'est__max_samples': [0.01, 0.5, 0.09]}, {'est__n_estimators': range(100, 1600, 100), 'est__min_samples_split': [2, 5, 10], 'est__min_samples_leaf': [1, 5, 10], 'est__max_features': ['sqrt', 'log2', None], 'est__bootstrap': [True], 'est__oob_score': [True, False], 'est__n_jobs': [-1], 'est__random_state': [42], 'est__max_samples': [0.01, 0.5, 0.09]}]

## Loaded CSV
- features_matlab.csv

## Estimator
### Type
- resampler = NoResampler
- estimator = ExtraTreesClassifier

### Arguments for hyperparameter search
- resampler = NoResampler
- estimator = ExtraTreesClassifier
- param_grid = 
	- {'est__n_estimators': range(100, 1600, 100), 'est__min_samples_split': [2, 5, 10], 'est__min_samples_leaf': [1, 5, 10], 'est__max_features': ['sqrt', 'log2', None], 'est__bootstrap': [False], 'est__n_jobs': [-1], 'est__random_state': [42], 'est__max_samples': [0.01, 0.5, 0.09]}
	- {'est__n_estimators': range(100, 1600, 100), 'est__min_samples_split': [2, 5, 10], 'est__min_samples_leaf': [1, 5, 10], 'est__max_features': ['sqrt', 'log2', None], 'est__bootstrap': [True], 'est__oob_score': [True, False], 'est__n_jobs': [-1], 'est__random_state': [42], 'est__max_samples': [0.01, 0.5, 0.09]}

- scoring = ['accuracy', 'balanced_accuracy', 'f1']
- refit = balanced_accuracy
- cv = 10

### Parameters of the best estimator
#### The best hyper-parameters
- best_resampler

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
	- min_samples_split = 2
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
- gp_max_val_max = 0.10434379391039317
- gp_max_val_mean = 0.0991853987207651
- gp_max_val_min = 0.0711912709341595
- gp_auc_min = 0.053684308041888215
- gp_auc_mean = 0.04192886256858785
- gp_max_val_std = 0.038448656815607885
- gp_max_val_range = 0.03819171271848432
- ratio_max_to_10ms_ave_peaks = 0.037514676313487004
- gp_auc_max = 0.034738476115438434
- gp_auc_range = 0.032641067597503085
- diff_auc = 0.031776547659488716
- gp_auc_std = 0.030220855398355524
- ratio_max_to_9th_ave_peaks = 0.02974015810427008
- srmr = 0.028892932176528285
- high_power = 0.028377321272406487
- hlbr = 0.02762448999190104
- diff_std = 0.026781590699631774
- ac_auc = 0.025565998039464403
- ac_std = 0.022409415074971854
- coe1[0] = 0.02224209762591242
- coe1[1] = 0.022005158046351683
- low_power = 0.02128051651492437
- coe3[2] = 0.020734732423107048
- coe3[3] = 0.0204381584754842
- tdoa_min = 0.01354995282524238
- gp_max_ix_mean = 0.012726687058783515
- tdoa_mean = 0.012566549576678611
- gp_max_ix_min = 0.012333839005773952
- gp_max_ix_std = 0.010273397649907218
- tdoa_std = 0.00977236189592083
- gp_max_ix_max = 0.0048668920671719774
- gp_max_ix_range = 0.00478265321512979
- tdoa_max = 0.004778072718945676
- tdoa_range = 0.004391398747333673
- coe3[0] = 0.0
- coe3[1] = 0.0

## Evaluation
cv = 10
### accuracy
- Scores = [ 0.8680555555555556, 0.90625, 0.9131944444444444, 0.9114583333333334, 0.9114583333333334, 0.8871527777777778, 0.8611111111111112, 0.9010416666666666, 0.9027777777777778, 0.875 ]
- Mean = 0.89375
- Standard deviation = 0.018484488408619666

### balanced_accuracy
- Scores = [ 0.7400793650793651, 0.7321428571428572, 0.7063492063492063, 0.6696428571428572, 0.6994047619047619, 0.5783730158730159, 0.6944444444444444, 0.6517857142857142, 0.6884920634920635, 0.5357142857142857 ]
- Mean = 0.669642857142857
- Standard deviation = 0.062174764761451645

### f1
- Scores = [ 0.5189873417721519, 0.5714285714285715, 0.5535714285714286, 0.4950495049504951, 0.5405405405405406, 0.2696629213483146, 0.4594594594594595, 0.4466019417475728, 0.5087719298245614, 0.14285714285714285 ]
- Mean = 0.4506930782500239
- Standard deviation = 0.1307160282606178

### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 4881 | 159 |
| Actual Positive | 453 | 267 |

      