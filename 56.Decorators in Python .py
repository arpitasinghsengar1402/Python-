'''
Python decorators are a powerful and versatile tool that allow you to modify the behavior of functions and methods. They are a way to extend the functionality of a function or method without modifying its source code.

A decorator is a function that takes another function as an argument and returns a new function that modifies the behavior of the original function. The new function is often referred to as a "decorated" function. The basic syntax for using a decorator is the following:
'''


def greet(fx):
    def mfx():
        print("good morning")
        fx()
        print("Thanks for using this function")
    return mfx
@greet
def hello():
    print("hello world")

def add(a,b):
    print(a+b)

hello()


'''
Conclusion
Decorators are a powerful and flexible feature in Python that can be used to add functionality to functions and methods without modifying their source code. 
They are a great tool for separating concerns, reducing code duplication, and making your code more readable and maintainable.

In conclusion, python decorators are a way to extend the functionality of functions and methods, by modifying its behavior without modifying the source code. 
They are used for a variety of purposes, such as logging, memoization, access control, and more. 
They are a powerful tool that can be used to make your code more readable, maintainable, and extendable.

'''
import logging

def log_function_call(func):
    def decorated(*args, **kwargs):
        logging.info(f"Calling {func.__name__} with args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        logging.info(f"{func.__name__} returned {result}")
        return result
    return decorated

@log_function_call
def my_function(a, b):
    return a + b