#!/usr/bin/env python
# coding: utf-8

# ### Given a non-empty string and an int n, return a new string where the character at index n has been removed. The value of n will be a valid index of a character in the original string (i.e. n will be in the range 0....len(str)-1 inclusive).

# In[1]:


def missing_char():
    word = input("word: ")
    n = int(input("char: "))
    word2 = word.replace(word[n],"")
    return word2


# In[2]:


missing_char()


# In[3]:


# method2

def missing_char2(word,n):
    front = word[:n]
    back = word[n+1:]
    return front + back


# In[6]:


word = "Istanbul"
n = 7
missing_char2(word,n)


# In[ ]:




