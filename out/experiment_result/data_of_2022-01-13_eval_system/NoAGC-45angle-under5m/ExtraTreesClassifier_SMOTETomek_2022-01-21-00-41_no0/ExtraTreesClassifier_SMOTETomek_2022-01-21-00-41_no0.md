# ExtraTreesClassifier_SMOTETomek_2022-01-21-00-41_no0
## Constants
- CSV_PATH = ../out/csv/experiment
- OUTPUT_PATH = ../out/experiment_result/data_of_2022-01-13_eval_system/NoAGC-45angle-under5m
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
- AGC_STATUS = ['NoAGC']

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
	- n_estimators = 290
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
- gp_max_val_mean = 0.13187721310713732
- gp_max_val_min = 0.11368092041713705
- gp_auc_min = 0.11337606433696941
- gp_auc_max = 0.09604955924016355
- gp_max_val_max = 0.0949752917065701
- gp_auc_mean = 0.09291581988477761
- srmr = 0.049901602127893754
- gp_max_ix_mean = 0.038481503963321236
- tdoa_mean = 0.03765763988444093
- hlbr = 0.02637090607618992
- gp_max_ix_std = 0.02223532144986647
- tdoa_std = 0.01812999351598067
- ratio_max_to_10ms_ave_peaks = 0.01527140656597135
- diff_auc = 0.012565535269704858
- gp_max_val_std = 0.012384628772406743
- diff_std = 0.01191507955512681
- gp_auc_range = 0.01141762699829787
- gp_auc_std = 0.010820712258248084
- gp_max_val_range = 0.010678215822530042
- gp_max_ix_min = 0.009288978098289461
- high_power = 0.008975864527961092
- tdoa_min = 0.008689092586720114
- gp_max_ix_range = 0.005971546297055576
- tdoa_max = 0.00575975422998925
- tdoa_range = 0.005392562744209623
- gp_max_ix_max = 0.005127372219344674
- coe1[0] = 0.004479294845219375
- coe3[2] = 0.00432620112220195
- coe3[3] = 0.004223895976820898
- coe1[1] = 0.004157133995553548
- low_power = 0.003827027737076758
- ac_std = 0.0037729371548486245
- ratio_max_to_9th_ave_peaks = 0.002753475075451912
- ac_auc = 0.0025498224365234864
- coe3[0] = 0.0
- coe3[1] = 0.0

## Evaluation
cv = 8
### robot-1
#### accuracy
- Mean = 0.9691666666666666
- Standard deviation = 0.011023963796102446
- Max = 0.9833333333333333
- 75% = 0.9783333333333333
- Median = 0.97
- 25% = 0.9591666666666666
- Min = 0.9533333333333334

#### f1
- Mean = 0.9241734790601912
- Standard deviation = 0.025062282656574397
- Max = 0.9586776859504132
- 75% = 0.9436640654031958
- Median = 0.9242937853107345
- 25% = 0.9009042033235581
- Min = 0.8925619834710743

#### precision
- Mean = 0.9198940195594936
- Standard deviation = 0.05281550920391679
- Max = 0.9824561403508771
- 75% = 0.958569299552906
- Median = 0.9321839080459771
- 25% = 0.8826844262295082
- Min = 0.8194444444444444

#### recall
- Mean = 0.93125
- Standard deviation = 0.029389033290970572
- Max = 0.9833333333333333
- 75% = 0.9416666666666667
- Median = 0.9333333333333333
- 25% = 0.9
- Min = 0.9

#### facing_probas
- Mean = [0.91425166 0.70436292 0.14791379 0.01134647 0.00647229]
- Standard deviation = [0.02414843 0.04831467 0.04712416 0.00858187 0.00472359]
- Max = [0.94651218 0.79843731 0.22716227 0.02108151 0.01267869]
- 75% = [0.93628963 0.73502702 0.18414976 0.01935376 0.01097177]
- Median = [0.91436889 0.6937334  0.13969099 0.01274627 0.00575506]
- 25% = [0.88974267 0.66101631 0.1170924  0.00224111 0.00187213]
- Min = [8.85832330e-01 6.53020183e-01 7.95680077e-02 6.66392994e-04
 1.09774676e-03]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 234.875 | 5.125 |
| Actual Positive | 4.125 | 55.875 |

### robot-2
#### accuracy
- Mean = 0.9329166666666666
- Standard deviation = 0.01751487463081974
- Max = 0.9566666666666667
- 75% = 0.9508333333333333
- Median = 0.9299999999999999
- 25% = 0.9183333333333333
- Min = 0.91

#### f1
- Mean = 0.8070376725959737
- Standard deviation = 0.05655765909766485
- Max = 0.882882882882883
- 75% = 0.8643815834182806
- Median = 0.7980074061012168
- 25% = 0.7654824305960009
- Min = 0.7272727272727274

#### precision
- Mean = 0.9382084443109424
- Standard deviation = 0.02816974569829351
- Max = 0.9791666666666666
- 75% = 0.9595838335334134
- Median = 0.9436948624805397
- 25% = 0.9184981684981686
- Min = 0.8913043478260869

#### recall
- Mean = 0.7104166666666667
- Standard deviation = 0.07497105923102741
- Max = 0.8166666666666667
- 75% = 0.7833333333333333
- Median = 0.7083333333333333
- 25% = 0.6458333333333334
- Min = 0.6

#### facing_probas
- Mean = [0.89350062 0.91752318 0.79457066 0.2596955  0.03176745]
- Standard deviation = [0.03364174 0.02393188 0.04794694 0.09364943 0.01609849]
- Max = [0.94667723 0.97178129 0.87656826 0.40707312 0.05782781]
- 75% = [0.92679784 0.9236229  0.83026588 0.33185656 0.04431183]
- Median = [0.88178516 0.90971481 0.78379747 0.2647804  0.02581279]
- 25% = [0.86521641 0.90162864 0.76226567 0.19000913 0.01772593]
- Min = [0.85326624 0.89225529 0.72110192 0.12836647 0.01566099]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 237.25 | 2.75 |
| Actual Positive | 17.375 | 42.625 |

### robot-3
#### accuracy
- Mean = 0.8904166666666666
- Standard deviation = 0.022138296381308698
- Max = 0.9266666666666666
- 75% = 0.9116666666666666
- Median = 0.88
- 25% = 0.8741666666666668
- Min = 0.8666666666666667

#### f1
- Mean = 0.6214260349815784
- Standard deviation = 0.10087166851628686
- Max = 0.7755102040816326
- 75% = 0.7224091155724363
- Median = 0.5857142857142857
- 25% = 0.5437114310902145
- Min = 0.5

#### precision
- Mean = 0.9748683748683749
- Standard deviation = 0.03271107184303002
- Max = 1.0
- 75% = 1.0
- Median = 0.9864864864864865
- 25% = 0.9672077922077922
- Min = 0.9

#### recall
- Mean = 0.46458333333333335
- Standard deviation = 0.11100472337297684
- Max = 0.6333333333333333
- 75% = 0.575
- Median = 0.42500000000000004
- 25% = 0.375
- Min = 0.3333333333333333

#### facing_probas
- Mean = [0.42767081 0.86003648 0.89295964 0.73082337 0.27706832]
- Standard deviation = [0.10892208 0.04367769 0.03820902 0.07503163 0.09475971]
- Max = [0.63105743 0.95462311 0.94569454 0.87099104 0.46182861]
- 75% = [0.47422299 0.87890037 0.93422084 0.77529862 0.33011284]
- Median = [0.38716538 0.85086694 0.88674106 0.72243901 0.24039628]
- 25% = [0.35226427 0.83007578 0.85408323 0.67539049 0.19584268]
- Min = [0.31649485 0.80512172 0.84723602 0.62823431 0.186521  ]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 239.25 | 0.75 |
| Actual Positive | 32.125 | 27.875 |

### robot-4
#### accuracy
- Mean = 0.8466666666666667
- Standard deviation = 0.034318767136623345
- Max = 0.8833333333333333
- 75% = 0.8716666666666667
- Median = 0.8600000000000001
- 25% = 0.8283333333333334
- Min = 0.7766666666666666

#### f1
- Mean = 0.5341768963607447
- Standard deviation = 0.09854907314425852
- Max = 0.6407766990291263
- 75% = 0.6112711213517665
- Median = 0.5729312762973353
- 25% = 0.47151360544217685
- Min = 0.34951456310679613

#### precision
- Mean = 0.6920621081709668
- Standard deviation = 0.14555573636746313
- Max = 0.8787878787878788
- 75% = 0.8139204545454546
- Median = 0.710644007155635
- 25% = 0.6125730994152047
- Min = 0.4186046511627907

#### recall
- Mean = 0.4395833333333333
- Standard deviation = 0.08856004711180118
- Max = 0.5666666666666667
- 75% = 0.5
- Median = 0.44166666666666665
- 25% = 0.38333333333333336
- Min = 0.3

#### facing_probas
- Mean = [0.02871734 0.43604138 0.84062677 0.9150938  0.76488953]
- Standard deviation = [0.02484823 0.08484797 0.05971237 0.04589587 0.08464113]
- Max = [0.07784421 0.64229039 0.93063784 0.97602684 0.90595293]
- 75% = [0.03804101 0.44707317 0.88639615 0.95842627 0.83675007]
- Median = [0.02042807 0.40585727 0.83076511 0.91485116 0.74968015]
- 25% = [0.00784963 0.38193202 0.79319536 0.87331635 0.69239255]
- Min = [0.00619885 0.36015305 0.75878806 0.85374959 0.6624717 ]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 227.625 | 12.375 |
| Actual Positive | 33.625 | 26.375 |

### robot-5
#### accuracy
- Mean = 0.9466666666666667
- Standard deviation = 0.01674979270186817
- Max = 0.9633333333333334
- 75% = 0.9608333333333333
- Median = 0.9533333333333334
- 25% = 0.9341666666666666
- Min = 0.9166666666666666

#### f1
- Mean = 0.8463786230946201
- Standard deviation = 0.05832012438820754
- Max = 0.9043478260869566
- 75% = 0.8948680823680824
- Median = 0.8702735145331391
- 25% = 0.8066504854368932
- Min = 0.7368421052631579

#### precision
- Mean = 0.9746805738615345
- Standard deviation = 0.014770734925983828
- Max = 1.0
- 75% = 0.9797919167667066
- Median = 0.9777337951509153
- 25% = 0.9716346153846154
- Min = 0.9454545454545454

#### recall
- Mean = 0.7541666666666667
- Standard deviation = 0.0938194187433142
- Max = 0.8666666666666667
- 75% = 0.8333333333333334
- Median = 0.7833333333333334
- 25% = 0.6875
- Min = 0.5833333333333334

#### facing_probas
- Mean = [0.01471648 0.02600128 0.30677232 0.88496576 0.87547583]
- Standard deviation = [0.00813462 0.01633327 0.11111438 0.05413377 0.05391692]
- Max = [0.03180451 0.06000267 0.53513047 0.95690346 0.95452075]
- 75% = [0.01779469 0.03158999 0.34020362 0.93227561 0.92116513]
- Median = [0.01227691 0.02285337 0.29030829 0.88419501 0.87244603]
- 25% = [0.00922778 0.01129875 0.20519635 0.83667825 0.8286062 ]
- Min = [0.00510767 0.00993407 0.19783491 0.81449065 0.79691409]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 238.75 | 1.25 |
| Actual Positive | 14.75 | 45.25 |

### robot-6
#### accuracy
- Mean = 0.6599999999999999
- Standard deviation = 0.05408326913195985
- Max = 0.7266666666666667
- 75% = 0.7116666666666667
- Median = 0.6583333333333333
- 25% = 0.6216666666666667
- Min = 0.57

#### f1
- Mean = 0.793892021143127
- Standard deviation = 0.0395700588073538
- Max = 0.8416988416988418
- 75% = 0.8315184604247104
- Median = 0.7939101553977066
- 25% = 0.7666655329569417
- Min = 0.7261146496815287

#### precision
- Mean = 1.0
- Standard deviation = 0.0
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 1.0
- Min = 1.0

#### recall
- Mean = 0.6599999999999999
- Standard deviation = 0.05408326913195985
- Max = 0.7266666666666667
- 75% = 0.7116666666666667
- Median = 0.6583333333333333
- 25% = 0.6216666666666667
- Min = 0.57

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
| Actual Positive | 102.0 | 198.0 |

