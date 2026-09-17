# File I/O

import os  # import the os module so the file can be removed.

# Lets open a file and write some data to it

# the standard way to open a file is the  with as command structure
print("Open and write to notes.txt")
with open("notes.txt", "w") as f: # open a file for write create and overwrite if exists
   f.write("Hello, Python\n")  # have to add /n for newline
   f.write("Second line.\n")

print("Open notes.txt for read and read file into a string")
with open("notes.txt", "r") as f:   # the "r" is default and not needed
   content = f.read()               # reads the whole file as one string
print(content)
print()

print("Open notes.txt for read, read and print one line at a time stripping of \n")
with open("notes.txt", "r") as f:
   for line in f:
      print(line.strip())     # .strip() removes the trailing \n
print()

print("Open notes.txt and read all lines into a list")
with open("notes.txt", "r") as f:
   lines = f.readlines()            #['Hell, Python\n', 'Second line.\n']
print(f"lines list - {lines}")
print()

print("Open missing.txt for read and use error handling")
try:
   with open("missing.txt", "r") as f:
      content = f.read()
except FileNotFoundError:
   print("That file doesn't exist.")
print()

print("Remove the file notes.txt.")
if os.path.exists("notes.txt"):
   os.remove("notes.txt")
   print("notes.txt removed")
else:
   print("Noting to delete")
  

