# ExtraTreesClassifier_ClusterCentroids_2022-01-17-17-15_no1
## Constants
- CSV_PATH = ../out/csv/experiment
- OUTPUT_PATH = ../out/experiment_result/data_of_2022-01-13_eval_system/AGC-0angle-under5m
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
- DISTANCE = [1, 3, 5]
- AGC_STATUS = ['AGC']

## Loaded CSV
- 2021-12-27_AGC.csv
- 2022-01-10_NoAGC.csv
- 2022-01-13_raspi_48000Hz_w1_N2^12_overlap80.csv

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
	- sampling_strategy_ = OrderedDict([(0, 45)])
	- estimator_ = KMeans(n_clusters=45, random_state=42)
	- voting_ = soft

- best_estimator
	- base_estimator = ExtraTreeClassifier()
	- n_estimators = 330
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
	- max_features = None
	- max_leaf_nodes = None
	- min_impurity_decrease = 0.0
	- ccp_alpha = 0.0
	- n_features_in_ = 36
	- n_outputs_ = 1
	- classes_ = [0 1]
	- n_classes_ = 2
	- base_estimator_ = ExtraTreeClassifier()
	- oob_decision_function_ = [[0.90547264 0.09452736]
 [0.59895833 0.40104167]
 [0.96410256 0.03589744]
 [0.98086124 0.01913876]
 [0.955      0.045     ]
 [0.9902439  0.0097561 ]
 [0.995      0.005     ]
 [0.96703297 0.03296703]
 [0.99459459 0.00540541]
 [0.9950495  0.0049505 ]
 [0.81188119 0.18811881]
 [0.96634615 0.03365385]
 [0.85221675 0.14778325]
 [0.81538462 0.18461538]
 [0.04950495 0.95049505]
 [0.92574257 0.07425743]
 [0.97087379 0.02912621]
 [0.79816514 0.20183486]
 [0.71782178 0.28217822]
 [0.70673077 0.29326923]
 [0.99512195 0.00487805]
 [0.97584541 0.02415459]
 [0.55307263 0.44692737]
 [0.97058824 0.02941176]
 [0.98947368 0.01052632]
 [0.85204082 0.14795918]
 [0.59615385 0.40384615]
 [0.51530612 0.48469388]
 [0.93478261 0.06521739]
 [0.85714286 0.14285714]
 [0.88839286 0.11160714]
 [0.95918367 0.04081633]
 [0.94       0.06      ]
 [0.89855072 0.10144928]
 [0.79274611 0.20725389]
 [0.43147208 0.56852792]
 [0.5106383  0.4893617 ]
 [0.46411483 0.53588517]
 [0.97159091 0.02840909]
 [0.81773399 0.18226601]
 [0.95454545 0.04545455]
 [0.98       0.02      ]
 [0.94300518 0.05699482]
 [0.99509804 0.00490196]
 [0.96244131 0.03755869]
 [0.22051282 0.77948718]
 [0.21105528 0.78894472]
 [0.00956938 0.99043062]
 [0.09004739 0.90995261]
 [0.03125    0.96875   ]
 [0.03827751 0.96172249]
 [0.35148515 0.64851485]
 [0.34693878 0.65306122]
 [0.11111111 0.88888889]
 [0.04926108 0.95073892]
 [0.03535354 0.96464646]
 [0.02173913 0.97826087]
 [0.00543478 0.99456522]
 [0.24102564 0.75897436]
 [0.01010101 0.98989899]
 [0.35294118 0.64705882]
 [0.16836735 0.83163265]
 [0.1319797  0.8680203 ]
 [0.05494505 0.94505495]
 [0.02272727 0.97727273]
 [0.01538462 0.98461538]
 [0.01470588 0.98529412]
 [0.01470588 0.98529412]
 [0.00490196 0.99509804]
 [0.18137255 0.81862745]
 [0.16080402 0.83919598]
 [0.08045977 0.91954023]
 [0.04060914 0.95939086]
 [0.0097561  0.9902439 ]
 [0.03902439 0.96097561]
 [0.12676056 0.87323944]
 [0.04830918 0.95169082]
 [0.06435644 0.93564356]
 [0.10900474 0.89099526]
 [0.13636364 0.86363636]
 [0.76649746 0.23350254]
 [0.10362694 0.89637306]
 [0.04878049 0.95121951]
 [0.02525253 0.97474747]
 [0.13333333 0.86666667]
 [0.00985222 0.99014778]
 [0.01522843 0.98477157]
 [0.21938776 0.78061224]
 [0.1319797  0.8680203 ]
 [0.1758794  0.8241206 ]]
	- oob_score_ = 0.9555555555555556

#### Importance of features
- gp_max_val_min = 0.1541098132070856
- gp_auc_min = 0.1362469744771867
- gp_auc_max = 0.07621168565160166
- gp_max_val_max = 0.07025820467948295
- gp_auc_mean = 0.06952615880514985
- gp_max_val_mean = 0.06895678124376405
- tdoa_mean = 0.03394086806194499
- gp_max_ix_mean = 0.033842244619147276
- gp_max_ix_std = 0.029641830201944507
- gp_max_ix_max = 0.027044702970945876
- tdoa_max = 0.02488526252692468
- srmr = 0.022399999765363478
- diff_auc = 0.022283286272201767
- tdoa_std = 0.021970449527631896
- gp_max_ix_min = 0.019788423567502902
- gp_max_ix_range = 0.01888516067104592
- tdoa_min = 0.01546411787375281
- ac_auc = 0.015394548606194438
- high_power = 0.013124362541062097
- hlbr = 0.013112143969267187
- tdoa_range = 0.013058172773551972
- ac_std = 0.013018530793054034
- diff_std = 0.012205461631651038
- coe1[1] = 0.012012527937253565
- coe3[2] = 0.009391175655585943
- gp_auc_range = 0.007372135095409363
- ratio_max_to_9th_ave_peaks = 0.007238116749444888
- gp_max_val_std = 0.006698086875898621
- gp_max_val_range = 0.006467335358390352
- gp_auc_std = 0.006401045576876562
- low_power = 0.005811881714094686
- coe3[3] = 0.004688283428315285
- ratio_max_to_10ms_ave_peaks = 0.004446452692965828
- coe1[0] = 0.0041037744783072065
- coe3[0] = 0.0
- coe3[1] = 0.0

## Evaluation
cv = 8
### robot-1
#### accuracy
- Mean = 0.9724191750278708
- Standard deviation = 0.008650024648241782
- Max = 0.9866220735785953
- 75% = 0.9774247491638797
- Median = 0.973288740245262
- 25% = 0.9665551839464883
- Min = 0.9565217391304348

#### f1
- Mean = 0.93088801142272
- Standard deviation = 0.02208244195347242
- Max = 0.9661016949152542
- 75% = 0.9441115702479338
- Median = 0.9327683615819209
- 25% = 0.9189244663382594
- Min = 0.8888888888888888

#### precision
- Mean = 0.9357863996963733
- Standard deviation = 0.02847559324927506
- Max = 0.9827586206896551
- 75% = 0.9487068965517241
- Median = 0.9404274004683841
- 25% = 0.9280701754385965
- Min = 0.8787878787878788

#### recall
- Mean = 0.9270833333333334
- Standard deviation = 0.033268165463898554
- Max = 0.9666666666666667
- 75% = 0.95
- Median = 0.9416666666666667
- 25% = 0.9083333333333333
- Min = 0.8666666666666667

#### facing_probas
- Mean = [0.86791035 0.53294823 0.1567803  0.04034722 0.03104798]
- Standard deviation = [0.02169546 0.04486704 0.026762   0.01095417 0.00913638]
- Max = [0.90040404 0.60919192 0.20323232 0.06191919 0.04808081]
- 75% = [0.88255051 0.56856061 0.16844697 0.04454545 0.03574495]
- Median = [0.87260101 0.51744949 0.15871212 0.04237374 0.03106061]
- 25% = [0.85186869 0.50405303 0.14455808 0.02960859 0.02619949]
- Min = [0.83040404 0.46762626 0.11439394 0.02727273 0.01535354]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 235.25 | 3.875 |
| Actual Positive | 4.375 | 55.625 |

### robot-2
#### accuracy
- Mean = 0.9155908584169454
- Standard deviation = 0.015280396640241594
- Max = 0.9364548494983278
- 75% = 0.9272575250836121
- Median = 0.9163879598662208
- 25% = 0.9065886287625418
- Min = 0.8862876254180602

#### f1
- Mean = 0.7772394645052315
- Standard deviation = 0.03796194916052182
- Max = 0.8264462809917356
- 75% = 0.8064220183486239
- Median = 0.7751320601381553
- 25% = 0.7564655172413792
- Min = 0.706896551724138

#### precision
- Mean = 0.8296507437390455
- Standard deviation = 0.058519740761884875
- Max = 0.9183673469387755
- 75% = 0.8834042553191489
- Median = 0.8136822194199244
- 25% = 0.7964285714285715
- Min = 0.7321428571428571

#### recall
- Mean = 0.7333333333333333
- Standard deviation = 0.04330127018922195
- Max = 0.8333333333333334
- 75% = 0.7374999999999999
- Median = 0.7333333333333333
- 25% = 0.7
- Min = 0.6833333333333333

#### facing_probas
- Mean = [0.72971591 0.86700126 0.5884154  0.18958965 0.03053662]
- Standard deviation = [0.04545381 0.0241574  0.02871249 0.02625887 0.00903137]
- Max = [0.80525253 0.91       0.63222222 0.2280303  0.0429798 ]
- 75% = [0.75530303 0.88051768 0.59948232 0.20715909 0.03772727]
- Median = [0.735      0.86868687 0.59505051 0.18974747 0.03260101]
- 25% = [0.70607323 0.84840909 0.58316919 0.17455808 0.02405303]
- Min = [0.63979798 0.82868687 0.52671717 0.14151515 0.01575758]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 229.875 | 9.25 |
| Actual Positive | 16.0 | 44.0 |

### robot-3
#### accuracy
- Mean = 0.9110033444816052
- Standard deviation = 0.016539027960176405
- Max = 0.9331103678929766
- 75% = 0.923913043478261
- Median = 0.9130434782608696
- 25% = 0.8996655518394648
- Min = 0.88

#### f1
- Mean = 0.7918002526080987
- Standard deviation = 0.03518211561651115
- Max = 0.8307692307692307
- 75% = 0.8170021186440678
- Median = 0.8004201680672269
- 25% = 0.7754811119030648
- Min = 0.7230769230769231

#### precision
- Mean = 0.7513399281773765
- Standard deviation = 0.05569809448321112
- Max = 0.8448275862068966
- 75% = 0.7819612590799032
- Median = 0.7533206831119544
- 25% = 0.7059716599190283
- Min = 0.6714285714285714

#### recall
- Mean = 0.8416666666666668
- Standard deviation = 0.05270462766947299
- Max = 0.9
- 75% = 0.9
- Median = 0.8416666666666667
- 25% = 0.7958333333333334
- Min = 0.7666666666666667

#### facing_probas
- Mean = [0.34049242 0.81093434 0.91845328 0.58789141 0.16952652]
- Standard deviation = [0.05182886 0.05297593 0.02255322 0.05052786 0.0408067 ]
- Max = [0.42368687 0.89005051 0.94005051 0.68515152 0.23494949]
- 75% = [0.38150253 0.83877525 0.93625    0.61765152 0.19787879]
- Median = [0.33058081 0.81760101 0.92361111 0.57381313 0.16984848]
- 25% = [0.30640152 0.77511364 0.91065657 0.56320707 0.14570707]
- Min = [0.27191919 0.71424242 0.86626263 0.50520202 0.1080303 ]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 222.0 | 17.125 |
| Actual Positive | 9.5 | 50.5 |

### robot-4
#### accuracy
- Mean = 0.9118380713489409
- Standard deviation = 0.017130244512830524
- Max = 0.9364548494983278
- 75% = 0.9264214046822743
- Median = 0.9113712374581939
- 25% = 0.9046822742474916
- Min = 0.8833333333333333

#### f1
- Mean = 0.7966267226837742
- Standard deviation = 0.042412330047913484
- Max = 0.8571428571428571
- 75% = 0.8258907077515648
- Median = 0.8026928191489362
- 25% = 0.7745511811023622
- Min = 0.7286821705426356

#### precision
- Mean = 0.7311534928076316
- Standard deviation = 0.03477776277533145
- Max = 0.7846153846153846
- 75% = 0.7525675675675676
- Median = 0.7372122762148338
- 25% = 0.6965077605321508
- Min = 0.6811594202898551

#### recall
- Mean = 0.8775776836158192
- Standard deviation = 0.07116863420410678
- Max = 0.9661016949152542
- 75% = 0.9533898305084746
- Median = 0.864406779661017
- 25% = 0.8314265536723163
- Min = 0.7796610169491526

#### facing_probas
- Mean = [0.04861999 0.27591872 0.66358222 0.89391628 0.55988925]
- Standard deviation = [0.01654585 0.02944028 0.06005994 0.01435166 0.04509866]
- Max = [0.06985105 0.30344119 0.74643041 0.91032357 0.60503338]
- 75% = [0.06087571 0.29425141 0.70508475 0.90233693 0.59102465]
- Median = [0.05321007 0.28834104 0.66927495 0.89798151 0.57628017]
- 25% = [0.03843285 0.2720981  0.63848228 0.89012583 0.54590395]
- Min = [0.01987673 0.21417565 0.53888033 0.8645095  0.45690806]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 220.875 | 19.125 |
| Actual Positive | 7.25 | 51.875 |

### robot-5
#### accuracy
- Mean = 0.9339757525083612
- Standard deviation = 0.009107902746191873
- Max = 0.9464882943143813
- 75% = 0.9406354515050168
- Median = 0.9347826086956522
- 25% = 0.9291053511705686
- Min = 0.9163879598662207

#### f1
- Mean = 0.8020933749464527
- Standard deviation = 0.033066435905248305
- Max = 0.846153846153846
- 75% = 0.8263849229011992
- Median = 0.805940594059406
- 25% = 0.7847866419294991
- Min = 0.7368421052631579

#### precision
- Mean = 1.0
- Standard deviation = 0.0
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 1.0
- Min = 1.0

#### recall
- Mean = 0.6708333333333334
- Standard deviation = 0.04545296714431546
- Max = 0.7333333333333333
- 75% = 0.7041666666666666
- Median = 0.675
- 25% = 0.6458333333333334
- Min = 0.5833333333333334

#### facing_probas
- Mean = [0.0286553  0.04918561 0.33272096 0.78284091 0.86629419]
- Standard deviation = [0.01010991 0.01702437 0.03084381 0.03058772 0.02847053]
- Max = [0.04585859 0.07252525 0.38914141 0.83166667 0.90792929]
- 75% = [0.03381313 0.06247475 0.3510101  0.80660354 0.88294192]
- Median = [0.02949495 0.05325758 0.33229798 0.78098485 0.87290404]
- 25% = [0.02237374 0.03517677 0.31521465 0.76445707 0.85709596]
- Min = [0.0109596  0.02383838 0.28282828 0.73181818 0.81131313]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 239.125 | 0.0 |
| Actual Positive | 19.75 | 40.25 |

### robot-6
#### accuracy
- Mean = 0.8098773690078038
- Standard deviation = 0.0197818602803094
- Max = 0.8394648829431438
- 75% = 0.8244147157190636
- Median = 0.8093645484949833
- 25% = 0.8001672240802675
- Min = 0.7733333333333333

#### f1
- Mean = 0.8948202670761993
- Standard deviation = 0.012122452882026282
- Max = 0.9127272727272727
- 75% = 0.9037552622310183
- Median = 0.8946357796911302
- 25% = 0.888985614598621
- Min = 0.8721804511278195

#### precision
- Mean = 1.0
- Standard deviation = 0.0
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 1.0
- Min = 1.0

#### recall
- Mean = 0.8098773690078038
- Standard deviation = 0.0197818602803094
- Max = 0.8394648829431438
- 75% = 0.8244147157190636
- Median = 0.8093645484949833
- 25% = 0.8001672240802675
- Min = 0.7733333333333333

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
| Actual Positive | 56.875 | 242.25 |

