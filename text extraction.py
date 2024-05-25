#!/usr/bin/env python
# coding: utf-8

# In[3]:


import easyocr
import cv2
import numpy as np


# In[71]:


montant = 45


# In[69]:


image_path = 'img1.jpg'


# In[70]:


reader = easyocr.Reader(['fr'], gpu=False)
result = reader.readtext(image_path)
result


# In[24]:


text = ''


# In[28]:


for i in result:
    text=text+str(i[1])


# In[26]:


print(text)


# In[ ]:


test=False


# In[72]:


if (' '+str(montant)+'.000 TND') in text or (' '+str(montant)+' ,000 ')in text:
    test=True
else:
    test=False


# In[73]:


print(test)


# In[ ]:




