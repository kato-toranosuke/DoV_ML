# ExtraTreesClassifier_SMOTETomek_2022-01-10_no6
## Constants
- CSV_PATH = ../out/csv/experiment
- OUTPUT_PATH = ../out/experiment_result/data_of_2022-01-10/NoAGC-0angle-5m
- FEATURE_ATTRBS = ['low_power', 'high_power', 'hlbr', 'coe1[0]', 'coe1[1]', 'coe3[0]', 'coe3[1]', 'coe3[2]', 'coe3[3]', 'ratio_max_to_10ms_ave_peaks', 'ratio_max_to_9th_ave_peaks', 'ac_std', 'ac_auc', 'diff_std', 'diff_auc', 'srmr', 'gp_max_val_std', 'gp_max_val_range', 'gp_max_val_min', 'gp_max_val_max', 'gp_max_val_mean', 'gp_max_ix_std', 'gp_max_ix_range', 'gp_max_ix_min', 'gp_max_ix_max', 'gp_max_ix_mean', 'gp_auc_std', 'gp_auc_range', 'gp_auc_min', 'gp_auc_max', 'gp_auc_mean', 'tdoa_std', 'tdoa_range', 'tdoa_min', 'tdoa_max', 'tdoa_mean']
- LABEL_ATTRB = ['facing']
- FACING_DOV_ANGLES = [1]
- NCV = 8
- SCORING = ['accuracy', 'balanced_accuracy', 'f1']
- REFIT_SCORING = balanced_accuracy
- PARAM_GRID = [{'est__n_estimators': [50, 100, 150, 200, 300], 'est__min_samples_split': [2, 5, 10], 'est__min_samples_leaf': [1, 5, 10], 'est__max_features': ['sqrt', 'log2', None], 'est__bootstrap': [False], 'est__n_jobs': [-1], 'est__random_state': [42], 'est__max_samples': [0.01, 0.5, 0.09]}, {'est__n_estimators': [50, 100, 150, 200, 300], 'est__min_samples_split': [2, 5, 10], 'est__min_samples_leaf': [1, 5, 10], 'est__max_features': ['sqrt', 'log2', None], 'est__bootstrap': [True], 'est__oob_score': [True, False], 'est__n_jobs': [-1], 'est__random_state': [42], 'est__max_samples': [0.01, 0.5, 0.09]}]
- TRAIN_SET_SESSION = ['trial1', 'trial2']
- TEST_SET_SESSION = ['trial3', 'trial4', 'trial5']
- DISTANCE = [5]
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
- gp_max_val_max = 0.1582750672129085
- gp_auc_max = 0.1354807487961051
- gp_auc_min = 0.09072088402809081
- gp_max_val_std = 0.08757986616804511
- gp_max_val_min = 0.08251638382050201
- gp_max_val_mean = 0.07298333027813803
- gp_auc_mean = 0.06367936488885008
- srmr = 0.061483476455427157
- gp_auc_std = 0.03934859665781712
- hlbr = 0.035071297048939916
- gp_max_ix_range = 0.020634960166669825
- high_power = 0.01977122448739549
- gp_auc_range = 0.017283486927021616
- gp_max_ix_mean = 0.01285016891660494
- gp_max_ix_min = 0.012520641210891784
- ratio_max_to_10ms_ave_peaks = 0.010332074781643689
- diff_std = 0.00910904498221051
- tdoa_max = 0.008443436744766915
- diff_auc = 0.007599045963702922
- coe3[2] = 0.005564004790126168
- coe3[3] = 0.0052570291415669395
- coe1[1] = 0.005239504226765557
- gp_max_ix_max = 0.005153356668545354
- tdoa_mean = 0.005004734620903085
- ac_std = 0.0046699739807282625
- ac_auc = 0.004614290996596933
- tdoa_std = 0.004593795604411933
- tdoa_min = 0.00435895274038103
- gp_max_val_range = 0.003275718291188997
- ratio_max_to_9th_ave_peaks = 0.0027222543629016652
- low_power = 0.002583942313735115
- tdoa_range = 0.0010013637697157123
- gp_max_ix_std = 0.000267855827672193
- coe1[0] = 1.0123129029643047e-05
- coe3[0] = 0.0
- coe3[1] = 0.0

## Evaluation
cv = 8
### accuracy
- Scores = [ 0.7, 0.8, 0.8, 0.7777777777777778, 0.6666666666666666, 0.8888888888888888, 0.8888888888888888, 1.0 ]
- Mean = 0.8152777777777778
- Standard deviation = 0.10136986122823737

### balanced_accuracy
- Scores = [ 0.8125, 0.6875, 0.875, 0.5, 0.6071428571428572, 0.75, 0.9285714285714286, 1.0 ]
- Mean = 0.7700892857142857
- Standard deviation = 0.1571244662533756

### f1
- Scores = [ 0.5714285714285715, 0.5, 0.6666666666666666, 0.0, 0.4, 0.6666666666666666, 0.8, 1.0 ]
- Mean = 0.575595238095238
- Standard deviation = 0.27724999463265915

### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 50 | 10 |
| Actual Positive | 1 | 14 |

      