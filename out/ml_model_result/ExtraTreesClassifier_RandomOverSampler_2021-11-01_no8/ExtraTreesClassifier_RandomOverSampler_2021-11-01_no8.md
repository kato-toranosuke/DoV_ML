# ExtraTreesClassifier_RandomOverSampler_2021-11-01_no8
## Constants
- CSV_PATH = ../../out/csv/
- OUTPUT_PATH = ./result/
- FEATURE_ATTRBS = ['low_power', 'high_power', 'hlbr', 'coe1[0]', 'coe1[1]', 'coe3[0]', 'coe3[1]', 'coe3[2]', 'coe3[3]', 'ratio_max_to_10ms_ave_peaks', 'ratio_max_to_9th_ave_peaks', 'ac_std', 'ac_auc', 'diff_std', 'diff_auc', 'srmr', 'gp_max_val_std', 'gp_max_val_range', 'gp_max_val_min', 'gp_max_val_max', 'gp_max_val_mean', 'gp_max_ix_std', 'gp_max_ix_range', 'gp_max_ix_min', 'gp_max_ix_max', 'gp_max_ix_mean', 'gp_auc_std', 'gp_auc_range', 'gp_auc_min', 'gp_auc_max', 'gp_auc_mean', 'tdoa_std', 'tdoa_range', 'tdoa_min', 'tdoa_max', 'tdoa_mean']
- LABEL_ATTRB = ['dov_angle']
- FACING_DOV_ANGLES = [0, 45, 315]
- NCV = 10
- SCORING = ['accuracy', 'balanced_accuracy', 'f1']
- REFIT_SCORING = balanced_accuracy
- PARAM_GRID = [{'est__n_estimators': [10], 'est__min_samples_split': [2], 'est__min_samples_leaf': [5], 'est__max_features': [None], 'est__bootstrap': [False], 'est__n_jobs': [-1], 'est__random_state': [42], 'est__max_samples': [0.5]}]

## Loaded CSV
- features_mono_ch_python.csv

## Estimator
### Type
- resampler = RandomOverSampler
- estimator = ExtraTreesClassifier

### Arguments for hyperparameter search
- resampler = RandomOverSampler
- estimator = ExtraTreesClassifier
- param_grid = 
	- {'est__n_estimators': [10], 'est__min_samples_split': [2], 'est__min_samples_leaf': [5], 'est__max_features': [None], 'est__bootstrap': [False], 'est__n_jobs': [-1], 'est__random_state': [42], 'est__max_samples': [0.5]}

- scoring = ['accuracy', 'balanced_accuracy', 'f1']
- refit = balanced_accuracy
- cv = 10

### Parameters of the best estimator
#### The best hyper-parameters
- best_resampler
	- sampling_strategy = auto
	- random_state = 42
	- shrinkage = None
	- n_features_in_ = 36
	- sampling_strategy_ = OrderedDict([(1, 1440)])
	- shrinkage_ = None
	- sample_indices_ = [   0    1    2 ... 1375 3697 2545]

- best_estimator
	- base_estimator = ExtraTreeClassifier()
	- n_estimators = 10
	- estimator_params = ('criterion', 'max_depth', 'min_samples_split', 'min_samples_leaf', 'min_weight_fraction_leaf', 'max_features', 'max_leaf_nodes', 'min_impurity_decrease', 'min_impurity_split', 'random_state', 'ccp_alpha')
	- bootstrap = False
	- oob_score = False
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
	- n_features_in_ = 36
	- n_features_ = 36
	- n_outputs_ = 1
	- classes_ = [0 1]
	- n_classes_ = 2
	- base_estimator_ = ExtraTreeClassifier()

#### Importance of features
- gp_max_val_max = 0.14097972954969146
- gp_auc_max = 0.13776830030330117
- gp_max_val_mean = 0.09778478030696082
- gp_auc_mean = 0.0935204508097077
- gp_max_val_min = 0.06780433540539213
- gp_auc_min = 0.042841852239795766
- gp_max_val_std = 0.02941893942501026
- tdoa_min = 0.025895167818311422
- tdoa_mean = 0.025348178723063376
- gp_max_ix_mean = 0.02388212845314215
- tdoa_std = 0.020549346468577624
- gp_max_ix_std = 0.01948771067949227
- gp_max_val_range = 0.017812847329593783
- gp_max_ix_min = 0.01683017555991139
- ac_auc = 0.016311062192858654
- gp_auc_std = 0.016183181540565535
- tdoa_max = 0.015579977727809825
- gp_max_ix_range = 0.015309467108393773
- diff_auc = 0.014993419091344875
- srmr = 0.014900555616739846
- gp_auc_range = 0.013661389847010957
- coe1[1] = 0.013317280363658998
- diff_std = 0.01233601806953582
- ratio_max_to_10ms_ave_peaks = 0.011835198932972104
- tdoa_range = 0.01175853967502606
- gp_max_ix_max = 0.011658883249509162
- ratio_max_to_9th_ave_peaks = 0.01065008076243731
- ac_std = 0.010009958484375645
- high_power = 0.009333113465104048
- hlbr = 0.009327919351583098
- low_power = 0.00897756758607031
- coe1[0] = 0.008308108784171644
- coe3[2] = 0.008263935239134552
- coe3[3] = 0.007360399839746503
- coe3[0] = 0.0
- coe3[1] = 0.0

## Evaluation
cv = 10
### accuracy
- Scores = [ 0.7881944444444444, 0.8767361111111112, 0.8524305555555556, 0.8506944444444444, 0.8506944444444444, 0.8003472222222222, 0.828125, 0.8142361111111112, 0.8871527777777778, 0.7777777777777778 ]
- Mean = 0.8326388888888889
- Standard deviation = 0.035138134049863455

### balanced_accuracy
- Scores = [ 0.8166666666666667, 0.8662037037037037, 0.8449074074074074, 0.8194444444444444, 0.8305555555555555, 0.7560185185185185, 0.8384259259259259, 0.7847222222222222, 0.8745370370370371, 0.7138888888888889 ]
- Mean = 0.8145370370370371
- Standard deviation = 0.04742476534076775

### f1
- Scores = [ 0.7671755725190841, 0.8337236533957846, 0.8054919908466818, 0.7772020725388601, 0.7902439024390243, 0.684931506849315, 0.7933194154488518, 0.7291139240506329, 0.8456057007125891, 0.607361963190184 ]
- Mean = 0.7634169701991007
- Standard deviation = 0.06853915180108142

### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 3194 | 406 |
| Actual Positive | 556 | 1604 |

      