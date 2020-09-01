#!/usr/bin/env python
# coding: utf-8

# ### Count the number of each letter in a sentence.
# 
# The department you work for undertook a project construction that makes word / text analysis. You are asked to calculate the number of letters or any chars in the sentences entered under this project.
# 
# Write a Python program that;
# takes a sentence from the user,
# counts the number of each letter of the sentence,
# collects the letters/chars as a key and the counted numbers as a value in a dictionary.
# 
# hippo runs to us!	
# {'s': 2, 'r': 1, 't': 1, 'h': 1, 'n': 1, 
# 'i': 1, 'u': 2, 'o': 2, 'p': 2, ' ': 3    
#     
# 

# In[2]:


sentence = input("please enter a sentence: ")
letter = list(sentence)
number = []

for i in letter:
    number.append(letter.count(i))

print(dict(zip(letter,number)))


# In[3]:


# Method 2

sentence_2 = input("please enter a sentence: ")
dicti = {}

for i in sentence_2:
    keys = dicti.keys()
    if i in keys :
        dicti[i] += 1
    else:
        dicti[i] = 1
print(dicti)


# In[ ]:




