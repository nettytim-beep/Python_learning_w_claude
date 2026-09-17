# tuples and sets

print("tuples in Python are immutable")
print("tuples can contain an unlimited number of elements")
print("tuples are constructed like list but instead of [] which defines a list it uses () with a single element tuple requiring a trailing , to make it a tuple")

point = (10, 20)
person = ("Tim", 40, "Suwanee")

print(f"tuples can mix types, just like lists {person}")
print(f"index first tuple element point[0] = {point[0]}")
print(f"index last tuple element point[-1] = {point[-1]}")

print()
x, y = point
print(f"unpack a tuple x, y = point  x: {x}, y: {y}")
name, age, city = person
print(f"unpack a tuple name, age, city = person  name: {name}, age: {age}, city: {city}")

print()
print("functions return tuples")
def min_max(numbers):
   return min(numbers), max(numbers)   # this IS a tuple

result = min_max([4, 7, 1, 9])
print(type(result))  # <class, 'tuple'>

print("------ Sets ------")

colors = {"red", "green", "blue"}
print("set like list or tuple but uses { } to define the set")
print(f"set colors: {colors}")
colors.add("yellow")
print(f"colors.add('yellow'): {colors}")
colors.add("red")        # no effect — already there, no duplicates allowed
print(f"colors.add('red') no effedt, no duplicates allowed - {colors}")
colors.remove("green")
print(f"colors.remove('green') - {colors}")


print(f"'blue' in colors - {'blue' in colors}")   # True — fast membership check
len(colors)                # count of unique items
print(f"len(colors) - {len(colors)}")

nums = [1, 2 ,2 ,3 ,3 ,3 ,4]
print(f"list of nums {nums}")
unique = set(nums)
print(f"set built from nums  set(nums) : {unique} de-duplicate list")

print()
print("Set operations")
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
print(f"set a : {a}  and  set b: {b}")
print(f"set union a | b {a | b}")
print(f"set intersection  a & b {a & b}")
print(f"set difference a - b {a - b}")
print(f"set symmetric difference a ^ b {a ^ b}")

print()
print("set comprehension")
# pattern: {expression for item in iterable if condition exists}
evens = {n for n in range(1, 11) if n % 2 == 0}
# {2, 4, 6, 8, 10}
print(f"{{n for n in range(1, 11) if n % == 0}} = {evens}")





