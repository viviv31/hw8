#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import geopandas as geo
import numpy as np
df=pd.read_excel("downloads/gradedata.xlsx")
df.tail()


# In[2]:


df.take(np.random.permutation(len(df))[:500])


# In[ ]:





# In[ ]:




