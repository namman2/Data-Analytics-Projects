
# coding: utf-8

# In[1]:

# Importing the essential Python Libraries

import pandas as pd
import numpy as np
import statsmodels.api as sm
import matplotlib
import matplotlib.pyplot as plt
get_ipython().magic('matplotlib inline')
matplotlib.style.use('ggplot')
from pandas.tools.plotting import scatter_matrix


# In[2]:

# Importing the Parkinson's Telemedicine dataset

df = pd.DataFrame.from_csv('parkinsons_updrs.data.csv')


# In[3]:

# Checking the first 5 columns of the dataset

df.head()


# In[4]:

# Defining the dependent and the predictors or independent variables

dependent = 'total_UPDRS'
predictors = [colname for colname in df.columns if colname not in ['motor_UPDRS','total_UPDRS']]


# In[5]:

# Creating Boxplots for the firs 10 columns of the dataset 

boxplots1 = df[df.columns[:10]].plot(subplots=True, kind='box', figsize=(16,8))


# In[6]:

# Creating Boxplots for the remainder columns of the dataset

boxplots2 = df[df.columns[11:]].plot(subplots=True, kind='box', figsize=(16,8))


# In[7]:

# Plotting a histogram for one of the predictor variable

hist_ex = df['Jitter(%)'].plot(kind='hist', bins=40)


# In[8]:

# Taking a Log and plotting a histogram of the same predictor variable

hist_log_ex = df['Jitter(%)'].apply(np.log)

hist_log_ex.plot(kind='hist', bins=40)


# In[9]:

# Plotting a scatter matrix to check for multicollinearity in the predictor variables

plot = scatter_matrix(df[predictors], diagonal='kde', figsize=(30,30))


# In[10]:

# Eliminating the predictor variables with high multicollinearity

predictors.remove('Jitter:DDP')
predictors.remove('Shimmer:DDA')


# In[11]:

# Taking a log of the Jitter, Shimmer, NHR and PPE predictor variables

predictors_to_log = [predictor for predictor in predictors if any(lookforstring in predictor for lookforstring in ('Shimmer','Jitter','NHR', 'PPE'))]


# In[12]:

# Defining the series of columns to which a log function has to be applied

def log_columns(series):
    if series.name in predictors_to_log:
        return np.log(series)
    else:
        return series
    
final_df = df.apply(log_columns)


# In[13]:

#Ordinary Least Squares Estimation

model = sm.OLS(final_df[dependent], exog=final_df[predictors])

results = model.fit()

results.summary()

