#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


# In[4]:


#reading the dataset
df = pd.read_csv("Metadata_Country.csv")


# In[5]:


df.head()


# In[3]:


#bar chart plotting
gender_counts = df['Region'].value_counts()
bar_width = 0.9
x=range(len(gender_counts.index))


plt.bar(gender_counts.index,gender_counts.values)
plt.xlabel('Region')
plt.ylabel('Count')
plt.title('Distribution of Region')


plt.xticks(x,gender_counts.index,rotation=45)
plt.tight_layout()
plt.show()


# In[ ]:




