#!/usr/bin/env python
# coding: utf-8

# In[3]:


color=input()

if color=='green':
    print("i will eat it")


# In[5]:


color=input()

if color=='green':
    print("i will eat it")
else :
    print('i will eat burger')


# In[11]:


color=input()

if color=='green':
    print("i will eat it")
elif color == 'brown':
    print("i will eat on monday")
else :
    print('i will eat burger')


# In[21]:


color=input()
day=input()

if color=='green':
    print('the color is',color)
    if day=="monday":
        print("i will eat it")
else :
    print("fuck off")


# In[30]:


color=input()
day=input()

if color=='green':
    print('the color is',color)
    if day=="monday":
        print("i will eat proten")
    elif day=="tuesday":
        print("i will eat carbs")
    else:
        print('fuck off')
elif color=='red':
    print('the color is', color)
    if day=='monday':
        print('i will eat chicken')
    elif day=='tuesday':
        print('i will eat vegetables')
    else:
        print('fuck off')
else :
    print("fuck off")
    


# In[35]:


#USE OF IN:-

color=input()

if color in ('green','red','white'):
    print("i will eat it")
else :
    print('i will eat burger')


# In[42]:


#Ternary operator
#value-if-true if condition else value-if-false.

x=10
y=20

var1= x if x<y else y
print(var1)



# In[51]:


x=20
y=20

var1= 'x is less than y' if x<y else'x is equal to y' if x == y else 'x is greater than y'
print(var1)


# In[64]:


# A shop will give a discount of 10% on the total cost if the cost of the quantity purchased is more than 1000. 
#a. Ask user for the number of units 
#b. Suppose, one unit will cost 100. 
#c. Judge and print total cost for the user in the integer format.


units=int(input())

total_cost=(units*100)

if total_cost>1000:
    print("discounted price",total_cost-(0.1*total_cost))
else:
    print("Final price is", total_cost, "no disount")


# In[ ]:


x=int(input())
y=int(input())

sum=x+y

if sum>=100:
    print('High Sum')
else:
    print('Low Sum')


# In[ ]:


#You are given marks of a student as an integer input. 
#You need to print according to the following rules: 1 for marks above 90, print excellent. 
    #2 for marks above 80 and less than equal to 90, print good. 
    #3 for marks above 70 and less than equal to 80, print fair. 
    #4 for marks above 60 and less than equal to 70, print meets expectations. 
    #5 for marks above 40 and less than equal to 60, print below par. 
    #6 print failed if none of the above conditions follow.

marks=int(input())

if marks>90:
    print('Excellent')
elif marks>80 and marks<=90:
    print('Good')
elif marks>70 and marks<=80:
    print('Fair')
elif marks>60 and marks<=70:
    print('Meet Expectations')
elif marks>40 and marks<=60:
    print('Below par')
else :
    print('Failed.')


# In[ ]:


n=int(input())

f=n*(n-1)*(n-2)*...*1
print(f)

