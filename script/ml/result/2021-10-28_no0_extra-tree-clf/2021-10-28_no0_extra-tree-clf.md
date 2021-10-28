# 2021-10-28_no0_extra-tree-clf
## Constants
- CSV_PATH = ../../out/csv/
- OUTPUT_PATH = ./result/
- FEATURE_ATTRBS = ['low_power', 'high_power', 'hlbr', 'coe1[0]', 'coe1[1]', 'coe3[0]', 'coe3[1]', 'coe3[2]', 'coe3[3]', 'ratio_max_to_10ms_ave_peaks', 'ratio_max_to_9th_ave_peaks', 'ac_std', 'ac_auc', 'diff_std', 'diff_auc', 'srmr', 'gp_max_val_std', 'gp_max_val_range', 'gp_max_val_min', 'gp_max_val_max', 'gp_max_val_mean', 'gp_max_ix_std', 'gp_max_ix_range', 'gp_max_ix_min', 'gp_max_ix_max', 'gp_max_ix_mean', 'gp_auc_std', 'gp_auc_range', 'gp_auc_min', 'gp_auc_max', 'gp_auc_mean', 'tdoa_std', 'tdoa_range', 'tdoa_min', 'tdoa_max', 'tdoa_mean']
- LABEL_ATTRB = ['dov_angle']
- FACING_DOV_ANGLES = [0, 45, 315]
- NCV = 10
- SCORING = ['accuracy', 'balanced_accuracy', 'f1']
- REFIT_SCORING = balanced_accuracy
- PARAM_GRID = [{'n_estimators': [10], 'min_samples_split': [2], 'min_samples_leaf': [5], 'max_features': [None], 'bootstrap': [False], 'n_jobs': [-1], 'random_state': [42], 'max_samples': [0.5]}]

## Loaded CSV
- fearures_mono_ch_complete_211007.csv

## Estimator
### Type
ExtraTreesClassifier
### Arguments for hyperparameter search
- estimator = ExtraTreesClassifier
- param_grid = 
	- {'n_estimators': [10], 'min_samples_split': [2], 'min_samples_leaf': [5], 'max_features': [None], 'bootstrap': [False], 'n_jobs': [-1], 'random_state': [42], 'max_samples': [0.5]}

- scoring = ['accuracy', 'balanced_accuracy', 'f1']
- refit = balanced_accuracy
- cv = 10

### Parameters of the best estimator
#### The best hyper-parameters
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
- estimators_ = [ExtraTreeClassifier(max_features=None, min_samples_leaf=5,
                    random_state=1608637542), ExtraTreeClassifier(max_features=None, min_samples_leaf=5,
                    random_state=1273642419), ExtraTreeClassifier(max_features=None, min_samples_leaf=5,
                    random_state=1935803228), ExtraTreeClassifier(max_features=None, min_samples_leaf=5,
                    random_state=787846414), ExtraTreeClassifier(max_features=None, min_samples_leaf=5,
                    random_state=996406378), ExtraTreeClassifier(max_features=None, min_samples_leaf=5,
                    random_state=1201263687), ExtraTreeClassifier(max_features=None, min_samples_leaf=5,
                    random_state=423734972), ExtraTreeClassifier(max_features=None, min_samples_leaf=5,
                    random_state=415968276), ExtraTreeClassifier(max_features=None, min_samples_leaf=5,
                    random_state=670094950), ExtraTreeClassifier(max_features=None, min_samples_leaf=5,
                    random_state=1914837113)]

#### Importance of features
- high_power = 0.16054591945518026
- diff_std = 0.1544123883534813
- hlbr = 0.094466471580454
- diff_auc = 0.06991451431884008
- srmr = 0.04334347839668752
- coe1[1] = 0.04144773282016976
- coe1[0] = 0.03570185457401731
- ac_auc = 0.027006805517937625
- gp_auc_max = 0.02648309034749241
- coe3[3] = 0.026413032759559318
- gp_max_val_mean = 0.023999624715158117
- coe3[2] = 0.02264709285304872
- low_power = 0.019940151871501312
- ratio_max_to_10ms_ave_peaks = 0.019565034637140297
- gp_auc_std = 0.019050401149591854
- gp_max_val_max = 0.01820756521598376
- ratio_max_to_9th_ave_peaks = 0.018204867732130113
- gp_auc_min = 0.016490738354835267
- gp_max_val_std = 0.016380211187951313
- gp_auc_mean = 0.016242079244455566
- gp_max_val_min = 0.016188220486631856
- gp_max_val_range = 0.015330202484472139
- ac_std = 0.01512506717508883
- gp_auc_range = 0.014512044407477928
- tdoa_max = 0.0092535279515857
- gp_max_ix_mean = 0.007865125076328555
- gp_max_ix_range = 0.007862590171146358
- gp_max_ix_max = 0.007476437460060638
- tdoa_min = 0.007437615491879397
- tdoa_range = 0.006443628995461756
- tdoa_std = 0.005894566355662733
- gp_max_ix_min = 0.005689270128194678
- gp_max_ix_std = 0.005235799394331776
- tdoa_mean = 0.005222849336061724
- coe3[0] = 0.0
- coe3[1] = 0.0

## Evaluation
### accuracy
- Scores = [0.59375    0.71180556 0.76736111 0.72395833 0.76041667 0.69618056
 0.71701389 0.73263889 0.72916667 0.68402778]
- Mean = 0.7116319444444444
- Standard deviation = 0.046165215183928195

### balanced_accuracy
- Scores = [0.65833333 0.71759259 0.72222222 0.64305556 0.71018519 0.63472222
 0.71712963 0.66759259 0.69722222 0.58703704]
- Mean = 0.6755092592592592
- Standard deviation = 0.04273298621001394

### f1
- Scores = [0.62857143 0.65843621 0.63586957 0.46464646 0.61452514 0.48979592
 0.65539112 0.53333333 0.6119403  0.32089552]
- Mean = 0.561340500519546
- Standard deviation = 0.10334562109488096

### Confusion Matrix
[[2952  648]
 [1013 1147]]
