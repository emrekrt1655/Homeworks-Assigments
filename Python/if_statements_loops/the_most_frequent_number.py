#!/usr/bin/env python
# coding: utf-8

# In[1]:


numbers = [1, 2, 3, 7, 4, 3, 4, 4, 4, 4, 0, 3, 16, 3, 7]
item = max(numbers, key = numbers.count)

repetition = numbers.count(item)
print("the most frequent number is {} and it was {} times repeated".format(item, repetition))


# In[ ]:




