# ExtraTreesClassifier_NoResampler_2022-01-09_no0
## Constants
- CSV_PATH = ../out/csv/experiment
- OUTPUT_PATH = ../out/experiment_result/data_of_2022-01-07_new/AGC-0angle-1m
- FEATURE_ATTRBS = ['low_power', 'high_power', 'hlbr', 'coe1[0]', 'coe1[1]', 'coe3[0]', 'coe3[1]', 'coe3[2]', 'coe3[3]', 'ratio_max_to_10ms_ave_peaks', 'ratio_max_to_9th_ave_peaks', 'ac_std', 'ac_auc', 'diff_std', 'diff_auc', 'srmr', 'gp_max_val_std', 'gp_max_val_range', 'gp_max_val_min', 'gp_max_val_max', 'gp_max_val_mean', 'gp_max_ix_std', 'gp_max_ix_range', 'gp_max_ix_min', 'gp_max_ix_max', 'gp_max_ix_mean', 'gp_auc_std', 'gp_auc_range', 'gp_auc_min', 'gp_auc_max', 'gp_auc_mean', 'tdoa_std', 'tdoa_range', 'tdoa_min', 'tdoa_max', 'tdoa_mean']
- LABEL_ATTRB = ['facing']
- FACING_DOV_ANGLES = [1]
- NCV = 8
- SCORING = ['accuracy', 'balanced_accuracy', 'f1']
- REFIT_SCORING = balanced_accuracy
- PARAM_GRID = [{'est__n_estimators': [50, 100, 150, 200, 300], 'est__min_samples_split': [2, 5, 10], 'est__min_samples_leaf': [1, 5, 10], 'est__max_features': ['sqrt', 'log2', None], 'est__bootstrap': [False], 'est__n_jobs': [-1], 'est__random_state': [42], 'est__max_samples': [0.01, 0.5, 0.09]}, {'est__n_estimators': [50, 100, 150, 200, 300], 'est__min_samples_split': [2, 5, 10], 'est__min_samples_leaf': [1, 5, 10], 'est__max_features': ['sqrt', 'log2', None], 'est__bootstrap': [True], 'est__oob_score': [True, False], 'est__n_jobs': [-1], 'est__random_state': [42], 'est__max_samples': [0.01, 0.5, 0.09]}]
- TRAIN_SET_SESSION = ['trial1', 'trial2']
- TEST_SET_SESSION = ['trial3', 'trial4', 'trial5']
- DISTANCE = [1]
- AGC_STATUS = ['AGC']

## Loaded CSV
- 2021-12-27_raspi_48000Hz_w1_N2^12_overlap80_with2022-01-07.csv

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
	- estimator_params = ('criterion', 'max_depth', 'min_samples_split', 'min_samples_leaf', 'min_weight_fraction_leaf', 'max_features', 'max_leaf_nodes', 'min_impurity_decrease', 'random_state', 'ccp_alpha')
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
	- max_features = log2
	- max_leaf_nodes = None
	- min_impurity_decrease = 0.0
	- ccp_alpha = 0.0
	- n_features_in_ = 36
	- n_outputs_ = 1
	- classes_ = [0 1]
	- n_classes_ = 2
	- base_estimator_ = ExtraTreeClassifier()

#### Importance of features
- gp_auc_min = 0.0760439593546864
- gp_auc_max = 0.0553258047170319
- gp_max_val_max = 0.054420544674631345
- gp_max_val_range = 0.05068491766316999
- gp_auc_range = 0.047983269615014014
- gp_max_val_mean = 0.047830828785500594
- srmr = 0.047145268051434756
- gp_auc_mean = 0.0435336373931975
- gp_max_val_min = 0.04317821389412019
- gp_max_val_std = 0.038766807800449624
- low_power = 0.031937826141068625
- ac_std = 0.02940198393323379
- hlbr = 0.028217621664050237
- diff_std = 0.02797985448554095
- high_power = 0.027820060017013794
- gp_auc_std = 0.026699623135149446
- coe1[0] = 0.02660457694479433
- tdoa_std = 0.02571404509021141
- gp_max_ix_max = 0.024172082480909282
- ratio_max_to_10ms_ave_peaks = 0.023634037490987036
- tdoa_mean = 0.023615228253804195
- diff_auc = 0.023400974168925184
- gp_max_ix_std = 0.021995795361143936
- ac_auc = 0.019889445521798468
- coe3[3] = 0.01946225877780756
- coe1[1] = 0.017447384407716263
- tdoa_range = 0.015833604439449794
- tdoa_max = 0.0135771969460408
- gp_max_ix_mean = 0.013124623700054737
- gp_max_ix_min = 0.012193026219730603
- ratio_max_to_9th_ave_peaks = 0.011963239579048403
- tdoa_min = 0.010716799540328949
- coe3[2] = 0.010236299027059897
- gp_max_ix_range = 0.009449160724896015
- coe3[0] = 0.0
- coe3[1] = 0.0

## Evaluation
cv = 8
### accuracy
- Scores = [ 0.4, 0.7, 0.8, 0.6666666666666666, 0.7777777777777778, 0.7777777777777778, 0.7777777777777778, 0.8888888888888888 ]
- Mean = 0.7236111111111112
- Standard deviation = 0.13714882202452944

### balanced_accuracy
- Scores = [ 0.25, 0.8125, 0.5, 0.42857142857142855, 0.5, 0.8571428571428572, 0.5, 0.5 ]
- Mean = 0.5435267857142857
- Standard deviation = 0.18629702850137972

### f1
- Scores = [ 0.0, 0.5714285714285715, 0.0, 0.0, 0.0, 0.6666666666666666, 0.0, 0.0 ]
- Mean = 0.15476190476190477
- Standard deviation = 0.2691108227489837

### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 51 | 9 |
| Actual Positive | 14 | 1 |

      