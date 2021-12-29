# ExtraTreesClassifier_RandomOverSampler_2021-12-29_no3
## Constants
- CSV_PATH = ../out/csv/experiment
- OUTPUT_PATH = ../out/experiment_result/data_of_2021-12-27/AGC-0angle-under3m
- FEATURE_ATTRBS = ['low_power', 'high_power', 'hlbr', 'coe1[0]', 'coe1[1]', 'coe3[0]', 'coe3[1]', 'coe3[2]', 'coe3[3]', 'ratio_max_to_10ms_ave_peaks', 'ratio_max_to_9th_ave_peaks', 'ac_std', 'ac_auc', 'diff_std', 'diff_auc', 'srmr', 'gp_max_val_std', 'gp_max_val_range', 'gp_max_val_min', 'gp_max_val_max', 'gp_max_val_mean', 'gp_max_ix_std', 'gp_max_ix_range', 'gp_max_ix_min', 'gp_max_ix_max', 'gp_max_ix_mean', 'gp_auc_std', 'gp_auc_range', 'gp_auc_min', 'gp_auc_max', 'gp_auc_mean', 'tdoa_std', 'tdoa_range', 'tdoa_min', 'tdoa_max', 'tdoa_mean']
- LABEL_ATTRB = ['facing']
- FACING_DOV_ANGLES = [1]
- NCV = 8
- SCORING = ['accuracy', 'balanced_accuracy', 'f1']
- REFIT_SCORING = balanced_accuracy
- PARAM_GRID = [{'est__n_estimators': [50, 100, 150, 200, 300], 'est__min_samples_split': [2, 5, 10], 'est__min_samples_leaf': [1, 5, 10], 'est__max_features': ['sqrt', 'log2', None], 'est__bootstrap': [False], 'est__n_jobs': [-1], 'est__random_state': [42], 'est__max_samples': [0.01, 0.5, 0.09]}, {'est__n_estimators': [50, 100, 150, 200, 300], 'est__min_samples_split': [2, 5, 10], 'est__min_samples_leaf': [1, 5, 10], 'est__max_features': ['sqrt', 'log2', None], 'est__bootstrap': [True], 'est__oob_score': [True, False], 'est__n_jobs': [-1], 'est__random_state': [42], 'est__max_samples': [0.01, 0.5, 0.09]}]
- TRAIN_SET_SESSION = ['trial1', 'trial2']
- TEST_SET_SESSION = ['trial3', 'trial4', 'trial5']
- DISTANCE = [1, 3]
- AGC_STATUS = ['AGC']

## Loaded CSV
- 2021-12-27_raspi_48000Hz_w1_N2^12_overlap80_new.csv

## Estimator
### Type
- resampler = RandomOverSampler
- estimator = ExtraTreesClassifier

### Arguments for hyperparameter search
- resampler = RandomOverSampler
- estimator = ExtraTreesClassifier
- param_grid = 
	- {'est__n_estimators': [50, 100, 150, 200, 300], 'est__min_samples_split': [2, 5, 10], 'est__min_samples_leaf': [1, 5, 10], 'est__max_features': ['sqrt', 'log2', None], 'est__bootstrap': [False], 'est__n_jobs': [-1], 'est__random_state': [42], 'est__max_samples': [0.01, 0.5, 0.09]}
	- {'est__n_estimators': [50, 100, 150, 200, 300], 'est__min_samples_split': [2, 5, 10], 'est__min_samples_leaf': [1, 5, 10], 'est__max_features': ['sqrt', 'log2', None], 'est__bootstrap': [True], 'est__oob_score': [True, False], 'est__n_jobs': [-1], 'est__random_state': [42], 'est__max_samples': [0.01, 0.5, 0.09]}

- scoring = ['accuracy', 'balanced_accuracy', 'f1']
- refit = balanced_accuracy
- cv = 8

### Parameters of the best estimator
#### The best hyper-parameters
- best_resampler
	- sampling_strategy = auto
	- random_state = 42
	- shrinkage = None
	- n_features_in_ = 36
	- sampling_strategy_ = OrderedDict([(1, 58)])
	- shrinkage_ = None
	- sample_indices_ = [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23
 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47
 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71
 72 73 74 75 76 77 78 79 80 81 82 83 84 85 86 87 88 89 90 91 92 93 94 95
 96 97 32 97 76 54 33 32 96 54 54 11 33 10  1 55 23  1  0 55 55 88 45 77
 76 76 96 55 97 10 22 96 32 44 32 89 11 67 89 44  1 97 76 32 55 33 76 10
 67 88 11 89 33 11  1 23 45 11 89 55]

- best_estimator
	- base_estimator = ExtraTreeClassifier()
	- n_estimators = 200
	- estimator_params = ('criterion', 'max_depth', 'min_samples_split', 'min_samples_leaf', 'min_weight_fraction_leaf', 'max_features', 'max_leaf_nodes', 'min_impurity_decrease', 'min_impurity_split', 'random_state', 'ccp_alpha')
	- bootstrap = True
	- oob_score = True
	- n_jobs = -1
	- random_state = 42
	- verbose = 0
	- warm_start = False
	- class_weight = None
	- max_samples = 0.09
	- criterion = gini
	- max_depth = None
	- min_samples_split = 10
	- min_samples_leaf = 1
	- min_weight_fraction_leaf = 0.0
	- max_features = None
	- max_leaf_nodes = None
	- min_impurity_decrease = 0.0
	- min_impurity_split = None
	- ccp_alpha = 0.0
	- n_features_in_ = 36
	- n_features_ = 36
	- n_outputs_ = 1
	- classes_ = [0 1]
	- n_classes_ = 2
	- base_estimator_ = ExtraTreeClassifier()
	- oob_decision_function_ = [[0.41975431 0.58024569]
 [0.40066157 0.59933843]
 [0.44815824 0.55184176]
 [0.47384834 0.52615166]
 [0.35588003 0.64411997]
 [0.52430931 0.47569069]
 [0.89095898 0.10904102]
 [0.89865703 0.10134297]
 [0.8784977  0.1215023 ]
 [0.87590546 0.12409454]
 [0.35651203 0.64348797]
 [0.35551767 0.64448233]
 [0.39372996 0.60627004]
 [0.26809831 0.73190169]
 [0.84931638 0.15068362]
 [0.6645716  0.3354284 ]
 [0.87803922 0.12196078]
 [0.91318038 0.08681962]
 [0.80610239 0.19389761]
 [0.80321897 0.19678103]
 [0.38265057 0.61734943]
 [0.40619661 0.59380339]
 [0.39037718 0.60962282]
 [0.434233   0.565767  ]
 [0.455896   0.544104  ]
 [0.46050213 0.53949787]
 [0.70792161 0.29207839]
 [0.82498707 0.17501293]
 [0.89974506 0.10025494]
 [0.90801304 0.09198696]
 [0.76199103 0.23800897]
 [0.72522098 0.27477902]
 [0.27624391 0.72375609]
 [0.16672955 0.83327045]
 [0.35040785 0.64959215]
 [0.19425505 0.80574495]
 [0.84129133 0.15870867]
 [0.85261083 0.14738917]
 [0.8962784  0.1037216 ]
 [0.91001637 0.08998363]
 [0.87879787 0.12120213]
 [0.90173221 0.09826779]
 [0.5014168  0.4985832 ]
 [0.49633755 0.50366245]
 [0.42891027 0.57108973]
 [0.37978856 0.62021144]
 [0.40486055 0.59513945]
 [0.4588181  0.5411819 ]
 [0.78736935 0.21263065]
 [0.72694666 0.27305334]
 [0.88459067 0.11540933]
 [0.90487166 0.09512834]
 [0.68105246 0.31894754]
 [0.44207    0.55793   ]
 [0.18975662 0.81024338]
 [0.21365847 0.78634153]
 [0.36631834 0.63368166]
 [0.36621188 0.63378812]
 [0.8744326  0.1255674 ]
 [0.84288269 0.15711731]
 [0.89036978 0.10963022]
 [0.91372007 0.08627993]
 [0.7162655  0.2837345 ]
 [0.86695988 0.13304012]
 [0.41889907 0.58110093]
 [0.36500241 0.63499759]
 [0.20390638 0.79609362]
 [0.26480055 0.73519945]
 [0.50900538 0.49099462]
 [0.52947876 0.47052124]
 [0.90840608 0.09159392]
 [0.9005774  0.0994226 ]
 [0.87789054 0.12210946]
 [0.87750596 0.12249404]
 [0.28320678 0.71679322]
 [0.26230785 0.73769215]
 [0.20782926 0.79217074]
 [0.18989166 0.81010834]
 [0.41383564 0.58616436]
 [0.27339516 0.72660484]
 [0.91138516 0.08861484]
 [0.90040114 0.09959886]
 [0.90336122 0.09663878]
 [0.89462009 0.10537991]
 [0.84101347 0.15898653]
 [0.87011356 0.12988644]
 [0.39541988 0.60458012]
 [0.46709733 0.53290267]
 [0.45931564 0.54068436]
 [0.29306935 0.70693065]
 [0.91972201 0.08027799]
 [0.91722777 0.08277223]
 [0.87943529 0.12056471]
 [0.75127646 0.24872354]
 [0.50182476 0.49817524]
 [0.53825952 0.46174048]
 [0.33059777 0.66940223]
 [0.21121068 0.78878932]
 [0.26095039 0.73904961]
 [0.21505002 0.78494998]
 [0.21429434 0.78570566]
 [0.1851887  0.8148113 ]
 [0.16821577 0.83178423]
 [0.27466518 0.72533482]
 [0.34487734 0.65512266]
 [0.1849422  0.8150578 ]
 [0.19260127 0.80739873]
 [0.35774755 0.64225245]
 [0.17336912 0.82663088]
 [0.35823161 0.64176839]
 [0.38621329 0.61378671]
 [0.22142857 0.77857143]
 [0.42009    0.57991   ]
 [0.39072466 0.60927534]
 [0.40537677 0.59462323]
 [0.216555   0.783445  ]
 [0.21402402 0.78597598]
 [0.46540404 0.53459596]
 [0.3687918  0.6312082 ]
 [0.19703574 0.80296426]
 [0.21241039 0.78758961]
 [0.2090682  0.7909318 ]
 [0.32574217 0.67425783]
 [0.21895335 0.78104665]
 [0.2152543  0.7847457 ]
 [0.36902968 0.63097032]
 [0.39232097 0.60767903]
 [0.32614469 0.67385531]
 [0.27778814 0.72221186]
 [0.43189151 0.56810849]
 [0.27556477 0.72443523]
 [0.29189833 0.70810167]
 [0.35614187 0.64385813]
 [0.26720152 0.73279848]
 [0.2889579  0.7110421 ]
 [0.43972439 0.56027561]
 [0.408675   0.591325  ]
 [0.21271742 0.78728258]
 [0.21357143 0.78642857]
 [0.2718634  0.7281366 ]
 [0.2153789  0.7846211 ]
 [0.17560965 0.82439035]
 [0.21014277 0.78985723]
 [0.35931873 0.64068127]
 [0.27080961 0.72919039]
 [0.45943878 0.54056122]
 [0.35559024 0.64440976]
 [0.28181495 0.71818505]
 [0.16680534 0.83319466]
 [0.34990219 0.65009781]
 [0.41168525 0.58831475]
 [0.41990166 0.58009834]
 [0.37285867 0.62714133]
 [0.35792096 0.64207904]
 [0.2971535  0.7028465 ]
 [0.21911879 0.78088121]]
	- oob_score_ = 0.8397435897435898

#### Importance of features
- gp_max_val_min = 0.12176996560484979
- gp_auc_min = 0.11338507899366482
- gp_auc_mean = 0.08905480496161383
- coe1[0] = 0.07712189471487062
- gp_max_val_mean = 0.07647592631990398
- gp_max_val_max = 0.06411769754834087
- srmr = 0.04821866028708135
- low_power = 0.04224301485620826
- gp_auc_max = 0.041683760683760694
- diff_std = 0.03368761755485893
- coe1[1] = 0.03335568871069977
- diff_auc = 0.03123842466384839
- gp_max_val_range = 0.022986952049845064
- ratio_max_to_10ms_ave_peaks = 0.020568435188000403
- ac_std = 0.01935069145821977
- coe3[2] = 0.018600000000000002
- gp_max_val_std = 0.016960466371414514
- hlbr = 0.01582626262626263
- tdoa_max = 0.015200403425346343
- ac_auc = 0.015131013257575758
- ratio_max_to_9th_ave_peaks = 0.013682200539908049
- gp_auc_range = 0.013129249011857707
- coe3[3] = 0.012666666666666666
- high_power = 0.012346893692808164
- tdoa_range = 0.01
- gp_max_ix_std = 0.006325757575757576
- gp_max_ix_mean = 0.005553359683794466
- tdoa_std = 0.005
- gp_auc_std = 0.0022457997698504023
- gp_max_ix_max = 0.0014369501466275664
- gp_max_ix_min = 0.0006363636363636358
- coe3[0] = 0.0
- coe3[1] = 0.0
- gp_max_ix_range = 0.0
- tdoa_min = 0.0
- tdoa_mean = 0.0

## Evaluation
cv = 8
### accuracy
- Scores = [ 0.5789473684210527, 0.6842105263157895, 0.7894736842105263, 0.6842105263157895, 0.8947368421052632, 0.6111111111111112, 0.6666666666666666, 0.6666666666666666 ]
- Mean = 0.6970029239766082
- Standard deviation = 0.09429470390919088

### balanced_accuracy
- Scores = [ 0.7333333333333334, 0.8, 0.8666666666666667, 0.8, 0.9333333333333333, 0.6607142857142857, 0.6666666666666666, 0.4 ]
- Mean = 0.7325892857142857
- Standard deviation = 0.1530895650609654

### f1
- Scores = [ 0.5, 0.5714285714285715, 0.6666666666666666, 0.5714285714285715, 0.8, 0.46153846153846156, 0.4, 0.0 ]
- Mean = 0.4963827838827839
- Standard deviation = 0.22061178440071771

### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 79 | 40 |
| Actual Positive | 5 | 25 |

      