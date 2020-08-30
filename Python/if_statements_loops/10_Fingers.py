#!/usr/bin/env python
# coding: utf-8

# In[2]:


left =set("qwertasdfgzxcv")
right =set("yuıophjklnm")

word = input("Please enter a word: ")
set_word = set(word)

left_bool = bool(set_word.difference(left))
rigth_bool = bool(set_word.difference(right))
print(left_bool and rigth_bool)


# In[ ]:




