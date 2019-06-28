#!/usr/bin/env python
# coding: utf-8

# In[8]:


def printNaturalNumbers(n):
    count=1;
    while(count<=n):
        print(count,end='  ')
        count=count+1
    print()
    return


# In[ ]:





# In[25]:


def findfact(n):
    fact=1
    while(n!=0):
        fact=fact*n
        n=n-1                         
    return fact;

print(findfact(10));                                      


# In[30]:


def countOfPalindrome(n1,n2):
    cnt=0
    
    while(n1!=n2):
        sum=0
        buffer=n1
        while(n1!=0):
            r=n1%10
            sum=(sum*10)+r
            n1=n1//10
        if(buffer==sum):
            cnt=cnt+1
        n1=buffer
        n1=n1+1
    return cnt;
print(countOfPalindrome(10,30));
print(countOfPalindrome(1,10000000));
    


# In[10]:


def printEven(n):
    count=0
    sum=0
    while(count!=n):
        if(count%2==0):
            sum=sum+count
        count=count+1
    return sum;

printEven(20)
    


# In[17]:


def factorList(n):
    i=1
    while(i!=n):
        if(n%i==0):
            print(i,end="  ")
        i=i+1
    return i
factorList(12)


# In[28]:


list1=['p','r','a','n','a','y']
print(list1)
print(list1[0])


# In[38]:


list1=[1,2,3,4,5,6,7,8]
for x in list:
    print(x,end="  ")
    
print(list1[0])
print(list1[0:3])


# In[75]:


list1=[1,2,2,3,4,5,6,7,8,9,9]
del list1[1]
print(list1)
list1[1]=2
print(len(list1))
print(list1[2:-2])
print(list1[7:2:-1])
print(list1[::-2])
print(list1[::3])


# In[87]:


list1=[1,1,1,1,1]
print(list1.count(1))
list1.append(5)
print(list1)


# In[16]:


list=["pranay","shiva","ashish",1]
print(list)
list.remove(1)
print(list)
list.insert(2,1)
print(list)
print(list.index(1))
print(list)
list.reverse() 
print(list)
list.pop(3)
print(list)


# In[ ]:




