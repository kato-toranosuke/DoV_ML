# ExtraTreesClassifier_NoResampler_2021-12-29_no0
## Constants
- CSV_PATH = ../out/csv/experiment
- OUTPUT_PATH = ../out/experiment_result/data_of_2021-12-27/NoAGC-45angle-under5m
- FEATURE_ATTRBS = ['low_power', 'high_power', 'hlbr', 'coe1[0]', 'coe1[1]', 'coe3[0]', 'coe3[1]', 'coe3[2]', 'coe3[3]', 'ratio_max_to_10ms_ave_peaks', 'ratio_max_to_9th_ave_peaks', 'ac_std', 'ac_auc', 'diff_std', 'diff_auc', 'srmr', 'gp_max_val_std', 'gp_max_val_range', 'gp_max_val_min', 'gp_max_val_max', 'gp_max_val_mean', 'gp_max_ix_std', 'gp_max_ix_range', 'gp_max_ix_min', 'gp_max_ix_max', 'gp_max_ix_mean', 'gp_auc_std', 'gp_auc_range', 'gp_auc_min', 'gp_auc_max', 'gp_auc_mean', 'tdoa_std', 'tdoa_range', 'tdoa_min', 'tdoa_max', 'tdoa_mean']
- LABEL_ATTRB = ['facing2']
- FACING_DOV_ANGLES = [1, 2]
- NCV = 8
- SCORING = ['accuracy', 'balanced_accuracy', 'f1']
- REFIT_SCORING = balanced_accuracy
- PARAM_GRID = [{'est__n_estimators': [50, 100, 150, 200, 300], 'est__min_samples_split': [2, 5, 10], 'est__min_samples_leaf': [1, 5, 10], 'est__max_features': ['sqrt', 'log2', None], 'est__bootstrap': [False], 'est__n_jobs': [-1], 'est__random_state': [42], 'est__max_samples': [0.01, 0.5, 0.09]}, {'est__n_estimators': [50, 100, 150, 200, 300], 'est__min_samples_split': [2, 5, 10], 'est__min_samples_leaf': [1, 5, 10], 'est__max_features': ['sqrt', 'log2', None], 'est__bootstrap': [True], 'est__oob_score': [True, False], 'est__n_jobs': [-1], 'est__random_state': [42], 'est__max_samples': [0.01, 0.5, 0.09]}]
- TRAIN_SET_SESSION = ['trial1', 'trial2']
- TEST_SET_SESSION = ['trial3', 'trial4', 'trial5']
- DISTANCE = [1, 3, 5]
- AGC_STATUS = ['NoAGC']

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
	- n_estimators = 100
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
	- oob_decision_function_ = [[0.01694915 0.98305085]
 [0.01639344 0.98360656]
 [0.03174603 0.96825397]
 [0.01666667 0.98333333]
 [0.54545455 0.45454545]
 [0.57575758 0.42424242]
 [0.92424242 0.07575758]
 [0.96296296 0.03703704]
 [0.92982456 0.07017544]
 [0.98275862 0.01724138]
 [0.04615385 0.95384615]
 [0.03076923 0.96923077]
 [0.18032787 0.81967213]
 [0.03508772 0.96491228]
 [0.8        0.2       ]
 [0.54098361 0.45901639]
 [1.         0.        ]
 [0.98507463 0.01492537]
 [1.         0.        ]
 [0.96610169 0.03389831]
 [0.18309859 0.81690141]
 [0.07352941 0.92647059]
 [0.10909091 0.89090909]
 [0.140625   0.859375  ]
 [0.98       0.02      ]
 [0.93220339 0.06779661]
 [1.         0.        ]
 [1.         0.        ]
 [1.         0.        ]
 [1.         0.        ]
 [0.05263158 0.94736842]
 [0.05172414 0.94827586]
 [0.01612903 0.98387097]
 [0.03030303 0.96969697]
 [0.29032258 0.70967742]
 [0.21428571 0.78571429]
 [0.81481481 0.18518519]
 [0.81132075 0.18867925]
 [0.98181818 0.01818182]
 [0.73770492 0.26229508]
 [0.2037037  0.7962963 ]
 [0.05084746 0.94915254]
 [0.10714286 0.89285714]
 [0.01492537 0.98507463]
 [0.26153846 0.73846154]
 [0.10447761 0.89552239]
 [0.68333333 0.31666667]
 [0.50793651 0.49206349]
 [1.         0.        ]
 [1.         0.        ]
 [0.64179104 0.35820896]
 [0.37878788 0.62121212]
 [0.19298246 0.80701754]
 [0.140625   0.859375  ]
 [0.35087719 0.64912281]
 [0.15942029 0.84057971]
 [0.96296296 0.03703704]
 [0.94736842 0.05263158]
 [1.         0.        ]
 [1.         0.        ]
 [0.72222222 0.27777778]
 [0.625      0.375     ]
 [0.15873016 0.84126984]
 [0.03389831 0.96610169]
 [0.08928571 0.91071429]
 [0.07042254 0.92957746]
 [0.17241379 0.82758621]
 [0.10294118 0.89705882]
 [0.64516129 0.35483871]
 [0.5483871  0.4516129 ]
 [0.38181818 0.61818182]
 [0.19230769 0.80769231]
 [0.41538462 0.58461538]
 [0.09677419 0.90322581]
 [0.16363636 0.83636364]
 [0.         1.        ]
 [0.01639344 0.98360656]
 [0.         1.        ]
 [0.56521739 0.43478261]
 [0.60606061 0.39393939]
 [0.93220339 0.06779661]
 [0.8852459  0.1147541 ]
 [0.17142857 0.82857143]
 [0.06451613 0.93548387]
 [0.03636364 0.96363636]
 [0.         1.        ]
 [0.06666667 0.93333333]
 [0.41818182 0.58181818]
 [0.89473684 0.10526316]
 [0.96774194 0.03225806]
 [0.96491228 0.03508772]
 [0.96226415 0.03773585]
 [0.68253968 0.31746032]
 [0.62745098 0.37254902]
 [0.03225806 0.96774194]
 [0.05555556 0.94444444]
 [0.04918033 0.95081967]
 [0.03278689 0.96721311]
 [0.2295082  0.7704918 ]
 [0.30357143 0.69642857]
 [1.         0.        ]
 [1.         0.        ]
 [0.7704918  0.2295082 ]
 [0.671875   0.328125  ]
 [0.06557377 0.93442623]
 [0.         1.        ]
 [0.         1.        ]
 [0.         1.        ]
 [0.09433962 0.90566038]
 [0.         1.        ]
 [0.96825397 0.03174603]
 [0.93220339 0.06779661]
 [0.87692308 0.12307692]
 [0.83928571 0.16071429]
 [0.18965517 0.81034483]
 [0.05660377 0.94339623]
 [0.04918033 0.95081967]
 [0.03448276 0.96551724]
 [0.01818182 0.98181818]
 [0.13333333 0.86666667]]
	- oob_score_ = 0.975

#### Importance of features
- gp_max_val_mean = 0.08583330934581773
- gp_auc_min = 0.08519480355526006
- gp_max_val_min = 0.07696829448213749
- gp_auc_mean = 0.06065974468177387
- gp_auc_max = 0.05809783259545815
- gp_max_val_max = 0.0570266729097085
- diff_auc = 0.0509835629715556
- hlbr = 0.046206866049393225
- srmr = 0.04257474482665821
- diff_std = 0.03981894412547562
- high_power = 0.0357030182341697
- tdoa_max = 0.029526157231536152
- gp_max_ix_mean = 0.026982440884303165
- gp_max_ix_max = 0.02536282388594982
- ratio_max_to_10ms_ave_peaks = 0.025180985737663083
- gp_auc_std = 0.020706101796150043
- gp_max_ix_std = 0.018183657107414798
- coe1[0] = 0.018166611496946428
- gp_max_val_std = 0.01765236038817239
- gp_max_val_range = 0.017446352466196503
- coe1[1] = 0.016938851307564767
- tdoa_mean = 0.016145739738022948
- ac_std = 0.016074016209513764
- low_power = 0.015839293975769456
- gp_max_ix_range = 0.01379344298902383
- gp_auc_range = 0.01187274150363736
- tdoa_range = 0.011609326931756127
- coe3[3] = 0.010681259849336449
- gp_max_ix_min = 0.01022668368431086
- tdoa_min = 0.009884672245246641
- tdoa_std = 0.008252035054689898
- ac_auc = 0.008178392898207978
- coe3[2] = 0.007407404527536698
- ratio_max_to_9th_ave_peaks = 0.004820854313642903
- coe3[0] = 0.0
- coe3[1] = 0.0

## Evaluation
cv = 8
### accuracy
- Scores = [ 0.9130434782608695, 1.0, 1.0, 0.9545454545454546, 1.0, 0.8636363636363636, 1.0, 0.9545454545454546 ]
- Mean = 0.9607213438735178
- Standard deviation = 0.04736323308144869

### balanced_accuracy
- Scores = [ 0.9, 1.0, 1.0, 0.95, 1.0, 0.8583333333333334, 1.0, 0.9583333333333333 ]
- Mean = 0.9583333333333333
- Standard deviation = 0.050518148554092236

### f1
- Scores = [ 0.9285714285714286, 1.0, 1.0, 0.9600000000000001, 1.0, 0.8799999999999999, 1.0, 0.9565217391304348 ]
- Mean = 0.9656366459627329
- Standard deviation = 0.04114863178017592

### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 76 | 5 |
| Actual Positive | 2 | 96 |

      