# ExtraTreesClassifier_SMOTE_2021-12-28_no4
## Constants
- CSV_PATH = ../out/csv/experiment
- OUTPUT_PATH = ../out/experiment_result/2021-12-27-under3m
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
	- sampling_strategy_ = OrderedDict([(1, 58)])
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
	- oob_decision_function_ = [[0.30850444 0.69149556]
 [0.31784768 0.68215232]
 [0.43658122 0.56341878]
 [0.44040381 0.55959619]
 [0.36211686 0.63788314]
 [0.56980535 0.43019465]
 [0.98440775 0.01559225]
 [0.97923677 0.02076323]
 [0.97778094 0.02221906]
 [0.98353886 0.01646114]
 [0.40674449 0.59325551]
 [0.48964533 0.51035467]
 [0.34211542 0.65788458]
 [0.36048823 0.63951177]
 [0.94402709 0.05597291]
 [0.85117197 0.14882803]
 [0.98575448 0.01424552]
 [0.98676239 0.01323761]
 [0.94610928 0.05389072]
 [0.95097578 0.04902422]
 [0.22743033 0.77256967]
 [0.33587811 0.66412189]
 [0.27425381 0.72574619]
 [0.34611813 0.65388187]
 [0.43430921 0.56569079]
 [0.48484533 0.51515467]
 [0.77963853 0.22036147]
 [0.92944017 0.07055983]
 [0.98909935 0.01090065]
 [0.98974318 0.01025682]
 [0.87079552 0.12920448]
 [0.8256882  0.1743118 ]
 [0.28556006 0.71443994]
 [0.07789708 0.92210292]
 [0.48824918 0.51175082]
 [0.17082673 0.82917327]
 [0.94998211 0.05001789]
 [0.95409173 0.04590827]
 [0.98614303 0.01385697]
 [0.99107132 0.00892868]
 [0.96001939 0.03998061]
 [0.97076899 0.02923101]
 [0.51142698 0.48857302]
 [0.51012538 0.48987462]
 [0.49801513 0.50198487]
 [0.44895673 0.55104327]
 [0.424813   0.575187  ]
 [0.54803497 0.45196503]
 [0.87778116 0.12221884]
 [0.8356066  0.1643934 ]
 [0.98809251 0.01190749]
 [0.98774526 0.01225474]
 [0.73857521 0.26142479]
 [0.53731002 0.46268998]
 [0.08581705 0.91418295]
 [0.13573355 0.86426645]
 [0.43804156 0.56195844]
 [0.48501293 0.51498707]
 [0.95600985 0.04399015]
 [0.924172   0.075828  ]
 [0.98897472 0.01102528]
 [0.98690831 0.01309169]
 [0.77501293 0.22498707]
 [0.93913097 0.06086903]
 [0.3331072  0.6668928 ]
 [0.40495864 0.59504136]
 [0.17587957 0.82412043]
 [0.27598032 0.72401968]
 [0.63222962 0.36777038]
 [0.5829718  0.4170282 ]
 [0.97755118 0.02244882]
 [0.99074716 0.00925284]
 [0.98480821 0.01519179]
 [0.95784149 0.04215851]
 [0.3690571  0.6309429 ]
 [0.2747862  0.7252138 ]
 [0.19417328 0.80582672]
 [0.10447511 0.89552489]
 [0.50907625 0.49092375]
 [0.31269044 0.68730956]
 [0.99013096 0.00986904]
 [0.99437442 0.00562558]
 [0.98685472 0.01314528]
 [0.97392051 0.02607949]
 [0.92864131 0.07135869]
 [0.94218774 0.05781226]
 [0.46316635 0.53683365]
 [0.57994497 0.42005503]
 [0.56972123 0.43027877]
 [0.31984342 0.68015658]
 [0.98481359 0.01518641]
 [0.99179816 0.00820184]
 [0.97329315 0.02670685]
 [0.94262774 0.05737226]
 [0.64049951 0.35950049]
 [0.67768569 0.32231431]
 [0.34326265 0.65673735]
 [0.18132795 0.81867205]
 [0.12163769 0.87836231]
 [0.27677653 0.72322347]
 [0.14665486 0.85334514]
 [0.18613046 0.81386954]
 [0.19598393 0.80401607]
 [0.29902679 0.70097321]
 [0.5494858  0.4505142 ]
 [0.30107596 0.69892404]
 [0.06834444 0.93165556]
 [0.07518703 0.92481297]
 [0.31105457 0.68894543]
 [0.0630431  0.9369569 ]
 [0.3038051  0.6961949 ]
 [0.29898805 0.70101195]
 [0.2881277  0.7118723 ]
 [0.07685786 0.92314214]
 [0.29214717 0.70785283]
 [0.28956413 0.71043587]
 [0.34154653 0.65845347]
 [0.06790931 0.93209069]
 [0.28994455 0.71005545]
 [0.42554259 0.57445741]
 [0.07704509 0.92295491]
 [0.29059119 0.70940881]
 [0.28453007 0.71546993]
 [0.23705135 0.76294865]
 [0.10538266 0.89461734]
 [0.29916345 0.70083655]
 [0.20308209 0.79691791]
 [0.38250602 0.61749398]
 [0.26108354 0.73891646]
 [0.14501108 0.85498892]
 [0.43439717 0.56560283]
 [0.23183829 0.76816171]
 [0.09368062 0.90631938]
 [0.09751577 0.90248423]
 [0.33004777 0.66995223]
 [0.15528916 0.84471084]
 [0.19075859 0.80924141]
 [0.55932818 0.44067182]
 [0.30439383 0.69560617]
 [0.07194063 0.92805937]
 [0.1403045  0.8596955 ]
 [0.30465069 0.69534931]
 [0.27188166 0.72811834]
 [0.07151803 0.92848197]
 [0.28956121 0.71043879]
 [0.30613103 0.69386897]
 [0.12361853 0.87638147]
 [0.06275497 0.93724503]
 [0.19829357 0.80170643]
 [0.36739081 0.63260919]
 [0.2120005  0.7879995 ]
 [0.07301452 0.92698548]
 [0.48359648 0.51640352]
 [0.42336532 0.57663468]
 [0.26694511 0.73305489]
 [0.0770288  0.9229712 ]]
	- oob_score_ = 0.8525641025641025

#### Importance of features
- gp_max_val_min = 0.2194310486584233
- gp_auc_min = 0.17298205820989748
- gp_auc_mean = 0.1012720312595305
- gp_max_val_mean = 0.08077433904901352
- gp_auc_max = 0.0659342249109411
- gp_max_val_max = 0.050666038532778644
- diff_auc = 0.03815995878216147
- low_power = 0.035326228721414894
- coe1[0] = 0.033717848157384725
- srmr = 0.03018593890925777
- coe1[1] = 0.02782428584222293
- hlbr = 0.02346005714796158
- high_power = 0.01603636062984598
- ac_std = 0.01018345233159244
- gp_max_val_std = 0.009865976621763443
- coe3[3] = 0.009024093548745189
- diff_std = 0.00850403013380617
- gp_auc_std = 0.00749882431832155
- gp_max_ix_max = 0.007474493850580737
- ac_auc = 0.0068488640370588634
- tdoa_max = 0.005395732395616988
- coe3[2] = 0.005377408454826855
- gp_max_val_range = 0.0047123898698424385
- ratio_max_to_9th_ave_peaks = 0.0046864856392596615
- tdoa_std = 0.0045965523145165025
- tdoa_range = 0.003737583048950172
- gp_max_ix_std = 0.0033881673778934666
- gp_auc_range = 0.002532095453000661
- ratio_max_to_10ms_ave_peaks = 0.0023302927084071037
- gp_max_ix_mean = 0.00213350172129315
- gp_max_ix_min = 0.0019896436280695826
- gp_max_ix_range = 0.0016656905602075842
- tdoa_mean = 0.0015727133683997112
- tdoa_min = 0.0007115898070137171
- coe3[0] = 0.0
- coe3[1] = 0.0

## Evaluation
cv = 8
### accuracy
- Scores = [ 0.5789473684210527, 0.631578947368421, 0.8947368421052632, 0.7368421052631579, 0.8947368421052632, 0.6666666666666666, 0.6666666666666666, 0.7222222222222222 ]
- Mean = 0.7240497076023391
- Standard deviation = 0.10875795259344005

### balanced_accuracy
- Scores = [ 0.7333333333333334, 0.675, 0.9333333333333333, 0.7416666666666667, 0.9333333333333333, 0.6964285714285714, 0.4, 0.43333333333333335 ]
- Mean = 0.6933035714285715
- Standard deviation = 0.18477223820130728

### f1
- Scores = [ 0.5, 0.46153846153846156, 0.8, 0.5454545454545454, 0.8, 0.5, 0.0, 0.0 ]
- Mean = 0.4508741258741259
- Standard deviation = 0.28814896181798444

### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 87 | 32 |
| Actual Positive | 9 | 21 |

      