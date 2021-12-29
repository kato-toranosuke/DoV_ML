# ExtraTreesClassifier_SMOTETomek_2021-12-29_no6
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
- gp_auc_min = 0.19109342879953636
- diff_std = 0.13777006985082652
- diff_auc = 0.12660368524085966
- coe1[0] = 0.09590183401415432
- gp_max_val_min = 0.08223804854701854
- coe1[1] = 0.06558086780631575
- high_power = 0.03301509730479795
- gp_auc_mean = 0.03290219514187053
- gp_auc_max = 0.03047848691512771
- gp_max_val_mean = 0.025366589876430666
- gp_max_val_max = 0.024636771804310283
- gp_max_ix_std = 0.015961210400241718
- srmr = 0.014134950851223273
- gp_auc_range = 0.013616192757540257
- gp_max_val_range = 0.012540199727845525
- gp_max_ix_mean = 0.010710539785256691
- tdoa_mean = 0.008405829521248418
- hlbr = 0.007611729090051541
- ratio_max_to_10ms_ave_peaks = 0.007386801504991809
- tdoa_min = 0.007355831365820968
- coe3[3] = 0.006205687067045405
- gp_auc_std = 0.005885864092793544
- low_power = 0.005410346849317649
- tdoa_max = 0.0048661990653903805
- tdoa_std = 0.004834955310281224
- gp_max_ix_max = 0.004703209332742465
- gp_max_ix_range = 0.004545067288909981
- gp_max_val_std = 0.004527219450387362
- ac_std = 0.004479558396203971
- ac_auc = 0.004373427008286572
- gp_max_ix_min = 0.0035931325222963322
- tdoa_range = 0.0024102924221752423
- ratio_max_to_9th_ave_peaks = 0.00045735139801339285
- coe3[2] = 0.00039732949068798317
- coe3[0] = 0.0
- coe3[1] = 0.0

## Evaluation
cv = 8
### accuracy
- Scores = [ 0.8666666666666667, 0.8666666666666667, 0.8, 0.9333333333333333, 0.7333333333333333, 0.9333333333333333, 0.8, 0.7857142857142857 ]
- Mean = 0.8398809523809524
- Standard deviation = 0.06742500242774155

### balanced_accuracy
- Scores = [ 0.9166666666666667, 0.7916666666666666, 0.875, 0.9583333333333333, 0.7083333333333333, 0.8333333333333333, 0.75, 0.6212121212121212 ]
- Mean = 0.8068181818181819
- Standard deviation = 0.10487021363566006

### f1
- Scores = [ 0.7499999999999999, 0.6666666666666666, 0.6666666666666666, 0.8571428571428571, 0.5, 0.8, 0.5714285714285715, 0.4 ]
- Mean = 0.6514880952380953
- Standard deviation = 0.14453350510742985

### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 82 | 13 |
| Actual Positive | 6 | 18 |

      