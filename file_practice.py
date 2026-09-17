# Write some scores to a file
with open("scores.txt", "w") as f:
    f.write("Alice,85\n")
    f.write("Bob,72\n")
    f.write("Charlie,91\n")

# Read them back and parse each line
with open("scores.txt", "r") as f:
    for line in f:
        print(f"line - {line}")
        name, score = line.strip().split(",")   # strip /n and split at ,
        print(f"{name}: {score}")

# Try opening a file that doesn't exist
try:
    with open("nofile.txt", "r") as f:
        f.read()
except FileNotFoundError:
    print("nofile.txt doesn't exist yet.")
