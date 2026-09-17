# Simple class
# the __init__ is the constructor.  The first parameter of all class methods is self.  The self name is convention
# and can be anything but still refers to the class instance
# Notice that instance variables are not declared.  In the __init__ method the self.name and self.bread create and 
# initialize the instance variables.
# Notice when creating a instance of Dog that the __init__ is implectly called.
# Notice that returning the instance variable the instance itself simply gets the instance variable with instance.instancevar

class Dog:
    def __init__(self, name, breed):   # constructor (like Java's Dog(String name, ...)) Note: the 1st param is self
        self.name = name                # instance variable (like Java's this.name) Note: instance var created
        self.breed = breed

    def bark(self):                     # instance method
        return f"{self.name} says Woof!"

my_dog = Dog("Rex", "Labrador")
print(my_dog.name)        # Rex              return the name instance variable
print(my_dog.bark())      # Rex says Woof!   call the bark() method
