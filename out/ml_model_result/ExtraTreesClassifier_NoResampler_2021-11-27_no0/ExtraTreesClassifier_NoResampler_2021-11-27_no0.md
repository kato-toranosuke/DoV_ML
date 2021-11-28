# ExtraTreesClassifier_NoResampler_2021-11-27_no0
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
	- base_estimator_ = ExtraTreeClassifier()

#### Importance of features
- gp_max_val_mean = 0.11498401373869768
- gp_auc_mean = 0.11180116689212424
- gp_max_val_range = 0.05386784786231819
- gp_auc_range = 0.051241917531789104
- gp_max_val_std = 0.045434367891586856
- gp_auc_std = 0.04465367574927507
- tdoa_mean = 0.041045269213011736
- gp_max_ix_mean = 0.04056399651261422
- gp_max_ix_std = 0.03899807233276645
- diff_std = 0.03759930979623717
- tdoa_std = 0.0373667868811936
- diff_auc = 0.032591977474364514
- high_power = 0.03192496640035481
- hlbr = 0.029195245389432335
- gp_max_ix_range = 0.02893585353230775
- tdoa_range = 0.02853229244948202
- srmr = 0.028342860190512402
- coe1[1] = 0.026522409695691584
- ac_auc = 0.023902391891707182
- ratio_max_to_10ms_ave_peaks = 0.023021807930277357
- ratio_max_to_9th_ave_peaks = 0.022371269561920624
- low_power = 0.02235818407771683
- ac_std = 0.021860098931264706
- coe1[0] = 0.02151777282296053
- coe3[3] = 0.0211508005014747
- coe3[2] = 0.020215644748918394
- coe3[0] = 0.0
- coe3[1] = 0.0

## Evaluation
cv = 10
### accuracy
- Scores = [ 0.765625, 0.875, 0.8767361111111112, 0.8489583333333334, 0.8611111111111112, 0.7899305555555556, 0.8315972222222222, 0.8177083333333334, 0.8715277777777778, 0.7708333333333334 ]
- Mean = 0.8309027777777779
- Standard deviation = 0.04081301459698643

### balanced_accuracy
- Scores = [ 0.8060185185185185, 0.875, 0.8606481481481482, 0.8180555555555555, 0.8416666666666666, 0.7467592592592592, 0.8356481481481481, 0.7856481481481481, 0.8592592592592593, 0.700925925925926 ]
- Mean = 0.812962962962963
- Standard deviation = 0.052306620138258465

### f1
- Scores = [ 0.755877034358047, 0.8400000000000001, 0.8289156626506025, 0.7751937984496124, 0.8048780487804876, 0.6720867208672087, 0.7913978494623655, 0.7300771208226222, 0.8254716981132075, 0.5796178343949044 ]
- Mean = 0.7603515767899058
- Standard deviation = 0.07735905850949334

### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 3185 | 415 |
| Actual Positive | 559 | 1601 |

      