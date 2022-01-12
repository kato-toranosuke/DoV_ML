# ExtraTreesClassifier_RandomUnderSampler_2022-01-10_no2
## Constants
- CSV_PATH = ../out/csv/experiment
- OUTPUT_PATH = ../out/experiment_result/data_of_2022-01-10/NoAGC-0angle-under3m
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
- 2022-01-10_raspi_48000Hz_w1_N2^12_overlap80.csv

## Estimator
### Type
- resampler = RandomUnderSampler
- estimator = ExtraTreesClassifier

### Arguments for hyperparameter search
- resampler = RandomUnderSampler
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
	- sampling_strategy = auto
	- random_state = 42
	- replacement = False
	- n_features_in_ = 36
	- sampling_strategy_ = OrderedDict([(0, 20)])
	- sample_indices_ = [38  2 28 39 24 36 14 86  6 16 61 41 83 43 84 57 91 75 69 50  0  1 10 11
 22 23 32 33 44 45 54 55 66 67 76 77 88 89 98 99]

- best_estimator
	- base_estimator = ExtraTreeClassifier()
	- n_estimators = 100
	- estimator_params = ('criterion', 'max_depth', 'min_samples_split', 'min_samples_leaf', 'min_weight_fraction_leaf', 'max_features', 'max_leaf_nodes', 'min_impurity_decrease', 'random_state', 'ccp_alpha')
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
	- min_samples_split = 10
	- min_samples_leaf = 1
	- min_weight_fraction_leaf = 0.0
	- max_features = None
	- max_leaf_nodes = None
	- min_impurity_decrease = 0.0
	- ccp_alpha = 0.0
	- n_features_in_ = 36
	- n_outputs_ = 1
	- classes_ = [0 1]
	- n_classes_ = 2
	- base_estimator_ = ExtraTreeClassifier()
	- oob_decision_function_ = [[0.9262488  0.0737512 ]
 [0.20826914 0.79173086]
 [0.89237243 0.10762757]
 [0.89688518 0.10311482]
 [0.28667587 0.71332413]
 [0.78201659 0.21798341]
 [0.81587871 0.18412129]
 [0.34862467 0.65137533]
 [0.91734428 0.08265572]
 [0.95254665 0.04745335]
 [0.86958263 0.13041737]
 [0.82445332 0.17554668]
 [0.94366241 0.05633759]
 [0.32925284 0.67074716]
 [0.59832077 0.40167923]
 [0.59690713 0.40309287]
 [0.91752946 0.08247054]
 [0.4431008  0.5568992 ]
 [0.20718984 0.79281016]
 [0.827585   0.172415  ]
 [0.25549446 0.74450554]
 [0.31777088 0.68222912]
 [0.28928928 0.71071072]
 [0.38884746 0.61115254]
 [0.36868286 0.63131714]
 [0.33360299 0.66639701]
 [0.25802578 0.74197422]
 [0.31608205 0.68391795]
 [0.47094867 0.52905133]
 [0.34585006 0.65414994]
 [0.26008888 0.73991112]
 [0.2340913  0.7659087 ]
 [0.5396152  0.4603848 ]
 [0.52584779 0.47415221]
 [0.31664254 0.68335746]
 [0.50555006 0.49444994]
 [0.25352808 0.74647192]
 [0.23070092 0.76929908]
 [0.29826783 0.70173217]
 [0.35275097 0.64724903]]
	- oob_score_ = 0.775

#### Importance of features
- gp_auc_mean = 0.13372523629417193
- gp_auc_min = 0.12389337800371646
- gp_max_val_mean = 0.11431716597167975
- gp_max_val_min = 0.10221844312044617
- srmr = 0.09938919604666369
- gp_auc_max = 0.06985683985169504
- gp_max_val_max = 0.05132085153679838
- hlbr = 0.04498836892358478
- gp_max_ix_max = 0.03872815892802188
- diff_auc = 0.03025079801300077
- ratio_max_to_10ms_ave_peaks = 0.02995795753578553
- coe1[0] = 0.02
- gp_max_ix_mean = 0.02
- diff_std = 0.016982758620689656
- coe3[3] = 0.013805215393192126
- tdoa_min = 0.013260315843097299
- gp_max_val_std = 0.012028192360080882
- tdoa_max = 0.011078220025588446
- tdoa_mean = 0.007823270596558797
- gp_max_val_range = 0.007100350629762393
- high_power = 0.007051572108133194
- gp_auc_range = 0.006561159333532874
- low_power = 0.00617707836591957
- gp_auc_std = 0.00609049773755656
- coe1[1] = 0.00441758231290573
- ac_std = 0.003620987141219884
- coe3[2] = 0.0025345622119815675
- ratio_max_to_9th_ave_peaks = 0.0023944926668662075
- tdoa_range = 0.0004273504273504264
- coe3[0] = 0.0
- coe3[1] = 0.0
- ac_auc = 0.0
- gp_max_ix_std = 0.0
- gp_max_ix_range = 0.0
- gp_max_ix_min = 0.0
- tdoa_std = 0.0

## Evaluation
cv = 8
### accuracy
- Scores = [ 0.5263157894736842, 0.6842105263157895, 0.8947368421052632, 0.7894736842105263, 0.8947368421052632, 0.7368421052631579, 0.6666666666666666, 0.8333333333333334 ]
- Mean = 0.7532894736842105
- Standard deviation = 0.11821273913089302

### balanced_accuracy
- Scores = [ 0.7, 0.8, 0.9333333333333333, 0.8666666666666667, 0.75, 0.8333333333333333, 0.8, 0.9 ]
- Mean = 0.8229166666666666
- Standard deviation = 0.07213870705491995

### f1
- Scores = [ 0.47058823529411764, 0.5714285714285715, 0.8, 0.6666666666666666, 0.6666666666666666, 0.6153846153846153, 0.5, 0.6666666666666666 ]
- Mean = 0.6196751777634131
- Standard deviation = 0.09876541027770903

### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 83 | 37 |
| Actual Positive | 1 | 29 |

      