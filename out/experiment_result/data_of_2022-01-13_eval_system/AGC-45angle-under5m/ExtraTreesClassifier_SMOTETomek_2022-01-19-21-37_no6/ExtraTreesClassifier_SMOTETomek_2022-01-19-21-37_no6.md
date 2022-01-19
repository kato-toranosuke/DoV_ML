# ExtraTreesClassifier_SMOTETomek_2022-01-19-21-37_no6
## Constants
- CSV_PATH = ../out/csv/experiment
- OUTPUT_PATH = ../out/experiment_result/data_of_2022-01-13_eval_system/AGC-45angle-under5m
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
- DISTANCE = [1, 3, 5]
- AGC_STATUS = ['AGC']

## Loaded CSV
- 2021-12-27_AGC.csv
- 2022-01-10_NoAGC.csv
- 2022-01-13_raspi_48000Hz_w1_N2^12_overlap80.csv

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
	- n_estimators = 70
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
- gp_auc_max = 0.09613045268370421
- gp_max_val_mean = 0.0897524048684256
- gp_auc_min = 0.0860680405179794
- gp_max_val_min = 0.07682946689782376
- diff_std = 0.05971919051264977
- gp_max_val_max = 0.059186339715298915
- srmr = 0.053511282451627167
- high_power = 0.05264758529488675
- diff_auc = 0.05238310478255236
- hlbr = 0.04797703670927913
- gp_auc_mean = 0.04668222838150735
- gp_max_ix_mean = 0.02476139450200363
- tdoa_mean = 0.022151338599333794
- gp_max_val_range = 0.01594585010393656
- gp_max_val_std = 0.015452442490362366
- gp_max_ix_std = 0.015306174107075837
- tdoa_min = 0.014915186834782561
- gp_auc_std = 0.014909382402420337
- tdoa_std = 0.014618833822576808
- gp_auc_range = 0.012680074582667048
- coe1[0] = 0.012618638388384493
- gp_max_ix_min = 0.012332998059312147
- gp_max_ix_range = 0.01216069490488599
- coe3[2] = 0.011886322721947838
- ratio_max_to_10ms_ave_peaks = 0.011617800079895981
- coe1[1] = 0.011123474263952361
- tdoa_range = 0.01102972457943851
- low_power = 0.009088478572799845
- gp_max_ix_max = 0.006982630233775992
- ac_std = 0.0067005755173741525
- coe3[3] = 0.0064420605209436835
- ratio_max_to_9th_ave_peaks = 0.005671854519475159
- tdoa_max = 0.005430964188680594
- ac_auc = 0.00528597318823996
- coe3[0] = 0.0
- coe3[1] = 0.0

## Evaluation
cv = 8
### robot-1
#### accuracy
- Mean = 0.9678093645484951
- Standard deviation = 0.0057777069235306205
- Max = 0.9732441471571907
- 75% = 0.9732441471571907
- Median = 0.9698996655518395
- 25% = 0.9632107023411371
- Min = 0.9565217391304348

#### f1
- Mean = 0.9211719374280897
- Standard deviation = 0.015878349373048828
- Max = 0.9365079365079364
- 75% = 0.9349466562581317
- Median = 0.9274146341463414
- 25% = 0.9100869565217392
- Min = 0.8907563025210085

#### precision
- Mean = 0.903123241347681
- Standard deviation = 0.019536551430861655
- Max = 0.9454545454545454
- 75% = 0.9084101382488479
- Median = 0.8961222393425783
- 25% = 0.8935314685314686
- Min = 0.8769230769230769

#### recall
- Mean = 0.9416666666666667
- Standard deviation = 0.040824829046386284
- Max = 0.9833333333333333
- 75% = 0.9708333333333333
- Median = 0.95
- 25% = 0.9333333333333333
- Min = 0.8666666666666667

#### facing_probas
- Mean = [0.95732143 0.738125   0.13315476 0.00193452 0.00261905]
- Standard deviation = [0.01927901 0.04557696 0.03035125 0.00131728 0.002208  ]
- Max = [0.97880952 0.7947619  0.1852381  0.0047619  0.00642857]
- 75% = [0.97285714 0.76916667 0.15029762 0.00244048 0.00470238]
- Median = [0.96392857 0.75011905 0.12059524 0.00178571 0.00107143]
- 25% = [0.94208333 0.71625    0.11065476 0.00107143 0.00095238]
- Min = [9.22142857e-01 6.66428571e-01 9.92857143e-02 2.38095238e-04
 7.14285714e-04]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 232.875 | 6.125 |
| Actual Positive | 3.5 | 56.5 |

### robot-2
#### accuracy
- Mean = 0.9607023411371238
- Standard deviation = 0.006636499944141946
- Max = 0.9698996655518395
- 75% = 0.9665551839464883
- Median = 0.9615384615384616
- 25% = 0.955685618729097
- Min = 0.9498327759197325

#### f1
- Mean = 0.8988289149135311
- Standard deviation = 0.015980560779267086
- Max = 0.9230769230769231
- 75% = 0.912280701754386
- Median = 0.8986024844720497
- 25% = 0.8887197332173408
- Min = 0.8760330578512396

#### precision
- Mean = 0.9325389550691534
- Standard deviation = 0.03430610780369355
- Max = 0.9629629629629629
- 75% = 0.961894586894587
- Median = 0.9464114832535885
- 25% = 0.9157559198542805
- Min = 0.8688524590163934

#### recall
- Mean = 0.86875
- Standard deviation = 0.02420614591379635
- Max = 0.9
- 75% = 0.8875
- Median = 0.8666666666666667
- 25% = 0.8583333333333334
- Min = 0.8333333333333334

#### facing_probas
- Mean = [0.92092262 0.93282738 0.80702381 0.10431548 0.0066369 ]
- Standard deviation = [0.00769718 0.01322846 0.02253304 0.02974963 0.00385655]
- Max = [0.93214286 0.96       0.8497619  0.15761905 0.01261905]
- 75% = [0.92767857 0.93922619 0.81583333 0.12386905 0.01035714]
- Median = [0.92047619 0.93190476 0.8072619  0.09833333 0.00535714]
- 25% = [0.91428571 0.92279762 0.79696429 0.07565476 0.00327381]
- Min = [0.91071429 0.915      0.765      0.07357143 0.00238095]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 235.125 | 3.875 |
| Actual Positive | 7.875 | 52.125 |

### robot-3
#### accuracy
- Mean = 0.9485785953177258
- Standard deviation = 0.010567913595120843
- Max = 0.959866220735786
- 75% = 0.9565217391304348
- Median = 0.9531772575250836
- 25% = 0.9431438127090301
- Min = 0.9297658862876255

#### f1
- Mean = 0.8519724906649612
- Standard deviation = 0.03557152653823876
- Max = 0.888888888888889
- 75% = 0.8785046728971964
- Median = 0.8679245283018869
- 25% = 0.8346153846153845
- Min = 0.787878787878788

#### precision
- Mean = 1.0
- Standard deviation = 0.0
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 1.0
- Min = 1.0

#### recall
- Mean = 0.74375
- Standard deviation = 0.05266343608235226
- Max = 0.8
- 75% = 0.7833333333333333
- Median = 0.7666666666666667
- 25% = 0.7166666666666666
- Min = 0.65

#### facing_probas
- Mean = [0.33907738 0.94169643 0.97244048 0.89258929 0.13282738]
- Standard deviation = [0.0337345  0.02408514 0.00846976 0.02371572 0.02763763]
- Max = [0.40261905 0.97547619 0.98571429 0.93119048 0.17761905]
- 75% = [0.34880952 0.95910714 0.97910714 0.90517857 0.14797619]
- Median = [0.3447619  0.94845238 0.9725     0.88904762 0.13690476]
- 25% = [0.32714286 0.91839286 0.9664881  0.87803571 0.11261905]
- Min = [0.28380952 0.90833333 0.95833333 0.85428571 0.09071429]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 239.0 | 0.0 |
| Actual Positive | 15.375 | 44.625 |

### robot-4
#### accuracy
- Mean = 0.9443979933110368
- Standard deviation = 0.007832355349161865
- Max = 0.9565217391304348
- 75% = 0.9481605351170569
- Median = 0.9448160535117057
- 25% = 0.939799331103679
- Min = 0.9297658862876255

#### f1
- Mean = 0.8559443474183124
- Standard deviation = 0.02070531470475423
- Max = 0.8907563025210085
- 75% = 0.8681326709526593
- Median = 0.8535714285714286
- 25% = 0.8443310844166529
- Min = 0.8235294117647058

#### precision
- Mean = 0.8781999909108292
- Standard deviation = 0.04685923504810552
- Max = 0.9772727272727273
- 75% = 0.89746772591857
- Median = 0.8738700564971751
- 25% = 0.8446096137816059
- Min = 0.8166666666666667

#### recall
- Mean = 0.8389830508474576
- Standard deviation = 0.04793944279230833
- Max = 0.8983050847457628
- 75% = 0.864406779661017
- Median = 0.8559322033898304
- 25% = 0.826271186440678
- Min = 0.7288135593220338

#### facing_probas
- Mean = [0.01374092 0.15205811 0.91352906 0.96346852 0.75741525]
- Standard deviation = [0.00579061 0.02623797 0.02265425 0.01100992 0.05500945]
- Max = [0.02808717 0.19128329 0.93656174 0.98184019 0.83825666]
- 75% = [0.01374092 0.16670702 0.93038741 0.97384988 0.80556901]
- Median = [0.01113801 0.15520581 0.92300242 0.95956416 0.76065375]
- 25% = [0.01029056 0.14582324 0.90199758 0.9561138  0.71198547]
- Min = [0.00992736 0.09515738 0.87021792 0.94891041 0.66634383]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 232.875 | 7.125 |
| Actual Positive | 9.5 | 49.5 |

### robot-5
#### accuracy
- Mean = 0.9753344481605352
- Standard deviation = 0.009450380063091395
- Max = 0.9933110367892977
- 75% = 0.9807692307692308
- Median = 0.9749163879598662
- 25% = 0.9665551839464883
- Min = 0.9632107023411371

#### f1
- Mean = 0.9340566621462236
- Standard deviation = 0.02626717212861039
- Max = 0.983050847457627
- 75% = 0.9496567505720824
- Median = 0.9333122629582806
- 25% = 0.9103084415584415
- Min = 0.8990825688073394

#### precision
- Mean = 0.9975961538461539
- Standard deviation = 0.006359979113136049
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 1.0
- Min = 0.9807692307692307

#### recall
- Mean = 0.8791666666666667
- Standard deviation = 0.04545296714431547
- Max = 0.9666666666666667
- 75% = 0.9041666666666667
- Median = 0.875
- 25% = 0.8458333333333333
- Min = 0.8166666666666667

#### facing_probas
- Mean = [0.00357143 0.00464286 0.24232143 0.949375   0.951875  ]
- Standard deviation = [0.0013416  0.00605038 0.02083767 0.0096597  0.01483394]
- Max = [0.00571429 0.0197619  0.27880952 0.96547619 0.975     ]
- 75% = [0.00446429 0.00464286 0.25184524 0.95517857 0.95815476]
- Median = [0.00345238 0.00166667 0.24392857 0.94904762 0.95142857]
- 25% = [0.0027381  0.00136905 0.22434524 0.94553571 0.94428571]
- Min = [1.42857143e-03 4.76190476e-04 2.11428571e-01 9.30000000e-01
 9.27857143e-01]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 238.875 | 0.125 |
| Actual Positive | 7.25 | 52.75 |

### robot-6
#### accuracy
- Mean = 0.8545150501672241
- Standard deviation = 0.01672240802675584
- Max = 0.8729096989966555
- 75% = 0.8662207357859532
- Median = 0.8612040133779264
- 25% = 0.8469899665551839
- Min = 0.8193979933110368

#### f1
- Mean = 0.9214624826485985
- Standard deviation = 0.009811025114161818
- Max = 0.932142857142857
- 75% = 0.9283154121863798
- Median = 0.9254189673544512
- 25% = 0.91715107677133
- Min = 0.900735294117647

#### precision
- Mean = 1.0
- Standard deviation = 0.0
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 1.0
- Min = 1.0

#### recall
- Mean = 0.8545150501672241
- Standard deviation = 0.01672240802675584
- Max = 0.8729096989966555
- 75% = 0.8662207357859532
- Median = 0.8612040133779264
- 25% = 0.8469899665551839
- Min = 0.8193979933110368

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
| Actual Positive | 43.5 | 255.5 |

