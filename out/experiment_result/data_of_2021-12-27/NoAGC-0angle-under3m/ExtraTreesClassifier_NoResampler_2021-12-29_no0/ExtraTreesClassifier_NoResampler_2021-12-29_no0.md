# ExtraTreesClassifier_NoResampler_2021-12-29_no0
## Constants
- CSV_PATH = ../out/csv/experiment
- OUTPUT_PATH = ../out/experiment_result/data_of_2021-12-27/NoAGC-0angle-under3m
- FEATURE_ATTRBS = ['low_power', 'high_power', 'hlbr', 'coe1[0]', 'coe1[1]', 'coe3[0]', 'coe3[1]', 'coe3[2]', 'coe3[3]', 'ratio_max_to_10ms_ave_peaks', 'ratio_max_to_9th_ave_peaks', 'ac_std', 'ac_auc', 'diff_std', 'diff_auc', 'srmr', 'gp_max_val_std', 'gp_max_val_range', 'gp_max_val_min', 'gp_max_val_max', 'gp_max_val_mean', 'gp_max_ix_std', 'gp_max_ix_range', 'gp_max_ix_min', 'gp_max_ix_max', 'gp_max_ix_mean', 'gp_auc_std', 'gp_auc_range', 'gp_auc_min', 'gp_auc_max', 'gp_auc_mean', 'tdoa_std', 'tdoa_range', 'tdoa_min', 'tdoa_max', 'tdoa_mean']
- LABEL_ATTRB = ['facing']
- FACING_DOV_ANGLES = [1]
- NCV = 8
- SCORING = ['accuracy', 'balanced_accuracy', 'f1']
- REFIT_SCORING = balanced_accuracy
- PARAM_GRID = [{'est__n_estimators': [50, 100, 150, 200, 300], 'est__min_samples_split': [2, 5, 10], 'est__min_samples_leaf': [1, 5, 10], 'est__max_features': ['sqrt', 'log2', None], 'est__bootstrap': [False], 'est__n_jobs': [-1], 'est__random_state': [42], 'est__max_samples': [0.01, 0.5, 0.09]}, {'est__n_estimators': [50, 100, 150, 200, 300], 'est__min_samples_split': [2, 5, 10], 'est__min_samples_leaf': [1, 5, 10], 'est__max_features': ['sqrt', 'log2', None], 'est__bootstrap': [True], 'est__oob_score': [True, False], 'est__n_jobs': [-1], 'est__random_state': [42], 'est__max_samples': [0.01, 0.5, 0.09]}]
- TRAIN_SET_SESSION = ['trial1', 'trial2']
- TEST_SET_SESSION = ['trial3', 'trial4', 'trial5']
- DISTANCE = [1, 3]
- AGC_STATUS = ['NoAGC']

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
	- n_estimators = 150
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
- gp_auc_min = 0.15728842093989528
- gp_max_val_min = 0.1406422413770104
- coe1[1] = 0.10131644122372288
- diff_auc = 0.08597804691583599
- coe1[0] = 0.07395697281787222
- diff_std = 0.0716116695398821
- srmr = 0.0432468472176987
- gp_auc_max = 0.027747600298897848
- gp_max_val_max = 0.026738794038751377
- gp_max_val_mean = 0.026379814175030162
- high_power = 0.025790583562004085
- low_power = 0.01848880797127394
- coe3[3] = 0.017313346975768987
- gp_max_val_range = 0.017155453418463643
- gp_auc_range = 0.017022365870828237
- gp_auc_mean = 0.0167037059029141
- ac_auc = 0.015525188010904127
- gp_auc_std = 0.013754777729390077
- ac_std = 0.013221137011791326
- coe3[2] = 0.010604850828842383
- gp_max_ix_range = 0.008530234304230978
- tdoa_range = 0.0081456240429152
- ratio_max_to_10ms_ave_peaks = 0.007274930154009625
- tdoa_min = 0.00725497677873805
- gp_max_ix_min = 0.006282337189220801
- gp_max_val_std = 0.006209079957610803
- tdoa_std = 0.0061196554264476965
- tdoa_mean = 0.005739218824965643
- gp_max_ix_mean = 0.005665013165127563
- gp_max_ix_std = 0.004770394806812834
- ratio_max_to_9th_ave_peaks = 0.004467633904320593
- hlbr = 0.003920568574427238
- gp_max_ix_max = 0.0031582586524544222
- tdoa_max = 0.0019750083919406634
- coe3[0] = 0.0
- coe3[1] = 0.0

## Evaluation
cv = 8
### accuracy
- Scores = [ 0.8, 0.8666666666666667, 0.7333333333333333, 1.0, 0.7333333333333333, 0.9333333333333333, 0.7333333333333333, 0.8571428571428571 ]
- Mean = 0.8321428571428572
- Standard deviation = 0.09391189724653873

### balanced_accuracy
- Scores = [ 0.5, 0.6666666666666666, 0.4583333333333333, 1.0, 0.4583333333333333, 0.8333333333333333, 0.5833333333333334, 0.7878787878787878 ]
- Mean = 0.6609848484848484
- Standard deviation = 0.185354653479687

### f1
- Scores = [ 0.0, 0.5, 0.0, 1.0, 0.0, 0.8, 0.3333333333333333, 0.6666666666666666 ]
- Mean = 0.4125
- Standard deviation = 0.3681551228007624

### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 90 | 5 |
| Actual Positive | 15 | 9 |

      