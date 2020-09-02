#!/usr/bin/env python
# coding: utf-8

# ### Write a function that prints the numbers from 1 to 100 that make up the Pythagorean triangle on the screen. 

# In[21]:



def pisagor(a):
    my_list = list(range(1, a + 1))
    my_sec_list = []
    my_thi_list = []
    my_fourth_list = []
    my_fifth_list = []
    
    for i in my_list:
        for j in my_list:
            if str((i**2 + j**2) ** 0.5)[-1] == "0" :
                my_sec_list.append(i)
                my_thi_list.append(j)
                my_fourth_list.append(int((i**2+j**2)**0.5))
    
    
        
    
    d = (zip(my_sec_list,my_thi_list))
    e = dict(zip(d,my_fourth_list))
    e = dict(sorted(e.items(), key = lambda item : item[1]))
    temp=[]
    res = dict()
    for key,val in e.items():
        if val not in temp:
            temp.append(val)
            res[key]=val
    print(res)
    


# In[22]:


pisagor(100)


# In[ ]:




