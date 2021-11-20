# RandomForestClassifier_SMOTE_2021-11-12_no2
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
- resampler = SMOTE
- estimator = RandomForestClassifier

### Arguments for hyperparameter search
- resampler = SMOTE
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
	- k_neighbors = 5
	- n_jobs = -1
	- n_features_in_ = 36
	- sampling_strategy_ = OrderedDict([(1, 1440)])
	- nn_k_ = NearestNeighbors(n_neighbors=6)

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
	- min_samples_split = 5
	- min_samples_leaf = 1
	- min_weight_fraction_leaf = 0.0
	- max_features = sqrt
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
- gp_max_val_mean = 0.15532035777385317
- gp_max_val_max = 0.12688821029521694
- high_power = 0.06939142671623232
- gp_max_val_min = 0.0657950171182834
- gp_max_val_range = 0.04952961798173767
- gp_max_val_std = 0.042746542291296284
- hlbr = 0.04156765662901802
- diff_std = 0.03092407861473847
- srmr = 0.026082210549775983
- diff_auc = 0.02575396859532407
- gp_auc_min = 0.025713753992567225
- ac_auc = 0.021844633075306458
- gp_max_ix_mean = 0.019993954647506317
- tdoa_mean = 0.019529488834417102
- gp_auc_mean = 0.019356734468655226
- coe1[1] = 0.018909930620445256
- ratio_max_to_10ms_ave_peaks = 0.018225933011789736
- gp_auc_max = 0.017546698432244337
- ac_std = 0.017109095104246196
- ratio_max_to_9th_ave_peaks = 0.017065128023228102
- gp_max_ix_std = 0.016854291939238968
- tdoa_std = 0.016674278583748574
- low_power = 0.016556739398991053
- gp_auc_range = 0.01503551808459652
- coe3[3] = 0.014675940929751241
- gp_max_ix_min = 0.012629491521680622
- tdoa_min = 0.012446088029628228
- tdoa_range = 0.011713837632710921
- gp_max_ix_range = 0.011618513042430768
- tdoa_max = 0.011001330248617758
- gp_max_ix_max = 0.010993692588843142
- coe3[2] = 0.010288086370656358
- gp_auc_std = 0.00891880649744118
- coe1[0] = 0.0012989483557823594
- coe3[0] = 0.0
- coe3[1] = 0.0

## Evaluation
cv = 10
### accuracy
- Scores = [ 0.7569444444444444, 0.9097222222222222, 0.8923611111111112, 0.8663194444444444, 0.8732638888888888, 0.8159722222222222, 0.8506944444444444, 0.828125, 0.8975694444444444, 0.7621527777777778 ]
- Mean = 0.8453125
- Standard deviation = 0.051210569463427356

### balanced_accuracy
- Scores = [ 0.799074074074074, 0.9055555555555556, 0.887962962962963, 0.8328703703703704, 0.8550925925925926, 0.7685185185185186, 0.8648148148148148, 0.7902777777777777, 0.8828703703703704, 0.6921296296296297 ]
- Mean = 0.8279166666666666
- Standard deviation = 0.06244409365153433

### f1
- Scores = [ 0.7491039426523297, 0.8807339449541284, 0.8584474885844748, 0.7968337730870713, 0.8223844282238443, 0.702247191011236, 0.8223140495867768, 0.736, 0.8578313253012048, 0.5650793650793651 ]
- Mean = 0.7790975508480431
- Standard deviation = 0.09019320741012593

### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 3231 | 369 |
| Actual Positive | 522 | 1638 |

      