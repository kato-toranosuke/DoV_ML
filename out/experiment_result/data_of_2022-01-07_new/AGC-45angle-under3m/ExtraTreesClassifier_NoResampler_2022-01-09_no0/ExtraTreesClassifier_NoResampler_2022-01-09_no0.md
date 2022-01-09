# ExtraTreesClassifier_NoResampler_2022-01-09_no0
## Constants
- CSV_PATH = ../out/csv/experiment
- OUTPUT_PATH = ../out/experiment_result/data_of_2022-01-07_new/AGC-45angle-under3m
- FEATURE_ATTRBS = ['low_power', 'high_power', 'hlbr', 'coe1[0]', 'coe1[1]', 'coe3[0]', 'coe3[1]', 'coe3[2]', 'coe3[3]', 'ratio_max_to_10ms_ave_peaks', 'ratio_max_to_9th_ave_peaks', 'ac_std', 'ac_auc', 'diff_std', 'diff_auc', 'srmr', 'gp_max_val_std', 'gp_max_val_range', 'gp_max_val_min', 'gp_max_val_max', 'gp_max_val_mean', 'gp_max_ix_std', 'gp_max_ix_range', 'gp_max_ix_min', 'gp_max_ix_max', 'gp_max_ix_mean', 'gp_auc_std', 'gp_auc_range', 'gp_auc_min', 'gp_auc_max', 'gp_auc_mean', 'tdoa_std', 'tdoa_range', 'tdoa_min', 'tdoa_max', 'tdoa_mean']
- LABEL_ATTRB = ['facing2']
- FACING_DOV_ANGLES = [1, 2]
- NCV = 8
- SCORING = ['accuracy', 'balanced_accuracy', 'f1']
- REFIT_SCORING = balanced_accuracy
- PARAM_GRID = [{'est__n_estimators': [50, 100, 150, 200, 300], 'est__min_samples_split': [2, 5, 10], 'est__min_samples_leaf': [1, 5, 10], 'est__max_features': ['sqrt', 'log2', None], 'est__bootstrap': [False], 'est__n_jobs': [-1], 'est__random_state': [42], 'est__max_samples': [0.01, 0.5, 0.09]}, {'est__n_estimators': [50, 100, 150, 200, 300], 'est__min_samples_split': [2, 5, 10], 'est__min_samples_leaf': [1, 5, 10], 'est__max_features': ['sqrt', 'log2', None], 'est__bootstrap': [True], 'est__oob_score': [True, False], 'est__n_jobs': [-1], 'est__random_state': [42], 'est__max_samples': [0.01, 0.5, 0.09]}]
- TRAIN_SET_SESSION = ['trial1', 'trial2']
- TEST_SET_SESSION = ['trial3', 'trial4', 'trial5']
- DISTANCE = [1, 3]
- AGC_STATUS = ['AGC']

## Loaded CSV
- 2021-12-27_raspi_48000Hz_w1_N2^12_overlap80_with2022-01-07.csv

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
	- n_estimators = 50
	- estimator_params = ('criterion', 'max_depth', 'min_samples_split', 'min_samples_leaf', 'min_weight_fraction_leaf', 'max_features', 'max_leaf_nodes', 'min_impurity_decrease', 'random_state', 'ccp_alpha')
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
	- ccp_alpha = 0.0
	- n_features_in_ = 36
	- n_outputs_ = 1
	- classes_ = [0 1]
	- n_classes_ = 2
	- base_estimator_ = ExtraTreeClassifier()
	- oob_decision_function_ = [[0.125      0.875     ]
 [0.03030303 0.96969697]
 [0.12903226 0.87096774]
 [0.20833333 0.79166667]
 [0.03448276 0.96551724]
 [0.19354839 0.80645161]
 [0.97297297 0.02702703]
 [0.93333333 0.06666667]
 [1.         0.        ]
 [1.         0.        ]
 [0.03030303 0.96969697]
 [0.09375    0.90625   ]
 [0.17241379 0.82758621]
 [0.03448276 0.96551724]
 [0.70967742 0.29032258]
 [0.6        0.4       ]
 [1.         0.        ]
 [0.97222222 0.02777778]
 [1.         0.        ]
 [1.         0.        ]
 [0.1875     0.8125    ]
 [0.10810811 0.89189189]
 [0.07407407 0.92592593]
 [0.09677419 0.90322581]
 [0.16       0.84      ]
 [0.16129032 0.83870968]
 [0.64285714 0.35714286]
 [0.85714286 0.14285714]
 [1.         0.        ]
 [0.96969697 0.03030303]
 [0.1025641  0.8974359 ]
 [0.55172414 0.44827586]
 [0.1        0.9       ]
 [0.03448276 0.96551724]
 [0.08333333 0.91666667]
 [0.         1.        ]
 [0.81481481 0.18518519]
 [0.71428571 0.28571429]
 [1.         0.        ]
 [0.96875    0.03125   ]
 [0.92       0.08      ]
 [0.93103448 0.06896552]
 [0.10714286 0.89285714]
 [0.09375    0.90625   ]
 [0.12121212 0.87878788]
 [0.18181818 0.81818182]
 [0.1        0.9       ]
 [0.15151515 0.84848485]
 [0.80645161 0.19354839]
 [0.76923077 0.23076923]
 [0.59459459 0.40540541]
 [0.93939394 0.06060606]
 [0.51724138 0.48275862]
 [0.42424242 0.57575758]
 [0.03846154 0.96153846]
 [0.         1.        ]
 [0.03846154 0.96153846]
 [0.         1.        ]
 [0.82142857 0.17857143]
 [0.80645161 0.19354839]
 [1.         0.        ]
 [1.         0.        ]
 [0.58064516 0.41935484]
 [0.96428571 0.03571429]
 [0.15384615 0.84615385]
 [0.08571429 0.91428571]
 [0.13333333 0.86666667]
 [0.02857143 0.97142857]
 [0.12903226 0.87096774]
 [0.06666667 0.93333333]
 [0.85185185 0.14814815]
 [1.         0.        ]
 [0.97058824 0.02941176]
 [0.81481481 0.18518519]
 [0.         1.        ]
 [0.         1.        ]
 [0.         1.        ]
 [0.         1.        ]
 [0.02777778 0.97222222]
 [0.02941176 0.97058824]
 [1.         0.        ]
 [1.         0.        ]
 [1.         0.        ]
 [0.96969697 0.03030303]
 [0.83333333 0.16666667]
 [0.81818182 0.18181818]
 [0.09090909 0.90909091]
 [0.12       0.88      ]
 [0.2        0.8       ]
 [0.20588235 0.79411765]
 [0.96666667 0.03333333]
 [1.         0.        ]
 [1.         0.        ]
 [1.         0.        ]
 [0.93103448 0.06896552]
 [0.9        0.1       ]
 [0.18181818 0.81818182]
 [0.39285714 0.60714286]
 [0.         1.        ]
 [0.         1.        ]]
	- oob_score_ = 0.96

#### Importance of features
- gp_auc_min = 0.11942190806391897
- gp_auc_max = 0.11742515586246592
- gp_max_val_max = 0.0948264672019026
- gp_max_val_mean = 0.08962123457795756
- gp_max_val_min = 0.08335982234342401
- srmr = 0.07111200410734705
- gp_auc_mean = 0.06308371557140525
- diff_std = 0.040146563733834455
- diff_auc = 0.03913386471388256
- ratio_max_to_10ms_ave_peaks = 0.029271694670536218
- coe1[1] = 0.026838103271051107
- coe1[0] = 0.026495804132998596
- high_power = 0.02521681490483266
- hlbr = 0.01651214432962334
- tdoa_std = 0.01463191791885532
- low_power = 0.013944671115435731
- gp_max_val_std = 0.012084483417816753
- gp_auc_range = 0.011948437636718547
- ac_auc = 0.010911164650280915
- gp_max_ix_range = 0.00884855790283249
- ac_std = 0.008834142664865001
- tdoa_mean = 0.008457448765273871
- tdoa_min = 0.007620433525605938
- gp_max_val_range = 0.007591976481714202
- coe3[2] = 0.0073885439947059895
- ratio_max_to_9th_ave_peaks = 0.007078465190677469
- gp_max_ix_std = 0.006530727389844919
- gp_max_ix_min = 0.005773726323998061
- tdoa_range = 0.005424342526957346
- gp_auc_std = 0.004880039621415073
- tdoa_max = 0.0045604834650257685
- coe3[3] = 0.0040527386216324245
- gp_max_ix_max = 0.0036362027666375484
- gp_max_ix_mean = 0.0033361985345262933
- coe3[0] = 0.0
- coe3[1] = 0.0

## Evaluation
cv = 8
### accuracy
- Scores = [ 0.8421052631578947, 1.0, 0.9473684210526315, 0.9473684210526315, 1.0, 1.0, 1.0, 1.0 ]
- Mean = 0.9671052631578947
- Standard deviation = 0.05221877587627483

### balanced_accuracy
- Scores = [ 0.8333333333333333, 1.0, 0.95, 0.9444444444444444, 1.0, 1.0, 1.0, 1.0 ]
- Mean = 0.9659722222222222
- Standard deviation = 0.054887476083931935

### f1
- Scores = [ 0.8695652173913044, 1.0, 0.9473684210526316, 0.9523809523809523, 1.0, 1.0, 1.0, 1.0 ]
- Mean = 0.971164323853111
- Standard deviation = 0.04387328281829072

### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 69 | 3 |
| Actual Positive | 1 | 77 |

      