# RandomForestClassifier_RandomUnderSampler_2021-11-23_no1
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
- resampler = RandomUnderSampler
- estimator = RandomForestClassifier

### Arguments for hyperparameter search
- resampler = RandomUnderSampler
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
	- replacement = False
	- n_features_in_ = 28
	- sampling_strategy_ = OrderedDict([(0, 2160)])
	- sample_indices_ = [2146 2563 5678 ... 5752 5753 5759]

- best_estimator
	- base_estimator = DecisionTreeClassifier()
	- n_estimators = 1500
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
	- min_samples_split = 10
	- min_samples_leaf = 1
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
- gp_max_val_mean = 0.1792170161008815
- gp_max_val_range = 0.07761349123665731
- high_power = 0.07741351659518213
- gp_max_val_std = 0.05706842602262733
- hlbr = 0.05673902678336209
- gp_auc_mean = 0.05493410679755035
- diff_std = 0.048303823449749095
- gp_max_ix_mean = 0.04441948051577797
- tdoa_mean = 0.04298395431599201
- gp_max_ix_std = 0.04104279149394949
- tdoa_std = 0.03393998138841011
- diff_auc = 0.033764286461489885
- srmr = 0.032623100366207886
- coe1[1] = 0.027492217768540505
- ac_auc = 0.026526986479559186
- low_power = 0.0224656536849128
- ac_std = 0.02209796809051132
- ratio_max_to_10ms_ave_peaks = 0.021212437192219036
- coe3[3] = 0.018804231251679418
- ratio_max_to_9th_ave_peaks = 0.01825761061120667
- tdoa_range = 0.017702205929487177
- gp_max_ix_range = 0.017146010512421917
- coe3[2] = 0.012824791416231107
- gp_auc_range = 0.010292444712579077
- gp_auc_std = 0.004211024714853108
- coe1[0] = 0.0009034161079614429
- coe3[0] = 0.0
- coe3[1] = 0.0

## Evaluation
cv = 10
### accuracy
- Scores = [ 0.7326388888888888, 0.8559027777777778, 0.8767361111111112, 0.8454861111111112, 0.8611111111111112, 0.7881944444444444, 0.8454861111111112, 0.8142361111111112, 0.8680555555555556, 0.7638888888888888 ]
- Mean = 0.8251736111111111
- Standard deviation = 0.046221329639652406

### balanced_accuracy
- Scores = [ 0.7759259259259259, 0.8523148148148147, 0.8625, 0.8125, 0.8416666666666666, 0.7416666666666667, 0.8560185185185185, 0.7837962962962963, 0.8555555555555556, 0.6925925925925925 ]
- Mean = 0.8074537037037037
- Standard deviation = 0.05475912539594605

### f1
- Scores = [ 0.7269503546099291, 0.8134831460674158, 0.8305489260143198, 0.7676240208877285, 0.8048780487804876, 0.6629834254143646, 0.8134171907756813, 0.7277353689567431, 0.8207547169811321, 0.5641025641025641 ]
- Mean = 0.7532477762590366
- Standard deviation = 0.08119093305013353

### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 3162 | 438 |
| Actual Positive | 569 | 1591 |

      