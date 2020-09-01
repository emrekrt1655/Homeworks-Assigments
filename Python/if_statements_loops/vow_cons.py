#!/usr/bin/env python
# coding: utf-8

# ### Write a Python code that counts how many vowels and constants a string has that a user entered. 

# In[2]:


print("In order to calculate how many vowels and constants in given word")
word = input("Please enter a word")
vowel = ["a","e","i","o","u"]
count_vowel = 0
count_constant = 0


for i in word :
    if i in vowel:
        count_vowel += 1
    else :
        count_constant += 1
        
print("the numbers of vowels in", word, count_vowel)
print("the numbers of constants in", word, count_constant)
        


# In[ ]:




