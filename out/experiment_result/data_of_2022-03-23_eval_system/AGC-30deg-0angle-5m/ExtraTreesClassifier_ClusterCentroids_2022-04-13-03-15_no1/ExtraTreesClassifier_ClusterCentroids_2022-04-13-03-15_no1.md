# ExtraTreesClassifier_ClusterCentroids_2022-04-13-03-15_no1
## Constants
- CSV_PATH = ../out/csv/experiment
- OUTPUT_PATH = ../out/experiment_result/data_of_2022-03-23_eval_system/AGC-30deg-0angle-5m
- FEATURE_ATTRBS = ['low_power', 'high_power', 'hlbr', 'coe1[0]', 'coe1[1]', 'coe3[0]', 'coe3[1]', 'coe3[2]', 'coe3[3]', 'ratio_max_to_10ms_ave_peaks', 'ratio_max_to_9th_ave_peaks', 'ac_std', 'ac_auc', 'diff_std', 'diff_auc', 'srmr', 'gp_max_val_std', 'gp_max_val_range', 'gp_max_val_min', 'gp_max_val_max', 'gp_max_val_mean', 'gp_max_ix_std', 'gp_max_ix_range', 'gp_max_ix_min', 'gp_max_ix_max', 'gp_max_ix_mean', 'gp_auc_std', 'gp_auc_range', 'gp_auc_min', 'gp_auc_max', 'gp_auc_mean', 'tdoa_std', 'tdoa_range', 'tdoa_min', 'tdoa_max', 'tdoa_mean']
- LABEL_ATTRB = ['facing']
- FACING_DOV_ANGLES = [1]
- NCV = 8
- SCORING = ['accuracy', 'balanced_accuracy', 'f1']
- REFIT_SCORING = balanced_accuracy
- PARAM_GRID = [{'est__n_estimators': range(10, 400, 20), 'est__min_samples_split': [2, 5, 10], 'est__min_samples_leaf': [1, 5, 10], 'est__max_features': ['sqrt', 'log2', None], 'est__bootstrap': [False], 'est__n_jobs': [-1], 'est__random_state': [42], 'est__max_samples': [0.01, 0.5, 0.09]}, {'est__n_estimators': range(10, 400, 20), 'est__min_samples_split': [2, 5, 10], 'est__min_samples_leaf': [1, 5, 10], 'est__max_features': ['sqrt', 'log2', None], 'est__bootstrap': [True], 'est__oob_score': [True, False], 'est__n_jobs': [-1], 'est__random_state': [42], 'est__max_samples': [0.01, 0.5, 0.09]}]
- HP_SET_SESSION = ['trial1', 'trial21']
- TRAIN_SET_SESSION = None
- TEST_SET_SESSION = None
- DISTANCE = [5]
- AGC_STATUS = ['AGC-30deg']
- ANGLES = [30, 60, 90, 120, 150]

## Loaded CSV
- 2022-03-23_raspi_48000Hz_w1_N2^12_overlap80_all.csv

## Estimator
### Type
- resampler = ClusterCentroids
- estimator = ExtraTreesClassifier

### Arguments for hyperparameter search
- resampler = ClusterCentroids
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
	- estimator = None
	- voting = auto
	- n_jobs = deprecated
	- n_features_in_ = 36
	- sampling_strategy_ = OrderedDict([(0, 15)])
	- estimator_ = KMeans(n_clusters=15, random_state=42)
	- voting_ = soft

- best_estimator
	- base_estimator = ExtraTreeClassifier()
	- n_estimators = 90
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
	- min_samples_split = 10
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
- gp_max_val_min = 0.19857191920635917
- gp_max_val_mean = 0.18277678893129237
- gp_auc_mean = 0.17637286852701736
- gp_auc_min = 0.15433559409109218
- gp_max_val_max = 0.11468493898742085
- hlbr = 0.03687760200660097
- gp_auc_max = 0.027667116605741764
- high_power = 0.018646045074063648
- diff_std = 0.01317374312054739
- ac_auc = 0.01205620577347737
- ratio_max_to_10ms_ave_peaks = 0.01006048887961974
- diff_auc = 0.009329467559381476
- gp_max_val_std = 0.0073021262856962236
- ac_std = 0.00611717514467395
- srmr = 0.005159793337037921
- gp_max_ix_mean = 0.004807406054209124
- tdoa_std = 0.004424143394731629
- gp_max_ix_min = 0.004268071275483996
- tdoa_min = 0.00405735956934214
- gp_max_val_range = 0.0025996386630532976
- gp_max_ix_std = 0.002507122507122507
- gp_auc_std = 0.0017534046138780713
- coe1[1] = 0.001225490196078431
- gp_auc_range = 0.001225490196078431
- low_power = 0.0
- coe1[0] = 0.0
- coe3[0] = 0.0
- coe3[1] = 0.0
- coe3[2] = 0.0
- coe3[3] = 0.0
- ratio_max_to_9th_ave_peaks = 0.0
- gp_max_ix_range = 0.0
- gp_max_ix_max = 0.0
- tdoa_range = 0.0
- tdoa_max = 0.0
- tdoa_mean = 0.0

## Evaluation
cv = 8
### robot-1
#### accuracy
- Mean = 0.82875
- Standard deviation = 0.03887077951366552
- Max = 0.92
- 75% = 0.8425
- Median = 0.81
- 25% = 0.8
- Min = 0.8

#### f1
- Mean = 0.6559004019674313
- Standard deviation = 0.05770628446366633
- Max = 0.7894736842105262
- 75% = 0.6802127659574468
- Median = 0.6296296296296295
- 25% = 0.6252834467120181
- Min = 0.5957446808510639

#### precision
- Mean = 0.566044061302682
- Standard deviation = 0.10599209886849936
- Max = 0.8333333333333334
- 75% = 0.5731481481481482
- Median = 0.5178799489144317
- 25% = 0.5
- Min = 0.5

#### recall
- Mean = 0.8
- Standard deviation = 0.05590169943749474
- Max = 0.85
- 75% = 0.85
- Median = 0.825
- 25% = 0.75
- Min = 0.7

#### facing_probas
- Mean = [0.74573327 0.07584557 0.03509212 0.10327188 0.11660576]
- Standard deviation = [0.05653476 0.04187089 0.05519513 0.12840907 0.14387334]
- Max = [0.80444048 0.13155688 0.17893034 0.34847884 0.37064374]
- 75% = [0.79042284 0.11284044 0.0278912  0.21242703 0.19987743]
- Median = [0.76880093 0.07663062 0.01518739 0.01749317 0.03311265]
- 25% = [0.71289231 0.04447658 0.00516617 0.00486111 0.00555556]
- Min = [0.64100066 0.00791997 0.00422222 0.         0.        ]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 66.875 | 13.125 |
| Actual Positive | 4.0 | 16.0 |

### robot-2
#### accuracy
- Mean = 0.815
- Standard deviation = 0.03535533905932736
- Max = 0.9
- 75% = 0.8225
- Median = 0.8
- 25% = 0.79
- Min = 0.79

#### f1
- Mean = 0.39983121409532696
- Standard deviation = 0.1655800581036258
- Max = 0.7727272727272727
- 75% = 0.4410282258064516
- Median = 0.39803439803439805
- 25% = 0.2777777777777778
- Min = 0.2222222222222222

#### precision
- Mean = 0.5360910535542889
- Standard deviation = 0.09757831128393114
- Max = 0.7083333333333334
- 75% = 0.5965909090909092
- Median = 0.5210084033613445
- 25% = 0.4532967032967033
- Min = 0.42857142857142855

#### recall
- Mean = 0.34375
- Standard deviation = 0.21130176880471208
- Max = 0.85
- 75% = 0.3625
- Median = 0.32499999999999996
- 25% = 0.1875
- Min = 0.15

#### facing_probas
- Mean = [0.87793778 0.81750124 0.51387514 0.12491479 0.08830117]
- Standard deviation = [0.06524707 0.06102683 0.05524322 0.07209098 0.08229578]
- Max = [0.94718563 0.89174427 0.60184436 0.25152116 0.26764859]
- 75% = [0.92574405 0.87215316 0.54123997 0.18463255 0.11293419]
- Median = [0.90117119 0.81765035 0.5220593  0.09291082 0.05384843]
- 25% = [0.8301956  0.76714732 0.48925463 0.07714826 0.03055969]
- Min = [0.7486142  0.7290787  0.41184105 0.03844048 0.01605489]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 74.625 | 5.375 |
| Actual Positive | 13.125 | 6.875 |

### robot-3
#### accuracy
- Mean = 0.85625
- Standard deviation = 0.0193245310421754
- Max = 0.88
- 75% = 0.8725
- Median = 0.86
- 25% = 0.8374999999999999
- Min = 0.83

#### f1
- Mean = 0.5524876743626743
- Standard deviation = 0.08623735622290381
- Max = 0.6285714285714286
- 75% = 0.6145833333333334
- Median = 0.6
- 25% = 0.49621212121212116
- Min = 0.37037037037037035

#### precision
- Mean = 0.7448546245421246
- Standard deviation = 0.10661759065266371
- Max = 0.9
- 75% = 0.84375
- Median = 0.7238095238095238
- 25% = 0.6694711538461539
- Min = 0.6

#### recall
- Mean = 0.45625000000000004
- Standard deviation = 0.1102199505534275
- Max = 0.6
- 75% = 0.55
- Median = 0.475
- 25% = 0.3875
- Min = 0.25

#### facing_probas
- Mean = [0.33997594 0.67019637 0.72670051 0.54540892 0.06870186]
- Standard deviation = [0.04484159 0.06106211 0.05939493 0.05093612 0.07010658]
- Max = [0.4395172  0.76928175 0.80666975 0.62667945 0.21715785]
- 75% = [0.35625711 0.70613239 0.76229156 0.58107981 0.10571197]
- Median = [0.33018155 0.67481063 0.72864054 0.54758752 0.03676929]
- 25% = [0.31186778 0.64164297 0.71134392 0.49697068 0.01313905]
- Min = [0.28129233 0.57377866 0.59833576 0.48416336 0.00462632]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 76.5 | 3.5 |
| Actual Positive | 10.875 | 9.125 |

### robot-4
#### accuracy
- Mean = 0.8125
- Standard deviation = 0.04235268586524353
- Max = 0.89
- 75% = 0.8325
- Median = 0.795
- 25% = 0.78
- Min = 0.77

#### f1
- Mean = 0.6116690198969044
- Standard deviation = 0.06905128427343625
- Max = 0.7659574468085106
- 75% = 0.6291273584905661
- Median = 0.6066017316017316
- 25% = 0.569947209653092
- Min = 0.5217391304347826

#### precision
- Mean = 0.5426108529687159
- Standard deviation = 0.1077098844590184
- Max = 0.7692307692307693
- 75% = 0.5684523809523809
- Median = 0.4936868686868687
- 25% = 0.4669471153846154
- Min = 0.45161290322580644

#### recall
- Mean = 0.7375
- Standard deviation = 0.12686114456365274
- Max = 0.9
- 75% = 0.85
- Median = 0.75
- 25% = 0.6749999999999999
- Min = 0.5

#### facing_probas
- Mean = [0.06095869 0.21440683 0.66538244 0.83538117 0.31768174]
- Standard deviation = [0.08577456 0.04753251 0.05362854 0.04183728 0.0597628 ]
- Max = [0.2772866  0.32470547 0.76450287 0.88104519 0.43692923]
- 75% = [0.06909827 0.22836513 0.69255032 0.8662996  0.34524813]
- Median = [0.02255015 0.19623964 0.65298137 0.85065575 0.31452447]
- 25% = [0.00782821 0.18349752 0.62044081 0.81168237 0.28624741]
- Min = [0.0059321  0.16666468 0.60551962 0.75189837 0.22656768]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 66.5 | 13.5 |
| Actual Positive | 5.25 | 14.75 |

### robot-5
#### accuracy
- Mean = 0.8699999999999999
- Standard deviation = 0.03937003937005906
- Max = 0.94
- 75% = 0.885
- Median = 0.855
- 25% = 0.84
- Min = 0.83

#### f1
- Mean = 0.5492950775278362
- Standard deviation = 0.1653233028676407
- Max = 0.85
- 75% = 0.6107628004179729
- Median = 0.4888888888888889
- 25% = 0.42487684729064035
- Min = 0.3846153846153846

#### precision
- Mean = 0.8307539682539682
- Standard deviation = 0.09184836489583689
- Max = 1.0
- 75% = 0.865079365079365
- Median = 0.8416666666666667
- 25% = 0.7875000000000001
- Min = 0.6666666666666666

#### recall
- Mean = 0.43125
- Standard deviation = 0.19675095298371492
- Max = 0.85
- 75% = 0.4625
- Median = 0.35
- 25% = 0.3
- Min = 0.25

#### facing_probas
- Mean = [0.07466049 0.03909171 0.48283358 0.89294177 0.87377929]
- Standard deviation = [0.0895664  0.04276966 0.08618528 0.07019326 0.06970248]
- Max = [0.23398589 0.12820988 0.57329586 0.96767063 0.93963051]
- 75% = [0.15649085 0.05594621 0.54944896 0.94482457 0.9163141 ]
- Median = [0.01641204 0.0220032  0.50295425 0.91426014 0.90553549]
- 25% = [0.00384259 0.00445437 0.44609094 0.87188487 0.85877464]
- Min = [0.00000000e+00 7.17592593e-04 3.31789242e-01 7.66876764e-01
 7.53391755e-01]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 78.375 | 1.625 |
| Actual Positive | 11.375 | 8.625 |

### robot-6
#### accuracy
- Mean = 0.55375
- Standard deviation = 0.06688376110835872
- Max = 0.71
- 75% = 0.5625
- Median = 0.53
- 25% = 0.51
- Min = 0.49

#### f1
- Mean = 0.710538437747911
- Standard deviation = 0.052382439022133354
- Max = 0.8304093567251462
- 75% = 0.719758064516129
- Median = 0.6927546138072453
- 25% = 0.6754966887417219
- Min = 0.6577181208053691

#### precision
- Mean = 1.0
- Standard deviation = 0.0
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 1.0
- Min = 1.0

#### recall
- Mean = 0.55375
- Standard deviation = 0.06688376110835872
- Max = 0.71
- 75% = 0.5625
- Median = 0.53
- 25% = 0.51
- Min = 0.49

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
| Actual Positive | 44.625 | 55.375 |

