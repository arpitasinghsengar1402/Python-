def calculategmean(a,b):
    mean=(a*b)/(a+b)
    print(mean)
def isgreater(a,b):
    if(a>b):
        print("first no is greater")
    else:
        print("second no is less or equal")

a=int(input("enter first value"))
print(a)
b=int(input("enter second value"))
print(b)

isgreater(a,b)
calculategmean(a,b)

c=int(input("enter first value"))
print(c)
d=int(input("enter second value"))
print(d)

isgreater(c,d)
calculategmean(c,d)