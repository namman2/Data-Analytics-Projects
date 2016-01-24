
# coding: utf-8

# ### Importing all the essential Python Libraries

# In[1]:

import pandas as pd
from pandas import DataFrame, Series
import numpy as np
import matplotlib.pyplot as plt
import json
get_ipython().magic('matplotlib inline')


# ### Defining the file path to the Decode events log dataset

# In[2]:

file_path = 'C://Users/Chiku/Downloads/Bitly Challenge/decodesaa.json'


# ### Loading in the Decode log JSON dataset into Python

# In[3]:

decode_log = [json.loads(line) for line in open(file_path)]


# ### Displaying the first two records from the Dataset

# In[4]:

decode_log[0]


# In[5]:

decode_log[1]


# ### Converting the Dataset into a Python DataFrame

# In[6]:

df = pd.DataFrame(decode_log)


# #### Initial examination of the DataFrame

# In[7]:

df.shape


# In[8]:

df.head()


# ### Beginning the dataset Analysis

# #### Analysing the Top 10 Timezones for Bitlinks

# Dealing with the Missing and Blank values for the Timezone

# In[9]:

df['tz'].fillna(value='Missing', inplace=True)


# In[10]:

df[df['tz'] == ''] = 'Unknown'


# In[11]:

top_tz = df['tz'].value_counts()


# Listing out the Top 10 Timezones for the Bitlinks

# In[12]:

top_tz[:10]


# Visualizing the Top 10 Timezones for the Bitlinks

# In[13]:

top_tz[:10].plot(kind='barh', figsize=(10, 6), title='Top 10 Timezones for Bitlinks')


# #### Analyzing the Top 5 Browsers based on Bit.ly instances

# Handling the missing data for the Browser User agent

# In[14]:

web_browsers = df['a'].dropna()


# Splitting the User browser agent data to obtain browser information

# In[15]:

browser_type = Series([browser.split()[0] for browser in web_browsers])


# Counting the number of Instances for all the top 5 browsers and loading it into a new variable

# In[16]:

top_browsers = browser_type.value_counts()[:5]


# Visualizing the Top 5 Browsers for the Bitlinks

# In[17]:

top_browsers.plot(kind='bar', figsize=(10, 6), title='Top 10 Browsers for Bitlinks')


# #### Analyzing the number of Instances based on Windows, Mac OS, Android and iPhone systems

# Creating a new Dframe where the Null values of User browser agent are ignored

# In[18]:

dframe = df[df['a'].notnull()]


# Assigning a new column in the Dframe for the type of System accessing the Bitlinks

# In[35]:

OS_Windows = np.where(dframe['a'].dropna().str.contains('Windows'), 'Windows system', 'Not Windows')
OS_Windows = pd.DataFrame(OS_Windows)
OS_Windows.columns = ['Windows system or Not']


# In[37]:

OS_Mac = np.where(dframe['a'].str.contains('Mac OS'), 'Mac OS system', 'Not Mac OS')
OS_Mac = pd.DataFrame(OS_Mac)
OS_Mac.columns = ['Mac OS system or Not']


# In[38]:

Android = np.where(dframe['a'].dropna().str.contains('Android'), 'Android system', 'Not Android')
Android = pd.DataFrame(Android)
Android.columns = ['Android system or Not']


# In[39]:

iPhone = np.where(dframe['a'].dropna().str.contains('iPhone'), 'iPhone system', 'Not an iPhone')
iPhone = pd.DataFrame(iPhone)
iPhone.columns = ['iPhone device or Not']


# In[40]:

win_inst = OS_Windows['Windows system or Not'].str.contains(r'Windows system').sum()
mac_inst = OS_Mac['Mac OS system or Not'].str.contains(r'Mac OS system').sum()
android_inst = Android['Android system or Not'].str.contains(r'Android system').sum()
iphone_inst = iPhone['iPhone device or Not'].str.contains(r'iPhone system').sum()


# In[44]:

instances = pd.DataFrame( {'Number of Windows instances' : win_inst, 'Number of Mac instances' : mac_inst, 'Number of Android instances' : android_inst, 'Number of iPhone instances' : iphone_inst}, index = ['Type of Device'] )


# In[46]:

instances.plot(kind='bar', figsize=(10, 6), title='Most popular Devices accessing Bitlinks')


# In[47]:

instances


# #### Analyzing the Top 10 countries with the most number of Bitlink instances

# Dealing with the missing and the blank values for the Country column

# In[48]:

df['c'].fillna(value='Missing', inplace=True)


# In[49]:

df[df['c'] == ''] = 'Unknown'


# In[50]:

top_countries = df['c'].value_counts()


# In[51]:

top_countries[:10]


# In[52]:

top_countries[:10].plot(kind='barh', figsize=(10, 6), title='Top 10 Countries with most Bitlink instances')


# #### Analyzing the Top 10 most active users

# ##### Analyzing the Top 10 active users based on no. of instances

# In[53]:

df['h'].value_counts(sort=True, ascending=False).head(10)


# ##### Analyzing the Top 10 active users based on the most no of repeat-clicks

# In[55]:

repeat_client = dframe.groupby("h").agg({"nk": np.sum, "h": pd.Series.nunique})


# In[57]:

repeat_client.sort('nk', ascending=False).head(10)


# ## Bitly Challenge Decode Dataset 1 file
# ### Access it at: http://nbviewer.jupyter.org/github/namman2/Data-Analytics-Projects/tree/master/
