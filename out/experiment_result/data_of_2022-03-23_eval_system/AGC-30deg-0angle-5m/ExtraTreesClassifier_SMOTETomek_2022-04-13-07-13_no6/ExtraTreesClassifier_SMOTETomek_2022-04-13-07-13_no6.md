# ExtraTreesClassifier_SMOTETomek_2022-04-13-07-13_no6
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
- resampler = SMOTETomek
- estimator = ExtraTreesClassifier

### Arguments for hyperparameter search
- resampler = SMOTETomek
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
	- tomek = None
	- n_jobs = -1
	- n_features_in_ = 36
	- sampling_strategy_ = auto
	- smote_ = SMOTE(n_jobs=-1, random_state=42)
	- tomek_ = TomekLinks(n_jobs=-1, sampling_strategy='all')

- best_estimator
	- base_estimator = ExtraTreeClassifier()
	- n_estimators = 170
	- estimator_params = ('criterion', 'max_depth', 'min_samples_split', 'min_samples_leaf', 'min_weight_fraction_leaf', 'max_features', 'max_leaf_nodes', 'min_impurity_decrease', 'random_state', 'ccp_alpha')
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
	- ccp_alpha = 0.0
	- n_features_in_ = 36
	- n_outputs_ = 1
	- classes_ = [0 1]
	- n_classes_ = 2
	- base_estimator_ = ExtraTreeClassifier()
	- oob_decision_function_ = [[0.33333333 0.66666667]
 [0.42675159 0.57324841]
 [0.32911392 0.67088608]
 [0.45       0.55      ]
 [0.52631579 0.47368421]
 [0.41614907 0.58385093]
 [0.71895425 0.28104575]
 [0.62913907 0.37086093]
 [0.8590604  0.1409396 ]
 [0.85185185 0.14814815]
 [0.78980892 0.21019108]
 [0.59493671 0.40506329]
 [0.61935484 0.38064516]
 [0.74834437 0.25165563]
 [0.34177215 0.65822785]
 [0.46875    0.53125   ]
 [0.31410256 0.68589744]
 [0.68553459 0.31446541]
 [0.45394737 0.54605263]
 [0.52201258 0.47798742]
 [0.67080745 0.32919255]
 [0.71794872 0.28205128]
 [0.79617834 0.20382166]
 [0.71153846 0.28846154]
 [0.69536424 0.30463576]
 [0.74675325 0.25324675]
 [0.75974026 0.24025974]
 [0.4516129  0.5483871 ]
 [0.675      0.325     ]
 [0.42857143 0.57142857]
 [0.41139241 0.58860759]
 [0.5375     0.4625    ]
 [0.48734177 0.51265823]
 [0.42405063 0.57594937]
 [0.40909091 0.59090909]
 [0.55279503 0.44720497]
 [0.46405229 0.53594771]
 [0.77358491 0.22641509]
 [0.73856209 0.26143791]
 [0.64516129 0.35483871]
 [0.75974026 0.24025974]
 [0.50657895 0.49342105]
 [0.66025641 0.33974359]
 [0.30263158 0.69736842]
 [0.30246914 0.69753086]
 [0.33333333 0.66666667]
 [0.28666667 0.71333333]
 [0.80625    0.19375   ]
 [0.87820513 0.12179487]
 [0.79084967 0.20915033]
 [0.78846154 0.21153846]
 [0.70807453 0.29192547]
 [0.72903226 0.27096774]
 [0.77631579 0.22368421]
 [0.34375    0.65625   ]
 [0.64968153 0.35031847]
 [0.61842105 0.38157895]
 [0.32903226 0.67096774]
 [0.27564103 0.72435897]
 [0.33757962 0.66242038]
 [0.33333333 0.66666667]
 [0.35761589 0.64238411]
 [0.29677419 0.70322581]
 [0.43870968 0.56129032]
 [0.32098765 0.67901235]
 [0.26415094 0.73584906]
 [0.26923077 0.73076923]
 [0.27096774 0.72903226]
 [0.30120482 0.69879518]
 [0.28571429 0.71428571]
 [0.25333333 0.74666667]
 [0.375      0.625     ]
 [0.34437086 0.65562914]
 [0.26060606 0.73939394]
 [0.25157233 0.74842767]
 [0.32298137 0.67701863]
 [0.49019608 0.50980392]
 [0.35064935 0.64935065]
 [0.32484076 0.67515924]
 [0.67701863 0.32298137]
 [0.64596273 0.35403727]
 [0.3125     0.6875    ]
 [0.27329193 0.72670807]
 [0.35625    0.64375   ]
 [0.32026144 0.67973856]
 [0.36419753 0.63580247]
 [0.44370861 0.55629139]
 [0.45751634 0.54248366]
 [0.43421053 0.56578947]
 [0.50666667 0.49333333]
 [0.30434783 0.69565217]
 [0.33974359 0.66025641]
 [0.52941176 0.47058824]
 [0.33557047 0.66442953]]
	- oob_score_ = 0.8191489361702128

#### Importance of features
- high_power = 0.06207482993197278
- gp_max_val_min = 0.061023242630385485
- gp_max_val_mean = 0.056729024943310655
- gp_auc_mean = 0.05395880574452004
- gp_auc_min = 0.05260109599395314
- gp_auc_max = 0.051388888888888894
- hlbr = 0.04362055933484506
- diff_std = 0.0388095238095238
- srmr = 0.03558012093726379
- ratio_max_to_10ms_ave_peaks = 0.03244992441421013
- ac_auc = 0.03068783068783069
- gp_max_val_max = 0.030248488284202568
- gp_max_val_range = 0.029938586545729402
- coe3[3] = 0.028396636432350724
- tdoa_range = 0.027744708994708985
- gp_max_ix_min = 0.02724584278155706
- gp_auc_std = 0.025783730158730162
- gp_max_val_std = 0.025434618291761153
- low_power = 0.023599773242630386
- gp_auc_range = 0.023566704459561598
- coe3[2] = 0.02319302721088435
- coe1[0] = 0.02203325774754346
- tdoa_min = 0.02202569916855631
- tdoa_max = 0.021079931972789116
- tdoa_mean = 0.018849206349206348
- coe1[1] = 0.017660619803476947
- gp_max_ix_range = 0.016701625094482236
- diff_auc = 0.01655328798185941
- ratio_max_to_9th_ave_peaks = 0.015601851851851851
- gp_max_ix_max = 0.015383597883597883
- ac_std = 0.015178571428571434
- gp_max_ix_std = 0.013390022675736963
- gp_max_ix_mean = 0.011578798185941042
- tdoa_std = 0.009887566137566136
- coe3[0] = 0.0
- coe3[1] = 0.0

## Evaluation
cv = 8
### robot-1
#### accuracy
- Mean = 0.8687499999999999
- Standard deviation = 0.054643732485986
- Max = 0.92
- 75% = 0.9125000000000001
- Median = 0.885
- 25% = 0.845
- Min = 0.75

#### f1
- Mean = 0.7034574382258051
- Standard deviation = 0.08407678067301289
- Max = 0.8095238095238095
- 75% = 0.7536764705882353
- Median = 0.7165408373369939
- 25% = 0.6870748299319728
- Min = 0.5098039215686274

#### precision
- Mean = 0.7043596453704908
- Standard deviation = 0.18355215215782725
- Max = 1.0
- 75% = 0.8116883116883117
- Median = 0.6898148148148149
- 25% = 0.5767519466073414
- Min = 0.41935483870967744

#### recall
- Mean = 0.75
- Standard deviation = 0.11180339887498945
- Max = 0.85
- 75% = 0.85
- Median = 0.8
- 25% = 0.65
- Min = 0.55

#### facing_probas
- Mean = [0.58952206 0.30143382 0.24705882 0.17897059 0.16540441]
- Standard deviation = [0.04419624 0.02470651 0.02120301 0.01553891 0.02408532]
- Max = [0.65588235 0.35764706 0.29294118 0.20647059 0.20411765]
- 75% = [0.61       0.30830882 0.25970588 0.18985294 0.17808824]
- Median = [0.60323529 0.28926471 0.23485294 0.17485294 0.16808824]
- 25% = [0.57411765 0.28735294 0.23382353 0.17073529 0.15455882]
- Min = [0.51323529 0.27676471 0.22617647 0.15264706 0.12294118]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 71.875 | 8.125 |
| Actual Positive | 5.0 | 15.0 |

### robot-2
#### accuracy
- Mean = 0.835
- Standard deviation = 0.027386127875258293
- Max = 0.87
- 75% = 0.8625
- Median = 0.83
- 25% = 0.815
- Min = 0.8

#### f1
- Mean = 0.5329502955028165
- Standard deviation = 0.16487228767881137
- Max = 0.7346938775510204
- 75% = 0.6479591836734694
- Median = 0.5583333333333333
- 25% = 0.4422268907563025
- Min = 0.23076923076923075

#### precision
- Mean = 0.6035896215853112
- Standard deviation = 0.08823053025739755
- Max = 0.8
- 75% = 0.6217672413793104
- Median = 0.6057993730407524
- 25% = 0.5535714285714286
- Min = 0.5

#### recall
- Mean = 0.5437500000000001
- Standard deviation = 0.26743866119168336
- Max = 0.9
- 75% = 0.75
- Median = 0.525
- 25% = 0.36250000000000004
- Min = 0.15

#### facing_probas
- Mean = [0.62908088 0.64558824 0.51893382 0.323125   0.21003676]
- Standard deviation = [0.07669247 0.03656771 0.06310656 0.02913953 0.02843048]
- Max = [0.74470588 0.71147059 0.60882353 0.37323529 0.26558824]
- 75% = [0.69382353 0.67036765 0.57102941 0.33588235 0.22544118]
- Median = [0.62779412 0.64132353 0.51647059 0.31970588 0.20132353]
- 25% = [0.58375    0.61198529 0.48433824 0.31477941 0.19044118]
- Min = [0.50676471 0.60588235 0.42       0.26441176 0.17794118]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 72.625 | 7.375 |
| Actual Positive | 9.125 | 10.875 |

### robot-3
#### accuracy
- Mean = 0.8125
- Standard deviation = 0.025860201081971478
- Max = 0.85
- 75% = 0.8325
- Median = 0.815
- 25% = 0.79
- Min = 0.77

#### f1
- Mean = 0.35959039033421203
- Standard deviation = 0.16685400686022228
- Max = 0.5945945945945946
- 75% = 0.516025641025641
- Median = 0.3165024630541872
- 25% = 0.2535483870967742
- Min = 0.08695652173913045

#### precision
- Mean = 0.532385875003909
- Standard deviation = 0.12365791624036325
- Max = 0.6666666666666666
- 75% = 0.6305147058823529
- Median = 0.5894736842105264
- 25% = 0.4242424242424242
- Min = 0.3333333333333333

#### recall
- Mean = 0.29375
- Standard deviation = 0.1739926363384382
- Max = 0.55
- 75% = 0.4375
- Median = 0.225
- 25% = 0.1875
- Min = 0.05

#### facing_probas
- Mean = [0.40238971 0.56044118 0.56033088 0.49022059 0.25419118]
- Standard deviation = [0.03886568 0.03934943 0.04125188 0.0461654  0.0307795 ]
- Max = [0.45264706 0.60558824 0.63205882 0.54588235 0.3       ]
- 75% = [0.44073529 0.58602941 0.57669118 0.53338235 0.28352941]
- Median = [0.39985294 0.57602941 0.55191176 0.48794118 0.24573529]
- 25% = [0.37316176 0.54529412 0.53154412 0.46227941 0.23602941]
- Min = [0.34941176 0.47764706 0.50852941 0.40205882 0.20970588]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 75.375 | 4.625 |
| Actual Positive | 14.125 | 5.875 |

### robot-4
#### accuracy
- Mean = 0.8275
- Standard deviation = 0.03072051431861125
- Max = 0.89
- 75% = 0.8374999999999999
- Median = 0.8200000000000001
- 25% = 0.8
- Min = 0.8

#### f1
- Mean = 0.5534479217117214
- Standard deviation = 0.11403333954197324
- Max = 0.717948717948718
- 75% = 0.6291666666666667
- Median = 0.5599593495934959
- 25% = 0.5112781954887218
- Min = 0.32000000000000006

#### precision
- Mean = 0.5963314536340851
- Standard deviation = 0.11097470690177208
- Max = 0.8
- 75% = 0.6717105263157894
- Median = 0.5419047619047619
- 25% = 0.5
- Min = 0.5

#### recall
- Mean = 0.5625
- Standard deviation = 0.16153559979150106
- Max = 0.7
- 75% = 0.7
- Median = 0.6000000000000001
- 25% = 0.525
- Min = 0.2

#### facing_probas
- Mean = [0.24069853 0.41238971 0.55367647 0.60930147 0.46933824]
- Standard deviation = [0.01783111 0.03652908 0.05590015 0.05974154 0.03527014]
- Max = [0.265      0.47117647 0.64       0.69941176 0.52882353]
- 75% = [0.25411765 0.43161765 0.57772059 0.64095588 0.48522059]
- Median = [0.24352941 0.39720588 0.55088235 0.61558824 0.45808824]
- 25% = [0.22933824 0.39301471 0.51610294 0.58625    0.44948529]
- Min = [0.21029412 0.36323529 0.48176471 0.48441176 0.42323529]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 71.5 | 8.5 |
| Actual Positive | 8.75 | 11.25 |

### robot-5
#### accuracy
- Mean = 0.9199999999999999
- Standard deviation = 0.028284271247461877
- Max = 0.96
- 75% = 0.95
- Median = 0.915
- 25% = 0.8975
- Min = 0.88

#### f1
- Mean = 0.7569143264616766
- Standard deviation = 0.110134284266934
- Max = 0.9
- 75% = 0.8637873754152824
- Median = 0.7459893048128343
- 25% = 0.6907020872865275
- Min = 0.5714285714285715

#### precision
- Mean = 0.9179961343004821
- Standard deviation = 0.05716259859976032
- Max = 1.0
- 75% = 0.9464285714285714
- Median = 0.916083916083916
- 25% = 0.8892857142857142
- Min = 0.8260869565217391

#### recall
- Mean = 0.6687500000000001
- Standard deviation = 0.17666617531378212
- Max = 0.95
- 75% = 0.7875
- Median = 0.625
- 25% = 0.575
- Min = 0.4

#### facing_probas
- Mean = [0.18705882 0.26191176 0.50621324 0.66014706 0.69227941]
- Standard deviation = [0.01366935 0.02416289 0.05749689 0.05774807 0.04015211]
- Max = [0.20176471 0.29058824 0.57705882 0.73558824 0.74529412]
- 75% = [0.19639706 0.28397059 0.54948529 0.69389706 0.73669118]
- Median = [0.19323529 0.26632353 0.52764706 0.66691176 0.68544118]
- 25% = [0.17764706 0.24169118 0.46558824 0.64757353 0.65257353]
- Min = [0.15852941 0.22470588 0.41       0.52647059 0.64323529]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 78.625 | 1.375 |
| Actual Positive | 6.625 | 13.375 |

### robot-6
#### accuracy
- Mean = 0.56375
- Standard deviation = 0.06203577596838779
- Max = 0.62
- 75% = 0.5974999999999999
- Median = 0.57
- 25% = 0.5675
- Min = 0.41

#### f1
- Mean = 0.7188569391239983
- Standard deviation = 0.05464628912270814
- Max = 0.7654320987654321
- 75% = 0.7479617982762637
- Median = 0.7261146496815287
- 25% = 0.724073166748326
- Min = 0.5815602836879432

#### precision
- Mean = 1.0
- Standard deviation = 0.0
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 1.0
- Min = 1.0

#### recall
- Mean = 0.56375
- Standard deviation = 0.06203577596838779
- Max = 0.62
- 75% = 0.5974999999999999
- Median = 0.57
- 25% = 0.5675
- Min = 0.41

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
| Actual Positive | 43.625 | 56.375 |

