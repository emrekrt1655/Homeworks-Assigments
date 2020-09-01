#!/usr/bin/env python
# coding: utf-8

# ### Calculate the body mass index according to the height and weight values received from the user and print the following text on the screen according to the following rules.
# 
# 
# If the BMI is below 18.5 -------> Weak
# 
# If the BMI is between 18.5 and 25 ------> Normal
# 
# If the BMI is between 25 and 30 --------> Overweight
# 
# If the BMI is over 30 -------------> Obese

# In[7]:


height = float(input("Please enter your height as centimeter: "))
weight = float(input("Please enter yoru weight: "))

bmi = weight / ((height/100) ** 2)
bmi = round(bmi, 2)

if bmi < 18.5 :
    print(bmi, " : ", "Weak")
elif  18.5 <= bmi < 25 :
    print(bmi, " : ", "Normal")
elif 25 <= bmi < 30 :
    print(bmi, " : ", "Overweight")
else:
    print(bmi, " : ", "Obese")


# In[ ]:




