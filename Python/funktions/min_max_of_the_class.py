#!/usr/bin/env python
# coding: utf-8

# ### Write a Python code that finds the students who have maximum and minimum average at a given dictionary below.
# {'Student-1': {'Lesson-1': 57, 'Lesson-2': 46, 'Lesson-3': 58, 'Lesson-4': 81, 'Lesson-5': 85}, 'Student-2': {'Lesson-1': 85, 'Lesson-2': 56, 'Lesson-3': 51, 'Lesson-4': 69, 'Lesson-5': 67}, 'Student-3': {'Lesson-1': 68, 'Lesson-2': 76, 'Lesson-3': 87, 'Lesson-4': 57, 'Lesson-5': 56}, 'Student-4': {'Lesson-1': 78, 'Lesson-2': 93, 'Lesson-3': 88, 'Lesson-4': 38, 'Lesson-5': 54}, 'Student-5': {'Lesson-1': 50, 'Lesson-2': 46, 'Lesson-3': 78, 'Lesson-4': 81, 'Lesson-5': 75}}

# In[1]:


the_sco_class = {'Student-1': {'Lesson-1': 57, 'Lesson-2': 46, 'Lesson-3': 58, 'Lesson-4': 81, 'Lesson-5': 85}, 'Student-2': {'Lesson-1': 85, 'Lesson-2': 56, 'Lesson-3': 51, 'Lesson-4': 69, 'Lesson-5': 67}, 'Student-3': {'Lesson-1': 68, 'Lesson-2': 76, 'Lesson-3': 87, 'Lesson-4': 57, 'Lesson-5': 56}, 'Student-4': {'Lesson-1': 78, 'Lesson-2': 93, 'Lesson-3': 88, 'Lesson-4': 38, 'Lesson-5': 54}, 'Student-5': {'Lesson-1': 50, 'Lesson-2': 46, 'Lesson-3': 78, 'Lesson-4': 81, 'Lesson-5': 75}}
the_stu_list = ["Student 1", "Student 2", "Student 3", "Student 4", "Student 5" ]
the_score_list =[]

    


# In[2]:


avr_std_1 = (the_sco_class['Student-1'])
avr_std_2 = (the_sco_class['Student-2'])
avr_std_3 = (the_sco_class['Student-3'])
avr_std_4 = (the_sco_class['Student-4'])
avr_std_5 = (the_sco_class['Student-5'])

avr_std_1 = list(avr_std_1.values())
avr_std_2 = list(avr_std_2.values())
avr_std_3 = list(avr_std_3.values())
avr_std_4 = list(avr_std_4.values())
avr_std_5 = list(avr_std_5.values())


# In[3]:


def avr(a):
    summ = 0
    for i in a:
        summ += i / len(a)
    return the_score_list.append(summ)
        


# In[4]:


avr(avr_std_1)
avr(avr_std_2)
avr(avr_std_3)
avr(avr_std_4)
avr(avr_std_5)


# In[5]:


the_last_dict = dict(zip(the_stu_list, the_score_list))
the_last_dict = sorted(the_last_dict.items(), key=lambda x: x[1])

print("The minumum average of the class is below :  ")  
print((the_last_dict)[0])
print (" ")
print("The maximum average of the class is below :  ")  
print((the_last_dict)[-1])


# In[ ]:




