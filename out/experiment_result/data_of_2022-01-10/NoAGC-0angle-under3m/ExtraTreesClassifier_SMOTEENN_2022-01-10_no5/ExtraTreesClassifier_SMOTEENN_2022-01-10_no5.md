# ExtraTreesClassifier_SMOTEENN_2022-01-10_no5
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
	- n_estimators = 300
	- estimator_params = ('criterion', 'max_depth', 'min_samples_split', 'min_samples_leaf', 'min_weight_fraction_leaf', 'max_features', 'max_leaf_nodes', 'min_impurity_decrease', 'random_state', 'ccp_alpha')
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
	- ccp_alpha = 0.0
	- n_features_in_ = 36
	- n_outputs_ = 1
	- classes_ = [0 1]
	- n_classes_ = 2
	- base_estimator_ = ExtraTreeClassifier()
	- oob_decision_function_ = [[0.25185185 0.74814815]
 [0.62909091 0.37090909]
 [0.35869565 0.64130435]
 [0.40727273 0.59272727]
 [0.566787   0.433213  ]
 [0.53846154 0.46153846]
 [0.6329588  0.3670412 ]
 [0.6900369  0.3099631 ]
 [0.66539924 0.33460076]
 [0.56140351 0.43859649]
 [0.66785714 0.33214286]
 [0.40989399 0.59010601]
 [0.40808824 0.59191176]
 [0.63003663 0.36996337]
 [0.64444444 0.35555556]
 [0.44404332 0.55595668]
 [0.33453237 0.66546763]
 [0.30882353 0.69117647]
 [0.4379562  0.5620438 ]
 [0.36785714 0.63214286]
 [0.41428571 0.58571429]
 [0.27758007 0.72241993]
 [0.31365314 0.68634686]
 [0.43173432 0.56826568]
 [0.29433962 0.70566038]
 [0.33707865 0.66292135]
 [0.31226766 0.68773234]
 [0.35379061 0.64620939]
 [0.31111111 0.68888889]
 [0.33840304 0.66159696]
 [0.29090909 0.70909091]
 [0.38827839 0.61172161]
 [0.35661765 0.64338235]]
	- oob_score_ = 0.8181818181818182

#### Importance of features
- gp_auc_min = 0.08370044052863436
- gp_max_val_min = 0.06607929515418502
- high_power = 0.05726872246696035
- gp_auc_mean = 0.05286343612334802
- ratio_max_to_10ms_ave_peaks = 0.0473568281938326
- gp_max_val_mean = 0.04405286343612335
- gp_max_ix_max = 0.039647577092511016
- gp_auc_max = 0.039647577092511016
- low_power = 0.03524229074889868
- ratio_max_to_9th_ave_peaks = 0.03524229074889868
- gp_max_ix_range = 0.03524229074889868
- diff_auc = 0.030837004405286344
- tdoa_range = 0.030837004405286344
- coe3[3] = 0.02643171806167401
- srmr = 0.02643171806167401
- gp_max_val_range = 0.02643171806167401
- gp_max_val_max = 0.02643171806167401
- gp_max_ix_std = 0.02643171806167401
- gp_auc_range = 0.02643171806167401
- coe1[1] = 0.022026431718061675
- diff_std = 0.022026431718061675
- gp_max_val_std = 0.022026431718061675
- tdoa_std = 0.022026431718061675
- tdoa_max = 0.022026431718061675
- tdoa_mean = 0.022026431718061675
- coe3[2] = 0.018722466960352423
- hlbr = 0.01762114537444934
- ac_std = 0.01762114537444934
- gp_auc_std = 0.01762114537444934
- tdoa_min = 0.013215859030837005
- gp_max_ix_min = 0.00881057268722467
- gp_max_ix_mean = 0.00881057268722467
- coe1[0] = 0.004405286343612335
- ac_auc = 0.004405286343612335
- coe3[0] = 0.0
- coe3[1] = 0.0

## Evaluation
cv = 8
### accuracy
- Scores = [ 0.5789473684210527, 0.631578947368421, 0.8421052631578947, 0.631578947368421, 0.8947368421052632, 0.6842105263157895, 0.7777777777777778, 0.6666666666666666 ]
- Mean = 0.7134502923976608
- Standard deviation = 0.10493776868377988

### balanced_accuracy
- Scores = [ 0.7333333333333334, 0.675, 0.9, 0.675, 0.75, 0.43333333333333335, 0.8666666666666667, 0.4 ]
- Mean = 0.6791666666666667
- Standard deviation = 0.1696606089291861

### f1
- Scores = [ 0.5, 0.46153846153846156, 0.7272727272727273, 0.46153846153846156, 0.6666666666666666, 0.0, 0.6, 0.0 ]
- Mean = 0.42712703962703963
- Standard deviation = 0.2621796863301164

### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 87 | 33 |
| Actual Positive | 7 | 23 |

      