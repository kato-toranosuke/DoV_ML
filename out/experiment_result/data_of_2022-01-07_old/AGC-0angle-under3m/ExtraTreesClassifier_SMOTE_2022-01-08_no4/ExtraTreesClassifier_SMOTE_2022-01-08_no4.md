# ExtraTreesClassifier_SMOTE_2022-01-08_no4
## Constants
- CSV_PATH = ../out/csv/experiment
- OUTPUT_PATH = ../out/experiment_result/data_of_2022-01-07/AGC-0angle-under3m
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
- AGC_STATUS = ['AGC']

## Loaded CSV
- 2021-12-27_raspi_48000Hz_w1_N2^12_overlap80_with2022-01-07.csv

## Estimator
### Type
- resampler = SMOTE
- estimator = ExtraTreesClassifier

### Arguments for hyperparameter search
- resampler = SMOTE
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
	- k_neighbors = 5
	- n_jobs = -1
	- n_features_in_ = 36
	- sampling_strategy_ = OrderedDict([(1, 60)])
	- nn_k_ = NearestNeighbors(n_neighbors=6)

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
	- min_samples_split = 5
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
	- base_estimator_ = ExtraTreeClassifier()

#### Importance of features
- gp_auc_min = 0.10798083019268488
- gp_max_val_min = 0.08900836283530328
- gp_max_val_mean = 0.08598803596609086
- gp_max_val_max = 0.08454709555700883
- gp_auc_mean = 0.07677743867176406
- gp_auc_max = 0.0752563460288042
- diff_auc = 0.04358468109585543
- high_power = 0.02710380501550633
- srmr = 0.02654855427905206
- gp_auc_range = 0.02532427994510705
- diff_std = 0.024849869447054203
- gp_max_val_range = 0.021876367060247485
- coe1[0] = 0.020814156271838063
- gp_max_val_std = 0.020295634324608267
- hlbr = 0.020007931027106914
- tdoa_mean = 0.01902511601325963
- low_power = 0.01830905048421516
- ratio_max_to_10ms_ave_peaks = 0.016333093436687145
- gp_max_ix_max = 0.01591778316966943
- tdoa_max = 0.01495297995438534
- coe1[1] = 0.014626155112136914
- coe3[3] = 0.014327364114441198
- ac_std = 0.01420515779425776
- gp_auc_std = 0.013984806982287424
- tdoa_range = 0.013617727309839634
- coe3[2] = 0.013312579859240172
- ac_auc = 0.011580582043927926
- gp_max_ix_range = 0.011577336981074679
- gp_max_ix_min = 0.011252727205965063
- gp_max_ix_mean = 0.010240699865541353
- tdoa_std = 0.010085424646672777
- gp_max_ix_std = 0.009746643007308865
- ratio_max_to_9th_ave_peaks = 0.00864645005796754
- tdoa_min = 0.00829493424308992
- coe3[0] = 0.0
- coe3[1] = 0.0

## Evaluation
cv = 8
### accuracy
- Scores = [ 0.47368421052631576, 0.7368421052631579, 0.8947368421052632, 0.7894736842105263, 0.9473684210526315, 0.8947368421052632, 0.7222222222222222, 0.8888888888888888 ]
- Mean = 0.7934941520467835
- Standard deviation = 0.1431176597691791

### balanced_accuracy
- Scores = [ 0.39166666666666666, 0.7416666666666667, 0.8416666666666667, 0.5916666666666667, 0.875, 0.9333333333333333, 0.43333333333333335, 0.8 ]
- Mean = 0.7010416666666667
- Standard deviation = 0.19195799869734234

### f1
- Scores = [ 0.16666666666666666, 0.5454545454545454, 0.75, 0.3333333333333333, 0.8571428571428571, 0.8, 0.0, 0.6666666666666666 ]
- Mean = 0.5149080086580087
- Standard deviation = 0.29517067372118183

### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 104 | 16 |
| Actual Positive | 16 | 14 |

      