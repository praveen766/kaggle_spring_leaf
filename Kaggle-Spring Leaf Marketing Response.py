
# coding: utf-8

# ## Kaggle-Spring Leaf Marketing Response

# #### source : https://www.kaggle.com/c/springleaf-marketing-response

# In[1]:

# importing libraries
import numpy as np
import pandas as pd
import os as os
import datetime  as dt
import calendar as cal
from __future__ import division  ### to make sure that division results in float numbers
pd.set_option('display.max_columns', None)
import time


# In[2]:

#setting the working Directory
os.chdir("/local/common/pravengs/dwpublish/MISC/Spring Leaf Marketing Response")
print os.getcwd()


# ##### Unzipping the files 
# ! unzip test.csv.zip
# <br>
# ! unzip train.csv.zip

# In[3]:

# importing train and test
train=pd.read_csv("train.csv")
test=pd.read_csv("test.csv")


# In[4]:

print train.shape , train.columns
print "\n"
print test.shape, test.columns


# In[6]:

# for finding the datatypes
sdty=set(train.dtypes)
print sdty


# In[5]:

# train
# count of categorical and non categorical columns
cat_count=int_count=float_count=0
for i in train.columns:
    if train[i].dtypes=='O':
        cat_count+=1
    if train[i].dtypes=='int64':
        int_count+=1
    if train[i].dtypes=='float64':
        float_count+=1

print "cat count " , cat_count
print "int count " , int_count
print "float count " , float_count


# In[6]:

# test
# count of categorical and non categorical columns
test_cat_count=test_int_count=test_float_count=0
for i in test.columns:
    if test[i].dtypes=='O':
        test_cat_count+=1
    if test[i].dtypes=='int64':
        test_int_count+=1
    if test[i].dtypes=='float64':
        test_float_count+=1

print "test cat count " , test_cat_count
print "test int count " , test_int_count
print "test float count " , test_float_count


# In[7]:

#Finding the levels of categorical variables in train
cat_var=[]
for i in train.columns:
    if train[i].dtypes=='O':
        print i , len(train[i].unique())
        cat_var.append((i,len(train[i].unique())))


# In[8]:

#Finding the levels of categorical variables in test
test_cat_var=[]
for i in test.columns:
    if test[i].dtypes=='O':
        print i , len(test[i].unique())
        test_cat_var.append((i,len(test[i].unique())))


# In[11]:

#Finding the levels of noncategorical variables in train
non_cat_var=[]
for i in train.columns:
    if train[i].dtypes!='O':
        #print i , len(train[i].unique())
        non_cat_var.append((i,len(train[i].unique())))


# In[12]:

# classifying the categorical variables in to binary trilevel, lowlevel and high level variables
hl_cat_var=filter(lambda (x,v) : v >=10, cat_var ) ## high level cat variable
bin_cat_var=filter(lambda (x,v) : v==2, cat_var ) ### binary level cat variable
tri_cat_var=filter(lambda (x,v) : v==3, cat_var ) ### tri level cat variable
ll_cat_var=filter(lambda (x,v) : v>3 and v<10, cat_var ) ### low level cat variables


# In[13]:

# count of differrent types of categorical variables
print len(hl_cat_var),len(ll_cat_var),len(tri_cat_var),len(bin_cat_var)


# In[14]:

bin_cat_var


# In[15]:

## binary level cat variables
for i in bin_cat_var:
    #print k, v
    print i[0]
    print train[i[0]].unique()
    print "\n"
    print train[i[0]].value_counts(dropna=False)


# In[16]:

len(bin_cat_var), bin_cat_var


# ####  all the 13 binary categorical variables have 56 missing values , which is .39% of data, the othe rlevel is 'Flase' or single value whihc does not give additional infomation. Hence the binary variables are insignificant and can be safely ignored

# In[17]:

## tri level cat variables
for i in tri_cat_var:
    #print k, v
    print i[0]
    print train[i[0]].unique()
    print "\n"
    print train[i[0]].value_counts(dropna=False)
    print "----------------------"


# In[18]:

len(tri_cat_var), tri_cat_var


# #### there are 56 NaN in all the tri level variables which has to be imputed and all the 6 tri cat vars needs to be one hot Encoded (OHE)

# In[19]:

# low level cat variables
print ll_cat_var
for i in range(len(ll_cat_var)) :
    print ll_cat_var[i][0], len(train[ll_cat_var[i][0]].unique())
    print train[ll_cat_var[i][0]].value_counts(dropna=False)
    #print train[ll_cat_var[i][0]].value_counts(dropna=False,normalize=True)


# ##### there are 918 NaNs hence need missing value treatment( replace it with not applicable) for the ll_cat_var and then do OHE

# In[17]:

## find out the high level cat variables
for i in range(len(hl_cat_var)) :
    print hl_cat_var[i][0], len(train[hl_cat_var[i][0]].unique())
    print train[hl_cat_var[i][0]].unique()[0:5]


# #### most of the high level cat variables are date variables hence need to do the following
# 1. convert the string date to datetype
# 2. find the day, month, year, dayofweek and week of year from these dates which will be used in the modelng rather than the date variables themseleves
# 
# <!-- Rough Work
# strdates=('12MAR12:00:00:00', '25FEB12:00:00:00', '22DEC11:00:00:00','08DEC09:00:00:00')
# <br>
# a = pd.Series([pd.to_datetime(date,format='%d%b%y:%H:%M:%S') for date in strdates])
# <br>
# a
# <br>
# t_train['h']=t_train['VAR_0204'].map(lambda x : str(x)[8:10])  -->

# In[18]:

# high level non date variables
hl_cat_var_non_date=['VAR_0200'
                     ,'VAR_0214'
                     ,'VAR_0237'
                     ,'VAR_0274'
                     ,'VAR_0325'
                     ,'VAR_0342'
                     ,'VAR_0404'
                     ,'VAR_0493']


# In[19]:

for i in hl_cat_var_non_date:
    print i, len(train[i].unique())


# #### from hl_cat_var_non_date variables such as VAR_0200,VAR_0404 and VAR_0493 can be excluded as they have large number of levels, while others can be OHE

# In[20]:

# high level non date low level count variables for OHE
hl_cat_var_non_date_ll=[x for x in hl_cat_var_non_date if x not in ['VAR_0200','VAR_0404', 'VAR_0493'] ]


# In[21]:

for i in hl_cat_var_non_date_ll:
    print i,len(train[i].unique())
    print train[i].value_counts(dropna=False)
    print "\n"


# #### VAR_0214  can be eliminated as it has no information and majority (14219) as NaN

# In[22]:

# high level cat date  variables 
hl_cat_var_date=[x for (x,v) in hl_cat_var if x not in hl_cat_var_non_date]


# In[23]:

hl_cat_var_date


# In[24]:

## Train
## converting the string dates in to dates and then finding the day, month, year, day of week and week of year
for i in hl_cat_var_date:
    train[i]=pd.to_datetime(train[i],format='%d%b%y:%H:%M:%S')
    train[i+'_day']= train[i].dt.day
    train[i+'_month']= train[i].dt.month
    train[i+'_year']= train[i].dt.year
    train[i+'_dow']= train[i].dt.dayofweek
    train[i+'_woy']= train[i].dt.weekofyear
    


# In[25]:

## test
## converting the string dates in to dates and then finding the day, month, year, day of week and week of year
for i in hl_cat_var_date:
    test[i]=pd.to_datetime(test[i],format='%d%b%y:%H:%M:%S')
    test[i+'_day']= test[i].dt.day
    test[i+'_month']= test[i].dt.month
    test[i+'_year']= test[i].dt.year
    test[i+'_dow']= test[i].dt.dayofweek
    test[i+'_woy']= test[i].dt.weekofyear
    


# In[26]:

## train
for i in hl_cat_var_date:
    print i
    print train[i].dtypes
    print train[i+'_day'].unique(), train[i+'_day'].dtypes
    print train[i+'_dow'].unique(),train[i+'_dow'].dtypes
    print train[i+'_year'].unique(),train[i+'_year'].dtypes
    print train[i+'_woy'].unique(),train[i+'_woy'].dtypes
    print train[i+'_month'].unique(),train[i+'_month'].dtypes
    print "\n"
    


# In[27]:

## test
for i in hl_cat_var_date:
    print i
    print test[i].dtypes
    print test[i+'_day'].unique(), test[i+'_day'].dtypes
    print test[i+'_dow'].unique(),test[i+'_dow'].dtypes
    print test[i+'_year'].unique(),test[i+'_year'].dtypes
    print test[i+'_woy'].unique(),test[i+'_woy'].dtypes
    print test[i+'_month'].unique(),test[i+'_month'].dtypes
    print "\n"
    


# <!---
# import datetime as dt
# ## converting the string dates in to dates
# for i in hl_cat_var_date:
#     t_train[i]=pd.to_datetime(t_train[i],format='%d%b%y:%H:%M:%S')
#     t_train[i+'_day']= t_train[i].dt.day
# t_train['VAR_0073'+'_day']= t_train['VAR_0073'].dt.dayofweek  --->

# In[28]:

## variables for OHE: tri_cat_var, ll_cat_var, hl_cat_var_non_date_ll except VAR_0214
train_ohe_cols=[x for (x,v) in tri_cat_var] + [x for (x,v) in ll_cat_var]+[x for x in hl_cat_var_non_date_ll if x not in ['VAR_0214']]


# In[29]:

print len(train_ohe_cols)
print len(tri_cat_var)+len(ll_cat_var)+len(hl_cat_var_non_date_ll)
print train_ohe_cols


# In[30]:

# train
#replacing the NaNs in the OHE variables with NotApp
for i in train_ohe_cols:
    train[i].fillna('NotApp',inplace=True)


# In[32]:

# test
#replacing the NaNs in the OHE variables with NotApp
for i in train_ohe_cols:
    test[i].fillna('NotApp',inplace=True)


# In[33]:

# train
## creating OHE categorical variables
cat_features_train=train[train_ohe_cols]

print cat_features_train.shape, cat_features_train.columns

cat_features_train = pd.concat([pd.get_dummies(cat_features_train[col]
                                         , prefix=col
                                        ) for col in cat_features_train], axis=1)
print "\n"
print cat_features_train.shape, cat_features_train.columns


# In[34]:

#test
## creating OHE categorical variables
cat_features_test=test[train_ohe_cols]

print cat_features_test.shape, cat_features_test.columns


cat_features_test = pd.concat([pd.get_dummies(cat_features_test[col]
                                         , prefix=col
                                        ) for col in cat_features_test], axis=1)

print "\n"
print cat_features_test.shape, cat_features_test.columns


# In[35]:

#train
# other new features

train_new_date_vars=[]
for i in hl_cat_var_date:
    #train_new_date_vars.append(i)
    train_new_date_vars.append(i+'_day')
    train_new_date_vars.append(i+'_dow')
    train_new_date_vars.append(i+'_year')
    train_new_date_vars.append(i+'_woy')
print train_new_date_vars , len(train_new_date_vars)
print len(cat_features_train.columns)

# new variables (data variables and cat_ohe_variables)
train_add_variables=train_new_date_vars+ list(cat_features_train.columns)
print train_add_variables , len(train_add_variables)


# In[36]:

#test
# other new features

test_new_date_vars=[]
for i in hl_cat_var_date:
    #test_new_date_vars.append(i)
    test_new_date_vars.append(i+'_day')
    test_new_date_vars.append(i+'_dow')
    test_new_date_vars.append(i+'_year')
    test_new_date_vars.append(i+'_woy')
print test_new_date_vars , len(test_new_date_vars)
print len(cat_features_test.columns)

# new variables (data variables and cat_ohe_variables)
test_add_variables=test_new_date_vars+ list(cat_features_test.columns)
print test_add_variables , len(test_add_variables)


# In[37]:

##commmon new features between train and test
common_new_features=list(set(train_add_variables).intersection(test_add_variables))


# In[38]:

len(common_new_features), len(train_add_variables), len(test_add_variables), type(common_new_features)


# In[40]:

# new train dataset with additional features
train_add=pd.concat([train,cat_features_train], axis=1)


# In[39]:

# new test dataset with additional features
test_add=pd.concat([test,cat_features_test], axis=1)


# In[41]:

print train_add.shape, test_add.shape


# <!---
# ### Notes
# ######Steps
# 1. find all the 51 categorical variables ---done
# 2. find ways to reduce the dimensionality of the categorical variables --- use variable importance 
# 2. the two value variables appear to be binary variables ---done -->

# In[42]:

#event rate
print train['target'].value_counts()
print train['target'].value_counts(normalize=True)


# ### event rate is~23.3%

# In[43]:

# model features only the initial non cat variables excluding ID and target
model_features=[x for (x,v) in non_cat_var if x not in ['ID','target']]


# In[44]:

print len(non_cat_var), len(model_features), type(non_cat_var),type(model_features)


#  <!--#replacing inf and nan with zero in train
# train_data_model=train.replace([np.inf, -np.inf,np.nan], 0)
# print  "\n"; 
# 
# 
# 
# ## modeling using only non cat variables
# ## splitting in to train and val ( 80/20)
# from sklearn.cross_validation import train_test_split
# train_model, val_model = train_test_split(train_data_model, test_size=0.20, random_state=9876)
# 
# -->

# In[45]:

train_add.shape


# In[46]:

## modeling using new variables 

#replacing inf and nan with zero in train
train_add.replace([np.inf, -np.inf,np.nan], 0, inplace=True)
print  "\n";


# In[47]:

## splitting in to train and val (80/20)
from sklearn.cross_validation import train_test_split
train_add_model, val_add_model = train_test_split(train_add, test_size=0.20, random_state=9876)


# In[48]:

#replacing inf and nan with zero in test
test_add.replace([np.inf, -np.inf,np.nan], 0, inplace=True)


# In[49]:

print train_add_model.shape, val_add_model.shape, test_add.shape


# In[50]:

# model features including the new features
model_features_add=[x for (x,v) in non_cat_var if x not in ['ID','target']]+common_new_features


# In[51]:

print len(model_features_add), len(model_features)
print len(model_features_add)-len(model_features)


# In[52]:

##modeling 
### importing libraries
from sklearn import ensemble # for RandomForest
from sklearn.metrics import roc_curve, auc
from sklearn import cross_validation


# In[141]:

## classifiers
rf=ensemble.RandomForestClassifier(n_estimators=100,random_state=9876,n_jobs=16) ## random forest
ab=ensemble.AdaBoostClassifier(n_estimators=100) ## adaboost
gb=ensemble.GradientBoostingClassifier(n_estimators=100) ## gradient boosting


# In[118]:

### putting it all together in a function
# model function
def model(clfr,X,y,train_ds, val_ds, test_ds): ## parameters classifier, feature matrix,target, train_dataset, val_dataset, test_dataset
    
    clf = clfr ## Classifier(any of the classifier)
    clf.fit(train_ds[X], train_ds[y])
    
    ## predicting class on train ,val and test
    train_pred_class=clf.predict(train_ds[X])
    val_pred_class=clf.predict(val_ds[X])
    test_pred_class=clf.predict(test_ds[X])

    ## predicting probabilities on train, val  and test
    train_pred_prob=clf.predict_proba(train_ds[X])
    val_pred_prob=clf.predict_proba(val_ds[X])
    test_pred_prob=clf.predict_proba(test_ds[X])


    ##taking the probabilities for predicted class=1 (2 nd column in the array)
    train_pred_prob=train_pred_prob[:,1]
    val_pred_prob=val_pred_prob[:,1]
    test_pred_prob=test_pred_prob[:,1]
    
    #cf table
    cf_mat_train=pd.crosstab(train_ds[y], train_pred_class, rownames=['actual'], colnames=['preds'])
    cf_mat_val=pd.crosstab(val_ds[y], val_pred_class, rownames=['actual'], colnames=['preds'])
    
    ## train metrics
    train_err=(cf_mat_train.iloc[0,1]+cf_mat_train.iloc[1,0])/(cf_mat_train.iloc[0,1]+cf_mat_train.iloc[1,0]+cf_mat_train.iloc[0,0]+cf_mat_train.iloc[1,1])  ## error rate
    train_acc=(cf_mat_train.iloc[0,0]+cf_mat_train.iloc[1,1])/(cf_mat_train.iloc[0,1]+cf_mat_train.iloc[1,0]+cf_mat_train.iloc[0,0]+cf_mat_train.iloc[1,1]) ## accuracy
    train_recall =cf_mat_train.iloc[1,1]/(cf_mat_train.iloc[1,1]+cf_mat_train.iloc[1,0]) ###recall  or hit rate or tpr or sensitivity
    train_spc=cf_mat_train.iloc[0,0]/(cf_mat_train.iloc[0,0]+cf_mat_train.iloc[0,1])  ##tnr or specificity
    train_prec=cf_mat_train.iloc[1,1]/(cf_mat_train.iloc[1,1]+cf_mat_train.iloc[0,1]) ### precision  or positive predicted value(ppv) 
    train_npv =cf_mat_train.iloc[0,0]/(cf_mat_train.iloc[0,0]+cf_mat_train.iloc[1,0]) ###negative predicted value
    train_fpr =cf_mat_train.iloc[0,1]/(cf_mat_train.iloc[0,0]+cf_mat_train.iloc[0,1]) ###false positive rate or fall out  
    train_fdr =cf_mat_train.iloc[0,1]/(cf_mat_train.iloc[0,1]+cf_mat_train.iloc[1,1]) ###false discovery rate
    train_fnr =cf_mat_train.iloc[1,0]/(cf_mat_train.iloc[1,0]+cf_mat_train.iloc[1,1]) ###false negative rate
    train_f1score=(2*train_recall*train_prec)/(train_recall+train_prec)

    ## val metrics
    
    val_err=(cf_mat_val.iloc[0,1]+cf_mat_val.iloc[1,0])/(cf_mat_val.iloc[0,1]+cf_mat_val.iloc[1,0]+cf_mat_val.iloc[0,0]+cf_mat_val.iloc[1,1])  ## error rate
    val_acc=(cf_mat_val.iloc[0,0]+cf_mat_val.iloc[1,1])/(cf_mat_val.iloc[0,1]+cf_mat_val.iloc[1,0]+cf_mat_val.iloc[0,0]+cf_mat_val.iloc[1,1]) ## accuracy
    val_recall =cf_mat_val.iloc[1,1]/(cf_mat_val.iloc[1,1]+cf_mat_val.iloc[1,0]) ###recall  or hit rate or tpr or sensitivity
    val_spc=cf_mat_val.iloc[0,0]/(cf_mat_val.iloc[0,0]+cf_mat_val.iloc[0,1])  ##tnr or specificity
    val_prec=cf_mat_val.iloc[1,1]/(cf_mat_val.iloc[1,1]+cf_mat_val.iloc[0,1]) ### precision  or positive predicted value(ppv) 
    val_npv =cf_mat_val.iloc[0,0]/(cf_mat_val.iloc[0,0]+cf_mat_val.iloc[1,0]) ###negative predicted value
    val_fpr =cf_mat_val.iloc[0,1]/(cf_mat_val.iloc[0,0]+cf_mat_val.iloc[0,1]) ###false positive rate or fall out  
    val_fdr =cf_mat_val.iloc[0,1]/(cf_mat_val.iloc[0,1]+cf_mat_val.iloc[1,1]) ###false discovery rate
    val_fnr =cf_mat_val.iloc[1,0]/(cf_mat_val.iloc[1,0]+cf_mat_val.iloc[1,1]) ###false negative rate
    val_f1score=(2*val_recall*val_prec)/(val_recall+val_prec)
    
    
    train_met_dict={
        "accuracy":train_acc*100
        ,"error":train_err*100
        ,"precision":train_prec*100
        ,"recall":train_recall*100
        ,"FDR":train_fdr*100
        ,"FNR":train_fnr*100
        ,"F1 SCORE":train_f1score*100
    }

    val_met_dict={
        "accuracy":val_acc*100
        ,"error":val_err*100
        ,"precision":val_prec*100
        ,"recall":val_recall*100
        ,"FDR":val_fdr*100
        ,"FNR":val_fnr*100
        ,"F1 SCORE":val_f1score*100
    }
    

    ## feature importance
    feat_index = np.argsort(clf.feature_importances_)[::-1] ## sorting the indices of feature importance in decending order
    fet_imp = clf.feature_importances_[feat_index] ##using the descending sorted index and arranging the feature importance array 
    
    fet_imp_names = [X[i] for i in feat_index] ## collecting the feature names from the index
    
    ##Putting the sorted feature importance and feature names in a dataframe
    d = {'v_imp_names': pd.Series(fet_imp_names),
         'v_imp_values': pd.Series(fet_imp)
        }
    v_imp_df = pd.DataFrame(d)
    
    #train AUC
    fpr_train, tpr_train, thresholds_train = roc_curve(train_ds[y], train_pred_prob)
    roc_auc_train = auc(fpr_train, tpr_train)

    #val AUC
    fpr_val, tpr_val, thresholds_val = roc_curve(val_ds[y], val_pred_prob)
    roc_auc_val = auc(fpr_val, tpr_val)
    
    
    ret_dict={"train_pred_class":train_pred_class
              ,"test_pred_class":test_pred_class
              ,"val_pred_class":val_pred_class
              ,"train_pred_prob":train_pred_prob
              ,"test_pred_prob":test_pred_prob
              ,"val_pred_prob":val_pred_prob
              ,"cf_mat_train":cf_mat_train
              ,"cf_mat_val":cf_mat_val
              ,"train_met_dict":train_met_dict
              ,"val_met_dict":val_met_dict
              ,"v_imp_df":v_imp_df
              ,"train_auc":roc_auc_train
              ,"train_fpr_auc":fpr_train
              ,"train_tpr_auc":tpr_train
              ,"train_thresholds_auc":thresholds_train
              ,"val_auc":roc_auc_val
              ,"val_fpr_auc":fpr_val
              ,"val_tpr_auc":tpr_val
              ,"val_thresholds_auc":thresholds_val
             }
    return ret_dict


# In[123]:

## model Execution function
def model_execution(X,clfr): #paramters: feature matrix, classifier
    y='target'
    t_start=time.time()
    model_result=model(clfr,X,y,train_add_model,val_add_model,test_add)
    t_end=time.time()
    t_diff=t_end-t_start
    print "running time in seconds : ", t_diff ## tells the model running time in seconds
    return model_result 


# In[135]:

## model Results printing function
def model_results_print(model_name):
    print "VAL_CM:"
    print model_name['cf_mat_val']
    print "TRAIN_CM:"
    print model_name['cf_mat_train']
    print "\n"
    print model_name['val_met_dict']
    print "\n"
    print model_name['train_met_dict']
    print "\n"
    print "Train AUC:", model_name['train_auc']
    print "\n"
    print "Val AUC:",model_name['val_auc']


# In[128]:

rf_add1=model_execution(model_features_add,rf)


# In[136]:

model_results_print(rf_add1)


# In[130]:

rf_add1['v_imp_df']


# In[143]:

## creating a second features from only the important variables from First features which has importance >1%
fet_add2=list(rf_add1['v_imp_df']['v_imp_names'][rf_add1['v_imp_df']['v_imp_values']>=0.001])
print len(fet_add2)


# In[124]:

rf_add2=model_execution(fet_add2,rf)


# In[137]:

model_results_print(rf_add2)


# In[142]:

## creating a third features from only the important variables from second set of features 
fet_add3=list(rf_add2['v_imp_df']['v_imp_names'][rf_add2['v_imp_df']['v_imp_values']>=0.003])
print len(fet_add3)


# In[126]:

rf_add3=model_execution(fet_add3,rf)


# In[138]:

model_results_print(rf_add3)


# In[144]:

ab_add1=model_execution(model_features_add,ab)


# In[145]:

model_results_print(ab_add1)


# In[132]:

ab_add2=model_execution(fet_add2,ab)


# In[139]:

model_results_print(ab_add2)


# In[146]:

gb_add1=model_execution(model_features_add,gb)


# In[147]:

model_results_print(gb_add1)


# In[148]:

gb_add2=model_execution(fet_add2,gb)


# In[149]:

model_results_print(gb_add2)


# ## Submissions based on single Ensemble learners 

# In[154]:

def submission(filename, modelname): # filename as string, modelname
    sub=pd.concat([test_add['ID'],pd.DataFrame(modelname['test_pred_prob'])],axis=1)
    # renaming columns
    sub.columns=['ID','target']
    sub.to_csv(filename+'.csv',sep=',',index=None)


# In[155]:

## random forest submsissions
submission('rf_submission_init',rf_add1)
submission('rf_submission_fet2',rf_add2)
submission('rf_submission_fet3',rf_add3)


# In[156]:

# adaboost submissions
submission('ab_submission_init',ab_add1)
submission('ab_submission_fet2',ab_add2)


# In[157]:

# gradient boosting Submissions
submission('gb_submission_init',gb_add1)
submission('gb_submission_fet2',gb_add2)


# <!--- ! unzip sample_submission.csv.zip -->

# ## Submission based on average of ensemble Learners

# In[104]:

# Average of Ensenmble models of gb1,gb2,rf1 and ab2
sub_mean_gb1_gb2_rf1_ab2=pd.concat([sub_gb1
               ,sub_gb2[['target']]
               ,sub_rf1[['target']]
               ,sub_ab2[['target']]
              ,],axis=1)


# In[106]:

sub_mean_gb1_gb2_rf1_ab2.shape , sub_mean_gb1_gb2_rf1_ab2.columns


# In[107]:

sub_mean_gb1_gb2_rf1_ab2.columns=['ID','target_gb1','target_gb2','target_rf1','target_ab2']


# In[108]:

sub_mean_gb1_gb2_rf1_ab2.columns


# In[109]:

sub_mean_gb1_gb2_rf1_ab2['fin_target']=(sub_mean_gb1_gb2_rf1_ab2['target_gb1'] + sub_mean_gb1_gb2_rf1_ab2['target_gb2']+sub_mean_gb1_gb2_rf1_ab2['target_rf1']+sub_mean_gb1_gb2_rf1_ab2['target_ab2'])/4


# In[110]:

sub_mean_4_ensemble=sub_mean_gb1_gb2_rf1_ab2[['ID','fin_target']]


# In[114]:

sub_mean_gb1_gb2_rf1_ab2.head(5)


# In[112]:

sub_mean_4_ensemble.columns =['ID','target']


# In[115]:

sub_mean_4_ensemble.to_csv('mean_gb1_gb2_rf1_ab2_submission.csv',sep=',',index=None)


# In[89]:

# Average of Ensenmble models of rf1,gb1 an gb2
sub_mean_gb1_gb2_rf1=pd.merge(sub_gb1
                  ,pd.merge(sub_gb2
                            ,sub_rf1
                            ,left_on='ID'
                            ,right_on='ID'
                            ,how='inner')
                 ,left_on='ID'
                 ,right_on='ID'
                 ,how='inner')


# In[91]:

sub_mean_gb1_gb2_rf1.shape, sub_mean_gb1_gb2_rf1.columns


# In[92]:

sub_mean_gb1_gb2_rf1['fin_target']=(sub_mean_gb1_gb2_rf1['target'] + sub_mean_gb1_gb2_rf1['target_x']+sub_mean_gb1_gb2_rf1['target_y'])/3


# In[93]:

sub_mean_gb1_gb2_rf1.columns


# In[94]:

sub_mean_gb1_gb2_rf1.head(5)


# In[95]:

sub_mean=sub_mean_gb1_gb2_rf1[['ID','fin_target']]


# In[101]:

sub_mean.rename(columns= {'fin_target':'target'}, inplace=True)


# In[102]:

sub_mean.shape, sub_mean.columns


# In[103]:

sub_mean.to_csv('mean_gb1_gb2_rf1_submission.csv',sep=',',index=None)


# ##------------------------------------END-------------------------

# ## EXTRAS - ROUGH WORK

# In[104]:

rf1['cf_mat_val']


# In[105]:

rf1['cf_mat_train']


# In[120]:

print rf1['val_met_dict']
print "\n"
print rf1['train_met_dict']


# In[164]:

print rf1['train_auc']
print rf1['val_auc']


# In[111]:

rf1['v_imp_df']


# In[112]:

## creating a second features from only the important variables from First features which has importance >1%
fet2=list(rf1['v_imp_df']['v_imp_names'][rf1['v_imp_df']['v_imp_values']>=0.001])


# In[113]:

len(fet2)


# In[116]:

X=fet2
y='target'
rf2=rf_model(X,y,train_model,val_model)


# In[117]:

rf2['cf_mat_val']


# In[118]:

rf2['cf_mat_train']


# In[121]:

print rf2['val_met_dict']
print "\n"
print rf2['train_met_dict']


# In[163]:

print rf2['train_auc']
print rf2['val_auc']


# In[129]:

## creating a second features from only the important variables from First features which has importance >1%
fet3=list(rf2['v_imp_df']['v_imp_names'][rf2['v_imp_df']['v_imp_values']>=0.003])


# In[130]:

len(fet2),len(fet3)


# In[131]:

X=fet3
y='target'
rf3=rf_model(X,y,train_model,val_model)


# In[132]:

rf3['cf_mat_val']


# In[133]:

rf3['cf_mat_train']


# In[134]:

print rf3['val_met_dict']
print "\n"
print rf3['train_met_dict']


# In[162]:

print rf3['train_auc']
print rf3['val_auc']


# 

# In[135]:




# In[137]:

X=model_features
y='target'
t0_ab1=time.time()

adaboost1=adaboost_model(X,y,train_model,val_model)

t1_ab1=time.time()

delta_t_ab1=t1_ab1-t0_ab1

print "running time in seconds : ", delta_t_ab1


# In[139]:

adaboost1['cf_mat_val']


# In[140]:

adaboost1['cf_mat_train']


# In[141]:

print adaboost1['val_met_dict']
print "\n"
print adaboost1['train_met_dict']


# In[146]:

X=fet2
y='target'
t0_ab2=time.time()

adaboost2=adaboost_model(X,y,train_model,val_model)

t1_ab2=time.time()

delta_t_ab2=t1_ab2-t0_ab2

print "running time in seconds: " ,delta_t_ab2


# In[147]:

adaboost2['cf_mat_val']


# In[148]:

adaboost2['cf_mat_train']


# In[149]:

print adaboost2['val_met_dict']
print "\n"
print adaboost2['train_met_dict']


# 
# 

# In[151]:




# In[152]:

X=model_features
y='target'

t0_gb1=time.time()

gradboost1=gradboost_model(X,y,train_model,val_model)

t1_gb1=time.time()

delta_t_gb1=t1_gb1-t0_gb1

print "running time in seconds : ", delta_t_gb1


# In[153]:

gradboost1['cf_mat_val']


# In[154]:

gradboost1['cf_mat_train']


# In[155]:

print gradboost1['val_met_dict']
print "\n"
print gradboost1['train_met_dict']


# In[160]:

print gradboost1['train_auc']
print gradboost1['val_auc']


# In[156]:

X=fet2
y='target'

t0_gb2=time.time()

gradboost2=gradboost_model(X,y,train_model,val_model)

t1_gb2=time.time()

delta_t_gb2=t1_gb2-t0_gb2

print "running time in seconds : ", delta_t_gb2


# In[157]:

gradboost2['cf_mat_val']


# In[158]:

gradboost2['cf_mat_train']


# In[159]:

print gradboost2['val_met_dict']
print "\n"
print gradboost2['train_met_dict']


# In[161]:

print gradboost2['train_auc']
print gradboost2['val_auc']

