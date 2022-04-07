# ExtraTreesClassifier_SMOTEENN_2022-01-20-14-11_no5
## Constants
- CSV_PATH = ../out/csv/experiment
- OUTPUT_PATH = ../out/experiment_result/data_of_2022-01-13_eval_system/NoAGC-45angle-5m
- FEATURE_ATTRBS = ['low_power', 'high_power', 'hlbr', 'coe1[0]', 'coe1[1]', 'coe3[0]', 'coe3[1]', 'coe3[2]', 'coe3[3]', 'ratio_max_to_10ms_ave_peaks', 'ratio_max_to_9th_ave_peaks', 'ac_std', 'ac_auc', 'diff_std', 'diff_auc', 'srmr', 'gp_max_val_std', 'gp_max_val_range', 'gp_max_val_min', 'gp_max_val_max', 'gp_max_val_mean', 'gp_max_ix_std', 'gp_max_ix_range', 'gp_max_ix_min', 'gp_max_ix_max', 'gp_max_ix_mean', 'gp_auc_std', 'gp_auc_range', 'gp_auc_min', 'gp_auc_max', 'gp_auc_mean', 'tdoa_std', 'tdoa_range', 'tdoa_min', 'tdoa_max', 'tdoa_mean']
- LABEL_ATTRB = ['facing2']
- FACING_DOV_ANGLES = [1, 2]
- NCV = 8
- SCORING = ['accuracy', 'balanced_accuracy', 'f1']
- REFIT_SCORING = balanced_accuracy
- PARAM_GRID = [{'est__n_estimators': range(10, 400, 20), 'est__min_samples_split': [2, 5, 10], 'est__min_samples_leaf': [1, 5, 10], 'est__max_features': ['sqrt', 'log2', None], 'est__bootstrap': [False], 'est__n_jobs': [-1], 'est__random_state': [42], 'est__max_samples': [0.01, 0.5, 0.09]}, {'est__n_estimators': range(10, 400, 20), 'est__min_samples_split': [2, 5, 10], 'est__min_samples_leaf': [1, 5, 10], 'est__max_features': ['sqrt', 'log2', None], 'est__bootstrap': [True], 'est__oob_score': [True, False], 'est__n_jobs': [-1], 'est__random_state': [42], 'est__max_samples': [0.01, 0.5, 0.09]}]
- HP_SET_SESSION = ['trial1', 'trial21']
- TRAIN_SET_SESSION = None
- TEST_SET_SESSION = None
- DISTANCE = [5]
- AGC_STATUS = ['NoAGC']

## Loaded CSV
- 2021-12-27_AGC.csv
- 2022-01-10_NoAGC.csv
- 2022-01-13_raspi_48000Hz_w1_N2^12_overlap80.csv

## Estimator
### Type
- resampler = SMOTEENN
- estimator = ExtraTreesClassifier

### Arguments for hyperparameter search
- resampler = SMOTEENN
- estimator = ExtraTreesClassifier
- param_grid = 
	- {'est__n_estimators': range(10, 400, 20), 'est__min_samples_split': [2, 5, 10], 'est__min_samples_leaf': [1, 5, 10], 'est__max_features': ['sqrt', 'log2', None], 'est__bootstrap': [False], 'est__n_jobs': [-1], 'est__random_state': [42], 'est__max_samples': [0.01, 0.5, 0.09]}
	- {'est__n_estimators': range(10, 400, 20), 'est__min_samples_split': [2, 5, 10], 'est__min_samples_leaf': [1, 5, 10], 'est__max_features': ['sqrt', 'log2', None], 'est__bootstrap': [True], 'est__oob_score': [True, False], 'est__n_jobs': [-1], 'est__random_state': [42], 'est__max_samples': [0.01, 0.5, 0.09]}

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
	- n_estimators = 210
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
	- min_samples_split = 2
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
- gp_auc_max = 0.1413095238095238
- gp_max_val_max = 0.11916666666666667
- gp_auc_mean = 0.11273809523809525
- srmr = 0.09523809523809523
- gp_max_val_mean = 0.09523809523809523
- gp_max_val_min = 0.08892857142857143
- gp_max_val_std = 0.08095238095238096
- gp_auc_min = 0.07464285714285715
- gp_auc_range = 0.07297619047619047
- gp_max_val_range = 0.05714285714285714
- gp_auc_std = 0.047619047619047616
- hlbr = 0.0032142857142857147
- high_power = 0.0030952380952380953
- tdoa_std = 0.0030952380952380953
- low_power = 0.0015476190476190477
- coe1[0] = 0.0015476190476190477
- ac_std = 0.0015476190476190477
- coe1[1] = 0.0
- coe3[0] = 0.0
- coe3[1] = 0.0
- coe3[2] = 0.0
- coe3[3] = 0.0
- ratio_max_to_10ms_ave_peaks = 0.0
- ratio_max_to_9th_ave_peaks = 0.0
- ac_auc = 0.0
- diff_std = 0.0
- diff_auc = 0.0
- gp_max_ix_std = 0.0
- gp_max_ix_range = 0.0
- gp_max_ix_min = 0.0
- gp_max_ix_max = 0.0
- gp_max_ix_mean = 0.0
- tdoa_range = 0.0
- tdoa_min = 0.0
- tdoa_max = 0.0
- tdoa_mean = 0.0

## Evaluation
cv = 8
### robot-1
#### accuracy
- Mean = 0.90875
- Standard deviation = 0.07025622748198194
- Max = 0.97
- 75% = 0.9624999999999999
- Median = 0.955
- 25% = 0.84
- Min = 0.8

#### f1
- Mean = 0.6665726544317516
- Standard deviation = 0.3645522680607018
- Max = 0.9302325581395349
- 75% = 0.9143763213530656
- Median = 0.8809523809523809
- 25% = 0.5532212885154061
- Min = 0.0

#### precision
- Mean = 0.7520931616303286
- Standard deviation = 0.30915112825163993
- Max = 1.0
- 75% = 0.9021739130434783
- Median = 0.866600790513834
- 25% = 0.7701612903225807
- Min = 0.0

#### recall
- Mean = 0.70625
- Standard deviation = 0.401121474743001
- Max = 1.0
- 75% = 1.0
- Median = 0.925
- 25% = 0.575
- Min = 0.0

#### facing_probas
- Mean = [0.8608631  0.74107143 0.26217262 0.0660119  0.0408631 ]
- Standard deviation = [0.07298502 0.23240096 0.24323729 0.0624142  0.05014335]
- Max = [0.96238095 0.93166667 0.6347619  0.155      0.14761905]
- 75% = [0.92815476 0.86958333 0.47613095 0.13571429 0.05339286]
- Median = [0.85119048 0.81642857 0.14142857 0.03142857 0.01416667]
- 25% = [0.82845238 0.71684524 0.0627381  0.01303571 0.00744048]
- Min = [0.72142857 0.16214286 0.01428571 0.00571429 0.00190476]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 76.75 | 3.25 |
| Actual Positive | 5.875 | 14.125 |

### robot-2
#### accuracy
- Mean = 0.8525
- Standard deviation = 0.13026415470113026
- Max = 0.97
- 75% = 0.97
- Median = 0.895
- 25% = 0.7849999999999999
- Min = 0.64

#### f1
- Mean = 0.5942916574552155
- Standard deviation = 0.3207175700977892
- Max = 0.9189189189189189
- 75% = 0.9189189189189189
- Median = 0.6541889483065954
- 25% = 0.33658536585365856
- Min = 0.14285714285714282

#### precision
- Mean = 0.7368256743256744
- Standard deviation = 0.3664704685707659
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 0.49725274725274726
- Min = 0.13636363636363635

#### recall
- Mean = 0.525
- Standard deviation = 0.3
- Max = 0.85
- 75% = 0.85
- Median = 0.55
- 25% = 0.225
- Min = 0.15

#### facing_probas
- Mean = [0.84636905 0.89660714 0.72568452 0.2497619  0.0346131 ]
- Standard deviation = [0.0653724  0.09609833 0.15214809 0.21982742 0.04313254]
- Max = [0.95857143 0.97285714 0.92238095 0.6052381  0.11619048]
- 75% = [0.90755952 0.9610119  0.8039881  0.47035714 0.04154762]
- Median = [0.82035714 0.92404762 0.73761905 0.14690476 0.0177381 ]
- 25% = [0.80041667 0.8872619  0.70839286 0.06422619 0.00285714]
- Min = [0.75928571 0.65642857 0.38928571 0.02642857 0.        ]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 74.75 | 5.25 |
| Actual Positive | 9.5 | 10.5 |

### robot-3
#### accuracy
- Mean = 0.91125
- Standard deviation = 0.06508408023472405
- Max = 0.97
- 75% = 0.9624999999999999
- Median = 0.935
- 25% = 0.8875
- Min = 0.79

#### f1
- Mean = 0.7054332397698522
- Standard deviation = 0.25207495650924705
- Max = 0.9189189189189189
- 75% = 0.9007823613086771
- Median = 0.8109243697478992
- 25% = 0.6215437788018433
- Min = 0.2222222222222222

#### precision
- Mean = 0.8658234126984128
- Standard deviation = 0.20350590291656995
- Max = 1.0
- 75% = 1.0
- Median = 0.9722222222222222
- 25% = 0.8526785714285714
- Min = 0.42857142857142855

#### recall
- Mean = 0.6124999999999999
- Standard deviation = 0.25950674365033366
- Max = 0.85
- 75% = 0.85
- Median = 0.7
- 25% = 0.47500000000000003
- Min = 0.15

#### facing_probas
- Mean = [0.32535714 0.87172619 0.83098214 0.79782738 0.11791667]
- Standard deviation = [0.1595334  0.11692208 0.14136585 0.0933956  0.08932584]
- Max = [0.62428571 1.         0.92714286 0.94333333 0.29761905]
- 75% = [0.4247619  0.96404762 0.91940476 0.83011905 0.14803571]
- Median = [0.26940476 0.89107143 0.89809524 0.77630952 0.10083333]
- 25% = [0.2239881  0.84214286 0.82535714 0.7602381  0.04410714]
- Min = [0.11809524 0.615      0.49214286 0.63809524 0.02071429]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 78.875 | 1.125 |
| Actual Positive | 7.75 | 12.25 |

### robot-4
#### accuracy
- Mean = 0.80125
- Standard deviation = 0.09584329658353785
- Max = 0.89
- 75% = 0.8825000000000001
- Median = 0.85
- 25% = 0.7125
- Min = 0.66

#### f1
- Mean = 0.35365580793445905
- Standard deviation = 0.29622721446125816
- Max = 0.6857142857142857
- 75% = 0.6305147058823529
- Median = 0.4012539184952978
- 25% = 0.05172413793103449
- Min = 0.0

#### precision
- Mean = 0.5662698412698413
- Standard deviation = 0.41815738621632204
- Max = 1.0
- 75% = 0.875
- Median = 0.7928571428571429
- 25% = 0.08333333333333333
- Min = 0.0

#### recall
- Mean = 0.28125
- Standard deviation = 0.24866832830097202
- Max = 0.6
- 75% = 0.5125
- Median = 0.275
- 25% = 0.037500000000000006
- Min = 0.0

#### facing_probas
- Mean = [0.03095238 0.568125   0.76491071 0.89392857 0.67964286]
- Standard deviation = [0.0327833  0.28312629 0.25814171 0.06798328 0.11052704]
- Max = [0.08547619 0.99690476 0.92571429 0.94142857 0.8352381 ]
- 75% = [0.0577381  0.79279762 0.91529762 0.92910714 0.74154762]
- Median = [0.01595238 0.49702381 0.89345238 0.91714286 0.68345238]
- 25% = [0.00136905 0.38547619 0.78392857 0.90494048 0.63107143]
- Min = [0.         0.11142857 0.15404762 0.72190476 0.45738095]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 74.5 | 5.5 |
| Actual Positive | 14.375 | 5.625 |

### robot-5
#### accuracy
- Mean = 0.9437500000000001
- Standard deviation = 0.05313602826708071
- Max = 1.0
- 75% = 0.9824999999999999
- Median = 0.97
- 25% = 0.905
- Min = 0.86

#### f1
- Mean = 0.8040802695407958
- Standard deviation = 0.20972635720625538
- Max = 1.0
- 75% = 0.9541160593792173
- Median = 0.9189189189189189
- 25% = 0.6778846153846153
- Min = 0.4615384615384615

#### precision
- Mean = 1.0
- Standard deviation = 0.0
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 1.0
- Min = 1.0

#### recall
- Mean = 0.71875
- Standard deviation = 0.2656801413354035
- Max = 1.0
- 75% = 0.9125
- Median = 0.85
- 25% = 0.525
- Min = 0.3

#### facing_probas
- Mean = [0.03261905 0.03047619 0.23089286 0.84916667 0.73997024]
- Standard deviation = [0.03152178 0.03405553 0.11663482 0.06067424 0.18952297]
- Max = [0.0747619  0.08928571 0.37547619 0.92833333 0.88785714]
- 75% = [0.06827381 0.05922619 0.32279762 0.8710119  0.87077381]
- Median = [0.02357143 0.01321429 0.24047619 0.86369048 0.8172619 ]
- 25% = [1.78571429e-04 8.92857143e-04 1.77976190e-01 8.50714286e-01
 7.20238095e-01]
- Min = [0.         0.         0.00142857 0.70452381 0.30333333]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 80.0 | 0.0 |
| Actual Positive | 5.625 | 14.375 |

### robot-6
#### accuracy
- Mean = 0.5687500000000001
- Standard deviation = 0.2578486717049363
- Max = 0.8
- 75% = 0.76
- Median = 0.655
- 25% = 0.51
- Min = 0.12

#### f1
- Mean = 0.6824255836553902
- Standard deviation = 0.26045242496744825
- Max = 0.888888888888889
- 75% = 0.8635275339185954
- Median = 0.7912649722465674
- 25% = 0.6449719925313417
- Min = 0.21428571428571425

#### precision
- Mean = 1.0
- Standard deviation = 0.0
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 1.0
- Min = 1.0

#### recall
- Mean = 0.5687500000000001
- Standard deviation = 0.2578486717049363
- Max = 0.8
- 75% = 0.76
- Median = 0.655
- 25% = 0.51
- Min = 0.12

#### facing_probas
- Mean = -100.0
- Standard deviation = 0.0
- Max = -100
- 75% = -100.0
- Median = -100.0
- 25% = -100.0
- Min = -100

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 0.0 | 0.0 |
| Actual Positive | 43.125 | 56.875 |

