#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests


# In[2]:


url='https://en.wikipedia.org/wiki/List_of_U.S._states_and_territories_by_population'


# In[4]:


result=requests.get(url)


# In[5]:


result.status_code


# In[6]:


import bs4


# In[8]:


soup=bs4.BeautifulSoup(result.text,'lxml')


# In[9]:


contents=soup.prettify()


# In[10]:


print(contents)


# # Title

# In[36]:


soup.find('title')


# # Select class

# In[37]:


soup.find(class_="toctitle")


# In[51]:


res=soup.find_all(class_="toclevel-1 tocsection-1")


# In[52]:


for item in res:
    print (item.text)


# In[64]:


res1=soup.select('li',{'class':"toclevel-1 tocsection"})[:10]


# In[65]:


for item in res1:
    print (item.text)


# # Import table

# In[66]:


import pandas as pd 


# In[67]:


table=pd.read_html(url)


# In[68]:


len(table)


# In[69]:


table[2]


# In[70]:


table[2].head()


# In[72]:


table[2].to_csv('Web scraping_new.csv')


# In[ ]:




