#!/usr/bin/env python
# coding: utf-8

# In[42]:


import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
names = ['Bob','Jessica','Mary','John','Mel'] 
grades = [76,95,77,78,99]
GradeList = zip(names,grades)
df = pd.DataFrame(data = GradeList,
        columns=['Names', 'Grades']) 
get_ipython().run_line_magic('matplotlib', 'inline')


# In[41]:


import matplotlib.pyplot as plt 
df.plot()
displayText = "WOW" 
xloc = 0
yloc = 76
xtext = 8
ytext = 0 
plt.annotate(displayText,
             xy=(xloc, yloc), 
             xytext=(xtext,ytext), 
             xycoords=('axes fraction', 'data'), 
             textcoords='offset points')

