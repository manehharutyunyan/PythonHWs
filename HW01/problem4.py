#!/usr/bin/env python
# coding: utf-8

# In[28]:


market = {"dairy": ["yogurt","cheese"],
          "fruits": ["banana", "apple", "orange", "lemon", "apple", "banana","banana"]}
print(market)


# In[19]:


market["candies"] = ["mars", "kinder", "twix"]
print(market)


# In[20]:


market["fruits"] = sorted(market["fruits"], reverse = True)
print(market["fruits"])


# In[26]:


market["fruits"] = list(dict.fromkeys(market["fruits"]))
print(market["fruits"])


# In[24]:


print(market)

