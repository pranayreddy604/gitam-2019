#!/usr/bin/env python
# coding: utf-8

# In[2]:


def test():
    print("test() for function")
    return
test()


# In[22]:


class Demo:
    n=0
    m=0
    def test(self,n,m):
        self.n=n
        self.m=m
        print("test() for the class and method",n+m)
        return
obj=Demo()
obj.test(55,40)


# In[35]:


class demo1:
    def fact(self,n):
        fact=1
        while(n!=0):
            fact=fact*n
            n=n-1
            
        
        return fact
p1=demo1()
print(p1.fact(5))


# In[1]:


import numpy as np
np.arange(1,10)


# In[2]:


np.arange(1,20,5)


# In[5]:


print(np.arange(1,2048,564))
print(np.arange(1,20,5)


# In[8]:


a1=np.array([(1,2,3),(4,5,6)])
print("slicing column :",a1[:,1])


# In[9]:


a1=np.array([(1,2,3),(4,5,6)])
print("slicing column :",a1[:,2])


# In[10]:


a1=np.array([(1,2,3),(4,5,6)])
print("first row :",a1[0])


# In[11]:


a1=np.array([(1,2,3),(4,5,6)])
print("second row :",a1[1])


# In[16]:


a1=np.array([(1,2,3),(4,5,6)])
print(a1)


# In[18]:


a1=np.random.normal(5,1,10)
print(a1)
print("min value",np.min(a1))
print("max value",np.max(a1))
print("mean value",np.min(a1))
print("median value",np.median(a1))


# In[19]:


c1=np.array([1,2])
c2=np.array([4,5])
np.dot(c1,c2)


# In[22]:


c1=np.array([(1,2),(4,5)])
c2=np.array([(3,4),(3,2)])
np.dot(c1,c2)


# In[32]:


import pandas as pd
dict={"name":["anil","akhil","dinesh","harsha","ajay","kranth"],
    "email.Id":["anil@gmail.com","akhil@gmail.com","dinesh@gmail.com","harsha@gmail.com","ajay@gmail.com","kranth@gmail.com"],
                 "p.no":[686535498,25775418,71745,5419814,1472285,58255],
                 "address":["gfhscj","nfgths","ftgggfj","wnjhr","dgjtydt","bgffhhfgc"]}
b=pd.DataFrame(dict)
print(b)


# In[ ]:




