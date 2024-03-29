#!/usr/bin/env python
# coding: utf-8

# In[4]:


n=int(input())

factorial = 1

if n < 0:
   print("Sorry, factorial does not exist for negative numbers")
elif n == 0:
   print("The factorial of 0 is 1")
else:
   for i in range(1,n + 1):
       factorial = factorial*i
   print("The factorial of",n,"is",factorial)


# In[ ]:


x=5
y=4


print(x+y)
print(x-y)
print(x*y)
print(x/y)


# In[6]:


n=int(input())

factorial = 1

if n!=0:
   for i in range(1,n + 1):
       factorial = factorial*i
   print(factorial)


# In[7]:


x=input()

if (x == 'a' or x == 'e' or
        x == 'i' or x == 'o' or x == 'u'): 
    print("Vowel") 
else: 
    print("Consonant") 


# In[10]:


def reverse(string):
    string = string[::-1]
    return string
 
s = input()
 
print(end="")
print(reverse(s))


# In[14]:


rows = int(input())
ch = '*'

for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print('%c' %ch, end = '')
    print()
    
    


# In[25]:


n= int(input())
Oddtotal = 0

for number in range(1, n+1):
    if(number % 2 != 0):
        #print("{0}".format(number))
        Oddtotal = Oddtotal + number

print(Oddtotal)


# In[29]:


x = int(input())

if x%2==0:
    print('Even')
    if x>0:
        print('Positive')
    else:
        print('Negative')
else:
    print('Odd')


# In[ ]:


x=int(input())

if x%5==0 and x%3==0:
    print("Divisible")
elif x%3==0:
    print("Only by 3")
elif x%5==0:
    print("Only by 5")
else:
    print("Not Divisible")


# In[ ]:


t=float(input())
u=input()

if u == "C":
    print(float(((u-32)*5/9)))
else:
    print(float((5/9*(u-32))))



# In[ ]:


n= int(input())

# first two terms
n1, n2 = 0, 1
count = 0


if n>0:
   while count < n:
       print(n1, end=' ')
       nth = n1 + n2
       n1 = n2
       n2 = nth
       count += 1

