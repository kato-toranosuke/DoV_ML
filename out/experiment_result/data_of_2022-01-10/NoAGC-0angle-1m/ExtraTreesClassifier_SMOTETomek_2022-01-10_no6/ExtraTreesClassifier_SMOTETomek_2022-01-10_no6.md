# ExtraTreesClassifier_SMOTETomek_2022-01-10_no6
## Constants
- CSV_PATH = ../out/csv/experiment
- OUTPUT_PATH = ../out/experiment_result/data_of_2022-01-10/NoAGC-0angle-1m
- FEATURE_ATTRBS = ['low_power', 'high_power', 'hlbr', 'coe1[0]', 'coe1[1]', 'coe3[0]', 'coe3[1]', 'coe3[2]', 'coe3[3]', 'ratio_max_to_10ms_ave_peaks', 'ratio_max_to_9th_ave_peaks', 'ac_std', 'ac_auc', 'diff_std', 'diff_auc', 'srmr', 'gp_max_val_std', 'gp_max_val_range', 'gp_max_val_min', 'gp_max_val_max', 'gp_max_val_mean', 'gp_max_ix_std', 'gp_max_ix_range', 'gp_max_ix_min', 'gp_max_ix_max', 'gp_max_ix_mean', 'gp_auc_std', 'gp_auc_range', 'gp_auc_min', 'gp_auc_max', 'gp_auc_mean', 'tdoa_std', 'tdoa_range', 'tdoa_min', 'tdoa_max', 'tdoa_mean']
- LABEL_ATTRB = ['facing']
- FACING_DOV_ANGLES = [1]
- NCV = 8
- SCORING = ['accuracy', 'balanced_accuracy', 'f1']
- REFIT_SCORING = balanced_accuracy
- PARAM_GRID = [{'est__n_estimators': [50, 100, 150, 200, 300], 'est__min_samples_split': [2, 5, 10], 'est__min_samples_leaf': [1, 5, 10], 'est__max_features': ['sqrt', 'log2', None], 'est__bootstrap': [False], 'est__n_jobs': [-1], 'est__random_state': [42], 'est__max_samples': [0.01, 0.5, 0.09]}, {'est__n_estimators': [50, 100, 150, 200, 300], 'est__min_samples_split': [2, 5, 10], 'est__min_samples_leaf': [1, 5, 10], 'est__max_features': ['sqrt', 'log2', None], 'est__bootstrap': [True], 'est__oob_score': [True, False], 'est__n_jobs': [-1], 'est__random_state': [42], 'est__max_samples': [0.01, 0.5, 0.09]}]
- TRAIN_SET_SESSION = ['trial1', 'trial2']
- TEST_SET_SESSION = ['trial3', 'trial4', 'trial5']
- DISTANCE = [1]
- AGC_STATUS = ['NoAGC']

## Loaded CSV
- 2022-01-10_raspi_48000Hz_w1_N2^12_overlap80.csv

## Estimator
### Type
- resampler = SMOTETomek
- estimator = ExtraTreesClassifier

### Arguments for hyperparameter search
- resampler = SMOTETomek
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
	- tomek = None
	- n_jobs = -1
	- n_features_in_ = 36
	- sampling_strategy_ = auto
	- smote_ = SMOTE(n_jobs=-1, random_state=42)
	- tomek_ = TomekLinks(n_jobs=-1, sampling_strategy='all')

- best_estimator
	- base_estimator = ExtraTreeClassifier()
	- n_estimators = 50
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
	- max_features = log2
	- max_leaf_nodes = None
	- min_impurity_decrease = 0.0
	- ccp_alpha = 0.0
	- n_features_in_ = 36
	- n_outputs_ = 1
	- classes_ = [0 1]
	- n_classes_ = 2
	- base_estimator_ = ExtraTreeClassifier()
	- oob_decision_function_ = [[0.40425532 0.59574468]
 [0.26086957 0.73913043]
 [0.62222222 0.37777778]
 [0.625      0.375     ]
 [0.85106383 0.14893617]
 [0.8125     0.1875    ]
 [0.89130435 0.10869565]
 [0.88636364 0.11363636]
 [0.52380952 0.47619048]
 [0.42857143 0.57142857]
 [0.46666667 0.53333333]
 [0.4893617  0.5106383 ]
 [0.46341463 0.53658537]
 [0.69565217 0.30434783]
 [0.73913043 0.26086957]
 [0.73333333 0.26666667]
 [0.27659574 0.72340426]
 [0.35555556 0.64444444]
 [0.35555556 0.64444444]
 [0.59574468 0.40425532]
 [0.65217391 0.34782609]
 [0.8125     0.1875    ]
 [0.76595745 0.23404255]
 [0.28571429 0.71428571]
 [0.48780488 0.51219512]
 [0.15217391 0.84782609]
 [0.8        0.2       ]
 [0.55555556 0.44444444]
 [0.46808511 0.53191489]
 [0.33333333 0.66666667]
 [0.2173913  0.7826087 ]
 [0.27272727 0.72727273]
 [0.46666667 0.53333333]
 [0.35555556 0.64444444]
 [0.2173913  0.7826087 ]
 [0.40816327 0.59183673]
 [0.44444444 0.55555556]
 [0.38297872 0.61702128]
 [0.39130435 0.60869565]
 [0.23913043 0.76086957]
 [0.28571429 0.71428571]
 [0.40909091 0.59090909]
 [0.29787234 0.70212766]
 [0.42222222 0.57777778]
 [0.2826087  0.7173913 ]
 [0.31818182 0.68181818]
 [0.31818182 0.68181818]
 [0.34042553 0.65957447]
 [0.4        0.6       ]
 [0.48888889 0.51111111]
 [0.42222222 0.57777778]
 [0.37209302 0.62790698]]
	- oob_score_ = 0.8076923076923077

#### Importance of features
- tdoa_range = 0.07397959183673469
- tdoa_std = 0.0663265306122449
- hlbr = 0.049886621315192746
- gp_auc_mean = 0.04931972789115647
- gp_auc_min = 0.04280045351473923
- ac_std = 0.04223356009070295
- low_power = 0.04081632653061224
- high_power = 0.03939909297052154
- ratio_max_to_10ms_ave_peaks = 0.03939909297052154
- gp_max_val_min = 0.039257369614512476
- gp_auc_std = 0.03316326530612245
- coe1[1] = 0.031179138321995467
- ratio_max_to_9th_ave_peaks = 0.030328798185941044
- tdoa_mean = 0.030328798185941044
- gp_auc_max = 0.02947845804988662
- diff_auc = 0.02891156462585034
- gp_auc_range = 0.02891156462585034
- gp_max_val_mean = 0.02806122448979592
- gp_max_ix_range = 0.02806122448979592
- coe3[2] = 0.028061224489795915
- srmr = 0.025935374149659858
- gp_max_val_std = 0.02465986394557823
- gp_max_val_max = 0.02380952380952381
- gp_max_ix_min = 0.023242630385487528
- coe3[3] = 0.021825396825396824
- coe1[0] = 0.02040816326530612
- tdoa_min = 0.02040816326530612
- gp_max_val_range = 0.017006802721088437
- gp_max_ix_mean = 0.017006802721088437
- diff_std = 0.009070294784580499
- gp_max_ix_std = 0.009070294784580499
- tdoa_max = 0.007653061224489796
- coe3[0] = 0.0
- coe3[1] = 0.0
- ac_auc = 0.0
- gp_max_ix_max = 0.0

## Evaluation
cv = 8
### accuracy
- Scores = [ 0.6, 0.6, 0.7, 0.5555555555555556, 0.8888888888888888, 0.8888888888888888, 0.6666666666666666, 0.4444444444444444 ]
- Mean = 0.6680555555555556
- Standard deviation = 0.14597876346481375

### balanced_accuracy
- Scores = [ 0.75, 0.75, 0.8125, 0.7142857142857143, 0.75, 0.9285714285714286, 0.7857142857142857, 0.6875 ]
- Mean = 0.7723214285714286
- Standard deviation = 0.06916041689656102

### f1
- Scores = [ 0.5, 0.5, 0.5714285714285715, 0.5, 0.6666666666666666, 0.8, 0.5714285714285715, 0.2857142857142857 ]
- Mean = 0.549404761904762
- Standard deviation = 0.13891255467309277

### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 36 | 24 |
| Actual Positive | 3 | 12 |

      