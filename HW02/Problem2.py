#!/usr/bin/env python
# coding: utf-8

# In[2]:


def addTag(func):
    def wrapper(*args, **kwargs):
        print('<u> '+func(*args, **kwargs)+' </u>')
    return wrapper

def addString(func):
    def wrapper(*args, **kwargs):
        return(func(*args, **kwargs) + ', it’s me!')
    return wrapper

@addTag
@addString
def hi():
  return "HI"

hi()

