#!/usr/bin/env python
# coding: utf-8

# In[ ]:


s1 = "Sumit"
s2 = "Tiwari"
print("Sumit Tiwari")
print("Enrollment:  2301123044")

s1_even = s1[0::2]
s1_odd  = s1[1::2]

s2_even = s2[0::2]
s2_odd  = s2[1::2]

new_s1 = s2_even + s2_odd
new_s2 = s1_even + s1_odd

print(new_s1)
print(new_s2)


