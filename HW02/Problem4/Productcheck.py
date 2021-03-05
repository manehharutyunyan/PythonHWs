#!/usr/bin/env python
# coding: utf-8

# In[7]:


products = {
    'candy': 10,
    'juice': 5,
    'pen': 50
}

def check(product,num):
    if product in products.keys() and products[product] >= num:
        return True
    return False

