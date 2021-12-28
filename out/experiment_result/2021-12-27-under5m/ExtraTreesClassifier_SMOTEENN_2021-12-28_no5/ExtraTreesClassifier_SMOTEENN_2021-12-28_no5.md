# ExtraTreesClassifier_SMOTEENN_2021-12-28_no5
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
	- n_estimators = 200
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
	- min_samples_leaf = 5
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

#### Importance of features
- coe3[3] = 0.06761411560720082
- ac_std = 0.06442543663996668
- low_power = 0.0627322910393466
- ac_auc = 0.06116702815429151
- coe3[2] = 0.06082725219528253
- high_power = 0.05886381053286497
- coe1[0] = 0.056517276814388305
- gp_auc_min = 0.05303962746115999
- diff_auc = 0.052709262394557435
- coe1[1] = 0.052107113876512984
- gp_max_val_min = 0.045029744344363416
- diff_std = 0.04139050689632425
- hlbr = 0.03369733016442528
- gp_max_val_mean = 0.0330455365203204
- gp_auc_mean = 0.029304093072792872
- gp_max_ix_mean = 0.02791136504717486
- gp_max_val_max = 0.026872387920116213
- tdoa_mean = 0.02436603490449652
- gp_auc_max = 0.02207768560468476
- tdoa_std = 0.019516594582210476
- gp_max_ix_std = 0.017753780818847226
- srmr = 0.01541933857547684
- gp_auc_std = 0.01053168480875949
- tdoa_range = 0.010007624580152082
- gp_max_val_std = 0.009358017733654017
- tdoa_min = 0.007829931553960551
- gp_auc_range = 0.007231382519243594
- gp_max_ix_max = 0.007023884959494314
- tdoa_max = 0.006306060357688645
- gp_max_ix_range = 0.0041906897302687466
- gp_max_val_range = 0.003980906535005421
- gp_max_ix_min = 0.003426060258530721
- ratio_max_to_10ms_ave_peaks = 0.0031179987588712773
- ratio_max_to_9th_ave_peaks = 0.0006081450375663397
- coe3[0] = 0.0
- coe3[1] = 0.0

## Evaluation
cv = 8
### accuracy
- Scores = [ 0.6785714285714286, 0.8571428571428571, 0.7857142857142857, 0.6071428571428571, 0.7142857142857143, 0.8928571428571429, 0.6785714285714286, 0.7857142857142857 ]
- Mean = 0.75
- Standard deviation = 0.09105391988558544

### balanced_accuracy
- Scores = [ 0.553030303030303, 0.9090909090909092, 0.7424242424242424, 0.38636363636363635, 0.696969696969697, 0.9347826086956521, 0.491304347826087, 0.8695652173913043 ]
- Mean = 0.697941370223979
- Standard deviation = 0.19134101613589943

### f1
- Scores = [ 0.30769230769230765, 0.7499999999999999, 0.5714285714285715, 0.0, 0.5, 0.7692307692307693, 0.1818181818181818, 0.625 ]
- Mean = 0.46314622877122874
- Standard deviation = 0.2581347909108861

### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 141 | 38 |
| Actual Positive | 18 | 27 |

      