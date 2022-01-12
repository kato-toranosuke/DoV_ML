# ExtraTreesClassifier_NoResampler_2022-01-10_no0
## Constants
- CSV_PATH = ../out/csv/experiment
- OUTPUT_PATH = ../out/experiment_result/data_of_2022-01-10/NoAGC-0angle-under3m
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
- 2022-01-10_raspi_48000Hz_w1_N2^12_overlap80.csv

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
	- n_estimators = 300
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
- gp_max_val_min = 0.1981189522133698
- gp_auc_min = 0.18332719551482934
- gp_max_val_mean = 0.09471705601443973
- gp_auc_mean = 0.08987282750990017
- gp_auc_max = 0.0488675679590725
- gp_max_ix_max = 0.04504245216013482
- gp_max_val_max = 0.0438335130854925
- tdoa_max = 0.037785216584868296
- gp_max_val_std = 0.025867233047463363
- srmr = 0.024800211370772485
- gp_auc_std = 0.0194735831278769
- hlbr = 0.01833001438704789
- gp_max_ix_std = 0.01616054192766939
- gp_max_val_range = 0.015164563274545967
- tdoa_mean = 0.014901833775334158
- gp_auc_range = 0.012774180187880672
- gp_max_ix_mean = 0.01218493761666895
- tdoa_std = 0.010695516202028613
- ratio_max_to_9th_ave_peaks = 0.009938461938016086
- diff_std = 0.007310504903826104
- ratio_max_to_10ms_ave_peaks = 0.007220281835699433
- coe1[0] = 0.006957586630334724
- coe3[3] = 0.00682767074549377
- ac_auc = 0.00629679526790449
- high_power = 0.00551882606598976
- coe1[1] = 0.005437339471784715
- diff_auc = 0.005132181949391692
- coe3[2] = 0.004806720384374162
- low_power = 0.004706733803795367
- ac_std = 0.004227143542697563
- gp_max_ix_range = 0.0036939126830655596
- gp_max_ix_min = 0.003692848801603222
- tdoa_range = 0.0033687132829293438
- tdoa_min = 0.002946882733698437
- coe3[0] = 0.0
- coe3[1] = 0.0

## Evaluation
cv = 8
### accuracy
- Scores = [ 0.6842105263157895, 0.7368421052631579, 0.7894736842105263, 0.7894736842105263, 0.8947368421052632, 0.9473684210526315, 0.6111111111111112, 0.7222222222222222 ]
- Mean = 0.7719298245614035
- Standard deviation = 0.10230784816912808

### balanced_accuracy
- Scores = [ 0.525, 0.7416666666666667, 0.5, 0.5916666666666667, 0.75, 0.875, 0.36666666666666664, 0.43333333333333335 ]
- Mean = 0.5979166666666667
- Standard deviation = 0.16434582018144275

### f1
- Scores = [ 0.25, 0.5454545454545454, 0.0, 0.3333333333333333, 0.6666666666666666, 0.8571428571428571, 0.0, 0.0 ]
- Mean = 0.3315746753246753
- Standard deviation = 0.3103900714686058

### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 104 | 16 |
| Actual Positive | 18 | 12 |

      