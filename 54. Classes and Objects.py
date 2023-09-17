'''
A class is a blueprint or a template for creating objects, 
providing initial values for state (member variables or attributes), and 
implementations of behavior (member functions or methods). 
The user-defined objects are created using the class keyword.
'''

class person:
    name="arpita"
    occupation="student"
    salary= 10
    def info(self):
        print(f"{self.name} is a {self.occupation}")

a=person()
a.info()



class Details:
    name = "Rohan"
    age = 20

obj1 = Details()
print(obj1.name)
print(obj1.age)


'''
The self parameter is a reference to the current instance of the class, 
and is used to access variables that belongs to the class.
'''
