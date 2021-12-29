# ExtraTreesClassifier_SMOTEENN_2021-12-29_no5
## Constants
- CSV_PATH = ../out/csv/experiment
- OUTPUT_PATH = ../out/experiment_result/data_of_2021-12-27/AGC-45angle-under3m
- FEATURE_ATTRBS = ['low_power', 'high_power', 'hlbr', 'coe1[0]', 'coe1[1]', 'coe3[0]', 'coe3[1]', 'coe3[2]', 'coe3[3]', 'ratio_max_to_10ms_ave_peaks', 'ratio_max_to_9th_ave_peaks', 'ac_std', 'ac_auc', 'diff_std', 'diff_auc', 'srmr', 'gp_max_val_std', 'gp_max_val_range', 'gp_max_val_min', 'gp_max_val_max', 'gp_max_val_mean', 'gp_max_ix_std', 'gp_max_ix_range', 'gp_max_ix_min', 'gp_max_ix_max', 'gp_max_ix_mean', 'gp_auc_std', 'gp_auc_range', 'gp_auc_min', 'gp_auc_max', 'gp_auc_mean', 'tdoa_std', 'tdoa_range', 'tdoa_min', 'tdoa_max', 'tdoa_mean']
- LABEL_ATTRB = ['facing2']
- FACING_DOV_ANGLES = [1, 2]
- NCV = 8
- SCORING = ['accuracy', 'balanced_accuracy', 'f1']
- REFIT_SCORING = balanced_accuracy
- PARAM_GRID = [{'est__n_estimators': [50, 100, 150, 200, 300], 'est__min_samples_split': [2, 5, 10], 'est__min_samples_leaf': [1, 5, 10], 'est__max_features': ['sqrt', 'log2', None], 'est__bootstrap': [False], 'est__n_jobs': [-1], 'est__random_state': [42], 'est__max_samples': [0.01, 0.5, 0.09]}, {'est__n_estimators': [50, 100, 150, 200, 300], 'est__min_samples_split': [2, 5, 10], 'est__min_samples_leaf': [1, 5, 10], 'est__max_features': ['sqrt', 'log2', None], 'est__bootstrap': [True], 'est__oob_score': [True, False], 'est__n_jobs': [-1], 'est__random_state': [42], 'est__max_samples': [0.01, 0.5, 0.09]}]
- TRAIN_SET_SESSION = ['trial1', 'trial2']
- TEST_SET_SESSION = ['trial3', 'trial4', 'trial5']
- DISTANCE = [1, 3]
- AGC_STATUS = ['AGC']

## Loaded CSV
- 2021-12-27_raspi_48000Hz_w1_N2^12_overlap80_new.csv

## Estimator
### Type
- resampler = SMOTEENN
- estimator = ExtraTreesClassifier

### Arguments for hyperparameter search
- resampler = SMOTEENN
- estimator = ExtraTreesClassifier
- param_grid = 
	- {'est__n_estimators': [50, 100, 150, 200, 300], 'est__min_samples_split': [2, 5, 10], 'est__min_samples_leaf': [1, 5, 10], 'est__max_features': ['sqrt', 'log2', None], 'est__bootstrap': [False], 'est__n_jobs': [-1], 'est__random_state': [42], 'est__max_samples': [0.01, 0.5, 0.09]}
	- {'est__n_estimators': [50, 100, 150, 200, 300], 'est__min_samples_split': [2, 5, 10], 'est__min_samples_leaf': [1, 5, 10], 'est__max_features': ['sqrt', 'log2', None], 'est__bootstrap': [True], 'est__oob_score': [True, False], 'est__n_jobs': [-1], 'est__random_state': [42], 'est__max_samples': [0.01, 0.5, 0.09]}

- scoring = ['accuracy', 'balanced_accuracy', 'f1']
- refit = balanced_accuracy
- cv = 8

### Parameters of the best estimator
#### The best hyper-parameters
- best_resampler
	- sampling_strategy = auto
	- random_state = 42
	- smote = None
	- enn = None
	- n_jobs = -1
	- n_features_in_ = 36
	- sampling_strategy_ = auto
	- smote_ = SMOTE(n_jobs=-1, random_state=42)
	- enn_ = EditedNearestNeighbours(n_jobs=-1, sampling_strategy='all')

- best_estimator
	- base_estimator = ExtraTreeClassifier()
	- n_estimators = 300
	- estimator_params = ('criterion', 'max_depth', 'min_samples_split', 'min_samples_leaf', 'min_weight_fraction_leaf', 'max_features', 'max_leaf_nodes', 'min_impurity_decrease', 'min_impurity_split', 'random_state', 'ccp_alpha')
	- bootstrap = True
	- oob_score = True
	- n_jobs = -1
	- random_state = 42
	- verbose = 0
	- warm_start = False
	- class_weight = None
	- max_samples = 0.09
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
	- oob_decision_function_ = [[0.45357143 0.54642857]
 [0.55272727 0.44727273]
 [0.55714286 0.44285714]
 [0.40501792 0.59498208]
 [0.48571429 0.51428571]
 [0.34275618 0.65724382]
 [0.49103943 0.50896057]
 [0.51263538 0.48736462]
 [0.48708487 0.51291513]
 [0.56630824 0.43369176]
 [0.5229682  0.4770318 ]
 [0.55595668 0.44404332]
 [0.26568266 0.73431734]
 [0.35869565 0.64130435]
 [0.25830258 0.74169742]
 [0.25454545 0.74545455]
 [0.40070922 0.59929078]
 [0.2437276  0.7562724 ]
 [0.27272727 0.72727273]
 [0.34408602 0.65591398]
 [0.25448029 0.74551971]
 [0.25724638 0.74275362]
 [0.23636364 0.76363636]
 [0.23943662 0.76056338]
 [0.27372263 0.72627737]
 [0.25818182 0.74181818]]
	- oob_score_ = 0.7692307692307693

#### Importance of features
- gp_max_val_min = 0.08280254777070063
- diff_std = 0.050955414012738856
- srmr = 0.044585987261146494
- gp_max_val_range = 0.044585987261146494
- high_power = 0.03821656050955414
- hlbr = 0.03821656050955414
- gp_max_val_mean = 0.03821656050955414
- gp_auc_max = 0.03821656050955414
- tdoa_mean = 0.03821656050955414
- coe1[1] = 0.03184713375796178
- diff_auc = 0.03184713375796178
- gp_max_ix_min = 0.03184713375796178
- gp_max_ix_max = 0.03184713375796178
- gp_max_ix_mean = 0.03184713375796178
- tdoa_std = 0.03184713375796178
- ratio_max_to_10ms_ave_peaks = 0.025477707006369428
- ratio_max_to_9th_ave_peaks = 0.025477707006369428
- ac_auc = 0.025477707006369428
- gp_max_val_std = 0.025477707006369428
- gp_max_val_max = 0.025477707006369428
- gp_max_ix_range = 0.025477707006369428
- gp_auc_range = 0.025477707006369428
- gp_auc_min = 0.025477707006369428
- gp_auc_mean = 0.025477707006369428
- low_power = 0.01910828025477707
- coe3[2] = 0.01910828025477707
- coe3[3] = 0.01910828025477707
- gp_max_ix_std = 0.01910828025477707
- gp_auc_std = 0.01910828025477707
- tdoa_range = 0.01910828025477707
- coe1[0] = 0.012738853503184714
- ac_std = 0.012738853503184714
- tdoa_min = 0.012738853503184714
- tdoa_max = 0.012738853503184714
- coe3[0] = 0.0
- coe3[1] = 0.0

## Evaluation
cv = 8
### accuracy
- Scores = [ 0.7894736842105263, 0.42105263157894735, 0.7894736842105263, 0.7894736842105263, 0.5263157894736842, 0.8888888888888888, 0.5, 0.7222222222222222 ]
- Mean = 0.6783625730994152
- Standard deviation = 0.15985222605462157

### balanced_accuracy
- Scores = [ 0.7777777777777778, 0.4222222222222222, 0.7777777777777778, 0.7777777777777778, 0.5, 0.875, 0.5, 0.7222222222222222 ]
- Mean = 0.6690972222222222
- Standard deviation = 0.15763391756723105

### f1
- Scores = [ 0.8333333333333333, 0.4210526315789474, 0.8333333333333333, 0.8333333333333333, 0.6896551724137931, 0.9090909090909091, 0.6666666666666666, 0.761904761904762 ]
- Mean = 0.7435462677068847
- Standard deviation = 0.1435026491970679

### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 30 | 41 |
| Actual Positive | 7 | 71 |

      