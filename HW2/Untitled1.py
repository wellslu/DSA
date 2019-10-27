#!/usr/bin/env python
# coding: utf-8

# In[20]:


def heapsort(x):
    a=len(x)
    y=[]
    for i in range(a):
        for j in range(len(x),-1,-1):
            try:
                if x[j]>x[2*j+1]:
                    x[j],x[2*j+1] = x[2*j+1],x[j]
                if x[j]>x[2*j+2]:
                    x[j],x[2*j+2] = x[2*j+2],x[j]
            except:
                continue
        y.append(x.pop(0))
    return y


# In[26]:


a=[8,3,9,3,6,3,1,4,5,2,7,3,52,33,3,3,3,104]


# In[27]:


heapsort(a)


# In[ ]:




