# ExtraTreesClassifier_ClusterCentroids_2021-11-01_no2
## Constants
- CSV_PATH = ../../out/csv/
- OUTPUT_PATH = ./result/
- FEATURE_ATTRBS = ['low_power', 'high_power', 'hlbr', 'coe1[0]', 'coe1[1]', 'coe3[0]', 'coe3[1]', 'coe3[2]', 'coe3[3]', 'ratio_max_to_10ms_ave_peaks', 'ratio_max_to_9th_ave_peaks', 'ac_std', 'ac_auc', 'diff_std', 'diff_auc', 'srmr', 'gp_max_val_std', 'gp_max_val_range', 'gp_max_val_min', 'gp_max_val_max', 'gp_max_val_mean', 'gp_max_ix_std', 'gp_max_ix_range', 'gp_max_ix_min', 'gp_max_ix_max', 'gp_max_ix_mean', 'gp_auc_std', 'gp_auc_range', 'gp_auc_min', 'gp_auc_max', 'gp_auc_mean', 'tdoa_std', 'tdoa_range', 'tdoa_min', 'tdoa_max', 'tdoa_mean']
- LABEL_ATTRB = ['dov_angle']
- FACING_DOV_ANGLES = [0, 45, 315]
- NCV = 10
- SCORING = ['accuracy', 'balanced_accuracy', 'f1']
- REFIT_SCORING = balanced_accuracy
- PARAM_GRID = [{'est__n_estimators': [10], 'est__min_samples_split': [2], 'est__min_samples_leaf': [5], 'est__max_features': [None], 'est__bootstrap': [False], 'est__n_jobs': [-1], 'est__random_state': [42], 'est__max_samples': [0.5]}]

## Loaded CSV
- features_mono_ch_matlab.csv

## Estimator
### Type
- resampler = ClusterCentroids
- estimator = ExtraTreesClassifier

### Arguments for hyperparameter search
- resampler = ClusterCentroids
- estimator = ExtraTreesClassifier
- param_grid = 
	- {'est__n_estimators': [10], 'est__min_samples_split': [2], 'est__min_samples_leaf': [5], 'est__max_features': [None], 'est__bootstrap': [False], 'est__n_jobs': [-1], 'est__random_state': [42], 'est__max_samples': [0.5]}

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
	- base_estimator = ExtraTreeClassifier()
	- n_estimators = 10
	- estimator_params = ('criterion', 'max_depth', 'min_samples_split', 'min_samples_leaf', 'min_weight_fraction_leaf', 'max_features', 'max_leaf_nodes', 'min_impurity_decrease', 'min_impurity_split', 'random_state', 'ccp_alpha')
	- bootstrap = False
	- oob_score = False
	- n_jobs = -1
	- random_state = 42
	- verbose = 0
	- warm_start = False
	- class_weight = None
	- max_samples = 0.5
	- criterion = gini
	- max_depth = None
	- min_samples_split = 2
	- min_samples_leaf = 5
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

#### Importance of features
- gp_max_val_max = 0.18165250135303204
- gp_max_val_mean = 0.16654004905238765
- gp_max_val_min = 0.09740084816565854
- gp_max_val_range = 0.05015156423943301
- gp_max_val_std = 0.04738250300234116
- gp_auc_min = 0.042888514437764244
- gp_auc_mean = 0.04165073054144634
- tdoa_range = 0.029790863933956573
- high_power = 0.0266437616693651
- gp_max_ix_std = 0.0259273239756243
- gp_max_ix_min = 0.025832692601247133
- gp_max_ix_range = 0.02545880808246568
- tdoa_std = 0.024270823920589518
- tdoa_min = 0.022710664549847246
- gp_max_ix_mean = 0.022365181208119016
- tdoa_mean = 0.022016534178351935
- gp_auc_max = 0.021708283997776474
- gp_max_ix_max = 0.01699517521740293
- tdoa_max = 0.012829248742945557
- gp_auc_range = 0.009801637551496305
- gp_auc_std = 0.009744899871479121
- diff_std = 0.008344305086688712
- diff_auc = 0.008164531576489078
- ratio_max_to_9th_ave_peaks = 0.006946169551196084
- srmr = 0.006711607941390414
- coe3[3] = 0.006195329389760152
- ratio_max_to_10ms_ave_peaks = 0.006022944636854212
- low_power = 0.005587265645562711
- coe1[1] = 0.005509545115419349
- ac_std = 0.005259061737751563
- coe3[2] = 0.004894092679119716
- ac_auc = 0.004256603687598213
- coe1[0] = 0.00420988719609505
- hlbr = 0.004136045463344902
- coe3[0] = 0.0
- coe3[1] = 0.0

## Evaluation
cv = 10
### accuracy
- Scores = [ 0.7899305555555556, 0.8854166666666666, 0.8715277777777778, 0.8802083333333334, 0.8611111111111112, 0.8003472222222222, 0.8506944444444444, 0.828125, 0.8767361111111112, 0.7638888888888888 ]
- Mean = 0.8407986111111111
- Standard deviation = 0.04073058750008221

### balanced_accuracy
- Scores = [ 0.8208333333333333, 0.8861111111111111, 0.8703703703703703, 0.850462962962963, 0.8425925925925926, 0.7513888888888889, 0.862037037037037, 0.7893518518518519, 0.8569444444444445, 0.6925925925925925 ]
- Mean = 0.8222685185185185
- Standard deviation = 0.05771217265979384

### f1
- Scores = [ 0.771266540642722, 0.8533333333333333, 0.8348214285714284, 0.8207792207792208, 0.8058252427184466, 0.676056338028169, 0.8200836820083681, 0.7345844504021447, 0.8255528255528256, 0.5641025641025641 ]
- Mean = 0.7706405626139221
- Standard deviation = 0.08548313211587087

### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 3227 | 373 |
| Actual Positive | 544 | 1616 |

      