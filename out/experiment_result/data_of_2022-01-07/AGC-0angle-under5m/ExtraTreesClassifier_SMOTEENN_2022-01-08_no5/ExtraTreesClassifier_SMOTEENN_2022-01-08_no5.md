# ExtraTreesClassifier_SMOTEENN_2022-01-08_no5
## Constants
- CSV_PATH = ../out/csv/experiment
- OUTPUT_PATH = ../out/experiment_result/data_of_2022-01-07/AGC-0angle-under5m
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
- AGC_STATUS = ['AGC']

## Loaded CSV
- 2021-12-27_raspi_48000Hz_w1_N2^12_overlap80_with2022-01-07.csv

## Estimator
### Type
- resampler = SMOTEENN
- estimator = ExtraTreesClassifier

### Arguments for hyperparameter search
- resampler = SMOTEENN
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
	- enn = None
	- n_jobs = -1
	- n_features_in_ = 36
	- sampling_strategy_ = auto
	- smote_ = SMOTE(n_jobs=-1, random_state=42)
	- enn_ = EditedNearestNeighbours(n_jobs=-1, sampling_strategy='all')

- best_estimator
	- base_estimator = ExtraTreeClassifier()
	- n_estimators = 100
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
	- oob_decision_function_ = [[0.78333333 0.21666667]
 [0.98387097 0.01612903]
 [0.98275862 0.01724138]
 [0.84482759 0.15517241]
 [0.90740741 0.09259259]
 [0.50746269 0.49253731]
 [0.55882353 0.44117647]
 [0.90909091 0.09090909]
 [0.84210526 0.15789474]
 [0.51724138 0.48275862]
 [0.14516129 0.85483871]
 [0.90769231 0.09230769]
 [0.88333333 0.11666667]
 [0.9122807  0.0877193 ]
 [0.82539683 0.17460317]
 [0.83606557 0.16393443]
 [0.88888889 0.11111111]
 [0.82352941 0.17647059]
 [0.74545455 0.25454545]
 [0.27118644 0.72881356]
 [1.         0.        ]
 [1.         0.        ]
 [0.85185185 0.14814815]
 [0.96875    0.03125   ]
 [1.         0.        ]
 [0.76271186 0.23728814]
 [1.         0.        ]
 [0.96551724 0.03448276]
 [0.60655738 0.39344262]
 [1.         0.        ]
 [0.98684211 0.01315789]
 [0.71666667 0.28333333]
 [0.83606557 0.16393443]
 [1.         0.        ]
 [0.57142857 0.42857143]
 [0.60714286 0.39285714]
 [1.         0.        ]
 [1.         0.        ]
 [1.         0.        ]
 [0.6557377  0.3442623 ]
 [0.62962963 0.37037037]
 [0.68965517 0.31034483]
 [0.03571429 0.96428571]
 [0.34848485 0.65151515]
 [0.06153846 0.93846154]
 [0.01538462 0.98461538]
 [0.06666667 0.93333333]
 [0.14754098 0.85245902]
 [0.14516129 0.85483871]
 [0.03773585 0.96226415]
 [0.10447761 0.89552239]
 [0.24242424 0.75757576]
 [0.07142857 0.92857143]
 [0.01612903 0.98387097]
 [0.         1.        ]
 [0.04411765 0.95588235]
 [0.03703704 0.96296296]
 [0.01818182 0.98181818]
 [0.40384615 0.59615385]
 [0.19047619 0.80952381]
 [0.         1.        ]
 [0.41509434 0.58490566]
 [0.03225806 0.96774194]
 [0.03389831 0.96610169]
 [0.05357143 0.94642857]
 [0.04166667 0.95833333]
 [0.05084746 0.94915254]
 [0.10606061 0.89393939]
 [0.         1.        ]
 [0.         1.        ]
 [0.03703704 0.96296296]
 [0.         1.        ]
 [0.0625     0.9375    ]
 [0.03225806 0.96774194]
 [0.03703704 0.96296296]
 [0.40983607 0.59016393]
 [0.20338983 0.79661017]
 [0.03448276 0.96551724]
 [0.20833333 0.79166667]
 [0.70967742 0.29032258]
 [0.05084746 0.94915254]
 [0.01639344 0.98360656]
 [0.52941176 0.47058824]
 [0.04761905 0.95238095]
 [0.01886792 0.98113208]
 [0.         1.        ]
 [0.         1.        ]
 [0.01818182 0.98181818]]
	- oob_score_ = 0.9431818181818182

#### Importance of features
- high_power = 0.08068390085011677
- coe3[2] = 0.06365625243672114
- diff_auc = 0.052003651789693246
- gp_max_val_min = 0.048757235257850286
- gp_auc_min = 0.04504176342150009
- ac_auc = 0.04412558262738948
- tdoa_mean = 0.04106508947608924
- gp_max_val_max = 0.04031144808502533
- gp_max_ix_mean = 0.03979430475567381
- coe1[0] = 0.03933148568234705
- hlbr = 0.03811429360028742
- gp_auc_max = 0.037460704266136846
- gp_auc_mean = 0.036646053063974476
- coe3[3] = 0.03224834593963405
- tdoa_std = 0.031659077453397605
- gp_max_val_mean = 0.030548193914675698
- low_power = 0.0304007812077391
- diff_std = 0.027346191250342655
- gp_auc_std = 0.023698507407508815
- gp_max_val_std = 0.02240762702127184
- gp_auc_range = 0.021590344512528722
- srmr = 0.02000520653251825
- coe1[1] = 0.018960372100734677
- tdoa_min = 0.017353673280796178
- gp_max_val_range = 0.015552040175008499
- gp_max_ix_std = 0.01414499560518855
- ac_std = 0.013411341536848406
- gp_max_ix_max = 0.01319620220669481
- ratio_max_to_9th_ave_peaks = 0.011845630274764983
- tdoa_max = 0.010215671960998042
- gp_max_ix_range = 0.010163361810278201
- ratio_max_to_10ms_ave_peaks = 0.009925397301680213
- tdoa_range = 0.00936435256553725
- gp_max_ix_min = 0.008970920629048286
- coe3[0] = 0.0
- coe3[1] = 0.0

## Evaluation
cv = 8
### accuracy
- Scores = [ 0.6551724137931034, 0.8571428571428571, 0.7857142857142857, 0.75, 0.75, 0.8571428571428571, 0.7142857142857143, 0.7857142857142857 ]
- Mean = 0.7693965517241379
- Standard deviation = 0.06400017152442192

### balanced_accuracy
- Scores = [ 0.4746376811594203, 0.7272727272727273, 0.7424242424242424, 0.5378787878787878, 0.7196969696969697, 0.9130434782608696, 0.5130434782608696, 0.8695652173913043 ]
- Mean = 0.6871953227931489
- Standard deviation = 0.15320900769803467

### f1
- Scores = [ 0.16666666666666666, 0.6, 0.5714285714285715, 0.2222222222222222, 0.5333333333333333, 0.7142857142857143, 0.20000000000000004, 0.625 ]
- Mean = 0.4541170634920635
- Standard deviation = 0.2059084060061407

### Confusion Matrix
|  | Predicted Negative | Predicted Positive |
| --- | --- | --- |
| Actual Negative | 144 | 36 |
| Actual Positive | 18 | 27 |

      