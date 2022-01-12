# ExtraTreesClassifier_RandomUnderSampler_2022-01-10_no2
## Constants
- CSV_PATH = ../out/csv/experiment
- OUTPUT_PATH = ../out/experiment_result/data_of_2022-01-10/NoAGC-0angle-under5m
- FEATURE_ATTRBS = ['low_power', 'high_power', 'hlbr', 'coe1[0]', 'coe1[1]', 'coe3[0]', 'coe3[1]', 'coe3[2]', 'coe3[3]', 'ratio_max_to_10ms_ave_peaks', 'ratio_max_to_9th_ave_peaks', 'ac_std', 'ac_auc', 'diff_std', 'diff_auc', 'srmr', 'gp_max_val_std', 'gp_max_val_range', 'gp_max_val_min', 'gp_max_val_max', 'gp_max_val_mean', 'gp_max_ix_std', 'gp_max_ix_range', 'gp_max_ix_min', 'gp_max_ix_max', 'gp_max_ix_mean', 'gp_auc_std', 'gp_auc_range', 'gp_auc_min', 'gp_auc_max', 'gp_auc_mean', 'tdoa_std', 'tdoa_range', 'tdoa_min', 'tdoa_max', 'tdoa_mean']
- LABEL_ATTRB = ['facing']
- FACING_DOV_ANGLES = [1]
- NCV = 8
- SCORING = ['accuracy', 'balanced_accuracy', 'f1']
- REFIT_SCORING = balanced_accuracy
- PARAM_GRID = [{'est__n_estimators': [50, 100, 150, 200, 300], 'est__min_samples_split': [2, 5, 10], 'est__min_samples_leaf': [1, 5, 10], 'est__max_features': ['sqrt', 'log2', None], 'est__bootstrap': [False], 'est__n_jobs': [-1], 'est__random_state': [42], 'est__max_samples': [0.01, 0.5, 0.09]}, {'est__n_estimators': [50, 100, 150, 200, 300], 'est__min_samples_split': [2, 5, 10], 'est__min_samples_leaf': [1, 5, 10], 'est__max_features': ['sqrt', 'log2', None], 'est__bootstrap': [True], 'est__oob_score': [True, False], 'est__n_jobs': [-1], 'est__random_state': [42], 'est__max_samples': [0.01, 0.5, 0.09]}]
- TRAIN_SET_SESSION = ['trial1', 'trial2']
- TEST_SET_SESSION = ['trial3', 'trial4', 'trial5']
- DISTANCE = [1, 3, 5]
- AGC_STATUS = ['NoAGC']

## Loaded CSV
- 2022-01-10_raspi_48000Hz_w1_N2^12_overlap80.csv

## Estimator
### Type
- resampler = RandomUnderSampler
- estimator = ExtraTreesClassifier

### Arguments for hyperparameter search
- resampler = RandomUnderSampler
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
	- replacement = False
	- n_features_in_ = 36
	- sampling_strategy_ = OrderedDict([(0, 30)])
	- sample_indices_ = [ 56  59   6  69  34  80  91  14  50 133  24  78  15  46 111 113 135   2
 110 130  81  57  39  88  54  16  19 142  94 121   0   1  10  11  20  21
  32  33  42  43  52  53  64  65  74  75  84  85  96  97 106 107 116 117
 128 129 138 139 148 149]

- best_estimator
	- base_estimator = ExtraTreeClassifier()
	- n_estimators = 200
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
	- max_features = log2
	- max_leaf_nodes = None
	- min_impurity_decrease = 0.0
	- ccp_alpha = 0.0
	- n_features_in_ = 36
	- n_outputs_ = 1
	- classes_ = [0 1]
	- n_classes_ = 2
	- base_estimator_ = ExtraTreeClassifier()
	- oob_decision_function_ = [[0.93031609 0.06968391]
 [0.98269231 0.01730769]
 [0.92652778 0.07347222]
 [0.29580153 0.70419847]
 [0.20487805 0.79512195]
 [0.98010336 0.01989664]
 [0.91268437 0.08731563]
 [0.5957529  0.4042471 ]
 [0.72410714 0.27589286]
 [0.95419847 0.04580153]
 [0.75333333 0.24666667]
 [0.6327753  0.3672247 ]
 [0.46858974 0.53141026]
 [0.73042328 0.26957672]
 [0.95368852 0.04631148]
 [0.92286822 0.07713178]
 [0.69968516 0.30031484]
 [0.12016129 0.87983871]
 [0.95737705 0.04262295]
 [0.90620155 0.09379845]
 [0.94013333 0.05986667]
 [0.90647482 0.09352518]
 [0.76196581 0.23803419]
 [0.67886905 0.32113095]
 [0.4308908  0.5691092 ]
 [0.96440678 0.03559322]
 [0.97850877 0.02149123]
 [0.97859195 0.02140805]
 [0.15833333 0.84166667]
 [0.92484848 0.07515152]
 [0.25270655 0.74729345]
 [0.25891473 0.74108527]
 [0.08817664 0.91182336]
 [0.12245763 0.87754237]
 [0.47126437 0.52873563]
 [0.27550742 0.72449258]
 [0.37747748 0.62252252]
 [0.35319444 0.64680556]
 [0.19430199 0.80569801]
 [0.25056497 0.74943503]
 [0.36333333 0.63666667]
 [0.30673531 0.69326469]
 [0.28913309 0.71086691]
 [0.26567797 0.73432203]
 [0.10698279 0.89301721]
 [0.10632111 0.89367889]
 [0.36602891 0.63397109]
 [0.34144144 0.65855856]
 [0.41145038 0.58854962]
 [0.40664266 0.59335734]
 [0.13151261 0.86848739]
 [0.13747499 0.86252501]
 [0.26251044 0.73748956]
 [0.25618622 0.74381378]
 [0.21417411 0.78582589]
 [0.22114512 0.77885488]
 [0.11198347 0.88801653]
 [0.13178295 0.86821705]
 [0.24931694 0.75068306]
 [0.43202899 0.56797101]]
	- oob_score_ = 0.9

#### Importance of features
- gp_auc_min = 0.10462980490306463
- gp_max_val_min = 0.10443936646452584
- gp_max_val_mean = 0.09230212723680901
- gp_max_val_max = 0.0837414598896145
- gp_auc_max = 0.08229713637546432
- gp_auc_mean = 0.05848861467797992
- hlbr = 0.04717900173081456
- srmr = 0.039992257977266465
- gp_auc_std = 0.0340904819236581
- gp_max_val_std = 0.03297302785995219
- gp_max_val_range = 0.02221742990459129
- high_power = 0.021706869618492608
- tdoa_mean = 0.020701807266413137
- ratio_max_to_10ms_ave_peaks = 0.02049977119780203
- gp_max_ix_mean = 0.01889007333765724
- gp_auc_range = 0.01873029894282927
- gp_max_ix_min = 0.01776775964606739
- gp_max_ix_std = 0.01654349948081295
- tdoa_min = 0.015975846316953705
- gp_max_ix_range = 0.015555451020641804
- tdoa_range = 0.015544298586888152
- tdoa_std = 0.013137788604173103
- coe1[1] = 0.013030394322274175
- ac_auc = 0.01185140005506933
- gp_max_ix_max = 0.01148772271825557
- ratio_max_to_9th_ave_peaks = 0.011055260672097137
- coe3[2] = 0.009207230479092929
- tdoa_max = 0.008981003142949877
- coe1[0] = 0.007308204638755043
- diff_auc = 0.007187442079338251
- diff_std = 0.006981971238754305
- coe3[3] = 0.006207538242424498
- ac_std = 0.004893668541248739
- low_power = 0.004403990907268126
- coe3[0] = 0.0
- coe3[1] = 0.0

## Evaluation
cv = 8
### accuracy
- Scores = [ 0.6896551724137931, 0.5714285714285714, 0.7142857142857143, 0.7857142857142857, 0.75, 0.4642857142857143, 0.75, 0.8928571428571429 ]
- Mean = 0.7022783251231528
- Standard deviation = 0.12344139501638601

### balanced_accuracy
- Scores = [ 0.8043478260869565, 0.6666666666666667, 0.8181818181818181, 0.8636363636363636, 0.8409090909090908, 0.6739130434782609, 0.8478260869565217, 0.7 ]
- Mean = 0.7769351119894597
- Standard deviation = 0.07728174356267968

### f1
- Scores = [ 0.5714285714285715, 0.45454545454545453, 0.6, 0.6666666666666666, 0.631578947368421, 0.4, 0.5882352941176471, 0.5714285714285715 ]
- Mean = 0.5604854381944165
- Standard deviation = 0.08357523239793811

### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 108 | 72 |
| Actual Positive | 2 | 43 |

      