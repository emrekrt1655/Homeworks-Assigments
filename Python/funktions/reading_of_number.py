#!/usr/bin/env python
# coding: utf-8

# 
# ### Kullanıcıdan 2 basamaklı bir sayı alın ve bu sayının okunuşunu bulan bir fonksiyon yazın.
#     
#     
#       
#     
#         

# In[1]:


def reading ():
    a = input("Please enter 2 digits number: ")
    
    number = [0,1,2,3,4,5,6,7,8,9]

    digit_ten = ["ten", "twenty", "thirty", "forty", "fifty", "sixty","seventy", "eighty", "nighty",]
    exeption = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]

    if int(a[0]) == 1 and int(a[1]) in number: 
        print(exeption[int(a[1])])

    elif int(a[0]) in number:
        print(digit_ten[int(a[0])-1], end = " ")
        digit_one = ["","one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
        if int(a[1]) in number:
            print(digit_one[int(a[1])])


# In[2]:


reading()


# In[3]:


reading()
reading()
reading()
reading()
reading()


# In[ ]:




