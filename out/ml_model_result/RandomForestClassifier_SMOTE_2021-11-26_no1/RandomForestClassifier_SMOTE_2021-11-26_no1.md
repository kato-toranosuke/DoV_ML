# RandomForestClassifier_SMOTE_2021-11-26_no1
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
- resampler = SMOTE
- estimator = RandomForestClassifier

### Arguments for hyperparameter search
- resampler = SMOTE
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
	- k_neighbors = 5
	- n_jobs = -1
	- n_features_in_ = 28
	- sampling_strategy_ = OrderedDict([(1, 1440)])
	- nn_k_ = NearestNeighbors(n_neighbors=6)

- best_estimator
	- base_estimator = DecisionTreeClassifier()
	- n_estimators = 700
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
- gp_max_val_mean = 0.1860220381031241
- high_power = 0.09008473756045264
- gp_max_val_range = 0.06673668468132984
- hlbr = 0.06665241991647601
- gp_max_val_std = 0.05487451579129781
- diff_std = 0.04870661315641568
- gp_max_ix_mean = 0.037508533119590105
- gp_max_ix_std = 0.03722721458380765
- srmr = 0.03708980258550484
- diff_auc = 0.036473491886981936
- tdoa_mean = 0.03473546924220909
- tdoa_std = 0.029806870495429696
- coe1[1] = 0.027671801793153095
- gp_max_ix_range = 0.027412427145967273
- ac_auc = 0.027030275847692815
- tdoa_range = 0.026586272019074986
- gp_auc_mean = 0.023886527226163027
- ratio_max_to_10ms_ave_peaks = 0.023003804791543382
- ac_std = 0.022883493310113433
- low_power = 0.022580103117378302
- ratio_max_to_9th_ave_peaks = 0.021671005481297096
- coe3[3] = 0.020779681633557118
- coe3[2] = 0.01348004850446114
- gp_auc_range = 0.010794163978123765
- gp_auc_std = 0.004988160251475486
- coe1[0] = 0.0013138437773796711
- coe3[0] = 0.0
- coe3[1] = 0.0

## Evaluation
cv = 10
### accuracy
- Scores = [ 0.7430555555555556, 0.8541666666666666, 0.8836805555555556, 0.8454861111111112, 0.8611111111111112, 0.7847222222222222, 0.8385416666666666, 0.8142361111111112, 0.8732638888888888, 0.7690972222222222 ]
- Mean = 0.8267361111111111
- Standard deviation = 0.04480915894444619

### balanced_accuracy
- Scores = [ 0.7851851851851852, 0.8509259259259259, 0.8699074074074074, 0.8125, 0.8435185185185186, 0.737037037037037, 0.850462962962963, 0.7828703703703703, 0.8625, 0.6986111111111111 ]
- Mean = 0.8093518518518519
- Standard deviation = 0.05464955694307205

### f1
- Scores = [ 0.7357142857142857, 0.811659192825112, 0.8400954653937948, 0.7676240208877285, 0.8067632850241546, 0.6555555555555556, 0.8066528066528066, 0.7263427109974425, 0.82903981264637, 0.5750798722044728 ]
- Mean = 0.7554527007901722
- Standard deviation = 0.08055544162818694

### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 3164 | 436 |
| Actual Positive | 562 | 1598 |

      