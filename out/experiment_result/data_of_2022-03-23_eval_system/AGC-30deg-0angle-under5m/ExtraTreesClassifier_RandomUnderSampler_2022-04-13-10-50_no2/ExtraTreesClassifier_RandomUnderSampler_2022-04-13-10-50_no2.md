# ExtraTreesClassifier_RandomUnderSampler_2022-04-13-10-50_no2
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
- resampler = RandomUnderSampler
- estimator = ExtraTreesClassifier

### Arguments for hyperparameter search
- resampler = RandomUnderSampler
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
	- replacement = False
	- n_features_in_ = 36
	- sampling_strategy_ = OrderedDict([(0, 45)])
	- sample_indices_ = [ 25  54 189  99 181  21  33  86 140 148 117 198  87 178  57  22  66 155
 120  71 121 150 179  39  12 214  75  24 184 215 136  70 173 156  84  38
 147  83  85  40  18  53 154 124 200   0   1   2  15  16  17  30  31  32
  48  49  50  63  64  65  78  79  80  96  97  98 111 112 113 126 127 128
 144 145 146 159 160 161 174 175 176 192 193 194 207 208 209 222 223 224]

- best_estimator
	- base_estimator = ExtraTreeClassifier()
	- n_estimators = 10
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
- gp_max_val_mean = 0.25558073201370896
- gp_max_val_min = 0.22934469375946193
- diff_std = 0.09005929377099657
- gp_auc_max = 0.05181230680518819
- diff_auc = 0.05121263672151882
- gp_max_val_max = 0.04768507107256238
- gp_auc_mean = 0.0460291818265601
- coe1[1] = 0.033816411379791925
- high_power = 0.028739227489401508
- ratio_max_to_9th_ave_peaks = 0.028534435673223835
- ratio_max_to_10ms_ave_peaks = 0.02517459358382631
- srmr = 0.02482417108007409
- coe1[0] = 0.019926775325467987
- gp_auc_min = 0.015873064134329828
- low_power = 0.013873910635693256
- tdoa_min = 0.01385191947340604
- gp_auc_range = 0.007359426818127697
- gp_max_val_range = 0.006381859048584518
- coe3[3] = 0.004670891705896667
- ac_auc = 0.0029688880164883647
- tdoa_max = 0.0021645239715030722
- coe3[2] = 0.00011598569418802038
- hlbr = 0.0
- coe3[0] = 0.0
- coe3[1] = 0.0
- ac_std = 0.0
- gp_max_val_std = 0.0
- gp_max_ix_std = 0.0
- gp_max_ix_range = 0.0
- gp_max_ix_min = 0.0
- gp_max_ix_max = 0.0
- gp_max_ix_mean = 0.0
- gp_auc_std = 0.0
- tdoa_std = 0.0
- tdoa_range = 0.0
- tdoa_mean = 0.0

## Evaluation
cv = 8
### robot-1
#### accuracy
- Mean = 0.8841666666666665
- Standard deviation = 0.008457409637576853
- Max = 0.9
- 75% = 0.8858333333333333
- Median = 0.8833333333333333
- 25% = 0.88
- Min = 0.87

#### f1
- Mean = 0.7195409261003264
- Standard deviation = 0.029160023801510643
- Max = 0.7656250000000001
- 75% = 0.7364507250979146
- Median = 0.7186813186813186
- 25% = 0.7038303693570451
- Min = 0.6666666666666666

#### precision
- Mean = 0.7024433529213573
- Standard deviation = 0.04740925171104584
- Max = 0.7777777777777778
- 75% = 0.7327488687782806
- Median = 0.6916464891041162
- 25% = 0.6602018685352019
- Min = 0.6521739130434783

#### recall
- Mean = 0.75
- Standard deviation = 0.09013878188659971
- Max = 0.8833333333333333
- 75% = 0.8166666666666667
- Median = 0.7666666666666666
- 25% = 0.6916666666666667
- Min = 0.5833333333333334

#### facing_probas
- Mean = [0.6607842  0.40439872 0.33517812 0.19363725 0.08450388]
- Standard deviation = [0.02010928 0.03237871 0.022078   0.02583176 0.02021349]
- Max = [0.68361068 0.43932106 0.36269929 0.22789878 0.12323264]
- 75% = [0.67722099 0.42818286 0.34821232 0.2179931  0.0975801 ]
- Median = [0.66409742 0.41498678 0.33903376 0.19303659 0.07559416]
- 25% = [0.65054984 0.39148584 0.32652345 0.17245516 0.07006346]
- Min = [0.62121783 0.33547218 0.29233413 0.1533996  0.06052754]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 220.25 | 19.75 |
| Actual Positive | 15.0 | 45.0 |

### robot-2
#### accuracy
- Mean = 0.8079166666666666
- Standard deviation = 0.0202029632040011
- Max = 0.8333333333333334
- 75% = 0.8225
- Median = 0.8133333333333334
- 25% = 0.7933333333333333
- Min = 0.7733333333333333

#### f1
- Mean = 0.3909729948806408
- Standard deviation = 0.06974443635916942
- Max = 0.46808510638297873
- 75% = 0.43546195652173914
- Median = 0.4070567986230637
- 25% = 0.37727272727272726
- Min = 0.2278481012658228

#### precision
- Mean = 0.5497917682779373
- Standard deviation = 0.08947591440589661
- Max = 0.6956521739130435
- 75% = 0.599264705882353
- Median = 0.5620300751879699
- 25% = 0.4688995215311005
- Min = 0.42

#### recall
- Mean = 0.3145833333333333
- Standard deviation = 0.07792335087193768
- Max = 0.4166666666666667
- 75% = 0.35416666666666663
- Median = 0.35
- 25% = 0.26666666666666666
- Min = 0.15

#### facing_probas
- Mean = [0.60069536 0.61459389 0.57523813 0.38371028 0.23291628]
- Standard deviation = [0.02968438 0.02222416 0.02405581 0.03418356 0.0208901 ]
- Max = [0.63256462 0.66092801 0.61422272 0.43694502 0.26979898]
- 75% = [0.62395009 0.61907816 0.59264394 0.40573405 0.24238048]
- Median = [0.60802714 0.60821757 0.5667329  0.38904685 0.23531567]
- 25% = [0.58866826 0.59816558 0.55515245 0.36003339 0.22049856]
- Min = [0.54090739 0.59200964 0.54849182 0.32800121 0.19538052]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 223.5 | 16.5 |
| Actual Positive | 41.125 | 18.875 |

### robot-3
#### accuracy
- Mean = 0.745
- Standard deviation = 0.02449489742783178
- Max = 0.78
- 75% = 0.7608333333333334
- Median = 0.7466666666666666
- 25% = 0.7308333333333333
- Min = 0.7066666666666667

#### f1
- Mean = 0.36217947073521073
- Standard deviation = 0.05517795133418302
- Max = 0.44067796610169496
- 75% = 0.3988223984619082
- Median = 0.38494397759103643
- 25% = 0.31061259706643657
- Min = 0.27522935779816515

#### precision
- Mean = 0.3642941618858086
- Standard deviation = 0.05293144255378633
- Max = 0.4482758620689655
- 75% = 0.3988543628374137
- Median = 0.36027131782945737
- 25% = 0.32653061224489793
- Min = 0.2903225806451613

#### recall
- Mean = 0.36458333333333337
- Standard deviation = 0.07189764136140583
- Max = 0.48333333333333334
- 75% = 0.39583333333333337
- Median = 0.38333333333333336
- 25% = 0.3
- Min = 0.25

#### facing_probas
- Mean = [0.45641132 0.57830449 0.59573015 0.52559126 0.39502741]
- Standard deviation = [0.03404381 0.02820461 0.02182844 0.03069402 0.03431841]
- Max = [0.49689913 0.62926436 0.62870387 0.5680093  0.43765488]
- 75% = [0.47815496 0.59487645 0.61483483 0.54567879 0.4222711 ]
- Median = [0.46746714 0.56815819 0.58906369 0.52921875 0.40746845]
- 25% = [0.44485425 0.5565553  0.57701272 0.51261758 0.3653654 ]
- Min = [0.38115967 0.54754651 0.57195281 0.4658802  0.34309448]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 201.625 | 38.375 |
| Actual Positive | 38.125 | 21.875 |

### robot-4
#### accuracy
- Mean = 0.77
- Standard deviation = 0.023452078799117145
- Max = 0.8033333333333333
- 75% = 0.7841666666666667
- Median = 0.7716666666666667
- 25% = 0.7558333333333334
- Min = 0.7266666666666667

#### f1
- Mean = 0.25995582738637857
- Standard deviation = 0.057380893730554314
- Max = 0.3529411764705882
- 75% = 0.30435663627152987
- Median = 0.24237175216522316
- 25% = 0.22883702531645567
- Min = 0.163265306122449

#### precision
- Mean = 0.38106018723278784
- Standard deviation = 0.09495448933293955
- Max = 0.5263157894736842
- 75% = 0.4398496240601504
- Median = 0.39477124183006534
- 25% = 0.3121031746031746
- Min = 0.21052631578947367

#### recall
- Mean = 0.20416666666666666
- Standard deviation = 0.05758447900452189
- Max = 0.3
- 75% = 0.24583333333333335
- Median = 0.18333333333333332
- 25% = 0.16249999999999998
- Min = 0.13333333333333333

#### facing_probas
- Mean = [0.33088882 0.45777272 0.56747671 0.58360186 0.54580928]
- Standard deviation = [0.0312142  0.02521557 0.02311197 0.01482809 0.02103073]
- Max = [0.38219553 0.50034448 0.61376961 0.61501194 0.56662616]
- 75% = [0.35263385 0.47269931 0.57601507 0.58863847 0.56324507]
- Median = [0.32925684 0.4580754  0.56886011 0.58418847 0.55309987]
- 25% = [0.315054   0.4446331  0.55497053 0.57010084 0.53181444]
- Min = [0.27227346 0.41404844 0.53086931 0.56759241 0.50254954]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 218.75 | 21.25 |
| Actual Positive | 47.75 | 12.25 |

### robot-5
#### accuracy
- Mean = 0.8620833333333333
- Standard deviation = 0.025654623798103557
- Max = 0.9066666666666666
- 75% = 0.8741666666666666
- Median = 0.8566666666666667
- 25% = 0.8533333333333334
- Min = 0.8133333333333334

#### f1
- Mean = 0.6332347170303867
- Standard deviation = 0.07953033909281039
- Max = 0.7741935483870969
- 75% = 0.6766335227272727
- Median = 0.6242389336843838
- 25% = 0.6067527308838133
- Min = 0.4814814814814815

#### precision
- Mean = 0.6735247350579916
- Standard deviation = 0.07010007026535701
- Max = 0.76
- 75% = 0.7456395348837209
- Median = 0.6610305958132046
- 25% = 0.6365365111561867
- Min = 0.5416666666666666

#### recall
- Mean = 0.6041666666666667
- Standard deviation = 0.10857345183996153
- Max = 0.8
- 75% = 0.6541666666666667
- Median = 0.6000000000000001
- 25% = 0.5291666666666667
- Min = 0.43333333333333335

#### facing_probas
- Mean = [0.13525507 0.32426693 0.47036927 0.57804418 0.66073043]
- Standard deviation = [0.02665859 0.01960737 0.02788492 0.02063773 0.01354254]
- Max = [0.17216754 0.34401013 0.4974107  0.60892403 0.67885656]
- 75% = [0.1639511  0.34127184 0.4918038  0.59273422 0.67575828]
- Median = [0.12567905 0.33093763 0.47461853 0.57964182 0.65717108]
- 25% = [0.11385425 0.30980859 0.46388684 0.56611976 0.65159691]
- Min = [0.1004163  0.28695135 0.40507297 0.54204087 0.64068405]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 222.375 | 17.625 |
| Actual Positive | 23.75 | 36.25 |

### robot-6
#### accuracy
- Mean = 0.4475
- Standard deviation = 0.03290347837066605
- Max = 0.48333333333333334
- 75% = 0.47333333333333333
- Median = 0.46499999999999997
- 25% = 0.41583333333333333
- Min = 0.39

#### f1
- Mean = 0.6175832924682492
- Standard deviation = 0.03185931767179871
- Max = 0.6516853932584269
- 75% = 0.6425339366515836
- Median = 0.6348105197763512
- 25% = 0.5874028856825749
- Min = 0.5611510791366906

#### precision
- Mean = 1.0
- Standard deviation = 0.0
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 1.0
- Min = 1.0

#### recall
- Mean = 0.4475
- Standard deviation = 0.03290347837066605
- Max = 0.48333333333333334
- 75% = 0.47333333333333333
- Median = 0.46499999999999997
- 25% = 0.41583333333333333
- Min = 0.39

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
| Actual Positive | 165.75 | 134.25 |

