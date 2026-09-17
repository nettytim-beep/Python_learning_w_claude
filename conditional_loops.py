# if/elf/else
print("if/elif/else")
age = 20

if age < 13:
   print("Child")
elif age < 20:
   print("Teenager")
else:
   print("Adult")
print()


"""
No parentheses required around the condition, no braces — 
the colon : starts the block, and everything indented underneath 
belongs to it. Mixing tabs and spaces, or indenting inconsistently, 
will actually break your code (IndentationError), so most editors 
are set to auto-insert 4 spaces per level.
"""

# Comparison & logical operators
print("Comparison & logical operators")

x = 5
print(f" ==   {x == 5}")	# True  	equals like Java
print(f" !=   {x != 5}")	# False  	not equal
print(f" and  {x and x < 10}")	# True		'and' instead of &&
print(f" or   {x or x > 100}")	# 5		'or' instead of ||
print(f" not  {not (x == 5)}")	# False 	'not' instead of !  # noqa: SIM201 -- demonstrating `not`, not `!=`
print()

#------------------
# while loop
#------------------
print("while loop")
count = 0

while count < 5:
   print(count)
   count += 1		# no ++ operator in Python - use += 1
print()

#-------------------
# for loop
#-------------------
print("for loop")
for i in range(5):		# like Java's for(int i=0; i<5; i++)
   print(i)			# prints 0 1 2 3 4 
print()

"""
range(5) generates 0–4. You can also do range(2, 10, 2) for start/stop/step.
"""
print("loop across an array")
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:			# like Java's enhanced for-each loop
   print(fruit)
print()


