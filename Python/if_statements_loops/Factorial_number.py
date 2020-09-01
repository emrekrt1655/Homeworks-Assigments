#!/usr/bin/env python
# coding: utf-8

# ### Q:Write a code to calculate factorial of a number entered by user. 

# In[1]:


fac = int(input("Enter a positive digit number"))
summ = 1

if fac == 0 :
    print("the factorial of number 0 is 1")

for i in range(1,fac+1):
    summ *= i
print("the  factorial of", fac,"is", summ)


# In[ ]:




