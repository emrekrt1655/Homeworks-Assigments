#!/usr/bin/env python
# coding: utf-8

# ### **Kwargs

# In[1]:


# Method 1

def organizer(**kwargs):
    names = [i for i in kwargs.keys()]
    ages = [i for i in kwargs.values()]
    
    print("names = ",names)
    print("ages =", ages)


# In[2]:


organizer(Ahmet = 33, Mehmet = 22, Tulin = 44, Fatma = 2)


# In[5]:


# Method 2

def organizer(**people):
    name = []
    age = []
    for key, value in people.items():
        name.append(key)
        age.append(value)
    print("name = ",name)
    print("age =", age)


# In[6]:


organizer(Ahmet = 33, Mehmet = 22, Tulin = 44, Fatma = 2)


# In[ ]:




