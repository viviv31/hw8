#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
names = ['Bob','Jessica','Mary','John','Mel'] 
grades = [76,95,77,78,99]
bsdegrees = [1,1,0,0,1]
msdegrees = [2,1,0,0,0]
phddegrees = [0,1,0,0,0]

gradelist = zip(names,grades,bsdegrees,msdegrees,phddegrees)
df = pd.DataFrame(data=gradelist,
                 columns=['names', 'grades', 'bsdegrees' , 'msdegrees' , 'phddegrees'])
df


# In[5]:


df['grades'].count()


# In[4]:


df['grades'].mean()


# In[6]:


df['grades'].std()


# In[7]:


df['grades'].min()


# In[8]:


df['grades'].max()


# In[9]:


df['grades'].quantile(.25)


# In[10]:


df['grades'].quantile(.50)


# In[11]:


df['grades'].quantile(.75)


# In[12]:


df['bsdegrees'].count()


# In[13]:


df['bsdegrees'].mean()


# In[14]:


df['bsdegrees'].std()


# In[15]:


df['bsdegrees'].min()


# In[16]:


df['bsdegrees'].max()


# In[17]:


df['bsdegrees'].quantile(.25)


# In[18]:


df['bsdegrees'].quantile(.5)


# In[19]:


df['bsdegrees'].quantile(.75)


# In[20]:


df['msdegrees'].count()


# In[21]:


df['msdegrees'].mean()


# In[22]:


df['msdegrees'].std()


# In[23]:


df['msdegrees'].min()


# In[24]:


df['msdegrees'].max()


# In[25]:


df['msdegrees'].quantile(.25)


# In[26]:


df['msdegrees'].quantile(.5)


# In[27]:


df['msdegrees'].quantile(.75)


# In[28]:


df['phddegrees'].count()


# In[29]:


df['phddegrees'].mean()


# In[30]:


df['phddegrees'].std()


# In[31]:


df['phddegrees'].min()


# In[32]:


df['phddegrees'].max()


# In[33]:


df['phddegrees'].quantile(.25)


# In[34]:


df['phddegrees'].quantile(.5)


# In[35]:


df['phddegrees'].quantile(.75)


# In[ ]:




