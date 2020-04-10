#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
get_ipython().run_line_magic('matplotlib', 'inline')
df=pd.read_excel("downloads/gradedata.xlsx")
df.head()


# In[3]:


df.hist(column="age", by="gender")

