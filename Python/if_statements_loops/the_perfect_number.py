#!/usr/bin/env python
# coding: utf-8

# ### Kullanıcıdan aldığınız bir sayının mükemmel olup olmadığını bulmaya çalışın.
# 
# Bir sayının kendi hariç bölenlerinin toplamı kendine eşitse bu sayıya "mükemmel sayı" denir. Örnek olarak, 6 mükemmel bir sayıdır. (1 + 2 + 3 = 6) Kullanıcıdan aldığınız bir sayının mükemmel olup olmadığını bulmaya çalışın.
# 
# Bir sayının kendi hariç bölenlerinin toplamı kendine eşitse bu sayıya "mükemmel sayı" denir. Örnek olarak, 6 mükemmel bir sayıdır. (1 + 2 + 3 = 6)

# In[3]:


the_number = int(input("Please enter a positive number: "))

summ = 0
for i in range(1, the_number):
    if the_number % i == 0:
        summ += i
if summ == the_number:
    print(the_number, " is a perfect number.")
else:
    print(the_number, " is not a perfect number.")


# In[ ]:




