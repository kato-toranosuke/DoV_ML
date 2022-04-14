# ExtraTreesClassifier_SMOTETomek_2022-04-13-01-51_no2
## Constants
- CSV_PATH = ../out/csv/experiment
- OUTPUT_PATH = ../out/experiment_result/data_of_2022-03-23_eval_system/AGC-30deg-0angle-3m
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
- DISTANCE = [3]
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
	- n_estimators = 90
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
	- oob_decision_function_ = [[0.23251667 0.76748333]
 [0.56594153 0.43405847]
 [0.32430637 0.67569363]
 [0.48582118 0.51417882]
 [0.25584775 0.74415225]
 [0.41414496 0.58585504]
 [0.39313209 0.60686791]
 [0.73272401 0.26727599]
 [0.80046678 0.19953322]
 [0.69640629 0.30359371]
 [0.71890909 0.28109091]
 [0.72881811 0.27118189]
 [0.77518134 0.22481866]
 [0.37294123 0.62705877]
 [0.51178535 0.48821465]
 [0.40888268 0.59111732]
 [0.28369218 0.71630782]
 [0.58907991 0.41092009]
 [0.47931264 0.52068736]
 [0.41746391 0.58253609]
 [0.75512401 0.24487599]
 [0.6093927  0.3906073 ]
 [0.74042292 0.25957708]
 [0.76370007 0.23629993]
 [0.54763737 0.45236263]
 [0.30347886 0.69652114]
 [0.31224398 0.68775602]
 [0.36451503 0.63548497]
 [0.25399233 0.74600767]
 [0.27193612 0.72806388]
 [0.67080408 0.32919592]
 [0.75753355 0.24246645]
 [0.42041453 0.57958547]
 [0.74775615 0.25224385]
 [0.7991477  0.2008523 ]
 [0.82679766 0.17320234]
 [0.73266107 0.26733893]
 [0.58634163 0.41365837]
 [0.71592097 0.28407903]
 [0.34949882 0.65050118]
 [0.33249506 0.66750494]
 [0.19009289 0.80990711]
 [0.46156697 0.53843303]
 [0.75141832 0.24858168]
 [0.31131019 0.68868981]
 [0.80633978 0.19366022]
 [0.76830973 0.23169027]
 [0.83889441 0.16110559]
 [0.83921222 0.16078778]
 [0.82917012 0.17082988]
 [0.83967026 0.16032974]
 [0.80971939 0.19028061]
 [0.71129483 0.28870517]
 [0.65092158 0.34907842]
 [0.40210975 0.59789025]
 [0.37961456 0.62038544]
 [0.50496479 0.49503521]
 [0.25026977 0.74973023]
 [0.23750918 0.76249082]
 [0.36843579 0.63156421]
 [0.52779324 0.47220676]
 [0.23639138 0.76360862]
 [0.17912317 0.82087683]
 [0.523161   0.476839  ]
 [0.27033352 0.72966648]
 [0.41709949 0.58290051]
 [0.32689928 0.67310072]
 [0.17851644 0.82148356]
 [0.29620125 0.70379875]
 [0.31534952 0.68465048]
 [0.19688735 0.80311265]
 [0.35602153 0.64397847]
 [0.40844282 0.59155718]
 [0.43840006 0.56159994]
 [0.32420265 0.67579735]
 [0.4601002  0.5398998 ]
 [0.23506951 0.76493049]
 [0.39136391 0.60863609]
 [0.36972861 0.63027139]
 [0.21472972 0.78527028]
 [0.28744103 0.71255897]
 [0.26612131 0.73387869]
 [0.40315943 0.59684057]
 [0.34615936 0.65384064]
 [0.3228669  0.6771331 ]
 [0.29310056 0.70689944]
 [0.20903702 0.79096298]
 [0.55789855 0.44210145]
 [0.51792279 0.48207721]
 [0.27713483 0.72286517]
 [0.30053603 0.69946397]
 [0.22078737 0.77921263]
 [0.21593554 0.78406446]
 [0.38380831 0.61619169]]
	- oob_score_ = 0.7446808510638298

#### Importance of features
- gp_max_val_max = 0.13216623797932447
- gp_auc_max = 0.11284174519899197
- gp_max_val_mean = 0.09802621311537679
- hlbr = 0.07909663553936427
- gp_max_val_min = 0.07548609026959549
- gp_max_ix_min = 0.05936349885209207
- gp_auc_min = 0.040773702551697655
- coe3[3] = 0.03752523130192287
- tdoa_range = 0.03325499567522601
- gp_auc_mean = 0.03233693120169706
- diff_std = 0.02865014389889601
- gp_auc_std = 0.025897441335754622
- ratio_max_to_9th_ave_peaks = 0.02540307554220262
- gp_max_ix_std = 0.024781404017213196
- gp_max_ix_range = 0.023910613386312025
- tdoa_min = 0.023817795877121354
- coe3[2] = 0.022593029729872406
- high_power = 0.021169178641824184
- srmr = 0.020104033087803435
- gp_max_val_range = 0.01878852977168229
- gp_max_val_std = 0.015818966509014508
- ac_auc = 0.012893047524502346
- diff_auc = 0.011739148306256839
- gp_auc_range = 0.009176965486266021
- ratio_max_to_10ms_ave_peaks = 0.0069386444790278225
- coe1[1] = 0.005066741292698833
- low_power = 0.002033977428288448
- gp_max_ix_mean = 0.0003459819999743945
- coe1[0] = 0.0
- coe3[0] = 0.0
- coe3[1] = 0.0
- ac_std = 0.0
- gp_max_ix_max = 0.0
- tdoa_std = 0.0
- tdoa_max = 0.0
- tdoa_mean = 0.0

## Evaluation
cv = 8
### robot-1
#### accuracy
- Mean = 0.8325
- Standard deviation = 0.04736823830374103
- Max = 0.9
- 75% = 0.8674999999999999
- Median = 0.835
- 25% = 0.79
- Min = 0.76

#### f1
- Mean = 0.6276547514733977
- Standard deviation = 0.08211456714730542
- Max = 0.7317073170731706
- 75% = 0.7009844134536505
- Median = 0.6294642857142856
- 25% = 0.5495090016366612
- Min = 0.5263157894736842

#### precision
- Mean = 0.5974237787276581
- Standard deviation = 0.14589552227505787
- Max = 0.9166666666666666
- 75% = 0.6401098901098902
- Median = 0.5656565656565657
- 25% = 0.4824393358876118
- Min = 0.4375

#### recall
- Mean = 0.7
- Standard deviation = 0.1322875655532295
- Max = 0.95
- 75% = 0.7625
- Median = 0.7
- 25% = 0.625
- Min = 0.5

#### facing_probas
- Mean = [0.57014837 0.30151747 0.20363457 0.15319494 0.16347461]
- Standard deviation = [0.07984734 0.0567591  0.02721116 0.0289625  0.02885022]
- Max = [0.67868937 0.41558745 0.23661964 0.20951035 0.20306464]
- 75% = [0.63333799 0.31928035 0.22869571 0.16969834 0.18682108]
- Median = [0.57084061 0.2894766  0.20711897 0.15081279 0.16584037]
- 25% = [0.51798479 0.26436736 0.17819346 0.13776733 0.14362585]
- Min = [0.45228512 0.23589943 0.16133904 0.10967091 0.11300057]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 69.25 | 10.75 |
| Actual Positive | 6.0 | 14.0 |

### robot-2
#### accuracy
- Mean = 0.83375
- Standard deviation = 0.03739568825412897
- Max = 0.89
- 75% = 0.855
- Median = 0.84
- 25% = 0.8125
- Min = 0.77

#### f1
- Mean = 0.3918059073328213
- Standard deviation = 0.1644874628087374
- Max = 0.6451612903225806
- 75% = 0.5015673981191223
- Median = 0.4
- 25% = 0.2952853598014888
- Min = 0.08695652173913045

#### precision
- Mean = 0.7221250971250972
- Standard deviation = 0.25281853075989
- Max = 1.0
- 75% = 0.9318181818181818
- Median = 0.7777777777777777
- 25% = 0.5524475524475525
- Min = 0.3333333333333333

#### recall
- Mean = 0.28125
- Standard deviation = 0.1344839674459376
- Max = 0.5
- 75% = 0.4
- Median = 0.25
- 25% = 0.2
- Min = 0.05

#### facing_probas
- Mean = [0.62076217 0.59057636 0.53990697 0.21481617 0.16741572]
- Standard deviation = [0.05022363 0.05021333 0.06301285 0.04573642 0.02848976]
- Max = [0.69022779 0.66350092 0.63533178 0.31303516 0.21967141]
- 75% = [0.66402849 0.6246637  0.57305127 0.23413611 0.18131036]
- Median = [0.62407091 0.60885908 0.5452674  0.20808593 0.17153673]
- 25% = [0.58843742 0.54264277 0.50600186 0.17842091 0.14048772]
- Min = [0.54444717 0.51345181 0.4353316  0.1658104  0.12954303]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 77.75 | 2.25 |
| Actual Positive | 14.375 | 5.625 |

### robot-3
#### accuracy
- Mean = 0.8087500000000001
- Standard deviation = 0.04960783708246108
- Max = 0.9
- 75% = 0.8200000000000001
- Median = 0.81
- 25% = 0.795
- Min = 0.73

#### f1
- Mean = 0.5921207383697914
- Standard deviation = 0.09150137911143531
- Max = 0.7368421052631577
- 75% = 0.6477987421383647
- Median = 0.6039947894051239
- 25% = 0.5455927051671733
- Min = 0.4444444444444444

#### precision
- Mean = 0.5656697024980906
- Standard deviation = 0.15266892725301093
- Max = 0.8571428571428571
- 75% = 0.5833333333333333
- Median = 0.51619644723093
- 25% = 0.4897862979258328
- Min = 0.4074074074074074

#### recall
- Mean = 0.7124999999999999
- Standard deviation = 0.19645292056877137
- Max = 0.95
- 75% = 0.8625
- Median = 0.725
- 25% = 0.6625
- Min = 0.3

#### facing_probas
- Mean = [0.43876324 0.58841414 0.65364293 0.4430753  0.21017511]
- Standard deviation = [0.08772335 0.04691009 0.04741367 0.07913345 0.03111575]
- Max = [0.5488438  0.66969193 0.74516412 0.62965482 0.26553055]
- 75% = [0.50694223 0.61265247 0.67477833 0.46688412 0.22971493]
- Median = [0.46262799 0.59188638 0.64020625 0.415497   0.21118327]
- 25% = [0.38085136 0.55708684 0.61778441 0.38561587 0.18248744]
- Min = [0.30189219 0.51531315 0.59813515 0.37615391 0.16799493]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 66.625 | 13.375 |
| Actual Positive | 5.75 | 14.25 |

### robot-4
#### accuracy
- Mean = 0.7562500000000001
- Standard deviation = 0.047942022276912785
- Max = 0.85
- 75% = 0.79
- Median = 0.745
- 25% = 0.7175
- Min = 0.7

#### f1
- Mean = 0.2601159966620159
- Standard deviation = 0.19692104148910522
- Max = 0.5945945945945946
- 75% = 0.3418171866447729
- Median = 0.21590909090909094
- 25% = 0.14797794117647056
- Min = 0.0

#### precision
- Mean = 0.2935717146130963
- Standard deviation = 0.19373636603412753
- Max = 0.6470588235294118
- 75% = 0.4076227390180878
- Median = 0.28205128205128205
- 25% = 0.18154761904761904
- Min = 0.0

#### recall
- Mean = 0.26875
- Standard deviation = 0.2680222705298946
- Max = 0.85
- 75% = 0.28750000000000003
- Median = 0.175
- 25% = 0.125
- Min = 0.0

#### facing_probas
- Mean = [0.23333297 0.43931517 0.63731625 0.58707602 0.43252164]
- Standard deviation = [0.03982804 0.07931846 0.06469515 0.05672311 0.07224118]
- Max = [0.29246865 0.60170973 0.78482435 0.69692339 0.57741549]
- 75% = [0.25594407 0.46720328 0.64767309 0.60052287 0.48091779]
- Median = [0.23593868 0.41907292 0.61882677 0.57114189 0.39851774]
- 25% = [0.21164178 0.39805984 0.59576561 0.55762994 0.37269219]
- Min = [0.15644978 0.31843413 0.57555428 0.51177443 0.36731333]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 70.25 | 9.75 |
| Actual Positive | 14.625 | 5.375 |

### robot-5
#### accuracy
- Mean = 0.86375
- Standard deviation = 0.034255474015111795
- Max = 0.95
- 75% = 0.8625
- Median = 0.855
- 25% = 0.84
- Min = 0.84

#### f1
- Mean = 0.46234228734228733
- Standard deviation = 0.16311079155377306
- Max = 0.8571428571428571
- 75% = 0.47578347578347574
- Median = 0.4307692307692308
- 25% = 0.33333333333333337
- Min = 0.33333333333333337

#### precision
- Mean = 1.0
- Standard deviation = 0.0
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 1.0
- Min = 1.0

#### recall
- Mean = 0.31875
- Standard deviation = 0.17127737007555902
- Max = 0.75
- 75% = 0.3125
- Median = 0.275
- 25% = 0.2
- Min = 0.2

#### facing_probas
- Mean = [0.2222769  0.20679428 0.44012875 0.57253919 0.54944477]
- Standard deviation = [0.05559176 0.03282783 0.08553405 0.06702043 0.05515766]
- Max = [0.30619247 0.27170316 0.53567241 0.67168747 0.66352576]
- 75% = [0.25696003 0.22260579 0.50545625 0.61727586 0.57614628]
- Median = [0.21852207 0.20851608 0.47331202 0.58367588 0.53537456]
- 25% = [0.19059479 0.18135914 0.38269677 0.52440852 0.52283008]
- Min = [0.14449302 0.16198683 0.29761489 0.47420405 0.46667276]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 80.0 | 0.0 |
| Actual Positive | 13.625 | 6.375 |

### robot-6
#### accuracy
- Mean = 0.45625
- Standard deviation = 0.05633327169621876
- Max = 0.56
- 75% = 0.4875
- Median = 0.45
- 25% = 0.4175
- Min = 0.37

#### f1
- Mean = 0.6245747147019526
- Standard deviation = 0.05264580183544981
- Max = 0.717948717948718
- 75% = 0.655360658671917
- Median = 0.6206240487062405
- 25% = 0.5890520427529717
- Min = 0.5401459854014599

#### precision
- Mean = 1.0
- Standard deviation = 0.0
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 1.0
- Min = 1.0

#### recall
- Mean = 0.45625
- Standard deviation = 0.05633327169621876
- Max = 0.56
- 75% = 0.4875
- Median = 0.45
- 25% = 0.4175
- Min = 0.37

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
| Actual Positive | 54.375 | 45.625 |

