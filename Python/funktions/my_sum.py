#!/usr/bin/env python
# coding: utf-8

# ### Define a function named my_sum to return the sum of all int type inputted numbers.

# In[2]:


def my_sum(*a):
    summ = 0
    b = list(a)
    for i in b:
        summ += i
    return summ


# In[3]:


my_sum(3,4,5,6,-3,-4)

