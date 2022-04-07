# ExtraTreesClassifier_SMOTE_2022-01-20-03-15_no4
## Constants
- CSV_PATH = ../out/csv/experiment
- OUTPUT_PATH = ../out/experiment_result/data_of_2022-01-13_eval_system/NoAGC-45angle-1m
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
- DISTANCE = [1]
- AGC_STATUS = ['NoAGC']

## Loaded CSV
- 2021-12-27_AGC.csv
- 2022-01-10_NoAGC.csv
- 2022-01-13_raspi_48000Hz_w1_N2^12_overlap80.csv

## Estimator
### Type
- resampler = SMOTE
- estimator = ExtraTreesClassifier

### Arguments for hyperparameter search
- resampler = SMOTE
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
	- k_neighbors = 5
	- n_jobs = -1
	- n_features_in_ = 36
	- sampling_strategy_ = OrderedDict([(0, 3)])
	- nn_k_ = NearestNeighbors(n_neighbors=6)

- best_estimator
	- base_estimator = ExtraTreeClassifier()
	- n_estimators = 210
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
	- min_samples_leaf = 10
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
	- oob_decision_function_ = [[0.14696266 0.85303734]
 [0.20315424 0.79684576]
 [0.13581768 0.86418232]
 [0.10966664 0.89033336]
 [0.1929383  0.8070617 ]
 [0.15338966 0.84661034]
 [0.28469364 0.71530636]
 [0.37119642 0.62880358]
 [0.39697777 0.60302223]
 [0.93515343 0.06484657]
 [0.93678138 0.06321862]
 [0.9181232  0.0818768 ]
 [0.78938622 0.21061378]
 [0.92968995 0.07031005]
 [0.91133724 0.08866276]
 [0.49325703 0.50674297]
 [0.68042985 0.31957015]
 [0.52115597 0.47884403]
 [0.1156288  0.8843712 ]
 [0.15753445 0.84246555]
 [0.10977933 0.89022067]
 [0.11548179 0.88451821]
 [0.1134694  0.8865306 ]
 [0.12642415 0.87357585]
 [0.90510663 0.09489337]
 [0.84978908 0.15021092]
 [0.82715027 0.17284973]
 [0.91084271 0.08915729]
 [0.9202838  0.0797162 ]
 [0.93036882 0.06963118]
 [0.83880291 0.16119709]
 [0.83732035 0.16267965]
 [0.83597343 0.16402657]
 [0.16160691 0.83839309]
 [0.14103637 0.85896363]
 [0.13664307 0.86335693]
 [0.09617168 0.90382832]
 [0.10073232 0.89926768]
 [0.11965066 0.88034934]
 [0.23218945 0.76781055]
 [0.22241469 0.77758531]
 [0.26044025 0.73955975]
 [0.83654396 0.16345604]
 [0.75119115 0.24880885]
 [0.84815548 0.15184452]
 [0.91914549 0.08085451]
 [0.94243064 0.05756936]
 [0.92991876 0.07008124]
 [0.82766641 0.17233359]
 [0.89234416 0.10765584]
 [0.8699715  0.1300285 ]
 [0.47607699 0.52392301]
 [0.34921912 0.65078088]
 [0.35012078 0.64987922]
 [0.14253581 0.85746419]
 [0.18774052 0.81225948]
 [0.12577964 0.87422036]
 [0.14283485 0.85716515]
 [0.10051946 0.89948054]
 [0.11233201 0.88766799]
 [0.92296617 0.07703383]
 [0.93539919 0.06460081]
 [0.93405308 0.06594692]
 [0.93118283 0.06881717]
 [0.932174   0.067826  ]
 [0.93897797 0.06102203]
 [0.76723168 0.23276832]
 [0.36579992 0.63420008]
 [0.46806177 0.53193823]
 [0.14251175 0.85748825]
 [0.15384326 0.84615674]
 [0.14907582 0.85092418]
 [0.13771235 0.86228765]
 [0.16138475 0.83861525]
 [0.10710404 0.89289596]
 [0.9271736  0.0728264 ]
 [0.38841473 0.61158527]
 [0.79465255 0.20534745]]
	- oob_score_ = 0.8974358974358975

#### Importance of features
- gp_max_val_max = 0.15287481070692113
- gp_auc_mean = 0.1486484349490101
- gp_max_val_mean = 0.13863193065016466
- gp_auc_max = 0.12785266128194173
- gp_auc_min = 0.07058623742875193
- gp_max_val_min = 0.0669171431109018
- srmr = 0.05682365692906926
- hlbr = 0.056560166858538694
- gp_max_ix_std = 0.02978637374486151
- tdoa_std = 0.023923444976076555
- gp_max_ix_min = 0.022743292891319208
- tdoa_mean = 0.02166764620069561
- gp_max_ix_range = 0.019350324302443156
- ratio_max_to_10ms_ave_peaks = 0.016013953042229526
- tdoa_range = 0.013483419978833601
- tdoa_min = 0.012902356641823825
- coe1[1] = 0.004784688995215311
- tdoa_max = 0.004784688995215311
- diff_auc = 0.004314226997009399
- gp_max_ix_mean = 0.0034860481003575403
- coe1[0] = 0.0016133058943802459
- gp_max_ix_max = 0.0009717106712537814
- gp_auc_range = 0.00042155626971849153
- gp_max_val_std = 0.00034883116403953263
- high_power = 0.00034496936062730074
- gp_max_val_range = 0.0001006487976339791
- gp_auc_std = 5.205367690176556e-05
- coe3[2] = 1.141738406506455e-05
- low_power = 0.0
- coe3[0] = 0.0
- coe3[1] = 0.0
- coe3[3] = 0.0
- ratio_max_to_9th_ave_peaks = 0.0
- ac_std = 0.0
- ac_auc = 0.0
- diff_std = 0.0

## Evaluation
cv = 8
### robot-1
#### accuracy
- Mean = 0.9975
- Standard deviation = 0.004330127018922197
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 0.9975
- Min = 0.99

#### f1
- Mean = 0.9935897435897436
- Standard deviation = 0.011102889792108196
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 0.9935897435897436
- Min = 0.9743589743589743

#### precision
- Mean = 1.0
- Standard deviation = 0.0
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 1.0
- Min = 1.0

#### recall
- Mean = 0.9875
- Standard deviation = 0.021650635094610987
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 0.9875
- Min = 0.95

#### facing_probas
- Mean = [0.86582208 0.57255721 0.18865617 0.06625561 0.07170336]
- Standard deviation = [0.02655026 0.07599184 0.05287047 0.02003341 0.02601266]
- Max = [0.90394359 0.68747525 0.27291    0.11651778 0.13746848]
- 75% = [0.88037534 0.61243806 0.22956271 0.06618726 0.0714813 ]
- Median = [0.87088379 0.56474553 0.18577124 0.06192587 0.06445818]
- 25% = [0.85226064 0.54141319 0.14257482 0.05635913 0.05881238]
- Min = [0.81650054 0.43154428 0.12027457 0.04677163 0.04751691]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 80.0 | 0.0 |
| Actual Positive | 0.25 | 19.75 |

### robot-2
#### accuracy
- Mean = 0.98125
- Standard deviation = 0.012686114456365286
- Max = 0.99
- 75% = 0.99
- Median = 0.99
- 25% = 0.975
- Min = 0.96

#### f1
- Mean = 0.9540711828821584
- Standard deviation = 0.029558569856564746
- Max = 0.975609756097561
- 75% = 0.9743589743589743
- Median = 0.9743589743589743
- 25% = 0.9386904761904762
- Min = 0.9047619047619048

#### precision
- Mean = 0.9537067099567099
- Standard deviation = 0.0556923544085225
- Max = 1.0
- 75% = 1.0
- Median = 0.9761904761904762
- 25% = 0.9284090909090909
- Min = 0.8636363636363636

#### recall
- Mean = 0.9562499999999999
- Standard deviation = 0.016535945694153707
- Max = 1.0
- 75% = 0.95
- Median = 0.95
- 25% = 0.95
- Min = 0.95

#### facing_probas
- Mean = [0.85489611 0.87720245 0.8506095  0.17151209 0.08647842]
- Standard deviation = [0.01774067 0.01755897 0.02454537 0.03452528 0.01441588]
- Max = [0.87594956 0.89799548 0.87388059 0.22384709 0.12039324]
- 75% = [0.86407255 0.88811937 0.86329137 0.19348795 0.08892954]
- Median = [0.86035351 0.87927244 0.85679651 0.17913869 0.08411209]
- 25% = [0.85212715 0.87482689 0.85070298 0.15289624 0.07809271]
- Min = [0.81361476 0.83532126 0.79189212 0.11525789 0.06853889]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 79.0 | 1.0 |
| Actual Positive | 0.875 | 19.125 |

### robot-3
#### accuracy
- Mean = 0.82125
- Standard deviation = 0.012686114456365237
- Max = 0.84
- 75% = 0.83
- Median = 0.825
- 25% = 0.81
- Min = 0.8

#### f1
- Mean = 0.18602955015998496
- Standard deviation = 0.10583737160631342
- Max = 0.33333333333333337
- 75% = 0.2608695652173913
- Median = 0.22134387351778656
- 25% = 0.09523809523809523
- Min = 0.0

#### precision
- Mean = 0.875
- Standard deviation = 0.33071891388307384
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 1.0
- Min = 0.0

#### recall
- Mean = 0.10625
- Standard deviation = 0.06343057228182637
- Max = 0.2
- 75% = 0.15
- Median = 0.125
- 25% = 0.05
- Min = 0.0

#### facing_probas
- Mean = [0.55508868 0.85870425 0.86715387 0.58300921 0.45633634]
- Standard deviation = [0.08730739 0.03689069 0.02944958 0.07269507 0.07932936]
- Max = [0.6873642  0.90569313 0.90525549 0.68037043 0.58704194]
- 75% = [0.58286111 0.88298418 0.88743382 0.61900626 0.48476895]
- Median = [0.54166221 0.86660903 0.87498661 0.58590279 0.43841031]
- 25% = [0.51979374 0.84804268 0.85236948 0.55804147 0.42222631]
- Min = [0.4037203  0.78657581 0.80813914 0.44227402 0.32114174]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 80.0 | 0.0 |
| Actual Positive | 17.875 | 2.125 |

### robot-4
#### accuracy
- Mean = 0.9675
- Standard deviation = 0.004330127018922197
- Max = 0.97
- 75% = 0.97
- Median = 0.97
- 25% = 0.9675
- Min = 0.96

#### f1
- Mean = 0.9142214076424603
- Standard deviation = 0.013130111573204178
- Max = 0.9230769230769231
- 75% = 0.9230769230769231
- Median = 0.920997920997921
- 25% = 0.912873399715505
- Min = 0.888888888888889

#### precision
- Mean = 0.9667397660818713
- Standard deviation = 0.025779853764009316
- Max = 1.0
- 75% = 1.0
- Median = 0.9473684210526315
- 25% = 0.9473684210526315
- Min = 0.9444444444444444

#### recall
- Mean = 0.8687499999999999
- Standard deviation = 0.03479852726768764
- Max = 0.9
- 75% = 0.9
- Median = 0.875
- 25% = 0.85
- Min = 0.8

#### facing_probas
- Mean = [0.07666079 0.20203079 0.77773999 0.86242096 0.84547375]
- Standard deviation = [0.02546832 0.05122503 0.05096385 0.02755665 0.0336322 ]
- Max = [0.14051096 0.26940466 0.85173053 0.89958073 0.89366659]
- 75% = [0.07590071 0.25138808 0.81152206 0.87653698 0.85886368]
- Median = [0.06827879 0.20713541 0.77006544 0.86796577 0.84479578]
- 25% = [0.06547916 0.14754507 0.75888284 0.85160963 0.8354561 ]
- Min = [0.05291034 0.13789027 0.68355412 0.81348887 0.78536735]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 79.375 | 0.625 |
| Actual Positive | 2.625 | 17.375 |

### robot-5
#### accuracy
- Mean = 0.9737499999999999
- Standard deviation = 0.0048412291827592754
- Max = 0.98
- 75% = 0.98
- Median = 0.97
- 25% = 0.97
- Min = 0.97

#### f1
- Mean = 0.9364111498257839
- Standard deviation = 0.012370155867677587
- Max = 0.9523809523809523
- 75% = 0.9523809523809523
- Median = 0.9268292682926829
- 25% = 0.9268292682926829
- Min = 0.9268292682926829

#### precision
- Mean = 0.9063852813852814
- Standard deviation = 0.0020957702089866802
- Max = 0.9090909090909091
- 75% = 0.9090909090909091
- Median = 0.9047619047619048
- 25% = 0.9047619047619048
- Min = 0.9047619047619048

#### recall
- Mean = 0.96875
- Standard deviation = 0.024206145913796374
- Max = 1.0
- 75% = 1.0
- Median = 0.95
- 25% = 0.95
- Min = 0.95

#### facing_probas
- Mean = [0.08159095 0.07165186 0.24355369 0.89409121 0.88503275]
- Standard deviation = [0.02476696 0.01848669 0.0528409  0.02329236 0.02456796]
- Max = [0.14112406 0.11379654 0.32745678 0.91799067 0.91242536]
- 75% = [0.08157271 0.0736742  0.27260072 0.91134752 0.90248445]
- Median = [0.07563818 0.06967892 0.24160609 0.90575967 0.89571409]
- 25% = [0.07006697 0.06004938 0.21352562 0.87891297 0.87019149]
- Min = [0.05506594 0.04788174 0.15069175 0.85348757 0.84090112]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 78.0 | 2.0 |
| Actual Positive | 0.625 | 19.375 |

### robot-6
#### accuracy
- Mean = 0.7775000000000001
- Standard deviation = 0.015612494995996009
- Max = 0.8
- 75% = 0.79
- Median = 0.78
- 25% = 0.76
- Min = 0.76

#### f1
- Mean = 0.874737396213819
- Standard deviation = 0.009881825177829989
- Max = 0.888888888888889
- 75% = 0.8826815642458101
- Median = 0.8763690307104757
- 25% = 0.8636363636363636
- Min = 0.8636363636363636

#### precision
- Mean = 1.0
- Standard deviation = 0.0
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 1.0
- Min = 1.0

#### recall
- Mean = 0.7775000000000001
- Standard deviation = 0.015612494995996009
- Max = 0.8
- 75% = 0.79
- Median = 0.78
- 25% = 0.76
- Min = 0.76

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
| Actual Positive | 22.25 | 77.75 |

