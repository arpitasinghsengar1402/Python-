'''
A constructor is a special method in a class used to create and initialize an object of a class.
 There are different types of constructors. 
 Constructor is invoked automatically when an object of a class is created.

A constructor is a unique function that gets called automatically when an object is created of a class. 
The main purpose of a constructor is to initialize or assign values to the data members of that class.
 It cannot return any value other than None.
 '''

'''
Types of Constructors in Python
1.Parameterized Constructor
2.Default Constructor

Parameterized Constructor in Python:

When the constructor accepts arguments along with self, it is known as parameterized constructor.

These arguments can be used inside the class to assign the values to the data members.
'''

class Details:
    def __init__(self, animal, group):
        self.animal = animal
        self.group = group

obj1 = Details("Crab", "Crustaceans")

obj2= Details("cat","raptile")
print(obj1.animal, "belongs to the", obj1.group, "group.")
print(obj2.animal, "belongs to the", obj2.group, "group.")

obj2.animal="crocodile"
print(obj2.animal, "belongs to the", obj2.group, "group.")

obj3= Details(" ", " ")
obj3.animal=input("enter animal: ")
obj3.group=input("enter group: ")
print(obj3.animal, "belongs to the", obj3.group, "group.")

'''
Default Constructor in Python
When the constructor doesn't accept any arguments from the object and
 has only one argument, self, in the constructor, it is known as a Default constructor.
'''

class Details:
  def __init__(self):
    print("animal Crab belongs to Crustaceans group")
obj1=Details()
