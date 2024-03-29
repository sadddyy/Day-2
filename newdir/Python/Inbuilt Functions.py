#!/usr/bin/env python
# coding: utf-8

# Lambda Function
# 

# In[1]:


def prod(x):
    return x*2


# In[2]:


prod(5)


# In[3]:


# with lambda

prod=lambda x: x*2


# In[4]:


prod(5)


# In[5]:


prod=lambda x,y: x*y


# In[6]:


prod(2,5)


# In[8]:


def calculator(x,y,op):
    if op=="+":
        return x+y
    elif op=="-":
        return x-y
    else :
        return x*y


# In[10]:


calculator(2,3,"+")


# In[11]:


calculator(2,3,"-")


# In[13]:


# with lambda

calculator = lambda x,y,op: x+y if op=="+" else x-y if op=="-" else x*y


# In[14]:


calculator(2,3,"+")


# In[15]:


calculator(2,3,"-")


# Max function

# In[20]:


n=input().split()
lst2=[]

for i in n:
    lst2.append(int(i))


# In[21]:


lst2


# In[24]:


# with map function.

n=list(map(lambda x: int(x),lst2))


# In[25]:


lst2


# In[34]:


n=list(map(lambda x: int(x),lst2))


# In[35]:


lst2


# In[36]:


n=set(map(lambda x: int(x),lst2))


# In[37]:


lst2


# Filter Function.

# In[1]:


lst=[1,2,3,4,5,6,7,8,9]


# In[2]:


list(filter(lambda x:x>=5,lst))


# In[4]:


#without filter function.

lst2=[]
for i in lst:
    if i>=5:
        lst2.append(i)
    


# In[5]:


lst2


# In[6]:


lst


# In[14]:


# without lambda function

def gret_than_5(x):
    return x>=5


# In[15]:


gret_than_5(20)


# In[16]:


list(filter(gret_than_5,lst))


# Reduce Function.

# In[20]:


lst=[10,20,30,40,50]

sum_=0
for i in lst:
    sum_+=i


# In[21]:


sum_


# In[22]:


# using reduce function

import functools

functools.reduce(lambda x,y: x+y,lst)


# In[23]:


# map is used to transform the list.
# filter is used to filter the list.
# reduce is used to combine the list.
# pop is used to delete particular element of the list using index.
# remove is used to delete particular element of the list.


# In[24]:


# remove function.

lst=[1,2,3,4,5]

lst.remove(4)


# In[25]:


lst


# In[30]:


# pop function

lst=[6,7,8,9,10]
lst.pop(3)


# In[31]:


lst


# In[33]:


# 6
# 2 5 8 10 3 6
# print only even output in ascending order.

n=int(input())
lst=list(map(int,input().split()))

lst2=list(filter(lambda n:n%2==0,lst))

lst2.sort()

print(*lst2)


# In[35]:


# input : 
# 5
# 1, 2, 3, 4, 5
# output
# 120, 60, 40, 30, 24



n=int(input())
lst=list(map(int, input().split(", ")))

prod=[]

for i in range(len(lst)):
    product=1
    
    for j in range(len(lst)):
        if i!=j:
            product*=lst[j]
            
            
    prod.append(product)
    
for i in range(len(prod)):
    if i!=len(prod)-1:
        print(prod[i],end=", ")
    else:
        print(prod[i])


# In[37]:


n=int(input())
lst=list(map(int, input().split(", ")))

prod=''

for i in range(len(lst)):
    product=1
    
    for j in range(len(lst)):
        if i!=j:
            product*=lst[j]
            
            
    prod+=str(product)+", "
    
print(prod[:-2])


# In[45]:


#print common numbers.

n=int(input())
lst=list(map(int, input().split()))
n2=int(input())
lst2=list(map(int, input().split()))

lst3=[]

for i in lst:
    if i in lst2:
        lst3.append(i)
  
        
print(*lst3) if lst3 else [-1]



# In[46]:


def common(lst,lst2):
    newlst=[]
    for i in lst:
        if i in lst2:
            newlst.append(i)
    return newlst if newlst else [-1]


n=int(input())
lst=list(map(int, input().split()))
n2=int(input())
lst2=list(map(int, input().split()))

result=common(lst,lst2)
print(*result)


# In[ ]:


n=int(input())
lst=list(map(int, input().split()))
t=int(input())
n2=int(input())
lst2=list(map(int, input().split()))


lst3=list(filter(lambda x: x==t,lst ))

lst4=lst3.append(lst2)


# In[ ]:


# 5
# 1 2 3 2 4
# 2
# 3
# 5 6 7


# 1 5 6 7 3 5 6 7 4




n=int(input())
l1=list(map(int, input().split()))

target=int(input())

m=int(input())
l2=list(map(int, input().split()))

newlist=[]

for i in l1:
    if i==target:
        newlist.extend(l2)
    else :
        newlist.append(i)
        
print(*newlist)


# In[ ]:





# In[ ]:





# In[ ]:




