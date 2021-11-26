# ExtraTreesClassifier_ClusterCentroids_2021-11-24_no1
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
- resampler = ClusterCentroids
- estimator = ExtraTreesClassifier

### Arguments for hyperparameter search
- resampler = ClusterCentroids
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
	- estimator = None
	- voting = auto
	- n_jobs = deprecated
	- n_features_in_ = 36
	- sampling_strategy_ = OrderedDict([(0, 720)])
	- estimator_ = KMeans(n_clusters=720, random_state=42)
	- voting_ = soft

- best_estimator
	- base_estimator = ExtraTreeClassifier()
	- n_estimators = 200
	- estimator_params = ('criterion', 'max_depth', 'min_samples_split', 'min_samples_leaf', 'min_weight_fraction_leaf', 'max_features', 'max_leaf_nodes', 'min_impurity_decrease', 'min_impurity_split', 'random_state', 'ccp_alpha')
	- bootstrap = True
	- oob_score = True
	- n_jobs = -1
	- random_state = 42
	- verbose = 0
	- warm_start = False
	- class_weight = None
	- max_samples = 0.01
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
	- oob_decision_function_ = [[0.74676871 0.25323129]
 [0.61886217 0.38113783]
 [0.68195142 0.31804858]
 ...
 [0.65758555 0.34241445]
 [0.56731076 0.43268924]
 [0.55032937 0.44967063]]
	- oob_score_ = 0.8319444444444445

#### Importance of features
- gp_max_val_mean = 0.0822192334949391
- gp_auc_std = 0.050671388200513034
- gp_max_ix_range = 0.04800034251968931
- gp_max_ix_std = 0.04678508409225868
- gp_max_ix_mean = 0.04623717115455325
- gp_auc_mean = 0.044285706228035134
- gp_max_val_max = 0.043783021160485255
- gp_auc_max = 0.04368022755753439
- gp_max_val_range = 0.043331667412155335
- tdoa_mean = 0.0399328976323117
- gp_max_val_std = 0.03803551836255186
- gp_auc_min = 0.03791394890030702
- gp_auc_range = 0.03542931488801055
- gp_max_ix_max = 0.034045184766923905
- tdoa_range = 0.032229546539323035
- tdoa_min = 0.03129468259367155
- tdoa_max = 0.030998605500779427
- gp_max_ix_min = 0.030929299414626375
- tdoa_std = 0.026400000000000014
- gp_max_val_min = 0.026215192647435645
- srmr = 0.023616657500595804
- coe3[3] = 0.018924104179293084
- diff_std = 0.016534591828522807
- ratio_max_to_10ms_ave_peaks = 0.016361108751062024
- ratio_max_to_9th_ave_peaks = 0.014123241700827918
- coe1[0] = 0.013938492063492063
- ac_auc = 0.013890034030140986
- coe3[2] = 0.01265745290745291
- coe1[1] = 0.01259792239753596
- ac_std = 0.011938305045338297
- low_power = 0.009713040874565376
- diff_auc = 0.00849559922835785
- hlbr = 0.0080445632798574
- high_power = 0.006746853146853155
- coe3[0] = 0.0
- coe3[1] = 0.0

## Evaluation
cv = 10
### accuracy
- Scores = [ 0.8767361111111112, 0.8802083333333334, 0.8767361111111112, 0.875, 0.875, 0.8767361111111112, 0.875, 0.875, 0.8784722222222222, 0.875 ]
- Mean = 0.8763888888888889
- Standard deviation = 0.0017010345435994393

### balanced_accuracy
- Scores = [ 0.5248015873015873, 0.5208333333333334, 0.5069444444444444, 0.5, 0.5, 0.5069444444444444, 0.5, 0.5, 0.5138888888888888, 0.5 ]
- Mean = 0.5073412698412699
- Standard deviation = 0.008941789158129966

### f1
- Scores = [ 0.10126582278481013, 0.07999999999999999, 0.0273972602739726, 0.0, 0.0, 0.0273972602739726, 0.0, 0.0, 0.05405405405405406, 0.0 ]
- Mean = 0.02901143973868094
- Standard deviation = 0.03558256737208771

### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 5037 | 3 |
| Actual Positive | 709 | 11 |

      