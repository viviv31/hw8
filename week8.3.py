#!/usr/bin/env python
# coding: utf-8

# In[23]:


import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
names = ['Bob','Jessica','Mary','John','Mel'] 
status = ['Senior','Freshman','Sophomore','Senior',
'Junior']
grades = [76,95,77,78,99]
GradeList = zip(names,grades)
y_pos = np.arange(len(status))


# In[24]:


plt.bar(y_pos, grades)
 
plt.xticks(y_pos, status)
 
plt.show()

