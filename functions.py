# basic syntax

print("Basic Syntax")
def greet(name):
   return f"Hello, {name}!"

print(greet("Tim"))
print()

print("Default parameter values")
def greet(name, greeting="Hello"):
   return f"{greeting}, {name}!"

print('Using default greeting="Hello"')
print(greet("Tim"))			# Hello, Tim!
print('pass greeting="Hay"')
print(greet("Tim", "Hey"))		# Hay, Tim!
print()

print("Call by name or order")
def describe(name, age, city):
   print(f"{name} is {age} and lives in {city}")

describe(age=40, city="Suwanee", name="Tim")	# by NAME
describe("Jeff", 50, "L'ville")			# by ORDER
print()

print("Multiple return values")

def min_max(numbers):
   return min(numbers), max(numbers)

nums = [4, 7, 1, 9, 2]
low, high = min_max(nums)
print(f"From {nums} min is {low} and max is {high}")
print()





