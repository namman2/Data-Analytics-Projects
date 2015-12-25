
# coding: utf-8

# In[1]:

# Impoting essential Python Libraries

import numpy as np
import pandas as pd
from pandas import Series,DataFrame


# In[2]:

# Inputting the Wine quality dataset as a .CSV

dframe_wine = pd.read_csv('winequality-red.csv',sep=';')


# In[3]:

# First five rows of the dataset

dframe_wine.head()


# In[4]:

# Finding the average Alcohol level in all of the wines

dframe_wine['alcohol'].mean()


# In[5]:

# Creating a function named 'Max - Min'

def max_to_min(arr):
    return arr.max() - arr.min()


# In[6]:

# Categorize the dataset by Quality levels

wine_q = dframe_wine.groupby('quality')


# In[7]:

wine_q.describe()


# In[8]:

# Using the max_to_min function, an aggregation is done for all Quality levels of a wine

wine_q.agg(max_to_min)


# In[9]:

# Creating a new column as 'Quality to Alcohol ratio'

dframe_wine['quality/alcohol ratio'] = dframe_wine['quality']/dframe_wine['alcohol']


# In[10]:

dframe_wine.head()


# In[11]:

# Same as groupping by Wine 'Quality'

dframe_wine.pivot_table(index=['quality'])


# In[12]:

get_ipython().magic('matplotlib inline')


# In[13]:

# Plotting Quality vs Alcohol level as a scatter plot

dframe_wine.plot(kind='scatter',x='quality',y='alcohol')


# In[31]:

# Creating a new 'Rank' function

def rank(df):
    df['alcohol_content_rank'] = np.arange(len(df))+1
    return df


# In[ ]:




# In[ ]:




# In[32]:

# Sorting the dataset by their alcohol level and applying 'Rank' function

dframe_wine.sort_values('alcohol',ascending=False,inplace=True)
dframe_wine = dframe_wine.groupby('quality').apply(rank)


# In[ ]:




# In[ ]:




# In[ ]:




# In[33]:

dframe_wine.head()


# In[ ]:




# In[ ]:




# In[34]:

# Counting the number of Wines in a particular quality level

num_of_qual = dframe_wine['quality'].value_counts()


# In[ ]:




# In[ ]:




# In[35]:

num_of_qual


# In[ ]:




# In[36]:

# Listing all of the Wines with an alcohol content rank of 1

dframe_wine[dframe_wine.alcohol_content_rank == 1].head(len(num_of_qual))


# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:



