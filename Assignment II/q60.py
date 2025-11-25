print("Sumit Tiwari")
print("Enrollment:  2301123044")

t = (10, 20, 30, 40, 50)

total = 0

for num in t:
    total += num

print(total)


# In[1]:


t = (10, 20, "juhi",2.3,30, 40, 50)

total = 0

for num in t:
    if type(num)==int:
        total += num
print(total)

