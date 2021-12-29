# ExtraTreesClassifier_SMOTETomek_2021-12-29_no6
## Constants
- CSV_PATH = ../out/csv/experiment
- OUTPUT_PATH = ../out/experiment_result/data_of_2021-12-27/NoAGC-0angle-3m
- FEATURE_ATTRBS = ['low_power', 'high_power', 'hlbr', 'coe1[0]', 'coe1[1]', 'coe3[0]', 'coe3[1]', 'coe3[2]', 'coe3[3]', 'ratio_max_to_10ms_ave_peaks', 'ratio_max_to_9th_ave_peaks', 'ac_std', 'ac_auc', 'diff_std', 'diff_auc', 'srmr', 'gp_max_val_std', 'gp_max_val_range', 'gp_max_val_min', 'gp_max_val_max', 'gp_max_val_mean', 'gp_max_ix_std', 'gp_max_ix_range', 'gp_max_ix_min', 'gp_max_ix_max', 'gp_max_ix_mean', 'gp_auc_std', 'gp_auc_range', 'gp_auc_min', 'gp_auc_max', 'gp_auc_mean', 'tdoa_std', 'tdoa_range', 'tdoa_min', 'tdoa_max', 'tdoa_mean']
- LABEL_ATTRB = ['facing']
- FACING_DOV_ANGLES = [1]
- NCV = 8
- SCORING = ['accuracy', 'balanced_accuracy', 'f1']
- REFIT_SCORING = balanced_accuracy
- PARAM_GRID = [{'est__n_estimators': [50, 100, 150, 200, 300], 'est__min_samples_split': [2, 5, 10], 'est__min_samples_leaf': [1, 5, 10], 'est__max_features': ['sqrt', 'log2', None], 'est__bootstrap': [False], 'est__n_jobs': [-1], 'est__random_state': [42], 'est__max_samples': [0.01, 0.5, 0.09]}, {'est__n_estimators': [50, 100, 150, 200, 300], 'est__min_samples_split': [2, 5, 10], 'est__min_samples_leaf': [1, 5, 10], 'est__max_features': ['sqrt', 'log2', None], 'est__bootstrap': [True], 'est__oob_score': [True, False], 'est__n_jobs': [-1], 'est__random_state': [42], 'est__max_samples': [0.01, 0.5, 0.09]}]
- TRAIN_SET_SESSION = ['trial1', 'trial2']
- TEST_SET_SESSION = ['trial3', 'trial4', 'trial5']
- DISTANCE = [3]
- AGC_STATUS = ['NoAGC']

## Loaded CSV
- 2021-12-27_raspi_48000Hz_w1_N2^12_overlap80_new.csv

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
	- min_samples_leaf = 5
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
	- oob_decision_function_ = [[0.37750126 0.62249874]
 [0.56378145 0.43621855]
 [0.4237841  0.5762159 ]
 [0.65785759 0.34214241]
 [0.6983743  0.3016257 ]
 [0.63106329 0.36893671]
 [0.52850482 0.47149518]
 [0.4389041  0.5610959 ]
 [0.49575236 0.50424764]
 [0.69585524 0.30414476]
 [0.67306027 0.32693973]
 [0.66727818 0.33272182]
 [0.69555454 0.30444546]
 [0.51931575 0.48068425]
 [0.51970398 0.48029602]
 [0.3441707  0.6558293 ]
 [0.41134217 0.58865783]
 [0.37361284 0.62638716]
 [0.61070269 0.38929731]
 [0.68183841 0.31816159]
 [0.74054088 0.25945912]
 [0.67874119 0.32125881]
 [0.46502074 0.53497926]
 [0.24602092 0.75397908]
 [0.3741194  0.6258806 ]
 [0.4288961  0.5711039 ]
 [0.50746423 0.49253577]
 [0.3651962  0.6348038 ]
 [0.50610109 0.49389891]
 [0.29134199 0.70865801]
 [0.47081869 0.52918131]
 [0.30299795 0.69700205]
 [0.30056705 0.69943295]
 [0.55174269 0.44825731]
 [0.43372358 0.56627642]
 [0.36177551 0.63822449]
 [0.40609751 0.59390249]
 [0.30552137 0.69447863]
 [0.36463268 0.63536732]
 [0.35722    0.64278   ]
 [0.25852381 0.74147619]
 [0.31143389 0.68856611]
 [0.37401358 0.62598642]
 [0.47077988 0.52922012]]
	- oob_score_ = 0.7727272727272727

#### Importance of features
- srmr = 0.11879699248120298
- gp_max_val_max = 0.11139766639099569
- low_power = 0.09199660078637331
- gp_auc_max = 0.08971811529271208
- high_power = 0.05
- gp_auc_range = 0.05
- tdoa_std = 0.04873194786896795
- coe1[0] = 0.03930096424956623
- ac_auc = 0.029257713730927826
- gp_max_val_std = 0.029183386242324916
- gp_auc_std = 0.02599841345864093
- coe3[2] = 0.025437182410053986
- ratio_max_to_10ms_ave_peaks = 0.02502209663595457
- hlbr = 0.025
- gp_max_val_mean = 0.025
- gp_max_ix_mean = 0.025
- gp_auc_mean = 0.025
- tdoa_max = 0.025
- diff_std = 0.02497790336404543
- diff_auc = 0.024613220815752464
- gp_auc_min = 0.024365482233502538
- coe3[3] = 0.02222372346404947
- ac_std = 0.015826342281879194
- coe1[1] = 0.01018518518518518
- gp_max_val_min = 0.009173657718120804
- tdoa_range = 0.007051282051282051
- gp_max_ix_range = 0.0012680521310320532
- ratio_max_to_9th_ave_peaks = 0.0004740712074303397
- coe3[0] = 0.0
- coe3[1] = 0.0
- gp_max_val_range = 0.0
- gp_max_ix_std = 0.0
- gp_max_ix_min = 0.0
- gp_max_ix_max = 0.0
- tdoa_min = 0.0
- tdoa_mean = 0.0

## Evaluation
cv = 8
### accuracy
- Scores = [ 0.75, 0.875, 0.875, 0.875, 0.5714285714285714, 0.7142857142857143, 1.0, 0.14285714285714285 ]
- Mean = 0.7254464285714286
- Standard deviation = 0.2515794336105722

### balanced_accuracy
- Scores = [ 0.8333333333333333, 0.75, 0.9166666666666667, 0.75, 0.75, 0.8333333333333333, 1.0, 0.5 ]
- Mean = 0.7916666666666666
- Standard deviation = 0.13819269959814165

### f1
- Scores = [ 0.6666666666666666, 0.6666666666666666, 0.8, 0.6666666666666666, 0.4, 0.5, 1.0, 0.25 ]
- Mean = 0.6187499999999999
- Standard deviation = 0.21880951571324925

### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 34 | 14 |
| Actual Positive | 2 | 10 |

      