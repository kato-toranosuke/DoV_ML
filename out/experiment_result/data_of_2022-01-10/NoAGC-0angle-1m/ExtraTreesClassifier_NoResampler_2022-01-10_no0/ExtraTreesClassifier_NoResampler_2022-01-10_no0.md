# ExtraTreesClassifier_NoResampler_2022-01-10_no0
## Constants
- CSV_PATH = ../out/csv/experiment
- OUTPUT_PATH = ../out/experiment_result/data_of_2022-01-10/NoAGC-0angle-1m
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
- AGC_STATUS = ['NoAGC']

## Loaded CSV
- 2022-01-10_raspi_48000Hz_w1_N2^12_overlap80.csv

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
- gp_auc_max = 0.087636037196834
- gp_max_val_max = 0.06648633083587313
- gp_auc_min = 0.06578907360300039
- gp_max_val_mean = 0.04746033000029224
- gp_auc_mean = 0.04663039417976392
- gp_auc_std = 0.03998711392451716
- ratio_max_to_9th_ave_peaks = 0.03678276260273542
- tdoa_mean = 0.03380853992066613
- gp_max_val_min = 0.03251035013216677
- diff_std = 0.03242776051694458
- coe1[1] = 0.031668522136987176
- hlbr = 0.02856630590986241
- tdoa_max = 0.02836675653780917
- tdoa_std = 0.026912817483484452
- srmr = 0.025946180148763008
- tdoa_range = 0.02559003496503496
- diff_auc = 0.025163950498460933
- gp_max_ix_range = 0.024866960537895683
- gp_max_val_std = 0.0243484719399967
- gp_max_ix_mean = 0.02360497578424884
- high_power = 0.02342622655122655
- coe3[3] = 0.022043846659028987
- gp_max_ix_std = 0.021103137467108058
- gp_max_ix_max = 0.020879465801805615
- gp_auc_range = 0.0207454364520928
- ratio_max_to_10ms_ave_peaks = 0.019558531746031744
- ac_auc = 0.01874266157818789
- ac_std = 0.01847478093801623
- coe3[2] = 0.017420705286776708
- low_power = 0.016774758038523338
- gp_max_val_range = 0.01423142824456273
- gp_max_ix_min = 0.013742542882371908
- tdoa_min = 0.01120695276945277
- coe1[0] = 0.007095856729477415
- coe3[0] = 0.0
- coe3[1] = 0.0

## Evaluation
cv = 8
### accuracy
- Scores = [ 0.7, 0.8, 0.9, 0.4444444444444444, 0.7777777777777778, 0.7777777777777778, 0.7777777777777778, 0.7777777777777778 ]
- Mean = 0.7444444444444445
- Standard deviation = 0.12435016269777441

### balanced_accuracy
- Scores = [ 0.8125, 0.5, 0.75, 0.2857142857142857, 0.5, 0.5, 0.6785714285714286, 0.875 ]
- Mean = 0.6127232142857143
- Standard deviation = 0.18605617032826238

### f1
- Scores = [ 0.5714285714285715, 0.0, 0.6666666666666666, 0.0, 0.0, 0.0, 0.5, 0.5 ]
- Mean = 0.27976190476190477
- Standard deviation = 0.2839104766121862

### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 55 | 5 |
| Actual Positive | 13 | 2 |

      