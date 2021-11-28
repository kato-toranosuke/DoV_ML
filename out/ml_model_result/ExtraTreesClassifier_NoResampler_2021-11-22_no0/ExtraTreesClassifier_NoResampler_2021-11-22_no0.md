# ExtraTreesClassifier_NoResampler_2021-11-22_no0
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
- features_python.csv

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
	- n_estimators = 600
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
- gp_auc_max = 0.07408951372307651
- gp_max_val_max = 0.06934506378455982
- gp_max_val_mean = 0.05486092126216129
- gp_auc_mean = 0.05397143430604936
- ratio_max_to_10ms_ave_peaks = 0.03744876087604008
- gp_auc_min = 0.03677284596755668
- gp_max_val_min = 0.03548118833990922
- srmr = 0.0328197454619145
- gp_max_val_std = 0.03240376130675902
- ratio_max_to_9th_ave_peaks = 0.030773834662043698
- diff_auc = 0.03066678272886698
- gp_auc_std = 0.02953347188141853
- gp_auc_range = 0.027300727302243276
- high_power = 0.027195842943745944
- gp_max_val_range = 0.026967627275654653
- hlbr = 0.02651109062856019
- diff_std = 0.026153219961525753
- ac_auc = 0.025112148369033863
- gp_max_ix_mean = 0.025069121272358146
- tdoa_mean = 0.024416370756034544
- gp_max_ix_min = 0.024174371800967334
- tdoa_min = 0.023614017242595518
- ac_std = 0.022800686757554835
- coe1[1] = 0.021916269427542132
- coe3[2] = 0.021387626908508574
- gp_max_ix_std = 0.020959465304261876
- coe3[3] = 0.02082218172807742
- low_power = 0.020771601875385647
- tdoa_std = 0.02057080976220382
- coe1[0] = 0.020554332715481422
- tdoa_max = 0.014242503606773363
- gp_max_ix_max = 0.014193948588667625
- tdoa_range = 0.013785014114209604
- gp_max_ix_range = 0.013313697358258601
- coe3[0] = 0.0
- coe3[1] = 0.0

## Evaluation
cv = 10
### accuracy
- Scores = [ 0.8854166666666666, 0.9010416666666666, 0.9184027777777778, 0.9045138888888888, 0.9097222222222222, 0.8836805555555556, 0.875, 0.8802083333333334, 0.890625, 0.8888888888888888 ]
- Mean = 0.89375
- Standard deviation = 0.01330817215051166

### balanced_accuracy
- Scores = [ 0.7619047619047619, 0.6994047619047619, 0.7271825396825397, 0.6537698412698413, 0.6805555555555556, 0.558531746031746, 0.6845238095238095, 0.6101190476190477, 0.6517857142857143, 0.5615079365079365 ]
- Mean = 0.6589285714285714
- Standard deviation = 0.06328836371409405

### f1
- Scores = [ 0.5657894736842105, 0.5210084033613445, 0.591304347826087, 0.4554455445544554, 0.509433962264151, 0.21176470588235294, 0.4626865671641791, 0.34285714285714286, 0.43243243243243246, 0.21951219512195125 ]
- Mean = 0.43122347751483076
- Standard deviation = 0.12660277641201645

### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 4899 | 141 |
| Actual Positive | 471 | 249 |

      