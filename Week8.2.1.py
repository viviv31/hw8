#!/usr/bin/env python
# coding: utf-8

# In[5]:


import pandas as pd
import numpy as np
df=pd.read_excel("downloads/gradedata.xlsx")
df.head()


# In[6]:


df['gender_female'] = df.gender.map({'male':0, 'female':1})


# In[7]:


df.head()


# In[8]:


import statsmodels.formula.api as sm 
result = sm.ols(
formula='grade ~ age + exercise + hours',
data=df).fit() 
result.summary()


# In[9]:


import statsmodels.formula.api as sm 
result = sm.ols(
formula='grade ~ exercise + hours',
data=df).fit() 
result.summary()


# In[10]:


import statsmodels.formula.api as sm 
result = sm.ols(
formula='grade ~ exercise + hours + gender_female',
data=df).fit() 
result.summary()


# In[ ]:


#By just seeing the r-squared we can say that it improved by just a little by adding
#the dummy variable gender_female. However, we have to consider that this variable is not significant
#at the 5% significance level, we notice that given its p value.

