# ExtraTreesClassifier_RandomOverSampler_2021-12-27_no4
## Constants
- CSV_PATH = ../out/csv/experiment
- OUTPUT_PATH = ../out/experiment_result
- FEATURE_ATTRBS = ['low_power', 'high_power', 'hlbr', 'coe1[0]', 'coe1[1]', 'coe3[0]', 'coe3[1]', 'coe3[2]', 'coe3[3]', 'ratio_max_to_10ms_ave_peaks', 'ratio_max_to_9th_ave_peaks', 'ac_std', 'ac_auc', 'diff_std', 'diff_auc', 'srmr', 'gp_max_val_std', 'gp_max_val_range', 'gp_max_val_min', 'gp_max_val_max', 'gp_max_val_mean', 'gp_max_ix_std', 'gp_max_ix_range', 'gp_max_ix_min', 'gp_max_ix_max', 'gp_max_ix_mean', 'gp_auc_std', 'gp_auc_range', 'gp_auc_min', 'gp_auc_max', 'gp_auc_mean', 'tdoa_std', 'tdoa_range', 'tdoa_min', 'tdoa_max', 'tdoa_mean']
- LABEL_ATTRB = ['dov_angle']
- FACING_DOV_ANGLES = [0]
- NCV = 8
- SCORING = ['accuracy', 'balanced_accuracy', 'f1']
- REFIT_SCORING = balanced_accuracy
- PARAM_GRID = [{'est__n_estimators': [50, 100, 150, 200, 300], 'est__min_samples_split': [2, 5, 10], 'est__min_samples_leaf': [1, 5, 10], 'est__max_features': ['sqrt', 'log2', None], 'est__bootstrap': [False], 'est__n_jobs': [-1], 'est__random_state': [42], 'est__max_samples': [0.01, 0.5, 0.09]}, {'est__n_estimators': [50, 100, 150, 200, 300], 'est__min_samples_split': [2, 5, 10], 'est__min_samples_leaf': [1, 5, 10], 'est__max_features': ['sqrt', 'log2', None], 'est__bootstrap': [True], 'est__oob_score': [True, False], 'est__n_jobs': [-1], 'est__random_state': [42], 'est__max_samples': [0.01, 0.5, 0.09]}]
- TRAIN_SET_SESSION = ['trial1']
- TEST_SET_SESSION = ['trial2', 'trial3']

## Loaded CSV
- 2021-12-01_mac_48000Hz_w1_N2^12_overlap80.csv

## Estimator
### Type
- resampler = RandomOverSampler
- estimator = ExtraTreesClassifier

### Arguments for hyperparameter search
- resampler = RandomOverSampler
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
	- shrinkage = None
	- n_features_in_ = 36
	- sampling_strategy_ = OrderedDict([(1, 54)])
	- shrinkage_ = None
	- sample_indices_ = [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23
 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47
 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71
 48 24 56 32 48 16 48 56 32 24 56 56 16 40 32  8 56 40  8 32  0 40 64  0
 16 48 24 64 16 32 16 48 32 64 48  8 24 64  8 64 32  8 24 48 56 16  0 24
  8 56 24  8 40 40]

- best_estimator
	- base_estimator = ExtraTreeClassifier()
	- n_estimators = 200
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
	- min_samples_leaf = 10
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
	- oob_decision_function_ = [[0.27740523 0.72259477]
 [0.41910096 0.58089904]
 [0.64663221 0.35336779]
 [0.6009983  0.3990017 ]
 [0.77858969 0.22141031]
 [0.5636608  0.4363392 ]
 [0.50209754 0.49790246]
 [0.30051128 0.69948872]
 [0.24810446 0.75189554]
 [0.32067317 0.67932683]
 [0.73358228 0.26641772]
 [0.7611778  0.2388222 ]
 [0.79624616 0.20375384]
 [0.74538965 0.25461035]
 [0.48783874 0.51216126]
 [0.23621625 0.76378375]
 [0.32168181 0.67831819]
 [0.39874941 0.60125059]
 [0.64411529 0.35588471]
 [0.76726667 0.23273333]
 [0.86367873 0.13632127]
 [0.61045518 0.38954482]
 [0.31559517 0.68440483]
 [0.41682513 0.58317487]
 [0.34861512 0.65138488]
 [0.63462291 0.36537709]
 [0.5878189  0.4121811 ]
 [0.78514004 0.21485996]
 [0.66293116 0.33706884]
 [0.87893017 0.12106983]
 [0.53254555 0.46745445]
 [0.44528091 0.55471909]
 [0.35856702 0.64143298]
 [0.56148909 0.43851091]
 [0.74828891 0.25171109]
 [0.76381163 0.23618837]
 [0.78806903 0.21193097]
 [0.8594334  0.1405666 ]
 [0.63626314 0.36373686]
 [0.24892555 0.75107445]
 [0.29081493 0.70918507]
 [0.33286657 0.66713343]
 [0.62225879 0.37774121]
 [0.83736066 0.16263934]
 [0.61952919 0.38047081]
 [0.77323149 0.22676851]
 [0.60053889 0.39946111]
 [0.46342832 0.53657168]
 [0.34447497 0.65552503]
 [0.61121091 0.38878909]
 [0.80896246 0.19103754]
 [0.86212827 0.13787173]
 [0.73774869 0.26225131]
 [0.85584375 0.14415625]
 [0.78124728 0.21875272]
 [0.47070312 0.52929688]
 [0.39225219 0.60774781]
 [0.79376622 0.20623378]
 [0.76547589 0.23452411]
 [0.74530553 0.25469447]
 [0.71187526 0.28812474]
 [0.68859877 0.31140123]
 [0.69675472 0.30324528]
 [0.56804888 0.43195112]
 [0.52559662 0.47440338]
 [0.69087794 0.30912206]
 [0.84731479 0.15268521]
 [0.68807015 0.31192985]
 [0.85913007 0.14086993]
 [0.84747271 0.15252729]
 [0.76657654 0.23342346]
 [0.60075886 0.39924114]
 [0.33058276 0.66941724]
 [0.34120681 0.65879319]
 [0.40471236 0.59528764]
 [0.36892403 0.63107597]
 [0.33482439 0.66517561]
 [0.30503608 0.69496392]
 [0.35967827 0.64032173]
 [0.37760645 0.62239355]
 [0.36618899 0.63381101]
 [0.34617128 0.65382872]
 [0.3900909  0.6099091 ]
 [0.39887043 0.60112957]
 [0.32244969 0.67755031]
 [0.28476092 0.71523908]
 [0.3923091  0.6076909 ]
 [0.25238363 0.74761637]
 [0.41849518 0.58150482]
 [0.26717983 0.73282017]
 [0.24074631 0.75925369]
 [0.36070179 0.63929821]
 [0.27315585 0.72684415]
 [0.2724231  0.7275769 ]
 [0.49713387 0.50286613]
 [0.28943984 0.71056016]
 [0.32948569 0.67051431]
 [0.35328873 0.64671127]
 [0.34530725 0.65469275]
 [0.53093121 0.46906879]
 [0.3303547  0.6696453 ]
 [0.35649716 0.64350284]
 [0.31324446 0.68675554]
 [0.33787835 0.66212165]
 [0.35627544 0.64372456]
 [0.5070798  0.4929202 ]
 [0.35292162 0.64707838]
 [0.26528826 0.73471174]
 [0.34192224 0.65807776]
 [0.50100698 0.49899302]
 [0.24136022 0.75863978]
 [0.54727678 0.45272322]
 [0.34927071 0.65072929]
 [0.2505878  0.7494122 ]
 [0.37654466 0.62345534]
 [0.34275666 0.65724334]
 [0.38287068 0.61712932]
 [0.32519886 0.67480114]
 [0.28313274 0.71686726]
 [0.35600946 0.64399054]
 [0.25109295 0.74890705]
 [0.40163435 0.59836565]
 [0.35559218 0.64440782]
 [0.24139647 0.75860353]
 [0.28820553 0.71179447]
 [0.27243537 0.72756463]]
	- oob_score_ = 0.8571428571428571

#### Importance of features
- gp_auc_std = 0.06849980629879487
- gp_max_val_max = 0.06638188260612166
- gp_max_val_mean = 0.05863089671224084
- gp_auc_range = 0.05487402251612395
- gp_max_val_min = 0.05478426883514352
- gp_auc_max = 0.05408026317586903
- gp_max_val_std = 0.050758791933001514
- gp_auc_min = 0.047220389436122126
- coe1[0] = 0.04633695030364524
- gp_max_ix_std = 0.03642884745622217
- gp_max_val_range = 0.03324228743096552
- coe1[1] = 0.032171200114253416
- gp_auc_mean = 0.029203258478407736
- tdoa_std = 0.0264941607589113
- tdoa_range = 0.026037530590310193
- diff_auc = 0.025302642391909984
- coe3[3] = 0.024878503783717247
- low_power = 0.024532968786563022
- tdoa_min = 0.02288265020075738
- ratio_max_to_9th_ave_peaks = 0.022848974522763334
- tdoa_max = 0.02242625928456896
- gp_max_ix_min = 0.02198484868341708
- gp_max_ix_range = 0.021671783780019674
- gp_max_ix_mean = 0.020140222869739422
- tdoa_mean = 0.01740875879368254
- diff_std = 0.015579747090287923
- gp_max_ix_max = 0.015511089188529217
- coe3[2] = 0.014463488420448213
- high_power = 0.012388958234782336
- srmr = 0.010961887107189854
- ac_std = 0.009715498769264735
- ratio_max_to_10ms_ave_peaks = 0.007510746891712173
- ac_auc = 0.004199819569022712
- hlbr = 0.00044659498549087594
- coe3[0] = 0.0
- coe3[1] = 0.0

## Evaluation
cv = 8
### accuracy
- Scores = [ 0.8333333333333334, 0.8333333333333334, 0.8888888888888888, 0.8888888888888888, 0.8888888888888888, 0.8888888888888888, 0.8888888888888888, 0.8888888888888888 ]
- Mean = 0.875
- Standard deviation = 0.02405626121623437

### balanced_accuracy
- Scores = [ 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5 ]
- Mean = 0.5
- Standard deviation = 0.0

### f1
- Scores = [ 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0 ]
- Mean = 0.0
- Standard deviation = 0.0

### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 126 | 0 |
| Actual Positive | 18 | 0 |

      