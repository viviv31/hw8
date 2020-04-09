#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
import geopandas as geo
import numpy as np
df=pd.read_excel("downloads/gradedata.xlsx")
df.head()


# In[4]:


df=df.sort_values(by=['fname','age','grade'], ascending =[True, True, True])
df.head()


# In[ ]:





# In[ ]:




