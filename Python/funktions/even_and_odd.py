#!/usr/bin/env python
# coding: utf-8

# ### Arbitrary Argument

# In[1]:


#method 1

def slicer(*a):
    even_list= list()
    odd_list = list()
    for i in a:
        if i % 2 == 0 :
            even_list.append(i)
        else:
            odd_list.append(i)
    print("even_list: ", even_list)
    print("odd_list: ", odd_list)


# In[2]:


slicer(1, 2, 3, 4, 5, 6, 7, 8 ,9)


# In[3]:


# method 2
def slicer(*a):
    even = [i for i in a if i%2 == 0]
    odd = [j for j in a if j%2 != 0]
    print("even : ", even)
    print("odd : ", odd)


# In[4]:


slicer(1, 2, 3, 4, 5, 6, 7, 8 ,9)


# In[ ]:




