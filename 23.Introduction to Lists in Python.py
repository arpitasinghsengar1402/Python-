#Python Lists

#Lists are ordered collection of data items.
#They store multiple items in a single variable.
#List items are separated by commas and enclosed within square brackets [].
#Lists are changeable meaning we can alter them after creation.


marks=[3,5,6,"abc",'x',True]
print(marks)
print(type(marks))
print(marks[0])
print(marks[1])
print(marks[2])
print(marks[3])
print(marks[4])
print(marks[5])
print(type(marks[0]))
print(type(marks[1]))
print(type(marks[2]))
print(type(marks[3]))
print(type(marks[4]))
print(type(marks[5]))
print(marks[-1])
print(marks[-2])
print(marks[-3])
print(marks[-4])
print(marks[-5])
print(marks[-6])
print(marks[1:-1])
print(marks[1:])
print(marks[:6])
print(marks[:])
print(marks[1:8:3])
if 7 in marks:
    print(True)
else:
    print(False)

if "abc" in marks:
    print(True)
else:
    print(False)

if "ab" in "abc":
    print(True)
else:
    print(False)


lst1 = [1,2,2,3,5,4,6]
lst2 = ["Red", "Green", "Blue"]
print(lst1)
print(lst2)


details = ["Abhijeet", 18, "FYBScIT", 9.8]
print(details)