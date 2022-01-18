# ExtraTreesClassifier_SMOTETomek_2022-01-17-03-53_no5
## Constants
- CSV_PATH = ../out/csv/experiment
- OUTPUT_PATH = ../out/experiment_result/data_of_2022-01-13_eval_system/AGC-0angle-1m
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
	- n_estimators = 150
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

#### Importance of features
- gp_max_val_min = 0.2207587491833188
- gp_auc_min = 0.17984703662752063
- gp_auc_mean = 0.12324713412803158
- gp_max_val_mean = 0.12180594950200396
- gp_max_val_max = 0.06683462145057861
- gp_auc_max = 0.059681021399178844
- gp_max_val_range = 0.040649937466325205
- hlbr = 0.03569008527746899
- srmr = 0.02460864239506699
- gp_auc_range = 0.021955155460168328
- gp_max_ix_min = 0.015636933412171004
- tdoa_range = 0.01349734079970951
- gp_max_val_std = 0.011175970370955123
- gp_max_ix_range = 0.00928959274332869
- gp_auc_std = 0.007197959589529237
- tdoa_min = 0.007017635287523349
- gp_max_ix_mean = 0.006858853109005558
- gp_max_ix_std = 0.0068337557579771
- tdoa_max = 0.006701558611510911
- gp_max_ix_max = 0.006482713085754011
- high_power = 0.004840309405841821
- tdoa_std = 0.0024314335766949407
- coe1[1] = 0.0021034208301565246
- diff_std = 0.0015703866111680335
- diff_auc = 0.0008844488288188007
- tdoa_mean = 0.0008345533437376792
- ac_auc = 0.00034459132267120914
- coe1[0] = 0.0003352047341784794
- ratio_max_to_10ms_ave_peaks = 0.0002810298196925468
- coe3[2] = 0.0001871179682847267
- ac_std = 0.0001645953102263781
- coe3[3] = 0.0001523921437797914
- ratio_max_to_9th_ave_peaks = 9.98704476226261e-05
- low_power = 0.0
- coe3[0] = 0.0
- coe3[1] = 0.0

## Evaluation
cv = 8
### robot-1
#### accuracy
- Mean = 0.9419191919191919
- Standard deviation = 0.03936479108111086
- Max = 0.98989898989899
- 75% = 0.9646464646464646
- Median = 0.9494949494949495
- 25% = 0.9318181818181819
- Min = 0.8585858585858586

#### f1
- Mean = 0.8737747719420652
- Standard deviation = 0.07082178710961912
- Max = 0.9743589743589743
- 75% = 0.9160714285714286
- Median = 0.8809523809523809
- 25% = 0.8356605800214824
- Min = 0.7407407407407407

#### precision
- Mean = 0.8327792376093593
- Standard deviation = 0.12612267387373263
- Max = 1.0
- 75% = 0.9041666666666666
- Median = 0.8636363636363636
- 25% = 0.7860501567398119
- Min = 0.5882352941176471

#### recall
- Mean = 0.9375
- Standard deviation = 0.059947894041408975
- Max = 1.0
- 75% = 0.9624999999999999
- Median = 0.95
- 25% = 0.9375
- Min = 0.8

#### facing_probas
- Mean = [0.81836983 0.1894829  0.02841379 0.00261789 0.00986974]
- Standard deviation = [0.08454852 0.06001833 0.0209502  0.00255008 0.01160243]
- Max = [0.90035293 0.27233231 0.08057659 0.00646661 0.03838417]
- 75% = [0.86524791 0.25323222 0.02977878 0.00549555 0.01143759]
- Median = [0.83821356 0.16665159 0.02308803 0.00125909 0.00628461]
- 25% = [8.05420962e-01 1.41756970e-01 1.74282204e-02 4.55973193e-04
 1.57096931e-03]
- Min = [6.17032941e-01 1.16317393e-01 9.05610250e-03 6.06060606e-05
 7.87878788e-04]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 74.5 | 4.5 |
| Actual Positive | 1.25 | 18.75 |

### robot-2
#### accuracy
- Mean = 0.8926767676767677
- Standard deviation = 0.02471008306916786
- Max = 0.9191919191919192
- 75% = 0.9116161616161615
- Median = 0.8939393939393939
- 25% = 0.8863636363636364
- Min = 0.8383838383838383

#### f1
- Mean = 0.645759924189695
- Standard deviation = 0.11780988404296323
- Max = 0.7647058823529412
- 75% = 0.7366310160427809
- Median = 0.6663306451612903
- 25% = 0.6083743842364533
- Min = 0.3846153846153846

#### precision
- Mean = 0.9299138361638362
- Standard deviation = 0.04976364578930769
- Max = 1.0
- 75% = 0.9464285714285714
- Median = 0.9258241758241759
- 25% = 0.9147727272727273
- Min = 0.8333333333333334

#### recall
- Mean = 0.5062500000000001
- Standard deviation = 0.1285435237575196
- Max = 0.65
- 75% = 0.6125
- Median = 0.525
- 25% = 0.4375
- Min = 0.25

#### facing_probas
- Mean = [0.58862259 0.71257325 0.60246082 0.01054348 0.00533926]
- Standard deviation = [0.11891875 0.04827181 0.06916874 0.00780136 0.00280873]
- Max = [0.80678086 0.80134881 0.69289363 0.02851467 0.01225376]
- 75% = [0.67900628 0.74654451 0.66670404 0.01167007 0.00564792]
- Median = [0.55275319 0.69647335 0.6099504  0.00708082 0.00402814]
- 25% = [0.50733282 0.68062069 0.53271873 0.00591102 0.00367862]
- Min = [0.4146135  0.6474524  0.50593225 0.00399401 0.00332094]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 78.25 | 0.75 |
| Actual Positive | 9.875 | 10.125 |

### robot-3
#### accuracy
- Mean = 0.9343434343434343
- Standard deviation = 0.021427478217774173
- Max = 0.9696969696969697
- 75% = 0.952020202020202
- Median = 0.9292929292929293
- 25% = 0.9166666666666667
- Min = 0.9090909090909091

#### f1
- Mean = 0.8350652345838482
- Standard deviation = 0.048850111232259845
- Max = 0.9189189189189189
- 75% = 0.8723328591749644
- Median = 0.8205128205128205
- 25% = 0.7951219512195123
- Min = 0.7804878048780488

#### precision
- Mean = 0.8617051206447491
- Standard deviation = 0.08424890115797327
- Max = 1.0
- 75% = 0.9419934640522876
- Median = 0.8421052631578947
- 25% = 0.7904761904761906
- Min = 0.7619047619047619

#### recall
- Mean = 0.8125
- Standard deviation = 0.02165063509461094
- Max = 0.85
- 75% = 0.8125
- Median = 0.8
- 25% = 0.8
- Min = 0.8

#### facing_probas
- Mean = [0.10570331 0.36507801 0.77730351 0.22121931 0.02558414]
- Standard deviation = [0.05848577 0.14119641 0.03997635 0.10999736 0.0215466 ]
- Max = [0.22425124 0.55859635 0.84645628 0.45218004 0.06449036]
- 75% = [0.13351999 0.53157166 0.80773555 0.2888752  0.03564413]
- Median = [0.08342514 0.30384204 0.77600197 0.16697849 0.01352673]
- 25% = [0.06006387 0.23756739 0.74361749 0.13773633 0.01003375]
- Min = [0.04625738 0.22052516 0.72459726 0.11570051 0.00721739]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 76.25 | 2.75 |
| Actual Positive | 3.75 | 16.25 |

### robot-4
#### accuracy
- Mean = 0.9191919191919192
- Standard deviation = 0.029449251994168167
- Max = 0.9595959595959596
- 75% = 0.9343434343434344
- Median = 0.9242424242424243
- 25% = 0.9090909090909092
- Min = 0.8686868686868687

#### f1
- Mean = 0.7929822976815458
- Standard deviation = 0.06950419991276423
- Max = 0.9047619047619047
- 75% = 0.8260568260568261
- Median = 0.7886762360446571
- 25% = 0.7670068027210885
- Min = 0.6666666666666667

#### precision
- Mean = 0.7946096459178638
- Standard deviation = 0.09361648716272673
- Max = 0.9285714285714286
- 75% = 0.8375
- Median = 0.8248081841432224
- 25% = 0.7685758513931888
- Min = 0.6

#### recall
- Mean = 0.8092105263157895
- Standard deviation = 0.12041450801133637
- Max = 1.0
- 75% = 0.9078947368421053
- Median = 0.7894736842105263
- 25% = 0.7236842105263157
- Min = 0.631578947368421

#### facing_probas
- Mean = [0.00084175 0.00716532 0.19106185 0.72638413 0.20022667]
- Standard deviation = [0.00051277 0.00535061 0.13298656 0.06286743 0.11569472]
- Max = [0.00151378 0.01909349 0.45807164 0.84191252 0.38199738]
- 75% = [0.0012466  0.00873089 0.27908793 0.75425743 0.31790863]
- Median = [0.00097395 0.00624834 0.11994585 0.71943568 0.13859266]
- 25% = [4.42890443e-04 3.22840996e-03 8.96988668e-02 6.72800533e-01
 1.02116387e-01]
- Min = [0.         0.00173042 0.06470582 0.65501549 0.08413552]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 75.625 | 4.375 |
| Actual Positive | 3.625 | 15.375 |

### robot-5
#### accuracy
- Mean = 0.9356060606060606
- Standard deviation = 0.031107790390795243
- Max = 0.9797979797979798
- 75% = 0.9494949494949495
- Median = 0.9444444444444444
- 25% = 0.9318181818181819
- Min = 0.8686868686868687

#### f1
- Mean = 0.7992564692354964
- Standard deviation = 0.12247765439780636
- Max = 0.9473684210526316
- 75% = 0.8571428571428571
- Median = 0.8403361344537814
- 25% = 0.7950664136622391
- Min = 0.5185185185185185

#### precision
- Mean = 1.0
- Standard deviation = 0.0
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 1.0
- Min = 1.0

#### recall
- Mean = 0.68125
- Standard deviation = 0.1539835624344365
- Max = 0.9
- 75% = 0.75
- Median = 0.725
- 25% = 0.6625
- Min = 0.35

#### facing_probas
- Mean = [0.01151973 0.00085918 0.05159914 0.50408114 0.67582933]
- Standard deviation = [0.01128327 0.0008377  0.0264203  0.10853773 0.07484123]
- Max = [0.040444   0.00241928 0.1060111  0.66551109 0.8098398 ]
- 75% = [0.01116062 0.00134861 0.06118915 0.58663396 0.71951437]
- Median = [6.49785360e-03 5.87878788e-04 5.37273723e-02 4.89853237e-01
 6.68387274e-01]
- 25% = [5.63836772e-03 1.43939394e-04 3.09222189e-02 4.15562575e-01
 6.45989808e-01]
- Min = [0.00412453 0.         0.01544215 0.36448473 0.55726029]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 79.0 | 0.0 |
| Actual Positive | 6.375 | 13.625 |

### robot-6
#### accuracy
- Mean = 0.7487373737373737
- Standard deviation = 0.05331513214827629
- Max = 0.8383838383838383
- 75% = 0.7777777777777778
- Median = 0.7676767676767676
- 25% = 0.702020202020202
- Min = 0.6666666666666666

#### f1
- Mean = 0.855250549197463
- Standard deviation = 0.03501789482015442
- Max = 0.9120879120879121
- 75% = 0.8750000000000001
- Median = 0.8685714285714284
- 25% = 0.8248945895191864
- Min = 0.8

#### precision
- Mean = 1.0
- Standard deviation = 0.0
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 1.0
- Min = 1.0

#### recall
- Mean = 0.7487373737373737
- Standard deviation = 0.05331513214827629
- Max = 0.8383838383838383
- 75% = 0.7777777777777778
- Median = 0.7676767676767676
- 25% = 0.702020202020202
- Min = 0.6666666666666666

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
| Actual Positive | 24.875 | 74.125 |

