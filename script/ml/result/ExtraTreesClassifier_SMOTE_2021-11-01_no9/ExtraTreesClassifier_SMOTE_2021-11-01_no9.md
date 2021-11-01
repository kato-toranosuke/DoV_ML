# ExtraTreesClassifier_SMOTE_2021-11-01_no9
## Constants
- CSV_PATH = ../../out/csv/
- OUTPUT_PATH = ./result/
- FEATURE_ATTRBS = ['low_power', 'high_power', 'hlbr', 'coe1[0]', 'coe1[1]', 'coe3[0]', 'coe3[1]', 'coe3[2]', 'coe3[3]', 'ratio_max_to_10ms_ave_peaks', 'ratio_max_to_9th_ave_peaks', 'ac_std', 'ac_auc', 'diff_std', 'diff_auc', 'srmr', 'gp_max_val_std', 'gp_max_val_range', 'gp_max_val_min', 'gp_max_val_max', 'gp_max_val_mean', 'gp_max_ix_std', 'gp_max_ix_range', 'gp_max_ix_min', 'gp_max_ix_max', 'gp_max_ix_mean', 'gp_auc_std', 'gp_auc_range', 'gp_auc_min', 'gp_auc_max', 'gp_auc_mean', 'tdoa_std', 'tdoa_range', 'tdoa_min', 'tdoa_max', 'tdoa_mean']
- LABEL_ATTRB = ['dov_angle']
- FACING_DOV_ANGLES = [0, 45, 315]
- NCV = 10
- SCORING = ['accuracy', 'balanced_accuracy', 'f1']
- REFIT_SCORING = balanced_accuracy
- PARAM_GRID = [{'est__n_estimators': [10], 'est__min_samples_split': [2], 'est__min_samples_leaf': [5], 'est__max_features': [None], 'est__bootstrap': [False], 'est__n_jobs': [-1], 'est__random_state': [42], 'est__max_samples': [0.5]}]

## Loaded CSV
- features_mono_ch_python.csv

## Estimator
### Type
- resampler = SMOTE
- estimator = ExtraTreesClassifier

### Arguments for hyperparameter search
- resampler = SMOTE
- estimator = ExtraTreesClassifier
- param_grid = 
	- {'est__n_estimators': [10], 'est__min_samples_split': [2], 'est__min_samples_leaf': [5], 'est__max_features': [None], 'est__bootstrap': [False], 'est__n_jobs': [-1], 'est__random_state': [42], 'est__max_samples': [0.5]}

- scoring = ['accuracy', 'balanced_accuracy', 'f1']
- refit = balanced_accuracy
- cv = 10

### Parameters of the best estimator
#### The best hyper-parameters
- best_resampler
	- sampling_strategy = auto
	- random_state = 42
	- k_neighbors = 5
	- n_jobs = -1
	- n_features_in_ = 36
	- sampling_strategy_ = OrderedDict([(1, 1440)])
	- nn_k_ = NearestNeighbors(n_neighbors=6)

- best_estimator
	- base_estimator = ExtraTreeClassifier()
	- n_estimators = 10
	- estimator_params = ('criterion', 'max_depth', 'min_samples_split', 'min_samples_leaf', 'min_weight_fraction_leaf', 'max_features', 'max_leaf_nodes', 'min_impurity_decrease', 'min_impurity_split', 'random_state', 'ccp_alpha')
	- bootstrap = False
	- oob_score = False
	- n_jobs = -1
	- random_state = 42
	- verbose = 0
	- warm_start = False
	- class_weight = None
	- max_samples = 0.5
	- criterion = gini
	- max_depth = None
	- min_samples_split = 2
	- min_samples_leaf = 5
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

#### Importance of features
- gp_max_val_max = 0.19142476571301142
- gp_auc_max = 0.14060353525438446
- gp_auc_mean = 0.09167093405050059
- gp_max_val_mean = 0.09145503313959855
- gp_max_val_min = 0.0660389706744195
- gp_auc_min = 0.04051326467720452
- tdoa_min = 0.02372138259733257
- gp_max_val_std = 0.022003821306790114
- gp_max_ix_min = 0.021049345746921085
- gp_max_ix_mean = 0.020717389505983532
- gp_max_ix_range = 0.019446598869800914
- tdoa_mean = 0.018698970431775826
- tdoa_std = 0.018577043453710217
- tdoa_max = 0.017798047585572803
- gp_max_ix_std = 0.017689331758682487
- gp_auc_std = 0.016448948592133736
- gp_max_ix_max = 0.015267260338496177
- diff_auc = 0.015120283011518642
- tdoa_range = 0.014705948325998919
- ratio_max_to_10ms_ave_peaks = 0.013006430679882112
- ac_auc = 0.012708672106699664
- gp_max_val_range = 0.012025977425410414
- high_power = 0.011782028604208955
- gp_auc_range = 0.011611246584620573
- srmr = 0.01032244500499625
- ratio_max_to_9th_ave_peaks = 0.009349222428228804
- diff_std = 0.007849927544278632
- coe1[0] = 0.007652783731434303
- hlbr = 0.007500608298700376
- ac_std = 0.0073498813701169865
- coe1[1] = 0.007065590676586209
- coe3[2] = 0.006896409911678833
- low_power = 0.006201149942122733
- coe3[3] = 0.00572675065719906
- coe3[0] = 0.0
- coe3[1] = 0.0

## Evaluation
cv = 10
### accuracy
- Scores = [ 0.7881944444444444, 0.8767361111111112, 0.8524305555555556, 0.8506944444444444, 0.8506944444444444, 0.8003472222222222, 0.8298611111111112, 0.8142361111111112, 0.8871527777777778, 0.7777777777777778 ]
- Mean = 0.8328125
- Standard deviation = 0.035119686919681106

### balanced_accuracy
- Scores = [ 0.8166666666666667, 0.8662037037037037, 0.8449074074074074, 0.8194444444444444, 0.8305555555555555, 0.7560185185185185, 0.8398148148148148, 0.7847222222222222, 0.8745370370370371, 0.7138888888888889 ]
- Mean = 0.8146759259259259
- Standard deviation = 0.04749650283133626

### f1
- Scores = [ 0.7671755725190841, 0.8337236533957846, 0.8054919908466818, 0.7772020725388601, 0.7902439024390243, 0.684931506849315, 0.7949790794979079, 0.7291139240506329, 0.8456057007125891, 0.607361963190184 ]
- Mean = 0.7635829366040063
- Standard deviation = 0.06861332841301078

### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 3193 | 407 |
| Actual Positive | 557 | 1603 |

      