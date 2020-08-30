#!/usr/bin/env python
# coding: utf-8

# ### Task:
# 
# Find out if a given number is an "Armstrong Number".
# 
# An n-digit number that is the sum of the nth powers of its digits is called an n-Armstrong number.
# Examples : 371 = 33 + 73 + 13; 9474 = 94 + 44 + 74 + 44; 93084 = 95 + 35 + 05 + 85 + 45.
# 
# Write a Python program that; takes a positive integer number from the user, checks the entered number if it is Armstrong, consider the negative, float and any entries other than numeric values then display a warning message to the user.

# In[1]:


print("""
************

Armstrong or not?

************
""")

num = input("Please enter a positive number: ")

total = 0

while not num.isdigit():
    
    print("It is an invalid entry. Don't use non-numeric, float, or negative values! ")
    
    num = input("Please enter a positive number: ")
    
for i in num:
    
    total += int(i) ** int(len(num))
    
if total == int(num):
    print(total, "is a armstrong number")

else:
    print(num, "is not a armstrong number")


# In[2]:


# Method 2

while True:
    number = input("enter a positive number : ")
    digits = len(number)
    summ = 0
    if not number.isdigit() :
        print(number, "it is an invalid entry. Don't          use non-numeric, float, or negative values!")
    elif int(number) >= 0 :
        for i in range(digits):
            summ += int(number[i]) ** digits
        if summ == int(number) :
            print(number, "is an Armstrong number. ")
            break
        else:
            print(number, "is not an Armstrong number. ")
            break


# In[ ]:




