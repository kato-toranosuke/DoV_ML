# ExtraTreesClassifier_RandomUnderSampler_2021-11-24_no2
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
- features_matlab.csv

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
	- base_estimator_ = ExtraTreeClassifier()

#### Importance of features
- gp_max_val_mean = 0.09777789248148056
- gp_max_val_max = 0.09745651666582181
- gp_max_val_min = 0.06459797674747342
- gp_max_val_range = 0.049413375431567715
- gp_max_val_std = 0.04515507872413436
- gp_auc_mean = 0.031447291765753414
- gp_auc_min = 0.03135257115135717
- gp_max_ix_std = 0.030182562530688493
- tdoa_std = 0.0290646008198636
- tdoa_mean = 0.02891934044211267
- gp_auc_range = 0.0288688389032897
- gp_auc_max = 0.02853179301292056
- gp_max_ix_mean = 0.028173747825746887
- gp_auc_std = 0.027875090024515402
- diff_std = 0.025697824602589178
- srmr = 0.0253153820620905
- diff_auc = 0.024566767847066354
- ratio_max_to_10ms_ave_peaks = 0.021403915455359034
- high_power = 0.021279168248201103
- coe1[1] = 0.02124837751014788
- coe1[0] = 0.02045033850920009
- hlbr = 0.020137526761476125
- coe3[3] = 0.020027819314427188
- low_power = 0.019900598507186597
- tdoa_min = 0.019765380346584954
- gp_max_ix_min = 0.018765400633701697
- ac_std = 0.018072935426082303
- ac_auc = 0.01780972622765196
- ratio_max_to_9th_ave_peaks = 0.01764594855428835
- coe3[2] = 0.01734785288897402
- tdoa_max = 0.014911626768481474
- gp_max_ix_max = 0.013851182070325901
- tdoa_range = 0.011764127612818209
- gp_max_ix_range = 0.011221424126621329
- coe3[0] = 0.0
- coe3[1] = 0.0

## Evaluation
cv = 10
### accuracy
- Scores = [ 0.8854166666666666, 0.9097222222222222, 0.9097222222222222, 0.90625, 0.9097222222222222, 0.8871527777777778, 0.8802083333333334, 0.8923611111111112, 0.8975694444444444, 0.8784722222222222 ]
- Mean = 0.8956597222222221
- Standard deviation = 0.011964060523625029

### balanced_accuracy
- Scores = [ 0.7380952380952381, 0.6984126984126984, 0.6746031746031746, 0.6309523809523809, 0.6686507936507937, 0.566468253968254, 0.6875, 0.5992063492063492, 0.6319444444444444, 0.5138888888888888 ]
- Mean = 0.6409722222222223
- Standard deviation = 0.06357795839182687

### f1
- Scores = [ 0.5416666666666666, 0.5357142857142857, 0.5, 0.41304347826086957, 0.49019607843137253, 0.23529411764705882, 0.4732824427480916, 0.32608695652173914, 0.40404040404040403, 0.05405405405405406 ]
- Mean = 0.3973378484084542
- Standard deviation = 0.14641680594938963

### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 4942 | 98 |
| Actual Positive | 503 | 217 |

      