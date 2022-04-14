# ExtraTreesClassifier_RandomUnderSampler_2022-04-13-04-08_no2
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
	- sampling_strategy_ = OrderedDict([(0, 15)])
	- sample_indices_ = [ 3  8 45 57 16 66 42 60 15 69 58 62 40  6 64  0  1  2 18 19 20 36 37 38
 54 55 56 72 73 74]

- best_estimator
	- base_estimator = ExtraTreeClassifier()
	- n_estimators = 330
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
	- min_samples_split = 5
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
	- oob_decision_function_ = [[0.34935119 0.65064881]
 [0.57727487 0.42272513]
 [0.84192831 0.15807169]
 [0.38834154 0.61165846]
 [0.79608427 0.20391573]
 [0.77202932 0.22797068]
 [0.4531203  0.5468797 ]
 [0.8387728  0.1612272 ]
 [0.66999089 0.33000911]
 [0.58657188 0.41342812]
 [0.29150165 0.70849835]
 [0.82507974 0.17492026]
 [0.1841854  0.8158146 ]
 [0.70293436 0.29706564]
 [0.75884354 0.24115646]
 [0.50539322 0.49460678]
 [0.30969048 0.69030952]
 [0.53503909 0.46496091]
 [0.2916372  0.7083628 ]
 [0.31217904 0.68782096]
 [0.26377076 0.73622924]
 [0.32050333 0.67949667]
 [0.44516614 0.55483386]
 [0.40070208 0.59929792]
 [0.587125   0.412875  ]
 [0.52012531 0.47987469]
 [0.47826918 0.52173082]
 [0.27063095 0.72936905]
 [0.26152482 0.73847518]
 [0.29423307 0.70576693]]
	- oob_score_ = 0.7

#### Importance of features
- gp_auc_min = 0.07065102766613285
- gp_max_val_min = 0.06535377249932017
- gp_max_val_mean = 0.05823328574983757
- gp_auc_max = 0.05731129775994521
- gp_auc_mean = 0.05681322812349693
- gp_max_val_max = 0.04788558286807207
- diff_std = 0.04722053314404946
- hlbr = 0.04115711707332407
- high_power = 0.03742589081588575
- ratio_max_to_10ms_ave_peaks = 0.031191221416323033
- tdoa_min = 0.031030883670453886
- gp_max_ix_min = 0.02675093664828024
- gp_max_ix_mean = 0.026107398424196064
- gp_max_val_range = 0.025891635203930573
- ratio_max_to_9th_ave_peaks = 0.02550373334333143
- gp_auc_std = 0.02532231064993741
- coe3[2] = 0.024670517618410926
- gp_max_ix_std = 0.023999732262369743
- ac_auc = 0.023525722084065188
- gp_max_val_std = 0.02273126756713643
- srmr = 0.02271876409157768
- tdoa_mean = 0.022587852779065772
- tdoa_range = 0.021739139931354144
- gp_auc_range = 0.020354821545193434
- low_power = 0.019714649970203606
- ac_std = 0.019609579417872215
- diff_auc = 0.016732254959952206
- coe3[3] = 0.016634206784413547
- tdoa_max = 0.014547785362241541
- coe1[1] = 0.013966879161823006
- gp_max_ix_max = 0.013154479268248366
- coe1[0] = 0.011900939187863743
- gp_max_ix_range = 0.010975254634471632
- tdoa_std = 0.0065862983172201035
- coe3[0] = 0.0
- coe3[1] = 0.0

## Evaluation
cv = 8
### robot-1
#### accuracy
- Mean = 0.9275
- Standard deviation = 0.02537222891273052
- Max = 0.96
- 75% = 0.95
- Median = 0.9299999999999999
- 25% = 0.91
- Min = 0.88

#### f1
- Mean = 0.8170768162043905
- Standard deviation = 0.0515646867749163
- Max = 0.8947368421052632
- 75% = 0.8571428571428571
- Median = 0.8250000000000001
- 25% = 0.7692307692307692
- Min = 0.7391304347826088

#### precision
- Mean = 0.8534047458389564
- Standard deviation = 0.11298795062950161
- Max = 1.0
- 75% = 0.9583333333333333
- Median = 0.825
- 25% = 0.7894736842105263
- Min = 0.6538461538461539

#### recall
- Mean = 0.7937500000000001
- Standard deviation = 0.04635124054434789
- Max = 0.85
- 75% = 0.85
- Median = 0.775
- 25% = 0.75
- Min = 0.75

#### facing_probas
- Mean = [0.56875359 0.28020161 0.23206418 0.138832   0.13295582]
- Standard deviation = [0.03950077 0.04506599 0.02434301 0.02624112 0.01642411]
- Max = [0.64162121 0.35043939 0.28068254 0.1995184  0.16935317]
- 75% = [0.59059352 0.30635714 0.241193   0.14147939 0.13996792]
- Median = [0.56853048 0.26749531 0.22820851 0.1376324  0.12917136]
- 25% = [0.53908586 0.25104942 0.21293724 0.11772394 0.11938402]
- Min = [0.5075172  0.21593326 0.20418831 0.11340765 0.11649531]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 76.875 | 3.125 |
| Actual Positive | 4.125 | 15.875 |

### robot-2
#### accuracy
- Mean = 0.86375
- Standard deviation = 0.02057759704144293
- Max = 0.91
- 75% = 0.865
- Median = 0.86
- 25% = 0.85
- Min = 0.84

#### f1
- Mean = 0.6937314850516989
- Standard deviation = 0.060360602781879845
- Max = 0.8085106382978724
- 75% = 0.7140468227424749
- Median = 0.6737588652482269
- 25% = 0.6627906976744186
- Min = 0.6111111111111112

#### precision
- Mean = 0.6300835964558791
- Standard deviation = 0.042280812696282075
- Max = 0.7037037037037037
- 75% = 0.6491477272727273
- Median = 0.6201923076923077
- 25% = 0.604669887278583
- Min = 0.5714285714285714

#### recall
- Mean = 0.7875000000000001
- Standard deviation = 0.13404756618454508
- Max = 1.0
- 75% = 0.8375
- Median = 0.8
- 25% = 0.7
- Min = 0.55

#### facing_probas
- Mean = [0.59853552 0.67960365 0.53688474 0.28848116 0.19441229]
- Standard deviation = [0.05703171 0.02109776 0.04727092 0.04687947 0.02943482]
- Max = [0.71398593 0.71735804 0.62457035 0.37605339 0.26177561]
- 75% = [0.61940954 0.68747529 0.5547399  0.31506457 0.20514561]
- Median = [0.60558405 0.68129798 0.52157756 0.28521699 0.18568642]
- 25% = [0.55124324 0.65894625 0.51395969 0.25122891 0.17556566]
- Min = [0.51659692 0.65489827 0.46844949 0.22415079 0.16106926]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 70.625 | 9.375 |
| Actual Positive | 4.25 | 15.75 |

### robot-3
#### accuracy
- Mean = 0.78125
- Standard deviation = 0.045672064766112776
- Max = 0.83
- 75% = 0.82
- Median = 0.795
- 25% = 0.7575000000000001
- Min = 0.7

#### f1
- Mean = 0.3793152257186784
- Standard deviation = 0.07878077991246515
- Max = 0.5128205128205129
- 75% = 0.4111253196930946
- Median = 0.3796296296296296
- 25% = 0.33406593406593404
- Min = 0.25

#### precision
- Mean = 0.4890438235010603
- Standard deviation = 0.14941774214518228
- Max = 0.7142857142857143
- 75% = 0.5952380952380952
- Median = 0.4819078947368421
- 25% = 0.38653846153846155
- Min = 0.25

#### recall
- Mean = 0.3375
- Standard deviation = 0.09921567416492215
- Max = 0.5
- 75% = 0.41250000000000003
- Median = 0.32499999999999996
- 25% = 0.25
- Min = 0.2

#### facing_probas
- Mean = [0.3970946  0.60093466 0.59769877 0.47780816 0.24991042]
- Standard deviation = [0.0351403  0.03092444 0.02869538 0.04100728 0.03172598]
- Max = [0.45002579 0.65226569 0.64069877 0.53857107 0.2984899 ]
- 75% = [0.42469363 0.61944214 0.6225974  0.50264421 0.27011476]
- Median = [0.39776876 0.60568939 0.58746122 0.47269724 0.24836923]
- 25% = [0.36850956 0.58232404 0.57254798 0.46098722 0.23177967]
- Min = [0.34926094 0.54664683 0.56693218 0.41230592 0.19216017]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 71.375 | 8.625 |
| Actual Positive | 13.25 | 6.75 |

### robot-4
#### accuracy
- Mean = 0.86375
- Standard deviation = 0.02394655507583504
- Max = 0.9
- 75% = 0.8825000000000001
- Median = 0.86
- 25% = 0.85
- Min = 0.82

#### f1
- Mean = 0.5152319902319902
- Standard deviation = 0.16437190135184115
- Max = 0.7555555555555556
- 75% = 0.6160714285714286
- Median = 0.49743589743589745
- 25% = 0.4
- Min = 0.24999999999999997

#### precision
- Mean = 0.8725
- Standard deviation = 0.13102957681378657
- Max = 1.0
- 75% = 1.0
- Median = 0.9
- 25% = 0.75
- Min = 0.68

#### recall
- Mean = 0.41875
- Standard deviation = 0.23443749166888814
- Max = 0.85
- 75% = 0.48750000000000004
- Median = 0.35
- 25% = 0.25
- Min = 0.15

#### facing_probas
- Mean = [0.21468064 0.41073369 0.57635278 0.58484585 0.47880258]
- Standard deviation = [0.03243254 0.03446874 0.03884853 0.04424307 0.03772262]
- Max = [0.27794877 0.45096429 0.6394026  0.64249603 0.53491649]
- 75% = [0.23696726 0.43661797 0.60887139 0.63148904 0.50513424]
- Median = [0.20275685 0.41932197 0.56652922 0.57746032 0.48356638]
- 25% = [0.19460097 0.39510519 0.54406133 0.54915458 0.45763916]
- Min = [0.1734329  0.34954978 0.52386123 0.51692641 0.40590981]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 78.0 | 2.0 |
| Actual Positive | 11.625 | 8.375 |

### robot-5
#### accuracy
- Mean = 0.9550000000000001
- Standard deviation = 0.020615528128088288
- Max = 0.98
- 75% = 0.9724999999999999
- Median = 0.955
- 25% = 0.9375
- Min = 0.93

#### f1
- Mean = 0.8849663209363332
- Standard deviation = 0.05661197424809388
- Max = 0.9523809523809523
- 75% = 0.934516523867809
- Median = 0.8912776412776412
- 25% = 0.8408812729498165
- Min = 0.787878787878788

#### precision
- Mean = 0.9052275472112428
- Standard deviation = 0.08398704428324798
- Max = 1.0
- 75% = 1.0
- Median = 0.898989898989899
- 25% = 0.8500905797101449
- Min = 0.782608695652174

#### recall
- Mean = 0.8812500000000001
- Standard deviation = 0.10879309490955755
- Max = 1.0
- 75% = 0.9624999999999999
- Median = 0.9
- 25% = 0.8375
- Min = 0.65

#### facing_probas
- Mean = [0.15609948 0.26279409 0.55176113 0.62147268 0.73450882]
- Standard deviation = [0.03292726 0.04306705 0.03103047 0.05337727 0.01679492]
- Max = [0.22639141 0.35087374 0.59480483 0.69730808 0.75857035]
- 75% = [0.16965909 0.29002119 0.58136337 0.67138424 0.75084853]
- Median = [0.14941053 0.24817051 0.54964006 0.61775307 0.73075325]
- 25% = [0.13327814 0.23566238 0.52209076 0.57580619 0.71983892]
- Min = [0.11700758 0.20643903 0.5101443  0.54283189 0.71410534]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 77.875 | 2.125 |
| Actual Positive | 2.375 | 17.625 |

### robot-6
#### accuracy
- Mean = 0.6437499999999999
- Standard deviation = 0.036033838263498943
- Max = 0.7
- 75% = 0.68
- Median = 0.635
- 25% = 0.615
- Min = 0.6

#### f1
- Mean = 0.7826878836781413
- Standard deviation = 0.026555833739704018
- Max = 0.8235294117647058
- 75% = 0.8095238095238095
- Median = 0.776746969923687
- 25% = 0.761574074074074
- Min = 0.7499999999999999

#### precision
- Mean = 1.0
- Standard deviation = 0.0
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 1.0
- Min = 1.0

#### recall
- Mean = 0.6437499999999999
- Standard deviation = 0.036033838263498943
- Max = 0.7
- 75% = 0.68
- Median = 0.635
- 25% = 0.615
- Min = 0.6

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
| Actual Positive | 35.625 | 64.375 |

