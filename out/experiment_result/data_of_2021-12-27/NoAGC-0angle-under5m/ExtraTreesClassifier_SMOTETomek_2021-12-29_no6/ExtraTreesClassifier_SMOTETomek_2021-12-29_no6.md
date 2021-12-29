# ExtraTreesClassifier_SMOTETomek_2021-12-29_no6
## Constants
- CSV_PATH = ../out/csv/experiment
- OUTPUT_PATH = ../out/experiment_result/data_of_2021-12-27/NoAGC-0angle-under5m
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
	- max_samples = 0.09
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
	- oob_decision_function_ = [[0.22727273 0.77272727]
 [0.28571429 0.71428571]
 [0.30612245 0.69387755]
 [0.35555556 0.64444444]
 [0.46666667 0.53333333]
 [0.85106383 0.14893617]
 [0.74468085 0.25531915]
 [0.79166667 0.20833333]
 [0.93333333 0.06666667]
 [0.37777778 0.62222222]
 [0.17391304 0.82608696]
 [0.65217391 0.34782609]
 [0.63043478 0.36956522]
 [0.88372093 0.11627907]
 [0.84444444 0.15555556]
 [0.9787234  0.0212766 ]
 [0.95744681 0.04255319]
 [0.91489362 0.08510638]
 [0.3902439  0.6097561 ]
 [0.31111111 0.68888889]
 [0.44680851 0.55319149]
 [0.46808511 0.53191489]
 [0.91111111 0.08888889]
 [0.91111111 0.08888889]
 [0.97674419 0.02325581]
 [1.         0.        ]
 [0.95744681 0.04255319]
 [0.93333333 0.06666667]
 [0.20833333 0.79166667]
 [0.28888889 0.71111111]
 [0.32653061 0.67346939]
 [0.36956522 0.63043478]
 [0.59574468 0.40425532]
 [0.6        0.4       ]
 [0.82608696 0.17391304]
 [0.75555556 0.24444444]
 [0.46808511 0.53191489]
 [0.63043478 0.36956522]
 [0.77272727 0.22727273]
 [1.         0.        ]
 [1.         0.        ]
 [0.71111111 0.28888889]
 [0.68888889 0.31111111]
 [0.58139535 0.41860465]
 [0.33333333 0.66666667]
 [1.         0.        ]
 [1.         0.        ]
 [0.46808511 0.53191489]
 [0.26190476 0.73809524]
 [0.31818182 0.68181818]
 [0.33333333 0.66666667]
 [0.29787234 0.70212766]
 [0.41304348 0.58695652]
 [0.39130435 0.60869565]
 [0.35555556 0.64444444]
 [0.68888889 0.31111111]
 [0.65116279 0.34883721]
 [0.63636364 0.36363636]
 [0.48888889 0.51111111]
 [0.54347826 0.45652174]
 [0.63414634 0.36585366]
 [0.53658537 0.46341463]
 [0.72916667 0.27083333]
 [0.82608696 0.17391304]
 [0.55319149 0.44680851]
 [0.36170213 0.63829787]
 [0.42222222 0.57777778]
 [0.31914894 0.68085106]
 [0.56521739 0.43478261]
 [0.60869565 0.39130435]
 [0.92857143 0.07142857]
 [0.90909091 0.09090909]
 [0.52173913 0.47826087]
 [0.25531915 0.74468085]
 [0.31914894 0.68085106]
 [0.2173913  0.7826087 ]
 [0.39130435 0.60869565]
 [0.36363636 0.63636364]
 [0.95744681 0.04255319]
 [0.93478261 0.06521739]
 [0.88636364 0.11363636]
 [0.29545455 0.70454545]
 [0.45833333 0.54166667]
 [0.6        0.4       ]
 [0.97619048 0.02380952]
 [0.91111111 0.08888889]
 [0.7755102  0.2244898 ]
 [0.79069767 0.20930233]
 [0.53333333 0.46666667]
 [0.37777778 0.62222222]
 [0.24444444 0.75555556]
 [0.27659574 0.72340426]
 [0.36956522 0.63043478]
 [0.44444444 0.55555556]
 [0.26666667 0.73333333]
 [0.26086957 0.73913043]
 [0.47916667 0.52083333]
 [0.4047619  0.5952381 ]
 [0.31914894 0.68085106]
 [0.35555556 0.64444444]
 [0.33333333 0.66666667]
 [0.37777778 0.62222222]
 [0.23404255 0.76595745]
 [0.29787234 0.70212766]
 [0.26829268 0.73170732]
 [0.23404255 0.76595745]
 [0.29787234 0.70212766]
 [0.34042553 0.65957447]
 [0.24444444 0.75555556]
 [0.25       0.75      ]
 [0.25       0.75      ]
 [0.275      0.725     ]
 [0.43478261 0.56521739]
 [0.29787234 0.70212766]
 [0.25581395 0.74418605]
 [0.27906977 0.72093023]
 [0.34042553 0.65957447]
 [0.42222222 0.57777778]
 [0.25       0.75      ]
 [0.2826087  0.7173913 ]
 [0.34782609 0.65217391]
 [0.23404255 0.76595745]
 [0.31111111 0.68888889]
 [0.31111111 0.68888889]
 [0.27083333 0.72916667]
 [0.57777778 0.42222222]
 [0.2173913  0.7826087 ]
 [0.26666667 0.73333333]
 [0.25       0.75      ]
 [0.27083333 0.72916667]
 [0.3        0.7       ]
 [0.36956522 0.63043478]
 [0.27659574 0.72340426]
 [0.24489796 0.75510204]
 [0.27659574 0.72340426]
 [0.27659574 0.72340426]
 [0.28571429 0.71428571]
 [0.29787234 0.70212766]
 [0.3125     0.6875    ]
 [0.23404255 0.76595745]
 [0.27659574 0.72340426]
 [0.34090909 0.65909091]
 [0.54347826 0.45652174]
 [0.29166667 0.70833333]
 [0.17021277 0.82978723]
 [0.19148936 0.80851064]
 [0.34090909 0.65909091]
 [0.28888889 0.71111111]
 [0.41304348 0.58695652]
 [0.27659574 0.72340426]
 [0.2826087  0.7173913 ]
 [0.19148936 0.80851064]
 [0.44186047 0.55813953]
 [0.25       0.75      ]]
	- oob_score_ = 0.8051948051948052

#### Importance of features
- gp_auc_min = 0.06787063921528208
- tdoa_max = 0.056048137048137034
- ratio_max_to_10ms_ave_peaks = 0.05064580498866214
- high_power = 0.049766414141414146
- gp_auc_range = 0.04719789734075448
- gp_auc_max = 0.0459961334961335
- low_power = 0.044170479916908485
- gp_auc_mean = 0.03964547225261511
- hlbr = 0.03813131313131313
- diff_auc = 0.03748505462791177
- ratio_max_to_9th_ave_peaks = 0.03715263605442177
- gp_max_val_std = 0.03699084865751532
- gp_max_val_max = 0.03686464646464646
- gp_max_val_min = 0.032929896492396506
- gp_max_val_mean = 0.029017857142857144
- gp_auc_std = 0.028720238095238094
- ac_auc = 0.02857875523946953
- srmr = 0.027995580808080803
- coe3[2] = 0.02725025510204082
- ac_std = 0.027192551892551896
- gp_max_ix_max = 0.02509342278092278
- coe1[0] = 0.024775222462722457
- diff_std = 0.022940251723585058
- gp_max_ix_min = 0.02076488095238095
- coe1[1] = 0.02014541014541014
- tdoa_min = 0.016631944444444442
- gp_max_val_range = 0.014705026455026457
- gp_max_ix_range = 0.012525072150072154
- coe3[3] = 0.011333333333333332
- gp_max_ix_std = 0.009860101010101008
- gp_max_ix_mean = 0.009071150608650609
- tdoa_mean = 0.009002525252525252
- tdoa_range = 0.007510204081632654
- tdoa_std = 0.00599084249084249
- coe3[0] = 0.0
- coe3[1] = 0.0

## Evaluation
cv = 8
### accuracy
- Scores = [ 0.782608695652174, 0.8260869565217391, 0.782608695652174, 0.9090909090909091, 0.4090909090909091, 0.8636363636363636, 0.8181818181818182, 0.6818181818181818 ]
- Mean = 0.7591403162055336
- Standard deviation = 0.14619643694179232

### balanced_accuracy
- Scores = [ 0.8611111111111112, 0.6, 0.788888888888889, 0.8, 0.5416666666666666, 0.9166666666666667, 0.8888888888888888, 0.7083333333333333 ]
- Mean = 0.7631944444444445
- Standard deviation = 0.12731460437693048

### f1
- Scores = [ 0.6666666666666666, 0.33333333333333337, 0.6153846153846154, 0.7499999999999999, 0.31578947368421056, 0.7272727272727273, 0.6666666666666666, 0.46153846153846156 ]
- Mean = 0.5670814930683352
- Standard deviation = 0.1621007516989527

### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 109 | 34 |
| Actual Positive | 9 | 27 |

      