# ExtraTreesClassifier_NoResampler_2022-01-09_no0
## Constants
- CSV_PATH = ../out/csv/experiment
- OUTPUT_PATH = ../out/experiment_result/data_of_2022-01-07_new/AGC-0angle-under3m
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
- 2021-12-27_raspi_48000Hz_w1_N2^12_overlap80_with2022-01-07.csv

## Estimator
### Type
- resampler = NoResampler
- estimator = ExtraTreesClassifier

### Arguments for hyperparameter search
- resampler = NoResampler
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

- best_estimator
	- base_estimator = ExtraTreeClassifier()
	- n_estimators = 100
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
	- min_samples_split = 5
	- min_samples_leaf = 1
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
- gp_max_val_min = 0.12091163604155906
- gp_auc_min = 0.1155949935288609
- gp_max_val_mean = 0.08467738878248977
- gp_auc_mean = 0.06938810995004037
- gp_auc_max = 0.05525409435773958
- diff_auc = 0.051764430731360986
- high_power = 0.04113476109515637
- srmr = 0.03949004719008906
- diff_std = 0.034457857615507154
- gp_max_val_max = 0.03422150755719978
- coe1[1] = 0.03285094794706822
- ratio_max_to_9th_ave_peaks = 0.026280210162378744
- low_power = 0.023615260384667675
- coe1[0] = 0.023576309501548643
- gp_auc_std = 0.022530896898671597
- tdoa_max = 0.022432263142640827
- gp_max_ix_max = 0.021545914458947078
- coe3[3] = 0.01958210296109484
- gp_auc_range = 0.01861964010080186
- gp_max_val_range = 0.01844898714081669
- ratio_max_to_10ms_ave_peaks = 0.016495367184063938
- gp_max_val_std = 0.01648199244920019
- ac_std = 0.015926213688031543
- coe3[2] = 0.010235978369719376
- hlbr = 0.010151681468435786
- gp_max_ix_mean = 0.008076643822430816
- tdoa_range = 0.006910255534649357
- tdoa_mean = 0.006818040546570927
- ac_auc = 0.0063964786212229565
- tdoa_min = 0.0062169134206577804
- gp_max_ix_std = 0.005582967738609059
- gp_max_ix_min = 0.005471279713612202
- tdoa_std = 0.0045109503773491395
- gp_max_ix_range = 0.004347877516807814
- coe3[0] = 0.0
- coe3[1] = 0.0

## Evaluation
cv = 8
### accuracy
- Scores = [ 0.631578947368421, 0.6842105263157895, 0.8947368421052632, 0.7368421052631579, 0.8947368421052632, 0.7894736842105263, 0.7222222222222222, 0.8888888888888888 ]
- Mean = 0.7803362573099415
- Standard deviation = 0.09661782298878946

### balanced_accuracy
- Scores = [ 0.49166666666666664, 0.525, 0.8416666666666667, 0.5583333333333333, 0.75, 0.8666666666666667, 0.43333333333333335, 0.8 ]
- Mean = 0.6583333333333333
- Standard deviation = 0.1626601774661928

### f1
- Scores = [ 0.22222222222222224, 0.25, 0.75, 0.28571428571428575, 0.6666666666666666, 0.6666666666666666, 0.0, 0.6666666666666666 ]
- Mean = 0.4384920634920635
- Standard deviation = 0.26247532847863003

### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 103 | 17 |
| Actual Positive | 16 | 14 |

      