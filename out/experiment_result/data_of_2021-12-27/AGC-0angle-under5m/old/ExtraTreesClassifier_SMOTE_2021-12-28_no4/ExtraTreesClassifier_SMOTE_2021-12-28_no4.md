# ExtraTreesClassifier_SMOTE_2021-12-28_no4
## Constants
- CSV_PATH = ../out/csv/experiment
- OUTPUT_PATH = ../out/experiment_result
- FEATURE_ATTRBS = ['low_power', 'high_power', 'hlbr', 'coe1[0]', 'coe1[1]', 'coe3[0]', 'coe3[1]', 'coe3[2]', 'coe3[3]', 'ratio_max_to_10ms_ave_peaks', 'ratio_max_to_9th_ave_peaks', 'ac_std', 'ac_auc', 'diff_std', 'diff_auc', 'srmr', 'gp_max_val_std', 'gp_max_val_range', 'gp_max_val_min', 'gp_max_val_max', 'gp_max_val_mean', 'gp_max_ix_std', 'gp_max_ix_range', 'gp_max_ix_min', 'gp_max_ix_max', 'gp_max_ix_mean', 'gp_auc_std', 'gp_auc_range', 'gp_auc_min', 'gp_auc_max', 'gp_auc_mean', 'tdoa_std', 'tdoa_range', 'tdoa_min', 'tdoa_max', 'tdoa_mean']
- LABEL_ATTRB = ['facing']
- FACING_DOV_ANGLES = [1]
- NCV = 8
- SCORING = ['accuracy', 'balanced_accuracy', 'f1']
- REFIT_SCORING = balanced_accuracy
- PARAM_GRID = [{'est__n_estimators': [50, 100, 150, 200, 300], 'est__min_samples_split': [2, 5, 10], 'est__min_samples_leaf': [1, 5, 10], 'est__max_features': ['sqrt', 'log2', None], 'est__bootstrap': [False], 'est__n_jobs': [-1], 'est__random_state': [42], 'est__max_samples': [0.01, 0.5, 0.09]}, {'est__n_estimators': [50, 100, 150, 200, 300], 'est__min_samples_split': [2, 5, 10], 'est__min_samples_leaf': [1, 5, 10], 'est__max_features': ['sqrt', 'log2', None], 'est__bootstrap': [True], 'est__oob_score': [True, False], 'est__n_jobs': [-1], 'est__random_state': [42], 'est__max_samples': [0.01, 0.5, 0.09]}]
- TRAIN_SET_SESSION = ['trial1', 'trial2']
- TEST_SET_SESSION = ['trial3', 'trial4', 'trial5']

## Loaded CSV
- 2021-12-27_raspi_48000Hz_w1_N2^12_overlap80_withfacing.csv

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
	- sampling_strategy_ = OrderedDict([(1, 88)])
	- nn_k_ = NearestNeighbors(n_neighbors=6)

- best_estimator
	- base_estimator = ExtraTreeClassifier()
	- n_estimators = 150
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
	- max_features = sqrt
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
	- oob_decision_function_ = [[0.45298113 0.54701887]
 [0.43909605 0.56090395]
 [0.43646455 0.56353545]
 [0.44075716 0.55924284]
 [0.40390898 0.59609102]
 [0.45658404 0.54341596]
 [0.89068311 0.10931689]
 [0.90903589 0.09096411]
 [0.95302883 0.04697117]
 [0.93267625 0.06732375]
 [0.32326935 0.67673065]
 [0.35545808 0.64454192]
 [0.46290146 0.53709854]
 [0.329574   0.670426  ]
 [0.74213513 0.25786487]
 [0.54853752 0.45146248]
 [0.95961851 0.04038149]
 [0.95989821 0.04010179]
 [0.87968105 0.12031895]
 [0.87576576 0.12423424]
 [0.3744445  0.6255555 ]
 [0.33186463 0.66813537]
 [0.81109656 0.18890344]
 [0.56654667 0.43345333]
 [0.88085782 0.11914218]
 [0.75870263 0.24129737]
 [0.95998783 0.04001217]
 [0.94943681 0.05056319]
 [0.9373044  0.0626956 ]
 [0.94605237 0.05394763]
 [0.42525848 0.57474152]
 [0.45169271 0.54830729]
 [0.42588192 0.57411808]
 [0.45447483 0.54552517]
 [0.44433018 0.55566982]
 [0.45553388 0.54446612]
 [0.59082161 0.40917839]
 [0.60108188 0.39891812]
 [0.92925747 0.07074253]
 [0.94398819 0.05601181]
 [0.64472946 0.35527054]
 [0.62952415 0.37047585]
 [0.31235804 0.68764196]
 [0.17523695 0.82476305]
 [0.37541231 0.62458769]
 [0.22437717 0.77562283]
 [0.78038277 0.21961723]
 [0.72912923 0.27087077]
 [0.96573711 0.03426289]
 [0.95934888 0.04065112]
 [0.51491829 0.48508171]
 [0.45515831 0.54484169]
 [0.66231472 0.33768528]
 [0.33971527 0.66028473]
 [0.38706533 0.61293467]
 [0.35058227 0.64941773]
 [0.85162145 0.14837855]
 [0.74929017 0.25070983]
 [0.89577091 0.10422909]
 [0.87451606 0.12548394]
 [0.64254066 0.35745934]
 [0.70102647 0.29897353]
 [0.42700863 0.57299137]
 [0.42656665 0.57343335]
 [0.44633949 0.55366051]
 [0.4501872  0.5498128 ]
 [0.41873277 0.58126723]
 [0.44478345 0.55521655]
 [0.61147287 0.38852713]
 [0.52644081 0.47355919]
 [0.90057938 0.09942062]
 [0.87243867 0.12756133]
 [0.608816   0.391184  ]
 [0.46638008 0.53361992]
 [0.1889524  0.8110476 ]
 [0.18867515 0.81132485]
 [0.3119005  0.6880995 ]
 [0.33672893 0.66327107]
 [0.72462434 0.27537566]
 [0.65418618 0.34581382]
 [0.93633261 0.06366739]
 [0.93139396 0.06860604]
 [0.88359522 0.11640478]
 [0.64155822 0.35844178]
 [0.2914581  0.7085419 ]
 [0.27318613 0.72681387]
 [0.45427633 0.54572367]
 [0.40282517 0.59717483]
 [0.85754537 0.14245463]
 [0.87867732 0.12132268]
 [0.93114842 0.06885158]
 [0.92267152 0.07732848]
 [0.53398279 0.46601721]
 [0.65199789 0.34800211]
 [0.42024393 0.57975607]
 [0.40137202 0.59862798]
 [0.29719201 0.70280799]
 [0.3175084  0.6824916 ]
 [0.4216661  0.5783339 ]
 [0.43852763 0.56147237]
 [0.86034704 0.13965296]
 [0.95459076 0.04540924]
 [0.87207704 0.12792296]
 [0.76651799 0.23348201]
 [0.3327222  0.6672778 ]
 [0.22528042 0.77471958]
 [0.21411922 0.78588078]
 [0.21744598 0.78255402]
 [0.37650848 0.62349152]
 [0.25486375 0.74513625]
 [0.95570499 0.04429501]
 [0.93950179 0.06049821]
 [0.96112297 0.03887703]
 [0.9244247  0.0755753 ]
 [0.62962886 0.37037114]
 [0.5235509  0.4764491 ]
 [0.27937791 0.72062209]
 [0.32849696 0.67150304]
 [0.39136657 0.60863343]
 [0.59147172 0.40852828]
 [0.95592427 0.04407573]
 [0.94902711 0.05097289]
 [0.89605577 0.10394423]
 [0.85916992 0.14083008]
 [0.64891503 0.35108497]
 [0.65906509 0.34093491]
 [0.33555537 0.66444463]
 [0.40353123 0.59646877]
 [0.40143899 0.59856101]
 [0.37992728 0.62007272]
 [0.91744747 0.08255253]
 [0.95696926 0.04303074]
 [0.84627237 0.15372763]
 [0.74225067 0.25774933]
 [0.321388   0.678612  ]
 [0.34552407 0.65447593]
 [0.20882075 0.79117925]
 [0.21299099 0.78700901]
 [0.96550981 0.03449019]
 [0.9606019  0.0393981 ]
 [0.97056776 0.02943224]
 [0.95703873 0.04296127]
 [0.92497953 0.07502047]
 [0.87096793 0.12903207]
 [0.49017591 0.50982409]
 [0.59185506 0.40814494]
 [0.29068445 0.70931555]
 [0.38543725 0.61456275]
 [0.20410281 0.79589719]
 [0.29572993 0.70427007]
 [0.33230916 0.66769084]
 [0.21631199 0.78368801]
 [0.21402947 0.78597053]
 [0.25795617 0.74204383]
 [0.2101296  0.7898704 ]
 [0.35997146 0.64002854]
 [0.17411855 0.82588145]
 [0.32980097 0.67019903]
 [0.31075406 0.68924594]
 [0.35139598 0.64860402]
 [0.31008486 0.68991514]
 [0.2155597  0.7844403 ]
 [0.28991001 0.71008999]
 [0.22323606 0.77676394]
 [0.44386257 0.55613743]
 [0.32358781 0.67641219]
 [0.43555874 0.56444126]
 [0.32191657 0.67808343]
 [0.2831084  0.7168916 ]
 [0.31154808 0.68845192]
 [0.41949915 0.58050085]
 [0.26844225 0.73155775]
 [0.17992415 0.82007585]
 [0.23755263 0.76244737]
 [0.21278901 0.78721099]
 [0.41215003 0.58784997]
 [0.18595611 0.81404389]
 [0.36766882 0.63233118]
 [0.42942112 0.57057888]
 [0.21763905 0.78236095]
 [0.67297747 0.32702253]
 [0.30917015 0.69082985]
 [0.33490876 0.66509124]
 [0.2047881  0.7952119 ]
 [0.30202201 0.69797799]
 [0.21701966 0.78298034]
 [0.33181141 0.66818859]
 [0.20851702 0.79148298]
 [0.35617141 0.64382859]
 [0.45426959 0.54573041]
 [0.23910216 0.76089784]
 [0.20718338 0.79281662]
 [0.28381802 0.71618198]
 [0.20419708 0.79580292]
 [0.31777523 0.68222477]
 [0.2831818  0.7168182 ]
 [0.43423371 0.56576629]
 [0.43731025 0.56268975]
 [0.19640494 0.80359506]
 [0.18552608 0.81447392]
 [0.29940601 0.70059399]
 [0.20399223 0.79600777]
 [0.4445309  0.5554691 ]
 [0.21773304 0.78226696]
 [0.48405344 0.51594656]
 [0.38809181 0.61190819]
 [0.41178194 0.58821806]
 [0.37641589 0.62358411]
 [0.27428543 0.72571457]
 [0.33001155 0.66998845]
 [0.3751768  0.6248232 ]
 [0.18619567 0.81380433]
 [0.18251491 0.81748509]
 [0.22288532 0.77711468]
 [0.42907998 0.57092002]
 [0.20291664 0.79708336]
 [0.28901027 0.71098973]
 [0.22349615 0.77650385]
 [0.21758084 0.78241916]
 [0.36646103 0.63353897]
 [0.27664507 0.72335493]
 [0.17120093 0.82879907]
 [0.2925413  0.7074587 ]
 [0.45199134 0.54800866]
 [0.3144259  0.6855741 ]
 [0.18670293 0.81329707]
 [0.42145234 0.57854766]
 [0.29625217 0.70374783]
 [0.29815015 0.70184985]
 [0.19223184 0.80776816]
 [0.43071589 0.56928411]
 [0.18676198 0.81323802]
 [0.18739491 0.81260509]
 [0.18062148 0.81937852]
 [0.44283776 0.55716224]
 [0.42706815 0.57293185]]
	- oob_score_ = 0.8305084745762712

#### Importance of features
- gp_max_val_min = 0.08859212859487514
- gp_auc_min = 0.07665525476239228
- gp_auc_max = 0.07326994320887885
- gp_max_val_mean = 0.0709239294453245
- gp_max_val_max = 0.06539820024378079
- gp_auc_mean = 0.0625292951848922
- high_power = 0.06163182187447374
- hlbr = 0.055165692140676084
- coe1[1] = 0.05188451831898214
- diff_std = 0.05042982487704985
- coe1[0] = 0.050112808699483063
- diff_auc = 0.049363744952990334
- coe3[3] = 0.040082710374404376
- low_power = 0.03460104214378517
- srmr = 0.029825687759900073
- coe3[2] = 0.028697845983058436
- gp_auc_range = 0.01113583143025043
- tdoa_range = 0.010460883478761028
- gp_max_ix_max = 0.00888779863028604
- ac_std = 0.008864767245712345
- tdoa_min = 0.007937041988868588
- ratio_max_to_10ms_ave_peaks = 0.007495802219645999
- ac_auc = 0.007009669083504785
- gp_max_val_range = 0.006026917392299101
- tdoa_max = 0.0057263420010449
- gp_max_ix_min = 0.005445291109674317
- gp_max_ix_mean = 0.005275789860013665
- gp_max_val_std = 0.005006999200581777
- gp_max_ix_range = 0.003946212080274223
- tdoa_mean = 0.003818943325032251
- ratio_max_to_9th_ave_peaks = 0.0037900605459032454
- gp_auc_std = 0.003774786381018859
- tdoa_std = 0.003553691769002679
- gp_max_ix_std = 0.0026787236931788737
- coe3[0] = 0.0
- coe3[1] = 0.0

## Evaluation
cv = 8
### accuracy
- Scores = [ 0.6785714285714286, 0.7857142857142857, 0.6785714285714286, 0.7142857142857143, 0.7857142857142857, 0.5357142857142857, 0.75, 0.8571428571428571 ]
- Mean = 0.7232142857142858
- Standard deviation = 0.09061510325975194

### balanced_accuracy
- Scores = [ 0.7348484848484849, 0.8636363636363636, 0.6136363636363636, 0.8181818181818181, 0.8636363636363636, 0.717391304347826, 0.7695652173913043, 0.9130434782608696 ]
- Mean = 0.7867424242424242
- Standard deviation = 0.09119283894493607

### f1
- Scores = [ 0.5263157894736842, 0.6666666666666666, 0.4, 0.6, 0.6666666666666666, 0.4347826086956522, 0.5333333333333333, 0.7142857142857143 ]
- Mean = 0.5677563473902147
- Standard deviation = 0.10653842148754687

### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 122 | 57 |
| Actual Positive | 5 | 40 |

      