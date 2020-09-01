#!/usr/bin/env python
# coding: utf-8

# ### Task : Print the prime numbers which are between 1 to entered limit number (n).
# 
# You can use a nested for loop.
# Collect all these numbers into a list
# The desired output for n=100 :

# In[1]:


n= (int(input("Please enter a digit number in order to creat a prime list until this number: ")))

nat_num = list(range(2,n))

not_pri_num = []

for i in nat_num :
    for j in range(2,i):
        if i % j == 0 :
            not_pri_num.append(i)

nat_num = set(nat_num)

not_pri_num = set(not_pri_num)

desired = list(nat_num.difference(not_pri_num))

print(desired)


# In[ ]:




