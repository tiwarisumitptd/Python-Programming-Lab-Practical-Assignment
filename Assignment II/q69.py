#!/usr/bin/env python
# coding: utf-8

# In[1]:


a = "Sumit Tiwari"
print("Sumit Tiwari")
print("Enrollment:  2301123044")

evenc = []
oddc= [] 

for i in range(len(a)):
    if i % 2 == 0: 
        evenc.append(a[i])
    else:
        oddc.append(a[i])

print(format(oddc))  
print(format(evenc))

