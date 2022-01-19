# ExtraTreesClassifier_RandomUnderSampler_2022-01-18-20-46_no2
## Constants
- CSV_PATH = ../out/csv/experiment
- OUTPUT_PATH = ../out/experiment_result/data_of_2022-01-13_eval_system/AGC-45angle-3m
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
- DISTANCE = [3]
- AGC_STATUS = ['AGC']

## Loaded CSV
- 2021-12-27_AGC.csv
- 2022-01-10_NoAGC.csv
- 2022-01-13_raspi_48000Hz_w1_N2^12_overlap80.csv

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
	- sampling_strategy_ = OrderedDict([(1, 36)])
	- sample_indices_ = [ 6  7  8  9 10 11 12 13 14 24 25 26 27 28 29 30 31 32 42 43 44 45 46 47
 48 49 50 60 61 62 63 64 65 66 67 68 69 72  4 22 57 53 15 54 51 33 35 17
 34 21 37 18 59  0 52  5 20  1 73 39  2 56 71  3 70 41 58 19 40 36 38 16]

- best_estimator
	- base_estimator = ExtraTreeClassifier()
	- n_estimators = 190
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
	- max_features = sqrt
	- max_leaf_nodes = None
	- min_impurity_decrease = 0.0
	- ccp_alpha = 0.0
	- n_features_in_ = 36
	- n_outputs_ = 1
	- classes_ = [0 1]
	- n_classes_ = 2
	- base_estimator_ = ExtraTreeClassifier()

#### Importance of features
- gp_max_val_mean = 0.1511510303556846
- gp_max_val_min = 0.11988711772880571
- gp_auc_mean = 0.1189318075437959
- gp_auc_min = 0.11286391777704832
- gp_auc_max = 0.11225733171398124
- gp_max_val_max = 0.10158747549902562
- srmr = 0.0766191947037089
- diff_auc = 0.0373471478043737
- diff_std = 0.03695757148855591
- high_power = 0.03363478475955004
- hlbr = 0.021608316921873653
- gp_max_ix_mean = 0.011018360408238507
- tdoa_mean = 0.010348091541534574
- coe1[0] = 0.00956053479756482
- gp_max_ix_std = 0.0058754221602055415
- low_power = 0.004504702684763803
- tdoa_std = 0.0038363841269381705
- coe1[1] = 0.0033543669520553518
- tdoa_min = 0.0031477399362332564
- ratio_max_to_10ms_ave_peaks = 0.0028095239783975548
- ac_auc = 0.0027586754250798176
- coe3[3] = 0.002376123223285528
- coe3[2] = 0.002061915478264599
- gp_auc_range = 0.0019307107702229336
- gp_max_ix_min = 0.0018255379605174092
- gp_max_val_range = 0.0016613755662183646
- ac_std = 0.0016550515174202781
- tdoa_range = 0.0016160432189868458
- gp_max_val_std = 0.0015440641204559936
- tdoa_max = 0.0014245284860650647
- gp_auc_std = 0.0012209435840203583
- ratio_max_to_9th_ave_peaks = 0.0011821889352967344
- gp_max_ix_range = 0.0009362570303267959
- gp_max_ix_max = 0.0005057618015039885
- coe3[0] = 0.0
- coe3[1] = 0.0

## Evaluation
cv = 8
### robot-1
#### accuracy
- Mean = 0.95625
- Standard deviation = 0.009921567416492224
- Max = 0.97
- 75% = 0.9624999999999999
- Median = 0.955
- 25% = 0.95
- Min = 0.94

#### f1
- Mean = 0.9018598523148573
- Standard deviation = 0.02019368204805447
- Max = 0.9302325581395349
- 75% = 0.9143763213530656
- Median = 0.898989898989899
- 25% = 0.888888888888889
- Min = 0.8695652173913044

#### precision
- Mean = 0.8218784838350056
- Standard deviation = 0.03357503217869353
- Max = 0.8695652173913043
- 75% = 0.8423913043478262
- Median = 0.8166666666666667
- 25% = 0.8
- Min = 0.7692307692307693

#### recall
- Mean = 1.0
- Standard deviation = 0.0
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 1.0
- Min = 1.0

#### facing_probas
- Mean = [0.96532589 0.86068362 0.15680583 0.02645851 0.02056974]
- Standard deviation = [0.00545565 0.01889044 0.03545753 0.01060803 0.00636727]
- Max = [0.97256492 0.8846793  0.20656242 0.03985587 0.02965038]
- 75% = [0.97086562 0.87315153 0.18016321 0.03809131 0.02701946]
- Median = [0.96409215 0.86495858 0.17123558 0.02467239 0.02003675]
- 25% = [0.9619141  0.8529139  0.12431804 0.01901822 0.01476961]
- Min = [0.95634204 0.82306258 0.10539336 0.01126553 0.01183344]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 75.625 | 4.375 |
| Actual Positive | 0.0 | 20.0 |

### robot-2
#### accuracy
- Mean = 0.95625
- Standard deviation = 0.009921567416492224
- Max = 0.97
- 75% = 0.9624999999999999
- Median = 0.955
- 25% = 0.95
- Min = 0.94

#### f1
- Mean = 0.8763216998511116
- Standard deviation = 0.03129581507471475
- Max = 0.9189189189189189
- 75% = 0.8963963963963965
- Median = 0.873015873015873
- 25% = 0.8571428571428571
- Min = 0.8235294117647058

#### precision
- Mean = 1.0
- Standard deviation = 0.0
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 1.0
- Min = 1.0

#### recall
- Mean = 0.78125
- Standard deviation = 0.04960783708246108
- Max = 0.85
- 75% = 0.8125
- Median = 0.775
- 25% = 0.75
- Min = 0.7

#### facing_probas
- Mean = [0.87882255 0.94239465 0.60949496 0.12868692 0.01446758]
- Standard deviation = [0.02184717 0.0099951  0.02806702 0.03941639 0.00411893]
- Max = [0.91150406 0.95918065 0.65101504 0.19412806 0.01989169]
- 75% = [0.88925026 0.94970093 0.63015204 0.15308128 0.0187427 ]
- Median = [0.88095718 0.94300799 0.60773983 0.13389261 0.01385425]
- 25% = [0.87215113 0.93407867 0.59014304 0.09804508 0.01126901]
- Min = [0.83129386 0.92757802 0.56257191 0.07120035 0.00871294]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 80.0 | 0.0 |
| Actual Positive | 4.375 | 15.625 |

### robot-3
#### accuracy
- Mean = 0.9875
- Standard deviation = 0.01198957880828181
- Max = 1.0
- 75% = 1.0
- Median = 0.99
- 25% = 0.9775
- Min = 0.97

#### f1
- Mean = 0.9667405259510523
- Standard deviation = 0.03237234545254873
- Max = 1.0
- 75% = 1.0
- Median = 0.9743589743589743
- 25% = 0.9402560455192035
- Min = 0.9189189189189189

#### precision
- Mean = 1.0
- Standard deviation = 0.0
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 1.0
- Min = 1.0

#### recall
- Mean = 0.9375
- Standard deviation = 0.059947894041408996
- Max = 1.0
- 75% = 1.0
- Median = 0.95
- 25% = 0.8875
- Min = 0.85

#### facing_probas
- Mean = [0.24628172 0.94220669 0.97463639 0.89281934 0.13864596]
- Standard deviation = [0.03175395 0.01108954 0.00354011 0.01799726 0.02120232]
- Max = [0.30843221 0.95739792 0.98097652 0.91344578 0.17706614]
- 75% = [0.26191337 0.95019553 0.97664517 0.90922661 0.15414966]
- Median = [0.24526634 0.94341739 0.97447353 0.89416955 0.12928477]
- 25% = [0.22821544 0.93538001 0.9727853  0.88296084 0.12336453]
- Min = [0.19308959 0.92451265 0.968258   0.85860581 0.11377303]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 80.0 | 0.0 |
| Actual Positive | 1.25 | 18.75 |

### robot-4
#### accuracy
- Mean = 0.945
- Standard deviation = 0.016583123951776982
- Max = 0.97
- 75% = 0.955
- Median = 0.94
- 25% = 0.9375
- Min = 0.92

#### f1
- Mean = 0.8639103499072303
- Standard deviation = 0.04220871618289934
- Max = 0.9268292682926829
- 75% = 0.8935599284436495
- Median = 0.8535714285714286
- 25% = 0.8426282051282051
- Min = 0.8000000000000002

#### precision
- Mean = 0.8548130454594985
- Standard deviation = 0.045333086138998724
- Max = 0.9473684210526315
- 75% = 0.8636904761904762
- Median = 0.8460526315789474
- 25% = 0.8241106719367589
- Min = 0.8

#### recall
- Mean = 0.875
- Standard deviation = 0.05590169943749472
- Max = 0.95
- 75% = 0.9125
- Median = 0.875
- 25% = 0.8375
- Min = 0.8

#### facing_probas
- Mean = [0.01769021 0.26793928 0.91304951 0.9643123  0.72338294]
- Standard deviation = [0.00607937 0.03124739 0.01174658 0.0070074  0.04273512]
- Max = [0.02530372 0.31808408 0.92833715 0.97543899 0.78181305]
- 75% = [0.0237787  0.28390746 0.92202567 0.96761896 0.75605968]
- Median = [0.01803264 0.25983009 0.9172631  0.96407023 0.72360394]
- 25% = [0.01202305 0.25118953 0.90342725 0.962076   0.69896597]
- Min = [0.00949831 0.22700137 0.89216328 0.94990833 0.6484022 ]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 77.0 | 3.0 |
| Actual Positive | 2.5 | 17.5 |

### robot-5
#### accuracy
- Mean = 0.97
- Standard deviation = 0.010000000000000009
- Max = 0.99
- 75% = 0.9724999999999999
- Median = 0.97
- 25% = 0.96
- Min = 0.96

#### f1
- Mean = 0.9181438523543787
- Standard deviation = 0.028687053273711956
- Max = 0.9743589743589743
- 75% = 0.926031294452347
- Median = 0.9189189189189189
- 25% = 0.888888888888889
- Min = 0.888888888888889

#### precision
- Mean = 1.0
- Standard deviation = 0.0
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 1.0
- Min = 1.0

#### recall
- Mean = 0.85
- Standard deviation = 0.049999999999999975
- Max = 0.95
- 75% = 0.8625
- Median = 0.85
- 25% = 0.8
- Min = 0.8

#### facing_probas
- Mean = [0.01086819 0.01784829 0.29014533 0.9550861  0.96586579]
- Standard deviation = [0.00237764 0.00579733 0.01826546 0.00749821 0.00533187]
- Max = [0.01368853 0.0265704  0.31939922 0.96844913 0.97315684]
- 75% = [0.01251781 0.02345167 0.30774846 0.96124487 0.96956649]
- Median = [0.01186453 0.01694037 0.28288427 0.95201472 0.96762526]
- 25% = [0.00882237 0.01271178 0.27850293 0.94987613 0.96182184]
- Min = [0.00657009 0.00988806 0.2662552  0.94544246 0.95782547]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 80.0 | 0.0 |
| Actual Positive | 3.0 | 17.0 |

### robot-6
#### accuracy
- Mean = 0.88875
- Standard deviation = 0.026663411259626922
- Max = 0.94
- 75% = 0.9
- Median = 0.895
- 25% = 0.8674999999999999
- Min = 0.85

#### f1
- Mean = 0.940888469380296
- Standard deviation = 0.014887694388923586
- Max = 0.9690721649484536
- 75% = 0.9473684210526316
- Median = 0.9445836814257866
- 25% = 0.9290437582657696
- Min = 0.9189189189189189

#### precision
- Mean = 1.0
- Standard deviation = 0.0
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 1.0
- Min = 1.0

#### recall
- Mean = 0.88875
- Standard deviation = 0.026663411259626922
- Max = 0.94
- 75% = 0.9
- Median = 0.895
- 25% = 0.8674999999999999
- Min = 0.85

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
| Actual Positive | 11.125 | 88.875 |

