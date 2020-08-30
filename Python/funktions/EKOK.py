#!/usr/bin/env python
# coding: utf-8

# ### Write a function that takes 2 numbers from the user and returns the smallest multiple of these numbers (EKOK).

# In[1]:


from modules.tlcdd import tlcd


# In[2]:


def EKOK(x,y):
    
    return (x * y)  / (tlcd(x, y))


# In[16]:


EKOK(15,20)


# In[11]:


# Method 2
def prime(a):
    count = 0

    for i in range (1, a+1) :
        if not (a % i) : count += 1
        
    if (a == 0) or (a == 1) or (count >= 3) : return None
    else : return a


# In[12]:


def EKOK2(c,d):
    cd_list = []
    counter = 2
    ekok = 1
    while c != 1 or d != 1:
        if c % counter == 0 or d % counter == 0:
            if counter == prime(counter):
               
                if c % counter == 0 and d % counter != 0:
                    c = c / counter
                    cd_list.append(counter)
                elif d % counter == 0 and c % counter != 0:
                    d = d / counter
                    cd_list.append(counter)
                elif c % counter == 0 and d % counter == 0:
                    c = c / counter
                    d = d / counter
                    cd_list.append(counter)
        elif c % counter != 0 and d % counter != 0 :
            counter += 1
    for i in cd_list:
        ekok *= i
    print(cd_list)
    return ekok
        
                    


# In[17]:


EKOK2(15,20)


# In[ ]:




