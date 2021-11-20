# ExtraTreesClassifier_SMOTE_2021-11-01_no5
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
- resampler = SMOTE
- estimator = ExtraTreesClassifier

### Arguments for hyperparameter search
- resampler = SMOTE
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
	- k_neighbors = 5
	- n_jobs = -1
	- n_features_in_ = 36
	- sampling_strategy_ = OrderedDict([(1, 1440)])
	- nn_k_ = NearestNeighbors(n_neighbors=6)

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
- gp_max_val_mean = 0.21774695069295258
- gp_max_val_max = 0.20507295512661183
- gp_max_val_min = 0.0830067298787059
- gp_auc_min = 0.050335883477982485
- high_power = 0.0490967748932823
- gp_max_val_range = 0.0406925125689788
- gp_max_val_std = 0.03534388669659185
- gp_max_ix_min = 0.024297290229936905
- gp_auc_mean = 0.021958256413058645
- gp_max_ix_mean = 0.01817735069681312
- gp_auc_max = 0.016679679708299994
- tdoa_min = 0.016415583883169976
- diff_auc = 0.016072548534282003
- ac_auc = 0.015516020146547814
- tdoa_mean = 0.015357267563983736
- gp_auc_std = 0.01418613913409511
- gp_max_ix_max = 0.01340027486136158
- tdoa_std = 0.012659537657577621
- gp_auc_range = 0.012196162800282188
- gp_max_ix_std = 0.012078587648918974
- tdoa_max = 0.011017566122628332
- diff_std = 0.009365854733309507
- tdoa_range = 0.009332651107226876
- ratio_max_to_9th_ave_peaks = 0.008951376974672383
- gp_max_ix_range = 0.008373148561029662
- coe1[0] = 0.008372249571722635
- ratio_max_to_10ms_ave_peaks = 0.007994982511662875
- srmr = 0.007877167223479961
- coe1[1] = 0.007378984534333967
- ac_std = 0.00728568184380631
- hlbr = 0.006896594440257645
- coe3[3] = 0.0061160869043388215
- coe3[2] = 0.005472973741717234
- low_power = 0.005274289116380161
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

      