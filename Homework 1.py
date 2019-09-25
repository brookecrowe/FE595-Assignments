#!/usr/bin/env python
# coding: utf-8

# In[7]:


import requests
import re


# In[60]:


#Scrape screen
response = requests.get('https://theyfightcrime.org')
text = str(response.content)
#Define text input
test_str = text


# In[68]:


hes = []
shes = []


# In[57]:


#Create Regular Expression for the He character
def his_line(text):
    regex_m = r"\bHe\b(.+)\bShe\b"
    #Find matches
    matches = re.search(regex_m, test_str, re.MULTILINE)
    #Clean match, drop 'She's'
    hisStr = matches.group(0)
    hisStr = hisStr[:-4]
    #Add to His list
    hes.append(hisStr)


# In[59]:


#Create Regular Expression for the She character
def her_line(text):
    regex_f = r"\bShe\b(.+)\bThey fight\b"
    #Find matches
    matches = re.search(regex_f, test_str, re.MULTILINE)
    #Clean match, drop 'They'
    herStr = matches.group(0)
    herStr = herStr[:-11]
    #Add to Her list
    shes.append(herStr)


# In[69]:


for i in range(50):
    #Scrape screen
    response = requests.get('https://theyfightcrime.org')
    text = str(response.content)
    #Define text input
    test_str = text
    his_line(test_str)
    her_line(test_str)


# In[70]:


with open('hesfile.txt', 'w') as filehandle:
    for listitem in hes:
        filehandle.write('%s\n' % listitem)
        
with open('shesfile.txt', 'w') as filehandle:
    for listitem in shes:
        filehandle.write('%s\n' % listitem)

