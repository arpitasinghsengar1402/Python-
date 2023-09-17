n=int(input("Enter the number : "))
print(n)
if(n<0):
    print("LESS THAN O \n")
elif(n>0):
    print("GREATER THAN 0\n")
    if(n<=30):
        print("POOR")
    elif(n>30 & n<=50):
        print("BEST")
    elif(n>50 & n<=70):
        print("GOOD")
    else:
        print("EXCELLENT")
else:
    print("zero")
    