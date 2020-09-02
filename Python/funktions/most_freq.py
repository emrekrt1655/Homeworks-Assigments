#!/usr/bin/env python
# coding: utf-8

# ### Given a list, return the most frequent (repeating) element.

# In[2]:


def most_freq(*a):
    b = list(a)
    return max(b, key= b.count)


# In[3]:


most_freq(1,2,3,4,5,6,6,4,3,232,3,3,3,3,3)


# In[4]:


# Method 2

def most_freq2(my_list):
    return max(my_list, key= my_list.count)
my_list = [1,2,3,4,5,6,6,4,3,232,3,3,3,3,3]


# In[5]:


most_freq2(my_list)
    

