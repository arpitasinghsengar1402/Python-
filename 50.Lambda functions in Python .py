def avg(x):
    return x*2

print(avg(5))

# In Python, a lambda function is a small anonymous function without a name. It is defined using the lambda keyword and has the following syntax:
# Lambda functions are often used in situations where a small function is required for a short period of time. 
#They are commonly used as arguments to higher-order functions, such as map, filter, and reduce.


avg=lambda x:x*2
cube=lambda x:x*x*x
print(cube(5))
print(avg(5))

"""
The above lambda function has the same functionality as the double function defined earlier. However, the lambda function is anonymous, as it does not have a name.

Lambda functions can have multiple arguments, just like regular functions. Here is an example of a lambda function with multiple arguments:
"""

max=lambda x,y:x*y/2
print(max(4,8))


# Lambda function to calculate the product of two numbers,
# with additional print statement
lambda x, y: print(f'{x} * {y} = {x * y}')
