# ExtraTreesClassifier_RandomUnderSampler_2021-11-10_no1
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
- features_mono_ch_python.csv

## Estimator
### Type
- resampler = RandomUnderSampler
- estimator = ExtraTreesClassifier

### Arguments for hyperparameter search
- resampler = RandomUnderSampler
- estimator = ExtraTreesClassifier
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
	- replacement = False
	- n_features_in_ = 36
	- sampling_strategy_ = OrderedDict([(0, 2160)])
	- sample_indices_ = [2146 2563 5678 ... 5752 5753 5759]

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
	- max_features = log2
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
- gp_max_val_max = 0.08369427974687835
- gp_max_val_mean = 0.07862658485799096
- gp_auc_max = 0.07098149951120467
- gp_auc_mean = 0.0709212087922908
- gp_max_val_min = 0.050289529027440764
- gp_auc_min = 0.047055933018330644
- gp_auc_std = 0.03773012645624978
- gp_auc_range = 0.037076782161005004
- gp_max_val_range = 0.03565944274426429
- gp_max_val_std = 0.033559020719395975
- gp_max_ix_min = 0.02711213425769178
- tdoa_mean = 0.02700624462457368
- tdoa_min = 0.026995675264870247
- gp_max_ix_mean = 0.026569695084975323
- tdoa_std = 0.026026598535791853
- gp_max_ix_std = 0.025982267414453045
- diff_std = 0.021691975391345385
- diff_auc = 0.020876071300507715
- tdoa_max = 0.019815140656875726
- gp_max_ix_max = 0.019519103137391622
- gp_max_ix_range = 0.019016657068915272
- tdoa_range = 0.018387159212592007
- srmr = 0.017136543754010452
- high_power = 0.01666382544762652
- ac_auc = 0.01608097036152628
- hlbr = 0.015905391737338386
- coe1[1] = 0.015632945850872437
- coe1[0] = 0.014810541996774451
- low_power = 0.01390404613649497
- ratio_max_to_10ms_ave_peaks = 0.013561822540926883
- coe3[3] = 0.013498740754498837
- ac_std = 0.013393863739892901
- ratio_max_to_9th_ave_peaks = 0.012760150329275114
- coe3[2] = 0.012058028365727714
- coe3[0] = 0.0
- coe3[1] = 0.0

## Evaluation
cv = 10
### accuracy
- Scores = [ 0.7864583333333334, 0.8836805555555556, 0.8819444444444444, 0.8524305555555556, 0.8715277777777778, 0.8125, 0.859375, 0.828125, 0.8854166666666666, 0.7690972222222222 ]
- Mean = 0.8430555555555556
- Standard deviation = 0.03993961249943392

### balanced_accuracy
- Scores = [ 0.8199074074074074, 0.8791666666666667, 0.8731481481481481, 0.8245370370370371, 0.8509259259259259, 0.775, 0.8699074074074074, 0.7976851851851852, 0.8703703703703705, 0.7023148148148148 ]
- Mean = 0.8262962962962963
- Standard deviation = 0.05320401309677865

### f1
- Scores = [ 0.7700934579439253, 0.8473804100227791, 0.8418604651162791, 0.7837150127226462, 0.8177339901477831, 0.7142857142857143, 0.8294736842105264, 0.7468030690537085, 0.841346153846154, 0.5856697819314641 ]
- Mean = 0.777836173928098
- Standard deviation = 0.07697495925357296

### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 3216 | 384 |
| Actual Positive | 520 | 1640 |

      