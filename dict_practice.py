scores = {"Alice": 85, "Bob": 72, "Charlie": 91}

# Add a new person
scores["Diana"] = 68

# Update an existing score
scores["Bob"] = 75

# Loop through and classify pass/fail
for name, score in scores.items():
   if score >= 80:
      print(f"{name}:  Pass ({score})")
   else:
      print(f"{name}:  Fail ({score})")

# Safe lookup for someone not in the dict
print(scores.get("Eve", "Not found"))


