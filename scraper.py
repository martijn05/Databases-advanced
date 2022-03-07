#!/usr/bin/env python
# coding: utf-8

# In[14]:


from bs4 import BeautifulSoup
import numpy as np
import pandas as pd
import re
import requests


# In[15]:


url = "https://www.blockchain.com/btc/unconfirmed-transactions"
r = requests.get(url)


# In[16]:


results = []
Time = []
Hash = []


# In[17]:


c = r.content
soup = BeautifulSoup(c)


# In[18]:



for link in soup.find_all("div",class_= "sc-1au2w4e-0 emaUuf" ):
    Time.append(link.getText())

    strtime = "{}".format(Time)

    x = re.sub("Time", "", strtime)
    
    x = "{}".format(x)

    print(x)


# In[19]:


for link in soup.find_all("div",class_= "sc-1au2w4e-0 fTyXWG" ):
    print(link.getText())
    


# In[20]:


for link in soup.find_all("div",class_= "sc-1au2w4e-0 bTgHwk" ):
    Hash.append(link.getText())

strhash = "{}".format(Hash)
    
y = re.sub("Hash", "", strhash)

y = "{}".format(y)

print(y)


# In[ ]:





# In[ ]:





# In[ ]:





# In[10]:


BTC_DF = pd.DataFrame(results, columns = ['Hash', 'Time'])
BTC_DF = BTC_DF.astype([{'Hash': str, 'Time': str}])


# In[ ]:





# In[ ]:





# In[ ]:




