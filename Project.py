#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[3]:


data=pd.read_csv('telecom_churn_me.csv')


# In[4]:


data


# In[6]:


data.plot(kind='box')


# In[7]:


data.hist()


# In[8]:


data.isnull().sum()


# In[11]:


data.plot(kind='box',subplots=True,layout=(14,2),sharex=False,sharey=False,figsize=(20,40))


# In[12]:


data['POSTPAID_LINES'].plot(kind='box')


# In[13]:


data['BILL_AMOUNT']


# In[17]:


data['STATUS'].head(22)


# In[ ]:




