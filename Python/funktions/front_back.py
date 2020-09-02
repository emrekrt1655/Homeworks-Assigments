#!/usr/bin/env python
# coding: utf-8

# ### Given a string, return a new string where the first and last chars have been exchanged.

# In[13]:


def front_back():
    word = input("Word: ")
    if len(word) == 1 : print(word)
    else: 
        my_list = [i for i in word]
        my_list.append(my_list.pop(0))
        my_list.insert(0,my_list.pop(-2))
        for i in my_list:
            print(i, end="")
    
    


# In[14]:


front_back()


# In[15]:


front_back()


# In[16]:


#Method 2

def front_back2(word):
    if len(word) <= 1:
        return word
    else:
        mid = word[1:-1]
        return word[-1] + mid + word[0]


# In[17]:


word = 'Bursa'
front_back2(word)


# In[19]:


word = "a"
front_back2(word)


# In[ ]:




