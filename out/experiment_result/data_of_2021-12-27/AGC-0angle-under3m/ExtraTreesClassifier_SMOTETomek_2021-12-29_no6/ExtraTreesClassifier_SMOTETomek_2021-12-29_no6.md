# ExtraTreesClassifier_SMOTETomek_2021-12-29_no6
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
- resampler = SMOTETomek
- estimator = ExtraTreesClassifier

### Arguments for hyperparameter search
- resampler = SMOTETomek
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
	- smote = None
	- tomek = None
	- n_jobs = -1
	- n_features_in_ = 36
	- sampling_strategy_ = auto
	- smote_ = SMOTE(n_jobs=-1, random_state=42)
	- tomek_ = TomekLinks(n_jobs=-1, sampling_strategy='all')

- best_estimator
	- base_estimator = ExtraTreeClassifier()
	- n_estimators = 50
	- estimator_params = ('criterion', 'max_depth', 'min_samples_split', 'min_samples_leaf', 'min_weight_fraction_leaf', 'max_features', 'max_leaf_nodes', 'min_impurity_decrease', 'min_impurity_split', 'random_state', 'ccp_alpha')
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
	- min_impurity_split = None
	- ccp_alpha = 0.0
	- n_features_in_ = 36
	- n_features_ = 36
	- n_outputs_ = 1
	- classes_ = [0 1]
	- n_classes_ = 2
	- base_estimator_ = ExtraTreeClassifier()
	- oob_decision_function_ = [[0.3450113  0.6549887 ]
 [0.31992703 0.68007297]
 [0.40344512 0.59655488]
 [0.45137005 0.54862995]
 [0.32804042 0.67195958]
 [0.48727521 0.51272479]
 [0.97369807 0.02630193]
 [0.96375169 0.03624831]
 [0.93601773 0.06398227]
 [0.94213479 0.05786521]
 [0.40242562 0.59757438]
 [0.90104037 0.09895963]
 [0.89135228 0.10864772]
 [0.87736849 0.12263151]
 [0.28322912 0.71677088]
 [0.37270695 0.62729305]
 [0.35626675 0.64373325]
 [0.46001741 0.53998259]
 [0.69931796 0.30068204]
 [0.89077895 0.10922105]
 [0.97732075 0.02267925]
 [0.97501113 0.02498887]
 [0.86325604 0.13674396]
 [0.83591768 0.16408232]
 [0.20438246 0.79561754]
 [0.08359661 0.91640339]
 [0.89928047 0.10071953]
 [0.95494238 0.04505762]
 [0.96021036 0.03978964]
 [0.97173444 0.02826556]
 [0.97423654 0.02576346]
 [0.53957325 0.46042675]
 [0.4842713  0.5157287 ]
 [0.38739079 0.61260921]
 [0.41898445 0.58101555]
 [0.43938138 0.56061862]
 [0.81246763 0.18753237]
 [0.78565078 0.21434922]
 [0.95391723 0.04608277]
 [0.94899389 0.05100611]
 [0.7866233  0.2133767 ]
 [0.53065081 0.46934919]
 [0.07956162 0.92043838]
 [0.09253492 0.90746508]
 [0.54988699 0.45011301]
 [0.93484941 0.06515059]
 [0.89388125 0.10611875]
 [0.97224869 0.02775131]
 [0.98015955 0.01984045]
 [0.67148565 0.32851435]
 [0.35114581 0.64885419]
 [0.38685502 0.61314498]
 [0.19446341 0.80553659]
 [0.51082424 0.48917576]
 [0.97514378 0.02485622]
 [0.96256434 0.03743566]
 [0.95861426 0.04138574]
 [0.41405421 0.58594579]
 [0.2907317  0.7092683 ]
 [0.18656967 0.81343033]
 [0.11067735 0.88932265]
 [0.47180961 0.52819039]
 [0.28623223 0.71376777]
 [0.97044913 0.02955087]
 [0.96669377 0.03330623]
 [0.98293511 0.01706489]
 [0.94381994 0.05618006]
 [0.94943149 0.05056851]
 [0.45241173 0.54758827]
 [0.96669991 0.03330009]
 [0.97670603 0.02329397]
 [0.95263347 0.04736653]
 [0.51890371 0.48109629]
 [0.46952229 0.53047771]
 [0.28654348 0.71345652]
 [0.18392789 0.81607211]
 [0.10658911 0.89341089]
 [0.1655202  0.8344798 ]
 [0.1763314  0.8236686 ]
 [0.19261775 0.80738225]
 [0.3183443  0.6816557 ]
 [0.53891315 0.46108685]
 [0.06579459 0.93420541]
 [0.07576318 0.92423682]
 [0.32347422 0.67652578]
 [0.33822349 0.66177651]
 [0.33840789 0.66159211]
 [0.06923122 0.93076878]
 [0.28684074 0.71315926]
 [0.3788605  0.6211395 ]
 [0.05654746 0.94345254]
 [0.27881537 0.72118463]
 [0.39705369 0.60294631]
 [0.05794359 0.94205641]
 [0.31345655 0.68654345]
 [0.07829731 0.92170269]
 [0.34879817 0.65120183]
 [0.27211831 0.72788169]
 [0.17826959 0.82173041]
 [0.07616861 0.92383139]
 [0.42033631 0.57966369]
 [0.17359303 0.82640697]
 [0.07494272 0.92505728]
 [0.10496193 0.89503807]
 [0.20018341 0.79981659]
 [0.2458473  0.7541527 ]
 [0.43356749 0.56643251]
 [0.41623737 0.58376263]
 [0.06631862 0.93368138]
 [0.19451931 0.80548069]
 [0.2684949  0.7315051 ]
 [0.32860307 0.67139693]
 [0.08612964 0.91387036]
 [0.36086435 0.63913565]
 [0.12786648 0.87213352]
 [0.07370065 0.92629935]
 [0.37927121 0.62072879]
 [0.07889589 0.92110411]
 [0.47496787 0.52503213]
 [0.07485402 0.92514598]]
	- oob_score_ = 0.8583333333333333

#### Importance of features
- gp_auc_min = 0.16094488976796906
- gp_max_val_min = 0.13461568428021026
- gp_max_val_mean = 0.10559445432107899
- gp_auc_max = 0.09563288008293007
- srmr = 0.0823287846040332
- coe1[0] = 0.07851787687036704
- gp_max_val_max = 0.07372011030299762
- gp_auc_mean = 0.051245391083885046
- coe1[1] = 0.050628219984758964
- low_power = 0.02704918197596804
- ac_std = 0.02702182590721974
- diff_auc = 0.018890372753729522
- gp_max_val_std = 0.01802953726384193
- diff_std = 0.017782860949167246
- hlbr = 0.01775293667930532
- high_power = 0.011324845869665057
- gp_max_val_range = 0.006081061586000711
- gp_auc_range = 0.005453788516728311
- coe3[2] = 0.0042525566369678355
- tdoa_range = 0.0038122408351386507
- gp_max_ix_mean = 0.0024311242375249335
- gp_max_ix_std = 0.0021559537911801084
- ratio_max_to_10ms_ave_peaks = 0.002119556593294494
- ratio_max_to_9th_ave_peaks = 0.001788737602176668
- coe3[3] = 0.0006885010757829311
- tdoa_max = 9.640296439115468e-05
- gp_max_ix_min = 4.022346368715153e-05
- coe3[0] = 0.0
- coe3[1] = 0.0
- ac_auc = 0.0
- gp_max_ix_range = 0.0
- gp_max_ix_max = 0.0
- gp_auc_std = 0.0
- tdoa_std = 0.0
- tdoa_min = 0.0
- tdoa_mean = 0.0

## Evaluation
cv = 8
### accuracy
- Scores = [ 0.5789473684210527, 0.631578947368421, 0.8947368421052632, 0.631578947368421, 0.8947368421052632, 0.6111111111111112, 0.7777777777777778, 0.7222222222222222 ]
- Mean = 0.7178362573099415
- Standard deviation = 0.11819522182109789

### balanced_accuracy
- Scores = [ 0.7333333333333334, 0.675, 0.9333333333333333, 0.675, 0.9333333333333333, 0.6607142857142857, 0.7333333333333334, 0.5666666666666667 ]
- Mean = 0.7388392857142857
- Standard deviation = 0.12227752007087214

### f1
- Scores = [ 0.5, 0.46153846153846156, 0.8, 0.46153846153846156, 0.8, 0.46153846153846156, 0.5, 0.28571428571428575 ]
- Mean = 0.5337912087912088
- Standard deviation = 0.16629096143388833

### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 83 | 36 |
| Actual Positive | 6 | 24 |

      