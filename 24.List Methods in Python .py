l=[11,22,23,2,4,5,2,5,2,2]
print(l)
l.append(6)  #appending means adding at the last
print(l)
l.sort()   # sorting
print(l)
l.sort(reverse=True) 
print(l)
l.reverse() 
print(l)
print(l.index(5))           #index gives the postion of the element present
print(l)
print(l.count(2))
print(l)
m=l
m[0] = 0 
print(l)
l.insert(1,899)
print(l)
m=[900,1000,1100]
l.extend(m)
print(l)
k=l+m             #concatenation
print(k)