#!/usr/bin/env python
# coding: utf-8

# ### Please reverse the text below without using text indexing methods. Please create a loop for solution.  text = “Clarusway”

# In[4]:


# Method 1
text = "Clarusway"
reversed_text = ""
index = len(text)

while index > 0:
    reversed_text += text[index-1]
    index = index - 1
print(reversed_text)


# In[3]:


# Method 2
text = "Clarusway"
newtext = ""
for i in range(len(text)-1, -1, -1):
   newtext += text[i]
print(newtext)


# In[ ]:




