# RandomForestClassifier_RandomUnderSampler_2021-11-23_no0
## Constants
- CSV_PATH = ../../out/csv/
- OUTPUT_PATH = ./result/
- FEATURE_ATTRBS = ['low_power', 'high_power', 'hlbr', 'coe1[0]', 'coe1[1]', 'coe3[0]', 'coe3[1]', 'coe3[2]', 'coe3[3]', 'ratio_max_to_10ms_ave_peaks', 'ratio_max_to_9th_ave_peaks', 'ac_std', 'ac_auc', 'diff_std', 'diff_auc', 'srmr', 'gp_max_val_std', 'gp_max_val_range', 'gp_max_val_mean', 'gp_max_ix_std', 'gp_max_ix_range', 'gp_max_ix_mean', 'gp_auc_std', 'gp_auc_range', 'gp_auc_mean', 'tdoa_std', 'tdoa_range', 'tdoa_mean']
- LABEL_ATTRB = ['dov_angle']
- FACING_DOV_ANGLES = [0, 45, 315]
- NCV = 10
- SCORING = ['accuracy', 'balanced_accuracy', 'f1']
- REFIT_SCORING = balanced_accuracy
- PARAM_GRID = [{'est__n_estimators': range(100, 1600, 100), 'est__min_samples_split': [2, 5, 10], 'est__min_samples_leaf': [1, 5, 10], 'est__max_features': ['sqrt', 'log2', None], 'est__bootstrap': [False], 'est__n_jobs': [-1], 'est__random_state': [42], 'est__max_samples': [0.01, 0.5, 0.09]}, {'est__n_estimators': range(100, 1600, 100), 'est__min_samples_split': [2, 5, 10], 'est__min_samples_leaf': [1, 5, 10], 'est__max_features': ['sqrt', 'log2', None], 'est__bootstrap': [True], 'est__oob_score': [True, False], 'est__n_jobs': [-1], 'est__random_state': [42], 'est__max_samples': [0.01, 0.5, 0.09]}]

## Loaded CSV
- features_mono_ch_matlab.csv

## Estimator
### Type
- resampler = RandomUnderSampler
- estimator = RandomForestClassifier

### Arguments for hyperparameter search
- resampler = RandomUnderSampler
- estimator = RandomForestClassifier
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
	- replacement = False
	- n_features_in_ = 28
	- sampling_strategy_ = OrderedDict([(0, 2160)])
	- sample_indices_ = [2146 2563 5678 ... 5752 5753 5759]

- best_estimator
	- base_estimator = DecisionTreeClassifier()
	- n_estimators = 1200
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
	- max_features = None
	- max_leaf_nodes = None
	- min_impurity_decrease = 0.0
	- min_impurity_split = None
	- ccp_alpha = 0.0
	- n_features_in_ = 28
	- n_features_ = 28
	- n_outputs_ = 1
	- classes_ = [0 1]
	- n_classes_ = 2
	- base_estimator_ = DecisionTreeClassifier()
	- oob_decision_function_ = [[0.87649219 0.12350781]
 [0.96093089 0.03906911]
 [0.91848659 0.08151341]
 ...
 [0.49521526 0.50478474]
 [0.91850841 0.08149159]
 [0.81031637 0.18968363]]
	- oob_score_ = 0.8381944444444445

#### Importance of features
- gp_max_val_mean = 0.4280736871746332
- gp_auc_mean = 0.053368265661422776
- gp_max_val_range = 0.051137154340765184
- gp_max_val_std = 0.04281014949845162
- ac_auc = 0.037919590243436635
- srmr = 0.03370417417028259
- diff_auc = 0.03246191719227425
- ratio_max_to_10ms_ave_peaks = 0.031162866443319334
- hlbr = 0.029544587871064183
- ratio_max_to_9th_ave_peaks = 0.029476304354395598
- high_power = 0.027762324681303227
- ac_std = 0.02465799435162739
- diff_std = 0.02359414847515257
- gp_auc_range = 0.02204926732136505
- gp_max_ix_mean = 0.016423203638104657
- coe1[1] = 0.015872956731172304
- tdoa_mean = 0.015734985712736564
- gp_max_ix_std = 0.015549078412406428
- tdoa_std = 0.015408621982002659
- low_power = 0.012959387875012001
- coe3[3] = 0.012071964938832565
- gp_auc_std = 0.010560938183822416
- coe3[2] = 0.009875638175060323
- gp_max_ix_range = 0.003577517362559537
- tdoa_range = 0.003424993359178636
- coe1[0] = 0.0008182818496183768
- coe3[0] = 0.0
- coe3[1] = 0.0

## Evaluation
cv = 10
### accuracy
- Scores = [ 0.7413194444444444, 0.9027777777777778, 0.859375, 0.8628472222222222, 0.8576388888888888, 0.7934027777777778, 0.8541666666666666, 0.8159722222222222, 0.8784722222222222, 0.7517361111111112 ]
- Mean = 0.8317708333333333
- Standard deviation = 0.05141029255841049

### balanced_accuracy
- Scores = [ 0.7791666666666667, 0.9037037037037037, 0.8569444444444445, 0.8273148148148148, 0.837962962962963, 0.7393518518518518, 0.8657407407407407, 0.775, 0.8546296296296296, 0.6782407407407407 ]
- Mean = 0.8118055555555556
- Standard deviation = 0.06454416042838163

### f1
- Scores = [ 0.7295825771324864, 0.875, 0.8187919463087249, 0.7893333333333332, 0.8, 0.6550724637681159, 0.8242677824267782, 0.7135135135135134, 0.8241206030150754, 0.5372168284789645 ]
- Mean = 0.7566899047976993
- Standard deviation = 0.09539523682775047

### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 3210 | 390 |
| Actual Positive | 579 | 1581 |

      