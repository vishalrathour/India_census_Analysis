#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


data = pd.read_csv('India_Census_2011.csv')


# In[3]:


data


# In[4]:


data.head()


# In[5]:


data.tail()


# In[6]:


data.count()


# In[7]:


data['State_name'].value_counts()


# In[8]:


data['District_name'].value_counts()


# In[9]:


data.shape


# In[10]:


data['District_name'].unique()


# In[11]:


data.nunique()


# In[12]:


data.index


# In[13]:


data.columns


# In[14]:


data.isnull()


# In[15]:


data.isnull().sum()


# In[16]:


data.dtypes


# In[17]:


data.info()


# ### Q) 1. How will you hide the indexes of the DataFrame.

# In[18]:


# syntax
# df.style.hide_index()


# In[19]:


data.head()


# In[20]:


data.style.hide_index(2)  # when you not give perameter in hide_index the function authmatic remove 0th index in the dataframe
                          # if we want this format file creat a variable and write this syntax and stor the value


# In[21]:


data.head()


# ### Q) 2. How can we set the caption / heading on the dataframe.

# In[22]:


data.head()


# In[23]:


# syntax
# df.style.set_caption('caption title')


# In[24]:


data.style.set_caption('India cansus 2011 Dataset written by -- Vishal')


# ### Q) 3. Show the records related withe the Districts - New Delhi , Lucknow , Jaipur And your Districts name .

# In[25]:


data[data['District_name'].isin(['New Delhi' , 'Lucknow' , 'Jaipur','Firozabad'])]


# # Q) 4. Calculate state-wise.
# # A -  Total No. of population.
# # B -  Total No. of population with different religions. 

# In[26]:


data.dtypes


# In[27]:


data['State_name'].unique()


# In[28]:


data[data['District_name']=='Firozabad']


# # A.

# In[29]:


data.head()


# In[30]:


data.groupby('State_name').Population.sum()


# In[31]:


data.groupby('State_name').Population.sum().sort_values(ascending=True)


# In[32]:


data.groupby('State_name').Population.sum().sort_values(ascending=False)


# # B.

# In[33]:


data.head()


# In[34]:


data.columns


# In[35]:


data.groupby('State_name')['Hindus','Christians','Sikhs','Muslims','Buddhists','Jains'].sum()


# In[36]:


data.groupby('State_name')['Hindus','Christians','Sikhs','Muslims','Buddhists','Jains'].sum().sort_values(by='Hindus')


# In[37]:


data.groupby('State_name')['Hindus','Christians','Sikhs','Muslims','Buddhists','Jains'].sum().sort_values(by='Muslims')


# In[38]:


data.groupby('State_name')['Hindus','Christians','Sikhs','Muslims','Buddhists','Jains'].sum().sort_values(by='Christians')


# In[39]:


data.groupby('State_name')['Hindus','Christians','Sikhs','Muslims','Buddhists','Jains'].sum().sort_values(by='Sikhs')


# In[40]:


data.groupby('State_name')['Hindus','Christians','Sikhs','Muslims','Buddhists','Jains'].sum().sort_values(by='Jains')


# In[41]:


data.groupby('State_name')['Hindus','Christians','Sikhs','Muslims','Buddhists','Jains'].sum().sort_values(by='Buddhists')


# In[42]:


plt.plot(data.Female,data.Male,color='r')
# plt.()
plt.show()


# In[43]:


data.style.set_caption('Moti')


# ### Q) 5. How many Male workers in were there maharashtra state ? 

# In[44]:


data[data['State_name']=='MAHARASHTRA'].Male_Workers.sum()


# In[45]:


data[data['State_name']=='MAHARASHTRA']


# ### Q) 6. How to set a column an index of the Dataframe ?

# In[46]:


data


# In[47]:


data.set_index('District_code')


# ### Q) 7. Add a suffix to the column names.

# ### Q) 8. Add a prefix to the column names.

# In[48]:


#syntax
 
# df = df.add_suffix('_suffix')
# df = df.add_prefix('prefix_')


# In[49]:


data.head(2)


# In[50]:


data.add_suffix('_suffix')


# In[51]:


data.add_prefix('prefix_')

