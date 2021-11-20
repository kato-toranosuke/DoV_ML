# RandomForestClassifier_RandomOverSampler_2021-11-12_no0
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
- features_mono_ch_matlab.csv

## Estimator
### Type
- resampler = RandomOverSampler
- estimator = RandomForestClassifier

### Arguments for hyperparameter search
- resampler = RandomOverSampler
- estimator = RandomForestClassifier
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
	- base_estimator = DecisionTreeClassifier()
	- n_estimators = 800
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
	- min_samples_split = 2
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
	- base_estimator_ = DecisionTreeClassifier()
	- oob_decision_function_ = [[0.01046025 0.98953975]
 [0.01070664 0.98929336]
 [0.31101512 0.68898488]
 ...
 [0.03853955 0.96146045]
 [0.2327044  0.7672956 ]
 [0.30490405 0.69509595]]
	- oob_score_ = 0.9056944444444445

#### Importance of features
- gp_max_val_mean = 0.13108285584876528
- gp_max_val_max = 0.10910075560583486
- gp_max_val_min = 0.0626043141304414
- high_power = 0.05783329417016724
- gp_max_val_range = 0.05279278084724188
- gp_max_val_std = 0.045901621819825
- hlbr = 0.04099886193633572
- diff_std = 0.038416101313592875
- gp_auc_max = 0.03165424217270657
- diff_auc = 0.028500834761518108
- gp_auc_min = 0.02831586219392929
- srmr = 0.02824733277342783
- ac_auc = 0.026255505875729095
- gp_auc_mean = 0.024802592330537103
- coe1[1] = 0.024019115200129646
- ratio_max_to_10ms_ave_peaks = 0.023588969119285638
- ac_std = 0.022098987683031847
- low_power = 0.021472308827851786
- ratio_max_to_9th_ave_peaks = 0.021202494473836594
- gp_max_ix_mean = 0.02076262915238138
- tdoa_mean = 0.020536826749992187
- coe3[3] = 0.019305709491465154
- gp_max_ix_std = 0.018656344324919704
- tdoa_std = 0.018261308826383254
- gp_auc_range = 0.018223529211978253
- coe3[2] = 0.014438823969466025
- gp_auc_std = 0.01141265882792027
- tdoa_min = 0.008028627590857831
- gp_max_ix_min = 0.007850020541845372
- tdoa_range = 0.005956436299847108
- gp_max_ix_range = 0.005574903890136438
- gp_max_ix_max = 0.004812162432148934
- tdoa_max = 0.004679219217403927
- coe1[0] = 0.002611968389066445
- coe3[0] = 0.0
- coe3[1] = 0.0

## Evaluation
cv = 10
### accuracy
- Scores = [ 0.7552083333333334, 0.890625, 0.8871527777777778, 0.8611111111111112, 0.8576388888888888, 0.8003472222222222, 0.8524305555555556, 0.8229166666666666, 0.890625, 0.75 ]
- Mean = 0.8368055555555556
- Standard deviation = 0.050311289859689336

### balanced_accuracy
- Scores = [ 0.7967592592592592, 0.8939814814814815, 0.8800925925925926, 0.825, 0.837962962962963, 0.7476851851851852, 0.8625, 0.7833333333333333, 0.8736111111111111, 0.674074074074074 ]
- Mean = 0.8175000000000001
- Standard deviation = 0.06516005934108206

### f1
- Scores = [ 0.7468581687612209, 0.8615384615384615, 0.8498845265588915, 0.786096256684492, 0.8, 0.6685878962536024, 0.8210526315789475, 0.7258064516129031, 0.8467153284671534, 0.5263157894736842 ]
- Mean = 0.7632855510929356
- Standard deviation = 0.09803862243705468

### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 3221 | 379 |
| Actual Positive | 561 | 1599 |

      