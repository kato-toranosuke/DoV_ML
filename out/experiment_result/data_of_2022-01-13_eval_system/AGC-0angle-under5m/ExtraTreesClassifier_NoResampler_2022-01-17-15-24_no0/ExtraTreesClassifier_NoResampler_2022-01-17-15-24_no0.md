# ExtraTreesClassifier_NoResampler_2022-01-17-15-24_no0
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
- resampler = NoResampler
- estimator = ExtraTreesClassifier

### Arguments for hyperparameter search
- resampler = NoResampler
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

- best_estimator
	- base_estimator = ExtraTreeClassifier()
	- n_estimators = 170
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
- gp_max_val_min = 0.0806247210323559
- gp_auc_min = 0.0731916420864215
- gp_max_val_mean = 0.0683700959744755
- hlbr = 0.05976479151945472
- gp_auc_mean = 0.05621930835766634
- gp_auc_max = 0.053415336723298325
- high_power = 0.053204787092296986
- gp_max_val_max = 0.0508556928455332
- gp_max_val_range = 0.03588670444104898
- diff_auc = 0.02915120669547111
- gp_auc_range = 0.028551449319479644
- gp_max_val_std = 0.02750359633776142
- diff_std = 0.026890963305519218
- gp_max_ix_mean = 0.026109363042262204
- gp_auc_std = 0.025777241544073945
- tdoa_mean = 0.02528351257285006
- srmr = 0.025135624666364303
- tdoa_std = 0.023175276734494047
- gp_max_ix_std = 0.02118618595766183
- coe3[2] = 0.019530885533228345
- coe1[1] = 0.019026897445556898
- low_power = 0.017758008941142277
- ac_auc = 0.01676534548140673
- coe3[3] = 0.015195213959694977
- ac_std = 0.01434107782740342
- coe1[0] = 0.013858552982352626
- ratio_max_to_9th_ave_peaks = 0.013724399222283684
- ratio_max_to_10ms_ave_peaks = 0.013588216037851108
- tdoa_max = 0.012424610885765637
- gp_max_ix_range = 0.011934137023942165
- tdoa_range = 0.01155876206172563
- gp_max_ix_min = 0.011309969262150865
- tdoa_min = 0.009828568060022106
- gp_max_ix_max = 0.008857855026984374
- coe3[0] = 0.0
- coe3[1] = 0.0

## Evaluation
cv = 8
### robot-1
#### accuracy
- Mean = 0.943979933110368
- Standard deviation = 0.011310827139187855
- Max = 0.9632107023411371
- 75% = 0.9498327759197325
- Median = 0.9464882943143813
- 25% = 0.9381270903010034
- Min = 0.9230769230769231

#### f1
- Mean = 0.8443977115152689
- Standard deviation = 0.03670327904574452
- Max = 0.9026548672566371
- 75% = 0.865462807940684
- Median = 0.8545454545454546
- 25% = 0.8221153846153847
- Min = 0.7766990291262136

#### precision
- Mean = 0.9462524579220175
- Standard deviation = 0.01627856515877283
- Max = 0.9772727272727273
- 75% = 0.95647512864494
- Median = 0.9405882352941176
- 25% = 0.9375581395348836
- Min = 0.9245283018867925

#### recall
- Mean = 0.7645833333333334
- Standard deviation = 0.05918280296392414
- Max = 0.85
- 75% = 0.8041666666666667
- Median = 0.7833333333333333
- 25% = 0.7125
- Min = 0.6666666666666666

#### facing_probas
- Mean = [6.64129902e-01 1.53774510e-01 2.33823529e-02 3.79901961e-04
 4.77941176e-04]
- Standard deviation = [0.03042287 0.0126482  0.00390837 0.00024723 0.00028346]
- Max = [0.71568627 0.17176471 0.02843137 0.00078431 0.00107843]
- 75% = [6.75612745e-01 1.62598039e-01 2.66421569e-02 4.65686275e-04
 5.14705882e-04]
- Median = [6.71568627e-01 1.58676471e-01 2.39705882e-02 3.92156863e-04
 4.90196078e-04]
- 25% = [6.55710784e-01 1.42573529e-01 1.93872549e-02 2.45098039e-04
 3.67647059e-04]
- Min = [0.6122549  0.13490196 0.01833333 0.         0.        ]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 236.375 | 2.625 |
| Actual Positive | 14.125 | 45.875 |

### robot-2
#### accuracy
- Mean = 0.903010033444816
- Standard deviation = 0.01906647868058762
- Max = 0.9331103678929766
- 75% = 0.9138795986622074
- Median = 0.903010033444816
- 25% = 0.8904682274247491
- Min = 0.8729096989966555

#### f1
- Mean = 0.6904009520757097
- Standard deviation = 0.08123943857271529
- Max = 0.8076923076923077
- 75% = 0.7485790245691236
- Median = 0.684745362164717
- 25% = 0.6408158280410357
- Min = 0.5581395348837209

#### precision
- Mean = 0.9392657734751931
- Standard deviation = 0.03244940275557811
- Max = 1.0
- 75% = 0.9583333333333334
- Median = 0.9342672413793103
- 25% = 0.9179174484052534
- Min = 0.8958333333333334

#### recall
- Mean = 0.5541666666666667
- Standard deviation = 0.10663736576724772
- Max = 0.7166666666666667
- 75% = 0.6375
- Median = 0.525
- 25% = 0.4875
- Min = 0.4

#### facing_probas
- Mean = [0.29455882 0.54931373 0.24580882 0.02667892 0.00080882]
- Standard deviation = [0.01942909 0.04301772 0.03441238 0.00471135 0.00025823]
- Max = [0.32588235 0.61931373 0.31990196 0.03431373 0.00127451]
- 75% = [0.30338235 0.58164216 0.25904412 0.03120098 0.00090686]
- Median = [0.30098039 0.53769608 0.23730392 0.02421569 0.00078431]
- 25% = [0.28112745 0.51169118 0.22852941 0.02343137 0.0007598 ]
- Min = [2.60000000e-01 4.98627451e-01 1.97549020e-01 2.09803922e-02
 2.94117647e-04]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 236.75 | 2.25 |
| Actual Positive | 26.75 | 33.25 |

### robot-3
#### accuracy
- Mean = 0.9460702341137124
- Standard deviation = 0.014810191959797943
- Max = 0.9732441471571907
- 75% = 0.9506688963210703
- Median = 0.9431438127090301
- 25% = 0.9406354515050168
- Min = 0.9230769230769231

#### f1
- Mean = 0.8529446006792358
- Standard deviation = 0.04369316447979802
- Max = 0.9322033898305084
- 75% = 0.8730474506336575
- Median = 0.8439841710869749
- 25% = 0.8271939843898725
- Min = 0.7964601769911505

#### precision
- Mean = 0.934402510281912
- Standard deviation = 0.044677149919436346
- Max = 1.0
- 75% = 0.9621327254305978
- Median = 0.9390502117362372
- 25% = 0.914390756302521
- Min = 0.8490566037735849

#### recall
- Mean = 0.7895833333333333
- Standard deviation = 0.0763478425075362
- Max = 0.9166666666666666
- 75% = 0.8458333333333333
- Median = 0.7666666666666666
- 25% = 0.7416666666666667
- Min = 0.6833333333333333

#### facing_probas
- Mean = [0.04612745 0.27474265 0.67422794 0.16028186 0.01339461]
- Standard deviation = [0.00945342 0.0546522  0.02463134 0.03084893 0.00325379]
- Max = [0.05901961 0.37568627 0.71637255 0.21921569 0.01911765]
- 75% = [0.05186275 0.30303922 0.68997549 0.16769608 0.01544118]
- Median = [0.05058824 0.26602941 0.67073529 0.15009804 0.01279412]
- 25% = [0.03553922 0.25041667 0.65571078 0.14259804 0.01093137]
- Min = [0.03254902 0.19519608 0.64107843 0.12284314 0.00872549]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 235.5 | 3.5 |
| Actual Positive | 12.625 | 47.375 |

### robot-4
#### accuracy
- Mean = 0.9205685618729096
- Standard deviation = 0.018145931784457142
- Max = 0.9632107023411371
- 75% = 0.9205685618729097
- Median = 0.9147157190635451
- 25% = 0.9113712374581939
- Min = 0.903010033444816

#### f1
- Mean = 0.7791850204061784
- Standard deviation = 0.054218935659710886
- Max = 0.9026548672566371
- 75% = 0.7843045112781954
- Median = 0.7663551401869159
- 25% = 0.7427857935627081
- Min = 0.7238095238095238

#### precision
- Mean = 0.8575371783595644
- Standard deviation = 0.04098594614969989
- Max = 0.9444444444444444
- 75% = 0.8718736287845547
- Median = 0.8541666666666666
- 25% = 0.8288621646623496
- Min = 0.8

#### recall
- Mean = 0.7161016949152542
- Standard deviation = 0.07178421333092128
- Max = 0.864406779661017
- 75% = 0.7542372881355932
- Median = 0.6949152542372882
- 25% = 0.6567796610169492
- Min = 0.6440677966101694

#### facing_probas
- Mean = [0.00195663 0.03068295 0.19086491 0.61168993 0.11061815]
- Standard deviation = [0.00122812 0.00434722 0.02993344 0.03272145 0.03511344]
- Max = [0.00438684 0.03798604 0.24077767 0.66470588 0.17647059]
- 75% = [0.0024676  0.03315055 0.21308574 0.6391326  0.12627119]
- Median = [0.00199402 0.03090728 0.18868395 0.60857428 0.10304088]
- 25% = [0.00114656 0.0282652  0.1752991  0.58407278 0.08826022]
- Min = [1.99401795e-04 2.44267198e-02 1.40677966e-01 5.66899302e-01
 6.75972084e-02]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 233.0 | 7.0 |
| Actual Positive | 16.75 | 42.25 |

### robot-5
#### accuracy
- Mean = 0.9013377926421404
- Standard deviation = 0.010707565614436195
- Max = 0.9130434782608695
- 75% = 0.9105351170568561
- Median = 0.9046822742474916
- 25% = 0.8896321070234113
- Min = 0.8862876254180602

#### f1
- Mean = 0.6723575611437709
- Standard deviation = 0.04737188153203613
- Max = 0.7234042553191489
- 75% = 0.7131091283459163
- Median = 0.6881720430107527
- 25% = 0.6206896551724138
- Min = 0.6046511627906976

#### precision
- Mean = 1.0
- Standard deviation = 0.0
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 1.0
- Min = 1.0

#### recall
- Mean = 0.5083333333333333
- Standard deviation = 0.05335936864527374
- Max = 0.5666666666666667
- 75% = 0.5541666666666667
- Median = 0.525
- 25% = 0.45
- Min = 0.43333333333333335

#### facing_probas
- Mean = [1.26225490e-03 3.67647059e-04 5.79779412e-02 3.43394608e-01
 5.28088235e-01]
- Standard deviation = [0.00080314 0.00023889 0.00648671 0.03226119 0.03209677]
- Max = [0.00294118 0.00078431 0.0704902  0.39264706 0.58578431]
- 75% = [1.66666667e-03 4.65686275e-04 6.16421569e-02 3.71274510e-01
 5.44730392e-01]
- Median = [9.31372549e-04 3.43137255e-04 5.76960784e-02 3.32990196e-01
 5.28578431e-01]
- 25% = [8.08823529e-04 1.71568627e-04 5.26715686e-02 3.25612745e-01
 5.05416667e-01]
- Min = [2.94117647e-04 9.80392157e-05 4.89215686e-02 2.92352941e-01
 4.76274510e-01]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 239.0 | 0.0 |
| Actual Positive | 29.5 | 30.5 |

### robot-6
#### accuracy
- Mean = 0.6663879598662208
- Standard deviation = 0.03494743234783671
- Max = 0.7157190635451505
- 75% = 0.6822742474916388
- Median = 0.6722408026755853
- 25% = 0.6446488294314381
- Min = 0.6120401337792643

#### f1
- Mean = 0.7992699169095836
- Standard deviation = 0.02524740320795263
- Max = 0.834307992202729
- 75% = 0.8110078125
- Median = 0.804
- 25% = 0.7838578404774824
- Min = 0.7593360995850623

#### precision
- Mean = 1.0
- Standard deviation = 0.0
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 1.0
- Min = 1.0

#### recall
- Mean = 0.6663879598662208
- Standard deviation = 0.03494743234783671
- Max = 0.7157190635451505
- 75% = 0.6822742474916388
- Median = 0.6722408026755853
- 25% = 0.6446488294314381
- Min = 0.6120401337792643

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
| Actual Positive | 99.75 | 199.25 |

