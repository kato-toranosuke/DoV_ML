# ExtraTreesClassifier_NoResampler_2022-01-16-23-32_no0
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
	- min_samples_leaf = 5
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
- gp_max_val_min = 0.16771627259611926
- gp_max_val_mean = 0.15039423043654443
- gp_auc_min = 0.13170110115028325
- gp_max_val_max = 0.09411363502036695
- gp_auc_mean = 0.0852165614007237
- gp_auc_max = 0.07040447516806476
- srmr = 0.05037839847600863
- gp_auc_range = 0.03580080912397096
- hlbr = 0.027454223576410204
- gp_max_val_range = 0.024330437782219404
- ratio_max_to_10ms_ave_peaks = 0.021467917243825952
- tdoa_std = 0.01683392738168386
- gp_max_ix_std = 0.014397685823149318
- gp_auc_std = 0.013185693408863724
- tdoa_mean = 0.012574743385610255
- gp_max_ix_range = 0.01136835451568047
- gp_max_ix_max = 0.011170471405166211
- gp_max_ix_mean = 0.010874768229426537
- gp_max_val_std = 0.008931908171327569
- tdoa_range = 0.007305347293019858
- high_power = 0.007175817225565482
- gp_max_ix_min = 0.007106496990131437
- tdoa_max = 0.004424797476007116
- tdoa_min = 0.003947118908266231
- ac_auc = 0.003914189746686168
- ac_std = 0.0022497684670345717
- ratio_max_to_9th_ave_peaks = 0.0017732463969359965
- diff_auc = 0.0012205857770543563
- coe3[2] = 0.001210217784417016
- diff_std = 0.0009745903649194151
- low_power = 0.0001950268161872266
- coe1[1] = 0.0001871824583296185
- coe1[0] = 0.0
- coe3[0] = 0.0
- coe3[1] = 0.0
- coe3[3] = 0.0

## Evaluation
cv = 8
### robot-1
#### accuracy
- Mean = 0.9558585858585859
- Standard deviation = 0.021399604366295566
- Max = 1.0
- 75% = 0.9624242424242424
- Median = 0.9545454545454546
- 25% = 0.9444444444444444
- Min = 0.9292929292929293

#### f1
- Mean = 0.8973922208622331
- Standard deviation = 0.04768517875770311
- Max = 1.0
- 75% = 0.903610771113831
- Median = 0.8918128654970761
- 25% = 0.8777777777777778
- Min = 0.8372093023255814

#### precision
- Mean = 0.8626328502415459
- Standard deviation = 0.08447424205364851
- Max = 1.0
- 75% = 0.9444444444444444
- Median = 0.8347826086956522
- 25% = 0.7956521739130435
- Min = 0.76

#### recall
- Mean = 0.9437500000000001
- Standard deviation = 0.06343057228182639
- Max = 1.0
- 75% = 1.0
- Median = 0.975
- 25% = 0.8875
- Min = 0.85

#### facing_probas
- Mean = [0.77314928 0.09581271 0.00594515 0.00105896 0.00309687]
- Standard deviation = [0.03741137 0.02225458 0.00278175 0.00142983 0.00362134]
- Max = [0.8386872  0.13330187 0.01032313 0.00465873 0.01109921]
- 75% = [0.79285813 0.1100413  0.00719161 0.00109014 0.00398243]
- Median = [7.69701814e-01 9.09047233e-02 5.84693878e-03 5.95238095e-04
 1.38095238e-03]
- 25% = [7.45325468e-01 8.04570578e-02 4.86961451e-03 1.36904762e-04
 7.22222222e-04]
- Min = [0.72612807 0.06414087 0.001      0.         0.        ]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 75.875 | 3.25 |
| Actual Positive | 1.125 | 18.875 |

### robot-2
#### accuracy
- Mean = 0.9142676767676767
- Standard deviation = 0.019465340339778668
- Max = 0.9494949494949495
- 75% = 0.9242424242424243
- Median = 0.9090909090909091
- 25% = 0.8997474747474747
- Min = 0.8888888888888888

#### f1
- Mean = 0.7277056755051095
- Standard deviation = 0.07554995416738687
- Max = 0.8571428571428571
- 75% = 0.7683823529411764
- Median = 0.718475073313783
- 25% = 0.6666666666666666
- Min = 0.6206896551724138

#### precision
- Mean = 0.9903846153846154
- Standard deviation = 0.025439916452544124
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 1.0
- Min = 0.9230769230769231

#### recall
- Mean = 0.58125
- Standard deviation = 0.09662265521087691
- Max = 0.75
- 75% = 0.625
- Median = 0.575
- 25% = 0.5
- Min = 0.45

#### facing_probas
- Mean = [0.48287571 0.6097026  0.42260584 0.00327735 0.00217751]
- Standard deviation = [0.11183806 0.0773805  0.0537344  0.00276772 0.00190885]
- Max = [0.64105867 0.73484717 0.50489407 0.0095     0.00596372]
- 75% = [0.56662653 0.64825007 0.46067056 0.00358333 0.00301644]
- Median = [0.48859175 0.61696605 0.42431661 0.00241553 0.00153543]
- 25% = [0.39826559 0.53744076 0.39212673 0.00165391 0.00083163]
- Min = [3.30700680e-01 5.06509637e-01 3.39207766e-01 1.42857143e-04
 0.00000000e+00]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 79.0 | 0.125 |
| Actual Positive | 8.375 | 11.625 |

### robot-3
#### accuracy
- Mean = 0.9470580808080808
- Standard deviation = 0.01198326783644576
- Max = 0.9696969696969697
- 75% = 0.952020202020202
- Median = 0.9444444444444444
- 25% = 0.9393939393939394
- Min = 0.93

#### f1
- Mean = 0.857647046308037
- Standard deviation = 0.03413386631629391
- Max = 0.9189189189189189
- 75% = 0.8760683760683761
- Median = 0.8569500674763832
- 25% = 0.8308823529411765
- Min = 0.8108108108108107

#### precision
- Mean = 0.9372769392844857
- Standard deviation = 0.0509656324373844
- Max = 1.0
- 75% = 1.0
- Median = 0.9161184210526316
- 25% = 0.8932748538011696
- Min = 0.8823529411764706

#### recall
- Mean = 0.79375
- Standard deviation = 0.05266343608235224
- Max = 0.85
- 75% = 0.85
- Median = 0.8
- 25% = 0.75
- Min = 0.7

#### facing_probas
- Mean = [0.04157476 0.24827778 0.67727653 0.10594979 0.00507405]
- Standard deviation = [0.02471552 0.13164071 0.03022514 0.05335163 0.00307277]
- Max = [0.09340079 0.43062734 0.72318793 0.22137443 0.01019586]
- 75% = [0.05129358 0.36116757 0.71116955 0.13485835 0.00694055]
- Median = [0.03914399 0.25843041 0.66281168 0.08992474 0.00463832]
- 25% = [0.02055952 0.11102664 0.65377742 0.06198335 0.00306732]
- Min = [1.31164966e-02 8.15688776e-02 6.43756803e-01 5.15246599e-02
 5.71428571e-04]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 78.0 | 1.125 |
| Actual Positive | 4.125 | 15.875 |

### robot-4
#### accuracy
- Mean = 0.938219696969697
- Standard deviation = 0.011712810218821092
- Max = 0.9595959595959596
- 75% = 0.9419191919191919
- Median = 0.9393939393939394
- 25% = 0.9298232323232324
- Min = 0.9191919191919192

#### f1
- Mean = 0.8214714309383427
- Standard deviation = 0.045000969119912256
- Max = 0.8888888888888888
- 75% = 0.8429487179487178
- Median = 0.8220211161387632
- 25% = 0.806344696969697
- Min = 0.7333333333333334

#### precision
- Mean = 0.9258578431372548
- Standard deviation = 0.07094805063623047
- Max = 1.0
- 75% = 1.0
- Median = 0.9372549019607843
- 25% = 0.8742647058823529
- Min = 0.8

#### recall
- Mean = 0.7523026315789473
- Standard deviation = 0.10197527587891936
- Max = 0.8947368421052632
- 75% = 0.8421052631578947
- Median = 0.763157894736842
- 25% = 0.6756578947368421
- Min = 0.5789473684210527

#### facing_probas
- Mean = [1.89536341e-04 9.87170307e-04 7.98317978e-02 6.01896244e-01
 9.81065417e-02]
- Standard deviation = [0.00034645 0.00105515 0.08589069 0.05906714 0.07372741]
- Max = [0.00106516 0.00282373 0.21996778 0.701004   0.24446503]
- 75% = [1.87969925e-04 1.86448264e-03 1.34365134e-01 6.50625719e-01
 1.23446936e-01]
- Median = [0.00000000e+00 3.86382623e-04 3.28284998e-02 5.84927646e-01
 1.07690981e-01]
- 25% = [0.00000000e+00 1.38471178e-04 1.17327023e-02 5.61158495e-01
 2.05659014e-02]
- Min = [0.         0.         0.0070981  0.5245259  0.01843478]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 78.625 | 1.375 |
| Actual Positive | 4.75 | 14.375 |

### robot-5
#### accuracy
- Mean = 0.9483080808080808
- Standard deviation = 0.009294267305958922
- Max = 0.9696969696969697
- 75% = 0.9494949494949495
- Median = 0.9494949494949495
- 25% = 0.9398484848484848
- Min = 0.9393939393939394

#### f1
- Mean = 0.852259822848058
- Standard deviation = 0.029612330091821987
- Max = 0.9189189189189189
- 75% = 0.8571428571428571
- Median = 0.8571428571428571
- 25% = 0.8235294117647058
- Min = 0.8235294117647058

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
- Standard deviation = 0.0463512405443479
- Max = 0.85
- 75% = 0.75
- Median = 0.75
- 25% = 0.7
- Min = 0.7

#### facing_probas
- Mean = [3.79301304e-03 2.62719671e-04 1.76354521e-02 3.51669752e-01
 5.74263731e-01]
- Standard deviation = [0.00274862 0.0002915  0.01427267 0.08794371 0.03663821]
- Max = [0.00961451 0.00088294 0.04270181 0.47318991 0.64282001]
- 75% = [5.54336735e-03 4.26020408e-04 2.64476332e-02 4.21031205e-01
 5.94926214e-01]
- Median = [2.65334467e-03 1.82539683e-04 1.65348639e-02 3.65953373e-01
 5.75958192e-01]
- 25% = [0.00160034 0.         0.00534396 0.25256186 0.54480201]
- Min = [1.28571429e-03 0.00000000e+00 4.48979592e-04 2.43985261e-01
 5.24811508e-01]

#### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 79.125 | 0.0 |
| Actual Positive | 5.125 | 14.875 |

### robot-6
#### accuracy
- Mean = 0.7630176767676767
- Standard deviation = 0.057299764641814604
- Max = 0.8282828282828283
- 75% = 0.8106060606060606
- Median = 0.7878787878787878
- 25% = 0.6952272727272728
- Min = 0.6868686868686869

#### f1
- Mean = 0.8643675527948416
- Standard deviation = 0.03735259039088544
- Max = 0.9060773480662984
- 75% = 0.895391061452514
- Median = 0.8813202247191012
- 25% = 0.8202134404057482
- Min = 0.8143712574850299

#### precision
- Mean = 1.0
- Standard deviation = 0.0
- Max = 1.0
- 75% = 1.0
- Median = 1.0
- 25% = 1.0
- Min = 1.0

#### recall
- Mean = 0.7630176767676767
- Standard deviation = 0.057299764641814604
- Max = 0.8282828282828283
- 75% = 0.8106060606060606
- Median = 0.7878787878787878
- 25% = 0.6952272727272728
- Min = 0.6868686868686869

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
| Actual Positive | 23.5 | 75.625 |

