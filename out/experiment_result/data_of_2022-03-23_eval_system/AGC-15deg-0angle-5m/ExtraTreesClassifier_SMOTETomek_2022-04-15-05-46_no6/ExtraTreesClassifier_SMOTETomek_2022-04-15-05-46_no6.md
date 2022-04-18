# ExtraTreesClassifier_SMOTETomek_2022-04-15-05-46_no6
## Constants
- CSV_PATH = ../out/csv/experiment
- OUTPUT_PATH = ../out/experiment_result/data_of_2022-03-23_eval_system/AGC-15deg-0angle-5m
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
- AGC_STATUS = ['AGC-15deg']
- ANGLES = [60, 75, 90, 105, 120]

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
	- n_estimators = 30
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
	- oob_decision_function_ = [[0.46378467 0.53621533]
 [0.31281044 0.68718956]
 [0.30620491 0.69379509]
 [0.39026575 0.60973425]
 [0.20624299 0.79375701]
 [0.25227842 0.74772158]
 [0.43918178 0.56081822]
 [0.34477861 0.65522139]
 [0.33439654 0.66560346]
 [0.56227188 0.43772812]
 [0.43439239 0.56560761]
 [0.59000722 0.40999278]
 [0.44590291 0.55409709]
 [0.40643572 0.59356428]
 [0.39962662 0.60037338]
 [0.42084823 0.57915177]
 [0.39524022 0.60475978]
 [0.57848616 0.42151384]
 [0.50895616 0.49104384]
 [0.66137566 0.33862434]
 [0.49428962 0.50571038]
 [0.64015667 0.35984333]
 [0.42930142 0.57069858]
 [0.50251722 0.49748278]
 [0.44873922 0.55126078]
 [0.49837619 0.50162381]
 [0.54495952 0.45504048]
 [0.46806672 0.53193328]
 [0.34363137 0.65636863]
 [0.49001022 0.50998978]
 [0.56812443 0.43187557]
 [0.46633563 0.53366437]
 [0.68946609 0.31053391]
 [0.46497615 0.53502385]
 [0.55840391 0.44159609]
 [0.45509861 0.54490139]
 [0.5408392  0.4591608 ]
 [0.53710223 0.46289777]
 [0.55393759 0.44606241]
 [0.52799784 0.47200216]
 [0.44519962 0.55480038]
 [0.62716728 0.37283272]
 [0.66558229 0.33441771]
 [0.68062771 0.31937229]
 [0.47605601 0.52394399]
 [0.46723532 0.53276468]
 [0.66274238 0.33725762]
 [0.45779115 0.54220885]
 [0.513404   0.486596  ]
 [0.58058712 0.41941288]
 [0.54240211 0.45759789]
 [0.43614618 0.56385382]
 [0.38930269 0.61069731]
 [0.24512626 0.75487374]
 [0.32376744 0.67623256]
 [0.50904481 0.49095519]
 [0.46981808 0.53018192]
 [0.54261492 0.45738508]
 [0.32382531 0.67617469]
 [0.38528987 0.61471013]
 [0.55264121 0.44735879]
 [0.41064075 0.58935925]
 [0.46719655 0.53280345]
 [0.62771417 0.37228583]
 [0.42541486 0.57458514]
 [0.42140512 0.57859488]
 [0.44035847 0.55964153]
 [0.42166021 0.57833979]
 [0.50630211 0.49369789]
 [0.54467246 0.45532754]
 [0.50705628 0.49294372]
 [0.47170703 0.52829297]
 [0.44368286 0.55631714]
 [0.46389101 0.53610899]
 [0.54372931 0.45627069]
 [0.46083874 0.53916126]
 [0.31005366 0.68994634]
 [0.2871645  0.7128355 ]
 [0.42140348 0.57859652]
 [0.28643779 0.71356221]
 [0.38889791 0.61110209]
 [0.45672399 0.54327601]
 [0.4218254  0.5781746 ]
 [0.45963522 0.54036478]]
	- oob_score_ = 0.5952380952380952

#### Importance of features
- gp_max_ix_min = 0.09708511795659241
- gp_max_ix_range = 0.0913890197097596
- high_power = 0.07819627980073438
- gp_max_val_std = 0.06336744947996914
- diff_auc = 0.053673713920214076
- diff_std = 0.052770236241420486
- gp_max_ix_max = 0.05255387720798752
- gp_auc_max = 0.039813430792282674
- gp_max_val_min = 0.03931259833760469
- gp_max_val_max = 0.03530553934937043
- coe3[2] = 0.034540779643889984
- ac_std = 0.028795884767725544
- gp_max_val_mean = 0.02836859709327138
- tdoa_std = 0.025225319914864548
- gp_max_val_range = 0.025143467601893493
- coe1[1] = 0.024142738556196638
- gp_max_ix_mean = 0.021727620931241753
- tdoa_max = 0.02138199934515801
- tdoa_range = 0.019186784845288123
- low_power = 0.018416554206027922
- gp_auc_mean = 0.017015629283917373
- gp_auc_range = 0.016463254319942392
- ratio_max_to_9th_ave_peaks = 0.01618037690050123
- hlbr = 0.013883859894897738
- srmr = 0.013781781710868012
- ratio_max_to_10ms_ave_peaks = 0.013371998091875297
- coe1[0] = 0.012467890636839516
- gp_auc_std = 0.01136227654473647
- ac_auc = 0.009163571384666712
- coe3[3] = 0.008815028655547737
- tdoa_min = 0.008300486001226666
- gp_auc_min = 0.00365929221076116
- gp_max_ix_std = 0.002781492252581483
- tdoa_mean = 0.0023560524101454354
- coe3[0] = 0.0
- coe3[1] = 0.0

## Evaluation
cv = 8
### robot-1
#### accuracy
- Mean = 0.7425
- Standard deviation = 0.1805373922488081
- Max = 0.85
- 75% = 0.8425
- Median = 0.82
- 25% = 0.7725000000000001
- Min = 0.29

#### f1
- Mean = 0.30064151408821815
- Standard deviation = 0.11916400758868502
- Max = 0.4444444444444444
- 75% = 0.39957264957264954
- Median = 0.3090062111801242
- 25% = 0.22287390029325516
- Min = 0.09523809523809523

#### precision
- Mean = 0.694259151236891
- Standard deviation = 0.31113731562410385
- Max = 1.0
- 75% = 0.8928571428571428
- Median = 0.8452380952380952
- 25% = 0.5264423076923077
- Min = 0.1506849315068493

#### recall
- Mean = 0.26249999999999996
- Standard deviation = 0.14086784586980808
- Max = 0.55
- 75% = 0.3
- Median = 0.275
- 25% = 0.2125
- Min = 0.05

#### facing_probas
- Mean = [0.46060201 0.42398316 0.37020876 0.35413148 0.33930822]
- Standard deviation = [0.0527554  0.06995674 0.02968507 0.03216049 0.03719327]
- Max = [0.55131307 0.5118645  0.40446223 0.40716375 0.41189976]
- 75% = [0.49225468 0.48881564 0.39100406 0.3657852  0.35943974]
- Median = [0.46416879 0.41695671 0.37783899 0.35483478 0.33156307]
- 25% = [0.43001142 0.38300164 0.35932671 0.33724869 0.3148108 ]
- Min = [0.3619204  0.30230143 0.30925325 0.29755538 0.28846004]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 69.0 | 11.0 |
| Actual Positive | 14.75 | 5.25 |

### robot-2
#### accuracy
- Mean = 0.7975
- Standard deviation = 0.07310095758606724
- Max = 0.92
- 75% = 0.8474999999999999
- Median = 0.7949999999999999
- 25% = 0.74
- Min = 0.7

#### f1
- Mean = 0.42102146632608817
- Standard deviation = 0.22151321850795505
- Max = 0.8095238095238095
- 75% = 0.559220985691574
- Median = 0.40408163265306124
- 25% = 0.2481060606060606
- Min = 0.08000000000000002

#### precision
- Mean = 0.5071649994697662
- Standard deviation = 0.21740045951216658
- Max = 0.7727272727272727
- 75% = 0.7169117647058824
- Median = 0.49384236453201974
- 25% = 0.3269230769230769
- Min = 0.2

#### recall
- Mean = 0.4125
- Standard deviation = 0.24717149916606485
- Max = 0.85
- 75% = 0.525
- Median = 0.475
- 25% = 0.1875
- Min = 0.05

#### facing_probas
- Mean = [0.52860969 0.6011865  0.56546539 0.52922508 0.43522226]
- Standard deviation = [0.06345975 0.05514347 0.09380122 0.02436251 0.04757537]
- Max = [0.67443714 0.69121533 0.69750757 0.55564218 0.52597582]
- 75% = [0.54500476 0.64678215 0.64388071 0.54953261 0.45623366]
- Median = [0.50820136 0.59821464 0.5763822  0.53800338 0.4321495 ]
- 25% = [0.48757641 0.55190711 0.47905545 0.50932274 0.40699821]
- Min = [0.46051291 0.52669325 0.42801948 0.48333195 0.35790373]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 71.5 | 8.5 |
| Actual Positive | 11.75 | 8.25 |

### robot-3
#### accuracy
- Mean = 0.74125
- Standard deviation = 0.06273705045664806
- Max = 0.8
- 75% = 0.8
- Median = 0.765
- 25% = 0.69
- Min = 0.62

#### f1
- Mean = 0.2606284258543943
- Standard deviation = 0.21793804011858386
- Max = 0.523076923076923
- 75% = 0.4542682926829268
- Median = 0.3114630467571644
- 25% = 0.0
- Min = 0.0

#### precision
- Mean = 0.24602694572452638
- Standard deviation = 0.19727155241607963
- Max = 0.5
- 75% = 0.3904761904761905
- Median = 0.33093317972350234
- 25% = 0.0
- Min = 0.0

#### recall
- Mean = 0.36250000000000004
- Standard deviation = 0.362068708949006
- Max = 0.95
- 75% = 0.5875
- Median = 0.3
- 25% = 0.0
- Min = 0.0

#### facing_probas
- Mean = [0.48028909 0.52597414 0.53411887 0.50678783 0.43072116]
- Standard deviation = [0.06557681 0.03148263 0.08349716 0.0252194  0.04928007]
- Max = [0.63263907 0.58511961 0.66011368 0.53751338 0.53207951]
- 75% = [0.49567705 0.54160775 0.58981387 0.52725457 0.450258  ]
- Median = [0.46596193 0.5253796  0.52544046 0.50891989 0.41498729]
- 25% = [0.4355337  0.50123983 0.4656314  0.48964471 0.40216001]
- Min = [0.40947767 0.47842577 0.42477393 0.46369658 0.36167904]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 66.875 | 13.125 |
| Actual Positive | 12.75 | 7.25 |

### robot-4
#### accuracy
- Mean = 0.7424999999999999
- Standard deviation = 0.04023369234857774
- Max = 0.81
- 75% = 0.775
- Median = 0.73
- 25% = 0.71
- Min = 0.69

#### f1
- Mean = 0.34079368972793067
- Standard deviation = 0.1279072323733982
- Max = 0.5777777777777778
- 75% = 0.43970893970893965
- Median = 0.3018970189701897
- 25% = 0.24403183023872682
- Min = 0.18749999999999997

#### precision
- Mean = 0.34722421863482233
- Standard deviation = 0.09411221020634823
- Max = 0.52
- 75% = 0.39889705882352944
- Median = 0.30952380952380953
- 25% = 0.27578947368421053
- Min = 0.25

#### recall
- Mean = 0.35624999999999996
- Standard deviation = 0.17577951388031543
- Max = 0.65
- 75% = 0.45
- Median = 0.32499999999999996
- 25% = 0.225
- Min = 0.15

#### facing_probas
- Mean = [0.47136932 0.5229959  0.53890746 0.56560269 0.48584926]
- Standard deviation = [0.06850879 0.02679654 0.06767114 0.04876143 0.03980995]
- Max = [0.61709331 0.57459148 0.64155599 0.62281173 0.56453442]
- 75% = [0.497217   0.5371428  0.58393808 0.60923396 0.50078665]
- Median = [0.46219217 0.52209386 0.5315794  0.57377725 0.49179488]
- 25% = [0.42613025 0.50219316 0.49805999 0.52430286 0.45094037]
- Min = [0.3870881  0.4885543  0.44190106 0.49644748 0.42927927]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 67.125 | 12.875 |
| Actual Positive | 12.875 | 7.125 |

### robot-5
#### accuracy
- Mean = 0.7775000000000001
- Standard deviation = 0.06015604707757984
- Max = 0.81
- 75% = 0.8025
- Median = 0.8
- 25% = 0.795
- Min = 0.62

#### f1
- Mean = 0.09077380952380952
- Standard deviation = 0.11261450144352703
- Max = 0.32142857142857145
- 75% = 0.12499999999999999
- Median = 0.047619047619047616
- 25% = 0.0
- Min = 0.0

#### precision
- Mean = 0.328125
- Standard deviation = 0.4095419506900361
- Max = 1.0
- 75% = 0.53125
- Median = 0.125
- 25% = 0.0
- Min = 0.0

#### recall
- Mean = 0.08750000000000001
- Standard deviation = 0.14523687548277814
- Max = 0.45
- 75% = 0.075
- Median = 0.025
- 25% = 0.0
- Min = 0.0

#### facing_probas
- Mean = [0.40068486 0.43649128 0.4613747  0.5355008  0.4588666 ]
- Standard deviation = [0.07519443 0.050496   0.05091682 0.02984493 0.04731866]
- Max = [0.51794004 0.51918978 0.56460694 0.58637981 0.53944817]
- 75% = [0.46231493 0.45514863 0.47609472 0.55413749 0.49116699]
- Median = [0.37296523 0.42474496 0.4556637  0.53791575 0.45586365]
- 25% = [0.35234336 0.41240512 0.43175069 0.51662601 0.41771984]
- Min = [0.29982748 0.35309149 0.38859327 0.48285237 0.39758259]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 76.0 | 4.0 |
| Actual Positive | 18.25 | 1.75 |

### robot-6
#### accuracy
- Mean = 0.29625
- Standard deviation = 0.07920503456220444
- Max = 0.4
- 75% = 0.3625
- Median = 0.30500000000000005
- 25% = 0.2475
- Min = 0.16

#### f1
- Mean = 0.4511642222721547
- Standard deviation = 0.09707345481548607
- Max = 0.5714285714285715
- 75% = 0.5320953198797768
- Median = 0.4663297684804325
- 25% = 0.3963006690279418
- Min = 0.2758620689655173

#### precision
- Mean = 1.0
- Standard deviation = 0.0
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 1.0
- Min = 1.0

#### recall
- Mean = 0.29625
- Standard deviation = 0.07920503456220444
- Max = 0.4
- 75% = 0.3625
- Median = 0.30500000000000005
- 25% = 0.2475
- Min = 0.16

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
| Actual Positive | 70.375 | 29.625 |

