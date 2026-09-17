# try/expect error handling

print("Error handling to handle input of a number")

try:
   age = int(input("Enter your age: "))
   print(f"Next year you'll be {age + 1}")
except ValueError:
   print("That's not a valid number.")

print()
print("Catch multiple specific error types.  Note: if multiole will catch the first error not all")
try:
    numbers = [1, 2, 3]
    print(numbers[5])          # IndexError
    result = 10 / 0            # ZeroDivisionError
except IndexError:
    print("That index doesn't exist.")
except ZeroDivisionError:
    print("Can't divide by zero.")

print()
print("Catch any exception and use  as e  to capture the exception to printout")
def risky_thing():
    return 1 / 0            # deliberately raises to demonstrate a catch-all


try:
    risky_thing()
except Exception as e:      # noqa: BLE001 -- deliberately broad, that's the point of the demo
    print(f"Something went wrong: {e}")

print()
print("Using else and finally in try except block")
try:
    age = int(input("Enter your age: "))
except ValueError:
    print("Invalid input.")
else:
    print(f"Valid age: {age}")   # only runs if NO exception occurred
finally:
    print("Done processing.")     # ALWAYS runs, error or not

