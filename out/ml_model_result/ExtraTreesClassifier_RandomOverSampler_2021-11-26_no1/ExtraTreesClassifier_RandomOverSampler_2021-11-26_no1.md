# ExtraTreesClassifier_RandomOverSampler_2021-11-26_no1
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
- features_python.csv

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
	- n_estimators = 100
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
	- oob_decision_function_ = [[0.03370787 0.96629213]
 [0.13829787 0.86170213]
 [0.35869565 0.64130435]
 ...
 [0.14444444 0.85555556]
 [0.06976744 0.93023256]
 [0.23655914 0.76344086]]
	- oob_score_ = 0.8968253968253969

#### Importance of features
- gp_max_val_max = 0.09595032016885137
- gp_auc_mean = 0.08840094507166688
- gp_auc_max = 0.08579168701994755
- gp_max_val_mean = 0.07664121013361722
- gp_auc_min = 0.0342227267281223
- gp_max_val_min = 0.03357032241572061
- ratio_max_to_10ms_ave_peaks = 0.030152494575446956
- gp_max_val_std = 0.027747667823614854
- srmr = 0.027655780115620043
- gp_auc_range = 0.026945818515191528
- gp_max_val_range = 0.026678452146644265
- tdoa_mean = 0.026445974783664127
- gp_auc_std = 0.025577111537337063
- ratio_max_to_9th_ave_peaks = 0.024411585643126604
- gp_max_ix_min = 0.02437671423949946
- gp_max_ix_mean = 0.024242825963898332
- ac_auc = 0.0241404309778956
- diff_auc = 0.022924350589838074
- hlbr = 0.021917138791101354
- tdoa_min = 0.021258101032812938
- diff_std = 0.02057668683757107
- ac_std = 0.020282748906594896
- high_power = 0.020230990275329413
- gp_max_ix_std = 0.018842970078045463
- tdoa_std = 0.018436159847153754
- coe3[2] = 0.017683199733698574
- coe1[1] = 0.01641482413124446
- coe3[3] = 0.016203763129578
- coe1[0] = 0.01483127257478209
- tdoa_max = 0.014824357001986302
- low_power = 0.014379613034433608
- gp_max_ix_max = 0.014340640906467118
- tdoa_range = 0.012302746832858492
- gp_max_ix_range = 0.01159836843663973
- coe3[0] = 0.0
- coe3[1] = 0.0

## Evaluation
cv = 10
### accuracy
- Scores = [ 0.875, 0.8975694444444444, 0.9027777777777778, 0.890625, 0.8940972222222222, 0.8836805555555556, 0.8940972222222222, 0.8854166666666666, 0.8871527777777778, 0.8784722222222222 ]
- Mean = 0.888888888888889
- Standard deviation = 0.008180013187076212

### balanced_accuracy
- Scores = [ 0.6726190476190477, 0.6378968253968254, 0.6170634920634921, 0.5625, 0.6001984126984127, 0.5466269841269842, 0.6478174603174602, 0.5416666666666666, 0.566468253968254, 0.5138888888888888 ]
- Mean = 0.5906746031746032
- Standard deviation = 0.049613490990699324

### f1
- Scores = [ 0.4461538461538462, 0.4158415841584159, 0.37777777777777777, 0.2222222222222222, 0.32967032967032966, 0.17283950617283952, 0.4299065420560747, 0.15384615384615385, 0.23529411764705882, 0.05405405405405406 ]
- Mean = 0.28376061337587727
- Standard deviation = 0.12814243778884335

### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 4981 | 59 |
| Actual Positive | 581 | 139 |

      