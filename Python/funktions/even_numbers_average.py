#!/usr/bin/env python
# coding: utf-8

# ### Write the Python program that finds the average of the even numbers between the 2 numbers entered by the user
# 

# In[2]:


# method 1
def avr_even_num(num_1,num_2):
    total = 0
    even = [i for i in range(num_1,num_2) if i % 2 == 0]
    for i in even :
        total += i
    avr = total / len(even)
    print("The average of the even numbers is ", avr)
    return avr

num_1 = int(input("The first number is: "))
num_2 = int(input("The second number is: "))

avr_even_num(num_1, num_2)


# In[3]:


# method 2

def even(num):
    return num % 2 == 0

summ = 0
count = 0

a = int(input("The first number is: "))
b = int(input("The second number is: "))

for i in range(a,b):
    if(even(i)):
        summ += i
        count += 1
        
print("The average of the even numbers is ", summ/count)


# In[ ]:




