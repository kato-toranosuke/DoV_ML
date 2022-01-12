# ExtraTreesClassifier_SMOTETomek_2022-01-10_no6
## Constants
- CSV_PATH = ../out/csv/experiment
- OUTPUT_PATH = ../out/experiment_result/data_of_2022-01-10/NoAGC-0angle-under5m
- FEATURE_ATTRBS = ['low_power', 'high_power', 'hlbr', 'coe1[0]', 'coe1[1]', 'coe3[0]', 'coe3[1]', 'coe3[2]', 'coe3[3]', 'ratio_max_to_10ms_ave_peaks', 'ratio_max_to_9th_ave_peaks', 'ac_std', 'ac_auc', 'diff_std', 'diff_auc', 'srmr', 'gp_max_val_std', 'gp_max_val_range', 'gp_max_val_min', 'gp_max_val_max', 'gp_max_val_mean', 'gp_max_ix_std', 'gp_max_ix_range', 'gp_max_ix_min', 'gp_max_ix_max', 'gp_max_ix_mean', 'gp_auc_std', 'gp_auc_range', 'gp_auc_min', 'gp_auc_max', 'gp_auc_mean', 'tdoa_std', 'tdoa_range', 'tdoa_min', 'tdoa_max', 'tdoa_mean']
- LABEL_ATTRB = ['facing']
- FACING_DOV_ANGLES = [1]
- NCV = 8
- SCORING = ['accuracy', 'balanced_accuracy', 'f1']
- REFIT_SCORING = balanced_accuracy
- PARAM_GRID = [{'est__n_estimators': [50, 100, 150, 200, 300], 'est__min_samples_split': [2, 5, 10], 'est__min_samples_leaf': [1, 5, 10], 'est__max_features': ['sqrt', 'log2', None], 'est__bootstrap': [False], 'est__n_jobs': [-1], 'est__random_state': [42], 'est__max_samples': [0.01, 0.5, 0.09]}, {'est__n_estimators': [50, 100, 150, 200, 300], 'est__min_samples_split': [2, 5, 10], 'est__min_samples_leaf': [1, 5, 10], 'est__max_features': ['sqrt', 'log2', None], 'est__bootstrap': [True], 'est__oob_score': [True, False], 'est__n_jobs': [-1], 'est__random_state': [42], 'est__max_samples': [0.01, 0.5, 0.09]}]
- TRAIN_SET_SESSION = ['trial1', 'trial2']
- TEST_SET_SESSION = ['trial3', 'trial4', 'trial5']
- DISTANCE = [1, 3, 5]
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
	- n_estimators = 100
	- estimator_params = ('criterion', 'max_depth', 'min_samples_split', 'min_samples_leaf', 'min_weight_fraction_leaf', 'max_features', 'max_leaf_nodes', 'min_impurity_decrease', 'random_state', 'ccp_alpha')
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
	- min_samples_split = 10
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

#### Importance of features
- gp_max_val_min = 0.09390556548477232
- gp_auc_min = 0.09057945670119215
- gp_auc_max = 0.08128375177004328
- gp_max_val_mean = 0.07322296574381806
- gp_max_val_max = 0.07223934674885783
- gp_auc_mean = 0.05697045089994039
- hlbr = 0.05438882421786272
- srmr = 0.02661154042346971
- gp_auc_std = 0.026088348380555165
- gp_max_val_std = 0.025616112473535423
- coe1[0] = 0.0224123048076424
- coe1[1] = 0.020648413451556456
- tdoa_min = 0.020451354860047326
- tdoa_range = 0.019796984607503326
- tdoa_max = 0.01946464197915806
- gp_max_ix_min = 0.01890395916626921
- diff_auc = 0.018657012329347494
- tdoa_mean = 0.018349209209995044
- gp_max_ix_max = 0.01832512454367382
- high_power = 0.01802334693745739
- coe3[3] = 0.018008758588862857
- gp_max_ix_mean = 0.017889709762922302
- diff_std = 0.01775053195196442
- coe3[2] = 0.017656089495242798
- low_power = 0.016430998714949435
- gp_max_ix_range = 0.016173282356329137
- ratio_max_to_10ms_ave_peaks = 0.015634670220073695
- gp_auc_range = 0.01540476589582374
- tdoa_std = 0.0150015589544337
- ac_auc = 0.01321849413697881
- gp_max_ix_std = 0.01243834145203871
- gp_max_val_range = 0.012201865737003898
- ac_std = 0.011332715276143214
- ratio_max_to_9th_ave_peaks = 0.004919502720535583
- coe3[0] = 0.0
- coe3[1] = 0.0

## Evaluation
cv = 8
### accuracy
- Scores = [ 0.7931034482758621, 0.7142857142857143, 0.7857142857142857, 0.8214285714285714, 0.8214285714285714, 0.7142857142857143, 0.7857142857142857, 0.8214285714285714 ]
- Mean = 0.7821736453201971
- Standard deviation = 0.041810469521785645

### balanced_accuracy
- Scores = [ 0.7463768115942029, 0.7575757575757576, 0.6818181818181819, 0.7045454545454546, 0.7045454545454546, 0.6695652173913043, 0.6347826086956522, 0.5 ]
- Mean = 0.674901185770751
- Standard deviation = 0.07581033707201566

### f1
- Scores = [ 0.5714285714285715, 0.5555555555555556, 0.5, 0.5454545454545454, 0.5454545454545454, 0.42857142857142855, 0.4000000000000001, 0.0 ]
- Mean = 0.4433080808080808
- Standard deviation = 0.177380573618348

### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 150 | 30 |
| Actual Positive | 19 | 26 |

      