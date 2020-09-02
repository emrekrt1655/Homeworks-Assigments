#!/usr/bin/env python
# coding: utf-8

# ###  Write the Python program that calculates the area of the circle whose radius is entered using the function.
# 

# In[4]:


def area_circle(r):
    area = (3.14 * (r ** 2))
    print("Area of the circle is :", area)
    return area
r = int(input("please enter the radius"))

area_circle(r)


# In[ ]:




