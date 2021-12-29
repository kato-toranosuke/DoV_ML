# ExtraTreesClassifier_SMOTEENN_2021-12-29_no5
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
	- n_estimators = 150
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
	- oob_decision_function_ = [[0.27906977 0.72093023]
 [0.85714286 0.14285714]
 [0.88095238 0.11904762]
 [0.95833333 0.04166667]
 [0.96938776 0.03061224]
 [0.93478261 0.06521739]
 [0.73493976 0.26506024]
 [1.         0.        ]
 [0.69879518 0.30120482]
 [0.67741935 0.32258065]
 [0.94382022 0.05617978]
 [0.9893617  0.0106383 ]
 [0.96774194 0.03225806]
 [0.87356322 0.12643678]
 [0.6969697  0.3030303 ]
 [0.94505495 0.05494505]
 [0.93023256 0.06976744]
 [0.65909091 0.34090909]
 [0.9673913  0.0326087 ]
 [0.67346939 0.32653061]
 [0.55789474 0.44210526]
 [0.78431373 0.21568627]
 [0.79012346 0.20987654]
 [0.95402299 0.04597701]
 [0.20731707 0.79268293]
 [0.3372093  0.6627907 ]
 [0.20930233 0.79069767]
 [0.44871795 0.55128205]
 [0.03488372 0.96511628]
 [0.2345679  0.7654321 ]
 [0.05882353 0.94117647]
 [0.20689655 0.79310345]
 [0.34482759 0.65517241]
 [0.30337079 0.69662921]
 [0.20454545 0.79545455]
 [0.31460674 0.68539326]
 [0.3375     0.6625    ]
 [0.30337079 0.69662921]
 [0.35802469 0.64197531]]
	- oob_score_ = 0.9743589743589743

#### Importance of features
- diff_auc = 0.09508488779145981
- high_power = 0.07409410311458947
- low_power = 0.059784596181754836
- gp_auc_min = 0.05531587828316811
- coe1[0] = 0.05286113514264559
- coe1[1] = 0.05085801053413993
- hlbr = 0.040662544208706304
- diff_std = 0.04065647704453174
- ac_std = 0.03808980283521417
- coe3[3] = 0.03723984971316172
- ratio_max_to_10ms_ave_peaks = 0.03367844033037937
- ratio_max_to_9th_ave_peaks = 0.029524681974765987
- gp_auc_mean = 0.027901638966390585
- gp_max_val_min = 0.027828751101658746
- ac_auc = 0.027666239897613507
- srmr = 0.02482445138981087
- tdoa_range = 0.021477898581163373
- gp_max_val_max = 0.02128646089360375
- gp_max_val_range = 0.020508256993394078
- gp_auc_range = 0.020413401780857855
- tdoa_std = 0.019833492293576328
- gp_max_val_mean = 0.019802311134243904
- gp_max_val_std = 0.019746882902345088
- coe3[2] = 0.018680426613582136
- gp_max_ix_max = 0.01677721331639717
- tdoa_mean = 0.015356341189674523
- gp_auc_max = 0.015268934693362794
- tdoa_max = 0.015240372171919786
- gp_auc_std = 0.014144488318507929
- gp_max_ix_mean = 0.010535123642178967
- gp_max_ix_std = 0.010250091662323225
- tdoa_min = 0.009898632605703313
- gp_max_ix_min = 0.007769440436107103
- gp_max_ix_range = 0.006938742261067962
- coe3[0] = 0.0
- coe3[1] = 0.0

## Evaluation
cv = 8
### accuracy
- Scores = [ 0.8, 0.8666666666666667, 0.8, 0.8, 0.6666666666666666, 0.8666666666666667, 0.6666666666666666, 0.7857142857142857 ]
- Mean = 0.781547619047619
- Standard deviation = 0.0723918185765864

### balanced_accuracy
- Scores = [ 0.875, 0.7916666666666666, 0.875, 0.875, 0.6666666666666666, 0.7916666666666666, 0.4166666666666667, 0.8636363636363636 ]
- Mean = 0.7694128787878787
- Standard deviation = 0.149290455997533

### f1
- Scores = [ 0.6666666666666666, 0.6666666666666666, 0.6666666666666666, 0.6666666666666666, 0.4444444444444444, 0.6666666666666666, 0.0, 0.6666666666666666 ]
- Mean = 0.5555555555555556
- Standard deviation = 0.2222222222222222

### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 75 | 20 |
| Actual Positive | 6 | 18 |

      