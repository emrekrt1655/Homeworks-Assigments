#!/usr/bin/env python
# coding: utf-8

# ### Task : Write a program that takes a number from the user and prints the result to check The examples of the desired output are as follows : input →  19 ⇉ output : 19 is a prime number   input →  10 ⇉ output : 10 is not a prime number

# In[3]:


print("""
*************

Prime Number or not?

*************
""")

number = input("Please enter positive digit number: ")
counter = 2

while not number.isdigit() :
    print("Error!!!")
    number = input("Please enter positive digit number: ")
    
if int(number) == 1 :
    print(number,"it is not a prime number")
elif int(number) == 2 :
    print(number,"it is a prime number") 
    
number = int(number)
    
while counter < number : 
        
    if number % counter == 0:
        a += 1
        print (number,"it is not a prime number")
        break
    else:
        print(number, "it is a prime number")
        break


# In[2]:


# Method 2

n = int(input("enter a number to check if it is a prime or not: "))

count = 0

for i in range (1, n+1) :
    if not (n % i) : count += 1
        
if (n == 0) or (n == 1) or (count >= 3) : print(n, "is not a prime number.")
else : print(n, "is a prime number.") 


# In[ ]:




