# ExtraTreesClassifier_NoResampler_2021-11-30_no1
## Constants
- CSV_PATH = ../out/csv/experiment
- OUTPUT_PATH = ../out/ml_model_result
- FEATURE_ATTRBS = ['low_power', 'high_power', 'hlbr', 'coe1[0]', 'coe1[1]', 'coe3[0]', 'coe3[1]', 'coe3[2]', 'coe3[3]', 'ratio_max_to_10ms_ave_peaks', 'ratio_max_to_9th_ave_peaks', 'ac_std', 'ac_auc', 'diff_std', 'diff_auc', 'srmr', 'gp_max_val_std', 'gp_max_val_range', 'gp_max_val_min', 'gp_max_val_max', 'gp_max_val_mean', 'gp_max_ix_std', 'gp_max_ix_range', 'gp_max_ix_min', 'gp_max_ix_max', 'gp_max_ix_mean', 'gp_auc_std', 'gp_auc_range', 'gp_auc_min', 'gp_auc_max', 'gp_auc_mean', 'tdoa_std', 'tdoa_range', 'tdoa_min', 'tdoa_max', 'tdoa_mean']
- LABEL_ATTRB = ['dov_angle']
- FACING_DOV_ANGLES = [0, 45, 315]
- NCV = 8
- SCORING = ['accuracy', 'balanced_accuracy', 'f1']
- REFIT_SCORING = balanced_accuracy
- PARAM_GRID = [{'est__n_estimators': [100, 500, 1000], 'est__min_samples_split': [2, 5, 10], 'est__min_samples_leaf': [1, 5, 10], 'est__max_features': ['sqrt', 'log2', None], 'est__bootstrap': [False], 'est__n_jobs': [-1], 'est__random_state': [42], 'est__max_samples': [0.01, 0.5, 0.09]}, {'est__n_estimators': [100, 500, 1000], 'est__min_samples_split': [2, 5, 10], 'est__min_samples_leaf': [1, 5, 10], 'est__max_features': ['sqrt', 'log2', None], 'est__bootstrap': [True], 'est__oob_score': [True, False], 'est__n_jobs': [-1], 'est__random_state': [42], 'est__max_samples': [0.01, 0.5, 0.09]}]

## Loaded CSV
- 2021-11-29_mac_48000Hz_w1_N2^12_overlap80.csv

## Estimator
### Type
- resampler = NoResampler
- estimator = ExtraTreesClassifier

### Arguments for hyperparameter search
- resampler = NoResampler
- estimator = ExtraTreesClassifier
- param_grid = 
	- {'est__n_estimators': [100, 500, 1000], 'est__min_samples_split': [2, 5, 10], 'est__min_samples_leaf': [1, 5, 10], 'est__max_features': ['sqrt', 'log2', None], 'est__bootstrap': [False], 'est__n_jobs': [-1], 'est__random_state': [42], 'est__max_samples': [0.01, 0.5, 0.09]}
	- {'est__n_estimators': [100, 500, 1000], 'est__min_samples_split': [2, 5, 10], 'est__min_samples_leaf': [1, 5, 10], 'est__max_features': ['sqrt', 'log2', None], 'est__bootstrap': [True], 'est__oob_score': [True, False], 'est__n_jobs': [-1], 'est__random_state': [42], 'est__max_samples': [0.01, 0.5, 0.09]}

- scoring = ['accuracy', 'balanced_accuracy', 'f1']
- refit = balanced_accuracy
- cv = 8

### Parameters of the best estimator
#### The best hyper-parameters
- best_resampler

- best_estimator
	- base_estimator = ExtraTreeClassifier()
	- n_estimators = 100
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
	- oob_decision_function_ = [[0.32391304 0.67608696]
 [0.38560606 0.61439394]
 [0.72175141 0.27824859]
 [0.93937198 0.06062802]
 [0.88099415 0.11900585]
 [0.9362217  0.0637783 ]
 [0.73390805 0.26609195]
 [0.18090909 0.81909091]
 [0.26060606 0.73939394]
 [0.54959645 0.45040355]
 [0.89592413 0.10407587]
 [0.92916667 0.07083333]
 [0.98392857 0.01607143]
 [0.9240113  0.0759887 ]
 [0.70732323 0.29267677]
 [0.40777778 0.59222222]
 [0.20794872 0.79205128]
 [0.51888889 0.48111111]
 [0.83909091 0.16090909]
 [0.81454545 0.18545455]
 [0.95807292 0.04192708]
 [0.8625     0.1375    ]
 [0.44024725 0.55975275]
 [0.21601382 0.78398618]]
	- oob_score_ = 0.875

#### Importance of features
- gp_max_val_min = 0.1094631690803674
- gp_auc_max = 0.10893794425791585
- gp_auc_min = 0.10507676027676029
- gp_max_val_max = 0.08302180093214577
- gp_max_val_mean = 0.079520841617929
- high_power = 0.07358826358826359
- hlbr = 0.06715623770169224
- gp_auc_mean = 0.06551256613756613
- coe1[0] = 0.037931985540232964
- diff_auc = 0.036886243386243384
- gp_max_ix_std = 0.02857142857142857
- ratio_max_to_9th_ave_peaks = 0.017424242424242425
- diff_std = 0.016800401386608287
- coe3[3] = 0.014545454545454545
- tdoa_range = 0.014506974506974508
- tdoa_max = 0.014034154198627887
- tdoa_min = 0.013300163040422782
- ac_std = 0.012925959098372892
- gp_max_ix_mean = 0.012195767195767196
- gp_max_ix_max = 0.01142857142857143
- gp_max_val_range = 0.010885714285714285
- ratio_max_to_10ms_ave_peaks = 0.01037037037037037
- tdoa_std = 0.009033114651671352
- gp_max_ix_range = 0.007977011494252874
- coe1[1] = 0.007559838637382339
- srmr = 0.006666666666666666
- low_power = 0.0059878787878787886
- gp_auc_range = 0.005151515151515152
- gp_max_val_std = 0.005
- gp_max_ix_min = 0.003
- tdoa_mean = 0.0028571428571428563
- ac_auc = 0.002681818181818182
- coe3[0] = 0.0
- coe3[1] = 0.0
- coe3[2] = 0.0
- gp_auc_std = 0.0

## Evaluation
cv = 8
### accuracy
- Scores = [ 1.0, 1.0, 0.8333333333333334, 1.0, 1.0, 0.8333333333333334, 1.0, 1.0 ]
- Mean = 0.9583333333333334
- Standard deviation = 0.0721687836487032

### balanced_accuracy
- Scores = [ 1.0, 1.0, 0.875, 1.0, 1.0, 0.75, 1.0, 1.0 ]
- Mean = 0.953125
- Standard deviation = 0.08699631816921909

### f1
- Scores = [ 1.0, 1.0, 0.8, 1.0, 1.0, 0.6666666666666666, 1.0, 1.0 ]
- Mean = 0.9333333333333333
- Standard deviation = 0.12018504251546633

### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 29 | 1 |
| Actual Positive | 1 | 17 |

      