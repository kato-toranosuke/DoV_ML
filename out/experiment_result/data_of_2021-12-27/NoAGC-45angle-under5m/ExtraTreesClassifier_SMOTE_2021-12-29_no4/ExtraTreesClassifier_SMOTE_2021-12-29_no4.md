# ExtraTreesClassifier_SMOTE_2021-12-29_no4
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
- resampler = SMOTE
- estimator = ExtraTreesClassifier

### Arguments for hyperparameter search
- resampler = SMOTE
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
	- k_neighbors = 5
	- n_jobs = -1
	- n_features_in_ = 36
	- sampling_strategy_ = OrderedDict([(0, 12)])
	- nn_k_ = NearestNeighbors(n_neighbors=6)

- best_estimator
	- base_estimator = ExtraTreeClassifier()
	- n_estimators = 300
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
	- oob_decision_function_ = [[0.03550296 0.96449704]
 [0.01704545 0.98295455]
 [0.02150538 0.97849462]
 [0.00546448 0.99453552]
 [0.48387097 0.51612903]
 [0.49740933 0.50259067]
 [0.95505618 0.04494382]
 [0.92571429 0.07428571]
 [0.95721925 0.04278075]
 [0.96685083 0.03314917]
 [0.06770833 0.93229167]
 [0.04864865 0.95135135]
 [0.19886364 0.80113636]
 [0.06179775 0.93820225]
 [0.84042553 0.15957447]
 [0.60773481 0.39226519]
 [0.99468085 0.00531915]
 [0.98930481 0.01069519]
 [0.99453552 0.00546448]
 [0.97282609 0.02717391]
 [0.25142857 0.74857143]
 [0.16571429 0.83428571]
 [0.13333333 0.86666667]
 [0.22162162 0.77837838]
 [0.94535519 0.05464481]
 [0.89830508 0.10169492]
 [1.         0.        ]
 [0.99465241 0.00534759]
 [1.         0.        ]
 [1.         0.        ]
 [0.04975124 0.95024876]
 [0.02747253 0.97252747]
 [0.02197802 0.97802198]
 [0.02777778 0.97222222]
 [0.18131868 0.81868132]
 [0.14942529 0.85057471]
 [0.78191489 0.21808511]
 [0.75418994 0.24581006]
 [0.9939759  0.0060241 ]
 [0.7877095  0.2122905 ]
 [0.19125683 0.80874317]
 [0.05747126 0.94252874]
 [0.08383234 0.91616766]
 [0.03763441 0.96236559]
 [0.24742268 0.75257732]
 [0.13218391 0.86781609]
 [0.78609626 0.21390374]
 [0.59090909 0.40909091]
 [0.98963731 0.01036269]
 [0.98863636 0.01136364]
 [0.53072626 0.46927374]
 [0.32044199 0.67955801]
 [0.15428571 0.84571429]
 [0.13402062 0.86597938]
 [0.37368421 0.62631579]
 [0.17948718 0.82051282]
 [0.98275862 0.01724138]
 [0.97297297 0.02702703]
 [0.99418605 0.00581395]
 [0.98895028 0.01104972]
 [0.74719101 0.25280899]
 [0.66492147 0.33507853]
 [0.14367816 0.85632184]
 [0.01621622 0.98378378]
 [0.04022989 0.95977011]
 [0.0304878  0.9695122 ]
 [0.25136612 0.74863388]
 [0.0974359  0.9025641 ]
 [0.63978495 0.36021505]
 [0.66839378 0.33160622]
 [0.42708333 0.57291667]
 [0.29268293 0.70731707]
 [0.4516129  0.5483871 ]
 [0.1        0.9       ]
 [0.16756757 0.83243243]
 [0.03174603 0.96825397]
 [0.02209945 0.97790055]
 [0.02747253 0.97252747]
 [0.65463918 0.34536082]
 [0.70949721 0.29050279]
 [0.89847716 0.10152284]
 [0.87931034 0.12068966]
 [0.25       0.75      ]
 [0.09876543 0.90123457]
 [0.09473684 0.90526316]
 [0.03076923 0.96923077]
 [0.1734104  0.8265896 ]
 [0.43575419 0.56424581]
 [0.90857143 0.09142857]
 [0.97252747 0.02747253]
 [0.98333333 0.01666667]
 [0.95744681 0.04255319]
 [0.77889447 0.22110553]
 [0.68156425 0.31843575]
 [0.08       0.92      ]
 [0.12209302 0.87790698]
 [0.05913978 0.94086022]
 [0.04242424 0.95757576]
 [0.18617021 0.81382979]
 [0.22777778 0.77222222]
 [0.99421965 0.00578035]
 [1.         0.        ]
 [0.86285714 0.13714286]
 [0.77083333 0.22916667]
 [0.01744186 0.98255814]
 [0.06395349 0.93604651]
 [0.01621622 0.98378378]
 [0.01704545 0.98295455]
 [0.06626506 0.93373494]
 [0.03389831 0.96610169]
 [0.98295455 0.01704545]
 [0.93785311 0.06214689]
 [0.87912088 0.12087912]
 [0.82278481 0.17721519]
 [0.29213483 0.70786517]
 [0.10382514 0.89617486]
 [0.07954545 0.92045455]
 [0.02325581 0.97674419]
 [0.03278689 0.96721311]
 [0.16564417 0.83435583]
 [1.         0.        ]
 [0.95428571 0.04571429]
 [0.99465241 0.00534759]
 [0.83233533 0.16766467]
 [0.95977011 0.04022989]
 [1.         0.        ]
 [0.99450549 0.00549451]
 [0.97382199 0.02617801]
 [0.98404255 0.01595745]
 [0.83243243 0.16756757]
 [0.80701754 0.19298246]
 [0.98395722 0.01604278]]
	- oob_score_ = 0.9621212121212122

#### Importance of features
- gp_auc_min = 0.08550259970904361
- gp_max_val_min = 0.084396041098028
- gp_max_val_mean = 0.07940183292590897
- gp_auc_mean = 0.06183986312027694
- gp_max_val_max = 0.05550756889084524
- gp_auc_max = 0.05353619291005631
- srmr = 0.048958642895876474
- diff_std = 0.04217156051832545
- hlbr = 0.03917025332941626
- high_power = 0.03611797501063341
- diff_auc = 0.03536319438573789
- tdoa_max = 0.03035681421734541
- coe1[1] = 0.024618810299175835
- gp_max_ix_max = 0.022959128627941493
- gp_max_ix_std = 0.022752081010522084
- tdoa_range = 0.02077072349366122
- tdoa_mean = 0.02072425930365798
- coe1[0] = 0.02023212828776351
- ratio_max_to_10ms_ave_peaks = 0.018976851995678824
- gp_max_ix_range = 0.01804446312246828
- gp_max_ix_mean = 0.017444557612600692
- low_power = 0.017312089173373135
- gp_max_val_std = 0.016387268527211528
- gp_auc_std = 0.015892035513071424
- gp_auc_range = 0.015835038251292392
- gp_max_val_range = 0.013663037327045208
- tdoa_std = 0.01278054550330908
- coe3[2] = 0.01203614817436938
- tdoa_min = 0.011758613997935643
- coe3[3] = 0.010736597685844073
- ac_std = 0.010317424471373748
- gp_max_ix_min = 0.010125995009126304
- ratio_max_to_9th_ave_peaks = 0.007349940575517333
- ac_auc = 0.006959723025566912
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

      