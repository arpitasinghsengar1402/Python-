'''
local and global variables
Before we dive into the differences between local and global variables, let's first recall what a variable is in Python.

A variable is a named location in memory that stores a value. In Python, we can assign values to variables using the assignment operator =. For example:
'''
x = 10 # global variable

def my_function():
  global x
  x=4
  y = 5 # local variable
  print(y)

my_function()
print(x)
#print(y) # this will cause an error because y is a local variable and is not accessible outside of the function