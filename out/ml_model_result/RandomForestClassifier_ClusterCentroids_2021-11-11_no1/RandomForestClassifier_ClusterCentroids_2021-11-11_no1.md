# RandomForestClassifier_ClusterCentroids_2021-11-11_no1
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
- resampler = ClusterCentroids
- estimator = RandomForestClassifier

### Arguments for hyperparameter search
- resampler = ClusterCentroids
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
	- estimator = None
	- voting = auto
	- n_jobs = deprecated
	- n_features_in_ = 36
	- sampling_strategy_ = OrderedDict([(0, 2160)])
	- estimator_ = KMeans(n_clusters=2160, random_state=42)
	- voting_ = soft

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
	- base_estimator_ = DecisionTreeClassifier()

#### Importance of features
- gp_max_val_max = 0.12489854790976208
- gp_max_val_mean = 0.11787155459838411
- gp_max_val_range = 0.07131524604057299
- gp_max_val_min = 0.062136828942245245
- gp_max_val_std = 0.04812876437828438
- high_power = 0.04734766940847764
- gp_max_ix_std = 0.03372388539163845
- tdoa_std = 0.03265806757813755
- hlbr = 0.029996224858621304
- gp_auc_max = 0.029201918542426934
- diff_std = 0.028631724056948197
- gp_max_ix_mean = 0.027906955631420125
- tdoa_mean = 0.027256807328521454
- gp_auc_min = 0.023512726190004177
- gp_auc_mean = 0.02036099156142611
- gp_max_ix_range = 0.020157775521268566
- srmr = 0.020060229951496762
- tdoa_range = 0.019892114860643635
- diff_auc = 0.017160193653280587
- ac_auc = 0.016847971571047116
- ratio_max_to_9th_ave_peaks = 0.01668381842206936
- ratio_max_to_10ms_ave_peaks = 0.016679794124916197
- coe1[1] = 0.015551518986977009
- gp_max_ix_min = 0.01504738855413478
- ac_std = 0.014869135227980923
- tdoa_min = 0.014832103671521024
- low_power = 0.014324230397366343
- gp_auc_range = 0.014298296221424402
- coe3[3] = 0.013811228536245713
- gp_max_ix_max = 0.011765631207304762
- tdoa_max = 0.01144321295898622
- coe3[2] = 0.01068830193010687
- gp_auc_std = 0.008552867802194832
- coe1[0] = 0.0023862739841641915
- coe3[0] = 0.0
- coe3[1] = 0.0

## Evaluation
cv = 10
### accuracy
- Scores = [ 0.7586805555555556, 0.9079861111111112, 0.8871527777777778, 0.8645833333333334, 0.8767361111111112, 0.8159722222222222, 0.8506944444444444, 0.8246527777777778, 0.8940972222222222, 0.7690972222222222 ]
- Mean = 0.8449652777777779
- Standard deviation = 0.04903737954844646

### balanced_accuracy
- Scores = [ 0.8004629629629629, 0.9060185185185186, 0.8819444444444444, 0.8305555555555555, 0.8578703703703704, 0.7675925925925926, 0.8638888888888889, 0.7856481481481481, 0.8782407407407407, 0.7013888888888888 ]
- Mean = 0.827361111111111
- Standard deviation = 0.05994590968929713

### f1
- Scores = [ 0.7504488330341115, 0.8798185941043084, 0.851258581235698, 0.7936507936507936, 0.8264058679706602, 0.7005649717514124, 0.8215767634854771, 0.7292225201072386, 0.8523002421307505, 0.5830721003134797 ]
- Mean = 0.7788319267783931
- Standard deviation = 0.08536148986678826

### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 3232 | 368 |
| Actual Positive | 525 | 1635 |

      