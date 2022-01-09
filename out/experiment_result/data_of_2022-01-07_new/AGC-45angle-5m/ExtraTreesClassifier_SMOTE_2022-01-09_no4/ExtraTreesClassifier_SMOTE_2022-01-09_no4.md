# ExtraTreesClassifier_SMOTE_2022-01-09_no4
## Constants
- CSV_PATH = ../out/csv/experiment
- OUTPUT_PATH = ../out/experiment_result/data_of_2022-01-07_new/AGC-45angle-5m
- FEATURE_ATTRBS = ['low_power', 'high_power', 'hlbr', 'coe1[0]', 'coe1[1]', 'coe3[0]', 'coe3[1]', 'coe3[2]', 'coe3[3]', 'ratio_max_to_10ms_ave_peaks', 'ratio_max_to_9th_ave_peaks', 'ac_std', 'ac_auc', 'diff_std', 'diff_auc', 'srmr', 'gp_max_val_std', 'gp_max_val_range', 'gp_max_val_min', 'gp_max_val_max', 'gp_max_val_mean', 'gp_max_ix_std', 'gp_max_ix_range', 'gp_max_ix_min', 'gp_max_ix_max', 'gp_max_ix_mean', 'gp_auc_std', 'gp_auc_range', 'gp_auc_min', 'gp_auc_max', 'gp_auc_mean', 'tdoa_std', 'tdoa_range', 'tdoa_min', 'tdoa_max', 'tdoa_mean']
- LABEL_ATTRB = ['facing2']
- FACING_DOV_ANGLES = [1, 2]
- NCV = 8
- SCORING = ['accuracy', 'balanced_accuracy', 'f1']
- REFIT_SCORING = balanced_accuracy
- PARAM_GRID = [{'est__n_estimators': [50, 100, 150, 200, 300], 'est__min_samples_split': [2, 5, 10], 'est__min_samples_leaf': [1, 5, 10], 'est__max_features': ['sqrt', 'log2', None], 'est__bootstrap': [False], 'est__n_jobs': [-1], 'est__random_state': [42], 'est__max_samples': [0.01, 0.5, 0.09]}, {'est__n_estimators': [50, 100, 150, 200, 300], 'est__min_samples_split': [2, 5, 10], 'est__min_samples_leaf': [1, 5, 10], 'est__max_features': ['sqrt', 'log2', None], 'est__bootstrap': [True], 'est__oob_score': [True, False], 'est__n_jobs': [-1], 'est__random_state': [42], 'est__max_samples': [0.01, 0.5, 0.09]}]
- TRAIN_SET_SESSION = ['trial1', 'trial2']
- TEST_SET_SESSION = ['trial3', 'trial4', 'trial5']
- DISTANCE = [5]
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
	- sampling_strategy_ = OrderedDict([(0, 2)])
	- nn_k_ = NearestNeighbors(n_neighbors=6)

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
	- max_features = sqrt
	- max_leaf_nodes = None
	- min_impurity_decrease = 0.0
	- ccp_alpha = 0.0
	- n_features_in_ = 36
	- n_outputs_ = 1
	- classes_ = [0 1]
	- n_classes_ = 2
	- base_estimator_ = ExtraTreeClassifier()

#### Importance of features
- high_power = 0.11613404206362768
- gp_max_val_max = 0.10311204381628786
- gp_auc_max = 0.08950988729470351
- gp_max_val_mean = 0.08311254346997324
- gp_auc_mean = 0.06855236714594412
- gp_auc_min = 0.06502559906904906
- gp_max_val_min = 0.05793371960702278
- hlbr = 0.05192407452744329
- diff_auc = 0.04981089791434618
- srmr = 0.04549718300167933
- coe1[0] = 0.037354354017207485
- coe3[3] = 0.030896376940579368
- coe1[1] = 0.021332685419534054
- low_power = 0.020865106288675647
- coe3[2] = 0.019034748941733327
- diff_std = 0.017231684981684977
- gp_max_val_std = 0.016692950499649622
- gp_auc_std = 0.013740498432353636
- gp_auc_range = 0.012499636434419042
- tdoa_min = 0.012317771692519302
- tdoa_max = 0.011125375931258286
- gp_max_ix_min = 0.00962021682021682
- ac_auc = 0.009587289903079377
- gp_max_ix_max = 0.008994306768500316
- gp_max_ix_range = 0.008542692939244662
- tdoa_range = 0.005217500448269678
- ac_std = 0.004333333333333333
- gp_max_val_range = 0.0034968387933905186
- ratio_max_to_9th_ave_peaks = 0.0024102564102564104
- ratio_max_to_10ms_ave_peaks = 0.0014871794871794868
- gp_max_ix_mean = 0.0010683760683760685
- tdoa_std = 0.0010256410256410256
- tdoa_mean = 0.0005128205128205129
- coe3[0] = 0.0
- coe3[1] = 0.0
- gp_max_ix_std = 0.0

## Evaluation
cv = 8
### accuracy
- Scores = [ 0.9, 1.0, 0.9, 0.6666666666666666, 1.0, 1.0, 1.0, 1.0 ]
- Mean = 0.9333333333333333
- Standard deviation = 0.10929064207170001

### balanced_accuracy
- Scores = [ 0.9, 1.0, 0.9, 0.7, 1.0, 1.0, 1.0, 1.0 ]
- Mean = 0.9375
- Standard deviation = 0.09921567416492216

### f1
- Scores = [ 0.9090909090909091, 1.0, 0.9090909090909091, 0.5714285714285715, 1.0, 1.0, 1.0, 1.0 ]
- Mean = 0.9237012987012987
- Standard deviation = 0.13857780325896452

### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 34 | 2 |
| Actual Positive | 1 | 38 |

      