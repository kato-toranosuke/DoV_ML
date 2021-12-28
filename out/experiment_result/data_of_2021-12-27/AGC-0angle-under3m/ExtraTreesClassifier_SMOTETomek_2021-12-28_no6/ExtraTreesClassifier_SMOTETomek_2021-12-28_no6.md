# ExtraTreesClassifier_SMOTETomek_2021-12-28_no6
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
	- oob_decision_function_ = [[0.33773857 0.66226143]
 [0.31703281 0.68296719]
 [0.39016974 0.60983026]
 [0.45552626 0.54447374]
 [0.33351973 0.66648027]
 [0.50247988 0.49752012]
 [0.97367778 0.02632222]
 [0.96369793 0.03630207]
 [0.93601773 0.06398227]
 [0.94292561 0.05707439]
 [0.41328103 0.58671897]
 [0.89875615 0.10124385]
 [0.89135228 0.10864772]
 [0.87736849 0.12263151]
 [0.27861641 0.72138359]
 [0.35462655 0.64537345]
 [0.35379249 0.64620751]
 [0.45591334 0.54408666]
 [0.71016801 0.28983199]
 [0.88845058 0.11154942]
 [0.97511722 0.02488278]
 [0.97499083 0.02500917]
 [0.85730366 0.14269634]
 [0.83361353 0.16638647]
 [0.21104913 0.78895087]
 [0.07518879 0.92481121]
 [0.89928047 0.10071953]
 [0.95489609 0.04510391]
 [0.96279414 0.03720586]
 [0.96735493 0.03264507]
 [0.97238579 0.02761421]
 [0.50172264 0.49827736]
 [0.48190341 0.51809659]
 [0.40407237 0.59592763]
 [0.41408285 0.58591715]
 [0.42665558 0.57334442]
 [0.81302914 0.18697086]
 [0.78418234 0.21581766]
 [0.95386346 0.04613654]
 [0.9489418  0.0510582 ]
 [0.74877973 0.25122027]
 [0.47553537 0.52446463]
 [0.08125335 0.91874665]
 [0.09377499 0.90622501]
 [0.52672777 0.47327223]
 [0.9347989  0.0652011 ]
 [0.8962622  0.1037378 ]
 [0.97219967 0.02780033]
 [0.98015955 0.01984045]
 [0.66943087 0.33056913]
 [0.34520911 0.65479089]
 [0.38477697 0.61522303]
 [0.18929318 0.81070682]
 [0.51211908 0.48788092]
 [0.97004174 0.02995826]
 [0.96251532 0.03748468]
 [0.95457656 0.04542344]
 [0.41767192 0.58232808]
 [0.2998238  0.7001762 ]
 [0.18702919 0.81297081]
 [0.11351826 0.88648174]
 [0.47959462 0.52040538]
 [0.29438228 0.70561772]
 [0.9703896  0.0296104 ]
 [0.96662967 0.03337033]
 [0.98293511 0.01706489]
 [0.93947732 0.06052268]
 [0.9493852  0.0506148 ]
 [0.4390187  0.5609813 ]
 [0.96429392 0.03570608]
 [0.97664651 0.02335349]
 [0.95257175 0.04742825]
 [0.5270638  0.4729362 ]
 [0.48042086 0.51957914]
 [0.28925836 0.71074164]
 [0.18803844 0.81196156]
 [0.11191759 0.88808241]
 [0.16938023 0.83061977]
 [0.18668034 0.81331966]
 [0.19242772 0.80757228]
 [0.31302956 0.68697044]
 [0.53539612 0.46460388]
 [0.06927787 0.93072213]
 [0.07901901 0.92098099]
 [0.31932496 0.68067504]
 [0.32438748 0.67561252]
 [0.33330102 0.66669898]
 [0.07339868 0.92660132]
 [0.28038422 0.71961578]
 [0.35790812 0.64209188]
 [0.0611884  0.9388116 ]
 [0.2744374  0.7255626 ]
 [0.4004131  0.5995869 ]
 [0.06180362 0.93819638]
 [0.30660179 0.69339821]
 [0.07829731 0.92170269]
 [0.34902196 0.65097804]
 [0.26711816 0.73288184]
 [0.17429351 0.82570649]
 [0.0822291  0.9177709 ]
 [0.42144393 0.57855607]
 [0.18655581 0.81344419]
 [0.07663445 0.92336555]
 [0.11554378 0.88445622]
 [0.1947535  0.8052465 ]
 [0.24673255 0.75326745]
 [0.43112106 0.56887894]
 [0.43409174 0.56590826]
 [0.05518046 0.94481954]
 [0.18502128 0.81497872]
 [0.26480654 0.73519346]
 [0.32276586 0.67723414]
 [0.09870306 0.90129694]
 [0.36896392 0.63103608]
 [0.13059968 0.86940032]
 [0.07834159 0.92165841]
 [0.37446872 0.62553128]
 [0.06916531 0.93083469]
 [0.49985014 0.50014986]
 [0.07757437 0.92242563]]
	- oob_score_ = 0.8583333333333333

#### Importance of features
- gp_auc_min = 0.18028310944228393
- gp_max_val_min = 0.1349553149318766
- gp_max_val_mean = 0.09551291314210901
- gp_auc_max = 0.08724682121592672
- srmr = 0.082344464587849
- coe1[0] = 0.07881890816114957
- gp_max_val_max = 0.07343977024217031
- coe1[1] = 0.05062821998475898
- gp_auc_mean = 0.05022862274591375
- low_power = 0.028019881306134965
- ac_std = 0.02797243477759428
- diff_auc = 0.018890372753729526
- hlbr = 0.017752936679305324
- diff_std = 0.0173985825608237
- gp_max_val_std = 0.016239111769958216
- high_power = 0.009370742106367506
- gp_auc_range = 0.00563079930850688
- gp_max_val_range = 0.00561972091870439
- coe3[2] = 0.004252556636967836
- tdoa_range = 0.0038122408351386515
- gp_max_ix_mean = 0.002431124237524934
- gp_max_ix_std = 0.002155953791180109
- tdoa_std = 0.0018871808189815562
- ratio_max_to_10ms_ave_peaks = 0.0018670127795527168
- ratio_max_to_9th_ave_peaks = 0.0017887376021766684
- gp_max_ix_range = 0.0010474669100867195
- tdoa_max = 0.0003647762895411783
- gp_max_ix_min = 4.022346368715154e-05
- coe3[0] = 0.0
- coe3[1] = 0.0
- coe3[3] = 0.0
- ac_auc = 0.0
- gp_max_ix_max = 0.0
- gp_auc_std = 0.0
- tdoa_min = 0.0
- tdoa_mean = 0.0

## Evaluation
cv = 8
### accuracy
- Scores = [ 0.5263157894736842, 0.631578947368421, 0.9473684210526315, 0.631578947368421, 0.8947368421052632, 0.6111111111111112, 0.7777777777777778, 0.6666666666666666 ]
- Mean = 0.7108918128654971
- Standard deviation = 0.1381825490858307

### balanced_accuracy
- Scores = [ 0.6083333333333334, 0.675, 0.9666666666666667, 0.675, 0.9333333333333333, 0.6607142857142857, 0.7333333333333334, 0.4 ]
- Mean = 0.706547619047619
- Standard deviation = 0.16864157304392696

### f1
- Scores = [ 0.39999999999999997, 0.46153846153846156, 0.888888888888889, 0.46153846153846156, 0.8, 0.46153846153846156, 0.5, 0.0 ]
- Mean = 0.4966880341880342
- Standard deviation = 0.25139229422940823

### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 84 | 35 |
| Actual Positive | 8 | 22 |

      