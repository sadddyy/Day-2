# -*- coding: utf-8 -*-
"""Loops.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1svXhPNPxq0wVQ0Xn5bm21NW7OeuX9cMX
"""

a = [1,2,5,7]
a

for i in [1,2,5,2]:
  print(i)

# i = variable
# iterable (sequence)
# looping - iterate over an iterable

for number in range(10):
  print(number+1)

for name in ['sonu','monu','tonu']:
  print(name)

for name in ['sonu','monu','tonu']:
  print('The name is {}'.format(name))

for name in ['sonu','monu','tonu']:
  if name == 'sonu':
    print("my name is",name)

for name in ['sonu','monu','tonu']:
  if name == 'sonu':
    print("my name is",name)
  else:
    print("my naame is not",name)

# range(20) -> 0,1,2,3....19 (end)
# range(2,20) -> 2,3,4....19 (start)
# range(2,20,2) -> 2,4,6....18 (start,end,step)

for k in range(2,20,2):
  print(k)

for k in range(2,19,2):
  print(k)

for k in range(20,2,-2):   #descending order with negative
  print(k)

# print 10,9,8,7......0
for k in range(10,-1,-1):
  print(k)

a = [5,10,15,20]
for value in [5,10,15,20]:
  print(value, value + 10)

a = [5,10,15,20,'python']
#iterating over elements
for value in a:
  print(value)

a = [5, 10,20,8,30]
length = len(a)
#iterating over indices(index)
#print(length)

for i in range(length):
  print(i)

a = [5, 10,20,8,30]
length = len(a)
#iterating over indices(index)
#print(length)

for i in range(length):
  print(a[i])

a = [5, 10,20,8,30,'kite']
length = len(a)
#iterating over indices(index)
for i in range(length):
  print(a[i])

a = [5, 10,20,8,30,'kite']
#iterating over indices(index)
for i in range(len(a)):
  print(a[i])

"""While Loop : variable, condition, increament.

"""

a = [5, 10,20,8,30,'kite']

#initialize the variable
i = 0 #--(index)
# terminating condition
while i < len(a): #len(a) = 6
  print(a[i])
  # increament
  i = i + 1 #6

"""Nested Loop

"""

names = ['sonu','monu','tonu','ponu']
dishes = ['dosa','idli','wada']
for name in names:
  #one iteration of outer for-loop
  #all iteration of inner for-loop
  #name = monu
  for dish in dishes:
    # dish = dosa, idli, wada
    print(name,'eats',dish)