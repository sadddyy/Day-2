# -*- coding: utf-8 -*-
"""Conditional_Statements.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1WPZ0psmSyK2-5Ww11DCYfERjCXkhx6bG
"""

time_remaining = 50

if time_remaining > 50:
  print("there is a lot of time")
else:
  print("no more time left")

mark = 80

if mark > 90:
  print("A Grade")
elif mark > 70:
  print("B Grade")
elif mark > 50:
  print("C Grade")
else:
  print("D Grade")

"""# conditional operators

1- ==

2- !=

3- <

4- <=

5- >

6- >=

7- and

8- or



"""

# conditional operator.

name = 5 #assignment operator.
name == 5 #equality checking.

if name == 5:
  print("5")

name != 8

name > 8

name < 8

#logical operator

#and  #or

#AND
True and True

True and False

False and True

False and False

#OR
True or True

True or False

False or True

False or False

a = 5
b = 10
c = 20

if a>3 and b==10 and c!=30 :
  #true and true and true
  #true
  print("passed")
else :
  print("failed")

# recieve input from user and make decision.

mark = int(input("Please enter a mark between 0 to 100 :-"))

if mark > 90:
  print("A Grade")
elif mark > 70:
  print("B Grade")
elif mark > 50:
  print("C Grade")
else:
  print("D Grade")

"""#String Formatting

"""

#1st type of String formatting

name = "python"
f"my name is {name}"

#2nd type of String formatting

name = "python"
"my name is {}".format(name)

#2nd type of String formatting

name = "python"
"my name is %s" %name

name = "python"
f"my name is {name:<10}!"

name = "python"
f"my name is {name:>10}!"

name = "python"
f"my name is {name:^10}!"

name = "python"
f"my name is {name:*^10}!"