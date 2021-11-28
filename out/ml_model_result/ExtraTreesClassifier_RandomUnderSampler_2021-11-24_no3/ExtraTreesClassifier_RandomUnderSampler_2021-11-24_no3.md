# ExtraTreesClassifier_RandomUnderSampler_2021-11-24_no3
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
- resampler = RandomUnderSampler
- estimator = ExtraTreesClassifier

### Arguments for hyperparameter search
- resampler = RandomUnderSampler
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
	- sampling_strategy = auto
	- random_state = 42
	- replacement = False
	- n_features_in_ = 36
	- sampling_strategy_ = OrderedDict([(0, 720)])
	- sample_indices_ = [4972 3778 1985 ... 5736 5744 5752]

- best_estimator
	- base_estimator = ExtraTreeClassifier()
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
	- base_estimator_ = ExtraTreeClassifier()

#### Importance of features
- gp_max_val_mean = 0.07038726510294874
- gp_auc_max = 0.06089764051721089
- gp_max_val_max = 0.060549080654015056
- gp_auc_mean = 0.05630481645475974
- gp_max_val_min = 0.04452407915800321
- gp_auc_min = 0.04064687573176005
- gp_auc_range = 0.03430196074365009
- gp_max_val_std = 0.0327995605392273
- gp_auc_std = 0.03244977255120601
- gp_max_ix_mean = 0.03140946389359238
- tdoa_mean = 0.03006845605496661
- gp_max_val_range = 0.02913137819731219
- gp_max_ix_std = 0.029130907166520864
- tdoa_std = 0.027264720784324327
- srmr = 0.024722811587518635
- tdoa_min = 0.023829044630342692
- gp_max_ix_min = 0.023751567916065884
- diff_auc = 0.02313434839560352
- diff_std = 0.022931329858515394
- ratio_max_to_10ms_ave_peaks = 0.022835501586472223
- hlbr = 0.02194777489071003
- tdoa_max = 0.021558747844601923
- gp_max_ix_max = 0.021454961406875108
- high_power = 0.02130881854742764
- coe1[1] = 0.020270849241419184
- coe3[3] = 0.020110915091531567
- ratio_max_to_9th_ave_peaks = 0.019785745235976013
- low_power = 0.019591153624337963
- ac_std = 0.019466936395777353
- coe1[0] = 0.019319174675292615
- tdoa_range = 0.019013968590641604
- ac_auc = 0.018910349489929035
- gp_max_ix_range = 0.018335456622253457
- coe3[2] = 0.01785456681921058
- coe3[0] = 0.0
- coe3[1] = 0.0

## Evaluation
cv = 10
### accuracy
- Scores = [ 0.8854166666666666, 0.9114583333333334, 0.9201388888888888, 0.9079861111111112, 0.9166666666666666, 0.8819444444444444, 0.8836805555555556, 0.8888888888888888, 0.8923611111111112, 0.8854166666666666 ]
- Mean = 0.8973958333333332
- Standard deviation = 0.014177768321683543

### balanced_accuracy
- Scores = [ 0.7440476190476191, 0.6934523809523809, 0.7043650793650794, 0.6498015873015873, 0.6904761904761905, 0.5575396825396826, 0.6775793650793651, 0.621031746031746, 0.6408730158730158, 0.5416666666666666 ]
- Mean = 0.6520833333333333
- Standard deviation = 0.06103416163919388

### f1
- Scores = [ 0.547945205479452, 0.5321100917431194, 0.5660377358490566, 0.45360824742268036, 0.5384615384615385, 0.20930232558139536, 0.46399999999999997, 0.37254901960784315, 0.41509433962264153, 0.15384615384615385 ]
- Mean = 0.42529546576138816
- Standard deviation = 0.13586424851768597

### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 4935 | 105 |
| Actual Positive | 486 | 234 |

      