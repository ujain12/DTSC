#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
import pandas as pd
from bs4 import BeautifulSoup


# In[3]:


url = "https://webpages.charlotte.edu/mscipion/"

r= requests.get(url)


# In[5]:


soup = BeautifulSoup(r.text, 'html.parser')
table = soup.find('table')
print(table)


# In[6]:


headers = table.find_all("th")
print(headers)


# In[7]:


titles = []

for i in headers:
    title = i.text
    titles.append(title)
    
print(titles)


# In[11]:


df1= pd.DataFrame(columns=titles)
df1.describe()


# In[13]:


rows = table.find_all("tr")


# In[17]:


for i in rows[1:]:
    data = i.find_all("td")
    row = [tr.text for tr in data]
    l=len(df1)
    df1.loc[l] = row

df1


# In[ ]:




