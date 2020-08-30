#!/usr/bin/env python
# coding: utf-8

# ### Task :
# Now, think of that we have a list of flower names.
# Let's write them to a file named flowers.txt each on separate lines one ofter another and separated by an empty line.

# In[1]:


flowers = ["Jasmine","Rose", "Lily", "Daisy", "Tulip"]


# In[2]:


with open("flowers.txt", "w", encoding = "utf-8") as file:
    for flower in flowers :
        file.write(flower + "\n" * 2)


# In[3]:


with open("flowers.txt", "r", encoding = "utf-8") as file:
    print(file.read())


# In[ ]:




