# Tuples are immutable, hence if you want to add, remove or change tuple items, then first you must convert the tuple to a list. Then perform operation on that list and convert it back to tuple.

countries = ("Spain", "Italy", "India", "England", "Germany")
print(countries)
temp = list(countries)
temp.append("Russia")  
print(temp)     #add item 
temp.pop(3)                 #remove item
temp[2] = "Finland"   
print(temp)   
print(type(temp))      #change item
countries = tuple(temp)
print(countries)
print(type(countries))

#concatenation
countries = ("Pakistan", "Afghanistan", "Bangladesh", "ShriLanka")
countries2 = ("Vietnam", "India", "China")
southEastAsia = countries + countries2
print(southEastAsia)

# count
Tuple1 = (0, 1, 2, 3, 2, 3, 1, 3, 2)
res = Tuple1.count(3)
print('Count of 3 in Tuple1 is:', res)

#index
Tuple = (0, 1, 2, 3, 2, 3, 1, 3, 2)
res = Tuple.index(3)
print('First occurrence of 3 is', res)


