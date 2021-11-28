# ExtraTreesClassifier_RandomOverSampler_2021-11-26_no0
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
- resampler = RandomOverSampler
- estimator = ExtraTreesClassifier

### Arguments for hyperparameter search
- resampler = RandomOverSampler
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
	- shrinkage = None
	- n_features_in_ = 36
	- sampling_strategy_ = OrderedDict([(1, 4320)])
	- shrinkage_ = None
	- sample_indices_ = [   0    1    2 ... 2928 2160 5144]

- best_estimator
	- base_estimator = ExtraTreeClassifier()
	- n_estimators = 200
	- estimator_params = ('criterion', 'max_depth', 'min_samples_split', 'min_samples_leaf', 'min_weight_fraction_leaf', 'max_features', 'max_leaf_nodes', 'min_impurity_decrease', 'min_impurity_split', 'random_state', 'ccp_alpha')
	- bootstrap = True
	- oob_score = True
	- n_jobs = -1
	- random_state = 42
	- verbose = 0
	- warm_start = False
	- class_weight = None
	- max_samples = 0.09
	- criterion = gini
	- max_depth = None
	- min_samples_split = 2
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
	- oob_decision_function_ = [[0.07344633 0.92655367]
 [0.15300546 0.84699454]
 [0.54945055 0.45054945]
 ...
 [0.08695652 0.91304348]
 [0.11299435 0.88700565]
 [0.21693122 0.78306878]]
	- oob_score_ = 0.9017857142857143

#### Importance of features
- gp_max_val_max = 0.15014860424253937
- gp_max_val_mean = 0.13264573129986734
- gp_max_val_min = 0.05994024951799015
- gp_max_val_range = 0.049215672151784545
- gp_max_val_std = 0.041798928809301035
- gp_auc_min = 0.04146954385040988
- ratio_max_to_10ms_ave_peaks = 0.03347118838223463
- gp_auc_mean = 0.031383415707438855
- gp_auc_max = 0.02679568770554887
- diff_auc = 0.025063266546192044
- srmr = 0.02471276898603485
- ratio_max_to_9th_ave_peaks = 0.0242806496360688
- gp_auc_std = 0.02403314550088533
- ac_auc = 0.023754103722926665
- gp_auc_range = 0.023604265608063793
- hlbr = 0.021780001876653104
- high_power = 0.02169132759900649
- diff_std = 0.021678644001114095
- gp_max_ix_mean = 0.018485090051689124
- ac_std = 0.01836652835063924
- tdoa_mean = 0.018131124903506646
- coe3[2] = 0.017173736321475265
- coe1[0] = 0.016413986139955237
- coe1[1] = 0.016113379713407913
- coe3[3] = 0.015608814273379328
- low_power = 0.01550056987824042
- tdoa_min = 0.015365427837928087
- gp_max_ix_std = 0.014145933856262751
- gp_max_ix_min = 0.01409129862728109
- tdoa_std = 0.013520675218245721
- gp_max_ix_max = 0.008280415768725105
- tdoa_max = 0.007268931777350853
- tdoa_range = 0.007050557812736873
- gp_max_ix_range = 0.0070163343251164875
- coe3[0] = 0.0
- coe3[1] = 0.0

## Evaluation
cv = 10
### accuracy
- Scores = [ 0.8784722222222222, 0.9010416666666666, 0.9027777777777778, 0.8888888888888888, 0.890625, 0.8888888888888888, 0.8871527777777778, 0.8888888888888888, 0.8819444444444444, 0.8767361111111112 ]
- Mean = 0.8885416666666666
- Standard deviation = 0.008061240809891589

### balanced_accuracy
- Scores = [ 0.6686507936507936, 0.6577380952380952, 0.623015873015873, 0.5555555555555556, 0.5922619047619048, 0.5615079365079365, 0.6200396825396826, 0.5555555555555556, 0.5515873015873016, 0.5069444444444444 ]
- Mean = 0.5892857142857143
- Standard deviation = 0.04932062383526921

### f1
- Scores = [ 0.4444444444444444, 0.4571428571428572, 0.391304347826087, 0.19999999999999998, 0.3076923076923077, 0.21951219512195125, 0.36893203883495146, 0.19999999999999998, 0.1904761904761905, 0.0273972602739726 ]
- Mean = 0.28069016418127624
- Standard deviation = 0.12952322737207336

### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 4981 | 59 |
| Actual Positive | 583 | 137 |

      