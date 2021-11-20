# ExtraTreesClassifier_RandomOverSampler_2021-11-05_no1
## Constants
- CSV_PATH = ../../out/csv/
- OUTPUT_PATH = ./result/
- FEATURE_ATTRBS = ['low_power', 'high_power', 'hlbr', 'coe1[0]', 'coe1[1]', 'coe3[0]', 'coe3[1]', 'coe3[2]', 'coe3[3]', 'ratio_max_to_10ms_ave_peaks', 'ratio_max_to_9th_ave_peaks', 'ac_std', 'ac_auc', 'diff_std', 'diff_auc', 'srmr', 'gp_max_val_std', 'gp_max_val_range', 'gp_max_val_min', 'gp_max_val_max', 'gp_max_val_mean', 'gp_max_ix_std', 'gp_max_ix_range', 'gp_max_ix_min', 'gp_max_ix_max', 'gp_max_ix_mean', 'gp_auc_std', 'gp_auc_range', 'gp_auc_min', 'gp_auc_max', 'gp_auc_mean', 'tdoa_std', 'tdoa_range', 'tdoa_min', 'tdoa_max', 'tdoa_mean']
- LABEL_ATTRB = ['dov_angle']
- FACING_DOV_ANGLES = [0, 45, 315]
- NCV = 10
- SCORING = ['accuracy', 'balanced_accuracy', 'f1']
- REFIT_SCORING = balanced_accuracy
- PARAM_GRID = [{'est__n_estimators': [10, 100, 1000], 'est__min_samples_split': [2, 5, 10], 'est__min_samples_leaf': [1, 5, 10], 'est__max_features': ['sqrt', 'log2', None], 'est__bootstrap': [False], 'est__n_jobs': [-1], 'est__random_state': [42], 'est__max_samples': [0.01, 0.5, 0.09]}, {'est__n_estimators': [10, 100, 1000], 'est__min_samples_split': [2, 5, 10], 'est__min_samples_leaf': [1, 5, 10], 'est__max_features': ['sqrt', 'log2', None], 'est__bootstrap': [True], 'est__oob_score': [True, False], 'est__n_jobs': [-1], 'est__random_state': [42], 'est__max_samples': [0.01, 0.5, 0.09]}]

## Loaded CSV
- features_mono_ch_matlab.csv

## Estimator
### Type
- resampler = RandomOverSampler
- estimator = ExtraTreesClassifier

### Arguments for hyperparameter search
- resampler = RandomOverSampler
- estimator = ExtraTreesClassifier
- param_grid = 
	- {'est__n_estimators': [10, 100, 1000], 'est__min_samples_split': [2, 5, 10], 'est__min_samples_leaf': [1, 5, 10], 'est__max_features': ['sqrt', 'log2', None], 'est__bootstrap': [False], 'est__n_jobs': [-1], 'est__random_state': [42], 'est__max_samples': [0.01, 0.5, 0.09]}
	- {'est__n_estimators': [10, 100, 1000], 'est__min_samples_split': [2, 5, 10], 'est__min_samples_leaf': [1, 5, 10], 'est__max_features': ['sqrt', 'log2', None], 'est__bootstrap': [True], 'est__oob_score': [True, False], 'est__n_jobs': [-1], 'est__random_state': [42], 'est__max_samples': [0.01, 0.5, 0.09]}

- scoring = ['accuracy', 'balanced_accuracy', 'f1']
- refit = balanced_accuracy
- cv = 10

### Parameters of the best estimator
#### The best hyper-parameters
- best_resampler
	- sampling_strategy = auto
	- random_state = 42
	- shrinkage = None
	- n_features_in_ = 36
	- sampling_strategy_ = OrderedDict([(1, 1440)])
	- shrinkage_ = None
	- sample_indices_ = [   0    1    2 ... 1375 3697 2545]

- best_estimator
	- base_estimator = ExtraTreeClassifier()
	- n_estimators = 1000
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
	- oob_decision_function_ = [[0.00778146 0.99221854]
 [0.0052226  0.9947774 ]
 [0.33158566 0.66841434]
 ...
 [0.02254203 0.97745797]
 [0.33457859 0.66542141]
 [0.41273709 0.58726291]]
	- oob_score_ = 0.9045833333333333

#### Importance of features
- gp_max_val_max = 0.19331166599634056
- gp_max_val_mean = 0.17206322983437589
- gp_max_val_min = 0.06135232320050041
- gp_max_val_range = 0.04698982775886011
- gp_auc_min = 0.036838441332401106
- gp_auc_mean = 0.0363056717491303
- gp_max_val_std = 0.03369130015841887
- gp_auc_max = 0.0281056878869243
- ac_auc = 0.022100475923529574
- diff_std = 0.021020835974247573
- diff_auc = 0.0202936319876614
- tdoa_mean = 0.02008882144089134
- high_power = 0.019985189744347775
- gp_max_ix_mean = 0.019976369782997144
- ratio_max_to_10ms_ave_peaks = 0.01985652903328707
- ratio_max_to_9th_ave_peaks = 0.019451402407977655
- srmr = 0.01851942003186143
- gp_auc_std = 0.018284752436756944
- gp_auc_range = 0.01718118192939691
- hlbr = 0.015567919921760414
- tdoa_min = 0.01514389004625405
- tdoa_std = 0.014904752835336673
- gp_max_ix_min = 0.014869779196251324
- gp_max_ix_std = 0.014742098647345391
- ac_std = 0.013599506813506631
- coe1[1] = 0.011683319132845616
- coe1[0] = 0.010950561733402383
- coe3[2] = 0.010855093368842928
- low_power = 0.010417289936599627
- coe3[3] = 0.010061869987463584
- tdoa_range = 0.00804712134330019
- gp_max_ix_max = 0.007964927059376405
- gp_max_ix_range = 0.007912399838187817
- tdoa_max = 0.007862711529620623
- coe3[0] = 0.0
- coe3[1] = 0.0

## Evaluation
cv = 10
### accuracy
- Scores = [ 0.7829861111111112, 0.9045138888888888, 0.8923611111111112, 0.8802083333333334, 0.8611111111111112, 0.8246527777777778, 0.8506944444444444, 0.8333333333333334, 0.9010416666666666, 0.7604166666666666 ]
- Mean = 0.8491319444444445
- Standard deviation = 0.046729777616917274

### balanced_accuracy
- Scores = [ 0.8171296296296297, 0.9050925925925926, 0.8888888888888888, 0.849537037037037, 0.8435185185185186, 0.7773148148148148, 0.8629629629629629, 0.7962962962962963, 0.8847222222222222, 0.6907407407407408 ]
- Mean = 0.8316203703703703
- Standard deviation = 0.06098895268086152

### f1
- Scores = [ 0.7672253258845437, 0.8769574944071588, 0.8590909090909091, 0.8198433420365535, 0.8067632850241546, 0.7154929577464788, 0.8208333333333333, 0.7446808510638299, 0.8613138686131386, 0.5632911392405063 ]
- Mean = 0.7835492506440607
- Standard deviation = 0.08868356719447831

### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 3246 | 354 |
| Actual Positive | 515 | 1645 |

      