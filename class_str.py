class Dog1:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed


class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def __str__(self):
        return f"{self.name} ({self.breed})"

rex = Dog("Rex", "Labrador")
rex1 = Dog1("Rex1", "Beagle")
print(rex)   # Rex (Labrador)  -- instead of <__main__.Dog object at 0x...>
print(rex1)  # <__main__.Dog1 object at 0x....>
