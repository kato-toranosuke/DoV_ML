# ExtraTreesClassifier_SMOTE_2021-12-29_no4
## Constants
- CSV_PATH = ../out/csv/experiment
- OUTPUT_PATH = ../out/experiment_result/data_of_2021-12-27/NoAGC-0angle-under5m
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
- 2021-12-27_raspi_48000Hz_w1_N2^12_overlap80_new.csv

## Estimator
### Type
- resampler = SMOTE
- estimator = ExtraTreesClassifier

### Arguments for hyperparameter search
- resampler = SMOTE
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
	- k_neighbors = 5
	- n_jobs = -1
	- n_features_in_ = 36
	- sampling_strategy_ = OrderedDict([(1, 72)])
	- nn_k_ = NearestNeighbors(n_neighbors=6)

- best_estimator
	- base_estimator = ExtraTreeClassifier()
	- n_estimators = 300
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
	- min_samples_split = 5
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
	- oob_decision_function_ = [[0.32474555 0.67525445]
 [0.36480815 0.63519185]
 [0.30030193 0.69969807]
 [0.31391876 0.68608124]
 [0.50300245 0.49699755]
 [0.5203567  0.4796433 ]
 [0.91628931 0.08371069]
 [0.87735507 0.12264493]
 [0.83760843 0.16239157]
 [0.89722222 0.10277778]
 [0.33807829 0.66192171]
 [0.20848485 0.79151515]
 [0.55475309 0.44524691]
 [0.46088308 0.53911692]
 [0.78742479 0.21257521]
 [0.69509091 0.30490909]
 [0.96428571 0.03571429]
 [0.96227758 0.03772242]
 [0.9547088  0.0452912 ]
 [0.92404762 0.07595238]
 [0.54248252 0.45751748]
 [0.38723022 0.61276978]
 [0.59521212 0.40478788]
 [0.54356618 0.45643382]
 [0.91207729 0.08792271]
 [0.87990373 0.12009627]
 [0.96456835 0.03543165]
 [0.95636364 0.04363636]
 [0.95553483 0.04446517]
 [0.92020384 0.07979616]
 [0.31257414 0.68742586]
 [0.28290283 0.71709717]
 [0.32422062 0.67577938]
 [0.33544686 0.66455314]
 [0.38207071 0.61792929]
 [0.40085784 0.59914216]
 [0.66461353 0.33538647]
 [0.60857143 0.39142857]
 [0.86296296 0.13703704]
 [0.80606061 0.19393939]
 [0.49725275 0.50274725]
 [0.43967662 0.56032338]
 [0.54178832 0.45821168]
 [0.32441574 0.67558426]
 [0.56808511 0.43191489]
 [0.49921212 0.50078788]
 [0.62977528 0.37022472]
 [0.61873522 0.38126478]
 [0.94393939 0.05606061]
 [0.94505495 0.05494505]
 [0.78376225 0.21623775]
 [0.68763441 0.31236559]
 [0.46171498 0.53828502]
 [0.35364397 0.64635603]
 [0.71049161 0.28950839]
 [0.42371565 0.57628435]
 [0.92757576 0.07242424]
 [0.9413017  0.0586983 ]
 [0.95726496 0.04273504]
 [0.97461171 0.02538829]
 [0.53665437 0.46334563]
 [0.47086375 0.52913625]
 [0.39653524 0.60346476]
 [0.29861111 0.70138889]
 [0.33168498 0.66831502]
 [0.30635802 0.69364198]
 [0.5001199  0.4998801 ]
 [0.45339286 0.54660714]
 [0.45207592 0.54792408]
 [0.42220217 0.57779783]
 [0.6698032  0.3301968 ]
 [0.64001248 0.35998752]
 [0.55300245 0.44699755]
 [0.40163636 0.59836364]
 [0.51527273 0.48472727]
 [0.35425532 0.64574468]
 [0.41799037 0.58200963]
 [0.35747549 0.64252451]
 [0.62349823 0.37650177]
 [0.62661871 0.37338129]
 [0.81105006 0.18894994]
 [0.81303813 0.18696187]
 [0.67919664 0.32080336]
 [0.51240876 0.48759124]
 [0.47432099 0.52567901]
 [0.31232394 0.68767606]
 [0.60073529 0.39926471]
 [0.56455224 0.43544776]
 [0.94224664 0.05775336]
 [0.93611111 0.06388889]
 [0.87278788 0.12721212]
 [0.85625752 0.14374248]
 [0.64275618 0.35724382]
 [0.52084848 0.47915152]
 [0.40240674 0.59759326]
 [0.41257631 0.58742369]
 [0.36583924 0.63416076]
 [0.41226415 0.58773585]
 [0.43847584 0.56152416]
 [0.43042131 0.56957869]
 [0.91245552 0.08754448]
 [0.93977136 0.06022864]
 [0.9290012  0.0709988 ]
 [0.76113095 0.23886905]
 [0.38933333 0.61066667]
 [0.34616307 0.65383693]
 [0.21835138 0.78164862]
 [0.28381643 0.71618357]
 [0.36440252 0.63559748]
 [0.36748737 0.63251263]
 [0.87371324 0.12628676]
 [0.84702155 0.15297845]
 [0.83900836 0.16099164]
 [0.84322542 0.15677458]
 [0.73723022 0.26276978]
 [0.37882206 0.62117794]
 [0.30330927 0.69669073]
 [0.25442308 0.74557692]
 [0.42979616 0.57020384]
 [0.51875747 0.48124253]
 [0.23253968 0.76746032]
 [0.44618545 0.55381455]
 [0.36896135 0.63103865]
 [0.29244114 0.70755886]
 [0.35647131 0.64352869]
 [0.26935287 0.73064713]
 [0.31751208 0.68248792]
 [0.48901373 0.51098627]
 [0.23043735 0.76956265]
 [0.21145084 0.78854916]
 [0.283829   0.716171  ]
 [0.33061594 0.66938406]
 [0.26991422 0.73008578]
 [0.30693431 0.69306569]
 [0.28872902 0.71127098]
 [0.20710784 0.79289216]
 [0.27316602 0.72683398]
 [0.46690562 0.53309438]
 [0.30485612 0.69514388]
 [0.52144564 0.47855436]
 [0.24444444 0.75555556]
 [0.15074906 0.84925094]
 [0.30979319 0.69020681]
 [0.20557554 0.79442446]
 [0.42154031 0.57845969]
 [0.17626076 0.82373924]
 [0.15673887 0.84326113]
 [0.25076291 0.74923709]
 [0.30521583 0.69478417]
 [0.52327273 0.47672727]
 [0.47630907 0.52369093]
 [0.21697192 0.78302808]
 [0.30130112 0.69869888]
 [0.54751515 0.45248485]
 [0.20781441 0.79218559]
 [0.28634176 0.71365824]
 [0.29391727 0.70608273]
 [0.27209738 0.72790262]
 [0.33515152 0.66484848]
 [0.40065947 0.59934053]
 [0.3442285  0.6557715 ]
 [0.30103406 0.69896594]
 [0.31131387 0.68868613]
 [0.20083933 0.79916067]
 [0.26561728 0.73438272]
 [0.18247549 0.81752451]
 [0.37035024 0.62964976]
 [0.24385645 0.75614355]
 [0.21082411 0.78917589]
 [0.21363095 0.78636905]
 [0.20636364 0.79363636]
 [0.25509091 0.74490909]
 [0.24893883 0.75106117]
 [0.35771605 0.64228395]
 [0.26319444 0.73680556]
 [0.21509091 0.78490909]
 [0.17715827 0.82284173]
 [0.43935523 0.56064477]
 [0.42748227 0.57251773]
 [0.31235012 0.68764988]
 [0.20277778 0.79722222]
 [0.29320988 0.70679012]
 [0.28947689 0.71052311]
 [0.32254902 0.67745098]
 [0.31404151 0.68595849]
 [0.34471095 0.65528905]
 [0.20419664 0.79580336]
 [0.18060719 0.81939281]
 [0.24379562 0.75620438]
 [0.19475655 0.80524345]
 [0.37876053 0.62123947]
 [0.34758364 0.65241636]]
	- oob_score_ = 0.8125

#### Importance of features
- srmr = 0.06728935387620065
- gp_auc_min = 0.05845457006994757
- hlbr = 0.05591486689593848
- diff_std = 0.052273989252740356
- gp_max_val_max = 0.04766247310733675
- gp_max_val_min = 0.04675355040274645
- gp_auc_mean = 0.04637926659798599
- gp_auc_max = 0.04538024843153904
- ratio_max_to_10ms_ave_peaks = 0.04317335206113512
- diff_auc = 0.03965063183134288
- coe1[1] = 0.035753763836114144
- ratio_max_to_9th_ave_peaks = 0.03396298464303036
- ac_std = 0.03310837355946915
- gp_auc_std = 0.030808745462079797
- gp_auc_range = 0.029192217074457277
- gp_max_val_mean = 0.028342014084025147
- high_power = 0.027171331312352328
- gp_max_val_range = 0.02636183173896774
- gp_max_ix_max = 0.02311110631740941
- tdoa_max = 0.022941792603633607
- coe3[3] = 0.022014370949549833
- ac_auc = 0.02192921023930478
- coe1[0] = 0.021222101848826107
- low_power = 0.02096635468918773
- gp_max_val_std = 0.019724338510540146
- tdoa_mean = 0.016676370331434376
- coe3[2] = 0.014420792242451382
- gp_max_ix_mean = 0.013851172144676096
- tdoa_min = 0.01151899302736828
- gp_max_ix_min = 0.010036750693622478
- gp_max_ix_range = 0.008860047185883695
- gp_max_ix_std = 0.008695820970272805
- tdoa_range = 0.008540104764448974
- tdoa_std = 0.007857109243981225
- coe3[0] = 0.0
- coe3[1] = 0.0

## Evaluation
cv = 8
### accuracy
- Scores = [ 0.6521739130434783, 0.8260869565217391, 0.6521739130434783, 0.9090909090909091, 0.45454545454545453, 0.8181818181818182, 0.7727272727272727, 0.6363636363636364 ]
- Mean = 0.7151679841897233
- Standard deviation = 0.13504849828383422

### balanced_accuracy
- Scores = [ 0.7055555555555556, 0.6, 0.7777777777777778, 0.8, 0.5694444444444444, 0.7916666666666667, 0.8611111111111112, 0.4861111111111111 ]
- Mean = 0.6989583333333333
- Standard deviation = 0.12410899651908928

### f1
- Scores = [ 0.5000000000000001, 0.33333333333333337, 0.5555555555555556, 0.7499999999999999, 0.3333333333333333, 0.6, 0.6153846153846153, 0.2 ]
- Mean = 0.4859508547008547
- Standard deviation = 0.17061526782025016

### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 104 | 39 |
| Actual Positive | 12 | 24 |

      