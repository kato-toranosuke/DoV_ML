# ExtraTreesClassifier_SMOTEENN_2021-12-29_no5
## Constants
- CSV_PATH = ../out/csv/experiment
- OUTPUT_PATH = ../out/experiment_result/data_of_2021-12-27/NoAGC-45angle-under3m
- FEATURE_ATTRBS = ['low_power', 'high_power', 'hlbr', 'coe1[0]', 'coe1[1]', 'coe3[0]', 'coe3[1]', 'coe3[2]', 'coe3[3]', 'ratio_max_to_10ms_ave_peaks', 'ratio_max_to_9th_ave_peaks', 'ac_std', 'ac_auc', 'diff_std', 'diff_auc', 'srmr', 'gp_max_val_std', 'gp_max_val_range', 'gp_max_val_min', 'gp_max_val_max', 'gp_max_val_mean', 'gp_max_ix_std', 'gp_max_ix_range', 'gp_max_ix_min', 'gp_max_ix_max', 'gp_max_ix_mean', 'gp_auc_std', 'gp_auc_range', 'gp_auc_min', 'gp_auc_max', 'gp_auc_mean', 'tdoa_std', 'tdoa_range', 'tdoa_min', 'tdoa_max', 'tdoa_mean']
- LABEL_ATTRB = ['facing2']
- FACING_DOV_ANGLES = [1, 2]
- NCV = 8
- SCORING = ['accuracy', 'balanced_accuracy', 'f1']
- REFIT_SCORING = balanced_accuracy
- PARAM_GRID = [{'est__n_estimators': [50, 100, 150, 200, 300], 'est__min_samples_split': [2, 5, 10], 'est__min_samples_leaf': [1, 5, 10], 'est__max_features': ['sqrt', 'log2', None], 'est__bootstrap': [False], 'est__n_jobs': [-1], 'est__random_state': [42], 'est__max_samples': [0.01, 0.5, 0.09]}, {'est__n_estimators': [50, 100, 150, 200, 300], 'est__min_samples_split': [2, 5, 10], 'est__min_samples_leaf': [1, 5, 10], 'est__max_features': ['sqrt', 'log2', None], 'est__bootstrap': [True], 'est__oob_score': [True, False], 'est__n_jobs': [-1], 'est__random_state': [42], 'est__max_samples': [0.01, 0.5, 0.09]}]
- TRAIN_SET_SESSION = ['trial1', 'trial2']
- TEST_SET_SESSION = ['trial3', 'trial4', 'trial5']
- DISTANCE = [1, 3]
- AGC_STATUS = ['NoAGC']

## Loaded CSV
- 2021-12-27_raspi_48000Hz_w1_N2^12_overlap80_new.csv

## Estimator
### Type
- resampler = SMOTEENN
- estimator = ExtraTreesClassifier

### Arguments for hyperparameter search
- resampler = SMOTEENN
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
	- smote = None
	- enn = None
	- n_jobs = -1
	- n_features_in_ = 36
	- sampling_strategy_ = auto
	- smote_ = SMOTE(n_jobs=-1, random_state=42)
	- enn_ = EditedNearestNeighbours(n_jobs=-1, sampling_strategy='all')

- best_estimator
	- base_estimator = ExtraTreeClassifier()
	- n_estimators = 150
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

#### Importance of features
- coe1[0] = 0.08557823129251703
- low_power = 0.08261904761904763
- ac_std = 0.0771957671957672
- gp_auc_min = 0.07068405139833708
- gp_max_val_min = 0.06449735449735448
- srmr = 0.06179894179894179
- gp_auc_mean = 0.05923280423280422
- ac_auc = 0.055555555555555546
- gp_max_val_mean = 0.05454648526077096
- coe1[1] = 0.053412698412698405
- coe3[3] = 0.0524829931972789
- diff_auc = 0.0469047619047619
- gp_max_val_max = 0.0416931216931217
- high_power = 0.029126984126984123
- diff_std = 0.022910052910052908
- gp_auc_max = 0.020956160241874525
- hlbr = 0.020714285714285716
- gp_auc_std = 0.02050642479213908
- ratio_max_to_10ms_ave_peaks = 0.01507936507936508
- gp_max_val_range = 0.014712773998488284
- gp_auc_range = 0.00962962962962963
- gp_max_val_std = 0.008892668178382464
- tdoa_mean = 0.007936507936507934
- ratio_max_to_9th_ave_peaks = 0.005555555555555556
- gp_max_ix_max = 0.004285714285714285
- coe3[2] = 0.004232804232804232
- gp_max_ix_mean = 0.0031746031746031746
- tdoa_range = 0.002380952380952381
- gp_max_ix_range = 0.0015873015873015873
- gp_max_ix_min = 0.0015873015873015873
- gp_max_ix_std = 0.0002645502645502647
- tdoa_std = 0.0002645502645502647
- coe3[0] = 0.0
- coe3[1] = 0.0
- tdoa_min = 0.0
- tdoa_max = 0.0

## Evaluation
cv = 8
### accuracy
- Scores = [ 0.7333333333333333, 1.0, 0.9333333333333333, 0.6666666666666666, 1.0, 0.9333333333333333, 1.0, 0.8571428571428571 ]
- Mean = 0.8904761904761904
- Standard deviation = 0.12018504251546633

### balanced_accuracy
- Scores = [ 0.6666666666666666, 1.0, 0.9375, 0.6875, 1.0, 0.9375, 1.0, 0.8333333333333333 ]
- Mean = 0.8828125
- Standard deviation = 0.12966030504692297

### f1
- Scores = [ 0.8181818181818181, 1.0, 0.9333333333333333, 0.5454545454545454, 1.0, 0.9333333333333333, 1.0, 0.888888888888889 ]
- Mean = 0.8898989898989899
- Standard deviation = 0.14314596134135957

### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 48 | 6 |
| Actual Positive | 7 | 58 |

      