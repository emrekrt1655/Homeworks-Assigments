#!/usr/bin/env python
# coding: utf-8

# In[1]:


sea = open("fishes.txt", "r")

print(sea.read())
sea.close()


# In[2]:


sea = open("fishes.txt", "r")

print(sea.read(33))


sea.close()


# In[3]:


sea = open("fishes.txt", "r")

print(sea.read(33))
print(sea.read(23))
print(sea.read(4))


sea.close()


# In[6]:


sea = open("fishes.txt", "r")

print(sea.read(33))
sea.seek(0)
print(sea.read(25))
print(sea.read(3))


sea.close()


# In[7]:


sea = open("fishes.txt", "r")

print(sea.read(33))
sea.seek(0)
print(sea.read(25))
print(sea.read(3))
print(sea.tell())


sea.close()


# In[9]:


# Keyword Argument

sea = open(mode = "r", file = "fishes.txt")

print(sea.read(33))
sea.seek(0)
print(sea.read(25))
print(sea.read(3))
print(sea.tell())


sea.close()


# ###  
# 1) Create a txt file named rumi.txt in your current directory consisting of the following quotes of Rumi
# 2) Read and display the entire contents of this file at once
# 3) Display the first two lines using read() method
# 4) Display the next 13 chars of the content
# 5) Display the current location of cursor
# 6) Bring the cursor onto beginning of the second line again
# 7) close the file

# In[10]:


rumi = open("rumi.txt", "r")

print(rumi.read())

rumi.close()


# In[11]:


rumi = open("rumi.txt", "r")

print(rumi.read(35))

rumi.close()


# In[12]:


rumi = open("rumi.txt", "r")

print(rumi.read(35))
print(rumi.read(13))

rumi.close()


# In[13]:


rumi = open("rumi.txt", "r")

print(rumi.read(35))
print(rumi.read(13))
print(rumi.tell())

rumi.close()


# In[14]:


rumi = open("rumi.txt", "r")

print(rumi.read(35))
print(rumi.read(13))
print(rumi.tell())
print(rumi.seek(16))
print(rumi.read(20))

rumi.close()


# In[18]:


sea = open("fishes.txt","r")
print(sea.readline())
print(sea.readline())
print(sea.readline())
sea.close()


# In[19]:


sea = open("fishes.txt","r")
print(sea.readline(13))
print(sea.readline(13))
print(sea.readline(13))
print(sea.readline(13))
sea.close


# In[20]:


with open("dummy.txt", "w", encoding = "utf-8") as file:
    file.write("this is my first line")


# In[22]:


with open("dummy.txt", "r", encoding = "utf-8") as file:
    print(file.read())


# In[25]:


with open("dummy.txt", "w", encoding = "utf-8") as file:
    file.write("this is my second line")


# In[26]:


with open("dummy.txt", "r", encoding = "utf-8") as file:
    print(file.read())


# In[29]:


with open("dummy.txt", "w", encoding = "utf-8") as file:
    file.write("this is my first line\nthis is my second line")


# In[30]:


with open("dummy.txt", "r", encoding = "utf-8") as file:
    print(file.read())


# In[ ]:




