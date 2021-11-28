# RandomForestClassifier_ClusterCentroids_2021-11-22_no1
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
- resampler = ClusterCentroids
- estimator = RandomForestClassifier

### Arguments for hyperparameter search
- resampler = ClusterCentroids
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
	- estimator = None
	- voting = auto
	- n_jobs = deprecated
	- n_features_in_ = 28
	- sampling_strategy_ = OrderedDict([(0, 2160)])
	- estimator_ = KMeans(n_clusters=2160, random_state=42)
	- voting_ = soft

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
- gp_max_val_mean = 0.16254673980304837
- gp_max_val_range = 0.08552094417909895
- high_power = 0.06003329065438817
- gp_max_ix_std = 0.0561219388581736
- gp_max_val_std = 0.0552476582033426
- gp_max_ix_mean = 0.05183689263152686
- tdoa_mean = 0.05126803573494504
- gp_auc_mean = 0.05103976125690408
- tdoa_std = 0.04542126524971762
- hlbr = 0.04244821503837231
- diff_std = 0.04110661574752095
- gp_max_ix_range = 0.03904077890348946
- tdoa_range = 0.038842046129340384
- srmr = 0.026526349992295927
- diff_auc = 0.0226468888139157
- ratio_max_to_10ms_ave_peaks = 0.021395868339433896
- ac_auc = 0.020957245379443087
- ratio_max_to_9th_ave_peaks = 0.020935872743051653
- coe1[1] = 0.019417375045128648
- ac_std = 0.01901161244404756
- low_power = 0.01806291235598748
- coe3[3] = 0.017549306745055795
- coe3[2] = 0.013001039336499477
- gp_auc_range = 0.011796164512271081
- gp_auc_std = 0.005751955394408698
- coe1[0] = 0.002473226508592629
- coe3[0] = 0.0
- coe3[1] = 0.0

## Evaluation
cv = 10
### accuracy
- Scores = [ 0.7413194444444444, 0.8576388888888888, 0.8854166666666666, 0.8402777777777778, 0.8576388888888888, 0.7934027777777778, 0.8420138888888888, 0.8246527777777778, 0.8732638888888888, 0.7708333333333334 ]
- Mean = 0.8286458333333334
- Standard deviation = 0.04408525920406395

### balanced_accuracy
- Scores = [ 0.7810185185185186, 0.8574074074074074, 0.8759259259259259, 0.8064814814814815, 0.8388888888888888, 0.7458333333333333, 0.8541666666666667, 0.7958333333333334, 0.8606481481481482, 0.7018518518518518 ]
- Mean = 0.8118055555555556
- Standard deviation = 0.05364510292562811

### f1
- Scores = [ 0.7315315315315315, 0.8185840707964602, 0.8457943925233644, 0.7591623036649214, 0.8009708737864077, 0.6685236768802229, 0.8108108108108107, 0.7443037974683545, 0.8274231678486997, 0.5822784810126582 ]
- Mean = 0.7589383106323432
- Standard deviation = 0.07784479177306464

### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 3165 | 435 |
| Actual Positive | 552 | 1608 |

      