print("Sumit Tiwari")
print("Enrollment:  2301123044")

t1=(2,3,4)
print(t1)
print(type(t1))


# In[ ]:


#singletuple
t2=("20")
print(t2)
print(type(t2))


# In[ ]:


t3=(20,"igntu",3939)
print(t3)

print(t3[2])
print(t3[-2])


# In[ ]:


t=()
print(t)
print(type(t))


# In[1]:


t=(2,)
print(t)
print(type(t))


# In[ ]:


t4=((3,5,5),(3,2,5))
print(t4)
print(type(t4))


# In[ ]:


t5=tuple(((2,3),(8,6)))
print(t5)
print(type(t5))


# In[ ]:


t6=tuple("igntu",)
print(t6)
print(type(t6))


# In[ ]:


t7=tuple(("45",4,"igntu",2.5))
print(t7)
print(type(t7))


# In[ ]:


t8=tuple(range(6))
print((t8))


# In[3]:


t9= tuple(((2,)*7))
print(t9)
t11=tuple(range(6,9,3))
print((t11))


# In[ ]:


t12=tuple([3,4,2,4])
print(t12)
t13=tuple({12,2,3,23,2,4,2,})
print(t13)
print(type(t13))
x={"name":"juhi","age":20}
print(x)
print(type(x))
#dic to tuple
a1=tuple(x)
print(a1)
print(type(a1))
a3=tuple(x.values())
print(a3)
print(type(a3))
a4=tuple(x.items())
print(a4)
print(type(a4))
t15=12,13,131,44
print(t15)
print(type(t15))
#packing
#unpacking
a,b,c,d =t15
print(type(a))
t15=(2,13,131,44)
a,b,c,d =t15
print(type(a))


# In[4]:


t15=(2,13,131,44)
*a,b=t15
print(type(a))
print(t15)
print(a)
t15=(2,13,131,44)
a,*b=t15
print(type(b))
print(t15)

