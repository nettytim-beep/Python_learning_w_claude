# error_handling.py example

def safe_divide(a, b):
   try:
      return a / b
   except ZeroDivisionError:
      return "Cannot divide by zero"

print(safe_divide(10, 2))
print(safe_divide(10, 0))

scores = {"Alice": 85, "Bob": 72}

try:
   print(scores["Charlie"])
except KeyError:
   print("That name isn't in the scores dict.")


