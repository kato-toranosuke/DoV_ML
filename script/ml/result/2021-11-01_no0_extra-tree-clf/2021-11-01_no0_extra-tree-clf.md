# 2021-11-01_no0_extra-tree-clf
## Constants
- CSV_PATH = ../../out/csv/
- OUTPUT_PATH = ./result/
- FEATURE_ATTRBS = ['low_power', 'high_power', 'hlbr', 'coe1[0]', 'coe1[1]', 'coe3[0]', 'coe3[1]', 'coe3[2]', 'coe3[3]', 'ratio_max_to_10ms_ave_peaks', 'ratio_max_to_9th_ave_peaks', 'ac_std', 'ac_auc', 'diff_std', 'diff_auc', 'srmr', 'gp_max_val_std', 'gp_max_val_range', 'gp_max_val_min', 'gp_max_val_max', 'gp_max_val_mean', 'gp_max_ix_std', 'gp_max_ix_range', 'gp_max_ix_min', 'gp_max_ix_max', 'gp_max_ix_mean', 'gp_auc_std', 'gp_auc_range', 'gp_auc_min', 'gp_auc_max', 'gp_auc_mean', 'tdoa_std', 'tdoa_range', 'tdoa_min', 'tdoa_max', 'tdoa_mean']
- LABEL_ATTRB = ['dov_angle']
- FACING_DOV_ANGLES = [0, 45, 315]
- NCV = 10
- SCORING = ['accuracy', 'balanced_accuracy', 'f1']
- REFIT_SCORING = balanced_accuracy
- PARAM_GRID = [{'n_estimators': [100, 300, 500, 800, 1000, 1300, 1500], 'min_samples_split': [2, 5, 10], 'min_samples_leaf': [1, 5, 10], 'max_features': ['sqrt', 'log2', None], 'bootstrap': [False], 'n_jobs': [-1], 'random_state': [42], 'max_samples': [0.01, 0.5, 0.09]}]

## Loaded CSV
- features_mono_ch_matlab.csv

## Estimator
### Type
ExtraTreesClassifier
### Arguments for hyperparameter search
- estimator = ExtraTreesClassifier
- param_grid = 
	- {'n_estimators': [100, 300, 500, 800, 1000, 1300, 1500], 'min_samples_split': [2, 5, 10], 'min_samples_leaf': [1, 5, 10], 'max_features': ['sqrt', 'log2', None], 'bootstrap': [False], 'n_jobs': [-1], 'random_state': [42], 'max_samples': [0.01, 0.5, 0.09]}

- scoring = ['accuracy', 'balanced_accuracy', 'f1']
- refit = balanced_accuracy
- cv = 10

### Parameters of the best estimator
#### The best hyper-parameters
- base_estimator = ExtraTreeClassifier()
- n_estimators = 100
- estimator_params = ('criterion', 'max_depth', 'min_samples_split', 'min_samples_leaf', 'min_weight_fraction_leaf', 'max_features', 'max_leaf_nodes', 'min_impurity_decrease', 'min_impurity_split', 'random_state', 'ccp_alpha')
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
- estimators_ = 
	- ExtraTreeClassifier(max_features=None, min_samples_split=10,
                    random_state=1608637542)
	- ExtraTreeClassifier(max_features=None, min_samples_split=10,
                    random_state=1273642419)
	- ExtraTreeClassifier(max_features=None, min_samples_split=10,
                    random_state=1935803228)
	- ExtraTreeClassifier(max_features=None, min_samples_split=10,
                    random_state=787846414)
	- ExtraTreeClassifier(max_features=None, min_samples_split=10,
                    random_state=996406378)
	- ExtraTreeClassifier(max_features=None, min_samples_split=10,
                    random_state=1201263687)
	- ExtraTreeClassifier(max_features=None, min_samples_split=10,
                    random_state=423734972)
	- ExtraTreeClassifier(max_features=None, min_samples_split=10,
                    random_state=415968276)
	- ExtraTreeClassifier(max_features=None, min_samples_split=10,
                    random_state=670094950)
	- ExtraTreeClassifier(max_features=None, min_samples_split=10,
                    random_state=1914837113)
	- ExtraTreeClassifier(max_features=None, min_samples_split=10,
                    random_state=669991378)
	- ExtraTreeClassifier(max_features=None, min_samples_split=10,
                    random_state=429389014)
	- ExtraTreeClassifier(max_features=None, min_samples_split=10,
                    random_state=249467210)
	- ExtraTreeClassifier(max_features=None, min_samples_split=10,
                    random_state=1972458954)
	- ExtraTreeClassifier(max_features=None, min_samples_split=10,
                    random_state=1572714583)
	- ExtraTreeClassifier(max_features=None, min_samples_split=10,
                    random_state=1433267572)
	- ExtraTreeClassifier(max_features=None, min_samples_split=10,
                    random_state=434285667)
	- ExtraTreeClassifier(max_features=None, min_samples_split=10,
                    random_state=613608295)
	- ExtraTreeClassifier(max_features=None, min_samples_split=10,
                    random_state=893664919)
	- ExtraTreeClassifier(max_features=None, min_samples_split=10,
                    random_state=648061058)
	- ExtraTreeClassifier(max_features=None, min_samples_split=10,
                    random_state=88409749)
	- ExtraTreeClassifier(max_features=None, min_samples_split=10,
                    random_state=242285876)
	- ExtraTreeClassifier(max_features=None, min_samples_split=10,
                    random_state=2018247425)
	- ExtraTreeClassifier(max_features=None, min_samples_split=10,
                    random_state=953477463)
	- ExtraTreeClassifier(max_features=None, min_samples_split=10,
                    random_state=1427830251)
	- ExtraTreeClassifier(max_features=None, min_samples_split=10,
                    random_state=1883569565)
	- ExtraTreeClassifier(max_features=None, min_samples_split=10,
                    random_state=911989541)
	- ExtraTreeClassifier(max_features=None, min_samples_split=10,
                    random_state=3344769)
	- ExtraTreeClassifier(max_features=None, min_samples_split=10,
                    random_state=780932287)
	- ExtraTreeClassifier(max_features=None, min_samples_split=10,
                    random_state=2114032571)
	- ExtraTreeClassifier(max_features=None, min_samples_split=10,
                    random_state=787716372)
	- ExtraTreeClassifier(max_features=None, min_samples_split=10,
                    random_state=504579232)
	- ExtraTreeClassifier(max_features=None, min_samples_split=10,
                    random_state=1306710475)
	- ExtraTreeClassifier(max_features=None, min_samples_split=10,
                    random_state=479546681)
	- ExtraTreeClassifier(max_features=None, min_samples_split=10,
                    random_state=106328085)
	- ExtraTreeClassifier(max_features=None, min_samples_split=10,
                    random_state=30349564)
	- ExtraTreeClassifier(max_features=None, min_samples_split=10,
                    random_state=1855189739)
	- ExtraTreeClassifier(max_features=None, min_samples_split=10,
                    random_state=99052376)
	- ExtraTreeClassifier(max_features=None, min_samples_split=10,
                    random_state=1250819632)
	- ExtraTreeClassifier(max_features=None, min_samples_split=10,
                    random_state=106406362)
	- ExtraTreeClassifier(max_features=None, min_samples_split=10,
                    random_state=480404538)
	- ExtraTreeClassifier(max_features=None, min_samples_split=10,
                    random_state=1717389822)
	- ExtraTreeClassifier(max_features=None, min_samples_split=10,
                    random_state=599121577)
	- ExtraTreeClassifier(max_features=None, min_samples_split=10,
                    random_state=200427519)
	- ExtraTreeClassifier(max_features=None, min_samples_split=10,
                    random_state=1254751707)
	- ExtraTreeClassifier(max_features=None, min_samples_split=10,
                    random_state=2034764475)
	- ExtraTreeClassifier(max_features=None, min_samples_split=10,
                    random_state=1573512143)
	- ExtraTreeClassifier(max_features=None, min_samples_split=10,
                    random_state=999745294)
	- ExtraTreeClassifier(max_features=None, min_samples_split=10,
                    random_state=1958805693)
	- ExtraTreeClassifier(max_features=None, min_samples_split=10,
                    random_state=389151677)
	- ExtraTreeClassifier(max_features=None, min_samples_split=10,
                    random_state=1224821422)
	- ExtraTreeClassifier(max_features=None, min_samples_split=10,
                    random_state=508464061)
	- ExtraTreeClassifier(max_features=None, min_samples_split=10,
                    random_state=857592370)
	- ExtraTreeClassifier(max_features=None, min_samples_split=10,
                    random_state=1642661739)
	- ExtraTreeClassifier(max_features=None, min_samples_split=10,
                    random_state=61136438)
	- ExtraTreeClassifier(max_features=None, min_samples_split=10,
                    random_state=2075460851)
	- ExtraTreeClassifier(max_features=None, min_samples_split=10,
                    random_state=396917567)
	- ExtraTreeClassifier(max_features=None, min_samples_split=10,
                    random_state=2004731384)
	- ExtraTreeClassifier(max_features=None, min_samples_split=10,
                    random_state=199502978)
	- ExtraTreeClassifier(max_features=None, min_samples_split=10,
                    random_state=1545932260)
	- ExtraTreeClassifier(max_features=None, min_samples_split=10,
                    random_state=461901618)
	- ExtraTreeClassifier(max_features=None, min_samples_split=10,
                    random_state=774414982)
	- ExtraTreeClassifier(max_features=None, min_samples_split=10,
                    random_state=732395540)
	- ExtraTreeClassifier(max_features=None, min_samples_split=10,
                    random_state=1934879560)
	- ExtraTreeClassifier(max_features=None, min_samples_split=10,
                    random_state=279394470)
	- ExtraTreeClassifier(max_features=None, min_samples_split=10,
                    random_state=56972561)
	- ExtraTreeClassifier(max_features=None, min_samples_split=10,
                    random_state=1927948675)
	- ExtraTreeClassifier(max_features=None, min_samples_split=10,
                    random_state=1899242072)
	- ExtraTreeClassifier(max_features=None, min_samples_split=10,
                    random_state=1999874363)
	- ExtraTreeClassifier(max_features=None, min_samples_split=10,
                    random_state=271820813)
	- ExtraTreeClassifier(max_features=None, min_samples_split=10,
                    random_state=1324556529)
	- ExtraTreeClassifier(max_features=None, min_samples_split=10,
                    random_state=1655351289)
	- ExtraTreeClassifier(max_features=None, min_samples_split=10,
                    random_state=1308306184)
	- ExtraTreeClassifier(max_features=None, min_samples_split=10,
                    random_state=68574553)
	- ExtraTreeClassifier(max_features=None, min_samples_split=10,
                    random_state=419498548)
	- ExtraTreeClassifier(max_features=None, min_samples_split=10,
                    random_state=991681409)
	- ExtraTreeClassifier(max_features=None, min_samples_split=10,
                    random_state=791274835)
	- ExtraTreeClassifier(max_features=None, min_samples_split=10,
                    random_state=1035196507)
	- ExtraTreeClassifier(max_features=None, min_samples_split=10,
                    random_state=1890440558)
	- ExtraTreeClassifier(max_features=None, min_samples_split=10,
                    random_state=787110843)
	- ExtraTreeClassifier(max_features=None, min_samples_split=10,
                    random_state=524150214)
	- ExtraTreeClassifier(max_features=None, min_samples_split=10,
                    random_state=472432043)
	- ExtraTreeClassifier(max_features=None, min_samples_split=10,
                    random_state=2126768636)
	- ExtraTreeClassifier(max_features=None, min_samples_split=10,
                    random_state=1431061255)
	- ExtraTreeClassifier(max_features=None, min_samples_split=10,
                    random_state=147697582)
	- ExtraTreeClassifier(max_features=None, min_samples_split=10,
                    random_state=744595490)
	- ExtraTreeClassifier(max_features=None, min_samples_split=10,
                    random_state=1758017741)
	- ExtraTreeClassifier(max_features=None, min_samples_split=10,
                    random_state=1679592528)
	- ExtraTreeClassifier(max_features=None, min_samples_split=10,
                    random_state=1111451555)
	- ExtraTreeClassifier(max_features=None, min_samples_split=10,
                    random_state=782698033)
	- ExtraTreeClassifier(max_features=None, min_samples_split=10,
                    random_state=698027879)
	- ExtraTreeClassifier(max_features=None, min_samples_split=10,
                    random_state=1096768899)
	- ExtraTreeClassifier(max_features=None, min_samples_split=10,
                    random_state=1338788865)
	- ExtraTreeClassifier(max_features=None, min_samples_split=10,
                    random_state=1826030589)
	- ExtraTreeClassifier(max_features=None, min_samples_split=10,
                    random_state=86191493)
	- ExtraTreeClassifier(max_features=None, min_samples_split=10,
                    random_state=893102645)
	- ExtraTreeClassifier(max_features=None, min_samples_split=10,
                    random_state=200619113)
	- ExtraTreeClassifier(max_features=None, min_samples_split=10,
                    random_state=290770691)
	- ExtraTreeClassifier(max_features=None, min_samples_split=10,
                    random_state=793943861)
	- ExtraTreeClassifier(max_features=None, min_samples_split=10,
                    random_state=134489564)



#### Importance of features
- gp_max_val_mean = 0.20970068566334027
- gp_max_val_max = 0.18301899745980085
- gp_max_val_min = 0.07732995484484728
- gp_max_val_range = 0.04229788017488329
- gp_auc_min = 0.04048990972185364
- gp_auc_mean = 0.03760714441177824
- gp_max_val_std = 0.03542693851118826
- gp_auc_max = 0.027422735088577576
- diff_std = 0.022320463061415687
- gp_max_ix_min = 0.020227982668428172
- gp_max_ix_mean = 0.019629675685101804
- tdoa_min = 0.018868484218478292
- tdoa_mean = 0.018818881983900273
- high_power = 0.01857620301120222
- ac_auc = 0.017610196578673257
- diff_auc = 0.01647503519334952
- gp_auc_std = 0.016269523734804815
- gp_max_ix_std = 0.015524650324561419
- srmr = 0.014623286962367876
- gp_auc_range = 0.014350139029108812
- tdoa_std = 0.014181813859627166
- ratio_max_to_10ms_ave_peaks = 0.013710505489651173
- ratio_max_to_9th_ave_peaks = 0.013497535629739318
- hlbr = 0.011474847450355196
- ac_std = 0.010345876571962485
- coe1[0] = 0.009574719432283243
- coe1[1] = 0.008657774344713116
- coe3[2] = 0.008134191396492772
- coe3[3] = 0.007928381753844796
- low_power = 0.007848503810917878
- tdoa_max = 0.007724063864960979
- gp_max_ix_max = 0.007149155006435402
- gp_max_ix_range = 0.006813387351709431
- tdoa_range = 0.006370475709645549
- coe3[0] = 0.0
- coe3[1] = 0.0

## Evaluation
### accuracy
- Scores = [ 0.7916666666666666, 0.9097222222222222, 0.8854166666666666, 0.8871527777777778, 0.8680555555555556, 0.8315972222222222, 0.8506944444444444, 0.8368055555555556, 0.8940972222222222, 0.7673611111111112 ]
- Mean = 0.8522569444444444
- Standard deviation = 0.04377926986053564

### balanced_accuracy
- Scores = [ 0.825, 0.9083333333333333, 0.8814814814814815, 0.8606481481481482, 0.8518518518518519, 0.7837962962962963, 0.862037037037037, 0.799074074074074, 0.8782407407407407, 0.6990740740740741 ]
- Mean = 0.8349537037037036
- Standard deviation = 0.05793894085696498

### f1
- Scores = [ 0.7752808988764045, 0.8823529411764707, 0.85, 0.8337595907928389, 0.8173076923076923, 0.725212464589235, 0.8200836820083681, 0.7486631016042781, 0.8523002421307505, 0.5786163522012578 ]
- Mean = 0.7883576965687296
- Standard deviation = 0.08387783764783684

### Confusion Matrix
[[3255  345]
 [ 506 1654]]
