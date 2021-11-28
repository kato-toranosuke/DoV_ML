# RandomForestClassifier_NoResampler_2021-11-18_no0
## Constants
- CSV_PATH = ../../out/csv/
- OUTPUT_PATH = ./result/
- FEATURE_ATTRBS = ['low_power', 'high_power', 'hlbr', 'coe1[0]', 'coe1[1]', 'coe3[0]', 'coe3[1]', 'coe3[2]', 'coe3[3]', 'ratio_max_to_10ms_ave_peaks', 'ratio_max_to_9th_ave_peaks', 'ac_std', 'ac_auc', 'diff_std', 'diff_auc', 'srmr', 'gp_max_val_std', 'gp_max_val_range', 'gp_max_val_mean', 'gp_max_ix_std', 'gp_max_ix_range', 'gp_max_ix_mean', 'gp_auc_std', 'gp_auc_range', 'gp_auc_mean', 'tdoa_std', 'tdoa_range', 'tdoa_mean']
- LABEL_ATTRB = ['dov_angle']
- FACING_DOV_ANGLES = [0, 45, 315]
- NCV = 10
- SCORING = ['accuracy', 'balanced_accuracy', 'f1']
- REFIT_SCORING = balanced_accuracy
- PARAM_GRID = [{'est__n_estimators': range(100, 1600, 100), 'est__min_samples_split': [2, 5, 10], 'est__min_samples_leaf': [1, 5, 10], 'est__max_features': ['sqrt', 'log2', None], 'est__bootstrap': [False], 'est__n_jobs': [-1], 'est__random_state': [42], 'est__max_samples': [0.01, 0.5, 0.09]}, {'est__n_estimators': range(100, 1600, 100), 'est__min_samples_split': [2, 5, 10], 'est__min_samples_leaf': [1, 5, 10], 'est__max_features': ['sqrt', 'log2', None], 'est__bootstrap': [True], 'est__oob_score': [True, False], 'est__n_jobs': [-1], 'est__random_state': [42], 'est__max_samples': [0.01, 0.5, 0.09]}]

## Loaded CSV
- features_mono_ch_matlab.csv

## Estimator
### Type
- resampler = NoResampler
- estimator = RandomForestClassifier

### Arguments for hyperparameter search
- resampler = NoResampler
- estimator = RandomForestClassifier
- param_grid = 
	- {'est__n_estimators': range(100, 1600, 100), 'est__min_samples_split': [2, 5, 10], 'est__min_samples_leaf': [1, 5, 10], 'est__max_features': ['sqrt', 'log2', None], 'est__bootstrap': [False], 'est__n_jobs': [-1], 'est__random_state': [42], 'est__max_samples': [0.01, 0.5, 0.09]}
	- {'est__n_estimators': range(100, 1600, 100), 'est__min_samples_split': [2, 5, 10], 'est__min_samples_leaf': [1, 5, 10], 'est__max_features': ['sqrt', 'log2', None], 'est__bootstrap': [True], 'est__oob_score': [True, False], 'est__n_jobs': [-1], 'est__random_state': [42], 'est__max_samples': [0.01, 0.5, 0.09]}

- scoring = ['accuracy', 'balanced_accuracy', 'f1']
- refit = balanced_accuracy
- cv = 10

### Parameters of the best estimator
#### The best hyper-parameters
- best_resampler

- best_estimator
	- base_estimator = DecisionTreeClassifier()
	- n_estimators = 1100
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
	- min_samples_leaf = 1
	- min_weight_fraction_leaf = 0.0
	- max_features = None
	- max_leaf_nodes = None
	- min_impurity_decrease = 0.0
	- min_impurity_split = None
	- ccp_alpha = 0.0
	- n_features_in_ = 28
	- n_features_ = 28
	- n_outputs_ = 1
	- classes_ = [0 1]
	- n_classes_ = 2
	- base_estimator_ = DecisionTreeClassifier()
	- oob_decision_function_ = [[0.01501502 0.98498498]
 [0.00775194 0.99224806]
 [0.50392465 0.49607535]
 ...
 [0.96769231 0.03230769]
 [0.88549618 0.11450382]
 [0.84962406 0.15037594]]
	- oob_score_ = 0.8532986111111112

#### Importance of features
- gp_max_val_mean = 0.41268532862029905
- gp_auc_mean = 0.05707277412662133
- gp_max_val_range = 0.04826938836636286
- gp_max_val_std = 0.045611387817385975
- srmr = 0.036751728406762156
- ratio_max_to_10ms_ave_peaks = 0.03310804638263845
- ac_auc = 0.032979049812322546
- ratio_max_to_9th_ave_peaks = 0.031743571380028944
- diff_auc = 0.030644017213563964
- hlbr = 0.029037009687065955
- high_power = 0.02626290920507495
- ac_std = 0.025955305700049745
- diff_std = 0.025144332323024633
- gp_auc_range = 0.024952868264383275
- coe1[1] = 0.01755557962401744
- tdoa_mean = 0.016278576946293127
- gp_max_ix_mean = 0.016278002348252163
- low_power = 0.01467120078911029
- gp_max_ix_std = 0.01447117872612155
- tdoa_std = 0.014271471209408394
- coe3[3] = 0.013781384851713837
- gp_auc_std = 0.01125651874607614
- coe3[2] = 0.010849874136826377
- gp_max_ix_range = 0.0044332919088868866
- tdoa_range = 0.004261194924895925
- coe1[0] = 0.0016740084828138933
- coe3[0] = 0.0
- coe3[1] = 0.0

## Evaluation
cv = 10
### accuracy
- Scores = [ 0.7482638888888888, 0.9027777777777778, 0.8628472222222222, 0.8697916666666666, 0.859375, 0.7934027777777778, 0.8541666666666666, 0.8125, 0.8732638888888888, 0.7517361111111112 ]
- Mean = 0.8328125
- Standard deviation = 0.05064596473770602

### balanced_accuracy
- Scores = [ 0.7856481481481481, 0.9027777777777778, 0.8587962962962963, 0.8347222222222221, 0.8393518518518519, 0.7384259259259259, 0.8657407407407407, 0.7703703703703704, 0.8476851851851852, 0.6791666666666667 ]
- Mean = 0.8122685185185186
- Standard deviation = 0.06429695566844866

### f1
- Scores = [ 0.7358834244080145, 0.874439461883408, 0.8216704288939052, 0.8, 0.8019559902200489, 0.653061224489796, 0.8242677824267782, 0.7065217391304347, 0.8151898734177216, 0.5401929260450161 ]
- Mean = 0.7573182850915123
- Standard deviation = 0.09516137686113713

### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 3220 | 380 |
| Actual Positive | 583 | 1577 |

      