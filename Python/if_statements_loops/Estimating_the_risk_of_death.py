#!/usr/bin/env python
# coding: utf-8

# ### Task : Estimating the risk of death from coronavirus. Write a program that;
# 
# Takes "Yes" or "No" from the user as an answer to the following questions :
# 
# Are you a cigarette addict older than 75 years old? Variable → age
# 
# Do you have a severe chronic disease? Variable → chronic
# 
# Is your immune system too weak? Variable → immune
# 
# Set a logical algorithm using boolean logic operators (and/or)  and use if-statements with the given variables in order to print out us a message : "You are in risky group"(if True ) or "You are not in risky group" (if False).)

# In[1]:


print("""
***********

Are You in a risk group or not?

Please answer the questions as YES or NO

************
""")

age = input("Are you a cigarette addict older than 75 years old? ")
age = age.title()
chronic = input("Do you have a severe chronic disease? ")
chronic = chronic.title()
immune = input("Is your immune system too weak? ")
immune = immune.title()


if (age == "Yes") and (chronic == "Yes") and (immune == "Yes"):

    print("You are in risky group")

elif ((age == "Yes" and chronic == "Yes") or immune == "Yes") and ((age == "Yes" and immune == "Yes") or chronic == "Yes" ) and ((chronic == "Yes" and immune == "Yes") or age == "Yes"):
    
    print(("You are in quitely risky group"))

else:
    
    print("you are not in risky group")


# In[ ]:





# In[ ]:




