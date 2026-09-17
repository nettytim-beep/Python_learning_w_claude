
# Lists are built-in dynamic array with no type declaration needed
fruits = ["apple", "banana", "cherry"]    # list no declaration needed
oddnums = [1, 3, 5, 7, 9]

print(*fruits)    # the * unpacks the list so that it can be printed out
print(f"fruits list {*fruits,}")

print()
fruits.append('date')
print(f"fruits.append('date') added date to the end of the list {*fruits,}")

print(f"fruits[0] returns first element {fruits[0]}")
print(f"fruits[-1] returns last element {fruits[-1]}")
fruits.remove('banana')
print(f"fruits.remove('banana') = {*fruits,}")
print(f"len(fruits) = {len(fruits)}")

print()
print("looping over the list")
for fruit in fruits:
   print(fruit)

print()
print("Lets use enumerate in a for loop which returns the index, element in enumerate(fruits)")
for i, fruit in enumerate(fruits):
   print(i, fruit)

 
