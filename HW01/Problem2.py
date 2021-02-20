#!/usr/bin/env python
# coding: utf-8

# In[2]:


import time
import calendar
import datetime


# In[9]:


bday = datetime.date(1998, 11, 22)
print(bday)
print('Date: ', bday)
print('Year: ', bday.year, type(bday.year))
print('Month: ', bday.month)
print('Day: ', bday.day)
#4?
print('Day of the week: ', bday.weekday())

myDay = datetime.date(2021, 11, 22)
tday = datetime.date.today()
till_bday = myDay - tday
print("Days until my next birthday: ", till_bday)


# In[11]:



cal = calendar.month(2017, 5)
print (cal)


# In[15]:


today = datetime.date.today()
one_day = datetime.timedelta(days = 1)
yesterday = today - one_day
print('Yesterday : ',yesterday)
print('Added 2 days to yesterday’s date :', yesterday + 2*one_day)
print('Substracted 3 days from yesterday :', yesterday - 3*one_day)

