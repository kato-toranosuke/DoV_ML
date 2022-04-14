# ExtraTreesClassifier_RandomUnderSampler_2022-04-12-17-49_no2
## Constants
- CSV_PATH = ../out/csv/experiment
- OUTPUT_PATH = ../out/experiment_result/data_of_2022-03-23_eval_system/AGC-30deg-0angle-1m
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
- DISTANCE = [1]
- AGC_STATUS = ['AGC-30deg']
- ANGLES = [30, 60, 90, 120, 150]

## Loaded CSV
- 2022-03-23_raspi_48000Hz_w1_N2^12_overlap80_all.csv

## Estimator
### Type
- resampler = RandomUnderSampler
- estimator = ExtraTreesClassifier

### Arguments for hyperparameter search
- resampler = RandomUnderSampler
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
	- replacement = False
	- n_features_in_ = 36
	- sampling_strategy_ = OrderedDict([(0, 15)])
	- sample_indices_ = [ 3  8 45 57 16 66 42 60 15 69 58 62 40  6 64  0  1  2 18 19 20 36 37 38
 54 55 56 72 73 74]

- best_estimator
	- base_estimator = ExtraTreeClassifier()
	- n_estimators = 10
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
	- min_samples_leaf = 5
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
- gp_auc_min = 0.27797304792527794
- tdoa_mean = 0.14476092692770076
- gp_max_val_min = 0.12887927285691023
- gp_max_val_max = 0.0795836634373655
- low_power = 0.06770896494053538
- gp_auc_max = 0.06444683136412459
- gp_max_ix_range = 0.055094830578471345
- diff_auc = 0.04571362779976722
- tdoa_max = 0.02616822429906541
- srmr = 0.023303857639493535
- ratio_max_to_9th_ave_peaks = 0.018045112781954874
- coe1[1] = 0.01441842828704141
- coe1[0] = 0.010569044387472994
- gp_auc_std = 0.009126466753585402
- gp_max_val_range = 0.008571428571428575
- gp_max_ix_mean = 0.00830302614423933
- diff_std = 0.005383022774327139
- tdoa_min = 0.003975495307612107
- gp_max_val_std = 0.0030075187969924944
- tdoa_range = 0.0026271893244370374
- ratio_max_to_10ms_ave_peaks = 0.0023400191021967576
- high_power = 0.0
- hlbr = 0.0
- coe3[0] = 0.0
- coe3[1] = 0.0
- coe3[2] = 0.0
- coe3[3] = 0.0
- ac_std = 0.0
- ac_auc = 0.0
- gp_max_val_mean = 0.0
- gp_max_ix_std = 0.0
- gp_max_ix_min = 0.0
- gp_max_ix_max = 0.0
- gp_auc_range = 0.0
- gp_auc_mean = 0.0
- tdoa_std = 0.0

## Evaluation
cv = 8
### robot-1
#### accuracy
- Mean = 0.9825
- Standard deviation = 0.016393596310755015
- Max = 1.0
- 75% = 0.9924999999999999
- Median = 0.99
- 25% = 0.97
- Min = 0.95

#### f1
- Mean = 0.9590538660306103
- Standard deviation = 0.0364697998200393
- Max = 1.0
- 75% = 0.9807692307692307
- Median = 0.9743589743589743
- 25% = 0.9302325581395349
- Min = 0.888888888888889

#### precision
- Mean = 0.942391304347826
- Standard deviation = 0.07703600660599964
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 0.8695652173913043
- Min = 0.8

#### recall
- Mean = 0.98125
- Standard deviation = 0.024206145913796374
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 0.95
- Min = 0.95

#### facing_probas
- Mean = [0.82209177 0.13849901 0.04515675 0.02680357 0.04748884]
- Standard deviation = [0.05468369 0.05792353 0.01853533 0.01906424 0.04095573]
- Max = [0.94225    0.21359921 0.0764504  0.05678571 0.10642857]
- 75% = [0.83881052 0.20013492 0.05815179 0.03923214 0.09296875]
- Median = [0.80893849 0.12499504 0.04316667 0.0275     0.03309524]
- 25% = [0.79537599 0.10713988 0.03295982 0.015      0.015     ]
- Min = [0.75456349 0.04959722 0.01642857 0.         0.        ]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 78.625 | 1.375 |
| Actual Positive | 0.375 | 19.625 |

### robot-2
#### accuracy
- Mean = 0.825
- Standard deviation = 0.05678908345800274
- Max = 0.89
- 75% = 0.8625
- Median = 0.85
- 25% = 0.795
- Min = 0.72

#### f1
- Mean = 0.5970786493383337
- Standard deviation = 0.14872297086425137
- Max = 0.7555555555555556
- 75% = 0.7208994708994709
- Median = 0.649673202614379
- 25% = 0.48217636022514077
- Min = 0.3636363636363636

#### precision
- Mean = 0.5523347584647894
- Standard deviation = 0.12724065429031428
- Max = 0.7142857142857143
- 75% = 0.65
- Median = 0.5718954248366013
- 25% = 0.4899749373433584
- Min = 0.3333333333333333

#### recall
- Mean = 0.68125
- Standard deviation = 0.24230339968725162
- Max = 1.0
- 75% = 0.8875
- Median = 0.65
- 25% = 0.475
- Min = 0.4

#### facing_probas
- Mean = [0.49705308 0.79526687 0.72280481 0.27848165 0.01866964]
- Standard deviation = [0.11722239 0.03189495 0.06899713 0.0760248  0.01181361]
- Max = [0.68093254 0.84522222 0.82500198 0.41194444 0.03142857]
- 75% = [0.59964435 0.81617411 0.75269395 0.32446776 0.02873214]
- Median = [0.48413591 0.79721528 0.71780357 0.29288393 0.0225    ]
- 25% = [0.38559226 0.7815997  0.70440129 0.21588839 0.01125   ]
- Min = [0.35678571 0.7312996  0.57830556 0.16661706 0.        ]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 68.875 | 11.125 |
| Actual Positive | 6.375 | 13.625 |

### robot-3
#### accuracy
- Mean = 0.7925
- Standard deviation = 0.03799671038392665
- Max = 0.84
- 75% = 0.8225
- Median = 0.8
- 25% = 0.77
- Min = 0.73

#### f1
- Mean = 0.2822901069182534
- Standard deviation = 0.11685777135719878
- Max = 0.4666666666666667
- 75% = 0.34290271132376393
- Median = 0.28428093645484953
- 25% = 0.20616883116883114
- Min = 0.08695652173913045

#### precision
- Mean = 0.5744897098515519
- Standard deviation = 0.27436372494185907
- Max = 1.0
- 75% = 0.7749999999999999
- Median = 0.4567307692307692
- 25% = 0.3333333333333333
- Min = 0.3157894736842105

#### recall
- Mean = 0.21874999999999997
- Standard deviation = 0.11162856937182344
- Max = 0.35
- 75% = 0.3125
- Median = 0.22499999999999998
- 25% = 0.1375
- Min = 0.05

#### facing_probas
- Mean = [0.11619568 0.68063343 0.61415848 0.52377406 0.24042138]
- Standard deviation = [0.05235804 0.05651851 0.0501773  0.07251436 0.05391347]
- Max = [0.2065     0.77630754 0.70561508 0.6336746  0.34666865]
- 75% = [0.15458333 0.70410268 0.6474246  0.58003373 0.26692113]
- Median = [0.11349107 0.68087004 0.61059524 0.52542163 0.24066964]
- 25% = [0.06163294 0.66035119 0.57718304 0.4588125  0.19854861]
- Min = [0.05634921 0.56791071 0.53925    0.42828571 0.16611111]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 74.875 | 5.125 |
| Actual Positive | 15.625 | 4.375 |

### robot-4
#### accuracy
- Mean = 0.7875
- Standard deviation = 0.06199798383818624
- Max = 0.92
- 75% = 0.8150000000000001
- Median = 0.775
- 25% = 0.7424999999999999
- Min = 0.72

#### f1
- Mean = 0.5282203889862768
- Standard deviation = 0.1284320474482357
- Max = 0.8095238095238095
- 75% = 0.5796747967479675
- Median = 0.5157312925170068
- 25% = 0.4270943796394485
- Min = 0.3913043478260869

#### precision
- Mean = 0.48288922284611935
- Standard deviation = 0.13166550169230992
- Max = 0.7727272727272727
- 75% = 0.5328571428571429
- Median = 0.4464285714285714
- 25% = 0.3968832891246684
- Min = 0.34615384615384615

#### recall
- Mean = 0.5875
- Standard deviation = 0.1293010054098575
- Max = 0.85
- 75% = 0.65
- Median = 0.6
- 25% = 0.45
- Min = 0.45

#### facing_probas
- Mean = [0.03452877 0.44376612 0.42471999 0.74449206 0.71176389]
- Standard deviation = [0.02310775 0.08401904 0.05967797 0.02090091 0.03695507]
- Max = [0.08333333 0.59222619 0.52043452 0.77570635 0.7642381 ]
- 75% = [0.03864881 0.48856101 0.47505903 0.76101637 0.75286458]
- Median = [0.03251984 0.45137103 0.41420139 0.74267163 0.69258333]
- 25% = [0.02148214 0.39747222 0.38264583 0.73122173 0.68605208]
- Min = [0.         0.2874881  0.3432381  0.71246627 0.66803571]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 67.0 | 13.0 |
| Actual Positive | 8.25 | 11.75 |

### robot-5
#### accuracy
- Mean = 0.8287500000000001
- Standard deviation = 0.07183966522750505
- Max = 0.96
- 75% = 0.87
- Median = 0.8200000000000001
- 25% = 0.7675000000000001
- Min = 0.74

#### f1
- Mean = 0.48500559368598306
- Standard deviation = 0.2686049945311901
- Max = 0.9
- 75% = 0.6788482834994463
- Median = 0.4862903225806452
- 25% = 0.20517241379310344
- Min = 0.18749999999999997

#### precision
- Mean = 0.5279808959156785
- Standard deviation = 0.2156525233314581
- Max = 0.9
- 75% = 0.6693181818181818
- Median = 0.5316205533596838
- 25% = 0.32499999999999996
- Min = 0.25

#### recall
- Mean = 0.46875
- Standard deviation = 0.3030444480600164
- Max = 0.9
- 75% = 0.725
- Median = 0.45
- 25% = 0.15
- Min = 0.15

#### facing_probas
- Mean = [0.02794048 0.11755308 0.06288244 0.74812847 0.74505084]
- Standard deviation = [0.02149    0.04989917 0.02680768 0.07079759 0.07832603]
- Max = [0.06233333 0.20105357 0.09789881 0.81525    0.82241071]
- 75% = [0.03910714 0.1455     0.09421379 0.80059722 0.80031101]
- Median = [0.02571429 0.12321131 0.05344048 0.77681944 0.76824802]
- 25% = [0.015      0.07521925 0.03672619 0.71670536 0.72598958]
- Min = [0.         0.03861905 0.03592063 0.59433333 0.58850794]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 73.5 | 6.5 |
| Actual Positive | 10.625 | 9.375 |

### robot-6
#### accuracy
- Mean = 0.5874999999999999
- Standard deviation = 0.09202581159652981
- Max = 0.72
- 75% = 0.665
- Median = 0.585
- 25% = 0.535
- Min = 0.45

#### f1
- Mean = 0.7358504804806234
- Standard deviation = 0.07439277080606213
- Max = 0.8372093023255813
- 75% = 0.7987664945496271
- Median = 0.7380573248407643
- 25% = 0.695995785036881
- Min = 0.6206896551724138

#### precision
- Mean = 1.0
- Standard deviation = 0.0
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 1.0
- Min = 1.0

#### recall
- Mean = 0.5874999999999999
- Standard deviation = 0.09202581159652981
- Max = 0.72
- 75% = 0.665
- Median = 0.585
- 25% = 0.535
- Min = 0.45

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
| Actual Positive | 41.25 | 58.75 |

