#!/usr/bin/env python
# coding: utf-8

# ### Her bir while döngüsünde kullanıcıdan bir sayı alın ve kullanıcının girdiği sayıları "toplam" isimli bir değişkene ekleyin. Kullanıcı "q" tuşuna bastığı zaman döngüyü sonlandırın ve ekrana "toplam değişkenini" bastırın.

# In[6]:


print("please enter 'q' in order to quit")
numm = input("Please enter a positiv number: ")

total = 0
while numm.isdigit():
    total += int(numm)
    numm = input("Please enter a positiv number: ")
    if numm == "q" :
        break
print("The summ of the given numbers is: ", total)


# In[ ]:




