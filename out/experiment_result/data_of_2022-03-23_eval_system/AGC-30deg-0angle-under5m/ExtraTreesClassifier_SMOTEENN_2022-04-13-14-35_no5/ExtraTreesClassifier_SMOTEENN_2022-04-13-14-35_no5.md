# ExtraTreesClassifier_SMOTEENN_2022-04-13-14-35_no5
## Constants
- CSV_PATH = ../out/csv/experiment
- OUTPUT_PATH = ../out/experiment_result/data_of_2022-03-23_eval_system/AGC-30deg-0angle-under5m
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
- AGC_STATUS = ['AGC-30deg']
- ANGLES = [30, 60, 90, 120, 150]

## Loaded CSV
- 2022-03-23_raspi_48000Hz_w1_N2^12_overlap80_all.csv

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
	- n_estimators = 10
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
	- min_samples_split = 10
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
	- oob_decision_function_ = [[0.32859848 0.67140152]
 [0.48541667 0.51458333]
 [0.66919192 0.33080808]
 [0.37020202 0.62979798]
 [0.11018519 0.88981481]
 [0.56590909 0.43409091]
 [0.87272727 0.12727273]
 [0.65530303 0.34469697]
 [0.25077304 0.74922696]
 [0.80227273 0.19772727]
 [0.19124579 0.80875421]
 [0.1497114  0.8502886 ]
 [0.20138889 0.79861111]
 [0.65222222 0.34777778]
 [0.84090909 0.15909091]
 [0.77272727 0.22727273]
 [0.82007576 0.17992424]
 [0.185      0.815     ]
 [0.50208333 0.49791667]
 [0.39686147 0.60313853]
 [0.67588126 0.32411874]
 [0.03240741 0.96759259]
 [0.21626984 0.78373016]
 [0.0952381  0.9047619 ]
 [0.21666667 0.78333333]
 [0.25992665 0.74007335]
 [0.18441558 0.81558442]
 [0.37638889 0.62361111]
 [0.35034014 0.64965986]
 [0.48674242 0.51325758]
 [0.27857143 0.72142857]
 [0.17380952 0.82619048]
 [0.21527778 0.78472222]
 [0.18362193 0.81637807]
 [0.32973184 0.67026816]
 [0.16262626 0.83737374]
 [0.23690476 0.76309524]
 [0.24393939 0.75606061]
 [0.39065055 0.60934945]
 [0.04444444 0.95555556]
 [0.10222222 0.89777778]
 [0.23410637 0.76589363]
 [0.45222222 0.54777778]
 [0.02222222 0.97777778]
 [0.43625541 0.56374459]
 [0.28825397 0.71174603]
 [0.31785714 0.68214286]
 [0.26041667 0.73958333]
 [0.19206349 0.80793651]
 [0.425      0.575     ]
 [0.37638889 0.62361111]
 [0.17037037 0.82962963]
 [0.16166126 0.83833874]
 [0.16944444 0.83055556]
 [0.19305556 0.80694444]
 [0.33396465 0.66603535]]
	- oob_score_ = 0.8214285714285714

#### Importance of features
- coe1[0] = 0.1653806057547212
- gp_max_val_std = 0.13829399585921323
- coe3[3] = 0.11804662562699497
- gp_max_ix_max = 0.08129196933071822
- gp_auc_min = 0.06765513833992096
- gp_max_val_min = 0.06757019475714979
- diff_auc = 0.05771719522079009
- gp_auc_mean = 0.045488018164523934
- tdoa_max = 0.03216593538093337
- gp_max_ix_range = 0.031130462470709448
- ac_std = 0.024085379407097585
- srmr = 0.02319410519732824
- hlbr = 0.022790697674418596
- coe3[2] = 0.022063329928498472
- gp_auc_std = 0.01815580064218904
- gp_max_ix_std = 0.017974326126173217
- high_power = 0.0176392572944297
- gp_max_val_mean = 0.015412676698586428
- gp_auc_range = 0.01375238095238095
- coe1[1] = 0.012549019607843123
- tdoa_range = 0.007642885565379431
- low_power = 0.0
- coe3[0] = 0.0
- coe3[1] = 0.0
- ratio_max_to_10ms_ave_peaks = 0.0
- ratio_max_to_9th_ave_peaks = 0.0
- ac_auc = 0.0
- diff_std = 0.0
- gp_max_val_range = 0.0
- gp_max_val_max = 0.0
- gp_max_ix_min = 0.0
- gp_max_ix_mean = 0.0
- gp_auc_max = 0.0
- tdoa_std = 0.0
- tdoa_min = 0.0
- tdoa_mean = 0.0

## Evaluation
cv = 8
### robot-1
#### accuracy
- Mean = 0.8320833333333333
- Standard deviation = 0.05405597664561349
- Max = 0.88
- 75% = 0.875
- Median = 0.8516666666666666
- 25% = 0.8133333333333334
- Min = 0.72

#### f1
- Mean = 0.6003866063776147
- Standard deviation = 0.09829574986495744
- Max = 0.75
- 75% = 0.6648270528683915
- Median = 0.6235332464146024
- 25% = 0.5267857142857143
- Min = 0.43243243243243246

#### precision
- Mean = 0.5950362574216421
- Standard deviation = 0.1251849920181026
- Max = 0.7727272727272727
- 75% = 0.6600274725274726
- Median = 0.6226196603190941
- 25% = 0.5445344129554656
- Min = 0.36363636363636365

#### recall
- Mean = 0.6229166666666667
- Standard deviation = 0.12074350109035085
- Max = 0.9
- 75% = 0.6416666666666667
- Median = 0.575
- 25% = 0.5583333333333333
- Min = 0.5

#### facing_probas
- Mean = [0.61741343 0.39391215 0.36070052 0.20487044 0.14790512]
- Standard deviation = [0.07035139 0.09747116 0.08308799 0.05750558 0.06697537]
- Max = [0.75516528 0.57974699 0.52389791 0.31258574 0.29199417]
- 75% = [0.63663781 0.43950364 0.38074076 0.23422348 0.15382701]
- Median = [0.5906344  0.38304425 0.34468889 0.19697039 0.12514856]
- 25% = [0.57282313 0.33031491 0.31406012 0.16811109 0.09745632]
- Min = [0.54091234 0.24951257 0.24126233 0.11324339 0.09293182]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 212.25 | 27.75 |
| Actual Positive | 22.625 | 37.375 |

### robot-2
#### accuracy
- Mean = 0.7845833333333333
- Standard deviation = 0.02449135334947601
- Max = 0.8133333333333334
- 75% = 0.8041666666666667
- Median = 0.7883333333333333
- 25% = 0.7758333333333334
- Min = 0.7333333333333333

#### f1
- Mean = 0.2782340225241426
- Standard deviation = 0.1016469661670317
- Max = 0.43999999999999995
- 75% = 0.34873150105708245
- Median = 0.24747474747474746
- 25% = 0.210561797752809
- Min = 0.13157894736842105

#### precision
- Mean = 0.4291513909940634
- Standard deviation = 0.10171133977276267
- Max = 0.55
- 75% = 0.5346153846153846
- Median = 0.4442857142857143
- 25% = 0.3119612068965517
- Min = 0.3

#### recall
- Mean = 0.21875
- Standard deviation = 0.10322490951531246
- Max = 0.38333333333333336
- 75% = 0.2791666666666667
- Median = 0.19166666666666665
- 25% = 0.14583333333333331
- Min = 0.08333333333333333

#### facing_probas
- Mean = [0.59819048 0.60057462 0.6156139  0.43692356 0.26106907]
- Standard deviation = [0.06727605 0.06769432 0.06728723 0.08516567 0.0617194 ]
- Max = [0.73150914 0.73941522 0.76709223 0.62404449 0.36388769]
- 75% = [0.61010899 0.64029678 0.63177845 0.45776811 0.29568795]
- Median = [0.58562925 0.58642539 0.58592113 0.41322694 0.26672022]
- 25% = [0.5717541  0.55446447 0.57300267 0.37941076 0.20585107]
- Min = [0.49717743 0.50680964 0.55054533 0.34172565 0.17023016]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 222.25 | 17.75 |
| Actual Positive | 46.875 | 13.125 |

### robot-3
#### accuracy
- Mean = 0.71375
- Standard deviation = 0.05183942890203257
- Max = 0.8033333333333333
- 75% = 0.7441666666666666
- Median = 0.7133333333333334
- 25% = 0.6908333333333334
- Min = 0.6133333333333333

#### f1
- Mean = 0.32049265343756556
- Standard deviation = 0.1080202067923916
- Max = 0.45871559633027525
- 75% = 0.40672137368371125
- Median = 0.32611424984306336
- 25% = 0.26103988603988604
- Min = 0.13725490196078433

#### precision
- Mean = 0.31007002949577256
- Standard deviation = 0.10290293046660114
- Max = 0.5102040816326531
- 75% = 0.3648353062274833
- Median = 0.3078616352201258
- 25% = 0.22682709447415328
- Min = 0.16666666666666666

#### recall
- Mean = 0.35
- Standard deviation = 0.14553540997144152
- Max = 0.6166666666666667
- 75% = 0.4166666666666667
- Median = 0.3666666666666667
- 25% = 0.29166666666666663
- Min = 0.11666666666666667

#### facing_probas
- Mean = [0.46531911 0.55879733 0.63656393 0.55226662 0.39853325]
- Standard deviation = [0.09460013 0.08607501 0.06509317 0.07985752 0.09032187]
- Max = [0.66235185 0.71698208 0.73197745 0.7072102  0.55075241]
- 75% = [0.48880554 0.59464433 0.68722756 0.58199026 0.43918528]
- Median = [0.44351465 0.56933502 0.62902935 0.53122855 0.39872588]
- 25% = [0.41953151 0.48734761 0.59811179 0.51261583 0.3535839 ]
- Min = [0.33682732 0.44543206 0.52725666 0.43469054 0.23812332]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 193.125 | 46.875 |
| Actual Positive | 39.0 | 21.0 |

### robot-4
#### accuracy
- Mean = 0.7333333333333334
- Standard deviation = 0.02915475947422651
- Max = 0.77
- 75% = 0.7616666666666667
- Median = 0.7316666666666667
- 25% = 0.7133333333333334
- Min = 0.6866666666666666

#### f1
- Mean = 0.30337969235642726
- Standard deviation = 0.08334968936031242
- Max = 0.43749999999999994
- 75% = 0.36241981099537834
- Median = 0.3103365384615384
- 25% = 0.2446311858076564
- Min = 0.16666666666666669

#### precision
- Mean = 0.31966532502965644
- Standard deviation = 0.0578798144716983
- Max = 0.4117647058823529
- 75% = 0.348616158792284
- Median = 0.3075980392156863
- 25% = 0.27582417582417584
- Min = 0.2542372881355932

#### recall
- Mean = 0.30208333333333337
- Standard deviation = 0.10783136912172944
- Max = 0.4666666666666667
- 75% = 0.375
- Median = 0.31666666666666665
- 25% = 0.23333333333333334
- Min = 0.11666666666666667

#### facing_probas
- Mean = [0.37096479 0.45953639 0.57960439 0.62131859 0.5517673 ]
- Standard deviation = [0.09473601 0.0991475  0.07020776 0.06976828 0.06264015]
- Max = [0.58244216 0.62525854 0.68657636 0.76984512 0.66612939]
- 75% = [0.39045674 0.52000394 0.62067357 0.64540505 0.56970988]
- Median = [0.3497311  0.46791847 0.57383538 0.59996883 0.54662581]
- 25% = [0.31428279 0.3822532  0.52420483 0.5671552  0.52072433]
- Min = [0.25716114 0.31524465 0.47809644 0.5475359  0.45914126]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 201.875 | 38.125 |
| Actual Positive | 41.875 | 18.125 |

### robot-5
#### accuracy
- Mean = 0.7966666666666666
- Standard deviation = 0.034840908267278106
- Max = 0.86
- 75% = 0.8216666666666667
- Median = 0.79
- 25% = 0.7658333333333334
- Min = 0.7566666666666667

#### f1
- Mean = 0.2906816416261371
- Standard deviation = 0.1756019150026533
- Max = 0.5714285714285714
- 75% = 0.4398271276595745
- Median = 0.2948563148997827
- 25% = 0.1314873417721519
- Min = 0.05405405405405406

#### precision
- Mean = 0.43123532263879993
- Standard deviation = 0.20727373175888408
- Max = 0.7368421052631579
- 75% = 0.5919117647058824
- Median = 0.4556541019955654
- 25% = 0.2644736842105263
- Min = 0.14285714285714285

#### recall
- Mean = 0.225
- Standard deviation = 0.14743171677461778
- Max = 0.4666666666666667
- 75% = 0.35
- Median = 0.225
- 25% = 0.08750000000000001
- Min = 0.03333333333333333

#### facing_probas
- Mean = [0.19553914 0.33921294 0.50144673 0.64463431 0.60464299]
- Standard deviation = [0.07668434 0.10055707 0.07843111 0.07660423 0.08009354]
- Max = [0.37880038 0.52727321 0.65562025 0.79717677 0.77810125]
- 75% = [0.21059974 0.37633479 0.53122147 0.70478668 0.61550385]
- Median = [0.17252423 0.33411367 0.47622267 0.60351139 0.59663471]
- 25% = [0.14698975 0.28486566 0.45730166 0.58604428 0.58319904]
- Min = [0.12579648 0.20092563 0.40215554 0.569487   0.4639614 ]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 225.5 | 14.5 |
| Actual Positive | 46.5 | 13.5 |

### robot-6
#### accuracy
- Mean = 0.34375
- Standard deviation = 0.03735852944405362
- Max = 0.3933333333333333
- 75% = 0.37333333333333335
- Median = 0.35333333333333333
- 25% = 0.31916666666666665
- Min = 0.28

#### f1
- Mean = 0.5104614236740996
- Standard deviation = 0.041968244683551995
- Max = 0.5645933014354066
- 75% = 0.5436893203883496
- Median = 0.5220867940325311
- 25% = 0.4837426205578018
- Min = 0.43750000000000006

#### precision
- Mean = 1.0
- Standard deviation = 0.0
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 1.0
- Min = 1.0

#### recall
- Mean = 0.34375
- Standard deviation = 0.03735852944405362
- Max = 0.3933333333333333
- 75% = 0.37333333333333335
- Median = 0.35333333333333333
- 25% = 0.31916666666666665
- Min = 0.28

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
| Actual Positive | 196.875 | 103.125 |

