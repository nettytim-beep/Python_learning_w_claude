fruits = ["apple", "banana", "cherry"]
fruits.append("date")
fruits.remove("banana")

for i, fruit in enumerate(fruits):
   print(f"{i}:  {fruit}")
   
print(fruits[::-1])


