# RandomForestClassifier_RandomOverSampler_2021-11-25_no0
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
- features_mono_ch_matlab.csv

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
	- n_estimators = 400
	- estimator_params = ('criterion', 'max_depth', 'min_samples_split', 'min_samples_leaf', 'min_weight_fraction_leaf', 'max_features', 'max_leaf_nodes', 'min_impurity_decrease', 'min_impurity_split', 'random_state', 'ccp_alpha')
	- bootstrap = True
	- oob_score = True
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
	- n_features_in_ = 28
	- n_features_ = 28
	- n_outputs_ = 1
	- classes_ = [0 1]
	- n_classes_ = 2
	- base_estimator_ = DecisionTreeClassifier()
	- oob_decision_function_ = [[0.01418095 0.98581905]
 [0.00423535 0.99576465]
 [0.49989402 0.50010598]
 ...
 [0.08950599 0.91049401]
 [0.53442592 0.46557408]
 [0.53859456 0.46140544]]
	- oob_score_ = 0.8702777777777778

#### Importance of features
- gp_max_val_mean = 0.49445379144262114
- gp_max_val_range = 0.05148246087301603
- gp_auc_mean = 0.04894260602602856
- gp_max_val_std = 0.03683638888287001
- ac_auc = 0.03338577853830066
- srmr = 0.028370105122243413
- diff_auc = 0.026679293254123642
- ratio_max_to_10ms_ave_peaks = 0.026126039269291922
- ac_std = 0.024160588214311607
- hlbr = 0.024136068268825844
- ratio_max_to_9th_ave_peaks = 0.023395332677430238
- high_power = 0.021813176817100037
- gp_auc_range = 0.02069955260551492
- diff_std = 0.020091929315917127
- tdoa_mean = 0.01724224496328152
- gp_max_ix_mean = 0.01667940044347536
- coe1[1] = 0.016106334260739492
- gp_max_ix_std = 0.014110648274738766
- tdoa_std = 0.013391643970483993
- low_power = 0.011134088841156655
- coe3[3] = 0.009292341179863094
- coe3[2] = 0.006664023861502985
- gp_auc_std = 0.005127529937519621
- tdoa_range = 0.005018464008592246
- gp_max_ix_range = 0.004561744234594627
- coe1[0] = 9.842471645642242e-05
- coe3[0] = 0.0
- coe3[1] = 0.0

## Evaluation
cv = 10
### accuracy
- Scores = [ 0.75, 0.8993055555555556, 0.8541666666666666, 0.8576388888888888, 0.8541666666666666, 0.8038194444444444, 0.8576388888888888, 0.8107638888888888, 0.8645833333333334, 0.7430555555555556 ]
- Mean = 0.8295138888888889
- Standard deviation = 0.04869041150821695

### balanced_accuracy
- Scores = [ 0.7824074074074074, 0.9027777777777777, 0.8481481481481481, 0.8194444444444444, 0.8314814814814815, 0.7486111111111111, 0.8675925925925926, 0.7680555555555555, 0.8388888888888889, 0.6675925925925926 ]
- Mean = 0.8074999999999999
- Standard deviation = 0.06424311356560766

### f1
- Scores = [ 0.7323420074349443, 0.8722466960352422, 0.809090909090909, 0.7783783783783784, 0.7920792079207921, 0.6686217008797654, 0.8270042194092827, 0.7029972752043596, 0.803030303030303, 0.5163398692810458 ]
- Mean = 0.7502130566665022
- Standard deviation = 0.09669226253283214

### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 3224 | 376 |
| Actual Positive | 606 | 1554 |

      