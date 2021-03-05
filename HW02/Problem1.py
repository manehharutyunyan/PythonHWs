#!/usr/bin/env python
# coding: utf-8

# In[5]:


def my_max(*args):
    if len(args)==0:
        return "no numbers given"
    result = args[0]
    for num in args:
        if num > result:
            result = num
    return result

my_max(1, 2, -6, 7)

