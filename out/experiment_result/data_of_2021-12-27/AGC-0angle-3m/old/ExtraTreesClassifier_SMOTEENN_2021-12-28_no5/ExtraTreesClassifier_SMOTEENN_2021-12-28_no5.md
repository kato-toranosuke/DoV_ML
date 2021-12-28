# ExtraTreesClassifier_SMOTEENN_2021-12-28_no5
## Constants
- CSV_PATH = ../out/csv/experiment
- OUTPUT_PATH = ../out/experiment_result/2021-12-27-3m
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
	- oob_decision_function_ = [[0.70652174 0.29347826]
 [0.8        0.2       ]
 [0.69148936 0.30851064]
 [0.70103093 0.29896907]
 [0.65263158 0.34736842]
 [0.63157895 0.36842105]
 [0.30337079 0.69662921]
 [0.70652174 0.29347826]
 [0.81111111 0.18888889]
 [0.84536082 0.15463918]
 [0.8125     0.1875    ]
 [0.80645161 0.19354839]
 [0.61176471 0.38823529]
 [0.7173913  0.2826087 ]
 [0.66666667 0.33333333]
 [0.85869565 0.14130435]
 [0.80645161 0.19354839]
 [0.77419355 0.22580645]
 [0.73033708 0.26966292]
 [0.88043478 0.11956522]
 [0.85263158 0.14736842]
 [0.30107527 0.69892473]
 [0.30434783 0.69565217]
 [0.09090909 0.90909091]
 [0.06976744 0.93023256]
 [0.10869565 0.89130435]
 [0.12765957 0.87234043]
 [0.21111111 0.78888889]
 [0.12087912 0.87912088]
 [0.13483146 0.86516854]
 [0.20879121 0.79120879]
 [0.06818182 0.93181818]
 [0.06521739 0.93478261]
 [0.0989011  0.9010989 ]
 [0.05376344 0.94623656]
 [0.04210526 0.95789474]
 [0.11235955 0.88764045]
 [0.06315789 0.93684211]
 [0.06593407 0.93406593]
 [0.14285714 0.85714286]
 [0.06896552 0.93103448]
 [0.19318182 0.80681818]
 [0.03296703 0.96703297]
 [0.07608696 0.92391304]
 [0.10989011 0.89010989]
 [0.08791209 0.91208791]]
	- oob_score_ = 0.9347826086956522

#### Importance of features
- high_power = 0.11702127659574468
- low_power = 0.09574468085106383
- coe3[2] = 0.06382978723404255
- diff_auc = 0.06382978723404255
- gp_max_val_mean = 0.06382978723404255
- gp_auc_mean = 0.06382978723404255
- ratio_max_to_10ms_ave_peaks = 0.05319148936170213
- gp_max_val_min = 0.05319148936170213
- coe1[0] = 0.0425531914893617
- coe3[3] = 0.0425531914893617
- gp_auc_max = 0.0425531914893617
- gp_max_val_max = 0.031914893617021274
- gp_auc_min = 0.031914893617021274
- hlbr = 0.02127659574468085
- ratio_max_to_9th_ave_peaks = 0.02127659574468085
- ac_std = 0.02127659574468085
- diff_std = 0.02127659574468085
- srmr = 0.02127659574468085
- gp_max_val_range = 0.02127659574468085
- gp_max_ix_std = 0.02127659574468085
- coe1[1] = 0.010638297872340425
- ac_auc = 0.010638297872340425
- gp_max_val_std = 0.010638297872340425
- gp_max_ix_min = 0.010638297872340425
- gp_auc_range = 0.010638297872340425
- tdoa_std = 0.010638297872340425
- tdoa_max = 0.010638297872340425
- tdoa_mean = 0.010638297872340425
- coe3[0] = 0.0
- coe3[1] = 0.0
- gp_max_ix_range = 0.0
- gp_max_ix_max = 0.0
- gp_max_ix_mean = 0.0
- gp_auc_std = 0.0
- tdoa_range = 0.0
- tdoa_min = 0.0

## Evaluation
cv = 8
### accuracy
- Scores = [ 0.7, 0.3, 0.4444444444444444, 0.5555555555555556, 0.6666666666666666, 0.7777777777777778, 0.7777777777777778, 0.4444444444444444 ]
- Mean = 0.5833333333333334
- Standard deviation = 0.16424161665660536

### balanced_accuracy
- Scores = [ 0.8125, 0.5625, 0.6428571428571428, 0.7142857142857143, 0.7857142857142857, 0.5, 0.6785714285714286, 0.6875 ]
- Mean = 0.6729910714285714
- Standard deviation = 0.0982079441946204

### f1
- Scores = [ 0.5714285714285715, 0.3636363636363636, 0.4444444444444445, 0.5, 0.5714285714285715, 0.0, 0.5, 0.2857142857142857 ]
- Mean = 0.4045815295815296
- Standard deviation = 0.17852395990419193

### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 31 | 28 |
| Actual Positive | 3 | 12 |

      