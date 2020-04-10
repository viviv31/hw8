#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
get_ipython().run_line_magic('matplotlib', 'inline')
df=pd.read_excel("downloads/gradedata.xlsx")
df.head()


# In[4]:


y=df['grade'];
x= df['hours']


# In[5]:


plt.xlabel('hours'); plt.ylabel('grade')
plt.scatter(x,y)


# In[ ]:




