
# coding: utf-8

# In[1]:

# Importing Essential Python libraries

import numpy as np
import pandas as pd
from pandas import Series,DataFrame

# Libraries for Data Visualizations
import matplotlib.pyplot as plt
get_ipython().magic('matplotlib inline')
import seaborn as sns
sns.set_style('whitegrid')

# Libraries for grabbing data from the web

import requests
from io import StringIO

# For timestamps

from datetime import datetime


# In[2]:

# Grabbbing 2012 Election dataset from HuffingtonPost website

url = 'http://elections.huffingtonpost.com/pollster/2012-general-election-romney-vs-obama.csv'

source = requests.get(url).text


# In[3]:

# Creating a DataFrame from the Poll dataset

poll_data = StringIO(source)

poll_df = pd.read_csv(poll_data)


# In[4]:

# First five rows of the Poll DataFrame

poll_df.head()


# In[5]:

# Information regarding the Poll dataset

poll_df.info()


# In[6]:

# Counting the affiliation of the Pollsters to different Parties

sns.factorplot('Affiliation',data=poll_df, kind='count')


# In[7]:

# Counting the affiliation of the Pollsters to different Parties, taking categories of people into account

sns.factorplot('Affiliation',data=poll_df,kind='count',hue='Population')


# In[8]:

# Creating an Average object, by dropping the Number of observations column

avg = pd.DataFrame(poll_df.mean())

avg.drop('Number of Observations',axis=0,inplace=True)


# In[9]:

# Viewing the Average of Polls for Obama and Romney

avg


# In[11]:

# Creating a Std deviation object, by dropping the Number of observations column

std = pd.DataFrame(poll_df.std())

std.drop('Number of Observations',axis=0,inplace=True)


# In[12]:

# Plotting the Number of votes for Obama, Romney and Undecided votes 

avg.plot(yerr=std,kind='bar',legend=False)


# In[13]:

# Combining the Average and Standard deviation of the poll results

poll_avg = pd.concat([avg,std],axis=1)

poll_avg.columns = ['Average','STD']

poll_avg


# In[14]:

# Plotting a time series of the polls for sentiment analysis

poll_df.plot(x='End Date',y=['Obama','Romney','Undecided'],linestyle='',marker='o')


# In[15]:

# Calculating the Percentage difference between two candidates

poll_df['Difference'] = (poll_df.Obama - poll_df.Romney)/100

poll_df.head()


# In[16]:

# Sentiment Analysis in difference of opinion over time

poll_df = poll_df.groupby(['Start Date'],as_index=False).mean()

poll_df.head()


# In[17]:

# Plotting a Timeseries of the Sentiment analysis between Obama and Romney

poll_df.plot('Start Date','Difference',figsize=(12,4),marker='o',linestyle='-',color='purple')


# In[18]:

## GOP Debate and analysing its affects on the Results

# Creating a timeline of the GOP Debate month
row_in = 0
xlimit = []

for date in poll_df['Start Date']:
    if date[0:7] == '2012-10':
        xlimit.append(row_in)
        row_in += 1
    else:
        row_in += 1
        
print(min(xlimit))
print(max(xlimit))


# In[19]:

# Plotting the GOP Debate markers and how it affected people's opinions and votes

poll_df.plot('Start Date','Difference',figsize=(12,4),marker='o',linestyle='-',color='purple',xlim=(329,356))

# Debate on Oct 3
plt.axvline(x=329+2,linewidth=4,color='grey')
# Debate on Oct 11
plt.axvline(x=329+10,linewidth=4,color='grey')
# Debate on Oct 22
plt.axvline(x=329+21,linewidth=4,color='grey')


# In[20]:

## Donor Dataset and taking into account Donors

# Reading in the Donor Dataset
donor_df = pd.read_csv('Election_Donor_Data.csv')


# In[21]:

donor_df.info()


# In[22]:

donor_df.head()


# In[23]:

# Counting the number of contributions been made for an individual amount

donor_df['contb_receipt_amt'].value_counts()


# In[24]:

# Average mean and std dev of the donations

don_mean = donor_df['contb_receipt_amt'].mean()

don_std = donor_df['contb_receipt_amt'].std()

print('The average donation was %.2f with a std deviation of %.2f' %(don_mean, don_std))


# In[25]:

# Sorting the Top donors by the amount donated

top_donor = donor_df['contb_receipt_amt'].copy()

top_donor.sort()

top_donor


# In[26]:

# Removing all the negative donations or refunds from the dataset

top_donor = top_donor[top_donor > 0]

top_donor.sort()


# In[27]:

top_donor.value_counts().head(10)


# In[28]:

# Visualizing the breakdown of donations below $2500

com_don = top_donor[top_donor < 2500]

com_don.hist(bins=100,)


# In[29]:

# Creating a Candidate object for Unqique candidates in the Presidential Elections

candidates = donor_df.cand_nm.unique()

candidates


# In[30]:

# Dictionary of Candidates and their respective party affiliation
party_map = {'Bachmann, Michelle': 'Republican',
           'Cain, Herman': 'Republican',
           'Gingrich, Newt': 'Republican',
           'Huntsman, Jon': 'Republican',
           'Johnson, Gary Earl': 'Republican',
           'McCotter, Thaddeus G': 'Republican',
           'Obama, Barack': 'Democrat',
           'Paul, Ron': 'Republican',
           'Pawlenty, Timothy': 'Republican',
           'Perry, Rick': 'Republican',
           "Roemer, Charles E. 'Buddy' III": 'Republican',
           'Romney, Mitt': 'Republican',
           'Santorum, Rick': 'Republican'}


# In[31]:

# Now mapping the candidates with their parties in to a new column
donor_df['Party'] = donor_df.cand_nm.map(party_map)


# In[34]:

donor_df.head()


# In[38]:

# Setting the Donor_df DataFrame to be positive donations

donor_df = donor_df[donor_df.contb_receipt_amt > 0]


# In[39]:

# Counting the total number of donations per candidate

donor_df.groupby('cand_nm')['contb_receipt_amt'].count()


# In[40]:

# Counting the total amount received by each candidate

donor_df.groupby('cand_nm')['contb_receipt_amt'].sum()


# In[41]:

# Printing out the total amount received by each candidate

cand_amt = donor_df.groupby('cand_nm')['contb_receipt_amt'].sum()

i = 0

for don in cand_amt:
    print('The candidate %s raised %.0f dollars' %(cand_amt.index[i],don))
    print('\n')
    i +=1


# In[42]:

# Visualizing the amount received by each candidate

cand_amt.plot(kind='bar')


# In[43]:

# Visualizing the donations received by each Party

donor_df.groupby('Party')['contb_receipt_amt'].sum().plot(kind='bar')


# In[44]:

# Analysing the Occupations of people who donated towards the campaigns

occupation_df = donor_df.pivot_table('contb_receipt_amt',index='contbr_occupation',columns='Party',aggfunc='sum')

occupation_df.head()


# In[45]:

# Total number of listed occupations of people making contributions

occupation_df.shape


# In[46]:

# Taking occupations into consideration who have collectively made over a Million dollar contribution

occupation_df = occupation_df[occupation_df.sum(1) > 1000000]

occupation_df.shape


# In[47]:

# Plotting the occupations who have made over a Million dollar in contribution

occupation_df.plot(kind='barh',figsize=(12,10))


# In[48]:

# Dropping Two irrelevant columns from the DataFrame

occupation_df.drop(['INFORMATION REQUESTED PER BEST EFFORTS','INFORMATION REQUESTED'],axis=0,inplace=True)


# In[49]:

# Merging the CEO and C.E.O. columns in the DataFrame

occupation_df.loc['CEO'] = occupation_df.loc['CEO'] + occupation_df.loc['C.E.O.']

occupation_df.drop('C.E.O.',inplace=True)


# In[50]:

# Plotting the final occupations of people who have made over a Million dollar in contribution

occupation_df.plot(kind='barh',figsize=(12,10))


# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:



