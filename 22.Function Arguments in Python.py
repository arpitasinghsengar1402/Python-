#Function Arguments and return statement
# There are four types of arguments that we can provide in a function:

# Default Arguments
# Keyword Arguments
# Variable length Arguments
# Required Arguments


def average(a=9, b=1):
    print(" the average is " , (a+b)/2)
average(4,6)
average(b=9)
average(4)


# keyword argument
# We can provide arguments with key = value, this way the interpreter recognizes the arguments by the parameter name. Hence, the the order in which the arguments are passed does not matter.

def name(fname, mname, lname):
    print("Hello , " , fname, mname , lname)
name("peter " , "ego ", " quill")


# default argument 
# We can provide a default value while creating a function. This way the function assumes a default value even if a value is not provided in the function call for that argument.

def name(fname, mname = "Jhon", lname = "Whatson"):
    print("Hello,", fname, mname, lname)
name("Amy")


# variable- lenght arguments
#Sometimes we may need to pass more arguments than those defined in the actual function. This can be done using variable-length arguments.
#There are two ways to achieve this:
#Arbitrary Arguments:
#While creating a function, pass a * before the parameter name while defining the function. The function accesses the arguments by processing them in the form of tuple.

def name(*name):
    print("Hello,", name[0], name[1], name[2])

name("James", "Buchanan", "Barnes")


#Keyword Arbitrary Arguments:
#While creating a function, pass a * before the parameter name while defining the function. The function accesses the arguments by processing them in the form of dictionary.

def name(**name):
    print("Hello,", name["fname"], name["mname"], name["lname"])

name(mname = "Buchanan", lname = "Barnes", fname = "James")


#return Statement
#The return statement is used to return the value of the expression back to the calling function.

def name(fname, mname, lname):
    return "Hello, " + fname + " " + mname + " " + lname

print(name("James", "Buchanan", "Barnes"))