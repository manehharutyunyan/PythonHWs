#!/usr/bin/env python
# coding: utf-8

# In[32]:


a = [1, 4, 5, 7, 8, -2, 0, -1]
print(a[3])
print(a[5])


# In[33]:


a_sorted = sorted(a, reverse=True)
print(a)
print(a_sorted)


# In[29]:


sub1 = a[1:4]
print(sub1)
sub2 = a[2:7]
print(sub2)


# In[35]:


print(a_sorted)
del a_sorted[2]
del a_sorted[3]
print(a_sorted)


# In[39]:


b = ["grapes", "Potatoes", "tomatoes","Orange", "Lemon", "Broccoli", "Carrot", "Sausages"]
print(b)


# In[41]:


b_sorted = sorted(b)
print(b_sorted)


# In[48]:


c = b[1:4] + b[4:7]
print(c)

