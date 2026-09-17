name = "Tim"
age = 40
print(f"Hi {name}, you are {age} years old")

# expressions inside the {}
print(f"Next year you'll be {age + 1}")
print(f"In caps: {name.upper()}")
print(f"Is even: {age % 2 == 0}")

# Number formatting
price = 19.999
print(f"${price:.2f}")		# $20.00   	-> 2 decimal places
big = 1234567
print(f"{big:,}")		# 1,234,567	-> thousands separator
pct = 0.856
print(f"{pct:.1%}")		# 85.6%		-> as a percentage

# Padding/alignment
print(f"{name:10}|")		# "Tim       |"	-> left-padded to 10 chars
print(f"{age:>5}")		#     40"	-> right-aligned in 5 chars

# Debugging shortcut (Python 3.8+)
# add = after var to print both name and value
print(f"{age=}")	# prints:  age=40

price = 4.5
quantity = 3

total = price * quantity

print(f"{quantity} items at ${price:.2f} each = ${total:.2f}")


