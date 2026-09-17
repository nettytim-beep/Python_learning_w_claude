class Dog:
    def __init__(self, name, breed, age):
        self.name = name
        self.breed = breed
        self.age = age

    def bark(self):
        return f"{self.name} says Woof!"

    def birthday(self):
        self.age += 1
        return f"{self.name} is now {self.age}"

rex = Dog("Rex", "Labrador", 3)
print(rex.birthday())   # Rex is now 4
print(rex.age)           # 4
print(rex)
