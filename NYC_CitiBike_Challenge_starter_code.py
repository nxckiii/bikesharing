#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[3]:


# 1. Create a DataFrame for the 201908-citibike-tripdata data. 
citybike_august_df = pd.read_csv(r"C:\Users\nisha\Desktop\Class\Module 14\bikesharing\bikesharing.csv")


# In[17]:


# 2. Check the datatypes of your columns. 
bikesharing_df.dtypes


# In[16]:


# 3. Convert the 'tripduration' column to datetime datatype.
citybike_august_df['tripduration'] = pd.to_datetime(bikesharing.csv['tripduration'], unit='s')


# In[15]:


# 4. Check the datatypes of your columns. 
bikesharing.csv_df.dtypes


# In[14]:


# 5. Export the Dataframe as a new CSV file without the index.
bikesharing.to_csv("bikesharing.csv", index = False)


# In[18]:


citybike_august_df.to_csv("bikesharing", index = False)


# In[ ]:




