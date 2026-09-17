import math
import random

numbers = [random.randint(1, 100) for _ in range(5)]
print(numbers)

print(f"Square root of max: {math.sqrt(max(numbers)):.2f}")
print(f"Average: {sum(numbers) / len(numbers):.2f}")

import helpers

print(helpers.greet("Tim"))

import datetime

today = datetime.datetime.now().astimezone().date()         # today's date
print(f"today is {today}")

import os

cd = os.getcwd()                    # current working directory
print(f"current directory {cd}")
files = os.listdir(".")                # list files in current directory
print(f"files in current directory: {files}")
