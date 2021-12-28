# ExtraTreesClassifier_NoResampler_2021-12-28_no7
## Constants
- CSV_PATH = ../out/csv/experiment
- OUTPUT_PATH = ../out/experiment_result/data_of_2021-12-27/AGC-0angle-under5m
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
- AGC_STATUS = ['AGC']

## Loaded CSV
- 2021-12-27_raspi_48000Hz_w1_N2^12_overlap80_new.csv

## Estimator
### Type
- resampler = NoResampler
- estimator = ExtraTreesClassifier

### Arguments for hyperparameter search
- resampler = NoResampler
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
	- min_samples_split = 5
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

#### Importance of features
- diff_auc = 0.12452968725132278
- high_power = 0.10680729929750965
- gp_auc_min = 0.09228200689150269
- gp_max_val_min = 0.06460444960834898
- coe1[1] = 0.05289213503416863
- gp_auc_mean = 0.044256336697446406
- coe1[0] = 0.04306516302955103
- diff_std = 0.04081447125582557
- gp_max_val_mean = 0.03243093131396184
- ratio_max_to_9th_ave_peaks = 0.03128584167669886
- low_power = 0.028577436005606152
- gp_max_val_range = 0.027626925643534913
- gp_max_val_max = 0.024888802177254067
- hlbr = 0.024055533972970274
- coe3[3] = 0.02386322157988987
- srmr = 0.02359842786891892
- ratio_max_to_10ms_ave_peaks = 0.02301828511487762
- gp_auc_std = 0.02100278677945163
- gp_auc_max = 0.018909956268750458
- gp_auc_range = 0.018466680175202258
- gp_max_ix_max = 0.018151371633050584
- tdoa_max = 0.016905434616313383
- gp_max_val_std = 0.01685280275962527
- coe3[2] = 0.011546120228307859
- ac_auc = 0.011463408606970616
- tdoa_mean = 0.010636674238365531
- gp_max_ix_min = 0.00842743799478902
- ac_std = 0.007438215851287563
- gp_max_ix_mean = 0.006404678193096143
- tdoa_std = 0.006367289029171235
- gp_max_ix_std = 0.006204034916228043
- gp_max_ix_range = 0.006200023209055629
- tdoa_range = 0.004309712597900347
- tdoa_min = 0.0021164184830461917
- coe3[0] = 0.0
- coe3[1] = 0.0

## Evaluation
cv = 8
### accuracy
- Scores = [ 0.75, 0.75, 0.8571428571428571, 0.75, 0.8928571428571429, 0.8571428571428571, 0.75, 0.8214285714285714 ]
- Mean = 0.8035714285714286
- Standard deviation = 0.05646924393157819

### balanced_accuracy
- Scores = [ 0.5984848484848485, 0.6590909090909092, 0.7272727272727273, 0.4772727272727273, 0.8106060606060606, 0.8347826086956522, 0.6130434782608696, 0.5782608695652174 ]
- Mean = 0.6623517786561266
- Standard deviation = 0.11389299562215036

### f1
- Scores = [ 0.3636363636363636, 0.4615384615384615, 0.6, 0.0, 0.7272727272727272, 0.6666666666666666, 0.3636363636363636, 0.28571428571428575 ]
- Mean = 0.43355810855810856
- Standard deviation = 0.22042635129594526

### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 161 | 18 |
| Actual Positive | 26 | 19 |

      