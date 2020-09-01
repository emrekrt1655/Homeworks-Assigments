#!/usr/bin/env python
# coding: utf-8

# ### Task : Create a list consisting of Fibonacci numbers from 1 to 55 using control flow statements.

# In[1]:


fibonacci = [1, 1]

for i in fibonacci :
    if fibonacci[-1] == 55:
        break
    fibonacci.append(fibonacci[-1]+fibonacci[-2])
        
print("fibonacci → ", fibonacci)      


# In[4]:


# method 2

fibo = []

for i in range(-2,8) :
    if i < 0 : fibo.append(1)
    else : fibo.append(fibo[i] + fibo[i+1])

print("fibonacci → ", fibo )
    


# In[ ]:




