# ExtraTreesClassifier_NoResampler_2021-12-29_no0
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
	- n_estimators = 100
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
- gp_max_val_min = 0.2457703643091998
- gp_auc_min = 0.17685355727741928
- gp_max_val_mean = 0.14992086483007971
- gp_auc_mean = 0.13439301814153978
- gp_max_val_max = 0.06486216339394886
- srmr = 0.05003069350505856
- gp_auc_max = 0.04608665615754643
- diff_auc = 0.029833019385550344
- diff_std = 0.0262483720395025
- ratio_max_to_10ms_ave_peaks = 0.010435171407619102
- hlbr = 0.009599499681364719
- coe1[1] = 0.009524806844348517
- coe1[0] = 0.008089791453798139
- gp_max_val_range = 0.005821217361255715
- coe3[2] = 0.005282949014193694
- low_power = 0.004877131517520466
- high_power = 0.004195893619547225
- ratio_max_to_9th_ave_peaks = 0.003377917222403301
- coe3[3] = 0.002460882743826121
- gp_auc_range = 0.0023694463343729775
- ac_std = 0.0023172468621612033
- ac_auc = 0.0019138749263747355
- gp_max_val_std = 0.0018392668032598519
- tdoa_std = 0.0014298425736679618
- gp_max_ix_mean = 0.0006287379433598866
- gp_max_ix_std = 0.0006074494390859834
- gp_auc_std = 0.0005324208552976725
- gp_max_ix_range = 0.00034056046957381094
- tdoa_min = 0.00024618490569801733
- tdoa_range = 4.6706136500827293e-05
- gp_max_ix_min = 3.252885315167473e-05
- gp_max_ix_max = 3.176399177318528e-05
- coe3[0] = 0.0
- coe3[1] = 0.0
- tdoa_max = 0.0
- tdoa_mean = 0.0

## Evaluation
cv = 8
### accuracy
- Scores = [ 0.8421052631578947, 1.0, 1.0, 0.8421052631578947, 1.0, 1.0, 0.9444444444444444, 0.9444444444444444 ]
- Mean = 0.9466374269005848
- Standard deviation = 0.06447268965298869

### balanced_accuracy
- Scores = [ 0.8333333333333333, 1.0, 1.0, 0.8388888888888889, 1.0, 1.0, 0.9444444444444444, 0.9444444444444444 ]
- Mean = 0.945138888888889
- Standard deviation = 0.06692297373533433

### f1
- Scores = [ 0.8695652173913044, 1.0, 1.0, 0.8571428571428572, 1.0, 1.0, 0.9411764705882353, 0.9411764705882353 ]
- Mean = 0.9511326269638289
- Standard deviation = 0.056166771565520565

### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 66 | 5 |
| Actual Positive | 3 | 75 |

      