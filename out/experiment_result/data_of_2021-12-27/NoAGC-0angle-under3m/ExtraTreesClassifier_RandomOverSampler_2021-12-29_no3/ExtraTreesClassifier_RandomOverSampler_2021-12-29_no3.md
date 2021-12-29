# ExtraTreesClassifier_RandomOverSampler_2021-12-29_no3
## Constants
- CSV_PATH = ../out/csv/experiment
- OUTPUT_PATH = ../out/experiment_result/data_of_2021-12-27/NoAGC-0angle-under3m
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
- 2021-12-27_raspi_48000Hz_w1_N2^12_overlap80_new.csv

## Estimator
### Type
- resampler = RandomOverSampler
- estimator = ExtraTreesClassifier

### Arguments for hyperparameter search
- resampler = RandomOverSampler
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
	- shrinkage = None
	- n_features_in_ = 36
	- sampling_strategy_ = OrderedDict([(1, 48)])
	- shrinkage_ = None
	- sample_indices_ = [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23
 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47
 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71
 72 73 74 75 76 77 78 79 32 11 66 76 54 33 66 22 32 45 10 32 54 54 33 22
 11 33 33 10 23 22  1 33 55 67 23  1 77 55 22  0 55 45 23 66 55 44  0 54
 54 76 45 77 55 55 77 76]

- best_estimator
	- base_estimator = ExtraTreeClassifier()
	- n_estimators = 100
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
	- min_samples_leaf = 10
	- min_weight_fraction_leaf = 0.0
	- max_features = log2
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
- gp_auc_min = 0.12377748226800697
- gp_max_val_mean = 0.08601575519372616
- gp_auc_mean = 0.08511107739749679
- gp_max_val_min = 0.07696767119877132
- diff_std = 0.0688737386138547
- gp_auc_max = 0.05659197971573421
- diff_auc = 0.05591470976177394
- gp_max_val_max = 0.05098531948174699
- low_power = 0.04913420326947185
- coe1[0] = 0.038111786100988865
- high_power = 0.03431823911244792
- srmr = 0.03411532125469023
- coe1[1] = 0.027659664464522584
- hlbr = 0.023430590771018483
- gp_max_ix_std = 0.023283884225293948
- coe3[3] = 0.02038823430568656
- ratio_max_to_9th_ave_peaks = 0.016121004037312373
- gp_max_ix_mean = 0.01103373882539645
- gp_auc_range = 0.010910001240334614
- coe3[2] = 0.009361757683739152
- gp_max_ix_min = 0.009299303939614097
- ac_auc = 0.008770001709252946
- tdoa_min = 0.00839039188668244
- tdoa_std = 0.007907831436454698
- tdoa_mean = 0.007832762812311994
- ratio_max_to_10ms_ave_peaks = 0.00751072523095807
- gp_max_val_std = 0.0071722059501666425
- tdoa_max = 0.006887148813633508
- ac_std = 0.006758292617996971
- gp_max_ix_max = 0.0067329677381092025
- gp_auc_std = 0.005736028604994851
- gp_max_ix_range = 0.00542181763883389
- gp_max_val_range = 0.0052816273884166275
- tdoa_range = 0.004192735310559955
- coe3[0] = 0.0
- coe3[1] = 0.0

## Evaluation
cv = 8
### accuracy
- Scores = [ 0.6666666666666666, 0.9333333333333333, 0.8, 0.8666666666666667, 0.7333333333333333, 0.8, 0.8666666666666667, 0.7857142857142857 ]
- Mean = 0.8065476190476191
- Standard deviation = 0.07806247497998

### balanced_accuracy
- Scores = [ 0.5416666666666666, 0.9583333333333333, 0.875, 0.9166666666666667, 0.7083333333333333, 0.75, 0.9166666666666667, 0.8636363636363636 ]
- Mean = 0.8162878787878788
- Standard deviation = 0.13109289758085013

### f1
- Scores = [ 0.28571428571428575, 0.8571428571428571, 0.6666666666666666, 0.7499999999999999, 0.5, 0.5714285714285715, 0.7499999999999999, 0.6666666666666666 ]
- Mean = 0.6309523809523809
- Standard deviation = 0.1665603402337288

### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 76 | 19 |
| Actual Positive | 4 | 20 |

      