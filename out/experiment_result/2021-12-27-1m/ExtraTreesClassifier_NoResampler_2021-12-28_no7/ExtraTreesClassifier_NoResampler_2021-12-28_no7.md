# ExtraTreesClassifier_NoResampler_2021-12-28_no7
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
	- min_samples_leaf = 1
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
- gp_auc_min = 0.0717347061805566
- gp_auc_max = 0.057564839862913816
- gp_max_val_mean = 0.053051457688733074
- gp_max_val_min = 0.04795754788358758
- gp_max_val_max = 0.047922244738257444
- gp_auc_range = 0.046429988754471636
- gp_auc_mean = 0.0457799534804939
- srmr = 0.041532977909983025
- gp_max_val_std = 0.039790278544260684
- gp_max_val_range = 0.03472921094988304
- hlbr = 0.0321306012534629
- high_power = 0.029815414952543164
- ac_std = 0.029642479918973688
- diff_std = 0.028904150886773526
- ac_auc = 0.027368256842042
- low_power = 0.02716235058730142
- coe3[3] = 0.02655377664262027
- gp_auc_std = 0.026237952171228415
- tdoa_mean = 0.025027636769079462
- coe3[2] = 0.02303416882445057
- coe1[1] = 0.020988081399458854
- diff_auc = 0.020983413397280208
- gp_max_ix_max = 0.02045940552514952
- coe1[0] = 0.02012204105626891
- ratio_max_to_10ms_ave_peaks = 0.018716368007342776
- tdoa_std = 0.017708729954068643
- gp_max_ix_mean = 0.017641461530183238
- tdoa_min = 0.017272988132653377
- tdoa_max = 0.0153642747773569
- ratio_max_to_9th_ave_peaks = 0.01524983874377256
- gp_max_ix_range = 0.014140694855528452
- gp_max_ix_std = 0.013164239041135296
- gp_max_ix_min = 0.013069479270797971
- tdoa_range = 0.012748989467386963
- coe3[0] = 0.0
- coe3[1] = 0.0

## Evaluation
cv = 8
### accuracy
- Scores = [ 0.5, 0.7, 0.8, 0.6666666666666666, 0.7777777777777778, 0.6666666666666666, 0.7777777777777778, 0.8888888888888888 ]
- Mean = 0.7222222222222222
- Standard deviation = 0.10957268290731123

### balanced_accuracy
- Scores = [ 0.3125, 0.8125, 0.5, 0.42857142857142855, 0.5, 0.7857142857142857, 0.5, 0.5 ]
- Mean = 0.5424107142857143
- Standard deviation = 0.16013972195701287

### f1
- Scores = [ 0.0, 0.5714285714285715, 0.0, 0.0, 0.0, 0.5714285714285715, 0.0, 0.0 ]
- Mean = 0.14285714285714288
- Standard deviation = 0.24743582965269678

### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 50 | 10 |
| Actual Positive | 11 | 4 |

      