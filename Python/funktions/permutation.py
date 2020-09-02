#!/usr/bin/env python
# coding: utf-8

# ###  Define a “function” to calculate permutation of 2 numbers.
# Reminder: P(n,r) = n!/(n-r)!
# Clue: Defining a function that calculates factorial of given number, may be helpful.
#  
# 

# In[9]:


# Method 1
def permutation(n, r):
    n_fac = 1
    r_fac = 1
    if n < r :
        print("Invalid entry. n must be         higher than r")
        return False
    else:
        for i in range(1, n + 1):
            n_fac *= i
        for i in range(1, n- r + 1):
            r_fac *= i
            
    print("The permutation of ({},{}) is {} ".format(n,r, n_fac / r_fac))
    return n_fac / r_fac

print("please enter the numbers in order to calculate the permutation")
n = int(input("n: "))
r = int(input("r: "))

permutation(n, r)


# In[10]:


# method 2

def fac(k):
    fact = 1
    for i in range(1, k+1):
        fact *= i
    return fact

def per(l, m):
    if l < m :
        print("Invalid entry. l must be         higher than m")
        return False
    else:
        result = fac(l) / fac(l - m)
    print("The permutation of ({},{}) is {} ".format(l, m, result))
    return result

l = int(input("l: "))
m = int(input("m: "))

per(l, m)


# In[ ]:




