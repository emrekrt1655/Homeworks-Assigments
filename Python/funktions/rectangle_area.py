#!/usr/bin/env python
# coding: utf-8

# ### Write a Python program that calculates the area of the rectangle whose width and height are entered by using the function

# In[1]:


def rectangle_area(a,b):
    area = a * b
    print("The area of the rectangle is: ", area)
    return area

a = int(input("Please enter the width: "))
b = int(input("Please enter the height: "))

rectangle_area(a,b)


# In[ ]:




