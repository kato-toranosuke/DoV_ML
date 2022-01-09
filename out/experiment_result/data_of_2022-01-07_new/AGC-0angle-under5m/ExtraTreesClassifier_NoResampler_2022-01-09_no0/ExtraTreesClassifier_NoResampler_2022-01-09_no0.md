# ExtraTreesClassifier_NoResampler_2022-01-09_no0
## Constants
- CSV_PATH = ../out/csv/experiment
- OUTPUT_PATH = ../out/experiment_result/data_of_2022-01-07_new/AGC-0angle-under5m
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
- 2021-12-27_raspi_48000Hz_w1_N2^12_overlap80_with2022-01-07.csv

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
	- n_estimators = 200
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
	- max_features = None
	- max_leaf_nodes = None
	- min_impurity_decrease = 0.0
	- ccp_alpha = 0.0
	- n_features_in_ = 36
	- n_outputs_ = 1
	- classes_ = [0 1]
	- n_classes_ = 2
	- base_estimator_ = ExtraTreeClassifier()

#### Importance of features
- high_power = 0.1374774533348667
- diff_auc = 0.10492596195479585
- gp_max_val_min = 0.09131453411737428
- gp_auc_min = 0.08680438744582604
- diff_std = 0.06867406286788855
- gp_max_val_mean = 0.042768992923956965
- gp_auc_mean = 0.042364871936567405
- hlbr = 0.03647025041361415
- gp_auc_range = 0.03547316330107938
- coe1[1] = 0.032455478875643054
- ratio_max_to_9th_ave_peaks = 0.029833141106515332
- gp_max_val_range = 0.02621551733463391
- gp_max_val_std = 0.023752337392343205
- gp_max_val_max = 0.022819748364106315
- srmr = 0.022696481336239093
- gp_auc_max = 0.02123232163055669
- gp_auc_std = 0.02109004489069792
- low_power = 0.019238656758990752
- coe1[0] = 0.019066149298669777
- ratio_max_to_10ms_ave_peaks = 0.013846588145460392
- gp_max_ix_max = 0.013720028129326689
- tdoa_max = 0.013245567973465211
- coe3[3] = 0.013192147948863985
- ac_auc = 0.01096247143089913
- coe3[2] = 0.009065989506601339
- ac_std = 0.008757214321868826
- gp_max_ix_range = 0.007269690299865872
- tdoa_range = 0.007093139375141492
- tdoa_mean = 0.005422930370322231
- tdoa_std = 0.0035746135018656995
- gp_max_ix_mean = 0.0030306497016071086
- gp_max_ix_min = 0.0025624806812992473
- gp_max_ix_std = 0.001971466420893638
- tdoa_min = 0.001611466908153775
- coe3[0] = 0.0
- coe3[1] = 0.0

## Evaluation
cv = 8
### accuracy
- Scores = [ 0.7586206896551724, 0.75, 0.8571428571428571, 0.7857142857142857, 0.8928571428571429, 0.8214285714285714, 0.8214285714285714, 0.7857142857142857 ]
- Mean = 0.8091133004926108
- Standard deviation = 0.045774057980408386

### balanced_accuracy
- Scores = [ 0.6014492753623188, 0.5984848484848485, 0.7272727272727273, 0.5606060606060607, 0.8106060606060606, 0.8913043478260869, 0.5782608695652174, 0.6347826086956522 ]
- Mean = 0.6753458498023716
- Standard deviation = 0.11359698745905944

### f1
- Scores = [ 0.3636363636363636, 0.3636363636363636, 0.6, 0.25, 0.7272727272727272, 0.6666666666666666, 0.28571428571428575, 0.4000000000000001 ]
- Mean = 0.45711580086580084
- Standard deviation = 0.16967862418712135

### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 162 | 18 |
| Actual Positive | 27 | 18 |

      