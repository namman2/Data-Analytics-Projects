
# coding: utf-8

# In[1]:

# Importing essential Python libraries

import numpy as np
import pandas as pd
from pandas import Series,DataFrame
import seaborn as sns
import matplotlib.pyplot as plt
get_ipython().magic('matplotlib inline')


# In[2]:

# Reading in the Titanic Dataset

titanic_df = pd.read_csv('train.csv')


# In[3]:

# Displaying first Five rows of the Titanic Dataset

titanic_df.head()


# In[4]:

titanic_df.info()


# In[5]:

# Defining a new Person function

def male_female_child(passenger):
    age,sex = passenger
    
    if age < 16:
        return 'child'
    else:
        return sex


# In[6]:

# Adding a new Person column to the dataset

titanic_df['person'] = titanic_df[['Age','Sex']].apply(male_female_child, axis=1)


# In[7]:

# Creating a Deck statement in the dataset

deck = titanic_df['Cabin'].dropna()


# In[8]:

# Assigning Deck Level letters in the Dataset

levels = []

for level in deck:
    levels.append(level[0])
    
cabin_df = DataFrame(levels)
cabin_df.columns = ['Cabin']

cabin_df = cabin_df[cabin_df.Cabin != 'T']


# In[9]:

# Create a new Column called 'Levels' for the Deck levels

titanic_df['Level'] = Series(levels,index=deck.index)


# In[10]:

# View the First 10 Rows of the new dataset

titanic_df[0:10]


# In[11]:

# Visualizing the number of people in different Deck Levels

sns.factorplot('Cabin',data=cabin_df,x_order=['A','B','C','D','E','F'],kind='count',palette='winter_d')


# In[12]:

# Male vs Female count on the Titanic

sns.factorplot('Sex',data=titanic_df,kind='count')


# In[13]:

# Plotting the Male vs Female vs Child breakdown according to Class

sns.factorplot('Pclass',data=titanic_df,kind='count',hue='person')


# In[14]:

# Plotting the ages of the passengers on the Titanic

titanic_df['Age'].hist(bins=70)


# In[15]:

# Average age of passengers on the Titanic

titanic_df['Age'].mean()


# In[16]:

# Number of people who are male, female and child

titanic_df['person'].value_counts()


# In[17]:

# KDEplot for the Ages vs Male/Female

fig = sns.FacetGrid(titanic_df,hue='Sex',aspect=4)
fig.map(sns.kdeplot,'Age',shade=True)

oldest = titanic_df['Age'].max()
fig.set(xlim=(0,oldest))
fig.add_legend()


# In[18]:

# KDEplot for the Ages vs Male/Female/Child

fig = sns.FacetGrid(titanic_df,hue='person',aspect=4)
fig.map(sns.kdeplot,'Age',shade=True)

oldest = titanic_df['Age'].max()
fig.set(xlim=(0,oldest))
fig.add_legend()


# In[19]:

# KDEplot for the Ages vs Passenger Class

fig = sns.FacetGrid(titanic_df,hue='Pclass',aspect=4)
fig.map(sns.kdeplot,'Age',shade=True)

oldest = titanic_df['Age'].max()
fig.set(xlim=(0,oldest))
fig.add_legend()


# In[20]:

# Plotting the Class of Passengers embarked from different locations

sns.factorplot('Embarked',data=titanic_df,hue='Pclass',x_order=['C','Q','S'],kind='count')


# In[21]:

# Creating a new column for People who were travelling alone

titanic_df['Alone'] = titanic_df.SibSp + titanic_df.Parch


# In[22]:

# Assigning relevant strings to the different values of the Alone column

titanic_df['Alone'].loc[titanic_df['Alone'] > 0] = 'With Family'

titanic_df['Alone'].loc[titanic_df['Alone'] == 0] = 'Alone'


# In[23]:

# Counting the passengers who were travelling alone vs who were with family

sns.factorplot('Alone',data=titanic_df,kind='count',palette='Blues')


# In[24]:

# Family vs Alone passengers according to their Class breakdown

sns.factorplot('Alone',data=titanic_df,kind='count',palette='Blues',hue='Pclass')


# In[25]:

# Creating a new Survivor column

titanic_df['Survivor'] = titanic_df.Survived.map({0 : 'no', 1 : 'yes'})


# In[26]:

# Counting the number of Survivors on the Titanic

sns.factorplot('Survivor',data=titanic_df,palette='Set1',kind='count')


# In[27]:

# Being a Male/Female/Child travelling on different Classes and the chances of survival

sns.factorplot('Pclass','Survived',data=titanic_df,hue='person')


# In[28]:

# Defining a new Bin

generations = [10,20,40,60,80]


# In[29]:

# Plotting the Age, Survival rate and the Passenger Class

sns.lmplot('Age','Survived',hue='Pclass',data=titanic_df,palette='winter',x_bins=generations)


# In[30]:

# How Age and the Sex had an impact on the Survival rate

sns.lmplot('Age','Survived',hue='Sex',data=titanic_df,palette='winter',x_bins=generations)


# In[31]:

# How the Deck level had an impact on the Survival rate

sns.factorplot('Level','Survived',x_order=['A','B','C','D','E','F'],data=titanic_df)


# In[32]:

# How being with a Family or alone had an impact on the Survival rate

sns.factorplot('Alone','Survived',data=titanic_df)


# In[33]:

# Final Dataset Top 10 Rows

titanic_df[0:10]


# In[ ]:



