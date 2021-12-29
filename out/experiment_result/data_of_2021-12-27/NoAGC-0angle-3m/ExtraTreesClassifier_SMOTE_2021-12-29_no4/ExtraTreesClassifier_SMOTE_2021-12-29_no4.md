# ExtraTreesClassifier_SMOTE_2021-12-29_no4
## Constants
- CSV_PATH = ../out/csv/experiment
- OUTPUT_PATH = ../out/experiment_result/data_of_2021-12-27/NoAGC-0angle-3m
- FEATURE_ATTRBS = ['low_power', 'high_power', 'hlbr', 'coe1[0]', 'coe1[1]', 'coe3[0]', 'coe3[1]', 'coe3[2]', 'coe3[3]', 'ratio_max_to_10ms_ave_peaks', 'ratio_max_to_9th_ave_peaks', 'ac_std', 'ac_auc', 'diff_std', 'diff_auc', 'srmr', 'gp_max_val_std', 'gp_max_val_range', 'gp_max_val_min', 'gp_max_val_max', 'gp_max_val_mean', 'gp_max_ix_std', 'gp_max_ix_range', 'gp_max_ix_min', 'gp_max_ix_max', 'gp_max_ix_mean', 'gp_auc_std', 'gp_auc_range', 'gp_auc_min', 'gp_auc_max', 'gp_auc_mean', 'tdoa_std', 'tdoa_range', 'tdoa_min', 'tdoa_max', 'tdoa_mean']
- LABEL_ATTRB = ['facing']
- FACING_DOV_ANGLES = [1]
- NCV = 8
- SCORING = ['accuracy', 'balanced_accuracy', 'f1']
- REFIT_SCORING = balanced_accuracy
- PARAM_GRID = [{'est__n_estimators': [50, 100, 150, 200, 300], 'est__min_samples_split': [2, 5, 10], 'est__min_samples_leaf': [1, 5, 10], 'est__max_features': ['sqrt', 'log2', None], 'est__bootstrap': [False], 'est__n_jobs': [-1], 'est__random_state': [42], 'est__max_samples': [0.01, 0.5, 0.09]}, {'est__n_estimators': [50, 100, 150, 200, 300], 'est__min_samples_split': [2, 5, 10], 'est__min_samples_leaf': [1, 5, 10], 'est__max_features': ['sqrt', 'log2', None], 'est__bootstrap': [True], 'est__oob_score': [True, False], 'est__n_jobs': [-1], 'est__random_state': [42], 'est__max_samples': [0.01, 0.5, 0.09]}]
- TRAIN_SET_SESSION = ['trial1', 'trial2']
- TEST_SET_SESSION = ['trial3', 'trial4', 'trial5']
- DISTANCE = [3]
- AGC_STATUS = ['NoAGC']

## Loaded CSV
- 2021-12-27_raspi_48000Hz_w1_N2^12_overlap80_new.csv

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
	- sampling_strategy_ = OrderedDict([(1, 24)])
	- nn_k_ = NearestNeighbors(n_neighbors=6)

- best_estimator
	- base_estimator = ExtraTreeClassifier()
	- n_estimators = 50
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
	- min_samples_split = 10
	- min_samples_leaf = 1
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
	- base_estimator_ = ExtraTreeClassifier()
	- oob_decision_function_ = [[0.15212392 0.84787608]
 [0.18474284 0.81525716]
 [0.83219419 0.16780581]
 [0.46169109 0.53830891]
 [0.98518519 0.01481481]
 [0.85755208 0.14244792]
 [0.96488095 0.03511905]
 [0.96089744 0.03910256]
 [0.96362007 0.03637993]
 [0.91612903 0.08387097]
 [0.71888121 0.28111879]
 [0.39448329 0.60551671]
 [0.43758971 0.56241029]
 [0.23935786 0.76064214]
 [0.65649454 0.34350546]
 [0.59262935 0.40737065]
 [0.92658472 0.07341528]
 [0.88945594 0.11054406]
 [0.92662835 0.07337165]
 [0.87642857 0.12357143]
 [0.81488095 0.18511905]
 [0.86186975 0.13813025]
 [0.95955988 0.04044012]
 [0.76516715 0.23483285]
 [0.32645202 0.67354798]
 [0.28685854 0.71314146]
 [0.46096013 0.53903987]
 [0.34760656 0.65239344]
 [0.96168503 0.03831497]
 [0.9758547  0.0241453 ]
 [0.99666667 0.00333333]
 [0.96369048 0.03630952]
 [0.97992991 0.02007009]
 [0.96666667 0.03333333]
 [0.71679487 0.28320513]
 [0.28471699 0.71528301]
 [0.10491522 0.89508478]
 [0.0940931  0.9059069 ]
 [0.43186545 0.56813455]
 [0.44084804 0.55915196]
 [0.20598701 0.79401299]
 [0.25627656 0.74372344]
 [0.45581755 0.54418245]
 [0.06359628 0.93640372]
 [0.31068417 0.68931583]
 [0.03657361 0.96342639]
 [0.11489448 0.88510552]
 [0.18405751 0.81594249]
 [0.41528711 0.58471289]
 [0.15942703 0.84057297]
 [0.26525858 0.73474142]
 [0.2210152  0.7789848 ]
 [0.10734007 0.89265993]
 [0.29200261 0.70799739]
 [0.12907415 0.87092585]
 [0.15678953 0.84321047]
 [0.18380952 0.81619048]
 [0.29440795 0.70559205]
 [0.13206328 0.86793672]
 [0.03858693 0.96141307]
 [0.16577767 0.83422233]
 [0.25648578 0.74351422]
 [0.12584835 0.87415165]
 [0.26768529 0.73231471]]
	- oob_score_ = 0.890625

#### Importance of features
- high_power = 0.21126738336680334
- gp_auc_max = 0.08723383663129951
- srmr = 0.07097754806249969
- gp_auc_min = 0.06878874867323467
- diff_auc = 0.06680975334807288
- gp_max_val_max = 0.04919254932960302
- gp_auc_mean = 0.04646687676313992
- gp_max_val_mean = 0.04552227888619757
- hlbr = 0.044257297226477144
- gp_max_val_min = 0.036555216060980424
- ac_auc = 0.033258386345441864
- low_power = 0.03208103802805237
- diff_std = 0.03070995984666209
- gp_max_val_range = 0.02384085766283861
- tdoa_mean = 0.01890198145530605
- gp_max_ix_std = 0.01778133152835773
- gp_max_ix_max = 0.017394374375146043
- ratio_max_to_10ms_ave_peaks = 0.017021821442562386
- coe3[3] = 0.01548661199090164
- gp_max_ix_mean = 0.013680839796604742
- gp_auc_range = 0.010882168015665897
- gp_max_val_std = 0.007517702819232972
- coe1[0] = 0.007467329150497468
- ratio_max_to_9th_ave_peaks = 0.004897094438048845
- tdoa_std = 0.004368856295833984
- coe1[1] = 0.0043297402775077575
- ac_std = 0.003901899317720818
- coe3[2] = 0.0033026046938889842
- tdoa_max = 0.003140502246010549
- gp_max_ix_range = 0.002308650020649181
- tdoa_range = 0.0006547619047619056
- coe3[0] = 0.0
- coe3[1] = 0.0
- gp_max_ix_min = 0.0
- gp_auc_std = 0.0
- tdoa_min = 0.0

## Evaluation
cv = 8
### accuracy
- Scores = [ 0.875, 0.875, 0.875, 0.875, 0.7142857142857143, 0.7142857142857143, 1.0, 0.42857142857142855 ]
- Mean = 0.7946428571428572
- Standard deviation = 0.16390678348826623

### balanced_accuracy
- Scores = [ 0.9166666666666667, 0.75, 0.9166666666666667, 0.75, 0.8333333333333333, 0.8333333333333333, 1.0, 0.6666666666666666 ]
- Mean = 0.8333333333333333
- Standard deviation = 0.10206207261596578

### f1
- Scores = [ 0.8, 0.6666666666666666, 0.8, 0.6666666666666666, 0.5, 0.5, 1.0, 0.33333333333333337 ]
- Mean = 0.6583333333333334
- Standard deviation = 0.19773017529507786

### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 38 | 10 |
| Actual Positive | 2 | 10 |

      