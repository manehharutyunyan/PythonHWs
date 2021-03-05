#!/usr/bin/env python
# coding: utf-8

# In[1]:


def my_range(n):
    i=0
    while i <= n+1:
        if i == n+1:
            print('there are no values left')
            return
        yield (i)
        i+=1
        
my_nums = my_range(3)


# In[6]:


print(next(my_nums))

