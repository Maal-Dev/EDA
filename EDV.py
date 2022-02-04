#!/usr/bin/env python
# coding: utf-8

# In[2]:


# Import Library
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt #visualization
import seaborn as sns #visualization
get_ipython().run_line_magic('matplotlib', 'inline')
sns.set(color_codes=True)


# In[57]:


#Import Table
table = pd.read_csv('C://Users\my\Desktop\Data Analysis\data\data.csv')
table.head(5)


# In[4]:


# last 5 rows
table.tail(5)


# In[5]:


# Check Data Type
table.dtypes


# In[58]:


#Drop some Column
table1 = table.drop(['Engine Fuel Type','Market Category','Vehicle Style','Popularity','Number of Doors','Vehicle Size'],axis=1)
table1.head(5)


# In[59]:


table1 = table1.rename(columns ={'Engine Hp':'Hp','Engine Cylinders': 'Cylinders','Transmission Type':'Transmission','Driven_Wheels':'Drive Mode','highway MPG':'MPG-H','city mpg':'MPG-C','MSRP': 'Price'})
table1.head(5)


# In[60]:


table1.shape


# In[61]:


duplicate_ = table1[table1.duplicated()]
duplicate_


# In[62]:


table1.count()


# In[63]:


table1.drop_duplicates()


# In[64]:


table1.isnull().sum()


# In[65]:


table1=table1.dropna()
table1.count()


# In[66]:


table1.isnull().sum()


# In[67]:


sns.boxplot(x=table1['Price'])


# In[55]:


sns.boxplot(x=table1['Engine HP'])


# In[42]:


sns.boxplot(x=table1['Cylinders'])


# In[68]:


Q1 = table1.quantile(0.25)
Q3 = table1.quantile(0.75)
IQR = Q3 - Q1
print(IQR)


# In[71]:


table1 = table1[~((table1 < (Q1- 1.5 * IQR)) |(table1 > (Q3 + 1.5 * IQR))).any(axis=1)]
table1.shape


# In[82]:


table1.Make.value_counts().nlargest(50).plot(kind='bar',figsize=(10,5))


# In[88]:


plt.figure(figsize=(20,10))
c = table1.corr()
sns.heatmap(c, cmap='BrBG', annot = True)
c


# In[93]:


fig, ax = plt.subplots(figsize=(10,6))
ax.scatter(table1['Engine HP'], table1['Price'])
ax.set_xlabel('HP')
ax.set_ylabel('Price')
plt.show()


# In[ ]:




