# ExtraTreesClassifier_SMOTE_2021-12-28_no11
## Constants
- CSV_PATH = ../out/csv/experiment
- OUTPUT_PATH = ../out/experiment_result
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
- resampler = SMOTE
- estimator = ExtraTreesClassifier

### Arguments for hyperparameter search
- resampler = SMOTE
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
	- k_neighbors = 5
	- n_jobs = -1
	- n_features_in_ = 36
	- sampling_strategy_ = OrderedDict([(1, 30)])
	- nn_k_ = NearestNeighbors(n_neighbors=6)

- best_estimator
	- base_estimator = ExtraTreeClassifier()
	- n_estimators = 50
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
	- min_samples_split = 2
	- min_samples_leaf = 10
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
	- oob_decision_function_ = [[0.40722062 0.59277938]
 [0.25325588 0.74674412]
 [0.38366764 0.61633236]
 [0.38321859 0.61678141]
 [0.26381248 0.73618752]
 [0.54440541 0.45559459]
 [0.8339397  0.1660603 ]
 [0.78862415 0.21137585]
 [0.73796579 0.26203421]
 [0.74926717 0.25073283]
 [0.31100753 0.68899247]
 [0.4067551  0.5932449 ]
 [0.27053981 0.72946019]
 [0.41336131 0.58663869]
 [0.40565316 0.59434684]
 [0.49711279 0.50288721]
 [0.64329987 0.35670013]
 [0.79621753 0.20378247]
 [0.8174829  0.1825171 ]
 [0.76449544 0.23550456]
 [0.80711057 0.19288943]
 [0.83526408 0.16473592]
 [0.37016501 0.62983499]
 [0.44788451 0.55211549]
 [0.42369209 0.57630791]
 [0.3231135  0.6768865 ]
 [0.34294708 0.65705292]
 [0.47847467 0.52152533]
 [0.78863247 0.21136753]
 [0.70243427 0.29756573]
 [0.79987991 0.20012009]
 [0.82911585 0.17088415]
 [0.72420791 0.27579209]
 [0.8155223  0.1844777 ]
 [0.37286132 0.62713868]
 [0.27737499 0.72262501]
 [0.24593533 0.75406467]
 [0.35061705 0.64938295]
 [0.47536691 0.52463309]
 [0.54004441 0.45995559]
 [0.73721057 0.26278943]
 [0.75360934 0.24639066]
 [0.80411308 0.19588692]
 [0.75720989 0.24279011]
 [0.74707329 0.25292671]
 [0.70479648 0.29520352]
 [0.46707304 0.53292696]
 [0.57446817 0.42553183]
 [0.48428845 0.51571155]
 [0.46386052 0.53613948]
 [0.28523076 0.71476924]
 [0.22627073 0.77372927]
 [0.26916465 0.73083535]
 [0.36796324 0.63203676]
 [0.26590045 0.73409955]
 [0.34085529 0.65914471]
 [0.27843612 0.72156388]
 [0.33165337 0.66834663]
 [0.22594773 0.77405227]
 [0.27274739 0.72725261]
 [0.21015781 0.78984219]
 [0.26503658 0.73496342]
 [0.23554244 0.76445756]
 [0.34466686 0.65533314]
 [0.28415979 0.71584021]
 [0.3114948  0.6885052 ]
 [0.31330935 0.68669065]
 [0.39971389 0.60028611]
 [0.28152705 0.71847295]
 [0.54222121 0.45777879]
 [0.27363432 0.72636568]
 [0.56561154 0.43438846]
 [0.23808973 0.76191027]
 [0.30285518 0.69714482]
 [0.36846797 0.63153203]
 [0.24468252 0.75531748]
 [0.40475727 0.59524273]
 [0.52774054 0.47225946]
 [0.31340431 0.68659569]
 [0.26382702 0.73617298]]
	- oob_score_ = 0.775

#### Importance of features
- gp_auc_min = 0.17257113448388256
- srmr = 0.1319165331914542
- tdoa_max = 0.11394659252287
- hlbr = 0.10658345872154683
- gp_max_val_min = 0.07820728291316527
- gp_auc_mean = 0.05131940501191546
- gp_max_val_mean = 0.04661157024793388
- gp_max_val_max = 0.04331477061787324
- gp_max_ix_max = 0.04110215557638238
- diff_auc = 0.03338842975206612
- high_power = 0.028472434081499232
- coe3[3] = 0.02
- ratio_max_to_10ms_ave_peaks = 0.02
- ac_auc = 0.02
- tdoa_std = 0.02
- gp_auc_max = 0.019794026776519053
- tdoa_mean = 0.018499946731062884
- diff_std = 0.010003894719665696
- coe3[2] = 0.00848978516351188
- gp_auc_std = 0.0046886446886446834
- gp_max_ix_std = 0.004091653027823247
- tdoa_min = 0.003599550056242976
- ratio_max_to_9th_ave_peaks = 0.0020979020979020975
- gp_max_val_range = 0.0008524541691306926
- ac_std = 0.00020597322348094672
- coe1[0] = 0.00013962730250791796
- coe1[1] = 0.00010277492291881172
- low_power = 0.0
- coe3[0] = 0.0
- coe3[1] = 0.0
- gp_max_val_std = 0.0
- gp_max_ix_range = 0.0
- gp_max_ix_min = 0.0
- gp_max_ix_mean = 0.0
- gp_auc_range = 0.0
- tdoa_range = 0.0

## Evaluation
cv = 8
### accuracy
- Scores = [ 0.4, 0.6, 0.8, 0.4444444444444444, 0.8888888888888888, 0.6666666666666666, 0.8888888888888888, 0.8888888888888888 ]
- Mean = 0.6972222222222222
- Standard deviation = 0.18821366240538803

### balanced_accuracy
- Scores = [ 0.625, 0.75, 0.875, 0.4642857142857143, 0.9285714285714286, 0.7857142857142857, 0.75, 0.9375 ]
- Mean = 0.7645089285714286
- Standard deviation = 0.1497990722188477

### f1
- Scores = [ 0.4, 0.5, 0.6666666666666666, 0.28571428571428575, 0.8, 0.5714285714285715, 0.6666666666666666, 0.6666666666666666 ]
- Mean = 0.5696428571428571
- Standard deviation = 0.15634605890797

### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 39 | 21 |
| Actual Positive | 2 | 13 |

      