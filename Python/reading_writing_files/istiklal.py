#!/usr/bin/env python
# coding: utf-8

# ### add a new empty line in every 4 lines in the given istiklal.txt

# In[2]:


with open("istiklal.txt", "r", encoding="utf-8") as file:
    print(file.read())


# In[3]:


with open("istiklal.txt", "r", encoding="utf-8") as file:
    ist = file.readlines()


# In[4]:


ist


# In[7]:


counter = 0

with open("istiklal.txt", "w", encoding="utf-8") as file:
    for i in ist:
        counter += 1
        if counter % 4 == 0 :
            file.write(i + "\n")
        else :
            file.write(i)


# In[8]:


with open("istiklal.txt", "r", encoding="utf-8") as file:
    print(file.read())


# ### Task 2 :
# Add the old text below the new one

# In[9]:


with open("istiklal.txt", "r", encoding="utf-8") as file:
    istikk = file.readlines()


# In[10]:


istikk


# In[11]:


with open("istiklal.txt", "a", encoding="utf-8") as file:
    file.write("\n")
    for i in istikk:
        if i == "\n":
            i.replace("\n","")
        else:
            file.write(i)
            
with open("istiklal.txt", "r", encoding="utf-8") as file:
    print(file.read())


# In[ ]:




