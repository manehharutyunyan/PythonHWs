#!/usr/bin/env python
# coding: utf-8

# In[3]:


givenText = input("Give the text:")
firstWord = input("Give the first word:")
secondWord = input("Give the second word:")
givenText.replace(firstWord, secondWord)

print("The given text: ", givenText)
print("First word:: ", firstWord)
print("Second word: ", secondWord)


# In[ ]:


givenText.split(' ', 1)[0]

