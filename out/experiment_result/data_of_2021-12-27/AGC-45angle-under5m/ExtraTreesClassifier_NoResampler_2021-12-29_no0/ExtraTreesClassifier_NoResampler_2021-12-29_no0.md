# ExtraTreesClassifier_NoResampler_2021-12-29_no0
## Constants
- CSV_PATH = ../out/csv/experiment
- OUTPUT_PATH = ../out/experiment_result/data_of_2021-12-27/AGC-45angle-under5m
- FEATURE_ATTRBS = ['low_power', 'high_power', 'hlbr', 'coe1[0]', 'coe1[1]', 'coe3[0]', 'coe3[1]', 'coe3[2]', 'coe3[3]', 'ratio_max_to_10ms_ave_peaks', 'ratio_max_to_9th_ave_peaks', 'ac_std', 'ac_auc', 'diff_std', 'diff_auc', 'srmr', 'gp_max_val_std', 'gp_max_val_range', 'gp_max_val_min', 'gp_max_val_max', 'gp_max_val_mean', 'gp_max_ix_std', 'gp_max_ix_range', 'gp_max_ix_min', 'gp_max_ix_max', 'gp_max_ix_mean', 'gp_auc_std', 'gp_auc_range', 'gp_auc_min', 'gp_auc_max', 'gp_auc_mean', 'tdoa_std', 'tdoa_range', 'tdoa_min', 'tdoa_max', 'tdoa_mean']
- LABEL_ATTRB = ['facing2']
- FACING_DOV_ANGLES = [1, 2]
- NCV = 8
- SCORING = ['accuracy', 'balanced_accuracy', 'f1']
- REFIT_SCORING = balanced_accuracy
- PARAM_GRID = [{'est__n_estimators': [50, 100, 150, 200, 300], 'est__min_samples_split': [2, 5, 10], 'est__min_samples_leaf': [1, 5, 10], 'est__max_features': ['sqrt', 'log2', None], 'est__bootstrap': [False], 'est__n_jobs': [-1], 'est__random_state': [42], 'est__max_samples': [0.01, 0.5, 0.09]}, {'est__n_estimators': [50, 100, 150, 200, 300], 'est__min_samples_split': [2, 5, 10], 'est__min_samples_leaf': [1, 5, 10], 'est__max_features': ['sqrt', 'log2', None], 'est__bootstrap': [True], 'est__oob_score': [True, False], 'est__n_jobs': [-1], 'est__random_state': [42], 'est__max_samples': [0.01, 0.5, 0.09]}]
- TRAIN_SET_SESSION = ['trial1', 'trial2']
- TEST_SET_SESSION = ['trial3', 'trial4', 'trial5']
- DISTANCE = [1, 3, 5]
- AGC_STATUS = ['AGC']

## Loaded CSV
- 2021-12-27_raspi_48000Hz_w1_N2^12_overlap80_new.csv

## Estimator
### Type
- resampler = NoResampler
- estimator = ExtraTreesClassifier

### Arguments for hyperparameter search
- resampler = NoResampler
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

- best_estimator
	- base_estimator = ExtraTreeClassifier()
	- n_estimators = 50
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
- gp_auc_min = 0.10987749742055099
- gp_auc_max = 0.09616319314296917
- diff_auc = 0.08070267487407258
- gp_max_val_min = 0.07516441632995652
- gp_max_val_mean = 0.0749143315812147
- high_power = 0.06527745084009455
- gp_auc_mean = 0.06183688336703201
- gp_max_val_max = 0.0463415248627898
- diff_std = 0.043115792099203354
- coe1[0] = 0.042987821510229125
- coe1[1] = 0.032656878881299166
- hlbr = 0.028415337100024505
- srmr = 0.02819531813203449
- coe3[3] = 0.022559367009454333
- ratio_max_to_10ms_ave_peaks = 0.017490643928502404
- low_power = 0.016713097687098815
- coe3[2] = 0.015674224178048084
- tdoa_min = 0.012190079917766829
- ac_auc = 0.011880656885788684
- tdoa_range = 0.011737228978081566
- ac_std = 0.010874699642698354
- gp_max_ix_range = 0.010278418069050006
- tdoa_std = 0.010062715609562383
- tdoa_mean = 0.009353046670413626
- gp_max_val_std = 0.009142146167492777
- gp_auc_std = 0.008914113279879182
- gp_max_ix_std = 0.008727267923325059
- gp_max_val_range = 0.008244751004858946
- gp_max_ix_min = 0.0062371552048377755
- tdoa_max = 0.006078855385582377
- gp_auc_range = 0.0055676258829941705
- ratio_max_to_9th_ave_peaks = 0.004444609190732553
- gp_max_ix_mean = 0.004426064092143885
- gp_max_ix_max = 0.0037541131502170835
- coe3[0] = 0.0
- coe3[1] = 0.0

## Evaluation
cv = 8
### accuracy
- Scores = [ 0.8928571428571429, 0.9285714285714286, 0.8928571428571429, 0.9285714285714286, 0.8928571428571429, 0.9642857142857143, 1.0, 0.9642857142857143 ]
- Mean = 0.9330357142857144
- Standard deviation = 0.03761674005882301

### balanced_accuracy
- Scores = [ 0.8846153846153846, 0.9333333333333333, 0.8948717948717949, 0.9282051282051282, 0.9, 0.9642857142857143, 1.0, 0.9642857142857143 ]
- Mean = 0.9336996336996337
- Standard deviation = 0.037665648934210275

### f1
- Scores = [ 0.9090909090909091, 0.9285714285714286, 0.896551724137931, 0.9333333333333333, 0.888888888888889, 0.962962962962963, 1.0, 0.962962962962963 ]
- Mean = 0.9352952762435521
- Standard deviation = 0.03554582759559935

### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 102 | 5 |
| Actual Positive | 10 | 107 |

      