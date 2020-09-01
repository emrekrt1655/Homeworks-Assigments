#!/usr/bin/env python
# coding: utf-8

# ### Now let's do the geometric shape calculation. First, ask the user if he wants to find the type of triangle or quadrilateral.
# 
# If the user replies "Rectangle", ask for 4 edges and try to find out if this rectangle is a square, rectangle, or an ordinary quadrilateral.
# 
# If the user replies "Triangle", ask for 3 edges and try to find out whether this triangle is equilateral triangle, isosceles triangle or is an ordinary triangle. If the given edges do not specify a triangle, write "No triangle" on the screen.
# 
# If you do not know the condition of specifying a triangle, you can look online.
# 
# You will also need to find absolute value in this problem. For this, you can use the abs () function, which is a Pythonda ready function. Usage is as follows;

# In[19]:


wanted = input("Please enter which you want to calculate geometric shape Triangle or Quadrilateral: ")
wanted = wanted.title()
if wanted == "Triangle" :
    a = int(input("The first edge: "))
    b = int(input("The second edge: "))
    c = int(input("The third edge: "))
    if (abs(a-b) < c < abs(a+b)) or (abs(a-c) < b < abs(a+c)) or (abs(b-c) < a < abs(c+b))  :  
        if a == b and a == c :
            print("This is an equilateral triangle")
        elif a == b or a == c or b == c :
            print("This is an isosceles triangle")
        else:
            print("This is an ordinary triangle")
    else:
        print("you could not make a triangle with this values")
    
        
elif wanted == "Quadrilateral":
    k = int(input("The first edge: "))
    l = int(input("The second edge: "))
    m = int(input("The third edge: "))
    n = int(input("The fourth edge: "))
    if k == l and k == m and k == n :
        print("This is a square")
    elif (k == l and m == n) or (k == m and l == n) or (k == n and m == l):
        print("This is a rectangle")
    else:
        print("This is an ordinary quadrilateral")
else:
    print("There is an invalid entry")
    


# In[ ]:




