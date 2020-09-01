#!/usr/bin/env python
# coding: utf-8

# ### Calculate the letter grade according to the grades of visa1, visa2, final grades entered by the user.
# 
#      Visa1 will affect 30% of the total grade.
# 
#      Visa2 will affect 30% of the total grade.
# 
#      The final will affect 40% of the total grade.
# 
# 
#      Total Grade> = 90 -----> AA
# 
#      Total Grade> = 85 -----> BA
# 
#      Total Grade> = 80 -----> BB
# 
#      Total Grade> = 75 -----> CB
# 
#      Total Grade> = 70 -----> CC
# 
#      Total Grade> = 65 -----> DC
# 
#      Total Grade> = 60 -----> DD
# 
#      Total Grade> = 55 -----> FD
# 
#      Total Grade <55 -----> FF

# In[3]:


visa_1 = (int(input("Please enter your first visa score: "))) * 30 / 100
visa_2 = (int(input("Please enter your second visa score: "))) * 30 / 100
final = (int(input("Please enter your final score: "))) * 40 / 100

total_grade = visa_1 + visa_2 + final

if total_grade >= 90 :
    print("You passed the class with AA. Your Grade is: ", total_grade)
elif 90 > total_grade >= 85 :
    print("You passed the class with BA. Your Grade is: ", total_grade)
elif 85 > total_grade >= 80 :
    print("You passed the class with BB. Your Grade is: ", total_grade)
elif 80 > total_grade >= 75 :
    print("You passed the class with CB. Your Grade is: ", total_grade)
elif 75 > total_grade >= 70 :
    print("You passed the class with CC. Your Grade is: ", total_grade)
elif 70 > total_grade >= 65 :
    print("You passed the class with DC. Your Grade is: ", total_grade)
elif 65 > total_grade >= 60 :
    print("You passed the class with DD. Your Grade is: ", total_grade)
elif 60 > total_grade >= 55 :
    print("You passed the class with FD. Your Grade is: ", total_grade)
else:
    print("You could'not pass the class. Your note is FF. Your Grade is: ", total_grade)


# In[ ]:




