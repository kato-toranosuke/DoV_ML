# ExtraTreesClassifier_RandomUnderSampler_2022-01-09_no2
## Constants
- CSV_PATH = ../out/csv/experiment
- OUTPUT_PATH = ../out/experiment_result/data_of_2022-01-07_new/AGC-45angle-under3m
- FEATURE_ATTRBS = ['low_power', 'high_power', 'hlbr', 'coe1[0]', 'coe1[1]', 'coe3[0]', 'coe3[1]', 'coe3[2]', 'coe3[3]', 'ratio_max_to_10ms_ave_peaks', 'ratio_max_to_9th_ave_peaks', 'ac_std', 'ac_auc', 'diff_std', 'diff_auc', 'srmr', 'gp_max_val_std', 'gp_max_val_range', 'gp_max_val_min', 'gp_max_val_max', 'gp_max_val_mean', 'gp_max_ix_std', 'gp_max_ix_range', 'gp_max_ix_min', 'gp_max_ix_max', 'gp_max_ix_mean', 'gp_auc_std', 'gp_auc_range', 'gp_auc_min', 'gp_auc_max', 'gp_auc_mean', 'tdoa_std', 'tdoa_range', 'tdoa_min', 'tdoa_max', 'tdoa_mean']
- LABEL_ATTRB = ['facing2']
- FACING_DOV_ANGLES = [1, 2]
- NCV = 8
- SCORING = ['accuracy', 'balanced_accuracy', 'f1']
- REFIT_SCORING = balanced_accuracy
- PARAM_GRID = [{'est__n_estimators': [50, 100, 150, 200, 300], 'est__min_samples_split': [2, 5, 10], 'est__min_samples_leaf': [1, 5, 10], 'est__max_features': ['sqrt', 'log2', None], 'est__bootstrap': [False], 'est__n_jobs': [-1], 'est__random_state': [42], 'est__max_samples': [0.01, 0.5, 0.09]}, {'est__n_estimators': [50, 100, 150, 200, 300], 'est__min_samples_split': [2, 5, 10], 'est__min_samples_leaf': [1, 5, 10], 'est__max_features': ['sqrt', 'log2', None], 'est__bootstrap': [True], 'est__oob_score': [True, False], 'est__n_jobs': [-1], 'est__random_state': [42], 'est__max_samples': [0.01, 0.5, 0.09]}]
- TRAIN_SET_SESSION = ['trial1', 'trial2']
- TEST_SET_SESSION = ['trial3', 'trial4', 'trial5']
- DISTANCE = [1, 3]
- AGC_STATUS = ['AGC']

## Loaded CSV
- 2021-12-27_raspi_48000Hz_w1_N2^12_overlap80_with2022-01-07.csv

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
	- sampling_strategy_ = OrderedDict([(1, 48)])
	- sample_indices_ = [ 4  5  6  7  8  9 14 15 16 17 18 19 26 27 28 29 36 37 38 39 40 41 48 49
 50 51 58 59 60 61 62 63 70 71 72 73 80 81 82 83 84 85 90 91 92 93 94 95
 35 77 89 24 79 11 33 98  3 64 25 20 52 12 66 10 69 46 86 65 97 31 21 32
 56 68 47 23  0 88 53 57 75 55 87  1 43  2 76 67 45 96 22 44 34 99 42 13]

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
	- oob_decision_function_ = [[0.10400303 0.89599697]
 [0.10262322 0.89737678]
 [0.97249944 0.02750056]
 [0.96783065 0.03216935]
 [0.98562656 0.01437344]
 [0.98705174 0.01294826]
 [0.77735733 0.22264267]
 [0.51137289 0.48862711]
 [0.97154809 0.02845191]
 [0.98224221 0.01775779]
 [0.96904733 0.03095267]
 [0.96654693 0.03345307]
 [0.51080636 0.48919364]
 [0.76370356 0.23629644]
 [0.97569925 0.02430075]
 [0.96917474 0.03082526]
 [0.81842082 0.18157918]
 [0.76280147 0.23719853]
 [0.98388194 0.01611806]
 [0.95729152 0.04270848]
 [0.81361707 0.18638293]
 [0.8292534  0.1707466 ]
 [0.62794249 0.37205751]
 [0.54525217 0.45474783]
 [0.72066145 0.27933855]
 [0.92683344 0.07316656]
 [0.85310204 0.14689796]
 [0.80051021 0.19948979]
 [0.95391694 0.04608306]
 [0.96205699 0.03794301]
 [0.52655366 0.47344634]
 [0.76756186 0.23243814]
 [0.92863261 0.07136739]
 [0.98824067 0.01175933]
 [0.92728076 0.07271924]
 [0.8850277  0.1149723 ]
 [0.97345072 0.02654928]
 [0.9741178  0.0258822 ]
 [0.95357143 0.04642857]
 [0.89757075 0.10242925]
 [0.69630964 0.30369036]
 [0.77039    0.22961   ]
 [0.94279029 0.05720971]
 [0.96768819 0.03231181]
 [0.98898342 0.01101658]
 [0.97261209 0.02738791]
 [0.90218622 0.09781378]
 [0.85203738 0.14796262]
 [0.05012834 0.94987166]
 [0.06549593 0.93450407]
 [0.09452673 0.90547327]
 [0.19225074 0.80774926]
 [0.08946548 0.91053452]
 [0.13172712 0.86827288]
 [0.06939419 0.93060581]
 [0.07147391 0.92852609]
 [0.19791729 0.80208271]
 [0.21729586 0.78270414]
 [0.19462802 0.80537198]
 [0.22194484 0.77805516]
 [0.47443497 0.52556503]
 [0.26583373 0.73416627]
 [0.07197984 0.92802016]
 [0.04234184 0.95765816]
 [0.13222555 0.86777445]
 [0.12381433 0.87618567]
 [0.09469337 0.90530663]
 [0.14919874 0.85080126]
 [0.35564678 0.64435322]
 [0.59771447 0.40228553]
 [0.19700224 0.80299776]
 [0.13523252 0.86476748]
 [0.18710448 0.81289552]
 [0.21223998 0.78776002]
 [0.14803582 0.85196418]
 [0.17447563 0.82552437]
 [0.18597217 0.81402783]
 [0.18960979 0.81039021]
 [0.49118242 0.50881758]
 [0.17739548 0.82260452]
 [0.07055817 0.92944183]
 [0.04283581 0.95716419]
 [0.21041516 0.78958484]
 [0.13713391 0.86286609]
 [0.19833839 0.80166161]
 [0.17439306 0.82560694]
 [0.06788425 0.93211575]
 [0.08971813 0.91028187]
 [0.13935997 0.86064003]
 [0.29419081 0.70580919]
 [0.12752419 0.87247581]
 [0.17255249 0.82744751]
 [0.16999306 0.83000694]
 [0.04801262 0.95198738]
 [0.15462517 0.84537483]
 [0.1481224  0.8518776 ]]
	- oob_score_ = 0.96875

#### Importance of features
- gp_max_val_mean = 0.11348647654018085
- gp_max_val_min = 0.1121178791830667
- gp_auc_min = 0.10604017273631906
- gp_auc_max = 0.09812569106169924
- gp_auc_mean = 0.09259135829005778
- gp_max_val_max = 0.08979646715522323
- srmr = 0.06751218479807566
- diff_auc = 0.04237876617999579
- diff_std = 0.03345432777331585
- high_power = 0.028015399653273772
- hlbr = 0.021415314025586312
- ratio_max_to_10ms_ave_peaks = 0.0190618566366475
- coe1[0] = 0.0176334889256493
- low_power = 0.015907818573118765
- gp_max_ix_range = 0.013528087019416709
- gp_max_ix_std = 0.012801529183581278
- coe1[1] = 0.012072375196145112
- tdoa_range = 0.010484605383760882
- gp_max_val_std = 0.008874521099120663
- gp_max_ix_mean = 0.008398700102942398
- gp_max_val_range = 0.008035012907262853
- gp_max_ix_min = 0.007519557000493025
- tdoa_min = 0.0072094293671870185
- tdoa_std = 0.005938865212908222
- tdoa_mean = 0.00571034429458619
- gp_auc_std = 0.005539787155825563
- tdoa_max = 0.005420605063445855
- coe3[2] = 0.005407666703833872
- coe3[3] = 0.005018547096352327
- ac_auc = 0.004975119085594092
- gp_auc_range = 0.004940952301450435
- ac_std = 0.004181619775205962
- gp_max_ix_max = 0.003487988727460563
- ratio_max_to_9th_ave_peaks = 0.0029174857912169657
- coe3[0] = 0.0
- coe3[1] = 0.0

## Evaluation
cv = 8
### accuracy
- Scores = [ 0.8421052631578947, 1.0, 1.0, 0.9473684210526315, 1.0, 1.0, 1.0, 1.0 ]
- Mean = 0.9736842105263157
- Standard deviation = 0.05263157894736844

### balanced_accuracy
- Scores = [ 0.8333333333333333, 1.0, 1.0, 0.9444444444444444, 1.0, 1.0, 1.0, 1.0 ]
- Mean = 0.9722222222222222
- Standard deviation = 0.05555555555555558

### f1
- Scores = [ 0.8695652173913044, 1.0, 1.0, 0.9523809523809523, 1.0, 1.0, 1.0, 1.0 ]
- Mean = 0.9777432712215322
- Standard deviation = 0.043757728464490345

### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 67 | 5 |
| Actual Positive | 1 | 77 |

      