# TABLE of any number
# break
n=int(input("enter the number you want the table for"))
print(n)
for i in range(12):
    if(i==10):
        break
    print(n, " X", i+1 , "=" , n*(i+1))


# continue
for i in range(100):
    if(i==10):
        print("skip the iteration")
        continue
    print("5 X",i,"=",5*i)