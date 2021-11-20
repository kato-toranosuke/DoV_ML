# RandomForestClassifier_RandomUnderSampler_2021-11-11_no4
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
- resampler = RandomUnderSampler
- estimator = RandomForestClassifier

### Arguments for hyperparameter search
- resampler = RandomUnderSampler
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
	- replacement = False
	- n_features_in_ = 36
	- sampling_strategy_ = OrderedDict([(0, 2160)])
	- sample_indices_ = [2146 2563 5678 ... 5752 5753 5759]

- best_estimator
	- base_estimator = DecisionTreeClassifier()
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
	- min_samples_split = 2
	- min_samples_leaf = 10
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
	- base_estimator_ = DecisionTreeClassifier()

#### Importance of features
- gp_max_val_mean = 0.1657939302415762
- gp_max_val_max = 0.14146458111685115
- gp_auc_max = 0.08429877465729504
- gp_max_val_min = 0.06026189677778013
- high_power = 0.056523190666619066
- gp_max_val_range = 0.055321369016008246
- gp_max_val_std = 0.03727028778808756
- gp_max_ix_mean = 0.030056349165249675
- tdoa_mean = 0.02859757993573597
- hlbr = 0.026783701325434815
- diff_std = 0.02665965033903292
- gp_max_ix_std = 0.02639454679683279
- gp_auc_mean = 0.024904105897515797
- tdoa_std = 0.019028346252579913
- diff_auc = 0.018471057876946712
- gp_max_ix_min = 0.017693138638341127
- ac_auc = 0.016804390709298796
- srmr = 0.01662277431502668
- tdoa_min = 0.016606691828820536
- gp_auc_min = 0.013931288223803857
- coe1[1] = 0.013774344991313242
- gp_max_ix_max = 0.013440301249181464
- tdoa_max = 0.013256419882909301
- ac_std = 0.011204754812417336
- gp_max_ix_range = 0.010799557848812268
- tdoa_range = 0.010422640670934659
- low_power = 0.01020413408208301
- ratio_max_to_10ms_ave_peaks = 0.009374587590522475
- coe3[3] = 0.008377000937383883
- ratio_max_to_9th_ave_peaks = 0.006982967260367624
- coe3[2] = 0.004890023375287556
- gp_auc_range = 0.003022933249182624
- gp_auc_std = 0.0007228804946810865
- coe1[0] = 3.980198608651155e-05
- coe3[0] = 0.0
- coe3[1] = 0.0

## Evaluation
cv = 10
### accuracy
- Scores = [ 0.765625, 0.8819444444444444, 0.8784722222222222, 0.8541666666666666, 0.8697916666666666, 0.8020833333333334, 0.8506944444444444, 0.8159722222222222, 0.8802083333333334, 0.765625 ]
- Mean = 0.8364583333333332
- Standard deviation = 0.04360231908899194

### balanced_accuracy
- Scores = [ 0.8041666666666667, 0.8777777777777778, 0.8675925925925926, 0.8231481481481482, 0.8486111111111111, 0.7592592592592593, 0.8611111111111112, 0.787037037037037, 0.8652777777777778, 0.6949074074074074 ]
- Mean = 0.818888888888889
- Standard deviation = 0.05552885160678344

### f1
- Scores = [ 0.7540983606557377, 0.8454545454545456, 0.8356807511737089, 0.7823834196891192, 0.8148148148148149, 0.6902173913043478, 0.8193277310924371, 0.7323232323232323, 0.8345323741007193, 0.5686900958466453 ]
- Mean = 0.7677522716455308
- Standard deviation = 0.08202410552133221

### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 3201 | 399 |
| Actual Positive | 543 | 1617 |

      