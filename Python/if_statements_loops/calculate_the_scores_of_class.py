#!/usr/bin/env python
# coding: utf-8

# ### Write a Python code that calculates the average of scores that students took in a math class at below.
# scores = {"Mary" : 85, "Susan": 75, "Barry" : 65, "Alexis" : 88, "Jane" : 45, "Tina" : 100, "Tom" : 90, "Tim": 60}

# In[1]:


scores = {"Mary" : 85, "Susan": 75, "Barry" : 65, "Alexis" : 88, "Jane" : 45, "Tina" : 100, "Tom" : 90, "Tim": 60}

sum_scores = 0

for i in scores.values():
    sum_scores += i
    
avr = sum_scores / len(scores)

print("the average of scores is", avr )


# In[ ]:




