# ExtraTreesClassifier_RandomOverSampler_2021-11-10_no2
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
- resampler = RandomOverSampler
- estimator = ExtraTreesClassifier

### Arguments for hyperparameter search
- resampler = RandomOverSampler
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
	- shrinkage = None
	- n_features_in_ = 36
	- sampling_strategy_ = OrderedDict([(1, 1440)])
	- shrinkage_ = None
	- sample_indices_ = [   0    1    2 ... 1375 3697 2545]

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
	- min_samples_split = 10
	- min_samples_leaf = 1
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
- gp_max_val_max = 0.12856867135542377
- gp_auc_max = 0.12454098204325155
- gp_auc_mean = 0.11054992428117434
- gp_max_val_mean = 0.10613460661923578
- gp_max_val_min = 0.03241039191423974
- gp_auc_min = 0.03060153066400955
- tdoa_mean = 0.026520456534685224
- gp_max_ix_mean = 0.026420965351643896
- gp_max_val_range = 0.02154113523095255
- gp_auc_range = 0.021434845093996957
- tdoa_min = 0.02101374852694524
- gp_max_ix_min = 0.020898399017568757
- tdoa_std = 0.02082106079095627
- gp_max_ix_std = 0.02034719826943473
- ac_auc = 0.019417849004532
- gp_max_val_std = 0.01894542059225329
- gp_auc_std = 0.017660086210583778
- gp_max_ix_range = 0.01725865012135156
- ratio_max_to_10ms_ave_peaks = 0.01702997304590626
- srmr = 0.016641654620949346
- diff_std = 0.016632303438260013
- tdoa_range = 0.01647128972793563
- high_power = 0.016224687796726825
- diff_auc = 0.016086303379648517
- ratio_max_to_9th_ave_peaks = 0.01590352302675558
- tdoa_max = 0.013874073963329217
- gp_max_ix_max = 0.013787774158153101
- hlbr = 0.01360565765559205
- ac_std = 0.011300189766870661
- coe1[1] = 0.010011503203544133
- coe3[2] = 0.00979643499546225
- coe1[0] = 0.009573691910299774
- coe3[3] = 0.00907145021128146
- low_power = 0.008903567477046164
- coe3[0] = 0.0
- coe3[1] = 0.0

## Evaluation
cv = 10
### accuracy
- Scores = [ 0.7847222222222222, 0.8819444444444444, 0.8784722222222222, 0.8645833333333334, 0.8611111111111112, 0.7951388888888888, 0.8420138888888888, 0.8246527777777778, 0.8836805555555556, 0.7690972222222222 ]
- Mean = 0.8385416666666666
- Standard deviation = 0.0406339021585379

### balanced_accuracy
- Scores = [ 0.8148148148148149, 0.8731481481481481, 0.875, 0.836111111111111, 0.8407407407407408, 0.7555555555555555, 0.8541666666666667, 0.7921296296296296, 0.8689814814814816, 0.7013888888888888 ]
- Mean = 0.8212037037037037
- Standard deviation = 0.05396003639843765

### f1
- Scores = [ 0.7651515151515151, 0.8418604651162791, 0.8416289592760181, 0.7999999999999999, 0.8039215686274509, 0.6861702127659575, 0.8108108108108107, 0.7390180878552973, 0.8393285371702638, 0.5830721003134797 ]
- Mean = 0.7710962257087072
- Standard deviation = 0.07858633335598952

### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 3206 | 394 |
| Actual Positive | 536 | 1624 |

      