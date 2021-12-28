# ExtraTreesClassifier_ClusterCentroids_2021-12-28_no1
## Constants
- CSV_PATH = ../out/csv/experiment
- OUTPUT_PATH = ../out/experiment_result/2021-12-27-under3m
- FEATURE_ATTRBS = ['low_power', 'high_power', 'hlbr', 'coe1[0]', 'coe1[1]', 'coe3[0]', 'coe3[1]', 'coe3[2]', 'coe3[3]', 'ratio_max_to_10ms_ave_peaks', 'ratio_max_to_9th_ave_peaks', 'ac_std', 'ac_auc', 'diff_std', 'diff_auc', 'srmr', 'gp_max_val_std', 'gp_max_val_range', 'gp_max_val_min', 'gp_max_val_max', 'gp_max_val_mean', 'gp_max_ix_std', 'gp_max_ix_range', 'gp_max_ix_min', 'gp_max_ix_max', 'gp_max_ix_mean', 'gp_auc_std', 'gp_auc_range', 'gp_auc_min', 'gp_auc_max', 'gp_auc_mean', 'tdoa_std', 'tdoa_range', 'tdoa_min', 'tdoa_max', 'tdoa_mean']
- LABEL_ATTRB = ['facing']
- FACING_DOV_ANGLES = [1]
- NCV = 8
- SCORING = ['accuracy', 'balanced_accuracy', 'f1']
- REFIT_SCORING = balanced_accuracy
- PARAM_GRID = [{'est__n_estimators': [50, 100, 150, 200, 300], 'est__min_samples_split': [2, 5, 10], 'est__min_samples_leaf': [1, 5, 10], 'est__max_features': ['sqrt', 'log2', None], 'est__bootstrap': [False], 'est__n_jobs': [-1], 'est__random_state': [42], 'est__max_samples': [0.01, 0.5, 0.09]}, {'est__n_estimators': [50, 100, 150, 200, 300], 'est__min_samples_split': [2, 5, 10], 'est__min_samples_leaf': [1, 5, 10], 'est__max_features': ['sqrt', 'log2', None], 'est__bootstrap': [True], 'est__oob_score': [True, False], 'est__n_jobs': [-1], 'est__random_state': [42], 'est__max_samples': [0.01, 0.5, 0.09]}]
- TRAIN_SET_SESSION = ['trial1', 'trial2']
- TEST_SET_SESSION = ['trial3', 'trial4', 'trial5']

## Loaded CSV
- 2021-12-27_raspi_48000Hz_w1_N2^12_overlap80_withfacing.csv

## Estimator
### Type
- resampler = ClusterCentroids
- estimator = ExtraTreesClassifier

### Arguments for hyperparameter search
- resampler = ClusterCentroids
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
	- estimator = None
	- voting = auto
	- n_jobs = deprecated
	- n_features_in_ = 36
	- sampling_strategy_ = OrderedDict([(0, 20)])
	- estimator_ = KMeans(n_clusters=20, random_state=42)
	- voting_ = soft

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
	- max_samples = 0.5
	- criterion = gini
	- max_depth = None
	- min_samples_split = 10
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
	- oob_decision_function_ = [[0.92271955 0.07728045]
 [0.94086303 0.05913697]
 [0.90076641 0.09923359]
 [0.76806733 0.23193267]
 [0.92482361 0.07517639]
 [0.42001306 0.57998694]
 [0.91655479 0.08344521]
 [0.96003045 0.03996955]
 [0.81752012 0.18247988]
 [0.90029829 0.09970171]
 [0.90968838 0.09031162]
 [0.17345637 0.82654363]
 [0.1602906  0.8397094 ]
 [0.93076894 0.06923106]
 [0.67776002 0.32223998]
 [0.84918033 0.15081967]
 [0.43695374 0.56304626]
 [0.83957104 0.16042896]
 [0.92963263 0.07036737]
 [0.93191899 0.06808101]
 [0.15213236 0.84786764]
 [0.1544285  0.8455715 ]
 [0.2888879  0.7111121 ]
 [0.3378487  0.6621513 ]
 [0.15350273 0.84649727]
 [0.13841078 0.86158922]
 [0.15641665 0.84358335]
 [0.11475492 0.88524508]
 [0.12402936 0.87597064]
 [0.12367725 0.87632275]
 [0.15129002 0.84870998]
 [0.35317222 0.64682778]
 [0.06498202 0.93501798]
 [0.07567587 0.92432413]
 [0.23950575 0.76049425]
 [0.14764599 0.85235401]
 [0.52640498 0.47359502]
 [0.08576909 0.91423091]
 [0.3679831  0.6320169 ]
 [0.24632129 0.75367871]]
	- oob_score_ = 0.875

#### Importance of features
- gp_max_val_mean = 0.16289148936168252
- gp_auc_min = 0.15830888752135452
- gp_auc_mean = 0.13376325625463414
- gp_max_val_min = 0.11665558503485576
- gp_auc_max = 0.11178427744162761
- gp_max_val_max = 0.11010971363077206
- srmr = 0.05074611816629414
- diff_auc = 0.03262236624746464
- tdoa_range = 0.021134538991681846
- diff_std = 0.017777777777777778
- tdoa_mean = 0.014444444444444444
- coe1[0] = 0.012507122507122506
- ratio_max_to_9th_ave_peaks = 0.008552036199095024
- coe1[1] = 0.007626592729891025
- coe3[3] = 0.007480938467532478
- low_power = 0.007007697986144526
- gp_max_ix_min = 0.005806451612903227
- high_power = 0.004591466289486093
- gp_max_ix_max = 0.004480519480519482
- gp_max_val_range = 0.00358974358974359
- ac_std = 0.002288106630211894
- ac_auc = 0.0019230769230769223
- gp_auc_range = 0.0019230769230769223
- coe3[2] = 0.001058201058201059
- hlbr = 0.0005836575875486384
- gp_max_val_std = 0.000342857142857144
- coe3[0] = 0.0
- coe3[1] = 0.0
- ratio_max_to_10ms_ave_peaks = 0.0
- gp_max_ix_std = 0.0
- gp_max_ix_range = 0.0
- gp_max_ix_mean = 0.0
- gp_auc_std = 0.0
- tdoa_std = 0.0
- tdoa_min = 0.0
- tdoa_max = 0.0

## Evaluation
cv = 8
### accuracy
- Scores = [ 0.5263157894736842, 0.6842105263157895, 0.7894736842105263, 0.6842105263157895, 0.8947368421052632, 0.5, 0.8333333333333334, 0.6666666666666666 ]
- Mean = 0.6973684210526316
- Standard deviation = 0.13010874538764322

### balanced_accuracy
- Scores = [ 0.7, 0.8, 0.8666666666666667, 0.8, 0.9333333333333333, 0.5892857142857143, 0.9, 0.4 ]
- Mean = 0.7486607142857143
- Standard deviation = 0.1679050901421244

### f1
- Scores = [ 0.47058823529411764, 0.5714285714285715, 0.6666666666666666, 0.5714285714285715, 0.8, 0.39999999999999997, 0.6666666666666666, 0.0 ]
- Mean = 0.5183473389355742
- Standard deviation = 0.22746749501939506

### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 78 | 41 |
| Actual Positive | 4 | 26 |

      