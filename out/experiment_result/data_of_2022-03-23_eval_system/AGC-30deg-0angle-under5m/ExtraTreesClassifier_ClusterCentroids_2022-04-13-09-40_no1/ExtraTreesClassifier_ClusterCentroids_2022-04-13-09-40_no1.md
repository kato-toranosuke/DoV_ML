# ExtraTreesClassifier_ClusterCentroids_2022-04-13-09-40_no1
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
	- n_estimators = 50
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
	- max_features = log2
	- max_leaf_nodes = None
	- min_impurity_decrease = 0.0
	- ccp_alpha = 0.0
	- n_features_in_ = 36
	- n_outputs_ = 1
	- classes_ = [0 1]
	- n_classes_ = 2
	- base_estimator_ = ExtraTreeClassifier()
	- oob_decision_function_ = [[0.73249158 0.26750842]
 [0.84446833 0.15553167]
 [0.29069743 0.70930257]
 [0.67106782 0.32893218]
 [0.72967796 0.27032204]
 [0.49970307 0.50029693]
 [0.60192503 0.39807497]
 [0.78858865 0.21141135]
 [0.68961039 0.31038961]
 [0.85002319 0.14997681]
 [0.78145415 0.21854585]
 [0.52696076 0.47303924]
 [0.59943256 0.40056744]
 [0.73830049 0.26169951]
 [0.73324471 0.26675529]
 [0.70394558 0.29605442]
 [0.62783523 0.37216477]
 [0.81036055 0.18963945]
 [0.39775283 0.60224717]
 [0.38952078 0.61047922]
 [0.60711355 0.39288645]
 [0.51586901 0.48413099]
 [0.59283762 0.40716238]
 [0.57814157 0.42185843]
 [0.63718111 0.36281889]
 [0.56568315 0.43431685]
 [0.71927438 0.28072562]
 [0.59316882 0.40683118]
 [0.67465921 0.32534079]
 [0.77940157 0.22059843]
 [0.73459318 0.26540682]
 [0.36331446 0.63668554]
 [0.63598991 0.36401009]
 [0.25977815 0.74022185]
 [0.76087662 0.23912338]
 [0.8166911  0.1833089 ]
 [0.61627592 0.38372408]
 [0.61246184 0.38753816]
 [0.5562425  0.4437575 ]
 [0.54683442 0.45316558]
 [0.62716728 0.37283272]
 [0.88036616 0.11963384]
 [0.69805308 0.30194692]
 [0.26567519 0.73432481]
 [0.87792404 0.12207596]
 [0.19244207 0.80755793]
 [0.18620611 0.81379389]
 [0.17462225 0.82537775]
 [0.38025979 0.61974021]
 [0.15428183 0.84571817]
 [0.23707381 0.76292619]
 [0.63944918 0.36055082]
 [0.43141581 0.56858419]
 [0.57503946 0.42496054]
 [0.16172161 0.83827839]
 [0.19263985 0.80736015]
 [0.17740537 0.82259463]
 [0.21154444 0.78845556]
 [0.26426351 0.73573649]
 [0.2734528  0.7265472 ]
 [0.68605311 0.31394689]
 [0.44377157 0.55622843]
 [0.57254905 0.42745095]
 [0.2642101  0.7357899 ]
 [0.22270808 0.77729192]
 [0.29300275 0.70699725]
 [0.3386754  0.6613246 ]
 [0.10650934 0.89349066]
 [0.14599871 0.85400129]
 [0.52223647 0.47776353]
 [0.52944905 0.47055095]
 [0.455562   0.544438  ]
 [0.55143353 0.44856647]
 [0.2787851  0.7212149 ]
 [0.17467842 0.82532158]
 [0.16235614 0.83764386]
 [0.32881672 0.67118328]
 [0.31597247 0.68402753]
 [0.42049764 0.57950236]
 [0.43947811 0.56052189]
 [0.73969125 0.26030875]
 [0.20640557 0.79359443]
 [0.21526529 0.78473471]
 [0.21182715 0.78817285]
 [0.365714   0.634286  ]
 [0.15426182 0.84573818]
 [0.29224975 0.70775025]
 [0.68192063 0.31807937]
 [0.47602453 0.52397547]
 [0.34937361 0.65062639]]
	- oob_score_ = 0.8222222222222222

#### Importance of features
- tdoa_mean = 0.07762426434112714
- gp_auc_mean = 0.06398274936467574
- gp_auc_min = 0.0634956800228938
- gp_max_val_min = 0.05963314509395744
- gp_max_val_max = 0.05699823059386321
- gp_max_ix_mean = 0.0543642184759695
- high_power = 0.04719747379654448
- gp_auc_max = 0.038974635967418826
- diff_auc = 0.03631239559605514
- tdoa_range = 0.03419958432459965
- srmr = 0.034085058736514386
- coe3[2] = 0.03235777283411896
- hlbr = 0.027957904413896593
- gp_auc_range = 0.02722187221227195
- gp_max_ix_std = 0.026482688169236365
- tdoa_min = 0.025979795381083096
- gp_max_val_range = 0.02465224549146637
- ratio_max_to_9th_ave_peaks = 0.023729523239593254
- gp_max_val_std = 0.023634270556080587
- ac_auc = 0.021766052455342005
- tdoa_std = 0.021091964938746578
- ac_std = 0.021001862283842643
- ratio_max_to_10ms_ave_peaks = 0.020916931252039493
- gp_max_val_mean = 0.018835957213907458
- gp_max_ix_max = 0.018371374957740515
- diff_std = 0.016829163499477596
- gp_auc_std = 0.01650750509933423
- gp_max_ix_min = 0.014901073621544657
- tdoa_max = 0.011371132858112825
- coe3[3] = 0.010934418111193637
- low_power = 0.009559859274609415
- coe1[1] = 0.006706819967200648
- gp_max_ix_range = 0.006691707586752472
- coe1[0] = 0.005630668268789286
- coe3[0] = 0.0
- coe3[1] = 0.0

## Evaluation
cv = 8
### robot-1
#### accuracy
- Mean = 0.9179166666666667
- Standard deviation = 0.008322910148099244
- Max = 0.93
- 75% = 0.9266666666666666
- Median = 0.9166666666666666
- 25% = 0.91
- Min = 0.9066666666666666

#### f1
- Mean = 0.7963139792599725
- Standard deviation = 0.025089053120483335
- Max = 0.8396946564885496
- 75% = 0.81651869787463
- Median = 0.7873192148760331
- 25% = 0.7763784887678693
- Min = 0.7692307692307692

#### precision
- Mean = 0.7901785366642897
- Standard deviation = 0.027997263401616075
- Max = 0.8301886792452831
- 75% = 0.7990018148820327
- Median = 0.7886762360446571
- 25% = 0.7838259062572154
- Min = 0.7352941176470589

#### recall
- Mean = 0.80625
- Standard deviation = 0.05947542676508416
- Max = 0.9166666666666666
- 75% = 0.8416666666666667
- Median = 0.8
- 25% = 0.75
- Min = 0.7333333333333333

#### facing_probas
- Mean = [0.71649776 0.49604482 0.40135426 0.29141471 0.2209028 ]
- Standard deviation = [0.02663976 0.03028047 0.03560037 0.05746092 0.04869733]
- Max = [0.76559272 0.56417081 0.46743869 0.40859912 0.33213955]
- 75% = [0.72974922 0.50176431 0.4219448  0.31593328 0.23409592]
- Median = [0.71093014 0.49225403 0.39275925 0.29029499 0.20869391]
- 25% = [0.70582338 0.47719098 0.37802541 0.2535515  0.18895434]
- Min = [0.67297118 0.45795574 0.34789505 0.20518894 0.17241167]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 227.0 | 13.0 |
| Actual Positive | 11.625 | 48.375 |

### robot-2
#### accuracy
- Mean = 0.7979166666666666
- Standard deviation = 0.023030022675725802
- Max = 0.8366666666666667
- 75% = 0.8116666666666668
- Median = 0.8016666666666667
- 25% = 0.7791666666666667
- Min = 0.76

#### f1
- Mean = 0.5387507642417414
- Standard deviation = 0.05228696321476997
- Max = 0.6258503401360546
- 75% = 0.5709825528007346
- Median = 0.5301003344481605
- 25% = 0.5113277133825079
- Min = 0.44628099173553715

#### precision
- Mean = 0.4982844991560196
- Standard deviation = 0.049126882865127855
- Max = 0.5901639344262295
- 75% = 0.5269207501512402
- Median = 0.5033333333333334
- 25% = 0.4568095838587642
- Min = 0.43023255813953487

#### recall
- Mean = 0.59375
- Standard deviation = 0.08777239347058709
- Max = 0.7666666666666667
- 75% = 0.6208333333333333
- Median = 0.6
- 25% = 0.5625
- Min = 0.45

#### facing_probas
- Mean = [0.69982499 0.7421176  0.6793113  0.52569945 0.29234412]
- Standard deviation = [0.02730337 0.02133351 0.02376045 0.03070971 0.04134038]
- Max = [0.74386027 0.77485129 0.72386624 0.59168762 0.38894814]
- 75% = [0.71811464 0.75684348 0.69168143 0.53709738 0.29970422]
- Median = [0.70133912 0.73946764 0.67793454 0.51622836 0.28534241]
- 25% = [0.67752302 0.7262182  0.65780653 0.50302423 0.26827153]
- Min = [0.65623386 0.71203056 0.65178361 0.49353507 0.24211805]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 203.75 | 36.25 |
| Actual Positive | 24.375 | 35.625 |

### robot-3
#### accuracy
- Mean = 0.7854166666666667
- Standard deviation = 0.009119195261766383
- Max = 0.8033333333333333
- 75% = 0.79
- Median = 0.7849999999999999
- 25% = 0.7808333333333333
- Min = 0.7733333333333333

#### f1
- Mean = 0.361829643014097
- Standard deviation = 0.0697005927937893
- Max = 0.4380952380952381
- 75% = 0.41631539796677414
- Median = 0.3846509477577439
- 25% = 0.32935301780286586
- Min = 0.22727272727272724

#### precision
- Mean = 0.44098802515702323
- Standard deviation = 0.045998034521348055
- Max = 0.5111111111111111
- 75% = 0.4661841480778358
- Median = 0.44917440660474717
- 25% = 0.42892156862745096
- Min = 0.35714285714285715

#### recall
- Mean = 0.3104166666666667
- Standard deviation = 0.07680128579652817
- Max = 0.38333333333333336
- 75% = 0.38333333333333336
- Median = 0.3333333333333333
- 25% = 0.26666666666666666
- Min = 0.16666666666666666

#### facing_probas
- Mean = [0.58617277 0.7189228  0.70472245 0.65031174 0.51429036]
- Standard deviation = [0.03060288 0.02477234 0.02009923 0.02301818 0.04118821]
- Max = [0.64847047 0.76619738 0.74350392 0.70261906 0.61522446]
- 75% = [0.59976213 0.73213976 0.71614798 0.65705419 0.51892866]
- Median = [0.58237532 0.7126075  0.70055164 0.64271061 0.50076003]
- 25% = [0.56521619 0.69766403 0.68766182 0.63355132 0.48793844]
- Min = [0.54340115 0.69152835 0.68307932 0.6270885  0.47775692]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 217.0 | 23.0 |
| Actual Positive | 41.375 | 18.625 |

### robot-4
#### accuracy
- Mean = 0.77375
- Standard deviation = 0.02988113024041168
- Max = 0.8233333333333334
- 75% = 0.7908333333333333
- Median = 0.77
- 25% = 0.7458333333333333
- Min = 0.74

#### f1
- Mean = 0.39941780730593945
- Standard deviation = 0.04530797639838547
- Max = 0.4814814814814815
- 75% = 0.42421287266648094
- Median = 0.3912948381452318
- 25% = 0.36381578947368415
- Min = 0.3448275862068965

#### precision
- Mean = 0.43673846597600985
- Standard deviation = 0.08390916801290893
- Max = 0.5945945945945946
- 75% = 0.4736519607843137
- Median = 0.4131944444444444
- 25% = 0.369136460554371
- Min = 0.35

#### recall
- Mean = 0.3729166666666667
- Standard deviation = 0.03326816546389858
- Max = 0.43333333333333335
- 75% = 0.3916666666666667
- Median = 0.3583333333333333
- 25% = 0.35
- Min = 0.3333333333333333

#### facing_probas
- Mean = [0.4163993  0.63167507 0.682004   0.71600433 0.66129699]
- Standard deviation = [0.03991141 0.03816657 0.02494149 0.017625   0.02530133]
- Max = [0.49572473 0.71460777 0.72357242 0.74219398 0.70792005]
- 75% = [0.4416782  0.63934263 0.69921005 0.72345526 0.67237267]
- Median = [0.40601221 0.63463958 0.68493504 0.71638677 0.66512163]
- 25% = [0.38977281 0.60847658 0.65799991 0.70643026 0.64723497]
- Min = [0.36075262 0.57280025 0.64983707 0.6832678  0.61624723]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 209.75 | 30.25 |
| Actual Positive | 37.625 | 22.375 |

### robot-5
#### accuracy
- Mean = 0.8620833333333333
- Standard deviation = 0.025327713192381876
- Max = 0.9066666666666666
- 75% = 0.88
- Median = 0.8533333333333333
- 25% = 0.8466666666666667
- Min = 0.8233333333333334

#### f1
- Mean = 0.5853377143919178
- Standard deviation = 0.09323987712540623
- Max = 0.7254901960784315
- 75% = 0.652238675194953
- Median = 0.5735752244823162
- 25% = 0.5169986263736264
- Min = 0.4421052631578947

#### precision
- Mean = 0.7250068532217964
- Standard deviation = 0.0794359011552425
- Max = 0.8809523809523809
- 75% = 0.7611596870685688
- Median = 0.7181899641577061
- 25% = 0.677304964539007
- Min = 0.6

#### recall
- Mean = 0.49583333333333335
- Standard deviation = 0.10466547239233724
- Max = 0.6666666666666666
- 75% = 0.5541666666666667
- Median = 0.5
- 25% = 0.4083333333333333
- Min = 0.35

#### facing_probas
- Mean = [0.22923098 0.45787784 0.53020312 0.73114373 0.73304834]
- Standard deviation = [0.04536354 0.05224764 0.02563003 0.0250609  0.02378163]
- Max = [0.34242169 0.58190083 0.58707799 0.76926448 0.76827784]
- 75% = [0.23147199 0.46731384 0.5371436  0.75433955 0.75558572]
- Median = [0.21686582 0.44248147 0.52927048 0.72730768 0.7273124 ]
- 25% = [0.20601771 0.4242879  0.51064687 0.7157105  0.71857299]
- Min = [0.18340722 0.40701901 0.49809478 0.69388343 0.69449066]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 228.875 | 11.125 |
| Actual Positive | 30.25 | 29.75 |

### robot-6
#### accuracy
- Mean = 0.5158333333333334
- Standard deviation = 0.03550234734023466
- Max = 0.5666666666666667
- 75% = 0.545
- Median = 0.5183333333333333
- 25% = 0.4925
- Min = 0.4533333333333333

#### f1
- Mean = 0.6798641897937006
- Standard deviation = 0.03115714008763117
- Max = 0.7234042553191489
- 75% = 0.7054971086184072
- Median = 0.6827646038172355
- 25% = 0.6599349906699572
- Min = 0.6238532110091742

#### precision
- Mean = 1.0
- Standard deviation = 0.0
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 1.0
- Min = 1.0

#### recall
- Mean = 0.5158333333333334
- Standard deviation = 0.03550234734023466
- Max = 0.5666666666666667
- 75% = 0.545
- Median = 0.5183333333333333
- 25% = 0.4925
- Min = 0.4533333333333333

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
| Actual Positive | 145.25 | 154.75 |

