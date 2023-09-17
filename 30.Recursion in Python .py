# Recursion is the process of defining something in terms of itself.
# In Python, we know that a function can call other functions.
# It is even possible for the function to call itself.
# These types of construct are termed as recursive functions.


def factorial(n):
    if(n==0 or n==1):
        return 1
    else:
        return n*factorial(n-1)
n=int(input("ENTER THE NUMBER FOR FACTORIAL"))
print(n)
print("FACTORIAL : " , factorial(n))




# fabinoacci series
n=int(input("ENTER THE NUMBER : "))
print(n)
def fabonacci(n):
    if(n==0 or n==1):
        return 1
    else:
        return fabonacci(n-1) + fabonacci(n-2)
for i in range(n):
    print(fabonacci(i))


 