#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def binarySearch(a,index1,index2,item):
    while index1<=index2:
        mindex=index1+(index2-index1)//2
        if(a[mindex]==item):
            return mindex
        if(a[mindex]>item):
            index2=mindex-1
        else:
            index1=mindex+1
    return -1
list1=[1,4,9,15,25,45,57,88,87,98]
res=binarySearch(list1,0,10,87)
if(res!=-1):
    print("element found")
else:
    print("element  not found")


# In[ ]:


def bubbleSort(a):
    for i in range (len(a)-1):
        for j in range(len(a)-1):
            if(a[j]>a[j+1]):
                a[j],a[j+1]=a[j+1],a[j]
    for i in range(len(a)):
        print(a[i],end="  ")

list=[19,2,4,1,70]
bubbleSort(list)


# In[ ]:


str="application"
print(str)
str1='application'
print(str1)
str2="""Application Test
      working
      completed
      list
      strings
      python """
print(str2)


# In[ ]:


str="Application"
print(str)
print("str[0]=",str[0])
print("str[6]=",str[6])
print("str[-1]=",str[-1])
print("str[0:6]=",str[0:6])
print("str[::2]=",str[::2])
print("str[2:]=",str[2:])
print("str[9:2:-1]=",str[10:0:-2])
print("str[-2::]=",str[2:])


# In[ ]:



  
def isPalindrome(s): 
     
    rev = reverse(s) 
  
    if (s == rev): 
        return True
    return False
  
  
s=input("Enter The Character")

ans = isPalindrome(s) 
  
    if ans == True: 
        print("Yes") 
    else: 
        print("No") 


# In[ ]:



#count of digits of a number
n=int(input("Enter The Number"))
cnt=0
while n!=0:
    cnt=cnt+1
    n=n//10
print(cnt)


# In[ ]:





# In[ ]:



def countdigit(n):
    return len(n)

countdigit("123456789")


# In[ ]:


def countuppercase(str):
    count=0
    lst=list(str)
    for x in range(len(lst)):
        if ord(lst[x])>= 65 and ord(lst[x]) <= 90:
            count=count+1
    return count

print(countuppercase("APPlication"))


# In[43]:


def printdigits(str):
    lst=list(str)
    for x in range(len(lst)):
        if ord(lst[x])>= 48 and ord(lst[x]) <= 57:
            print(lst[x],end=" ")
            
    return
print(printdigits("App18"))


# In[4]:


str=input()
lst=ord(str)
print(lst)


# In[3]:


def sumOfDigits(str):
    sum=0
    lst=list(str)
    for x in range(len(lst)):
        if ord(lst[x])>=48 and ord(lst[x])<=57:
            sum=sum+ord(lst[x])-48
    return sum
sumOfDigits("pranay123")


# In[24]:


def sumOfDigits1(str):
    sum=0
    lst=list(str)
    for x in range(len(lst)):
      
            if ord(lst[x])>=48 and ord(lst[x])<=57:
               if ((ord(lst[x])-48)%2==0):
                     sum=sum+ord(lst[x])-48
            
    return sum
print(sumOfDigits1("pranay6042001"))


# In[ ]:




