# -*- coding: utf-8 -*-
"""scoring credit.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1omxpHiPypo4qmCz3EZ_lYriI6iAdj51E
"""

from google.colab import drive
drive.mount('/content/drive')

import warnings
warnings.filterwarnings('ignore')
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

print('Numpy Version:', np.__version__)
print('Pandas Version:', pd.__version__)
print('Seaborn Version:', sns.__version__)

from matplotlib import rcParams
rcParams['figure.figsize'] = 12, 4
rcParams['lines.linewidth'] = 3
rcParams['xtick.labelsize'] = 'x-large'
rcParams['ytick.labelsize'] = 'x-large'

df = pd.read_csv('/content/drive/My Drive/Virtual Internship - IDX Partners - Scoring Credit/loan_data_2007_2014.csv')

#df = pd.read_csv('loan_data_2007_2014.csv')

df

df1=pd.read_excel('LCDataDictionary.xlsx')

df1

"""## EDA"""

df.head()

df.info()

df.select_dtypes(include='object').describe().T

cats=['term','grade','sub_grade','emp_title','emp_length','home_ownership','verification_status','issue_d','loan_status','pymnt_plan','url','desc','purpose','title','zip_code','addr_state','earliest_cr_line','initial_list_status','last_pymnt_d','next_pymnt_d','last_credit_pull_d','application_type']

df.select_dtypes(include=np.number).describe().T

nums=['Unnamed: 0','id','member_id','loan_amnt','funded_amnt','funded_amnt_inv','int_rate','installment','annual_inc','dti','delling_2yrs','inq_last_6mths','mths_since_last_delinq','mths_since_last_record','open_acc','pub_rec','revol_bal','revol_util','total_acc','out_prncp','out_prncp_inv','total_pymnt','total_pymnt_inv','total_rec_prncp','total_rec_int',
      'total_rec_late_fee','recoveries','collection_recovery_fee','last_pymnt_amnt','collections_12_mths_ex_med','mths_since_last_major_derog','policy_code','annual_inc_joint','dti_joint','verification_status_joint','acc_now_delinq','tot_coll_amt','tot_cur_bal','open_acc_6m','open_il_6m','open_il_12m','open_il_24m','mths_since_rcnt_il','total_bal_il','il_util','open_rv_12m',
      'open_rv_24m','max_bal_bc','all_util','total_rev_hi_lim','inq_fi','total_cu_tl','inq_last_12m']

cats=['term','grade','sub_grade','emp_title','emp_length','home_ownership','verification_status','issue_d','loan_status','pymnt_plan','url','desc','purpose','title','zip_code','addr_state','earliest_cr_line','initial_list_status','last_pymnt_d','next_pymnt_d','last_credit_pull_d','application_type']
nums=['Unnamed: 0','id','member_id','loan_amnt','funded_amnt','funded_amnt_inv','int_rate','installment','annual_inc','dti','delinq_2yrs','inq_last_6mths','mths_since_last_delinq','mths_since_last_record','open_acc','pub_rec','revol_bal','revol_util','total_acc','out_prncp','out_prncp_inv','total_pymnt','total_pymnt_inv','total_rec_prncp','total_rec_int',
      'total_rec_late_fee','recoveries','collection_recovery_fee','last_pymnt_amnt','collections_12_mths_ex_med','mths_since_last_major_derog','policy_code','annual_inc_joint','dti_joint','verification_status_joint','acc_now_delinq','tot_coll_amt','tot_cur_bal','open_acc_6m','open_il_6m','open_il_12m','open_il_24m','mths_since_rcnt_il','total_bal_il','il_util','open_rv_12m',
      'open_rv_24m','max_bal_bc','all_util','total_rev_hi_lim','inq_fi','total_cu_tl','inq_last_12m']

features=nums
plt.figure(figsize=(30,25))
for i in range (0, len(features)):
    plt.subplot(10,6,i+1)
    sns.boxplot(y=df[features[i]], color='blue', orient='v')
    plt.tight_layout()

df['loan_status'].value_counts()

sns.countplot(y=df['loan_status'])
plt.savefig('Loan_status.jpg')

"""approved= Fully Paid
reject= Charged Off , Does not meet the credit policy Sattus:Charged Off , Default, Does not meet the credit policy Status:Fully Paid
still being considered = Current, Late (31-120 days), In Grace Period, Late (16-30 days)
"""

good = ['Fully Paid']
bad = ['Charged Off' , 'Does not meet the credit policy. Status:Charged Off' , 'Default','Does not meet the credit policy. Status:Fully Paid']

def loan(status):
    if status in bad:
        return 0
    return 1

df2=df[df['loan_status'].isin(good+bad)].copy()

df2['loan_status'].value_counts()

df2['loan_status']=df2['loan_status'].apply(loan)

df2['loan_status'].value_counts()

df2

df2.info()

"""cats=['term','grade','sub_grade','emp_title','emp_length','home_ownership','verification_status','issue_d','loan_status','pymnt_plan','url','desc','purpose','title','zip_code','addr_state','earliest_cr_line','initial_list_status','last_pymnt_d','next_pymnt_d','last_credit_pull_d','application_type']

nums=['Unnamed: 0','id','member_id','loan_amnt','funded_amnt','funded_amnt_inv','int_rate','installment','annual_inc','dti','delling_2yrs','inq_last_6mths','mths_since_last_delinq','mths_since_last_record','open_acc','pub_rec','revol_bal','revol_util','total_acc','out_prncp','out_prncp_inv','total_pymnt','total_pymnt_inv','total_rec_prncp','total_rec_int',
      'total_rec_late_fee','recoveries','collection_recovery_fee','last_pymnt_amnt','collections_12_mths_ex_med','mths_since_last_major_derog','policy_code','annual_inc_joint','dti_joint','verification_status_joint','acc_now_delinq','tot_coll_amt','tot_cur_bal','open_acc_6m','open_il_6m','open_il_12m','open_il_24m','mths_since_rcnt_il','total_bal_il','il_util','open_rv_12m',
      'open_rv_24m','max_bal_bc','all_util','total_rev_hi_lim','inq_fi','total_cu_tl','inq_last_12m']
"""

cats1 = ['term','grade','sub_grade','home_ownership','verification_status','pymnt_plan','purpose','title']

sns.countplot(x=df2['loan_status'])
plt.savefig('Status.jpg')

sns.countplot(y=df2['purpose'])
plt.savefig('purpose.jpg')

newpalette=['#FFABE1','#937DC2']

sns.countplot(x='term', data=df2, hue='loan_status', palette=newpalette)
plt.tight_layout()
plt.savefig('term.jpg')

sns.countplot(x='grade', data=df2, hue='loan_status', palette=newpalette)
plt.tight_layout()
plt.savefig('grade.jpg')

sns.countplot(y='sub_grade', data=df2, hue='loan_status', palette=newpalette)
plt.tight_layout()

sns.countplot(x='home_ownership', data=df2, hue='loan_status', palette=newpalette)
plt.tight_layout()
plt.savefig('own.jpg')

sns.countplot(x='pymnt_plan', data=df2, hue='loan_status', palette=newpalette)
plt.tight_layout()

sns.countplot(y='purpose', data=df2, hue='loan_status', palette=newpalette)
plt.tight_layout()
plt.savefig('purpose_loan.jpg')

nums1 = ['loan_amnt','funded_amnt','funded_amnt_inv','int_rate','installment','annual_inc','inq_last_6mths','mths_since_last_delinq','mths_since_last_record','open_acc','total_acc','total_rec_prncp']

features = nums1
plt.figure(figsize=(20, 25))
for i in range(0, len(features)):
    plt.subplot(12, 1, i+1) 
    sns.histplot(x=features[i], data=df2,  palette="seismic", hue="loan_status")
    #plt.xlabel(features[i])
    plt.tight_layout()

color=['#319DA0','#FFD39A']

sns.histplot(x='loan_amnt', data=df2, palette=color, hue='loan_status')
plt.tight_layout()
plt.savefig('loanamnt.jpg')

sns.histplot(x='int_rate', data=df2, palette=color, hue='loan_status')
plt.tight_layout()
plt.savefig('intrate.jpg')

sns.histplot(x='installment', data=df2, palette=color, hue='loan_status')
plt.tight_layout()
plt.savefig('install.jpg')

sns.histplot(x='funded_amnt', data=df2, palette=color, hue='loan_status')
plt.tight_layout()
plt.savefig('funded.jpg')

"""## Data Preprocessing"""

df2.info()

df3=df2.drop(columns=(['Unnamed: 0','id','member_id']))

df3

cats=['term','grade','sub_grade','emp_title','emp_length','home_ownership','verification_status','issue_d','loan_status','pymnt_plan','url','desc','purpose','title','zip_code','addr_state','earliest_cr_line','initial_list_status','last_pymnt_d','next_pymnt_d','last_credit_pull_d','application_type']
nums=['Unnamed: 0','id','member_id','loan_amnt','funded_amnt','funded_amnt_inv','int_rate','installment','annual_inc','dti','delinq_2yrs','inq_last_6mths','mths_since_last_delinq','mths_since_last_record','open_acc','pub_rec','revol_bal','revol_util','total_acc','out_prncp','out_prncp_inv','total_pymnt','total_pymnt_inv','total_rec_prncp','total_rec_int',
      'total_rec_late_fee','recoveries','collection_recovery_fee','last_pymnt_amnt','collections_12_mths_ex_med','mths_since_last_major_derog','policy_code','annual_inc_joint','dti_joint','verification_status_joint','acc_now_delinq','tot_coll_amt','tot_cur_bal','open_acc_6m','open_il_6m','open_il_12m','open_il_24m','mths_since_rcnt_il','total_bal_il','il_util','open_rv_12m',
      'open_rv_24m','max_bal_bc','all_util','total_rev_hi_lim','inq_fi','total_cu_tl','inq_last_12m']

cats=['term','grade','sub_grade','emp_title','emp_length','home_ownership','verification_status','issue_d','loan_status','pymnt_plan','url','desc','purpose','title','zip_code','addr_state','earliest_cr_line','initial_list_status','last_pymnt_d','next_pymnt_d','last_credit_pull_d','application_type']
for col in cats:
  print(f'''Value count kolom {col}:''')
  print(df3[col].value_counts())
  print()

nums=['loan_amnt','funded_amnt','funded_amnt_inv','int_rate','installment','annual_inc','dti','delinq_2yrs','inq_last_6mths','mths_since_last_delinq','mths_since_last_record','open_acc','pub_rec','revol_bal','revol_util','total_acc','out_prncp','out_prncp_inv','total_pymnt','total_pymnt_inv','total_rec_prncp','total_rec_int',
      'total_rec_late_fee','recoveries','collection_recovery_fee','last_pymnt_amnt','collections_12_mths_ex_med','mths_since_last_major_derog','policy_code','annual_inc_joint','dti_joint','verification_status_joint','acc_now_delinq','tot_coll_amt','tot_cur_bal','open_acc_6m','open_il_6m','open_il_12m','open_il_24m','mths_since_rcnt_il','total_bal_il','il_util','open_rv_12m',
      'open_rv_24m','max_bal_bc','all_util','total_rev_hi_lim','inq_fi','total_cu_tl','inq_last_12m']
for col in nums:
  print(f'''Value count kolom {col}:''')
  print(df3[col].value_counts())
  print()

df3['terms']=df3['term'].str.replace(' months',' ')
df3['terms']=df3['terms'].astype('float')

df3['terms'].unique()

df3['emp_length'].unique()

df3['emp_length'] = df3['emp_length'].str.replace('\+ years', '')
df3['emp_length'] = df3['emp_length'].str.replace('< 1 year', str(0))
df3['emp_length'] = df3['emp_length'].str.replace(' years', '')
df3['emp_length'] = df3['emp_length'].str.replace(' year', '')

df3['emp_length']=df3['emp_length'].astype('float')

df3['emp_length'].unique()

df3['issue_d'].unique()

df3['issue_d_date']= pd.to_datetime(df3['issue_d'],format='%b-%y')

df3['issue_d_date'].head()

df3['month_issue_d']=round((pd.to_datetime('2019-12-01')-df3['issue_d_date'])/np.timedelta64(1,'M'),2)

df3['month_issue_d']

df3['earliest_cr_line_date']= pd.to_datetime(df3['earliest_cr_line'], format='%b-%y')

df3['earliest_cr_line_months']=round((pd.to_datetime('2019-12-01')-df3['earliest_cr_line_date'])/np.timedelta64(1,'M'),2)

df3['earliest_cr_line_months']

df3['earliest_cr_line_months'].describe()

df3.info()

df3['last_credit_pull_d_date']= pd.to_datetime(df3['last_credit_pull_d'], format='%b-%y')

df3['last_credit_pull_d_months']=round((pd.to_datetime('2019-12-01')-df3['last_credit_pull_d_date'])/np.timedelta64(1,'M'),2)

df3['last_credit_pull_d_months'].head()

df3['next_pymnt_d'].value_counts()

df3['next_pymnt_d_date']= pd.to_datetime(df3['next_pymnt_d'], format='%b-%y')

df3['next_pymnt_d_months']=round((pd.to_datetime('2019-12-01')-df3['next_pymnt_d_date'])/np.timedelta64(1,'M'),2)

df3['next_pymnt_d_months'].value_counts()

df3['last_pymnt_d_date']= pd.to_datetime(df3['last_pymnt_d'], format='%b-%y')

df3['last_pymnt_d_months']=round((pd.to_datetime('2019-12-01')-df3['last_pymnt_d_date'])/np.timedelta64(1,'M'),2)

df3['last_pymnt_d_months'].head()

df3.info()

df4=df3.drop(columns=(['term','issue_d_date','earliest_cr_line_date','next_pymnt_d_date','last_credit_pull_d_date','last_pymnt_d_date',
                      'issue_d','url','desc','title','zip_code','addr_state','last_pymnt_d','next_pymnt_d','last_credit_pull_d',
                      'annual_inc_joint','dti_joint','verification_status_joint','open_acc_6m','open_il_6m','open_il_12m','open_il_24m',
                      'mths_since_rcnt_il','total_bal_il','il_util','open_rv_12m','open_rv_24m','max_bal_bc','all_util','inq_fi',
                      'total_cu_tl','inq_last_12m','policy_code','sub_grade']))

df4.info()

df4.corr()

plt.figure(figsize=(35, 35))
sns.heatmap(df4.corr(), cmap='Blues', annot=True, fmt='.2f')

corrmat = df4.corr()
top_corr_features = corrmat.index
plt.figure(figsize=(35,35))
g=sns.heatmap(df4[top_corr_features].corr(),annot=True,cmap="RdYlGn")

a = corrmat['loan_status']
hasil = a[(a>0.7)|(a<-0.7)]
hasil

df4.select_dtypes(include='object').nunique()

df4.select_dtypes(exclude='object').nunique()

df5=df4.drop(columns=['mths_since_last_record','mths_since_last_major_derog','next_pymnt_d_months','emp_title','earliest_cr_line','application_type'])

df5.isna().sum()

df5.select_dtypes(include='object').describe().T

df5.select_dtypes(include=np.number).describe().T

df5['emp_length']=df5['emp_length'].fillna(df5['emp_length'].mean())
df5['mths_since_last_delinq']=df5['mths_since_last_delinq'].fillna(df5['mths_since_last_delinq'].median())
df5['annual_inc']=df5['annual_inc'].fillna(df5['annual_inc'].median())
df5['delinq_2yrs']=df5['delinq_2yrs'].fillna(df5['delinq_2yrs'].median())
df5['inq_last_6mths']=df5['inq_last_6mths'].fillna(df5['inq_last_6mths'].mean())
df5['open_acc']=df5['open_acc'].fillna(df5['open_acc'].mean())
df5['pub_rec']=df5['pub_rec'].fillna(df5['pub_rec'].mean())
df5['revol_util']=df5['revol_util'].fillna(df5['revol_util'].median())
df5['total_acc']=df5['total_acc'].fillna(df5['total_acc'].mean())
df5['collections_12_mths_ex_med']=df5['collections_12_mths_ex_med'].fillna(df5['collections_12_mths_ex_med'].median())
df5['acc_now_delinq']=df5['acc_now_delinq'].fillna(df5['acc_now_delinq'].mean())
df5['tot_coll_amt']=df5['tot_coll_amt'].fillna(df5['tot_coll_amt'].median())
df5['tot_cur_bal']=df5['tot_cur_bal'].fillna(df5['tot_cur_bal'].median())
df5['total_rev_hi_lim']=df5['total_rev_hi_lim'].fillna(df5['total_rev_hi_lim'].median())
df5['earliest_cr_line_months']=df5['earliest_cr_line_months'].fillna(df5['earliest_cr_line_months'].median())
df5['last_credit_pull_d_months']=df5['last_credit_pull_d_months'].fillna(df5['last_credit_pull_d_months'].mean())
df5['last_pymnt_d_months']=df5['last_pymnt_d_months'].fillna(df5['last_pymnt_d_months'].median())

df5.isna().sum()

df5.duplicated().sum()

df5.select_dtypes(include='object').describe().T

df5['grade'].value_counts()

mapping_grade={'A':1,'B':2,'C':3,'D':4,'E':5,'F':6,'G':8}
df5['grade']=df5['grade'].map(mapping_grade)

df5.info()

df5['verification_status'].value_counts()

mapping_verif={'Verified':1,'Not Verified':2,'Source Verified':3}
df5['verification_status']=df5['verification_status'].map(mapping_verif)

df5.info()

df5['initial_list_status'].value_counts()

mapping_status={'f':1,'w':2}
df5['initial_list_status']=df5['initial_list_status'].map(mapping_status)

df5.info()

df5['pymnt_plan'].value_counts()

mapping_plan={'n':1,'y':2}
df5['pymnt_plan']=df5['pymnt_plan'].map(mapping_plan)

df5.info()

one_hots=['home_ownership','purpose']
for one_hots in ['home_ownership','purpose']:
    onehots= pd.get_dummies(df5[one_hots], prefix=one_hots)
    df5=df5.join(onehots)

df5.info()

df5=df5.drop(columns=['home_ownership','purpose'])

df5.info()

from sklearn.preprocessing import MinMaxScaler

df_norm = (df5-df5.min())/(df5.max()-df5.min())
df_norm

df_norm.info()

"""### Split Data"""

df_norm.info()

df_norm['loan_status'].value_counts()

from sklearn.model_selection import train_test_split

x = df_norm.drop('loan_status', axis=1)
y = df_norm['loan_status']

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=0)

x_data= df_norm.drop('loan_status', axis=1)
y_data= df_norm['loan_status']

x_data

y_data

x_train.shape, x_test.shape

"""## Modelling and Evaluation"""

from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score

def eval_classification(model):
    y_pred = model.predict(x_test)
    print("Accuracy (Test Set): %.2f" % accuracy_score(y_test, y_pred))
    print("Precision (Test Set): %.2f" % precision_score(y_test, y_pred))
    print("Recall (Test Set): %.2f" % recall_score(y_test, y_pred))
    print("F1-Score (Test Set): %.2f" % f1_score(y_test, y_pred))
    print('AUC:'+ str(roc_auc_score(y_test, y_pred)))

def show_feature_importance(model):
    feat_importances = pd.Series(model.feature_importances_, index=x.columns)
    ax = feat_importances.nlargest(25).plot(kind='barh', figsize=(10, 8))
    ax.invert_yaxis()

    plt.xlabel('score')
    plt.ylabel('feature')
    plt.title('feature importance score')

def show_best_hyperparameter(model, hyperparameters):
    for key, value in hyperparameters.items() :
        print('Best '+key+':', model.get_params()[key])

"""### Logistic Regression"""

from sklearn.linear_model import LogisticRegression
lr = LogisticRegression(random_state=0)
lr.fit(x_train, y_train)

eval_classification(lr)

print('Train score: ' + str(lr.score(x_train, y_train)))
print('Test score: ' + str(lr.score(x_test, y_test)))

from sklearn.model_selection import RandomizedSearchCV, GridSearchCV

# List Hyperparameters yang akan diuji
solver = ['newton-cg', 'lbfgs', 'liblinear']
penalty = ['l2','l1', 'elasticnet', 'none']
C = [100, 10, 1.0, 0.1, 0.01, 0.001, 0.0001]
hyperparameters = dict(penalty=penalty, C=C, solver=solver )

# Inisiasi model
logres = LogisticRegression(random_state=0)
lr_tuned = RandomizedSearchCV(logres, hyperparameters, cv=5, random_state=0, scoring='recall')

# Fitting Model & Evaluation
lr_tuned.fit(x_train, y_train)
eval_classification(lr_tuned)

logres = LogisticRegression(penalty='l2', C=0.0001, solver='lbfgs', random_state=0)
logres.fit(x_train, y_train)
y_pred = logres.predict(x_test)
print (y_pred)

import math

feature_names = x_train.columns.to_list()

#Get the scores
score = logres.score(x_train.values, y_train)
print(score)
w0 = logres.intercept_[0]
w = logres.coef_[0]

feature_importance = pd.DataFrame(feature_names, columns = ['feature'])
feature_importance['importance'] = pow(math.e, w)
feature_importance = feature_importance.sort_values(by=['importance'],ascending=False)
feature_importance = feature_importance[:8].sort_values(by=['importance'], ascending=False)

#Visualization
ax = feature_importance.sort_values(by=['importance'], ascending=True).plot.barh(x='feature', y='importance')

plt.title('Important Feature')
plt.show()

"""### Decision Tree"""

from sklearn.tree import DecisionTreeClassifier
dt = DecisionTreeClassifier(random_state=0)
dt.fit(x_train, y_train)

eval_classification(dt)

print('Train score: ' + str(dt.score(x_train, y_train)))
print('Test score:' + str(dt.score(x_test, y_test)))

from sklearn.model_selection import RandomizedSearchCV
from scipy.stats import uniform
import numpy as np

# List of hyperparameter
max_depth = [int(x) for x in np.linspace(1, 110, num = 30)] # Maximum number of levels in tree
min_samples_split = [2, 5, 10, 100] # Minimum number of samples required to split a node
min_samples_leaf = [1, 2, 4, 10, 20, 50] # Minimum number of samples required at each leaf node
max_features = ['auto', 'sqrt'] # Number of features to consider at every split

hyperparameters = dict(max_depth=max_depth, 
                       min_samples_split=min_samples_split, 
                       min_samples_leaf=min_samples_leaf,
                       max_features=max_features
                      )

# Inisialisasi Model
dt = DecisionTreeClassifier(random_state=0)
dt_tuned = RandomizedSearchCV(dt, hyperparameters, cv=5, random_state=0, scoring='precision')
dt_tuned.fit(x_train, y_train)

# Predict & Evaluation
eval_classification(dt_tuned)

# plt.figsize(10, 8)
feat_importances = pd.Series(dt_tuned.best_estimator_.feature_importances_, index=x_train.columns)
ax = feat_importances.nlargest(25).plot(kind='barh', figsize=(10, 8))
ax.invert_yaxis()

plt.xlabel('score')
plt.ylabel('feature')
plt.title('feature importance score')



"""### XGBoost"""

from xgboost import XGBClassifier
xg = XGBClassifier(random_state=0)
xg.fit(x_train, y_train)

eval_classification(xg)

print('Train score: ' + str(xg.score(x_train, y_train)))
print('Test score:' + str(xg.score(x_test, y_test)))

show_feature_importance(xg)

from sklearn.model_selection import RandomizedSearchCV, GridSearchCV
import numpy as np

#Menjadikan ke dalam bentuk dictionary
hyperparameters = {
                    'max_depth' : [int(x) for x in np.linspace(10, 110, num = 11)],
                    'min_child_weight' : [int(x) for x in np.linspace(1, 20, num = 11)],
                    'gamma' : [float(x) for x in np.linspace(0, 1, num = 11)],
                    'tree_method' : ['auto', 'exact', 'approx', 'hist'],

                    'colsample_bytree' : [float(x) for x in np.linspace(0, 1, num = 11)],
                    'eta' : [float(x) for x in np.linspace(0, 1, num = 100)],

                    'lambda' : [float(x) for x in np.linspace(0, 1, num = 11)],
                    'alpha' : [float(x) for x in np.linspace(0, 1, num = 11)]
                    }

# Init
xg = XGBClassifier(random_state=42)
xg_tuned = RandomizedSearchCV(xg, hyperparameters, cv=5, random_state=42, scoring='recall')
xg_tuned.fit(x_train, y_train)

# Predict & Evaluation
eval_classification(xg_tuned)

# plt.figsize(10, 8)
feat_importances = pd.Series(xg_tuned.best_estimator_.feature_importances_, index=x_train.columns)
ax = feat_importances.nlargest(25).plot(kind='barh', figsize=(10, 8))
ax.invert_yaxis()

plt.xlabel('score')
plt.ylabel('feature')
plt.title('feature importance score')

from xgboost import XGBClassifier
xg1 = XGBClassifier(random_state=0)
xg1.fit(x_test, y_test)

eval_classification(xg1)

show_feature_importance(xg1)

from xgboost import XGBClassifier

xg.fit(x_test,y_test)
y_pred_proba = xg.predict_proba(x_test)[:][:,1]

df_actual_predicted = pd.concat([pd.DataFrame(np.array(y_test), columns=['y_actual']), pd.DataFrame(y_pred_proba, columns=['y_pred_proba'])], axis=1)
df_actual_predicted.index = y_test.index

df_actual_predicted

from sklearn.metrics import roc_curve, roc_auc_score

fpr, tpr, tr = roc_curve(df_actual_predicted['y_actual'], df_actual_predicted['y_pred_proba'])
auc = roc_auc_score(df_actual_predicted['y_actual'], df_actual_predicted['y_pred_proba'])

plt.plot(fpr, tpr, label='AUC = %0.4f' %auc)
plt.plot(fpr, fpr, linestyle = '--', color='k')
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('ROC Curve')
plt.legend()
plt.savefig('roc.jpg')

from sklearn.metrics import confusion_matrix

#Generate the confusion matrix
y_pred = xg.predict(x_test)
cf_matrix = confusion_matrix(y_test, y_pred)

print(cf_matrix)

group_names = ['True Negative','False Positive','False Negative','True Positive']
group_counts = ["{0:0.0f}".format(value) for value in
cf_matrix.flatten()]
group_percentages = ["{0:.2%}".format(value) for value in
cf_matrix.flatten()/np.sum(cf_matrix)]
labels = [f"{v1}\n{v2}\n{v3}" for v1, v2, v3 in
zip(group_names,group_counts,group_percentages)]
labels = np.asarray(labels).reshape(2,2)
ax = sns.heatmap(cf_matrix, annot=labels, fmt='', cmap='Blues')
ax.set_title('Confusion Matrix\n');
ax.set_xlabel('\nPredicted Values')
ax.set_ylabel('Actual Values ');
## Ticket labels - List must be in alphabetical order
ax.xaxis.set_ticklabels(['False','True'])
ax.yaxis.set_ticklabels(['False','True'])
## Display the visualization of the Confusion Matrix.
plt.show()
plt.savefig('confusionmatrix.jpg')



