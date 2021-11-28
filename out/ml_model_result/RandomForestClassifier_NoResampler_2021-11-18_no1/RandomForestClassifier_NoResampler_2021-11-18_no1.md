# RandomForestClassifier_NoResampler_2021-11-18_no1
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
- resampler = NoResampler
- estimator = RandomForestClassifier

### Arguments for hyperparameter search
- resampler = NoResampler
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

- best_estimator
	- base_estimator = DecisionTreeClassifier()
	- n_estimators = 200
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
	- max_features = sqrt
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
- gp_max_val_mean = 0.22165611893703896
- high_power = 0.08796747771741066
- gp_auc_mean = 0.0695560893040217
- gp_max_val_range = 0.06889996739715588
- gp_max_val_std = 0.058416333881773204
- diff_std = 0.05254538148344695
- tdoa_mean = 0.04397767759349998
- gp_max_ix_std = 0.0434672886438508
- hlbr = 0.042490205311358185
- gp_max_ix_mean = 0.04143670264053752
- tdoa_std = 0.03202784170099485
- srmr = 0.03072702558829232
- diff_auc = 0.027056661808964752
- coe1[1] = 0.023049580466325336
- ac_auc = 0.021841758791592777
- ac_std = 0.017718003718546062
- gp_max_ix_range = 0.01743706811131798
- tdoa_range = 0.017316142535378668
- ratio_max_to_10ms_ave_peaks = 0.016720177508929793
- low_power = 0.01599446962459103
- coe3[3] = 0.015141589861226037
- ratio_max_to_9th_ave_peaks = 0.014667297384591698
- coe3[2] = 0.010135101484825063
- gp_auc_range = 0.007173270396157358
- gp_auc_std = 0.0023450752998594175
- coe1[0] = 0.00023569280831308565
- coe3[0] = 0.0
- coe3[1] = 0.0

## Evaluation
cv = 10
### accuracy
- Scores = [ 0.7569444444444444, 0.8576388888888888, 0.8715277777777778, 0.8385416666666666, 0.859375, 0.7951388888888888, 0.84375, 0.8072916666666666, 0.875, 0.765625 ]
- Mean = 0.8270833333333332
- Standard deviation = 0.040945730606966484

### balanced_accuracy
- Scores = [ 0.7953703703703704, 0.8583333333333334, 0.862037037037037, 0.8041666666666667, 0.8412037037037037, 0.750925925925926, 0.8546296296296296, 0.7763888888888889, 0.8638888888888889, 0.6939814814814814 ]
- Mean = 0.8100925925925926
- Standard deviation = 0.05407510463249323

### f1
- Scores = [ 0.7454545454545454, 0.8193832599118943, 0.827906976744186, 0.7559055118110236, 0.8038740920096852, 0.6775956284153005, 0.8117154811715481, 0.7175572519083969, 0.8309859154929577, 0.5659163987138264 ]
- Mean = 0.7556295061633364
- Standard deviation = 0.08004610591209216

### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 3161 | 439 |
| Actual Positive | 557 | 1603 |

      