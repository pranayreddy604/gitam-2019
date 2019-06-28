#!/usr/bin/env python
# coding: utf-8

# In[1]:


s="pranay123"
r="PranayReddy"
print(s.isalpha())
print(r.isalpha())


# In[4]:


s="pranay123"
r="2345142357698"
print(s.isnumeric())
print(r.isnumeric())


# In[5]:


s="pranay123"
r="PranayReddy"
print(s.islower())
print(r.islower())


# In[7]:


s="pranay123"
r="PRANAYREDDY"
print(s.isupper())
print(r.isupper())


# In[8]:


s="PrAnAy"
print(s.lower())
print(s.upper())


# In[1]:


s="Pranay123"
r="Pranay Reddy"
print(s.istitle())
print(r.istitle())


# In[4]:


s="pranay     "
r="   "
print(s.isspace())
print(r.isspace())


# In[26]:


s="Pranay123"
print("*".join(s))


# In[46]:


s="P*r*a*n*a*y*1*2*3"
print("".join(s))


# In[49]:


st=s.split("*")
print(st)
"".join(st)


# In[51]:


s="pkr"
print(s.replace("kr"," ranay"))


# In[61]:


t1=("pkr","pranay","PranayReddy","6042001","970","139","3638","pranayKumarReddy")
print("t1[0]=",t1[0])
print("t1[1]=",t1[1])
print("t1[2]=",t1[2])
print("t1[3]=",t1[3])
print("t1[4]=",t1[4])
print("t1[::2]=",t1[::2])
print("t1[2::-1]=",t1[2::-1])
print("t1[::-2]=",t1[::-2])
print("t1[7:0:-1]=",t1[7:0:-1])


# In[70]:


t1=("pkr","pranay","PranayReddy","6042001","970","139","3638","pranayKumarReddy")
#del t1

print(t1)


# In[79]:


t2=(12,23,34,45,56,21)
t3=(34,54,98,12,23,21)
print(min(t2))
print(max(t2))
print(len(t2))
a=cmp(t1,t2)
print(a)


# In[87]:


list=[12,23,34,45,67,56,89,90]
print(list)
tuple=tuple(list)
print(tuple)


# In[98]:


contact={}
def addContact(name,phone):
    if name not in contacts:
        contact[name]=phone
        print("contact %s added" %name)
    else:
        print("contact %s already exists"%name)
    return
addContact("anil",95137521)
addContact("harsha",6353554)
addContact("anil",25417445855)


# In[102]:


def searchContact(name):
    if name in contact:
        print(name,":",contact[name])
    else:
        print("%s not found" %name)
    return
searchContact("anil")
searchContact("harsha")


# In[111]:


def importContacts(newcontacts):
    contact.update(newcontacts)
    print(len(newcontacts.keys()),"contacts added")
    return
newcontacts={'dinesh':354557581448,'ajay':587855656}
importContacts(newcontacts)


# In[112]:


print(contact)


# In[113]:


def deleteContact(name):
    if name in contact:
        del contact[name]
        print(name,": is deleted")
    else:
        print(name,":not exists")
    return
deleteContact('harsha')
deleteContact('naveen')


# In[117]:


def updateContact(name,phone):
    if name in contact:
        contacts[name]=phone
        print(name,":update completed")
    else:
        print(name,"not exists")
    return
updateContact("anil",58746656874)
updateContact("pkr",21454645)


# In[120]:


import random
def generateRandomNumbers(n,lb,ub):
    for i in range(0,n):
        print(random.randint(lb,ub),end=" ")
    return
generateRandomNumbers(10,12,120)


# In[122]:


import math 
  
a = 2.3
print ("The ceil of 2.3 is : ", end="") 
print (math.ceil(a))


# In[123]:


print ("The floor of 2.3 is : ", end="") 
print (math.floor(a))


# In[124]:


a = -10
  
b= 5
  

print ("The absolute value of -10 is : ", end="") 
print (math.fabs(a)) 


# In[125]:


print ("The factorial of 5 is : ", end="") 
print (math.factorial(b)) 


# In[126]:


import math 
  
a = -10
b = 5.5
c = 15
d = 5 
print ("The copysigned value of -10 and 5.5 is : ", end="") 
print (math.copysign(5.5, -10)) 
  


# In[127]:



print ("The gcd of 5 and 15 is : ", end="") 
print (math.gcd(5,15)) 


# In[128]:


import math

print(math.pow(2, 3))


# In[129]:


number = 1e-4
print('The given number (x) is :', number)
print('e^x (using exp() function) is :', math.exp(number)-1)
print('log(fabs(x), base) is :', math.log(math.fabs(number), 10))


# In[130]:


import math

angleInDegree = 90
angleInRadian = math.radians(angleInDegree)

print('The given angle is :', angleInRadian)
print('sin(x) is :', math.sin(angleInRadian))
print('cos(x) is :', math.cos(angleInRadian))
print('tan(x) is :', math.tan(angleInRadian))


# In[ ]:




