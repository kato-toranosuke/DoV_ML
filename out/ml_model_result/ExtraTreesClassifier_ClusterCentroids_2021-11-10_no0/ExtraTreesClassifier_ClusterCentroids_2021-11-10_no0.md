# ExtraTreesClassifier_ClusterCentroids_2021-11-10_no0
## Constants
- CSV_PATH = ../../out/csv/
- OUTPUT_PATH = ./result/
- FEATURE_ATTRBS = ['low_power', 'high_power', 'hlbr', 'coe1[0]', 'coe1[1]', 'coe3[0]', 'coe3[1]', 'coe3[2]', 'coe3[3]', 'ratio_max_to_10ms_ave_peaks', 'ratio_max_to_9th_ave_peaks', 'ac_std', 'ac_auc', 'diff_std', 'diff_auc', 'srmr', 'gp_max_val_std', 'gp_max_val_range', 'gp_max_val_min', 'gp_max_val_max', 'gp_max_val_mean', 'gp_max_ix_std', 'gp_max_ix_range', 'gp_max_ix_min', 'gp_max_ix_max', 'gp_max_ix_mean', 'gp_auc_std', 'gp_auc_range', 'gp_auc_min', 'gp_auc_max', 'gp_auc_mean', 'tdoa_std', 'tdoa_range', 'tdoa_min', 'tdoa_max', 'tdoa_mean']
- LABEL_ATTRB = ['dov_angle']
- FACING_DOV_ANGLES = [0, 45, 315]
- NCV = 10
- SCORING = ['accuracy', 'balanced_accuracy', 'f1']
- REFIT_SCORING = balanced_accuracy
- PARAM_GRID = [{'est__n_estimators': [10, 100, 500, 800, 1000], 'est__min_samples_split': [2, 5, 10], 'est__min_samples_leaf': [1, 5, 10], 'est__max_features': ['sqrt', 'log2', None], 'est__bootstrap': [False], 'est__n_jobs': [-1], 'est__random_state': [42], 'est__max_samples': [0.01, 0.5, 0.09]}, {'est__n_estimators': [10, 100, 500, 800, 1000], 'est__min_samples_split': [2, 5, 10], 'est__min_samples_leaf': [1, 5, 10], 'est__max_features': ['sqrt', 'log2', None], 'est__bootstrap': [True], 'est__oob_score': [True, False], 'est__n_jobs': [-1], 'est__random_state': [42], 'est__max_samples': [0.01, 0.5, 0.09]}]

## Loaded CSV
- features_mono_ch_python.csv

## Estimator
### Type
- resampler = ClusterCentroids
- estimator = ExtraTreesClassifier

### Arguments for hyperparameter search
- resampler = ClusterCentroids
- estimator = ExtraTreesClassifier
- param_grid = 
	- {'est__n_estimators': [10, 100, 500, 800, 1000], 'est__min_samples_split': [2, 5, 10], 'est__min_samples_leaf': [1, 5, 10], 'est__max_features': ['sqrt', 'log2', None], 'est__bootstrap': [False], 'est__n_jobs': [-1], 'est__random_state': [42], 'est__max_samples': [0.01, 0.5, 0.09]}
	- {'est__n_estimators': [10, 100, 500, 800, 1000], 'est__min_samples_split': [2, 5, 10], 'est__min_samples_leaf': [1, 5, 10], 'est__max_features': ['sqrt', 'log2', None], 'est__bootstrap': [True], 'est__oob_score': [True, False], 'est__n_jobs': [-1], 'est__random_state': [42], 'est__max_samples': [0.01, 0.5, 0.09]}

- scoring = ['accuracy', 'balanced_accuracy', 'f1']
- refit = balanced_accuracy
- cv = 10

### Parameters of the best estimator
#### The best hyper-parameters
- best_resampler
	- sampling_strategy = auto
	- random_state = 42
	- estimator = None
	- voting = auto
	- n_jobs = deprecated
	- n_features_in_ = 36
	- sampling_strategy_ = OrderedDict([(0, 2160)])
	- estimator_ = KMeans(n_clusters=2160, random_state=42)
	- voting_ = soft

- best_estimator
	- base_estimator = ExtraTreeClassifier()
	- n_estimators = 500
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
	- min_samples_split = 2
	- min_samples_leaf = 1
	- min_weight_fraction_leaf = 0.0
	- max_features = log2
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
- gp_max_val_max = 0.07305710174584298
- gp_max_val_mean = 0.068839913339955
- gp_auc_mean = 0.06240039226349969
- gp_auc_max = 0.06128990548400478
- gp_max_val_min = 0.04660128153489962
- gp_auc_min = 0.043665417002651606
- gp_auc_std = 0.03775335617864545
- gp_max_val_range = 0.037394475981434076
- gp_auc_range = 0.036674773365414755
- gp_max_val_std = 0.03363412416532209
- gp_max_ix_std = 0.03225561648293081
- gp_max_ix_mean = 0.032110770755747815
- tdoa_std = 0.03155504502088724
- tdoa_mean = 0.031164003701008035
- tdoa_min = 0.028847739324646647
- gp_max_ix_min = 0.02819163383821039
- tdoa_range = 0.027444767209825638
- gp_max_ix_range = 0.02713860986624188
- tdoa_max = 0.025217504618340717
- gp_max_ix_max = 0.02515488092569242
- diff_std = 0.018728157885592837
- srmr = 0.01756243379682802
- high_power = 0.01690442664079248
- diff_auc = 0.0162238420857505
- hlbr = 0.015575423660394066
- ratio_max_to_10ms_ave_peaks = 0.015029263363592883
- ac_auc = 0.014610405405645635
- coe1[1] = 0.014396857971274763
- ratio_max_to_9th_ave_peaks = 0.014182439289929976
- low_power = 0.013533014911238614
- coe3[3] = 0.01341685963397109
- ac_std = 0.013323370830070453
- coe3[2] = 0.013071434300464091
- coe1[0] = 0.013050757419253038
- coe3[0] = 0.0
- coe3[1] = 0.0

## Evaluation
cv = 10
### accuracy
- Scores = [ 0.7899305555555556, 0.8732638888888888, 0.8819444444444444, 0.8576388888888888, 0.8680555555555556, 0.8159722222222222, 0.8541666666666666, 0.8298611111111112, 0.8802083333333334, 0.7690972222222222 ]
- Mean = 0.8420138888888887
- Standard deviation = 0.03735665762387154

### balanced_accuracy
- Scores = [ 0.8226851851851852, 0.8689814814814815, 0.8722222222222222, 0.8296296296296296, 0.8472222222222222, 0.7777777777777778, 0.8638888888888889, 0.799074074074074, 0.8652777777777778, 0.7032407407407407 ]
- Mean = 0.825
- Standard deviation = 0.05054402256187426

### f1
- Scores = [ 0.772983114446529, 0.8344671201814059, 0.8411214953271028, 0.7908163265306122, 0.812807881773399, 0.7180851063829787, 0.8227848101265824, 0.7487179487179486, 0.8345323741007193, 0.588235294117647 ]
- Mean = 0.7764551471704925
- Standard deviation = 0.07362708351808224

### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 3215 | 385 |
| Actual Positive | 525 | 1635 |

      