#!/usr/bin/env python
# coding: utf-8

# ### Get 3 numbers from the user and print the largest number on the screen.

# In[6]:


# Method 1
num_1 = int(input("The first number is: ")) 
num_2 = int(input("The second number is: "))
num_3 = int(input("The third number is: "))

if num_1 > num_2 and num_1 > num_3 :
    print("The largest number is: ", num_1)
elif num_2 > num_1 and num_2 > num_3 :
    print("The largest number is: ", num_2)
else:
    print("The largest number is: ", num_3)


# In[9]:


# Method 2
num_1 = int(input("The first number is: ")) 
num_2 = int(input("The second number is: "))
num_3 = int(input("The third number is: "))

my_list = [num_1, num_2, num_3]

my_list = sorted(my_list)
print("The largest number is: ", my_list[-1])


# In[ ]:




