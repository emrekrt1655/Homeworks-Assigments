#!/usr/bin/env python
# coding: utf-8

# ###  Print the perfect number of numbers from 1 to 1000 on the screen. Write a function that returns whether a number is perfect.
# If the sum of the divisors of a number equals itself, this number is an excellent number. For example, 6 is an excellent number (1 + 2 + 3 = 6).

# In[24]:


def perfect(x):
    total = 0 
    for i in range(1,x):
        if x % i == 0:
            total += i
    return total


# In[25]:


my_list = list(range(1,1000))
my_sec_list = [i for i in my_list if i == perfect(i)]
print(my_sec_list)


# In[ ]:




